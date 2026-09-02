# Workspace Audit Dashboard Specification

## Purpose

This specification defines the minimum machine-readable data shape for WGS workspace audit dashboards.
It turns manifest truth, inventory output, and audit findings into records that can be stored, compared, queried, and rendered without relying on prose-only reports.

The first implementation target is a local-first dataset generated from `tools/city_hall_audit.py` and `tools/workspace_inventory.py`.

## Scope

This spec covers:

- Workspace inventory records.
- Manifest coverage records.
- Audit finding records.
- Standard-suite coverage records.
- Run metadata for repeatable snapshots.

This spec does not require a dashboard front end, scheduled automation, CI integration, or a database engine in the first implementation. Those remain later backlog items.

## Output Formats

The first supported output format should be JSONL because it is easy to append, diff, inspect, and load into DuckDB or SQLite.

Generate structured records locally with:

```powershell
python WGS/tools/workspace_inventory.py --workspace-root D:/ --format jsonl
python WGS/tools/city_hall_audit.py --root D:/.city_hall --format jsonl
```

Recommended files for a single audit run:

| File | Grain | Producer |
| --- | --- | --- |
| `audit-run.json` | One record per run | audit wrapper or dashboard generator |
| `workspace-entities.jsonl` | One record per discovered entity | `workspace_inventory.py` |
| `manifest-coverage.jsonl` | One record per expected or discovered manifest | `workspace_inventory.py` |
| `audit-findings.jsonl` | One record per finding | `city_hall_audit.py` |
| `standard-suite-coverage.jsonl` | One record per standard suite | `city_hall_audit.py` |

## Common Fields

All JSONL records should include:

| Field | Type | Required | Notes |
| --- | --- | --- | --- |
| `schema_version` | string | yes | Start at `wgs.audit.v1`. |
| `run_id` | string | yes | Stable ID for one audit run, preferably timestamp-based. |
| `record_type` | string | yes | One of the record types below. |
| `workspace_root` | string | yes | Absolute path to the audited workspace root. |
| `path` | string | conditional | Absolute or workspace-relative path for the affected entity. |
| `generated_at` | string | yes | ISO 8601 timestamp. |

## Record Types

### Audit Run

`record_type`: `audit_run`

Required fields:

| Field | Type | Notes |
| --- | --- | --- |
| `tool_versions` | object | Tool names and versions or commit identifiers when available. |
| `inputs` | object | Root paths, manifest paths, and command options. |
| `summary` | object | Counts by severity, lifecycle, entity type, and standard. |
| `status` | string | `pass`, `warn`, `fail`, or `incomplete`. |

### Workspace Entity

`record_type`: `workspace_entity`

Required fields:

| Field | Type | Notes |
| --- | --- | --- |
| `entity_name` | string | Manifest entity name or derived directory name. |
| `entity_type` | string | Workspace, directory, project, standard, dataset, service, or other governed type. |
| `lifecycle` | string | Lifecycle value from manifest when available. |
| `governing_standards` | array | Standards declared or inferred for the entity. |
| `manifest_path` | string | Path to the entity manifest when present. |
| `readme_path` | string | Path to `README.md` or `Project-README.md` when present. |

### Manifest Coverage

`record_type`: `manifest_coverage`

Required fields:

| Field | Type | Notes |
| --- | --- | --- |
| `expected_manifest_path` | string | Expected canonical manifest path. |
| `actual_manifest_path` | string | Actual manifest path when found. |
| `coverage_status` | string | `present`, `missing`, `legacy_name`, `duplicate`, or `unexpected`. |
| `naming_status` | string | `canonical`, `legacy`, `unknown`, or `not_applicable`. |
| `parent_registered` | boolean | Whether the entity is registered by the expected parent. |

### Audit Finding

`record_type`: `audit_finding`

Required fields:

| Field | Type | Notes |
| --- | --- | --- |
| `finding_id` | string | Stable ID generated from rule ID and path. |
| `rule_id` | string | Machine-readable rule identifier. |
| `severity` | string | `info`, `warning`, `error`, or `blocker`. |
| `message` | string | Short human-readable finding. |
| `evidence` | object | Paths, values, or counts supporting the finding. |
| `recommended_action` | string | Concrete next action. |

### Standard Suite Coverage

`record_type`: `standard_suite_coverage`

Required fields:

| Field | Type | Notes |
| --- | --- | --- |
| `standard` | string | Standard short name. |
| `status` | string | Status from manifest or roadmap. |
| `maturity` | string | Maturity from manifest or roadmap. |
| `required_artifacts_present` | array | Required artifacts found. |
| `required_artifacts_missing` | array | Required artifacts not found. |
| `validators_registered` | array | Validator references found in manifest. |
| `examples_present` | array | Example artifacts found. |

