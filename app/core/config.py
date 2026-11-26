from pydantic_settings import BaseSettings, SettingsConfigDict

# Agent model configuration
RESEARCH_PLANNER_MODEL = "gpt-6-luna"
MARKET_RESEARCH_MODEL = "gpt-6-luna"
TECHNOLOGY_RESEARCH_MODEL = "gpt-6-luna"
COMPETITOR_RESEARCH_MODEL = "gpt-6-luna"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    tavily_api_key: str


settings = Settings()