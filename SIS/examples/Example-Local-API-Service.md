# Example Local API Service

## Service

- Name: Artifact Metadata API
- Service ID: `artifact-metadata-api`
- Class: service
- Readiness: documented

## Purpose

Provide a local-only HTTP API for querying artifact metadata records produced by FileCabinet and archive tools.

## Lifecycle

```powershell
python service.py start --config .\service.toml
python service.py stop --graceful
python service.py restart --graceful
python service.py health --json
```

## Health Output

```json
{
  "service_id": "artifact-metadata-api",
  "status": "healthy",
  "version": "0.1.0",
  "dependencies": [
    { "name": "metadata-index", "status": "healthy" }
  ],
  "ports": [
    { "name": "api", "port": 8732, "bind": "127.0.0.1" }
  ],
  "warnings": [],
  "errors": [],
  "next_safe_action": "none"
}
```

## Ports

| Name | Port | Protocol | Bind | Required |
| --- | ---: | --- | --- | --- |
| api | 8732 | HTTP | 127.0.0.1 | yes |

## Paths

- State: `D:\015-DPW\artifact-metadata-api\state`
- Cache: `D:\015-DPW\artifact-metadata-api\cache`
- Logs: `D:\015-DPW\artifact-metadata-api\logs`

## Resource Bounds

- Logs rotate at 10 MB per file.
- Logs retain the last 10 files.
- Cache cleanup starts at 2 GB.
- Cache is safe to rebuild from durable metadata records.

## Agent Rules

- Agents may run health and status checks.
- Agents may inspect logs.
- Agents may not restart the service during active indexing unless the runbook says the queue is idle.
