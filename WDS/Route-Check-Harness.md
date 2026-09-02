# WDS Route Check Harness

## Purpose

This harness pattern keeps preview and production route checks reusable across site projects.

## Preview

```powershell
python WDS/tools/route_check.py --base-url http://localhost:3000 --routes / /about /status --json
```

## Production

```powershell
python WDS/tools/route_check.py --base-url https://example.com --routes / /about /status --json
```

## Policy

- Preview checks prove local or staging routing before publication approval.
- Production checks prove the deployed URL after publication.
- Production checks should run after the deployment record is generated and before marking a site `published`.
