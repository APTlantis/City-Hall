# WGS CI Usage

## Purpose

Use WGS checks as read-only structural regression gates for governed workspace roots and standard-suite documentation changes.

## Local Checks

```powershell
python WGS/tools/city_hall_audit.py --root .
python WGS/tools/workspace_inventory.py --workspace-root D:/ --format jsonl
python WGS/tools/link_integrity.py WGS SFDS DRS CTS WDS PPS SESM AAMHS LDS
```

Use manifest diff when reviewing a manifest change:

```powershell
python WGS/tools/manifest_diff.py old.manifest.toml new.manifest.toml --json
```

## Scheduled Audit Sketch

```powershell
$stamp = Get-Date -Format yyyy-MM-dd
$out = "WGS/audit-history/$stamp"
New-Item -ItemType Directory -Force $out | Out-Null
python WGS/tools/city_hall_audit.py --root . --format jsonl | Set-Content "$out/standard-suite-coverage.jsonl"
python WGS/tools/workspace_inventory.py --workspace-root D:/ --format jsonl | Set-Content "$out/workspace-entities.jsonl"
```

Generated audit-history snapshots should be committed only for named reviews, migration checkpoints, release gates, or standards-health baselines.

## GitHub Actions Example

```yaml
name: wgs-structural-audit

on:
  pull_request:
    paths:
      - "**/*.manifest.toml"
      - "**/*.md"
      - "WGS/tools/**"

jobs:
  audit:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: Standards audit
        shell: pwsh
        run: python WGS/tools/city_hall_audit.py --root .
      - name: Link integrity
        shell: pwsh
        run: python WGS/tools/link_integrity.py WGS SFDS DRS CTS WDS PPS SESM AAMHS LDS
```
