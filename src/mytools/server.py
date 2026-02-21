from mcp.server.fastmcp import FastMCP

# create an mcp server instance
server = FastMCP("AddServer")

# add tools
@server.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

# start the server (streamable HTTP transport)
if __name__ == "__main__":
    server.run(transport="streamable-http")
