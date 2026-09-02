# SESM Validator Rules

## Purpose

This document defines the minimum validator behavior expected for SESM review and adoption.

Validators may be stricter than this document. They must not be weaker when claiming `sesm-safe` conformance.

## Validator Inputs

A validator should accept:

- an SVG file;
- optional SESM schema path;
- optional safe-profile mode;
- optional policy settings for remote references, maximum metadata size, and extension fields.

The current reference validator is `Validate-SESM-Safe.py`.

## Required Metadata Checks

Validators must check:

- the SVG is parseable XML;
- a SESM block exists when SESM validation is requested;
- no more than one `<metadata id="sesm">` block exists;
- the SESM block contains valid JSON;
- `sesm_version` exists;
- the SESM object validates against `svg_asset.schema.json` or a documented compatible profile;
- unknown fields are either ignored or reported according to validator policy;
- validation errors include enough path information to locate the problem.

## Required Safe-Profile Checks

When safe-profile validation is requested, validators must flag:

- `<script>` elements;
- event handler attributes matching `on*`;
- `javascript:` URLs;
- remote resource references;
- duplicate SESM blocks;
- oversized metadata blocks;
- hidden text or payload-like content that appears unrelated to visible asset purpose;
- SESM fields that request credentials, command execution, policy bypass, or privileged agent action.

Validators must not label an SVG `sesm-safe` if any forbidden feature is present.

## Recommended Limits

Adopters should define limits appropriate to their environment. Suggested defaults:

- maximum SESM JSON size: 64 KiB;
- maximum SVG file size for routine validation: 5 MiB;
- maximum XML depth: implementation-defined parser safety limit;
- network access during validation: disabled.

## Output Contract

Validators should produce a human-readable report by default.

Automation-facing validators should also support JSON output with:

- `status`: `ok`, `warning`, or `error`;
- `profile`: `sesm-valid`, `sesm-safe`, `sesm-unsafe`, or `sesm-unverified`;
- `file`;
- `errors`;
- `warnings`;
- `metadata_version`;
- `schema`;
- `safe_profile_checked`.

CTS governs command output behavior for City Hall command tools.

Example:

```powershell
python SESM\Validate-SESM-Safe.py SESM\fixtures\valid\basic-safe.svg --safe-profile --json
```

Example JSON output is preserved at `examples/validator-json-basic-safe.json`.

## Exit Codes

Recommended exit codes:

| Code | Meaning |
| --- | --- |
| 0 | Validation passed. |
| 1 | General failure. |
| 2 | Invalid usage or arguments. |
| 3 | Input file, schema, or resource missing. |
| 4 | Validation failed. |
| 5 | Dependency unavailable. |

## Non-Goals

SESM validators are not required to:

- render SVGs;
- prove visual identity;
- follow remote links;
- verify all provenance claims;
- replace release integrity records;
- replace a general-purpose SVG sanitizer.
