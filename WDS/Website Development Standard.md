# Website Development Standard

## Status

Candidate v0.2.1.

## Scope

WDS governs websites and web applications: site manifests, deployment records, accessibility requirements, SEO metadata, structured data, static asset organization, release documentation, monitoring, and uptime expectations.

## Does Not Govern

WDS does not govern desktop app releases, CLI output contracts, dataset provenance, or workspace root layout.

## Required Website Artifacts

- Site manifest.
- Deployment record.
- Accessibility checklist.
- SEO and structured metadata record.
- Static asset organization notes.
- Release or publication notes.
- Monitoring and uptime notes.
- Rollback or restore note.
- Key route inventory.

## Relationship to PPS and WGS

PPS defines why a website exists, who it serves, what success means, and what it must not become.
WGS registers the site project, lifecycle state, workspace placement, and governing relationships.
WDS governs build, deployment, accessibility, metadata, monitoring, and publication evidence.

## Deployment Record Requirements

Every deployment record must answer four questions:

- What changed?
- What was built?
- Where was it deployed?
- How was it verified?

Minimum deployment evidence:

- Site id and domain.
- Version, commit, or content snapshot.
- Build command and result.
- Deployment target and environment.
- Deploy time.
- Routes checked after deployment.
- Accessibility and metadata checks.
- Rollback or restore note.

## Environment Levels

| Level | Meaning |
| --- | --- |
| `local` | Runs on a developer machine only. |
| `preview` | Deployed for review, staging, or internal validation. |
| `production` | Public or canonical deployment target. |
| `archived` | Preserved snapshot or static copy; no active publishing expected. |

Deployment records must name the environment.
Production records must include post-deploy route checks.

## Website Readiness Levels

| Level | Meaning |
| --- | --- |
| `draft` | Site exists locally, but build/deploy/quality records are incomplete. |
| `preview` | Build works and a non-production deployment target is recorded. |
| `published` | Production deployment, metadata, accessibility, and key routes are verified. |
| `maintained` | Monitoring or review cadence is recorded. |
| `archived` | Site is intentionally preserved but no longer actively maintained. |

## Deployment Rules

- A deployment without a record is a file upload, not a governed release.
- Public pages must have title and description metadata.
- Key routes must be checked after deployment, not only during local build.
- Rollback expectations must be stated even when rollback is manual.
- Accessibility checks must be recorded before a public deployment is treated as published.
- Structured metadata should be present where it helps search, sharing, provenance, or agent interpretation.
- Generated assets must have source or generation notes when they are part of the site identity.
- Monitoring expectations must state whether uptime is actively monitored, manually reviewed, or intentionally unmanaged.

## Website Release Blockers

A WDS-governed site is blocked from publication when:

- Build or export commands fail.
- Deployment target or environment is unknown.
- Key routes are not listed or checked.
- Public pages lack title or description metadata.
- Accessibility review is missing for production publication.
- Rollback or restore expectation is undocumented.
- The site claims canonical status without a stable domain or publication record.
- Required legal, license, privacy, or attribution content is missing for the site context.
