# Deployment Record

## Site

- Site id:
- Domain:
- Environment: [preview / production / internal]

## Version / Commit

- Version:
- Commit or snapshot:
- Deployed at:

## Build Command

- Command:
- Result:
- Output path:

## Deployment Target

- Provider or host:
- Target URL:
- Deployment path or project:

## Verification

- [ ] Build passed.
- [ ] Site loaded.
- [ ] Key routes checked.
- [ ] Metadata checked.
- [ ] Accessibility smoke check completed.
- [ ] Static assets loaded.
- [ ] Rollback or restore path documented.

Suggested commands:

```powershell
python WDS\tools\wds_validate.py WDS\templates\Site-Manifest.toml
python WDS\tools\route_check.py https://example.com / /about --json
python WDS\tools\accessibility_smoke.py https://example.com --json
```

## Routes Checked

| Route | Expected result | Verified |
| --- | --- | --- |
| `/` | Loads successfully | [ ] |

## Notes
