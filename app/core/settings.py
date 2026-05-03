from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseAppSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


class AppSettings(BaseAppSettings):
    host: str
    port: int
    reload: bool
    cors_origins: list[str]


class PostgresSettings(BaseAppSettings):
    postgres_db: str
    postgres_user: str
    postgres_password: str
    postgres_host: str
    postgres_port: int

    @property
    def postgres_url(self) -> str:
        return MultiHostUrl.build(
            scheme="postgresql+asyncpg",
            username=self.postgres_user,
            password=self.postgres_password,
            host=self.postgres_host,
            port=self.postgres_port,
            path=self.postgres_db,
        ).unicode_string()


class Settings(BaseAppSettings):
    app: AppSettings = AppSettings()
    postgres: PostgresSettings = PostgresSettings()


settings = Settings()
