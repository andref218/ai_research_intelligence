from pydantic_settings import BaseSettings, SettingsConfigDict

# Model used by the Research Planner Agent to generate structured research plans.
RESEARCH_PLANNER_MODEL = "gpt-6-luna"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    tavily_api_key: str


settings = Settings()