# OpenNotebookAgent

MCP adapter for self-hosted or lab-hosted open-notebook systems, exposing guarded notebook entry search, retrieval, and provenance checks.

This repository follows the BioRouter `.brxt` extension convention used by `SPOKEAgent` and `UCSFOMOPAgent`: a root `manifest.json`, Python package under `src/`, and optional bundled skills under `skills/`.

## Tools

- `get_opennotebookagent_status`: report configured environment variables without revealing secrets.
- `get_opennotebookagent_request_plan`: explain whether an API request is read-only or requires explicit mutation approval.
- `call_opennotebookagent_api`: call a platform API endpoint with write methods blocked unless `allow_mutation=true`.
- `summarize_opennotebookagent_resource`: summarize a JSON export or API payload without making a network call.

## Configuration

| Variable | Required | Secret | Purpose |
|---|---:|---:|---|
| `OPEN_NOTEBOOK_BASE_URL` | true | false | Open notebook API base URL |
| `OPEN_NOTEBOOK_TOKEN` | false | true | Open notebook bearer token if required |
| `OPEN_NOTEBOOK_LOG_LEVEL` | false | false | Logging level |


## Build

```bash
uv sync
scripts/build_brxt.sh
```

The bundle is written to `dist/opennotebookagent.brxt`.

## Install in BioRouter

```bash
biorouter extension install dist/opennotebookagent.brxt
```

Add the required secrets with `--secret KEY=value` or configure them in the BioRouter UI.

## License

Apache-2.0. See `LICENSE`.
