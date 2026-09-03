from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Object-Oriented Consciousness"
    log_level: str = "DEBUG"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
