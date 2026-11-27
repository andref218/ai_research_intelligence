
"""
Manually executes the Verification & Analysis Agent.
Used for development and testing purposes.
"""

import asyncio
import json

from agents import Runner

from app.agents.verification_analyst import verification_analysis_agent
from app.tools.mcp.tavily import tavily_mcp_server


async def main():
    research_input = """
    Research objective:
    Assess the adoption of AI technologies among European SMEs.

    Research findings from the Market Research Agent:
    - AI adoption among European SMEs is increasing.
    - Smaller businesses face financial and technical barriers.
    - Access to skilled employees remains a significant challenge.

    Research findings from the Technology Research Agent:
    - RAG is an established implementation pattern for enterprise AI.
    - AI agents are becoming increasingly relevant for business automation.
    - Smaller open-weight models offer additional deployment options.

    Research findings from the Competitor Research Agent:
    - Microsoft, AWS and Google Cloud offer enterprise AI platforms.
    - OpenAI and IBM provide AI solutions for enterprise customers.
    - Salesforce and ServiceNow integrate AI into business workflows.

    Your task is to critically evaluate these findings.

    Identify:
    - Claims requiring additional verification.
    - Potential contradictions or inconsistencies.
    - Missing evidence and research gaps.
    - Source credibility issues.
    - Overall research reliability.

    Do not assume that the supplied findings are verified facts.
    """
    
    async with tavily_mcp_server:
        result = await Runner.run(
            verification_analysis_agent,
            research_input,
            max_turns=8,
        )

        print(json.dumps(
            result.final_output.model_dump(),
            indent=4,
            ensure_ascii=False,
        ))


if __name__ == "__main__":
    asyncio.run(main())
