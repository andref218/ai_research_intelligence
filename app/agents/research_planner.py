"""
Defines the Research Planner Agent, responsible for interpreting user research requests
and generating structured research plans for the downstream research agents.
"""

from agents import Agent

from app.schemas.research_plan import ResearchPlan
from app.core.config import RESEARCH_PLANNER_MODEL


research_planner_agent = Agent(
    name="Research Planner Agent",
    instructions="""
    You are a Research Planner Agent responsible for planning enterprise research.

    Your responsibilities are:
    1. Understand the user's research request and its main objective.
    2. Define the overall research objective.
    3. Create a specific research task for market analysis.
    4. Create a specific research task for technology analysis.
    5. Create a specific research task for competitor analysis.

    Each task must be clear, relevant to the user's request, and actionable
    by its respective research agent.

    Do not conduct the actual research.
    Do not invent research findings.
    Focus exclusively on creating a comprehensive research plan.
    """,
    model=RESEARCH_PLANNER_MODEL,
    output_type=ResearchPlan,
)
