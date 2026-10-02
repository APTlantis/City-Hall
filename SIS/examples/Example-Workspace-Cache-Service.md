# Example Workspace Cache Service

## Service

- Name: Local Model Cache
- Service ID: `local-model-cache`
- Class: infrastructure
- Readiness: documented

## Purpose

Provide a shared local cache for model files so multiple projects do not redownload the same artifacts.

## Lifecycle

This service is filesystem-backed and does not run a persistent network listener.

```powershell
cache-tool status --json
cache-tool cleanup --dry-run
cache-tool cleanup --max-size 500GB
```

## Health Output

```json
{
  "service_id": "local-model-cache",
  "status": "degraded",
  "dependencies": [],
  "ports": [],
  "storage": [
    { "path": "D:\\.hf", "status": "available", "used_gb": 460, "limit_gb": 500 }
  ],
  "warnings": ["cache usage is above 90 percent"],
  "errors": [],
  "next_safe_action": "run cleanup dry-run and review candidates"
}
```

## Ports

No ports.

## Paths

- Durable index: `D:\015-DPW\local-model-cache\index`
- Cache: `D:\.hf`
- Logs: `D:\015-DPW\local-model-cache\logs`

## Resource Bounds

- Cache warning threshold: 450 GB.
- Cache hard limit: 500 GB unless operator expands it.
- Cleanup must support dry-run.
- Logs rotate at 5 MB per file and retain 20 files.

## Agent Rules

- Agents may run status and cleanup dry-run commands.
- Agents may not delete cache entries without operator approval unless a project-specific runbook grants permission.
