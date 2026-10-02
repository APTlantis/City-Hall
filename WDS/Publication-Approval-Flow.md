# WDS Publication Approval Flow

## Purpose

This note defines the WGS registration and publication approval flow for WDS-governed sites.

## Flow

1. PPS records why the site exists and what success means.
2. WGS registers the site project, lifecycle state, workspace path, and governing standards.
3. WDS records site manifest, deployment evidence, route checks, accessibility checks, metadata checks, rollback expectations, and monitoring notes.
4. The site may be marked `published` only after production deployment evidence exists.

## Published State Requirements

A site must not be marked `published` until:

- the WGS project manifest exists or is queued with the site path and governing standards;
- `deployment.environment` is `production`;
- `metadata.title`, `metadata.description`, and `metadata.canonical` are recorded;
- key routes are checked after deployment;
- accessibility and metadata smoke checks are recorded;
- rollback or restore expectation is documented;
- a deployment record identifies version or content snapshot, target, environment, and verification evidence.

## Authority

WGS owns registration and lifecycle state.
WDS owns website publication evidence.
PPS owns the project intent boundary.
