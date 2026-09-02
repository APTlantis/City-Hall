# SESM Explainer

## Summary

SVG Embedded Semantic Metadata (SESM) is a small convention for placing a JSON metadata object inside an SVG `<metadata id="sesm">` block.

SESM lets an SVG remain a normal image while also carrying asset-level context: identity, provenance, theme meaning, UI hints, crawler hints, archive hints, integrity references, and language-model-readable summaries.

SESM is not an execution model. It is metadata.

## Problem

Visual assets often lose their context when they leave the page, build pipeline, database, or design system that produced them.

An SVG logo, badge, dataset card, dashboard panel, or generated documentation asset may be copied to a static site, mirrored by an archive, indexed by a crawler, or read by an agent. Without embedded context, the asset becomes harder to classify, verify, search, summarize, or rebuild.

Sidecar manifests can help, but sidecars are easy to separate from the image. Page-level structured data can help, but it does not travel with the asset. SESM addresses asset-level portability.

## Why SVG

SVG already has a standards-defined `<metadata>` element. It is text-based, portable, indexable, archivable, and commonly used for logos, diagrams, icons, interface elements, and generated visual artifacts.

SESM uses SVG because:

- the metadata can live inside the asset;
- the asset remains valid SVG;
- existing SVG renderers can ignore SESM safely;
- validators and build tools can parse the metadata without rendering the SVG;
- archives and mirrors can preserve one file instead of coordinating image-plus-sidecar bundles.

## Why Not JSON-LD Alone

JSON-LD is a strong fit for page-level and site-level semantics. SESM does not replace it.

JSON-LD alone is not enough for SESM's target use case because:

- JSON-LD usually lives in HTML, not inside the SVG asset;
- copied or downloaded SVGs can become separated from their page metadata;
- generated interface assets may need build, theme, provenance, or integrity details that are asset-specific;
- agents may inspect a standalone SVG file without the original page.

SESM can coexist with JSON-LD. A page can expose JSON-LD while each SVG carries its own portable asset-level metadata.

## Why Not Sidecar Files Alone

Sidecar files are useful when metadata is large, sensitive, frequently updated, or shared across many assets.

SESM does not replace sidecars. It handles the compact metadata that should survive when the SVG is copied, mirrored, archived, or inspected alone.

Use sidecars for large records, private records, access control, long histories, and operational state. Use SESM for public, asset-level, portable context.

## Use Cases

- Asset identity for logos, icons, badges, diagrams, cards, and generated panels.
- Provenance for generated SVG assets.
- Theme and design-system context for semantic colors and visual roles.
- Crawler and archival hints for asset-level indexing.
- LLM-readable summaries for agents that need to understand graphics without relying only on visual inference.
- Integrity references connecting an SVG to release or archive records.
- Build-pipeline validation for generated visual artifacts.

## Risks

SVG is an active-content-capable format. Arbitrary SVG files can contain unsafe features such as scripts, event handlers, remote references, and hidden payloads.

SESM does not make arbitrary SVG safe.

SESM metadata is untrusted input. Consumers must parse it as data, validate it, ignore unknown fields where appropriate, and never treat SESM text as executable instructions or authority.

The SESM safe profile is defined in `SAFE-PROFILE.md`.
The threat model is defined in `THREAT-MODEL.md`.

## Adoption Model

Adopters can begin with a minimal SESM block:

```json
{
  "sesm_version": "0.3.0",
  "asset": {
    "id": "example-logo",
    "role": "logo"
  }
}
```

Recommended adoption steps:

1. Embed a SESM block in selected non-executable SVG assets.
2. Validate the metadata against `svg_asset.schema.json`.
3. Validate the SVG against the safe profile when the asset is intended for broad ingestion.
4. Treat SESM as public metadata.
5. Document any extensions under `extra`.
6. Keep sidecar records for private, large, or operational metadata.

## Review Goals

External review should focus on:

- whether SESM's embedded metadata model is useful and appropriately scoped;
- whether the safe profile is clear enough for implementers;
- whether validator rules are practical;
- whether the schema vocabulary is too broad, too narrow, or missing common asset-level fields;
- whether the threat model is sufficient for crawler, archive, browser, and AI-agent consumers.
