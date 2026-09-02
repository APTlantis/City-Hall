# Manifest v2.4 Entity Adaptation

## Reason

The earlier default TOML manifest identified itself as `APTlantis Project Manifest v2.3` and assumed every governed object was a project. The workspace rollout requires manifests for directories as well as projects.

## Change

Version 2.4 introduces a common entity layer:

- `[manifest]` records schema, version, manifest type, canonical filename, and maintainer.
- `[entity]` records id, title, kind, class, status, description, and tags.
- Domain tables such as `[workspace]`, `[directory]`, and `[project]` remain specific to the governed object.

## Compatibility

Existing project-specific fields are preserved where possible. Directory manifests now identify themselves explicitly as directory entities instead of being inferred from filename alone.
