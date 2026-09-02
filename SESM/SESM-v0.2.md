# SVG Embedded Semantic Metadata (SESM)

**Status:** Candidate v0.3.0
**Scope:** Asset-level semantic metadata, artifact provenance, theme instructions, crawler hints, LLM hints, and UI runtime hints embedded directly inside SVG files.

---

## 1. Overview

The **SVG Embedded Semantic Metadata (SESM)** standard defines a simple, implementation-agnostic way to embed structured metadata and instructions directly inside SVG assets.

SESM treats SVGs not only as images, but as:

- visual assets
- metadata carriers
- semantic capsules
- archive-friendly documentation units
- LLM-readable context packets
- UI runtime hints
- generated artifacts with provenance

For **Aptlantis Studio**, SESM is especially important because many visible interface components are expected to be **compiled SVG artifacts** generated from JSON or JSONL manifests.

In that model, an SVG can represent:

- a dataset card
- a pipeline status panel
- a theme board
- a stats panel
- a navigation artifact
- a dataset identity badge
- a crawler-facing semantic summary

The SVG remains a valid SVG image even if no system understands SESM. Agents that understand SESM can read the embedded JSON and use it to interpret, classify, render, crawl, index, archive, or summarize the asset more intelligently.

---

## 2. Design Philosophy

SESM is intentionally simple:

> Put a valid JSON object inside an SVG `<metadata>` element.

Everything else is convention.

This simplicity matters because SESM is designed to survive:

- static hosting
- mirroring
- scraping
- archival
- direct filesystem copying
- Internet Archive uploads
- local agent indexing
- page extraction
- build pipeline regeneration

SESM should be easy to generate from a small Rust, Go, Python, or JavaScript utility.

---

## 3. Goals

SESM is designed to:

1. Embed structured metadata directly in SVG assets.
2. Preserve useful semantic context even when an SVG is separated from its original page.
3. Provide crawler and archival hints without requiring agents to fetch large external documents.
4. Provide LLM-facing summaries and usage hints.
5. Provide UI runtime hints for cards, panels, datasets, themes, and generated interface components.
6. Support generated artifact provenance.
7. Support deterministic rebuild systems.
8. Work alongside JSON-LD, HTML metadata, manifests, and site maps.
9. Remain optional and safely ignorable.
10. Remain simple enough to hand-author or generate automatically.

---

## 4. Non-Goals

SESM is **not** intended to:

- Replace JSON-LD in HTML: Page-level semantics belong in the HTML body; SESM focuses strictly on asset-level semantics.
- Replace site maps or robots.txt: Crawlers must still respect the host platform's central policies; SESM only offers asset-specific guidelines.
- Define a complete ontology for all visual assets: It does not represent a universal taxonomy for all media files.
- Enforce rendering behavior: Display styles are determined by CSS and SVG vector attributes; SESM only carries metadata hints.
- Act as access control: It does not manage authentication, permissions, or access to assets.
- Contain secrets, credentials, private links, or internal-only data: All embedded data must be treated as public-facing.
- Require any specific AI, LLM, crawler, or frontend framework: It remains implementation-agnostic and accessible to any standard parser.
- Require JavaScript to be useful: The metadata is static XML CDATA and does not execute runtime scripts.
- Replace package manifests or code declarations: System configurations, source manifests, and code definitions are maintained independently.
- Provide real-time state synchronization: SESM is statically built into SVG files and is updated only during compilation/embedding.

SESM provides semantic hints, not mandates.

For public-review safety and adoption framing, see:

- `EXPLAINER.md`
- `SAFE-PROFILE.md`
- `THREAT-MODEL.md`
- `PRIVACY.md`
- `CONFORMANCE.md`
- `SECURITY.md`
- `VALIDATOR-RULES.md`
- `REFERENCE-IMPLEMENTATION.md`
- `SUBMISSION-PITCH.md`

SESM metadata is untrusted input. SESM does not make arbitrary SVG safe, and SESM metadata must not be treated as executable instructions or agent command authority.

---

## 5. Terminology

### SESM Block

A single JSON object embedded inside an SVG’s `<metadata>` element.

### Agent

Any automated system that reads the SVG or SESM block. Examples include crawlers, archive bots, LLMs, local indexing tools, asset classifiers, build validators, and UI runtimes.

### UI Runtime

