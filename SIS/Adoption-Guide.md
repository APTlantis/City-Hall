# SIS Adoption Guide

Use SIS when a project runs as a local service, daemon, scheduled process, local API, shared cache, model service, indexer, or workspace infrastructure component.

## Steps

1. Read `Service and Infrastructure Standard.md`.
2. Create a service manifest from `templates/Service-Manifest.toml`.
3. Create a runbook from `templates/Service-Runbook.md`.
4. Create a health check contract from `templates/Health-Check-Contract.md`.
5. Create a resource constraint contract from `templates/Resource-Constraint-Contract.md`.
6. Declare lifecycle commands, ports, storage paths, log policy, cache policy, dependencies, and recovery steps.
7. Validate the service against `Validation-Checklist.md`.
8. Use CTS for command-line shape when lifecycle controls are CLI commands.
9. Use WGS to register placement and lifecycle state.

## Adoption Rule

Do not treat a service as broadly usable until an operator or agent can start it, stop it, check health, inspect logs, identify ports, bound disk growth, and recover from failure without reading source code.
