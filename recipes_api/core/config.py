from pathlib import Path
from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings
import os

BASE_DIR = Path(__file__).parent


class AccessToken(BaseModel):
    lifetime_seconds: int = 3600
    reset_password_token_secret: str = "006bbfd0611f21be911656b8982071ad72d53312247448d14bdaa12a4ac4bc88"
    verification_token_secret: str = "9a97b965dd2f61f0007c18fb7c7a77b915d5d2e779e96581e9d57c8c50e453ff"


class DatabaseSettings(BaseModel):
    user: str = os.getenv('DB_USER')
    password: str = os.getenv('DB_PASSWORD')
    db: str = os.getenv('DB_NAME')
    host: str = os.getenv('DB_HOST')
    port: str = os.getenv('DB_PORT')
    echo: bool = True

    @property
    def url(self):
        # return "postgresql+asyncpg://postgres:postgres@localhost:5432/recipes"
        return "postgresql+asyncpg://" + self.user + ":" + self.password + "@" + \
                self.host + ":" + self.port + "/" + self.db



class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    origins: list[str] = ["http://localhost:5173", "http://127.0.0.1:5173"]
    db_settings: DatabaseSettings = DatabaseSettings()
    access_token: AccessToken = AccessToken()


settings = Settings()

