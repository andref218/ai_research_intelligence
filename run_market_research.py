"""
Manually executes the Market Research Agent.
Used for development and testing purposes.
"""

import asyncio
import json

from agents import Runner

from app.agents.market_researcher import market_research_agent
from app.tools.mcp.tavily import tavily_mcp_server


async def main():
    research_task = """
    Analyze AI adoption among SMEs in the European Union.

    Identify:
    - The latest adoption trends.
    - Differences between small, medium and large enterprises.
    - Main barriers to adoption.
    - Two relevant market opportunities.
    """

    async with tavily_mcp_server:
        result = await Runner.run(
            market_research_agent,
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