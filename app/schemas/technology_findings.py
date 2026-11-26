"""
Defines the structured output for technology research findings.
"""

from pydantic import BaseModel, Field


class TechnologySource(BaseModel):
    title: str
    url: str
    relevance: str


class TechnologyFinding(BaseModel):
    technology: str
    description: str
    capabilities: list[str] = Field(default_factory=list)
    enterprise_applications: list[str] = Field(default_factory=list)
    maturity: str
    limitations: list[str] = Field(default_factory=list)
    infrastructure_requirements: list[str] = Field(default_factory=list)
    source_urls: list[str] = Field(default_factory=list)


class TechnologyFindings(BaseModel):
    research_objective: str
    executive_summary: str
    findings: list[TechnologyFinding]
    technology_trends: list[str] = Field(default_factory=list)
    sources: list[TechnologySource]
    limitations: list[str] = Field(default_factory=list)
