# Service and Infrastructure Standard

## Status

Candidate v0.1.0.

## Scope

SIS governs local-first background services, local APIs, daemons, schedulers, cache services, model services, indexing services, Docker-backed local infrastructure, and shared workspace infrastructure.

SIS applies when a project or workspace component:

- runs continuously or on a schedule;
- listens on a local port or socket;
- owns a cache, database, queue, index, or state directory;
- provides a dependency that other projects or agents call;
- requires startup, shutdown, health, log, or recovery behavior beyond a one-shot command.

## Does Not Govern

SIS does not govern:

- desktop application release packaging; use DRS;
- one-shot CLI command behavior; use CTS;
- public website deployment; use WDS;
- dataset provenance and splits; use DDS;
- project intent; use PPS;
- workspace placement and registration; use WGS.

## Relationship to WGS and PPS

WGS defines the shared services layer and registers service or infrastructure entities.

PPS defines why the service exists, who it serves, success criteria, failure criteria, and boundaries.

SIS defines how the service behaves while running and how operators or agents safely control it.

## Required Service Artifacts

Every SIS-governed service must provide:

- Service manifest.
- Service runbook.
- Health check contract.
- Resource constraint contract.
- Start command.
- Stop command.
- Restart command or documented restart procedure.
- Status or health command.
- Log location and rotation policy.
- State, cache, database, and storage paths.
- Port, socket, and network dependency declarations.
- Recovery procedure.
- Known failure modes.

## Lifecycle Commands

Every service must document automation-safe lifecycle commands:

| Command | Required | Purpose |
| --- | --- | --- |
| start | yes | Starts the service or declares why startup is host-managed. |
| stop | yes | Performs graceful shutdown. |
| restart | yes | Restarts safely or delegates to documented stop/start. |
| status | yes | Reports process and dependency status. |
| health | yes | Reports machine-readable service health. |
| logs | should | Shows recent logs without opening unbounded files. |

Lifecycle commands should be callable by an operator or agent without reading source code.

## Graceful Shutdown

A service must document how it handles graceful shutdown.

The service should:

- respond to the normal host shutdown signal;
- stop accepting new work before terminating active work;
- flush or checkpoint state when practical;
- avoid corrupting active databases, caches, queues, or index files;
- report whether forced termination is safe.

If graceful shutdown is not possible, the service must document the risk and recovery path.

## Health Checks

Every service must expose a health check through a command, endpoint, socket, or file contract.

Machine-readable health output should include:

- service ID;
- status: `healthy`, `degraded`, `offline`, or `unknown`;
- version when known;
- uptime or last-started time when known;
- checked dependencies;
- active port or socket when applicable;
- storage/cache state when applicable;
- warnings;
- errors;
- next safe action.

Health output must not require credentials for local operator visibility unless the service has a documented security reason.

## Port and Network Boundaries

Every service must declare:

- required ports;
- optional ports;
- protocol;
- bind address;
- whether the service is local-only;
- whether remote access is forbidden, optional, or required;
- port conflict behavior;
- firewall expectations when relevant.

Local-first services should bind to loopback by default unless the service manifest explains why broader binding is required.

## Storage and State Boundaries

Every service must declare:

- state paths;
- cache paths;
- database paths;
- log paths;
- temporary paths;
- backup or snapshot paths when relevant;
- cleanup rules.

The service must distinguish durable state from disposable cache.

## Resource Constraint Contract

Every service must document resource bounds:

- maximum log size or retention window;
- log rotation behavior;
- maximum cache size or cleanup trigger;
- database growth expectations;
- CPU expectations;
- memory expectations;
- disk pressure behavior;
- network behavior;
- cleanup command.

Services must not create unbounded logs or caches without an explicit exception.

## Logs

Logs should be useful to an operator without becoming a storage hazard.

A SIS-governed service must document:

- log directory;
- log format;
- rotation policy;
- retention policy;
- maximum size or maximum age;
- how to view recent logs;
- whether logs can contain sensitive data.

## Dependency Readiness

Services must declare dependencies such as:

- local databases;
- queues;
- model runtimes;
- Docker containers;
- file watchers;
- scheduled tasks;
- other services;
- network availability.

Health checks should report dependency state separately from service process state.

## Agent Orientation

An agent must be able to read the manifest and runbook to know:

- whether the service should be running;
- how to check health;
- whether it is safe to restart;
- which files or ports it must not modify;
- how to avoid interfering with active work;
- what evidence to record after changes.

If a service is production-like or preserves state, agents should not restart it without operator approval unless the runbook explicitly allows that action.

## Release and Change Readiness

A service is blocked from candidate or release use when:

- no health check exists;
- start/stop behavior is undocumented;
- ports are undocumented;
- state/cache/log paths are undocumented;
- logs or caches can grow without bounds;
- restart can corrupt state;
- dependencies are hidden in source code only;
- recovery procedure is missing;
- agent-safe operating rules are missing.

## Relationship to CTS

Service lifecycle commands should follow CTS where they are command-line tools.

SIS owns service behavior.
CTS owns command shape, stdout/stderr behavior, JSON output, and exit codes.

## Relationship to AAMHS and ARHS

When a service produces release artifacts, archives, snapshots, or preservation bundles, ARHS and AAMHS govern hash and archive integrity records.

SIS governs the running service and its local operating boundaries.

## Readiness Levels

| Level | Meaning |
| --- | --- |
| experimental | Service may run locally but lacks complete lifecycle and health contracts. |
| documented | Service has manifest, runbook, ports, paths, health check, and resource contract. |
| candidate | Service has been exercised by an operator or agent using only documented contracts. |
| stable | Service has repeatable lifecycle, health, recovery, and resource behavior across real use. |
| deprecated | Service remains documented but has a replacement or shutdown plan. |

## Core Principle

A local service is part of the workspace infrastructure.

It must not become a mystery process.
