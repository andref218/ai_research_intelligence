"""
Defines the structured output for research findings.
"""

from pydantic import BaseModel, Field


class ResearchSource(BaseModel):
    title: str
    url: str
    relevance: str


class ResearchFinding(BaseModel):
    topic: str
    finding: str
    evidence: str
    source_urls: list[str] = Field(default_factory=list)


class ResearchFindings(BaseModel):
    research_objective: str
    executive_summary: str
    findings: list[ResearchFinding]
    sources: list[ResearchSource]
    limitations: list[str] = Field(default_factory=list)