from pydantic_settings import BaseSettings
from functools import lru_cache

class TokenSettings(BaseSettings):
    token: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "allow"
        case_sensitive = False


@lru_cache()
def get_envs():
    return TokenSettings()