A system that uses SESM metadata to decide how an asset should be styled, placed, grouped, rendered, or interpreted.

### Artifact

A generated or curated file with semantic meaning. In Aptlantis Studio, many SVGs are artifacts compiled from manifests.

### Host Platform

The site or system that stores, serves, or generates the SVG. Example: Aptlantis or Aptlantis Studio.

### Source Manifest

The JSON, JSONL, TOML, YAML, database record, or pipeline output that produced the SVG artifact.

---

## 6. SESM Block Structure

A SESM block is a single JSON object.

Only `sesm_version` is required.

Recommended top-level fields:

```json
{
  "sesm_version": "0.3.0",
  "asset": {},
  "artifact": {},
  "theme": {},
  "ui": {},
  "crawl": {},
  "llm": {},
  "links": {},
  "provenance": {},
  "integrity": {},
  "extra": {}
}
```

Agents must ignore unknown fields rather than failing.

---

## 7. Required Field

### 7.1 `sesm_version`

```json
{
  "sesm_version": "0.3.0"
}
```

The SESM specification version used by the block.

For this draft:

```json
"sesm_version": "0.3.0"
```

Future revisions should follow semantic versioning:

- MAJOR: breaking changes
- MINOR: additive optional fields
- PATCH: documentation or clarification changes

---

## 8. `asset`

The `asset` object describes what the SVG represents.

### 8.1 Recommended Fields

```json
{
  "asset": {
    "id": "rust-code-corpus-card",
    "role": "dataset-card",
    "title": "Rust Code Corpus",
    "description": "Dataset card for a Rust fine-tuning corpus.",
    "ecosystem": "rust",
    "tags": ["rust", "dataset", "small-models", "fine-tuning"]
  }
}
```

### 8.2 Recommended Roles

Common `asset.role` values:

- `logo`
- `icon`
- `theme-board`
- `dataset-card`
- `dataset-header`
- `pipeline-panel`
- `stats-panel`
- `navigation-card`
- `graph-node`
- `graph-panel`
- `status-badge`
- `download-card`
- `schema-card`
- `archive-summary`
- `landing-hero`
- `page-header`
- `decorative`
- `unknown`

Roles should be stable and lowercase, using hyphen-separated names.

### 8.3 Detailed Role Specification

#### `logo`
* **Purpose**: Primary visual branding asset representing an ecosystem, project, organization, or tool.
* **Key Fields**: `asset.ecosystem`, `links.homepage`, `links.canonical_html`.
* **Example**:
  ```json
  {
    "asset": {
      "id": "apt-caddy-logo",
      "role": "logo",
      "title": "Caddy Web Server Logo",
      "ecosystem": "caddy"
    }
  }
  ```

#### `icon`
* **Purpose**: Reusable UI glyph or graphical signifier.
* **Key Fields**: `ui.dimensions` (typically square), `ui.preferred_layout` = "icon".
* **Example**:
  ```json
  {
    "asset": {
      "id": "icon-search",
      "role": "icon",
      "title": "Search Icon"
    }
  }
  ```

#### `theme-board`
* **Purpose**: Visual presentation representing a semantic color system or color palette.
* **Key Fields**: `theme.id`, `theme.tokens`, `theme.semantic_families`.
* **Example**:
  ```json
  {
    "asset": {
      "id": "neon-ink-board",
      "role": "theme-board",
      "title": "Neon Ink Theme Board"
    }
  }
  ```

#### `dataset-card`
* **Purpose**: Self-describing graphical card representing a compiled dataset.
* **Key Fields**: `artifact.source_id`, `links.manifest`, `crawl.discover_paths`, `llm.summary`.
* **Example**:
  ```json
  {
    "asset": {
      "id": "rust-corpus-card",
      "role": "dataset-card",
      "title": "Rust Code Corpus Card"
    }
  }
  ```

#### `dataset-header`
* **Purpose**: Large visual header displaying a summary banner of a dataset.
* **Key Fields**: `asset.ecosystem`, `ui.dimensions`.

#### `pipeline-panel`
* **Purpose**: Status panel visualizing data pipeline flow, execution metrics, or system runtime.
* **Key Fields**: `theme.state`, `provenance.generated_at`, `provenance.reproducible`.

#### `stats-panel`
* **Purpose**: Dashboard component showcasing statistics, counts, or visual summaries.
* **Key Fields**: `llm.summary` (explaining the statistics), `links.api`.

