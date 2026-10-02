# Current reference images

These three 1440 × 960 composition boards belong to NeonInk 0.2.0. SVGs are generated from current tokens and `examples/reference-data.json`; PNGs are rendered previews. All data are synthetic and visibly labeled. They replace the former website/manga art direction for current work.

| Reference | Purpose | Files |
| --- | --- | --- |
| Analytical report | Zero-based category comparison, interpretation, caveat and source | [SVG](boards/Analytical-Report.svg) · [PNG](boards/Analytical-Report.png) |
| Dataset profile | Counts, schema, unknown validation and provenance | [SVG](boards/Dataset-Profile.svg) · [PNG](boards/Dataset-Profile.png) |
| Color scale guide | Categorical, sequential and diverging semantics | [SVG](boards/Color-Scale-Guide.svg) · [PNG](boards/Color-Scale-Guide.png) |

Rebuild SVGs with `python tools/render_references.py`, then render each SVG with ImageMagick at its native size (for example `magick input.svg output.png`). The Python script needs no image dependencies. PNG font rendering is host-dependent and not part of exact-byte SVG freshness checks. Inspect previews after regeneration; do not infer visual correctness from successful rasterization alone.

Use [the HTML specimen](../../examples/presentation.html) for a responsive chart/table reading surface. The boards demonstrate composition and data ethics, not a complete component kit, production dashboard, or proof of accessible behavior in every host.
