# Build Artifact Signing Standard Proposal

## Project Type

Standard

## Readiness Level

sketch

## Governing Standards

- Proposal: PPS
- Workspace: WGS
- Delivery: SFDS, DRS
- Supporting: ARHS, AAMHS, ATS

## Problem Statement

ARHS and AAMHS govern hashing and archive integrity, but City Hall does not yet have a dedicated standard for release signing policy, signer identity, key rotation, or signature verification evidence.

## Mission

Create a Build Artifact Signing Standard that defines when signatures are required, what signature evidence must be recorded, and how signing records relate to ARHS and AAMHS hash records.

## Design Boundaries

The standard governs signing policy, signer metadata, verification records, and relationship rules with release and archive integrity standards.

The standard does not replace ARHS hashes, AAMHS archive manifests, DRS release packaging, or external legal policy.

## Success Criteria

- [ ] The suite follows SFDS directory and artifact requirements.
- [ ] The standard clearly distinguishes signing from hashing.
- [ ] Required signing records are template-backed.
- [ ] Validation checklist records unresolved key-management questions.

## Failure Criteria

- [ ] The standard weakens existing ARHS or AAMHS requirements.
- [ ] The suite omits README, primary specification, manifest, adoption guide, validation checklist, changelog, or examples.
- [ ] The proposal claims stable maturity before reference examples exist.

## Constraints

- Technical: Must support detached signatures and offline verification records.
- Scope: Artifact signing only.
- Runtime: Local release workflow first.
- Data: Key material must never be stored in the standard suite.

## Risks

- Risk: Premature rules could lock in the wrong signing tool.
- Mitigation: Keep v0.1 focused on records and verification expectations before selecting required tooling.

## Roadmap

1. Proposal.
2. SFDS-compliant draft suite.
3. Example signed artifact record.
4. DRS release integration review.
5. Candidate maturity review.
