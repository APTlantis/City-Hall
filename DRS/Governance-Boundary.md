# DRS Governance Boundary

## Scope

DRS governs desktop application release readiness: release notes, project manifests, artifact naming, artifact hashes, release checklists, documentation delivery, build verification, and release evidence.

## Does Not Govern

DRS does not govern initial project proposal quality, workspace root placement, CLI command output contracts, website deployment records, dataset provenance, or semantic design language.

## Relationship to WGS and SFDS

WGS places DRS in the workspace governance model.
SFDS describes the documentation-suite structure DRS now participates in: `DRS.manifest.toml` describes the DRS suite, while DRS domain schemas and templates describe adopter release artifacts.
DRS itself remains the practical release standard for desktop applications.

SFDS normalization must not rewrite the DRS release process, remove existing templates, replace the MiniVault example, or change `drs.ps1` behavior unless a future DRS revision explicitly calls for that work.
