#!/usr/bin/env python3
import asyncio
import os
import re
import subprocess
import sys
import tempfile
from datetime import datetime
from http.client import HTTPException
from pathlib import Path
from typing import Callable, Any

import aiofiles
import aiohttp
from shutil import unpack_archive
from packaging.version import Version
from loguru import logger
from pydantic import BaseModel

ARCHIVE_CONTENT_TYPES = ["application/zip", "application/x-gtar", "application/x-gzip", "application/x-zip-compressed"]

# noinspection PyTypeChecker
session: aiohttp.ClientSession = None

BASE_REPO_URL = "https://api.github.com/repos"

MODULE_DIR = Path(__file__).resolve().parent
INSTALL_DIR = MODULE_DIR

logger.configure(handlers=[dict(sink=sys.stdout, level="WARNING")])


class Item(BaseModel):
    id: int
    url: str
    created_at: datetime


class Asset(Item):
    name: str
    label: str | None = None
    content_type: str
    browser_download_url: str
    content_type: str
    updated_at: datetime


class Release(Item):
    tag_name: str
    body: str
    prerelease: bool
    tarball_url: str | None = None
    zipball_url: str | None = None
    published_at: datetime
    assets: list[Asset]


class TooManyRequests(HTTPException):
    pass


class NotFound(HTTPException):
    pass


async def get_release(
        session_: aiohttp.ClientSession,
        releases_url: str,
        prerelease: bool = False,
) -> Release:
    """

    :raises TooManyRequests: if the rate limit is exceeded
    """
    url = releases_url + "?per_page=1" if prerelease else "/latest"
    async with session_.get(url) as resp:
        data = await resp.json()

    if resp.status in [403, 429]:
        raise TooManyRequests("Got rate limited, x-ratelimit-reset=" + resp.headers["x-ratelimit-reset"])

    if resp.status == 404:
        raise NotFound("Repository was not found.")

    if prerelease:
        data = data[0]

    return Release.model_validate(data)


def _use_filters(asset: Asset, filters: dict[str, Callable[[Any], bool]]) -> bool:
    dumped = asset.model_dump()
    for field_name, filter_ in filters.items():
        if field_name not in dumped.keys():
            logger.warning(f"Key {field_name} doesn't exist on the asset with id {asset.id}")
            return False

        if not filter_(dumped[field_name]):
            return False

    return True


def filter_assets(
    assets: list[Asset], *,
    pattern: re.Pattern | str,
    **filters
) -> list[Asset]:
    result = []
    for asset in assets:
        if not re.match(pattern, asset.name):
            continue

        if not _use_filters(asset, filters):
            continue

        result.append(asset)

    return result


async def download_asset(
    session_: aiohttp.ClientSession,
    download_url: str,
    download_path: Path
):
    chunk_size = 4096

    async with session_.get(download_url) as resp:
        async with aiofiles.open(download_path, "wb") as f:
            async for data in resp.content.iter_chunked(chunk_size):
                # noinspection PyTypeChecker
                await f.write(data)


async def download_and_apply_archive(
    session_: aiohttp.ClientSession,
    filename: str,
    download_url: str
):
    tmpdir = tempfile.TemporaryDirectory(dir=INSTALL_DIR)
    path = Path(tmpdir.name)

    await download_asset(
        session_,
        download_url,
        path / filename
    )
    unpack_archive(path / filename, INSTALL_DIR)

    tmpdir.cleanup()


def close_session(_):
    asyncio.create_task(session.close())


@logger.catch(onerror=close_session)
async def update(
    *,
    repository_name: str,
    current_version: str,
    prerelease: bool = False,
    asset_name_pattern: re.Pattern | str = r".*",
    requirements: str | Path = None,
    **asset_field_name_to_filter: Callable[[Any], bool]
) -> bool:
    """ Updates the application from the specified GitHub repository.

    :param repository_name: the name of repository in format {username}/{repo_name}
    :param current_version: the current version of the app
    :param prerelease: apply prerelease if available
    :param asset_name_pattern: regex pattern for the target asset's name
    :param requirements: if specified will install the requirements from the file specified
    :param asset_field_name_to_filter: Asset model field name to filter function for it
    :returns: False if already latest version
    :raises ValueError: if wrong repository name, if there are none, more than one asset
        and if the asset is not an archive
    :raises NotFound: if repo with repository_name was not found
    """
    global session  # make it possible to close the session in outer functions

    if not re.match(r"^.+/.+$", repository_name):
        raise ValueError("Incorrect repository name. Make sure it is in format {username}/{repo_name}")

    releases_url = BASE_REPO_URL + f"/{repository_name}" + "/releases"
    session = aiohttp.ClientSession()
    current_version = Version(current_version)

    INSTALL_DIR.mkdir(parents=True, exist_ok=True)

    try:
        release = await get_release(session, releases_url, prerelease=prerelease)
    except TooManyRequests:
        logger.info("Rate limit exceeded")
        return False
    except NotFound as e:
        logger.critical("Repository with name " + repository_name + " was not found")
        raise e

    if current_version == Version(release.tag_name):
        logger.info("Latest version is already installed.")
        await session.close()
        return False

    assets = filter_assets(
        release.assets,
        pattern=asset_name_pattern,
        **asset_field_name_to_filter
    )

    if not assets:
        raise ValueError("No assets were found for the given parameters.")
    elif len(assets) > 1:
        raise ValueError("Multiple assets found for the given parameters.")
    else:
        asset = assets[0]

    if asset.content_type not in ARCHIVE_CONTENT_TYPES:
        raise ValueError(asset.content_type + " is not a known archive type.")

    await download_and_apply_archive(
        session,
        asset.name,
        asset.browser_download_url
    )

    await session.close()

    if requirements:
        subprocess.check_call(
            ["pip", "install", "-r", requirements],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT
        )

    os.execv(sys.executable, sys.argv)  # restart application
