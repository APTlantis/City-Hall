# Neon Ink v0.1

**Status:** Draft v0.1  
**Host System:** Aptlantis Studio  
**Scope:** Whole-brand visual and semantic design standard for website UI, generated SVG artifacts, SESM metadata, Tailwind/CSS tokens, Canva assets, presentations, social graphics, and future marketing surfaces.

---

## 1. Overview

<p align="center">
  <img src="../assets/mindmaps/NeonInk-Mindmap.png" alt="Neon Ink System Mindmap" width="700">
</p>

**Neon Ink** is the governing design standard for Aptlantis Studio.

```mermaid
%%{init: {"theme": "base"}}%%
graph TD

A[Neon Ink Design System]

A --> B[Design Pillars]
A --> C[Semantic Color Taxonomy]
A --> D[Background Hierarchy]
A --> E[Interface Grammar]
A --> F[Technical Integration]
A --> G[Typography]

classDef root fill:#0B0F1A,stroke:#22D3EE,color:#E5E7EB,stroke-width:2px;
classDef cyan fill:#0F172A,stroke:#22D3EE,color:#22D3EE;
classDef violet fill:#0F172A,stroke:#A78BFA,color:#A78BFA;
classDef magenta fill:#0F172A,stroke:#F472B6,color:#F472B6;
classDef green fill:#0F172A,stroke:#34D399,color:#34D399;

class A root;
class B,C cyan;
class D,E violet;
class F,G magenta;
```

It defines how the Studio should look, read, behave, and describe itself across:

- static website pages
- generated HTML
- compiled SVG panels
- SESM metadata blocks
- dataset and pipeline cards
- theme boards
- documentation pages
- Canva brand assets
- slide decks
- social and promotional graphics
- future brand surfaces

Neon Ink is not only a color palette. It is an artifact-driven interface standard.

Its core rule is:

> Visuals are derived from the data.

The website, SVGs, cards, theme boards, and marketing surfaces should feel like parts of the same durable archive: static enough to last, structured enough to regenerate, and expressive enough to make datasets worth exploring.

---

## 2. Source Map

This v0.1 specification synthesizes the current Aptlantis Studio materials into one canonical standard.

Reference categories used:

- **SESM precedent:** `SESM-v0.2-Aptlantis-Studio.md`
- **Palette contract:** `NIPC—NeonInkPaletteContract.md`
- **Brand guidelines:** `aptlantis_studio_brand_guidelines.pdf`
- **Neon Ink system docs:** design manual, roadmap, taxonomy expansion, and tag theme notes
- **Implementation notes:** CSS/Tailwind token docs and component pattern examples
- **Raw artifact examples:** SVG panel XML with embedded SESM metadata
- **Visual references:** web mockups, theme panels, infographics, logo panels, and latest HTML screenshots

When these sources conflict, this spec resolves the conflict by best synthesis. It chooses the rule that is clearest, most reusable, most compatible with SESM, and most useful for building final Aptlantis Studio pages.

---

## 3. Status & Scope

### 3.1 Status

This is the first canonical Neon Ink document.

From v0.1 forward, new final pages and brand assets should follow this spec unless a named theme variant explicitly overrides part of it.

### 3.2 In Scope

Neon Ink governs:

- color roles and semantic tokens
- typography roles
- panel and component grammar
- page composition
- dataset and pipeline visualization
- SESM theme requirements
- brand voice and content language
- brand collateral such as Canva templates, social posts, and presentations

### 3.3 Out of Scope

Neon Ink does not:

- replace SESM
- define a full dataset schema
- define Rust generator internals
- define access control, crawler policy, or licensing policy
- require one frontend framework
- require all artifacts to be SVG
- require marketing graphics to expose private build metadata

Neon Ink provides whole-brand expression and page/component grammar. NIPC provides canonical palette semantics. SESM provides embedded metadata conventions.

---

## 4. Design Philosophy

### 4.1 Signal Over Scale

Aptlantis Studio exists for high-signal datasets, focused pipelines, and small specialist models. Neon Ink should make that philosophy visible.

The interface must prioritize recognition, status, provenance, and reproducibility over decorative novelty.

### 4.2 Local-First Durability

Studio artifacts should remain meaningful when copied, mirrored, archived, screenshotted, or viewed outside the original website.

Generated SVGs should carry semantic context through SESM. Static pages should expose visible metadata where trust matters.

### 4.3 Panels As Artifacts

The default component model is not a generic dashboard card.

It is an artifact panel:

| Element | Meaning |
|---|---|
| Panel | Artifact container |
| Border/accent | Artifact type or classification |
| Glow | State or activity |
| Badge | Short state, role, or dataset class |
| Metadata | Trust, provenance, and scanability |
| Link/action | Canonical destination or next operation |

### 4.4 Dataset-First Publishing

Aptlantis Studio is a dataset and pipeline workshop before it is a model showcase.

