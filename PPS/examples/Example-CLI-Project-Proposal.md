# Example CLI Project Proposal

## Project Type

CLI tool

## Readiness Level

ready

## Governing Standards

- Proposal: PPS
- Workspace: WGS
- Delivery: CTS
- Supporting: DDS if the tool emits dataset records

## Problem Statement

The workspace needs a small command that checks standard manifests for missing required fields and broken artifact references.

## Mission

Build a read-only manifest audit CLI that reports standard-suite metadata gaps without modifying files.

## Design Boundaries

In scope:

- Read `PPS.manifest.toml` files.
- Check required SFDS sections.
- Check that referenced local artifacts exist.
- Print human-readable output by default and JSON with `--json`.

Out of scope:

- Editing manifests.
- Moving files.
- Validating domain-specific adopter artifacts.
- Replacing WGS inventory or SFDS validation checklists.

## Success Criteria

- [ ] Finds every `PPS.manifest.toml` under City Hall.
- [ ] Reports missing required sections.
- [ ] Reports missing referenced files.
- [ ] Returns documented CTS exit codes.
- [ ] Provides JSON output without progress text on stdout.

## Failure Criteria

- [ ] The tool mutates files during audit.
- [ ] JSON output mixes diagnostics with stdout.
- [ ] Missing files are silently ignored.

## Constraints

- Technical: Must run locally without network access.
- Scope: Standard-suite manifests only.
- Runtime: PowerShell or Python is acceptable.
- Data: Reads repository files only.

## Risks

- Risk: The tool could be mistaken for a full standards validator.
- Mitigation: Name and help text must state that it validates suite metadata only.

## Roadmap

1. Proposal.
2. Read-only manifest discovery.
3. Required-section checks.
4. Artifact-path checks.
5. CTS command contract and release checklist.

