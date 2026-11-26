"""
Provides the connection configuration for the Tavily MCP server.
"""

from agents.mcp import (
    MCPServerStreamableHttp,
    create_static_tool_filter,
)

from app.core.config import settings


def create_tavily_mcp_server() -> MCPServerStreamableHttp:
    """Creates a connection to the remote Tavily MCP server."""

    return MCPServerStreamableHttp(
        name="Tavily MCP Server",
        params={
            "url": "https://mcp.tavily.com/mcp/",
            "headers": {
                "Authorization": f"Bearer {settings.tavily_api_key}",
            },
            "timeout": 30,
        },
        cache_tools_list=True,
        tool_filter=create_static_tool_filter(
            allowed_tool_names=[
                "tavily_search",
                "tavily_extract",
            ],
        ),
    )

tavily_mcp_server = create_tavily_mcp_server()