Pages should answer:

- What is this dataset?
- What is it for?
- What produced it?
- What state is it in?
- What does it contain?
- What licenses or constraints matter?
- How can it be downloaded, inspected, reproduced, or extended?

### 4.5 Welcoming Technicality

Neon Ink should feel technical without becoming hostile or obscure.

The voice is precise, inventive, durable, and builder-friendly. It should avoid corporate AI hype and vague claims.

---

## 5. Terminology

### Artifact

A generated or curated unit with semantic meaning. Examples: dataset card, pipeline panel, SVG header, theme board, download card, release summary, or social asset.

### Artifact Panel

A visual container that presents one artifact and exposes its type, state, metadata, and destination.

### Semantic Role

A named meaning mapped to an NIPC color token, such as `info`, `pipeline`, `memory-anchor`, `verified`, `constraint`, or `code-heat`.

### Semantic Family

An NIPC color family that groups related roles by cognitive purpose, such as clarity/orientation, trust/validation, attention, risk, process, build/code, discovery, research, or neutral/archive.

### Psychological Intent

The reason a semantic role was chosen, written for future generators, validators, and agents. Examples: `orient-the-user`, `explain-system-flow`, `create-confidence`, or `mark-risk-before-proceeding`.

### State

The current activity or reliability condition of an artifact, such as `idle`, `active`, `running`, `featured`, `complete`, `verified`, `warning`, `error`, `archived`, or `experimental`.

### Theme Variant

A named visual subtheme that inherits Neon Ink rules while adjusting accent emphasis for a subject area. Example: Dungeon Synth.

### SESM Block

A JSON object embedded in an SVG `<metadata>` element according to SESM v0.2.0.

### Brand Surface

Any public-facing material that presents Aptlantis Studio, including the website, Canva graphics, presentations, social posts, screenshots, and exported images.

---

## 6. Brand Foundation

### 6.1 Position

Aptlantis Studio creates and publishes unique, niche, practical, and creative datasets for fine-tuning small local models.

It is not a massive scrape marketplace. It is a focused workshop for reproducible, human-sized model building.

### 6.2 Audience

Primary audiences:

- hobbyist model builders
- local AI experimenters
- dataset curators
- archivists and researchers
- creative tool makers
- developers building small specialist models

### 6.3 Personality

Neon Ink should feel:

- **Inventive:** experimental and future-facing
- **Durable:** archive-aware, reproducible, and local-first
- **Welcoming:** builder-friendly, not corporate
- **Precise:** clear about data, schemas, licenses, and build state
- **Expressive:** manga/cyberpunk energy without sacrificing scanability

### 6.4 Core Phrases

Preferred campaign language:

- Unique datasets.
- Real worlds.
- Local power.
- Build small. Train local. Create worlds.
- High-signal datasets for small specialist models.
- Compiled artifacts for reproducible local training.

---

## 7. Color & Token System

### 7.1 Background Layers

The background system creates depth through value shifts, not heavy chrome.

| Token | Hex | Role |
|---|---:|---|
| `--studio-void` | `#050816` | Deep baseline canvas |
| `--studio-base` | `#0B0F1A` | Page baseline and primary surface |
| `--studio-panel` | `#111827` | Artifact container |
| `--studio-raised` | `#162033` | Raised or emphasized panel layer |
| `--studio-soft` | `#0F172A` | Soft secondary panel layer |

Use the Void as the outermost environment. Use Base for main page regions. Use Panel for artifact containers.

### 7.2 Text Tokens

| Token | Hex | Role |
|---|---:|---|
| `--studio-text` | `#E5E7EB` | Primary text |
| `--studio-text-secondary` | `#CBD5E1` | Secondary text |
| `--studio-muted` | `#94A3B8` | Metadata and supporting text |
| `--studio-faint` | `#64748B` | Quiet timestamps, IDs, and low-priority labels |
| `--studio-inverse` | `#050816` | Text on bright neon fills |

### 7.3 NIPC Authority

NIPC is the canonical palette layer for Neon Ink. This document may summarize palette behavior, but final token names, color families, psychological intent, intensity rules, and palette validation come from `NIPC—NeonInkPaletteContract.md`.

