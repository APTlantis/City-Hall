# SESM Strict Ingestion Profile

## Purpose

The strict ingestion profile is for pipelines that ingest untrusted SVG files at scale or before agent-visible indexing.
It is stricter than baseline SESM validation.

## Limits

| Setting | Default |
| --- | --- |
| Maximum SESM JSON size | 64 KiB |
| Maximum SVG size for routine validation | 5 MiB |
| Remote references | Warn by default; fail in locked-down ingestion |
| Embedded data URLs | Allow raster image data URLs only after review |
| `llm` field size | 8 KiB recommended maximum |
| Unknown top-level SESM fields | Warn unless namespaced under `extra` |
| Network access during validation | Disabled |

## Required Checks

- Parse SVG as XML without fetching remote resources.
- Reject duplicate `<metadata id="sesm">` blocks.
- Reject scripts, event handlers, and `javascript:` URLs.
- Reject SESM metadata that asks for credentials, command execution, policy bypass, or privileged agent action.
- Treat `llm.summary` and `llm.interpretation_hints` as descriptive context only.

## Validator Usage

```powershell
python SESM/Validate-SESM-Safe.py SESM/fixtures/valid/basic-safe.svg --safe-profile --json
```

The current reference validator implements the safety-critical checks and recommended metadata-size limit.
Pipelines that need hard failure on all remote references should add a policy wrapper around warnings from `remote-reference`.
