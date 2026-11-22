# OpenNotebookAgent

Retired. This extension no longer calls an open-notebook server and only reports that it is retired. Remove it.

Current version: **0.2.0**

> **Retired.** OpenNotebookAgent was retired on 2026-11-22 and no longer calls any service. Why: Biorouter's built-in Knowledge extension now holds notes and sources. Use instead: Use the built-in Knowledge extension.

This is the final release of a retired Biorouter extension. It replaces every
earlier tool with one, `opennotebook_status`, which shows the notice above. It holds no
credentials, reads no setting and calls no service. Remove the extension in
Biorouter once you no longer need the notice.

## Tools

- `opennotebook_status`: shows why OpenNotebookAgent was retired and what to use instead. It calls no service.

## Bundled skills

Every skill an earlier release bundled is kept, and each now says where its content
moved. An update never deletes a file an earlier version installed, so keeping the
paths is what replaces the old instructions.

## Develop and release

```bash
uv sync
uv run python -m unittest discover -s tests -v
uv run python scripts/build_brxt.py
```

Do not edit `src/opennotebookagent/_kit/` or `tests/kit_testing/`: they are vendored from the BRXT
adapter kit in the Biorouter repository (`scripts/brxt-adapter-kit/`).

## License

Apache-2.0. See `LICENSE` and `NOTICE`.