```mermaid
graph TD

A[Semantic Color Taxonomy]

A --> B[Primary Layer]
A --> C[Specialized Classification]
A --> D[Expressive Layer]
A --> E[Intensity Scale]

B --> B1[Neon Cyan<br/>Structure]
B --> B2[Neon Violet<br/>Process]
B --> B3[Neon Magenta<br/>Discovery]

C --> C1[Neon Orange<br/>Code-Heat]
C --> C2[Neon Green<br/>Trust]
C --> C3[Neon Yellow<br/>Attention]
C --> C4[Neon Red<br/>Risk]

D --> D1[Deep Blue<br/>Advanced]
D --> D2[Electric Indigo<br/>Experimental]
D --> D3[Neon White<br/>Canonical]
D --> D4[Slate/Gray<br/>Archive]

E --> E1[0 Muted]
E --> E2[1 Whisper]
E --> E3[2 Soft]
E --> E4[3 Active]
E --> E5[4 Urgent]
E --> E6[5 Interrupt]

%% Classes
classDef cyan fill:#0F172A,stroke:#22D3EE,color:#22D3EE;
classDef violet fill:#0F172A,stroke:#A78BFA,color:#A78BFA;
classDef magenta fill:#0F172A,stroke:#F472B6,color:#F472B6;
classDef orange fill:#0F172A,stroke:#F97316,color:#F97316;
classDef green fill:#0F172A,stroke:#34D399,color:#34D399;
classDef yellow fill:#0F172A,stroke:#FACC15,color:#FACC15;
classDef red fill:#0F172A,stroke:#F43F5E,color:#F43F5E;
classDef neutral fill:#111827,stroke:#64748B,color:#CBD5E1;

class B1 cyan;
class B2 violet;
class B3 magenta;

class C1 orange;
class C2 green;
class C3 yellow;
class C4 red;

class D1,D2,D3,D4 neutral;
class E1,E2,E3,E4,E5,E6 neutral;
```

Use this four-layer model:

| Layer | Canonical Document | Responsibility |
|---|---|---|
| Meaning | `SESM-v0.2-Aptlantis-Studio.md` | Embedded metadata, identity, provenance, links, agent hints |
| Palette | `NIPC—NeonInkPaletteContract.md` | Hue, semantic family, psychological intent, intensity validation |
| Contract | `AIC-v0.1-Aptlantis-Studio.md` | Artifact type, required fields, layout, render targets |
| Expression | `NeonInk-v0.1-Aptlantis-Studio.md` | Brand system, typography, panel grammar, page composition |

Core rule:

> Color should reduce cognitive load before it adds beauty.

### 7.4 Core Stable Tokens

The original Neon Ink tags remain the stable base. NIPC expands them into families rather than replacing them.

| Core Token | Hex | NIPC Family | Primary Use |
|---|---:|---|---|
| `info` | `#22D3EE` | Clarity / Orientation | General info, calm understanding |
| `process` | `#A78BFA` | Process / Transformation | Pipelines, how-it-works, system flow |
| `featured` | `#F472B6` | Discovery / Creative | Featured, creative, spotlight content |
| `success` | `#34D399` | Trust / Validation | Validated, good, evidence-backed pass |
| `important` | `#FACC15` | Attention / Learning Anchor | Caveats, notes, memory anchors |
| `critical` | `#F43F5E` | Risk / Constraint | Risk, blocker, failure, urgency |
| `code-heat` | `#F97316` | Creation / Build / Code | Rust, build, execution, artifact output |
| `experimental` | `#818CF8` | Research / Experimental | Prototype, research, unsettled work |
| `canonical` | `#E5E7EB` | Canonical / Archive / Neutral | Definitions, schemas, anchor text |

### 7.5 Dataset Accent Language

Dataset accents describe subject matter, not global state.

| Dataset Accent | Primary Token | Use |
|---|---|---|
| Rust / Code Heat | `code-heat` | Rust corpora, compiler material, crate metadata, build pipelines |
| RPG / Dungeon Synth | `process`, `creative`, or named variant | Tabletop, lore, NPC dialogue, items, spells, worlds |
| Creative / Discovery | `featured`, `creative`, `discovery` | Generative writing, worldbuilding, featured creative releases |
| Verified / Complete | `success`, `verified`, `reproducible` | Release-ready artifacts, license pass, quality pass |
| Review / Warning | `important`, `caution`, `decision` | Partial validation, caveats, manual review |
| Error / Failed | `critical`, `error`, `blocked`, `constraint` | Broken builds, failed validation, blockers |

### 7.6 Legacy Color Aliases

Older mockups and raw SVG artifacts may use earlier neon values.

Known legacy aliases:

| Legacy Value | Canonical Role | Canonical Value | Allowed Use |
|---|---|---:|---|
| `#00E5FF` | `structure` | `#22D3EE` | Existing generated SVGs and preserved mockups |
| `#00AFC7` | `structure` border | `#22D3EE` | Existing SVG strokes |
| `#B554FF` | `process` variant | `#A78BFA` | Existing SVG violet accents |
| `#FF7A18` | `code-heat` variant | `#F97316` | Existing Rust SVG accents |
| `#50E060` | `success` variant | `#34D399` | Existing SVG status labels |
| `#FF2E96` | `discovery/error variant` | `#F472B6` or `#F43F5E` | Existing mockup emphasis only |

New final pages should use NIPC v0.1 tokens unless preserving an existing generated SVG or creating a named theme variant.

