# SESM Adoption Guide

Use SESM when SVG assets need embedded provenance, semantic role, theme, UI hints, LLM context, or integrity metadata.

## Steps

1. Read `SESM-v0.2.md`.
2. Validate metadata against `svg_asset.schema.json`.
3. Use `Validate-SESM-Safe.py` when claiming SESM-safe SVG conformance.
4. Use `Embed-SESM.py` when embedding or updating metadata.
5. Run `tests/run_tests.py` after changing tooling.
6. Record SESM adoption in the project or asset manifest.

## SFDS Relationship

Use SFDS to maintain SESM as a standard suite.
Use SESM to govern embedded SVG metadata, schema validation, conversion support, and semantic asset context.