## Metric Mapping

Initial dashboard metrics should be derived from the record types above:

| Metric | Source | Calculation |
| --- | --- | --- |
| Manifest coverage rate | `manifest_coverage` | present canonical manifests divided by expected manifests. |
| Legacy manifest count | `manifest_coverage` | count where `naming_status` is `legacy`. |
| Unregistered entity count | `manifest_coverage` | count where `parent_registered` is false. |
| Audit blockers | `audit_finding` | count where `severity` is `blocker`. |
| Audit errors | `audit_finding` | count where `severity` is `error`. |
| Standards with registered validators | `standard_suite_coverage` | count with non-empty `validators_registered`. |
| Standards missing required artifacts | `standard_suite_coverage` | count with non-empty `required_artifacts_missing`. |

## Manifest Field Mapping

Dashboard records should preserve the manifest fields that explain status and governance decisions, not only summary counts.

| Manifest field | Dashboard field or metric | Notes |
| --- | --- | --- |
| `manifest.canonical_name` | `manifest_coverage.naming_status` | Compare the declared canonical name to the expected entity-named manifest. |
| `manifest.manifest_type` | `workspace_entity.entity_type` | Use the manifest value when available; otherwise use a conservative derived type. |
| `standard.status` | `standard_suite_coverage.status` | Applies to standard suites. |
| `standard.maturity` | `standard_suite_coverage.maturity` | Applies to standard suites and maturity tracking. |
| `standard.version` | `standard_suite_coverage.version` | Optional v1 extension for release and changelog checks. |
| `entity.status` | `workspace_entity.lifecycle` | Use when project or directory manifests expose entity lifecycle state. |
| `project.stage` | `workspace_entity.lifecycle` | Use as a fallback or companion lifecycle signal for project manifests. |
| `governance.primary_standard_path` | `workspace_entity.governing_standards` | Resolve to WGS/SFDS/other governing standard labels when possible. |
| `governance.additional_standard_paths` | `workspace_entity.governing_standards` | Preserve multiple governing standards for cross-standard projects. |
| `relationships.parent` | `manifest_coverage.parent_registered` | Compare manifest parent to the parent registry or expected containing root. |
| `relationships.child_projects` | Manifest coverage metrics | Use to detect missing registered children. |
| `relationships.child_containers` | Manifest coverage metrics | Use to detect missing registered child containers. |
| `structure.children` | Manifest coverage metrics | Compare registered children to physical directories. |
| `artifacts.validators` | `standard_suite_coverage.validators_registered` | Count standards with runnable or documented validators. |
| `artifacts.examples` | `standard_suite_coverage.examples_present` | Use for suite evidence coverage. |
| `artifacts.reference_examples` | `standard_suite_coverage.examples_present` | Include reference examples when present. |

## Severity Semantics

| Severity | Meaning |
| --- | --- |
| `info` | Context or advisory note; no immediate action required. |
| `warning` | Drift or incompleteness that should be scheduled. |
| `error` | Structural issue that invalidates part of the workspace record. |
| `blocker` | Issue that prevents reliable audit, migration, release, or promotion. |

## Governed Audit History

Audit history should live under a governed WGS audit-history folder once created.
Until that folder exists, generated datasets should be treated as local outputs and should not be committed unless a task explicitly asks to preserve a specific snapshot.

Recommended future folder shape:

```text
WGS/audit-history/
  YYYY-MM-DD/
    audit-run.json
    workspace-entities.jsonl
    manifest-coverage.jsonl
    audit-findings.jsonl
    standard-suite-coverage.jsonl
```

Committed audit-history snapshots should be reserved for named reviews, migration checkpoints, release gates, or standards-health baselines.
Routine generated outputs may remain local scratch data unless they are explicitly promoted into the governed history.

## Implementation Notes

- `workspace_inventory.py` should own physical discovery, entity inventory, and manifest coverage records.
- `city_hall_audit.py` should own audit findings and standard-suite coverage records.
- A later dashboard generator may join both outputs, but the source tools should remain useful without the dashboard.
- Records should be deterministic enough for diffing when the workspace has not changed.
- Tool failures should emit an incomplete `audit_run` record when possible, with the failure reason captured in `summary` or a blocker finding.

## Acceptance Criteria

The first implementation of this spec is complete when:

- `workspace_inventory.py` can emit JSONL records for entities and manifest coverage.
- `city_hall_audit.py` can emit JSONL records for findings and standard-suite coverage.
- A single audit run can be identified by `run_id` across all output files.
- The output can be loaded by a simple JSONL reader without parsing Markdown.
- Documentation states that dashboard rendering is optional and separate from audit data generation.