### 7.7 NIPC-Compatible Theme Token JSON

```json
{
  "name": "Aptlantis Studio - Neon Ink",
  "version": "0.1.0",
  "mode": "dark",
  "colors": {
    "background": {
      "void": "#050816",
      "base": "#0B0F1A",
      "panel": "#111827",
      "raised": "#162033",
      "soft": "#0F172A"
    },
    "text": {
      "primary": "#E5E7EB",
      "secondary": "#CBD5E1",
      "muted": "#94A3B8",
      "faint": "#64748B",
      "inverse": "#050816"
    },
    "semantic": {
      "info": "#22D3EE",
      "structure": "#06B6D4",
      "navigation": "#38BDF8",
      "reference": "#7DD3FC",
      "orientation": "#67E8F9",
      "success": "#34D399",
      "verified": "#22C55E",
      "stable": "#86EFAC",
      "reproducible": "#2DD4BF",
      "available": "#A7F3D0",
      "important": "#FACC15",
      "note": "#FDE047",
      "caution": "#FBBF24",
      "decision": "#F59E0B",
      "memory_anchor": "#FEF08A",
      "critical": "#F43F5E",
      "error": "#EF4444",
      "blocked": "#FB7185",
      "constraint": "#E11D48",
      "deprecated": "#BE123C",
      "process": "#A78BFA",
      "pipeline": "#C084FC",
      "transform": "#D8B4FE",
      "automation": "#8B5CF6",
      "code_heat": "#F97316",
      "build": "#FB923C",
      "operation": "#FDBA74",
      "artifact_output": "#EA580C",
      "featured": "#F472B6",
      "creative": "#EC4899",
      "discovery": "#E879F9",
      "spotlight": "#F0ABFC",
      "experimental": "#818CF8",
      "research": "#6366F1",
      "prototype": "#A5B4FC",
      "canonical": "#E5E7EB",
      "archive": "#94A3B8",
      "muted": "#64748B",
      "unknown": "#CBD5E1"
    }
  }
}
```

### 7.8 Tailwind Token Map

```js
export default {
  theme: {
    extend: {
      colors: {
        studio: {
          void: "#050816",
          base: "#0B0F1A",
          panel: "#111827",
          raised: "#162033",
          soft: "#0F172A",
          text: "#E5E7EB",
          secondary: "#CBD5E1",
          muted: "#94A3B8",
          faint: "#64748B",
          cyan: "#22D3EE",
          structure: "#06B6D4",
          navigation: "#38BDF8",
          violet: "#A78BFA",
          magenta: "#F472B6",
          green: "#34D399",
          yellow: "#FACC15",
          red: "#F43F5E",
          orange: "#F97316",
          advanced: "#3B8DFB",
          experimental: "#818CF8",
          archive: "#94A3B8",
          critical: "#F43F5E",
          caution: "#FBBF24",
          verified: "#22C55E",
          reproducible: "#2DD4BF",
          build: "#FB923C",
          creative: "#EC4899"
        }
      },
      boxShadow: {
        "glow-idle": "0 0 0 rgba(34, 211, 238, 0)",
        "glow-soft": "0 0 16px rgba(34, 211, 238, 0.28)",
        "glow-active": "0 0 24px rgba(34, 211, 238, 0.45)",
        "glow-violet": "0 0 24px rgba(167, 139, 250, 0.42)",
        "glow-magenta": "0 0 24px rgba(244, 114, 182, 0.42)",
        "glow-success": "0 0 24px rgba(52, 211, 153, 0.42)",
        "glow-warning": "0 0 24px rgba(250, 204, 21, 0.38)",
        "glow-danger": "0 0 24px rgba(244, 63, 94, 0.45)",
        "panel": "0 8px 30px rgba(0, 0, 0, 0.35)"
      },
      fontFamily: {
        mono: ["JetBrains Mono", "Cascadia Code", "monospace"],
        display: ["Rajdhani", "Orbitron", "system-ui", "sans-serif"]
      }
    }
  }
};
```

---

## 8. Typography

```mermaid
graph TD

A[Typography]

A --> B[Display<br/>Heavy Italic]
A --> C[System Mono<br/>Technical Labels]
A --> D[Body Copy<br/>Clarity]

classDef cyan fill:#0F172A,stroke:#22D3EE,color:#22D3EE;
classDef neutral fill:#111827,stroke:#64748B,color:#CBD5E1;

class B cyan;
class C,D neutral;
```

### 8.1 Display Typography

Display type carries the brand's energy.

Use for:

- hero headlines
- campaign phrases
- large theme labels
- high-energy section headers

Preferred character:

- bold or heavy
- condensed when available
- optionally italic for campaign surfaces
- uppercase where it improves scanability

Do not use display styling for dense metadata or long explanatory paragraphs.

### 8.2 System Mono

Monospace type is the technical backbone.

Use for:

- dataset IDs
- version numbers
- pipeline names
- build status
- commands
- labels
- metadata rows
- manifest references
- compact navigation labels

Recommended stack:

```css
font-family: "JetBrains Mono", "Cascadia Code", monospace;
```

### 8.3 Body Copy

Body copy should be plain, readable, and direct.

Let panels, semantic color, and SVG artifacts carry the visual intensity. Body copy should provide clarity, not decoration.

### 8.4 Hierarchy

Recommended hierarchy:

| Role | Style |
|---|---|
| Hero headline | Display, heavy, large |
| Section heading | Display or mono, compact uppercase |
| Artifact title | Strong sans or display, readable |
| Metadata label | Mono, uppercase, muted |
| Metadata value | Mono or strong sans, semantic color when needed |
| Body | Plain sans or readable mono, restrained |

---

## 9. Layout & Page Composition

### 9.1 General Page Rules

Pages should feel like navigable archives, not generic SaaS dashboards.

Use:

- dark layered backgrounds
- clear left or top navigation
- dense but organized metadata
- artifact panels with visible roles and states
- semantic color used for meaning, not random decoration
- enough negative space to avoid visual noise

Avoid:

- generic blue SaaS gradients
- decorative cards with no semantic role
- hiding provenance or status
- overusing glow on static content
- making every page a marketing hero
- burying dataset identity below generic navigation

### 9.2 Home Page

The home page introduces the Studio and immediately exposes useful dataset activity.

Required content patterns:

- brand identity or wordmark visible in the first viewport
- concise Studio proposition
- primary dataset or featured artifact
- quick stats
- recent datasets
- latest pipeline runs
- route to datasets and pipelines
- visible active theme or system identity

The home page may use a large visual hero, but it should still behave like a working archive entry point.

### 9.3 Dataset Detail Page

Dataset pages are the most important artifact pages.

Required content patterns:

- dataset identity header
- semantic tags
- state badge
- quality or validation signal when available
- core stats: records, tokens, size, license, created/updated dates
- download or canonical action
- samples, structure, pipelines, versions, and changelog navigation
- overview and composition summary
- latest pipeline run
- compatibility and related datasets
- visible provenance or metadata when trust matters

Dataset pages should support quick scanning before reading long explanations.

### 9.4 About & Documentation Pages

About and docs pages should explain the system without losing the artifact grammar.

Use:

- Q&A accordions or structured sections
- semantic dot/bar indicators
- compact examples
- visible definitions
- links to canonical specs, manifests, and datasets

Avoid turning documentation into a plain article page when componentized artifact panels would clarify the system.

### 9.5 Pipeline Pages

Pipeline pages must make process state visible.

Required content patterns:

- pipeline name and version
- associated dataset
- current state
- stages such as collect, filter, normalize, dedupe, structure, shard, validate
- completion timestamps
- record/token changes
- warnings and errors
- link to logs, reports, or manifests when available

Use violet for process and running states. Use green, yellow, and red for validation outcomes.

### 9.6 Theme Boards

Theme boards demonstrate semantic mapping, not only mood.

Required content patterns:

- theme name and ID
- background layers
- semantic role swatches
- state behavior examples
- component examples
- intended use
- SESM theme summary when used for generated SVGs

### 9.7 Marketing Surfaces

Marketing assets should preserve the Studio's artifact language.

Use:

- dark backgrounds by default
- cyan, violet, and magenta as the primary brand triad
- monospace labels and status language
- short technical copy
- dataset/pipeline artifacts as visual anchors
- wordmark with generous spacing

Marketing surfaces may be more expressive than the website, but they should not contradict the semantic color roles.

---

## 10. Component Grammar

### 10.1 Panel State Table

```mermaid
graph LR

A[Panel States]

A --> B[Idle]
A --> C[Active]
A --> D[Running]
A --> E[Featured]
A --> F[Success]
A --> G[Error]

classDef idle fill:#111827,stroke:#64748B,color:#64748B;
classDef cyan fill:#0F172A,stroke:#22D3EE,color:#22D3EE;
classDef violet fill:#0F172A,stroke:#A78BFA,color:#A78BFA;
classDef magenta fill:#0F172A,stroke:#F472B6,color:#F472B6;
classDef green fill:#0F172A,stroke:#34D399,color:#34D399;
classDef red fill:#0F172A,stroke:#F43F5E,color:#F43F5E;

class B idle;
class C cyan;
class D violet;
class E magenta;
class F green;
class G red;
```

