# PPS CI Usage

## Purpose

Use PPS checks to keep proposal manifests complete enough for review before project creation, revival, or scope expansion.

## Local Checks

```powershell
python PPS/tools/pps_validate.py PPS/templates/PROJECT.manifest.toml --json
python PPS/tools/pps_new.py ExampleTool --type cli --dry-run
```

## JSONL Export

Proposal metadata can be exported as one JSON object per proposal:

```json
{"schema_version":"pps.proposal.v1","proposal_id":"manifest-audit","status":"ready","readiness":"approved-for-build","project_name":"Manifest Audit","project_type":"cli","delivery_standard":"CTS"}
```

Recommended fields are documented in `Proposal-Metadata-JSONL.md`.
