# WDS Monitoring Integration Fields

## Purpose

These optional fields let WDS adopters record monitoring expectations without requiring a specific monitoring vendor.

## Suggested Manifest Table

```toml
[monitoring]
uptime_check = "https://status.example.invalid/example-site"
synthetic_routes = ["/", "/status"]
accessibility_review_cadence = "before publication and after major layout changes"
owner = "site maintainer"
incident_runbook = "docs/Incident-Runbook.md"
```

## Rules

- Monitoring fields are optional for draft and preview sites.
- Published sites should record either active monitoring or a reason monitoring is not applicable.
- Monitoring does not replace WDS route checks, metadata checks, deployment records, or accessibility review.
