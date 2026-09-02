# SFDS Compatibility Matrix

## Purpose

This matrix records the machine-readable vocabulary SFDS expects standard-suite manifests to use.
It complements `STANDARD.manifest.schema.toml` and gives validators a shared compatibility target.

## Manifest Vocabulary

| Field | Supported values | Notes |
| --- | --- | --- |
| `[standard].status` | `concept`, `draft`, `planned`, `candidate-active`, `active`, `stable`, `deprecated`, `retired` | Standard suites should prefer `active` once adopted. `candidate-active` is allowed for promoted or pilot suites still gathering evidence. |
| `[standard].maturity` | `concept`, `draft`, `candidate`, `stable`, `reference-candidate`, `reference` | Matches the SFDS maturity ladder and its transitional reference-candidate label. |
| `[promotion].promotion_state` | `draft`, `candidate-active-library-copy`, `active-library-copy`, `promoted`, `deprecated` | Promotion state is optional and only applies when a standard copy moves between governed roots. |

## Compatibility Rules

| Change type | Compatibility effect | Required action |
| --- | --- | --- |
| Add optional manifest field | Compatible minor or patch change | Register the field in documentation before relying on automation. |
| Add required manifest field | Compatibility-impacting change | Major version or explicit migration note. |
| Add maturity/status value | Compatibility-impacting for validators | Update this matrix, validator vocabulary, examples, and changelog together. |
| Rename required artifact key | Breaking change | Preserve old examples or provide migration notes. |
| Add validator warning | Compatible | Document reviewer meaning in validation guidance. |
| Convert warning to error | Compatibility-impacting | Record the gate change in the changelog. |

## Current Validator Contract

`tools/sfds_validate.py` treats missing required suite sections, missing required artifact references, unresolved declared artifacts, and non-SFDS meta-standard declarations as errors.

Vocabulary values outside this matrix are warnings unless SFDS later promotes them to blocking errors.