| State | Visual Behavior | Semantic Meaning |
|---|---|---|
| `idle` | Dim border, no glow | Dormant, quiet, or default artifact |
| `active` | Soft cyan glow | Current, selected, browsed, ready |
| `running` | Pulsing violet glow | Pipeline or transformation in progress |
| `featured` | Magenta glow | Notable, new, creative, highlighted |
| `complete` | Green emitter | Completed successfully |
| `verified` | Green status signal | Quality or license verified |
| `warning` | Yellow accent/glow | Needs review or has caveat |
| `error` | Red accent/glow | Failed, blocked, invalid |
| `archived` | Slate/gray muted styling | Dormant, mirrored, historical |
| `experimental` | Indigo or magenta-violet accent | Non-canonical or in progress |

Use NIPC for hue and AIC for state strength. A panel has one dominant semantic accent; secondary colors should appear only as small badges, icons, rails, or metadata dots.

### 10.2 Artifact Panel Requirements

An artifact panel should expose:

- title
- artifact type or category
- state badge when state matters
- semantic accent
- brief description
- key metadata
- canonical action or destination

Dataset and pipeline panels should expose enough metadata for trust, not only visual appeal.

### 10.3 Badges

Badges should be:

- short
- uppercase
- state-driven or role-driven
- colored by semantic meaning
- readable at small sizes

Examples:

- `ACTIVE`
- `RUNNING`
- `VERIFIED`
- `WARNING`
- `FAILED`
- `RUST`
- `CODE`
- `TRAINING`
- `RPG`

### 10.4 Tags

Tags identify subject matter or semantic category.

Tags should use color consistently:

- Rust and compilation tags use orange.
- Process and pipeline tags use violet.
- Navigation/info tags use cyan.
- Featured or creative tags use magenta.
- Warning tags use yellow.
- Error tags use red.

### 10.5 Q&A Accordion Pattern

Q&A entries should support peripheral recognition.

Recommended sequence:

```text
Number -> Colored indicator -> Title text -> Expand/collapse icon
```

Use the colored indicator to communicate context before the user reads the full question.

Examples:

- Orange dot: Rust or code-heavy question
- Cyan dot: structure or general information
- Violet dot: pipeline or implementation process
- Yellow dot: caveat or review note

### 10.6 Links and Actions

Color links by purpose:

| Link Purpose | Color |
|---|---|
| Navigation/indexing | Cyan |
| Process/action | Violet |
| Discovery/featured | Magenta |
| Download/release-ready | Green or cyan |
| Dangerous/destructive | Red |

---

## 11. Dataset, Pipeline, and Artifact Patterns

### 11.1 Dataset Card Metadata

Dataset cards should include the strongest available subset of:

```json
{
  "dataset": {
    "id": "rust-code-corpus",
    "title": "Rust Code Corpus",
    "state": "active",
    "domain": "rust",
    "tags": ["rust", "code", "training"],
    "records": 532104,
    "tokens": "18.7B",
    "size": "7.2 GB",
    "license": "MIT",
    "quality_score": 96,
    "created": "2025-04-12",
    "updated": "2025-05-18",
    "models_supported": ["Local", "GGUF"]
  }
}
```

The exact data source may be JSON, JSONL, TOML, YAML, or another manifest, but the visible card should preserve the same trust signals.

### 11.2 Pipeline Run Card

Pipeline run cards should include:

- pipeline ID
- associated dataset
- state
- stage list
- progress or completion signal
- records changed
- tokens changed when available
- error and warning counts
- completed or updated timestamp
- link to report, log, or canonical pipeline page

Recommended stage language:

```text
Collect -> Filter -> Normalize -> Dedupe -> Structure -> Shard -> Validate
```

### 11.3 Stats Tiles

Stats tiles should be compact and scannable.

Use:

- mono labels
- semantic values
- restrained borders
- no decorative glow unless the stat communicates live state

Common stats:

- total datasets
- total records
- total tokens
- pipelines
- models supported
- last update
- unique crates
- license pass
- duplicate rate
- average tokens per record

### 11.4 Related Dataset Lists

Related dataset lists should preserve category color and visible type tags.

They should help users move laterally through the archive without losing context.

### 11.5 SVG Artifact Panels

SVG artifact panels are first-class content when they carry SESM metadata.

They should:

- remain valid SVG
- include `<metadata id="sesm">` when generated or semantically meaningful
- preserve aspect ratio
- expose readable text where possible
- avoid relying only on visual inference for meaning
- link or point back to canonical HTML when possible

---

## 12. SVG + SESM Requirements

### 12.1 Relationship To SESM

Neon Ink uses SESM v0.2.0 as its embedded semantic metadata carrier for SVG artifacts.

SESM remains the metadata standard. NIPC defines palette semantics. Neon Ink defines the brand expression and visual grammar that SESM can reference.

The **Artifact Interface Contract (AIC) v0.1** defines the bridge across the systems. Where SESM says what an artifact is, NIPC says what its color semantics mean, and Neon Ink says how the brand behaves, AIC says exactly how that artifact renders across SVG, HTML, metadata, and interaction targets.

```text
DATA -> SESM -> AIC -> SVG/HTML -> USER
```

