import uvicorn
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math MCP Server(sse)")
# mcp = FastMCP("Math MCP Server(sse)", port=8088)

@mcp.tool(
    name="add",
    description="求两个整数之和"
)
def add(a : int, b : int):
    return a + b

#
# def create_starlette_app():
#     sse = SseServerTransport("/messages/")
#     async def handle_sse(request: Request):
#         async with sse.connect_sse(request.scope, request.receive, request._send) as (read_stream, write_stream):
#             await mcp.run_sse_async(read_stream, write_stream, mcp.create_initialization_options())
#     return Starlette(routes=[
#         Route("/sse", endpoint=handle_sse),
#         Mount("/messages/", app=sse.handle_post_message)
#     ])

# uv run mcp_server_sse.py
# endpoint: http://127.0.0.1:8087/sse
if __name__ == "__main__":
    # mcp.run(transport="sse")
    uvicorn.run(mcp.sse_app, host="127.0.0.1", port=8087)
