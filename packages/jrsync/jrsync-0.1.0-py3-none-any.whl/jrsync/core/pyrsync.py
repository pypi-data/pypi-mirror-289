import logging
import subprocess
from pathlib import Path
from typing import List

import jrsync.conf as settings
from jrsync.core.sync_permission import can_sync_file, can_sync_day
from jrsync.model import Jsync

DEFAULT_RSYNC_OPTS = "-aP"
logger = logging.getLogger("jrsync")


def build_sync_path(path: Path, addresses: List[str]) -> str:
    """
    Return path to pass to rsync attaching the first valid remote address in addresses
    Args:
        path: Path to sync
        addresses: List of addresses in priority order.

    Returns:
        address:path if addresses contains at least one address not None, path otherwise
    """
    for address in addresses:
        if address is not None:
            return f"{address}:{path.as_posix()}"

    return path.as_posix()


def rsync(
    js: Jsync,
    src_address: str = None,
    dst_address: str = None,
    **kwargs,
) -> None:
    if not can_sync_day(js.day):
        logger.info(f"Skipping {js}")
        return

    # build  rsync parameters
    src_path = build_sync_path(js.source_dir, [src_address, js.src_address])
    dst_path = build_sync_path(js.dest_dir, [dst_address, js.dst_address])
    files_to_sync = js.file_to_sync

    if files_to_sync == settings.ALL_DIRECTORY:
        rsync_args = [[f"{src_path}/", f"{dst_path}"]]
    else:
        rsync_args = [
            [f"{src_path}/{f}", f"{dst_path}"]
            for f in files_to_sync
            if can_sync_file(f, dst_address)
        ]

    for args in rsync_args:
        wrapper_rsync(*args, **kwargs)


def wrapper_rsync(
    src: str, dst: str, options: str = None, dry_run: bool = False
) -> None:
    if options is None:
        options = DEFAULT_RSYNC_OPTS

    # Base rsync command
    command = ["rsync", options, src, dst]

    try:
        # Run the rsync command
        str_command = [str(c) for c in command]
        logger.info(f"Running: {' '.join(str_command)}")
        if dry_run:
            command = ["echo", *command]
        subprocess.run(command, check=True)

    except subprocess.CalledProcessError as e:
        # Handle errors in rsync command execution
        print("Error during rsync execution.")
        print("Return code:", e.returncode)
        print("Output:", e.output)
        print("Errors:", e.stderr)
    except Exception as e:
        # Handle other exceptions
        print("An unexpected error occurred:", str(e))
