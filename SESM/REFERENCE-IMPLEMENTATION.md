# SESM Reference Implementation

## Status

The current SESM reference implementation is the combination of schema, tools, tests, and examples in this directory.

The reference implementation demonstrates how to embed, convert, validate, and test SESM metadata. It is not the only permitted implementation.

## Files

| File or directory | Role |
| --- | --- |
| `svg_asset.schema.json` | Canonical SESM metadata schema for the current candidate profile. |
| `Embed-SESM.py` | Embeds and validates SESM metadata in SVG files. |
| `Validate-SESM-Safe.py` | Validates SESM metadata and the SESM safe SVG profile. |
| `Convert-to-SVG.py` | Converts raster image inputs to SVG outputs for SESM workflows. |
| `tests/` | Unit and integration tests for embedding, conversion, metadata merging, and validation behavior. |
| `fixtures/` | Valid, invalid, and warning SVG fixtures for validator review. |
| `templates/SESM-Metadata-Example.json` | Minimal example metadata payload for adopters. |
| `svg/` | Example SVG assets used by the local workflow. |
| `examples/SESM-Suite-Map.md` | SFDS suite map showing standard-suite structure. |

## Validation

Run the test suite:

```powershell
python SESM\tests\run_tests.py
```

Validate or embed metadata with:

```powershell
python SESM\Embed-SESM.py --input-dir SESM\svg --schema SESM\svg_asset.schema.json --validate-only
```

Validate the safe profile with:

```powershell
python SESM\Validate-SESM-Safe.py SESM\fixtures\valid\basic-safe.svg --safe-profile
```

## Reference Behavior

The reference implementation demonstrates:

- extraction and embedding of `<metadata id="sesm">`;
- JSON schema validation;
- fallback structural validation when optional dependencies are unavailable;
- deep merge behavior for override metadata;
- NeonInk/NIPC theme detection heuristics;
- raster-to-SVG conversion support;
- test-backed conversion behavior.
- safe-profile validation for executable SVG features, duplicate metadata, JSON errors, remote references, and unsafe agent-authority language.

## Safety Boundary

The reference implementation is not a complete SVG sanitizer.

For safety review, use:

- `SAFE-PROFILE.md`;
- `THREAT-MODEL.md`;
- `VALIDATOR-RULES.md`;
- independent SVG sanitization where untrusted SVG ingestion is required.

## External Implementations

External implementations should be able to:

1. locate the SESM metadata block;
2. parse the JSON payload;
3. validate the payload against the schema or a documented compatible profile;
4. ignore unknown fields unless intentionally supported;
5. enforce the safe profile before claiming `sesm-safe`;
6. report validation findings in a stable, automation-friendly form.
