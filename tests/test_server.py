import sys

import pytest
from mcp import Client
from mcp.client.stdio import StdioServerParameters

from claim_mcp_stdio_public.server import SERVER_NAME, SERVER_VERSION, mcp


@pytest.mark.anyio
async def test_identify_tool_in_process() -> None:
    async with Client(mcp) as client:
        result = await client.call_tool("identify", {"message": "in-process"})

    assert result.structured_content == {
        "server": SERVER_NAME,
        "version": SERVER_VERSION,
        "transport": "stdio",
        "message": "in-process",
    }


@pytest.mark.anyio
async def test_identify_tool_over_stdio() -> None:
    parameters = StdioServerParameters(
        command=sys.executable,
        args=["-m", "claim_mcp_stdio_public.server"],
    )

    async with Client(parameters) as client:
        result = await client.call_tool("identify", {"message": "transport-smoke"})

    assert result.structured_content == {
        "server": SERVER_NAME,
        "version": SERVER_VERSION,
        "transport": "stdio",
        "message": "transport-smoke",
    }

