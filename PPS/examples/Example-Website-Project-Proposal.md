# Public Standards Portal Proposal

## Project Type

Website

## Readiness Level

draft

## Governing Standards

- Proposal: PPS
- Workspace: WGS
- Delivery: WDS, DRS
- Supporting: CTS, ARHS

## Problem Statement

City Hall standards are maintained locally, but collaborators need a browsable, versioned way to read stable and candidate standards without navigating the workspace tree directly.

## Mission

Create a static website that publishes selected standards, maturity status, changelog excerpts, and adoption guidance from the City Hall documentation suite.

## Design Boundaries

The website may publish approved standards content, suite maps, maturity tables, and generated health summaries.

The website must not expose private workspace paths, unpublished notes, local service metadata, credentials, or draft content not approved for publication.

## Success Criteria

- [ ] The site provides one page per standard.
- [ ] Each page links README, primary specification, adoption guide, validation checklist, changelog, and examples where publishable.
- [ ] The site distinguishes stable, candidate, draft, and deprecated maturity states.
- [ ] Generated output can be reproduced from committed source documents.

## Failure Criteria

- [ ] The site implies candidate standards are stable.
- [ ] The build includes private local paths or unapproved reference files.
- [ ] The site has hand-authored status data that drifts from manifests.

## Constraints

- Technical: Static-first build with deterministic generation.
- Scope: Publishing and navigation only.
- Runtime: Local build, then static hosting.
- Data: Only approved standard-suite artifacts.

## Risks

- Risk: Generated navigation can drift from source manifests.
- Mitigation: Build from entity-named manifests and fail when required fields are missing.

## Roadmap

1. Proposal.
2. Content eligibility review.
3. Static generator prototype.
4. WDS design review.
5. DRS release package.
