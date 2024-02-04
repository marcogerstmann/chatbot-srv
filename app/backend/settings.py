from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False
    )

    openai_api_key: str
    pinecone_api_key: str
    pinecone_env_name: str
    pinecone_index_name: str


settings = Settings()