#### `navigation-card`
* **Purpose**: Layout element pointing to other resources or site sections.
* **Key Fields**: `links.canonical_html`, `ui.interaction`.

#### `graph-node`
* **Purpose**: Element inside a graphical node-link network visualization.
* **Key Fields**: `links.api`, `extra.vendor`.

#### `graph-panel`
* **Purpose**: Container element wrapping a network graph layout.
* **Key Fields**: `ui.preferred_layout`, `ui.preferred_regions`.

#### `status-badge`
* **Purpose**: Inline indicator showing current operational or development state.
* **Key Fields**: `theme.state`, `ui.dimensions`.
* **Example**:
  ```json
  {
    "asset": {
      "id": "badge-verified",
      "role": "status-badge",
      "title": "Verified Status Badge"
    }
  }
  ```

#### `download-card`
* **Purpose**: Card summarizing dynamic download endpoints and checksum validation.
* **Key Fields**: `links.download`, `integrity.content_hash`.

#### `schema-card`
* **Purpose**: Visualization detailing data formats or API structure definitions.
* **Key Fields**: `links.docs`, `links.jsonld`.

#### `archive-summary`
* **Purpose**: Archival container file summary.
* **Key Fields**: `crawl.archive` = true, `crawl.notes`.

#### `landing-hero`
* **Purpose**: Large splash graphic welcoming users to a site or hub.
* **Key Fields**: `ui.responsive_behavior`, `asset.description`.

#### `page-header`
* **Purpose**: Header banner displaying branding context for a web page.
* **Key Fields**: `ui.preferred_regions`, `links.homepage`.

#### `decorative`
* **Purpose**: Purely aesthetic asset containing no core semantic value.
* **Key Fields**: `crawl.indexable` = false, `crawl.archive` = false.

#### `unknown`
* **Purpose**: Default placeholder value for unclassified assets.
* **Key Fields**: `sesm_version`.

---

## 9. `artifact`

The `artifact` object describes the SVG as an artifact in a generated system.

This is especially relevant for Aptlantis Studio, where SVGs may be compiled from dataset and theme manifests.

### 9.1 Example

```json
{
  "artifact": {
    "kind": "compiled-svg",
    "artifact_id": "dataset-card-rust-code-corpus",
    "source_type": "dataset_manifest",
    "source_id": "rust_code_corpus",
    "source_path": "/data/datasets.jsonl",
    "template_id": "dataset-card-v1",
    "template_path": "/templates/svg/dataset_card.svg.tmpl",
    "output_path": "/svg/datasets/rust_code_corpus.svg",
    "build_profile": "production"
  }
}
```

### 9.2 Recommended Fields

- `kind`: Type of artifact.
- `artifact_id`: Stable ID for the generated artifact.
- `source_type`: Type of source data.
- `source_id`: ID of the source record.
- `source_path`: Path to source manifest or input.
- `template_id`: Stable template name/version.
- `template_path`: Path to the template used.
- `output_path`: Expected output location.
- `build_profile`: e.g. `dev`, `preview`, `production`.

---

## 10. `theme`

The `theme` object describes the visual theme and semantic color mapping used by the SVG.

For Aptlantis Studio, palette semantics come from `NIPC—NeonInkPaletteContract.md`, artifact rendering rules come from `AIC-v0.1-Aptlantis-Studio.md`, and brand expression comes from `NeonInk-v0.1-Aptlantis-Studio.md`. SESM remains the embedded metadata carrier; it does not make NIPC or AIC fields mandatory for every SVG.

### 10.1 Example

```json
{
  "theme": {
    "id": "neon-ink",
    "name": "Neon Ink",
    "version": "0.1.0",
    "palette_contract": "nipc-0.1",
    "mode": "dark",
    "accent": {
      "name": "code-heat",
      "hex": "#F97316",
      "semantic_role": "code-heat",
      "semantic_family": "creation-build-code",
      "psychological_intent": "signal-hands-on-code-build-work"
    },
    "state": {
      "name": "active",
      "intensity": 2,
      "glow": "soft",
      "priority": "medium"
    },
    "tokens": {
      "background": "#0B0F1A",
      "panel": "#111827",
      "text": "#E5E7EB",
      "muted": "#94A3B8",
      "info": "#22D3EE",
      "process": "#A78BFA",
      "featured": "#F472B6",
      "success": "#34D399",
      "important": "#FACC15",
      "critical": "#F43F5E",
      "code_heat": "#F97316"
    }
  }
}
```

