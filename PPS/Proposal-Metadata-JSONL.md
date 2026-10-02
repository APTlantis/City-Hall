# PPS Proposal Metadata JSONL

## Purpose

This format lets proposal records be indexed without parsing full Markdown proposals.

## Record Shape

```json
{
  "schema_version": "pps.proposal.v1",
  "proposal_id": "manifest-audit",
  "status": "ready",
  "readiness": "approved-for-build",
  "project_name": "Manifest Audit",
  "project_type": "cli",
  "mission": "Audit manifests for governed workspace drift.",
  "delivery_standard": "CTS",
  "created": "2026-07-30",
  "source": "PPS/examples/proposal-snapshots/Manifest-Audit-2026-07-30-ready.md"
}
```

## Vocabulary

| Field | Values |
| --- | --- |
| `status` | `sketch`, `draft`, `ready`, `approved`, `deferred`, `rejected`, `archived` |
| `readiness` | `sketch`, `ready-for-review`, `approved-for-build`, `blocked`, `deferred` |
| `delivery_standard` | `DRS`, `CTS`, `SIS`, `WDS`, `DDS`, `LDS`, or blank when undecided |

JSONL exports are indexing aids. The proposal document and proposal manifest remain authoritative.
