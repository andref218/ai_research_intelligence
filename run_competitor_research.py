"""
Manually executes the Competitor Research Agent.
Used for development and testing purposes.
"""

import asyncio
import json

from agents import Runner

from app.agents.competitor_researcher import competitor_research_agent
from app.tools.mcp.tavily import tavily_mcp_server


async def main():
    research_task = """
    Analyze the competitive landscape of AI solutions
    for enterprise adoption.

    Identify:
    - Relevant direct and indirect competitors.
    - Their main products and services.
    - Their target audiences and market positioning.
    - Their main strengths and weaknesses.
    - Their competitive advantages.
    - Relevant competitive trends.
    """

    async with tavily_mcp_server:
        result = await Runner.run(
            competitor_research_agent,
            research_task,
            max_turns=4,
        )

        print(json.dumps(
            result.final_output.model_dump(),
            indent=4,
            ensure_ascii=False,
        ))


if __name__ == "__main__":
    asyncio.run(main())