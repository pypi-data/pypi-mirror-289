import logging
import os

from jrsync.utils import timelib

logger = logging.getLogger("jrsync")


def can_sync_day(day: str) -> bool:
    return day == "*" or day == timelib.get_current_weekday()


def can_sync_file(f: str, src_address: str) -> bool:
    """
    Establish if a file can be synced or not.
    If f is a remote file, the check is skipped

    Args:
        f: Path to file
        src_address: Address of remote file

    Returns:
        True if file can be synced else False
    """
    if src_address is not None or os.path.exists(f):
        logger.debug(f"Cannot check if {f} exists on {src_address}")
        return True

    return False
