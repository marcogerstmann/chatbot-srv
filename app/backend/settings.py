from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)

    openai_api_key: str
    google_drive_vector_sources_ava_folder_id: str
    postgres_connection_string: str
    admin_api_key: str


@lru_cache
def get_settings():
    return Settings()
