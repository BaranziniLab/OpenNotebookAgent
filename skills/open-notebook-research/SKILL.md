---
name: open-notebook-research
description: Use OpenNotebookAgent when working with Open Notebook platform data, API resources, provenance, or reproducibility checks from inside BioRouter.
license: Apache-2.0
user-invocable: false
---

# OpenNotebookAgent Skill

Use this extension to inspect open-notebook entries, timestamps, authorship, attachments, and provenance without overwriting notebook records.

## Operating rules

- Start with `get_opennotebookagent_status` to confirm whether credentials and base URLs are configured.
- Use `get_opennotebookagent_request_plan` before any endpoint that may create, update, launch, upload, or delete a resource.
- Prefer read-only `GET` requests through `call_opennotebookagent_api` while exploring.
- Do not pass `allow_mutation=true` unless the user has explicitly approved the exact operation, target resource, and expected side effect.
- Preserve platform IDs, versions, owners/authors, timestamps, and URLs in any report.
- Never print API tokens, passwords, bearer headers, or session cookies.

## Useful starting endpoints

- `/entries`
- `/projects`
- `/search`
