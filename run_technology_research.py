"""
Manually executes the Technology Research Agent.
Used for development and testing purposes.
"""

import asyncio
import json

from agents import Runner

from app.agents.technology_researcher import technology_research_agent
from app.tools.mcp.tavily import tavily_mcp_server
from app.tools.mcp.huggingface import huggingface_mcp_server


async def main():
    research_task = """
    Analyze the current landscape of AI technologies
    relevant to enterprise adoption.

    Identify:
    - Emerging AI technologies and their capabilities.
    - Practical enterprise applications and use cases.
    - Technology maturity and production readiness.
    - Technical limitations and infrastructure requirements.
    - Relevant technological trends.
    """

    async with tavily_mcp_server, huggingface_mcp_server:
        result = await Runner.run(
            technology_research_agent,
            research_task,
            max_turns=8,
        )

        print(json.dumps(
            result.final_output.model_dump(),
            indent=4,
            ensure_ascii=False,
        ))


if __name__ == "__main__":
    asyncio.run(main())