### 10.2 Semantic Color Roles

SESM examples may use these NIPC-aligned roles. This list is recommended for Aptlantis Studio, not a universal SESM requirement.

| Family | Example Roles | Meaning |
|---|---|---|
| Clarity / Orientation | `info`, `structure`, `navigation`, `reference`, `orientation` | Understanding, wayfinding, docs |
| Trust / Validation | `success`, `verified`, `stable`, `reproducible`, `available` | Evidence-backed confidence |
| Attention | `important`, `note`, `caution`, `decision`, `memory-anchor` | Pause, notice, remember |
| Risk / Constraint | `critical`, `error`, `blocked`, `constraint`, `deprecated` | Failure, blocker, hard limit |
| Process / Transformation | `process`, `pipeline`, `transform`, `automation`, `orchestration` | Flow, generation, system mechanics |
| Creation / Build / Code | `code-heat`, `build`, `operation`, `artifact-output`, `tooling` | Rust, execution, generated output |
| Discovery / Creative | `featured`, `creative`, `discovery`, `spotlight`, `human-note` | Featured, expressive, exploratory |
| Research / Experimental | `experimental`, `research`, `prototype`, `hypothesis`, `unstable` | Not fully settled yet |
| Canonical / Archive / Neutral | `canonical`, `archive`, `muted`, `unknown`, `baseline` | Definitions, history, quiet metadata |

### 10.3 Recommended Dataset States

Common `theme.state.name` values:

- `idle`
- `active`
- `running`
- `featured`
- `complete`
- `verified`
- `warning`
- `error`
- `archived`
- `experimental`
- `deprecated`

---

## 11. `ui`

The `ui` object provides hints for runtime placement and layout.

These are hints, not requirements.

### 11.1 Example

```json
{
  "ui": {
    "component_type": "panel",
    "preferred_layout": "artifact-card",
    "preferred_regions": ["datasets", "rust", "featured"],
    "avoid_regions": ["internal-admin-only"],
    "responsive_behavior": "preserve-aspect-ratio",
    "interaction": {
      "click_target": "canonical_html",
      "hover_behavior": "show-metadata",
      "supports_focus": true
    },
    "dimensions": {
      "width": 600,
      "height": 220,
      "aspect_ratio": "30:11"
    }
  }
}
```

### 11.2 Recommended Fields

- `component_type`: e.g. `panel`, `card`, `badge`, `hero`, `graph-node`.
- `preferred_layout`: e.g. `artifact-card`, `logo-left-text-right`, `centered`.
- `preferred_regions`: Logical site regions where this asset belongs.
- `avoid_regions`: Regions where this asset should not appear.
- `responsive_behavior`: e.g. `preserve-aspect-ratio`, `crop-safe`, `scale-to-fit`.
- `interaction`: Suggested behavior for UI runtimes.
- `dimensions`: Intended dimensions and aspect ratio.

---

## 12. `crawl`

The `crawl` object provides indexing and archival hints.

### 12.1 Example

```json
{
  "crawl": {
    "indexable": true,
    "archive": true,
    "notes": "This dataset card and related paths may be freely crawled and archived.",
    "discover_paths": [
      "/datasets/rust-code-corpus",
      "/data/datasets.jsonl",
      "/api/datasets/rust-code-corpus.json"
    ],
    "canonical_group": "datasets"
  }
}
```

### 12.2 Recommended Fields

- `indexable`: Whether the asset is intended to be indexed.
- `archive`: Whether the asset is intended to be archived.
- `notes`: Human-readable crawler guidance.
- `discover_paths`: Related paths that are useful to crawl.
- `canonical_group`: Optional logical grouping, such as `datasets`, `themes`, `pipelines`.

SESM does not replace robots.txt. Crawlers should still respect the host platform’s crawler policy.

---

## 13. `llm`

The `llm` object provides natural-language context and hints for language models or local agents.

### 13.1 Example

