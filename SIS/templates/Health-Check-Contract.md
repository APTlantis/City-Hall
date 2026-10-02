# Health Check Contract

## Service

- Name:
- Service ID:

## Invocation

```text
service health --json
```

## Output

Machine-readable output should include:

```json
{
  "service_id": "example-service",
  "status": "healthy",
  "version": "",
  "uptime_seconds": 0,
  "dependencies": [],
  "ports": [],
  "storage": [],
  "warnings": [],
  "errors": [],
  "next_safe_action": "none"
}
```

## Status Values

| Status | Meaning |
| --- | --- |
| `healthy` | Service is running and dependencies are available. |
| `degraded` | Service is running but a dependency, resource, or non-critical function has a problem. |
| `offline` | Service is not running or cannot serve requests. |
| `unknown` | Health could not be determined. |

## Exit Codes

Use CTS exit code conventions when health is exposed as a command.

| Code | Meaning |
| --- | --- |
| 0 | Healthy. |
| 1 | General health command failure. |
| 3 | Service or dependency missing. |
| 4 | Service degraded or offline. |
| 5 | External dependency unavailable. |
