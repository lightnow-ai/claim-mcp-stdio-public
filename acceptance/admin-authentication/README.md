# Public metadata for local Admin STDIO authentication intake

Verified definition source: **2026-11-16**. These six secret-free `server.json`
files are byte-identical copies from the private implementation repository
[`lightnow-ai/claim-mcp-stdio`](https://github.com/lightnow-ai/claim-mcp-stdio),
commit `c2f3015a24998ef36275bcfb160f162a45b98467`, at the same subfolder paths.
Only public start definitions are mirrored; no private implementation, history,
credentials or captured scan results are copied.

The manifests retain the actual private `repository.url` and
`repository.subfolder`. This public repository supplies the metadata intake
source, which the normal SYSTEM import records separately. The public
repository's own anonymous `identify` server is unchanged.

All definitions select version `0.1.1` and the genuine amd64/arm64 image from
[Jenkins PR-3 build 3](https://jenkins.apitree.net/job/lightnow-ai/job/claim-mcp-stdio/job/PR-3/3/),
source `4abacff4952f65acfcc5f9992fd0d4fb5851c499`:
`harbor.apitree.net/lightnow-ai/claim-mcp-stdio@sha256:bb53c78c4424b26eb0456841604e1c14577003769448d02f2a8aae3dc47b61d1`.
The image owns `/app/auth-provider.json` as root:root 0444. Save only the
selected credential environment input through ordinary Admin Version Operations;
no client `runtimeFiles` are needed. Then use its separate manual scan control.

Use the reviewed public commit SHA as `<ref>` in normal Admin repository intake:

```text
https://github.com/lightnow-ai/claim-mcp-stdio-public/tree/<ref>/acceptance/admin-authentication/api-key
https://github.com/lightnow-ai/claim-mcp-stdio-public/tree/<ref>/acceptance/admin-authentication/pat
https://github.com/lightnow-ai/claim-mcp-stdio-public/tree/<ref>/acceptance/admin-authentication/generic
https://github.com/lightnow-ai/claim-mcp-stdio-public/tree/<ref>/acceptance/admin-authentication/oauth
https://github.com/lightnow-ai/claim-mcp-stdio-public/tree/<ref>/acceptance/admin-authentication/oauth2
https://github.com/lightnow-ai/claim-mcp-stdio-public/tree/<ref>/acceptance/admin-authentication/oidc
```

These definitions preload no credentials, capabilities, authentication results
or admission exceptions. The private fixture's direct protocol checks retain all
four complete lists, hash
`04b8700c95fd7967f94de07cead506d363858bbbe8b27a58bf09718369571119`;
this is not evidence of completed Admin configuration, storage or UI acceptance.
Those native journeys must be verified separately.

## Definition integrity

SHA-256 of each `server.json`, identical to the private source commit above:

| Profile | SHA-256 |
| --- | --- |
| `api-key` | `7237b7622c1e3f99161b7b0083fb9ccab86aa1f05e8366d7560c6a7a04551c84` |
| `pat` | `e3da8349046784901c4293ceb2e0bd8cab2405a91067dfa3ef6a9300c222af80` |
| `generic` | `2ae887c925565fd3330b700389a381177259e10ca52af4e9bba7d7f4b6670283` |
| `oauth` | `401b5475e6d59d2f031d0db960f549d54610e920698b56b3beb07cbba595a18e` |
| `oauth2` | `922daedbaaae17bb99a669b1cb8070057b97be8cf932757d0eb7133e16c36397` |
| `oidc` | `e41782bea430926047b45fd68b666e1303bdd6dfded5783f524a0643d521de2c` |
