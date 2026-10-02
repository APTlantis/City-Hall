# WDS Minimal Conformance Suite

## Purpose

This conformance suite gives WDS adopters a small repeatable validation target.

## Checks

```powershell
python WDS/tools/wds_validate.py WDS/templates/Site-Manifest.toml --json
python WDS/tools/route_check.py --base-url http://localhost:3000 --routes / --json
python WDS/tools/accessibility_smoke.py path/to/page.html --json
```

## Example Validator Output

```json
{
  "status": "ok",
  "tool": "wds-validate",
  "version": "0.1.0",
  "data": {
    "findings_count": 0
  },
  "errors": [],
  "warnings": []
}
```

Passing this suite means the site has the minimum WDS records and smoke checks.
It does not prove production readiness by itself.