Generated Aptlantis Studio artifacts should treat these documents as a three-layer system:

| Layer | Canonical Document | Responsibility |
|---|---|---|
| Meaning | [SESM v0.2.md](../specs/SESM-v0.2.md) | Metadata, identity, provenance, links, agent hints |
| Palette | [NIPC v0.1.1.md](../specs/NIPC-v0.1.1.md) | Color families, semantic roles, psychological intent, intensity validation |
| Contract | [AIC v0.1.1.md](../specs/AIC-v0.1.1.md) | Artifact types, required fields, layout regions, render targets |
| Expression | [NeonInk-v0.1.md](NeonInk-v0.1.md) | Typography, panel grammar, page composition, brand voice |

### 12.2 Required For Compiled SVG Artifacts

Compiled SVG artifacts should include:

```xml
<metadata id="sesm"><![CDATA[
{
  "sesm_version": "0.3.0"
}
]]></metadata>
```

Generated SVGs should include these top-level SESM fields when available:

- `asset`
- `artifact`
- `theme`
- `ui`
- `crawl`
- `llm`
- `links`
- `provenance`
- `integrity`

Only `sesm_version` is required by SESM, but Aptlantis Studio production artifacts should include enough metadata to remain self-describing.

### 12.3 Neon Ink SESM Theme Block

Recommended `theme` block:

```json
{
  "theme": {
    "id": "neon-ink",
    "name": "Neon Ink",
    "version": "0.1.0",
    "mode": "dark",
    "accent": {
      "name": "orange",
      "hex": "#F97316",
      "semantic_role": "code-heat",
      "semantic_family": "creation-build-code",
      "psychological_intent": "signal-hands-on-code-build-work"
    },
    "state": {
      "name": "active",
      "intensity": 2,
      "glow": "soft"
    },
    "priority": "medium",
    "tokens": {
      "void": "#050816",
      "base": "#0B0F1A",
      "panel": "#111827",
      "text": "#E5E7EB",
      "muted": "#94A3B8",
      "info": "#22D3EE",
      "structure": "#06B6D4",
      "process": "#A78BFA",
      "discovery": "#F472B6",
      "success": "#34D399",
      "important": "#FACC15",
      "critical": "#F43F5E",
      "code_heat": "#F97316"
    }
  }
}
```

### 12.4 Recommended Semantic Role Names

Use these role names in SESM and manifests:

- `info`
- `structure`
- `navigation`
- `reference`
- `orientation`
- `process`
- `pipeline`
- `transform`
- `automation`
- `discovery`
- `featured`
- `creative`
- `success`
- `verified`
- `reproducible`
- `important`
- `caution`
- `error`
- `critical`
- `blocked`
- `constraint`
- `code-heat`
- `build`
- `operation`
- `experimental`
- `research`
- `prototype`
- `canonical`
- `archive`
- `muted`

### 12.5 Recommended State Names

Use these state names in SESM and manifests:

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

### 12.6 Provenance Expectations

Generated artifacts should record:

- generator name
- generator version when available
- build ID
- source record IDs
- template ID
- source path or manifest reference
- output path
- reproducibility flag

### 12.7 UI Hints

Generated SVGs should include useful UI hints when applicable:

- component type
- preferred layout
- preferred regions
- responsive behavior
- dimensions or aspect ratio
- canonical interaction target

Example:

```json
{
  "ui": {
    "component_type": "dataset-hero-panel",
    "preferred_layout": "artifact-panel",
    "preferred_regions": ["dataset-header"],
    "responsive_behavior": "preserve-aspect-ratio",
    "dimensions": "intrinsic-svg-viewbox"
  }
}
```

---

## 13. Content & Voice Rules

### 13.1 Preferred Language

Use phrases like:

- high-signal datasets
- small specialist models
- local-first training
- reproducible pipelines
- compiled artifacts
- curated niche corpora
- dataset recipes
- manifests
- archive-ready releases
- local machines
- practical licensing

### 13.2 Avoid

Avoid phrases and positioning like:

- AI magic
- one-click intelligence
- massive scraped everything
- corporate productivity platform
- generic chatbot branding
- cloud-only framing
- promises beyond dataset scope
- vague claims of intelligence without data or evaluation context

### 13.3 Copy Style

Copy should be:

- concise
- concrete
- technically honest
- builder-friendly
- clear about constraints
- careful with licensing and quality claims

### 13.4 Example Brand Copy

```text
Build small. Train local. Create worlds.

Aptlantis Studio publishes focused datasets for builders who want useful
small models on personal hardware. Every release favors clear manifests,
durable formats, practical licensing, and reproducible pipelines over noisy
scale.
```

---

## 14. Brand Collateral Rules

### 14.1 Wordmark Usage

Use the full Aptlantis Studio wordmark on primary brand surfaces.

Do:

