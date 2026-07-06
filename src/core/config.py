import os

from dotenv import find_dotenv, load_dotenv
from pydantic_settings import BaseSettings

load_dotenv(dotenv_path=find_dotenv(".env"))

class DBSettings(BaseSettings):
    port: int = os.environ.get("PG_PORT")
    user: str = os.environ.get("PG_USER")
    password: str = os.environ.get("PG_PASS")
    name: str = os.environ.get("PG_NAME")
    host: str = os.environ.get("PG_HOST")

    @property
    def db_sync_url(self):
        return f'postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}'


    @property
    def db_async_url(self):
        return f'postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}'


class Settings(BaseSettings):
    db: DBSettings = DBSettings()


settings: Settings = Settings()