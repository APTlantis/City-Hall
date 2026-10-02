# SIS Suite Map

## Standard-Suite Governance

- README: `../README.md`
- Primary specification: `../Service and Infrastructure Standard.md`
- Manifest: `../SIS.manifest.toml`
- Adoption guide: `../Adoption-Guide.md`
- Validation checklist: `../Validation-Checklist.md`
- Changelog: `../CHANGELOG.md`
- Schema: `../ServiceManifest.schema.toml`
- Templates: `../templates/`

## Adopter Artifacts

SIS adopters use:

- service manifests;
- service runbooks;
- health check contracts;
- resource constraint contracts;
- lifecycle command documentation;
- log/cache/state path declarations.

## Boundary

SIS governs running local services and infrastructure.
WGS governs placement and registration.
CTS governs command shape when lifecycle or health controls are CLI commands.
