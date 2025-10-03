from functools import lru_cache
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseModel):
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "SelfStar Backend")
    VERSION: str = os.getenv("VERSION", "0.1.0")
    ENV: str = os.getenv("ENV", "dev")
    ALLOWED_ORIGINS: list[str] = [o.strip() for o in os.getenv("ALLOWED_ORIGINS", "*").split(",")]
    # Database
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: int = int(os.getenv("DB_PORT", "3306"))
    DB_USER: str = os.getenv("DB_USER", "root")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")
    DB_NAME: str = os.getenv("DB_NAME", "app")
    DB_ECHO: bool = os.getenv("DB_ECHO", "false").lower() == "true"

    @property
    def async_database_url(self) -> str:
        return (
            f"mysql+asyncmy://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
