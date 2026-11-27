
"""
Defines the structured output for research verification and analysis.
"""

from pydantic import BaseModel, Field


class SourceAssessment(BaseModel):
    title: str
    url: str
    credibility: str
    relevance: str
    assessment: str


class VerifiedClaim(BaseModel):
    claim: str
    verification_status: str
    evidence: str
    source_urls: list[str] = Field(default_factory=list)


class Contradiction(BaseModel):
    description: str
    conflicting_claims: list[str] = Field(default_factory=list)
    source_urls: list[str] = Field(default_factory=list)
    resolution: str


class ResearchGap(BaseModel):
    topic: str
    description: str
    importance: str
    recommended_follow_up: str


class VerificationAnalysis(BaseModel):
    research_objective: str
    executive_summary: str
    source_assessments: list[SourceAssessment]
    verified_claims: list[VerifiedClaim]
    contradictions: list[Contradiction] = Field(default_factory=list)
    research_gaps: list[ResearchGap] = Field(default_factory=list)
    limitations: list[str] = Field(default_factory=list)
    overall_assessment: str
