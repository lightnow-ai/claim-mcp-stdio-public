# claim-mcp-stdio-public

Public, minimal stdio MCP server for LightNow publisher acceptance tests.
Its single `identify` tool returns the fixture name, version, transport and supplied message. It does not call external services or contain credentials.

## Local development

```sh
python3 -m venv .venv
.venv/bin/pip install -e '.[test]'
.venv/bin/pytest
.venv/bin/claim-mcp-stdio-public
```

The server reads and writes the MCP protocol on standard input/output.

## Container

```sh
docker build -t claim-mcp-stdio-public:local .
docker run --rm -i claim-mcp-stdio-public:local
```

The image runs as UID/GID 10001. Jenkins tests the real MCP transport and publishes native amd64/arm64 images to `harbor.apitree.net/lightnow-ai/claim-mcp-stdio-public`. Acceptance manifests pin a verified immutable image digest.

## Test scope

This public repository covers catalog submission, ownership claim/publication and private owner copies. These journeys use separate manifest identities; private repository access is tested in the existing private sibling repositories. No repository history or credentials are copied from those repositories.
