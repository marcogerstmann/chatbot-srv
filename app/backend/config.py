from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)

    openai_api_key: str
    google_cloud_api_key: str
    google_drive_base_vector_sources_folder_id: str
    postgres_connection_string: str


config = Config()
