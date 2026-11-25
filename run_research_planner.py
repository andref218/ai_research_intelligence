"""
Manually executes the Research Planner Agent using an example research request.
Used for development and testing purposes.
"""

import asyncio
import json

from agents import Runner

from app.agents.research_planner import research_planner_agent


async def main():
    # Example research request for testing the Research Planner Agent.
    user_request = """
    Analyze the European market for AI solutions targeting SMEs.
    Identify market opportunities, emerging technologies and
    the main competitors.
    """

    result = await Runner.run(
        research_planner_agent,
        user_request,
    )

    print(json.dumps(
    result.final_output.model_dump(),
    indent=4,
    ensure_ascii=False,
))


if __name__ == "__main__":
    asyncio.run(main())
