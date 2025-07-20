from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math MCP Server(stdio)")

@mcp.tool(
    name="add",
    description="求两个整数之和"
)
def add(a : int, b : int):
    return a + b

# uv run
if __name__ == "__main__":
    mcp.run(transport="stdio")