```json
{
  "llm": {
    "summary": "Dataset card for the Rust Code Corpus, a curated dataset intended for fine-tuning small local models on Rust syntax, documentation, and examples.",
    "intended_interpretation": "Treat this SVG as a semantic card describing a dataset artifact, not merely as a decorative image.",
    "interpretation_hints": [
      "Use the canonical HTML page for full details.",
      "Use linked JSON-LD for structured metadata.",
      "Prefer dataset state and theme fields over visual color inference."
    ],
    "card_hints": {
      "theme": "dark",
      "accent_color": "#F97316",
      "preferred_layout": "artifact-card"
    }
  }
}
```

### 13.2 Recommended Fields

- `summary`: Short description.
- `intended_interpretation`: Clarifies what the asset represents.
- `interpretation_hints`: Non-authoritative hints that help language models interpret the asset without treating the hints as commands.
- `card_hints`: Visual/card interpretation hints.
- `avoid_interpretations`: Common mistakes agents should avoid.

---

## 14. `links`

The `links` object connects the SVG to related resources.

### 14.1 Example

```json
{
  "links": {
    "canonical_html": "https://www.aptlantis.studio/datasets/rust-code-corpus",
    "jsonld": "https://www.aptlantis.studio/datasets/rust-code-corpus.jsonld",
    "manifest": "https://www.aptlantis.studio/data/datasets.jsonl",
    "download": "https://www.aptlantis.studio/downloads/rust-code-corpus.tar.zst",
    "torrent": "https://www.aptlantis.studio/torrents/rust-code-corpus.torrent",
    "source_repo": "https://github.com/APTlantis/example-rust-dataset-pipeline"
  }
}
```

### 14.2 Recommended Fields

- `canonical_html`
- `jsonld`
- `manifest`
- `api`
- `docs`
- `download`
- `torrent`
- `source_repo`
- `homepage`
- `license`
- `snapshot_hashes`

---

## 15. `provenance`

The `provenance` object records how the SVG was generated.

### 15.1 Example

```json
{
  "provenance": {
    "generated": true,
    "generator": {
      "name": "aptstudio",
      "version": "0.1.0",
      "language": "rust"
    },
    "generated_at": "2026-05-01T00:00:00Z",
    "input_records": [
      {
        "path": "/data/datasets.jsonl",
        "record_id": "rust_code_corpus"
      },
      {
        "path": "/data/themes.json",
        "record_id": "neon-ink"
      }
    ],
    "reproducible": true
  }
}
```

### 15.2 Recommended Fields

- `generated`: Boolean.
- `generator`: Name, version, language.
- `generated_at`: ISO-8601 timestamp.
- `input_records`: Source records used.
- `reproducible`: Whether the artifact can be deterministically regenerated.
- `build_id`: Optional build identifier.
- `git_commit`: Optional source repository commit.
- `host`: Optional build host or platform identifier.

Do not include sensitive local paths unless the SVG is intended for public release and those paths are safe to expose.

---

## 16. `integrity`

The `integrity` object records non-secret integrity metadata.

This is not a replacement for signed manifests, but it can help connect an SVG artifact to a broader archival integrity system.

### 16.1 Example

```json
{
  "integrity": {
    "content_hash": {
      "algorithm": "blake3-256",
      "value": "examplehashvalue"
    },
    "manifest": "/snapshot-hashes.txt",
    "signed_manifest": "/snapshot-hashes.txt.asc"
  }
}
```

### 16.2 Recommended Fields

- `content_hash`: Hash of the SVG or source record.
- `manifest`: Path to a hash manifest.
- `signed_manifest`: Path to signed hash manifest.
- `signature`: Optional detached signature path.
- `verification_notes`: Human-readable verification guidance.

Avoid embedding signatures so large that they make the SVG difficult to work with. Prefer linking to signed manifests when appropriate.

---

## 17. `extra`

The `extra` object is a namespace for platform-specific extensions.

### 17.1 Example

```json
{
  "extra": {
    "vendor": {
      "aptlantis": {
        "schema_id": "DatasetCard",
        "schema_version": "1.0.0",
        "platform": "aptlantis-studio",
        "domain": "www.aptlantis.studio"
      }
    }
  }
}
```

Vendor extensions should be namespaced to avoid collisions.

Recommended pattern:

```json
{
  "extra": {
    "vendor": {
      "organization_or_platform_name": {}
    }
  }
}
```

---

## 18. Embedding SESM in SVG

### 18.1 Location

SESM metadata must be embedded inside an SVG `<metadata>` element.

Recommended form:

