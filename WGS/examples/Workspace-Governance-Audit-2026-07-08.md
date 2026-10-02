# Workspace Governance Audit — 2026-07-08

## Verdict

- Full audit exit code: `0`
- Audit scopes: `24`
- Inventory roots: `8`
- Failures: `0`
- Warnings: `0`
- Active governed project/group records: `55`
- Superseded fixed-name manifests remaining: `0`
- Duplicate local entity authorities: `0`

Lifecycle distribution: 34 active, 12 experimental, 6 paused, 2 reference, and 1 blocked. No project is classified `release-ready` from governance structure alone.

## Commands

```powershell
python D:\.city_hall\WGS\tools\workspace_inventory.py --workspace-root D:\
python D:\.city_hall\WGS\tools\city_hall_audit.py --root D:\.city_hall --workspace-root D:\
python D:\.city_hall\WGS\tools\snapshot_root_governance.py --workspace-root D:\
```

## Coverage

- Entity-named canonical manifest and exact filename
- Duplicate authority and superseded fixed-name detection
- Manifest path and parent relationship
- Physical versus registered child topology
- Child classification and project-group traversal
- Canonical `.city_hall` standard links
- Required agent/project documents
- Explicit project versions and lifecycle classifications
- Verification boundary and release-ready evidence guard
- Holding registration and exclusion from active reporting
- Portfolio-root Windows shortcut rejection
- Foundation root topology
- Root snapshot SHA-256 currency

## Scaffold acceptance

`governance_scaffold.py` was run first in dry-run mode and then with `--apply` against `WGS/tests/fixtures/TEST`. It created and registered `ExampleProject` with `AGENTS.md`, `ExampleProject.manifest.toml`, and `Project-README.md`. Both the parent fixture and generated project passed `city_hall_audit.py` without manual repair.

## Interpretation boundary

This verdict proves governance structure and metadata consistency. It does not prove every project's current build, tests, shipping artifact, installation, launch, or release readiness. Those claims remain project-specific and are represented by explicit verification fields.
