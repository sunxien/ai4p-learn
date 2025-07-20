from mcp.server.fastmcp import FastMCP

mcp = FastMCP("My First MCP Server", version="1.0.0")

# MCP Tool
@mcp.tool(
    name="add",
    description="对两个整数求和"
)
def add(a : int, b : int):
    return  a + b

# MCP Resource
@mcp.resource(
    uri="greeting://{name}",
    name="greeting",
    description="问候输入的名字"
)
def greeting(name: str):
    return f"Hello, {name}!"

# MCP Prompt
@mcp.prompt(
    name="translate",
    description="进行翻译的提示prompt"
)
def translate(content: str):
    return f"请将下面的内容翻译成中文：\n\n{content}"


# MCP: https://mcp-docs.cn/docs/concepts/resources#python
# OpenMCP: https://kirigaya.cn/openmcp/zh/plugin-tutorial/quick-start/first-mcp.html
# 1. uv run mcp run mymcp_server.py
# 2. append code snippets like below and `uv run mymcp_server.py`
if __name__ == "__main__":
    mcp.run()