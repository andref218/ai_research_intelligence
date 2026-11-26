"""
Defines the structured output for competitor research findings.
"""

from pydantic import BaseModel, Field


class CompetitorSource(BaseModel):
    title: str
    url: str
    relevance: str


class CompetitorFinding(BaseModel):
    name: str
    description: str
    website: str
    products_and_services: list[str] = Field(default_factory=list)
    target_audience: list[str] = Field(default_factory=list)
    market_positioning: str
    strengths: list[str] = Field(default_factory=list)
    weaknesses: list[str] = Field(default_factory=list)
    competitive_advantages: list[str] = Field(default_factory=list)
    source_urls: list[str] = Field(default_factory=list)


class CompetitorFindings(BaseModel):
    research_objective: str
    executive_summary: str
    competitors: list[CompetitorFinding]
    market_competitive_trends: list[str] = Field(default_factory=list)
    sources: list[CompetitorSource]
    limitations: list[str] = Field(default_factory=list)