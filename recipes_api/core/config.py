from pathlib import Path
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent


class Settings(BaseSettings):
    db_url: str = "sqlite+aiosqlite:///./db_sqlite3"
    db_echo: bool = True


settings = Settings()

