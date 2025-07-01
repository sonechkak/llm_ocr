from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    """
    Настройки приложения.
    """
    TITLE : str = "LLM bot for files"
    VERSION : str = "1.0.0"
    DEBUG : bool = False
    SECRET_KEY : str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"

    model_config = SettingsConfigDict(
        env_file="../../.env",
        case_sensitive=True,
        extra="ignore"
    )

settings = AppSettings()
