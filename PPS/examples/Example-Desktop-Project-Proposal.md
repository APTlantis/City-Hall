# City Hall Standards Workbench Proposal

## Project Type

Desktop application

## Readiness Level

draft

## Governing Standards

- Proposal: PPS
- Workspace: WGS
- Delivery: DRS
- Supporting: CTS, ATS, AAS

## Problem Statement

City Hall standards are readable as documents, but routine checks still require manual inspection across directories, manifests, changelogs, and validation checklists.

## Mission

Build a local desktop workbench that helps maintainers inspect standards, run non-mutating audits, open the relevant source documents, and record follow-up tasks without changing source files unexpectedly.

## Design Boundaries

The application belongs in the local City Hall workspace and may read standard directories, manifests, changelogs, validation checklists, and audit outputs.

The application does not define standards, auto-promote maturity, rewrite specifications, publish releases, or replace the governing documents.

## Success Criteria

- [ ] The app lists every registered standard directory.
- [ ] The app shows README, specification, manifest, changelog, adoption guide, validation checklist, examples, templates, and validators status.
- [ ] The app can run the WGS City Hall audit in read-only mode.
- [ ] The app records proposed follow-up tasks as ATS-compatible records.
- [ ] The app can be used without network access.

## Failure Criteria

- [ ] The app modifies standard documents without explicit user action.
- [ ] The app treats audit warnings as automatic authority to change maturity status.
- [ ] The app hides validation gaps from maintainers.

## Constraints

- Technical: Prefer native local file reads and explicit audit commands.
- Scope: Standards visibility and maintenance workflow only.
- Runtime: Windows desktop first.
- Data: No secrets, credentials, or private user notes are copied into task records.

## Risks

- Risk: UI convenience could make the workbench feel more authoritative than the standards.
- Mitigation: Display source file links and governing standard references beside each status.

## Roadmap

1. Proposal.
2. Read-only inventory prototype.
3. Audit integration and ATS task export.
4. DRS packaging review.
5. Candidate release.
