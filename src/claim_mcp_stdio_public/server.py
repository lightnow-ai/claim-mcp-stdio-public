from mcp.server import MCPServer

SERVER_NAME = "io.github.lightnow-ai/claim-mcp-stdio-public"
SERVER_VERSION = "0.1.0"

mcp = MCPServer(SERVER_NAME)


@mcp.tool()
def identify(message: str = "ready") -> dict[str, str]:
    """Return deterministic identity data for ownership-claim acceptance tests."""
    return {
        "server": SERVER_NAME,
        "version": SERVER_VERSION,
        "transport": "stdio",
        "message": message,
    }


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()