- keep generous negative space
- use cyan, white, or violet on dark backgrounds
- pair the wordmark with concise technical subtitles
- preserve the Studio identity in the first viewport or first visual frame

Avoid:

- generic AI platform mimicry
- overused blue SaaS gradient identity
- hiding dataset status or provenance
- flattening all surfaces into plain static cards

### 14.2 Canva Assets

Canva templates should include:

- primary colors: cyan, violet, magenta, void, panel, text
- secondary colors: green, orange, yellow, red, muted slate
- monospace labels
- strong display headlines
- reusable artifact panels
- dataset card template
- pipeline panel template
- theme board template

Canva assets do not need SESM metadata, but they should preserve Neon Ink's color meanings and artifact language.

### 14.3 Presentations

Presentation decks should use:

- dark-first title slides
- large display phrases
- mono section labels
- artifact panels for examples
- semantic color tables
- screenshots or generated visuals where useful

Slides should feel like guided archive views, not generic pitch templates.

### 14.4 Social Graphics

Social graphics may be punchier than website pages, but they should still:

- use Neon Ink tokens
- show dataset or artifact identity
- keep claims concise
- avoid generic AI hype
- preserve brand phrases and local-first positioning

---

## 15. Validation Checklist

Use this checklist before treating a page, SVG, template, or brand asset as Neon Ink compliant.

### 15.1 Color

- Uses NIPC v0.1 tokens for new work.
- Uses legacy aliases only for existing mockups or generated SVG preservation.
- Records `semantic_role`, `semantic_family`, `psychological_intent`, and `intensity` when generating semantic artifacts.
- Uses one dominant accent per artifact.
- Uses red/risk roles only for blockers, failures, hard constraints, or deprecation.
- Uses green/trust roles only when evidence exists, such as validation, availability, reproducibility, or quality pass.
- Uses yellow/attention roles as markers, not dominant surfaces.
- Uses orange/code roles for Rust, build, execution, and artifact output, not arbitrary decoration.

### 15.2 Layout

- Page reads as a navigable archive, not a generic SaaS dashboard.
- Important artifact identity appears early.
- Metadata remains visible where trust matters.
- Panels have clear roles and states.
- Glow is used for state/activity, not everywhere.

### 15.3 Components

- Panel, border, glow, badge, metadata, and action each have a clear role.
- Tags are semantically colored.
- Badges are short and uppercase.
- Dataset and pipeline cards expose enough scan-level metadata.

### 15.4 SESM

- Compiled SVGs include SESM v0.2.0 metadata.
- `theme.id` is `neon-ink`.
- Theme metadata is NIPC-compatible when palette semantics matter.
- Semantic role and family names match NIPC.
- State names match this spec.
- Generated artifacts include provenance when available.
- SVGs point to canonical HTML, manifests, or related resources when useful.

### 15.5 Brand

- Voice is precise, inventive, durable, and welcoming.
- Copy favors high-signal data, local-first training, and reproducible pipelines.
- Marketing surfaces use the same color meanings as the website.
- No generic AI magic or cloud-only positioning.

---

## 16. Compatibility Notes

### 16.1 Relationship To Existing Screenshots

Current built page screenshots are important references for layout density, sidebar behavior, dataset-page structure, and artifact-panel composition.

They are not automatically canonical where they conflict with stronger system rules in this document.

### 16.2 Relationship To Existing Mockups

Mockups are reference material for visual direction, composition, and theme energy.

They may include legacy color values or variant styling. New final pages should translate those ideas into NIPC v0.1 tokens.

### 16.3 Relationship To SESM v0.2

SESM v0.2 defines how semantic metadata is embedded in SVG assets.

Neon Ink v0.1 defines the Aptlantis Studio design language and theme semantics that can be expressed inside SESM.

### 16.4 Relationship To Theme Variants

Theme variants may adjust subject-specific emphasis while inheriting Neon Ink.

Example:

- Dungeon Synth may emphasize violet, green, and warmer fantasy imagery.
- Rust Code Corpus may emphasize orange, cyan, and technical metadata.

Variants must not invert core semantic meanings unless documented as a separate named standard.

### 16.5 Future Versions

Future Neon Ink versions may add:

- stricter accessibility contrast rules
- formal component schemas
- named theme variant specs
- generator validation tests
- design token package output
- screenshot acceptance baselines
- Canva template inventories

Breaking changes should increment the major version. Additive changes should increment the minor version.

---

## 17. Summary

Neon Ink is the Aptlantis Studio standard for turning data into durable visual artifacts.

It unifies:

- dark archival backgrounds
- semantic neon color
- panel-based composition
- visible provenance
- SESM-compatible SVG artifacts
- local-first dataset publishing
- precise builder-friendly brand voice

The north star is simple:

> Aptlantis Studio should feel like an archive that is alive: static enough to last, structured enough to regenerate, and expressive enough to make datasets feel like artifacts worth exploring.
