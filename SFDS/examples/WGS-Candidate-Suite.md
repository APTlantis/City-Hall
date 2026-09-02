# WGS Candidate Suite Example

## Purpose

This example shows SFDS applied to a governance standard rather than a release standard.
It complements the DRS reference example by demonstrating how a standard suite can govern workspace structure, manifests, agent procedures, and audit tooling.

## Suite Identity

- Standard: WGS
- Suite manifest: `WGS/WGS.manifest.toml`
- Primary specification: `WGS/Workspace Governance Standard.md`
- Maturity pattern: candidate standard with operational tooling and governed examples

## SFDS Suite Artifacts

| Artifact | WGS example |
| --- | --- |
| README | `WGS/README.md` |
| Primary specification | `WGS/Workspace Governance Standard.md` |
| Suite manifest | `WGS/WGS.manifest.toml` |
| Adoption guide | `WGS/Adoption-Guide.md` |
| Validation checklist | `WGS/Validation-Checklist.md` |
| Changelog | `WGS/CHANGELOG.md` |
| Governance notes | `WGS/Manifest-Conventions.md`, `WGS/Agent-Startup-Procedure.md`, `WGS/Agent-Closeout-Procedure.md`, `WGS/Workspace-Audit-Dashboard-Spec.md` |
| Validators | `WGS/tools/city_hall_audit.py`, `WGS/tools/workspace_inventory.py` |
| Templates | `WGS/templates/` |
| Examples | `WGS/examples/` |

## Why This Is Not DRS

DRS demonstrates a mature release standard with adopter-facing release artifacts.
WGS demonstrates a workspace constitution standard where the adopter-facing artifacts are manifests, read-first documents, health records, and audit outputs.

This gives SFDS maintainers a second suite pattern for standards whose domain is governance rather than product release.

## Validation Notes

Validate WGS as an SFDS suite by checking:

- Required suite artifacts are present and registered.
- WGS clearly separates workspace-governance rules from adopter templates.
- WGS tools are registered as validation support.
- WGS examples show real governed records rather than placeholder-only templates.
- WGS compatibility and migration expectations remain discoverable through its roadmap, manifest conventions, and migration notes.
