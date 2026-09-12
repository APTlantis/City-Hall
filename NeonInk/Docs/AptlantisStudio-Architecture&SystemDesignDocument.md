# Aptlantis Studio — Architecture & System Design Document

## 1. Overview

**Aptlantis Studio** is a data-driven platform for creating, curating, and distributing **focused datasets for small, locally runnable models**.

Unlike traditional web applications, Aptlantis Studio is not built as a dynamic frontend system. Instead, it operates as a:

> **Deterministic artifact compiler that transforms structured data into visual and navigable outputs**

The system compiles:

* SVG-based visual components
* Static HTML pages
* Theme-driven UI artifacts

All derived from structured data sources such as JSON and JSONL.

---

## 2. Core Philosophy

### 2.1 Artifact-First Design

Every visual element is an artifact generated from data:

* Dataset cards → SVG artifacts
* Pipeline states → visual artifacts
* Theme boards → metadata-rich SVGs

### 2.2 Data as Source of Truth

No UI element is manually authored beyond templates. All content originates from:

* dataset manifests
* pipeline outputs
* theme definitions

### 2.3 Static Output, Dynamic Generation

The system produces static files, but is:

* frequently regeneratable
* pipeline-driven
* event-triggered

### 2.4 Local-First & Durable

* No runtime dependencies required to view site
* Fully mirrorable
* Long-term reproducible

---

## 3. System Architecture

### 3.1 High-Level Flow

```plaintext
Data (JSON/JSONL)
      ↓
Rust Generator (themegen / aptstudio)
      ↓
Templates (SVG + HTML)
      ↓
Compiled Artifacts (SVG + HTML)
      ↓
Static Hosting (Caddy / filesystem)
```

---

## 4. Directory Structure

```plaintext
/AptStudio/

  /data/
    datasets.jsonl
    pipelines.jsonl
    stats.json
    themes.json

  /templates/
    /svg/
      dataset_card.svg.tmpl
      pipeline_panel.svg.tmpl
      theme_board.svg.tmpl

    /html/
      base.html
      dataset.html
      pipelines.html
      index.html

  /generated/
    /svg/
      /datasets/
      /pipelines/
      /themes/

    /html/
      /datasets/
      /pipelines/

  /static/
    /css/
    /icons/

  /tools/
    /aptstudio/   (Rust generator CLI)

  /public/
    (final compiled output served by Caddy)
```

---

## 5. Data Layer

### 5.1 Dataset Manifest (JSONL)

Each dataset is represented as a single record:

```json
{
  "id": "rust_code_corpus",
  "name": "Rust Code Corpus",
  "state": "active",
  "type": "code",
  "tokens": 18700000000,
  "records": 532104,
  "updated": "2026-05-01"
}
```

---

### 5.2 Pipeline Manifest

```json
{
  "id": "rust_pipeline",
  "status": "running",
  "progress": 72,
  "stage": "normalization"
}
```

---

### 5.3 Theme Tokens

```json
{
  "colors": {
    "cyan": "#22D3EE",
    "violet": "#A78BFA",
    "magenta": "#F472B6"
  },
  "semantic": {
    "active": "cyan",
    "running": "violet",
    "featured": "magenta"
  }
}
```

---

## 6. Generator Layer (Rust)

### 6.1 Responsibilities

The Rust generator:

* parses JSON/JSONL
* validates structured data
* maps semantic states to theme tokens
* renders templates (SVG + HTML)
* writes output to `/public`

---

### 6.2 Core Crates

```toml
serde
serde_json
tera
walkdir
anyhow
```

---

### 6.3 Core Execution Model

```plaintext
load data
→ resolve theme mappings
→ render templates
→ write files
```

---

### 6.4 CLI Interface (Planned)

```bash
aptstudio build
aptstudio build --dataset rust
aptstudio build --themes
aptstudio validate
```

---

## 7. SVG Component System

### 7.1 Role of SVG

SVGs act as:

* UI components
* metadata containers
* visual artifacts
* crawlable structured documents

---

### 7.2 SVG Template Structure

```xml
<svg>
  <metadata>
    {
      "dataset": "{{ id }}",
      "state": "{{ state }}"
    }
  </metadata>

  <rect fill="{{ theme.panel }}" />
  <rect stroke="{{ accent }}" />

  <text>{{ name }}</text>
</svg>
```

---

### 7.3 Benefits

* resolution independent
* easily themed
* embeddable anywhere
* machine-readable

---

## 8. HTML Layer

### 8.1 Philosophy

HTML is a **layout shell**, not a rendering engine.

---

### 8.2 Example

```html
<div class="panel">
  <img src="/svg/datasets/rust_code_corpus.svg">
</div>
```

---

### 8.3 Responsibilities

* layout composition
* navigation
* grouping artifacts

---

## 9. Styling System

### 9.1 Technologies

* **Tailwind (extended)** → tokens, colors, utilities
* **Bulma** → layout structure

---

### 9.2 Design Language

| Meaning   | Color   |
| --------- | ------- |
| Structure | Cyan    |
| Process   | Violet  |
| Discovery | Magenta |
| Success   | Green   |
| Warning   | Yellow  |
| Error     | Red     |
| Code/Rust | Orange  |

---

### 9.3 Glow Semantics

| State    | Visual         |
| -------- | -------------- |
| Idle     | No glow        |
| Active   | Soft cyan glow |
| Running  | Violet glow    |
| Featured | Magenta glow   |
| Error    | Red glow       |

---

## 10. Build & Update Strategy

### 10.1 Event-Driven Rebuilds

Trigger rebuild when:

* dataset updated
* pipeline completed
* stats changed

---

### 10.2 Build Command

```bash
cargo run --bin aptstudio -- build
```

---

### 10.3 Optional Watch Mode

* monitor `/data/`
* auto-trigger rebuild

---

### 10.4 Partial Rebuild (Future)

```plaintext
changed dataset → regenerate only related artifacts
```

---

## 11. Page Types

### 11.1 Landing Page

* overview panels
* featured datasets
* pipeline highlights

### 11.2 Dataset Page

* dataset artifact SVG
* metadata panels
* download links

### 11.3 Pipeline Page

* status panels
* progress indicators
* logs/steps

### 11.4 Theme Board Page

* palette visualization
* semantic mapping
* SVG export

---

## 12. Extensibility

### 12.1 Future Features

* dataset versioning
* schema validation
* artifact graph relationships
* theme switching per dataset
* exportable theme packs

---

### 12.2 Plugin Model (Conceptual)

```plaintext
/templates/
  /dataset/
  /pipeline/
  /theme/
```

Each template set acts as a rendering plugin.

---

## 13. Key Advantages

### 13.1 Durability

* no runtime dependencies
* fully static output

### 13.2 Consistency

* UI derived from structured data

### 13.3 Reproducibility

* artifacts can always be regenerated

### 13.4 Flexibility

* easy to add new datasets, themes, or pages

### 13.5 Personal Workflow Alignment

* integrates directly with existing Rust pipelines
* avoids repetitive manual HTML work
* enables creative visual expression

---

## 14. Final Definition

Aptlantis Studio is:

> A Rust-powered artifact compiler that transforms structured dataset pipelines into visual, navigable, and archivable static outputs.

---

## 15. Closing Notes

This system intentionally avoids:

* heavy frontend frameworks
* dynamic runtime complexity
* manual UI maintenance

Instead, it embraces:

* structure
* determinism
* composability
* long-term resilience

---

**End of Document**

