from enum import Enum
from functools import lru_cache

from pydantic import BaseSettings, FilePath


class Scopes(str, Enum):
    SPREADSHEET_SCOPE = "https://www.googleapis.com/auth/spreadsheets"


class Settings(BaseSettings):
    JSON_PATH: FilePath

    class Config:
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    return Settings()
