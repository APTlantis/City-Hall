# Service and Infrastructure Standard (SIS)

![Standard](https://img.shields.io/badge/service%20standard-SIS%20v0.1.0-blue)
![Manifest](https://img.shields.io/badge/manifest-TOML-orange)
![Status](https://img.shields.io/badge/status-candidate-lightgrey)

SIS governs local-first background services and shared infrastructure in the Aptlantis workspace.

It covers the things that do not behave like one-shot commands, desktop releases, websites, or datasets: long-running daemons, local APIs, model services, cache services, Docker-backed infrastructure, indexers, schedulers, and workspace-level support processes.

## City Hall Role

SIS fills the delivery-standard gap for the WGS shared services layer.

WGS decides where services live and how they are registered.
PPS decides why a service should exist.
SIS decides how a service must start, stop, report health, declare ports, bound resources, rotate logs, and recover safely.

## Read First

1. `Service and Infrastructure Standard.md`
2. `SIS.manifest.toml`
3. `Adoption-Guide.md`
4. `Validation-Checklist.md`
5. `templates/Service-Manifest.toml`
6. `templates/Service-Runbook.md`
7. `templates/Health-Check-Contract.md`
8. `templates/Resource-Constraint-Contract.md`

## Core Rule

A service is not ready for broad use until an operator or agent can answer:

- What starts it?
- What stops it safely?
- How do I know if it is healthy?
- What ports, paths, caches, and logs does it own?
- What are its resource bounds?
- What is the recovery path after failure?

If those answers are not documented, the service remains experimental.
