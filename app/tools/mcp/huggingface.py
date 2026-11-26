"""
Provides the connection configuration for the Hugging Face MCP server.
"""

from agents.mcp import (
    MCPServerStreamableHttp,
    create_static_tool_filter,
)


def create_huggingface_mcp_server() -> MCPServerStreamableHttp:
    return MCPServerStreamableHttp(
        name="Hugging Face MCP Server",
        params={
            "url": "https://huggingface.co/mcp",
            "timeout": 30,
        },
        cache_tools_list=True,
        tool_filter=create_static_tool_filter(
            allowed_tool_names=[
                "hub_repo_search",
                "hub_repo_details",
                "hf_fs",
            ],
        ),
    )


huggingface_mcp_server = create_huggingface_mcp_server()
