from typing import List
from pydantic_settings import BaseSettings  # Import BaseSettings from pydantic_settings
from pydantic import AnyHttpUrl
from pathlib import Path


class Settings(BaseSettings):
    # Redis settings
    REDIS_PORT: int
    REDIS_HOST: str

    @property
    def REDIS_URL(self) -> str:
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}/0"

    # Security settings
    SECRET_KEY: str
    ALGORITHM: str
    PROJECT_NAME: str
    CORS_ORIGINS: List[
        AnyHttpUrl
    ]  # Assuming CORS_ORIGINS is a comma-separated list of URLs
    DEBUG: bool

    # Domain settings
    DOMAIN: str

    # JWT settings
    ACCESS_TOKEN_EXPIRE_SECONDS: int

    # SMTP settings
    SMTP_USER: str
    SMTP_PASSWORD: str
    EMAILS_FROM_EMAIL: str
    SMTP_PORT: int
    SMTP_HOST: str
    EMAIL_FROM_NAME: str

    # PostgreSQL settings
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    BASE_DIR: Path = Path(__file__).resolve().parent
    ROOT_DIR: Path = Path(__file__).resolve().parent.parent

    class Config:
        case_sensitive = (
            True  # Ensures that environment variable names are case-sensitive
        )
        env_prefix = ""  # No prefix needed since you're passing variables directly


# Instantiate the settings
settings = Settings()
