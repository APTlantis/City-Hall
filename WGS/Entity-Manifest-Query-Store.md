# Entity Manifest Query Store

## Purpose

This note defines a small reference query-store shape for WGS entity manifests.
It is intentionally database-neutral and can be implemented in SQLite or DuckDB after `workspace_inventory.py` emits JSONL records.

## Minimal Tables

```sql
create table audit_runs (
  run_id text primary key,
  generated_at text not null,
  workspace_root text not null,
  status text not null
);

create table workspace_entities (
  run_id text not null,
  path text not null,
  entity_name text not null,
  entity_type text not null,
  lifecycle text,
  manifest_path text,
  readme_path text,
  governing_standards text,
  registered_children integer,
  physical_children integer,
  primary key (run_id, path)
);

create table manifest_coverage (
  run_id text not null,
  path text not null,
  expected_manifest_path text,
  actual_manifest_path text,
  coverage_status text not null,
  naming_status text,
  parent_registered integer,
  primary key (run_id, path)
);

create table audit_findings (
  run_id text not null,
  finding_id text not null,
  rule_id text not null,
  severity text not null,
  path text,
  message text not null,
  evidence_json text,
  recommended_action text,
  primary key (run_id, finding_id)
);
```

## Example Queries

```sql
select lifecycle, count(*) as entities
from workspace_entities
group by lifecycle
order by entities desc;
```

```sql
select coverage_status, count(*) as manifests
from manifest_coverage
group by coverage_status
order by manifests desc;
```

```sql
select severity, count(*) as findings
from audit_findings
group by severity
order by findings desc;
```

## Import Notes

JSONL records from WGS tools should remain the exchange format.
Database tables are a query convenience, not a new source of truth.

For DuckDB, import JSONL directly into staging tables and then insert the relevant record types into the tables above.
For SQLite, use a small loader that parses each JSONL row and stores array/object fields as JSON text.
