from datetime import datetime
from pathlib import Path
from typing import List

from pydantic import BaseModel, Field, field_validator
from pydantic_core.core_schema import ValidationInfo

import jrsync.conf as settings
from jrsync.utils import str_parser
from jrsync.utils import str_validator


class Jsync(BaseModel):
    date_to_sync: datetime
    src_address: str = Field(None)
    dst_address: str = Field(None)
    source_dir: Path
    dest_dir: Path
    file_to_sync: List[str] | str = Field(settings.ALL_DIRECTORY)
    day: str = Field("*")

    @field_validator("src_address", "dst_address", mode="before")
    @classmethod
    def check_address(cls, v):
        if not str_validator.is_valid_address(v):
            raise ValueError(f"Invalid address: {v}")

    @field_validator("source_dir", "dest_dir", mode="before")
    @classmethod
    def resolve_path(cls, v: str, info: ValidationInfo) -> Path:
        """Replace placeholders and global variables"""
        resolved_str_path = str_parser.resolve_str(v, info.data["date_to_sync"])
        return Path(resolved_str_path)

    @field_validator("file_to_sync", mode="before")
    @classmethod
    def resolve_filenames(cls, v: str, info: ValidationInfo) -> List[str]:
        """Replace placeholders and global variables"""
        date = info.data["date_to_sync"]
        return [str_parser.resolve_str(f, date) for f in v]