```xml
<metadata id="sesm"><![CDATA[
{
  "sesm_version": "0.3.0"
}
]]></metadata>
```

### 18.2 Raw JSON Form

Raw JSON is acceptable when the toolchain preserves it safely:

```xml
<metadata id="sesm">
{
  "sesm_version": "0.3.0"
}
</metadata>
```

### 18.3 CDATA Form

CDATA is recommended when:

- templates are processed by XML-aware tools
- special characters may appear in JSON strings
- maximum preservation is desired

```xml
<metadata id="sesm"><![CDATA[
{
  "sesm_version": "0.3.0",
  "asset": {
    "role": "dataset-card"
  }
}
]]></metadata>
```

### 18.4 Requirements

- The `<metadata>` element should use `id="sesm"`.
- The contents should be valid JSON text.
- Only one SESM JSON object should be present per SVG.
- If multiple SESM blocks are present, agents may parse the first and ignore the rest.
- Agents must ignore unknown fields.
- Agents must not fail because optional fields are missing.

---

## 19. Minimal Example

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <metadata id="sesm"><![CDATA[
{
  "sesm_version": "0.3.0"
}
  ]]></metadata>

  <circle cx="50" cy="50" r="40" fill="#22D3EE"/>
</svg>
```

This SVG is SESM-aware even though it only declares a version.

---

## 20. Aptlantis Studio Dataset Card Example

```xml
<svg xmlns="http://www.w3.org/2000/svg" width="600" height="220" viewBox="0 0 600 220">
  <metadata id="sesm"><![CDATA[
{
  "sesm_version": "0.3.0",
  "asset": {
    "id": "rust-code-corpus-card",
    "role": "dataset-card",
    "title": "Rust Code Corpus",
    "description": "Dataset card for a Rust fine-tuning corpus.",
    "ecosystem": "rust",
    "tags": ["rust", "dataset", "small-models", "fine-tuning"]
  },
  "artifact": {
    "kind": "compiled-svg",
    "artifact_id": "dataset-card-rust-code-corpus",
    "source_type": "dataset_manifest",
    "source_id": "rust_code_corpus",
    "source_path": "/data/datasets.jsonl",
    "template_id": "dataset-card-v1",
    "template_path": "/templates/svg/dataset_card.svg.tmpl",
    "output_path": "/svg/datasets/rust_code_corpus.svg",
    "build_profile": "production"
  },
  "theme": {
    "id": "neon-ink",
    "name": "Neon Ink",
    "version": "0.1.0",
    "palette_contract": "nipc-0.1",
    "mode": "dark",
    "accent": {
      "name": "code-heat",
      "hex": "#F97316",
      "semantic_role": "code-heat",
      "semantic_family": "creation-build-code",
      "psychological_intent": "signal-hands-on-code-build-work"
    },
    "state": {
      "name": "active",
      "intensity": 2,
      "glow": "soft",
      "priority": "medium"
    }
  },
  "ui": {
    "component_type": "panel",
    "preferred_layout": "artifact-card",
    "preferred_regions": ["datasets", "rust"],
    "responsive_behavior": "preserve-aspect-ratio",
    "interaction": {
      "click_target": "canonical_html",
      "hover_behavior": "show-metadata",
      "supports_focus": true
    },
    "dimensions": {
      "width": 600,
      "height": 220,
      "aspect_ratio": "30:11"
    }
  },
  "crawl": {
    "indexable": true,
    "archive": true,
    "notes": "This dataset card and related Rust dataset pages may be freely crawled and archived.",
    "discover_paths": [
      "/datasets/rust-code-corpus",
      "/data/datasets.jsonl"
    ],
    "canonical_group": "datasets"
  },
  "llm": {
    "summary": "Dataset card for the Rust Code Corpus, a curated dataset intended for fine-tuning small local models on Rust syntax, documentation, examples, and crate metadata.",
    "intended_interpretation": "Treat this SVG as a semantic card describing a dataset artifact, not merely as a decorative image.",
    "interpretation_hints": [
      "Use the canonical HTML page for full details.",
      "Use linked manifests for structured metadata.",
      "Prefer SESM state fields over visual color inference."
    ],
    "card_hints": {
      "theme": "dark",
      "accent_color": "#F97316",
      "preferred_layout": "artifact-card"
    }
  },
  "links": {
    "canonical_html": "https://www.aptlantis.studio/datasets/rust-code-corpus",
    "manifest": "https://www.aptlantis.studio/data/datasets.jsonl"
  },
  "provenance": {
    "generated": true,
    "generator": {
      "name": "aptstudio",
      "version": "0.1.0",
      "language": "rust"
    },
    "generated_at": "2026-05-01T00:00:00Z",
    "input_records": [
      {
        "path": "/data/datasets.jsonl",
        "record_id": "rust_code_corpus"
      },
      {
        "path": "/data/themes.json",
        "record_id": "neon-ink"
      }
    ],
    "reproducible": true
  },
  "extra": {
    "vendor": {
      "aptlantis": {
        "schema_id": "DatasetCard",
        "schema_version": "1.0.0",
        "platform": "aptlantis-studio",
        "domain": "www.aptlantis.studio"
      }
    }
  }
}
  ]]></metadata>

  <rect width="600" height="220" rx="18" fill="#0B0F1A"/>
  <rect x="0" y="0" width="600" height="4" fill="#F97316"/>
  <text x="24" y="58" fill="#E5E7EB" font-size="28" font-family="monospace">Rust Code Corpus</text>
  <text x="24" y="96" fill="#94A3B8" font-size="15" font-family="monospace">Small-model fine-tuning dataset</text>
