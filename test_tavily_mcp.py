import asyncio

from app.tools.mcp.tavily import create_tavily_mcp_server


async def main():
    server = create_tavily_mcp_server()

    async with server:
        tools = await server.list_tools()

        print("\nConnected to Tavily MCP Server!")
        print(f"\nAvailable tools: {len(tools)}")

        for tool in tools:
            print(f"\n- {tool.name}")
            print(f"  Description: {tool.description}")


if __name__ == "__main__":
    asyncio.run(main())