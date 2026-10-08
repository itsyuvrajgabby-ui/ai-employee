from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "AI Employee"
    environment: str = "development"

    openai_api_key: str
    ai_model: str = "gpt-5.6-mini"

    database_url: str = "sqlite:///./ai_employee.db"

    max_message_length: int = 10000

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
    )


settings = Settings()