</svg>
```

---

## 21. Aptlantis Studio Theme Board Example

```json
{
  "sesm_version": "0.3.0",
  "asset": {
    "id": "neon-ink-theme-board",
    "role": "theme-board",
    "title": "Neon Ink Theme Board",
    "tags": ["theme", "palette", "neon-ink", "aptlantis-studio"]
  },
  "theme": {
    "id": "neon-ink",
    "name": "Neon Ink",
    "version": "0.1.0",
    "palette_contract": "nipc-0.1",
    "mode": "dark",
    "tokens": {
      "void": "#050816",
      "base": "#0B0F1A",
      "panel": "#111827",
      "info": "#22D3EE",
      "process": "#A78BFA",
      "featured": "#F472B6",
      "success": "#34D399",
      "important": "#FACC15",
      "critical": "#F43F5E",
      "code_heat": "#F97316",
      "text": "#E5E7EB",
      "muted": "#94A3B8"
    },
    "semantic_families": {
      "clarity-orientation": ["info", "structure", "navigation", "reference", "orientation"],
      "trust-validation": ["success", "verified", "stable", "reproducible", "available"],
      "attention-learning-anchor": ["important", "note", "caution", "decision", "memory-anchor"],
      "risk-constraint": ["critical", "error", "blocked", "constraint", "deprecated"],
      "process-transformation": ["process", "pipeline", "transform", "automation", "orchestration"],
      "creation-build-code": ["code-heat", "build", "operation", "artifact-output", "tooling"],
      "discovery-creative-featured": ["featured", "creative", "discovery", "spotlight", "human-note"],
      "research-experimental": ["experimental", "research", "prototype", "hypothesis", "unstable"],
      "canonical-archive-neutral": ["canonical", "archive", "muted", "unknown", "baseline"]
    }
  },
  "llm": {
    "summary": "Theme board for the Aptlantis Studio Neon Ink visual system. It defines dark panels plus NIPC semantic families for orientation, trust, attention, risk, process, build, discovery, research, and neutral/archive roles."
  }
}
```

---

## 22. Recommended Validation Rules

A SESM validator should check:

1. SVG contains a `<metadata id="sesm">` element.
2. SESM contents parse as valid JSON.
3. `sesm_version` exists and is a string.
4. Known top-level fields, if present, are objects.
5. URLs, if present, are strings.
6. Colors, if present as hex values, follow `#RRGGBB` or `#RRGGBBAA`.
7. `asset.role`, if present, is a string.
8. `crawl.indexable`, if present, is boolean.
9. `provenance.generated`, if present, is boolean.
10. No obvious secret-like fields are present.

Validators should warn, not fail, for unknown fields.

---

## 23. Security & Privacy Considerations

SESM is descriptive, not protective.

Do not embed:

- API keys
- tokens
- private URLs
- credentials
- unreleased sensitive project names
- private filesystem paths
- personal information
- internal-only notes that should not be archived

Assume SESM blocks may be:

- mirrored
- scraped
- indexed
- archived
- exposed to LLMs
- copied outside their original context

