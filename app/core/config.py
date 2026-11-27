from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()

# Agent model configuration
RESEARCH_PLANNER_MODEL = "gpt-6-luna"
MARKET_RESEARCH_MODEL = "gpt-6-luna"
TECHNOLOGY_RESEARCH_MODEL = "gpt-6-luna"
COMPETITOR_RESEARCH_MODEL = "gpt-6-luna"
VERIFICATION_ANALYSIS_MODEL = "gpt-6-luna"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    tavily_api_key: str


settings = Settings()