# Deployment Record

## Site

- Site id: example-site
- Domain: example.local
- Environment: preview

## Version / Commit

- Version: 0.1.0
- Commit or snapshot: local-preview-2026-06-10
- Deployed at: 2026-06-10

## Build Command

- Command: `npm run build`
- Result: passed
- Output path: `dist`

## Deployment Target

- Provider or host: local static preview
- Target URL: `http://localhost:4173`
- Deployment path or project: `dist`

## Verification

- [x] Build passed.
- [x] Site loaded.
- [x] Key routes checked.
- [x] Metadata checked.
- [x] Accessibility smoke check completed.
- [x] Static assets loaded.
- [x] Rollback or restore path documented.

## Routes Checked

| Route | Expected result | Verified |
| --- | --- | --- |
| `/` | Loads successfully | [x] |
| `/about` | Loads successfully | [x] |

## Notes

Rollback is manual for preview: restore the previous build output or redeploy the prior commit.