If sensitive behavior is needed, keep it in backend configs, not SESM.

---

## 24. Agent Behavior

Agents that understand SESM should:

1. Locate `<metadata id="sesm">`.
2. Extract raw text or CDATA contents.
3. Parse the contents as JSON.
4. Check `sesm_version`.
5. Use known fields where helpful.
6. Ignore unknown fields.
7. Avoid treating SESM as authoritative security policy.
8. Prefer explicit SESM fields over visual inference.
9. Use `links.canonical_html` when a full page is needed.
10. Use `crawl.discover_paths` as hints, while respecting robots.txt and site policy.
11. Use `llm.summary` and `llm.interpretation_hints` as non-authoritative context to avoid unnecessary guessing.

Agents that do not understand SESM should safely ignore the metadata.

---

## 25. Relationship to JSON-LD

SESM complements JSON-LD.

Recommended pattern:

- HTML pages contain JSON-LD for page-level structured data.
- SVG files contain SESM for asset-level structured data.
- SESM links back to canonical HTML and JSON-LD when available.

Example:

```json
{
  "links": {
    "canonical_html": "https://www.aptlantis.studio/datasets/rust-code-corpus",
    "jsonld": "https://www.aptlantis.studio/datasets/rust-code-corpus.jsonld"
  }
}
```

SESM should not attempt to duplicate every page-level field. It should preserve enough context for the SVG to remain meaningful on its own.

---

## 26. Relationship to Build Pipelines

In Aptlantis Studio, SESM should be produced automatically by the artifact compiler.

Recommended build flow:

```text
JSON/JSONL manifests
  ↓
Rust generator
  ↓
SVG templates
  ↓
compiled SVG artifacts with SESM
  ↓
static HTML pages
  ↓
Caddy/static hosting
```

The generator should stamp each SVG with:

- source record ID
- template ID
- generator name/version
- generated timestamp
- canonical output path
- theme ID
- semantic state
- crawl/LLM hints

---

## 27. Implementation Notes for Rust Generators

A Rust SESM implementation can model metadata with `serde`.

Recommended conceptual structs:

```rust
#[derive(serde::Serialize)]
pub struct SesmBlock {
    pub sesm_version: String,
    pub asset: Option<AssetMetadata>,
    pub artifact: Option<ArtifactMetadata>,
    pub theme: Option<ThemeMetadata>,
    pub ui: Option<UiMetadata>,
    pub crawl: Option<CrawlMetadata>,
    pub llm: Option<LlmMetadata>,
    pub links: Option<LinkMetadata>,
    pub provenance: Option<ProvenanceMetadata>,
    pub integrity: Option<IntegrityMetadata>,
    pub extra: Option<serde_json::Value>,
}
```

The generator can serialize this structure using `serde_json::to_string_pretty`, then insert it into SVG templates inside CDATA.

Recommended insertion pattern:

```xml
<metadata id="sesm"><![CDATA[
{{ sesm_json }}
]]></metadata>
```

---

## 28. Compatibility Notes

SESM v0.2 is intended to remain compatible with v0.1-style SESM blocks.

A minimal v0.1-style block:

```json
{
  "sesm_version": "0.1.0",
  "asset": {
    "role": "logo"
  },
  "llm": {
    "summary": "Logo used for ecosystem cards."
  }
}
```

Should remain understandable to v0.2-aware agents.

Agents should not require every v0.2 field to be present.

---

## 29. Recommended File Naming

Suggested filename patterns:

```text
/svg/datasets/{dataset_id}.svg
/svg/pipelines/{pipeline_id}.svg
/svg/themes/{theme_id}-theme-board.svg
/svg/stats/{stats_id}.svg
```

Generated SVGs should use stable IDs so URLs remain durable.

---

## 30. Summary

SESM is an intentionally simple metadata convention for SVG files:

> A valid JSON object embedded inside `<metadata id="sesm">`.

For Aptlantis Studio, SESM gives generated SVGs a second life as:

- visual components
- structured metadata capsules
- crawler-friendly assets
- LLM-readable context documents
- archive-ready artifacts
- reproducible outputs from dataset pipelines

SESM works best when paired with:

- JSON/JSONL manifests
- deterministic Rust/Go generators
- static HTML pages
- JSON-LD
- signed manifests and archive hashes

The result is a visual system where SVGs are not just images.

They are self-describing artifacts.
