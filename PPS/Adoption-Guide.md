# PPS Adoption Guide

Use PPS before starting a new project or when reviving a project whose purpose has become unclear.

## Steps

1. Copy `templates/Project-Proposal.md`.
2. Fill in problem, mission, boundaries, success criteria, failure criteria, constraints, risks, and roadmap.
3. Create or update `YourProject.manifest.toml` using the generic v2.4 template as a starting point if needed.
4. Create or update `PROJECT-READMAP.toml` so evaluators know which files and evidence roots to read first.
5. Link the governing delivery standard such as DRS, CTS, SIS, WDS, or DDS.
6. Do not begin broad implementation until proposal exit criteria are met.
7. Mark the proposal `rework` if implementation drifts beyond the recorded mission, boundaries, or failure criteria.

## Generator

Use the lightweight generator to create proposal, entity-manifest, and project-read-map skeletons:

```powershell
python PPS\tools\pps_new.py "Manifest Audit" --type cli --delivery-standard CTS --readiness sketch --output-dir .\ManifestAudit
```

The generated files are starting points.
They must still pass the PPS validation checklist before broad implementation begins.

## SFDS Relationship

Use SFDS to maintain PPS as a standard suite.
Use PPS to decide whether a proposed project is clear enough to create, revive, or expand.

## WGS Relationship

Use WGS to place and register the project.
Use PPS to define why the project exists, what success means, what failure means, and which work must stay outside the boundary.
Use `WGS-Lifecycle-Mapping.md` to map proposal readiness to WGS lifecycle state.
