
"""
Inspects the tools available on the Hugging Face MCP server.
"""

import asyncio
from pprint import pprint

from agents.mcp import MCPServerStreamableHttp


async def main():
    async with MCPServerStreamableHttp(
        name="Hugging Face MCP Server",
        params={
            "url": "https://huggingface.co/mcp",
            "timeout": 30,
        },
    ) as server:

        tools = await server.list_tools()

        print("\nHugging Face MCP Available Tools:\n")

        for tool in tools:
            print(f"\nTool: {tool.name}")
            print(f"Description: {tool.description}")
            print("Input Schema:")
            pprint(tool.input_schema)
            print("-" * 80)


if __name__ == "__main__":
    asyncio.run(main())
