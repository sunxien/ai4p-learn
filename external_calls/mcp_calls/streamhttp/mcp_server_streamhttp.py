import uvicorn

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math MCP Server(streamable-http)")

@mcp.tool(
    name="add",
    description="求两个整数之和"
)
def add(a : int, b : int):
    return a + b

# uv run mcp_server_streamhttp.py
# endpoint: http://127.0.0.1:8088/mcp
if __name__ == "__main__":
    # mcp.run(transport="streamable-http")
    uvicorn.run(mcp.streamable_http_app, host="127.0.0.1", port=8088)