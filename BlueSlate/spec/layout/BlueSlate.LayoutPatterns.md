# Blue-Slate Layout Patterns

These patterns define the reusable content shapes for Aptlantis pages and tools. They are layout decisions, not generic components. Each pattern should consume the shared tokens from `spec/tokens/BlueSlate.Tokens.json`.

## Global Frame

All Blue-Slate surfaces use the same outer feeling: dark canvas, subtle technical grid, compact structure, pale text, meaningful cyan/teal action, and evidence-first panels.

The inner module changes by content purpose.

| Content purpose | Pattern |
| --- | --- |
| Explain | Dossier Stack |
| Summarize | Pillar Grid |
| Compare | Split Console |
| Prove | Evidence Grid |
| Operate | Workflow Rail |
| Monitor | Instrument Panel |
| Show visuals | Gallery Matrix |
| Teach interactively | Lab Stage |
| Switch concepts | Segmented Explainer |
| Organize references | Resource Shelf |

## Dossier Stack

Use for about pages, standards explanations, FAQs, release/trust notes, and evidence summaries.

Density: medium. Use compact cards with clear headings and short paragraphs.

Tokens: `panel`, `border-soft`, `text`, `text-soft`, occasional `action` for inline links.

## Pillar Grid

Use when the page must be understood in about ten seconds: mission, system, longevity; governance, standards, evidence; constraint, experiment, lesson.

Density: medium-high. Keep card heights balanced.

Tokens: `panel`, `panel-raised`, `border`, `text`, `text-muted`.

## Split Console

Use for source-to-output relationships: explanation plus terminal output, inputs plus generated artifact, architecture plus manifest, command settings plus generated command.

Density: high. This should feel like an embedded instrument.

Tokens: `panel-blue`, `codeBackground`, `codeText`, `border`, `action-soft`, `attention`.

## Evidence Grid

Use for manifests, checksums, screenshots, generated files, release notes, downloadable resources, and verification records.

Density: high. Cards should be smaller, file-like, and scannable.

Tokens: `panel`, `border-soft`, `text-soft`, `verified`, `taxonomy`.

## Workflow Rail

Use for operator workflows, import/export paths, migration plans, release pipelines, and staged repair flows.

Density: medium. Number badges should help scanning without becoming decorative.

Tokens: `action`, `attention`, `border`, `text`, `text-muted`.

## Instrument Panel

Use for dashboards, status summaries, quality gates, readiness scores, project health, and governance maturity.

Density: high. Use sparingly because numbers imply importance.

Tokens: `panel-raised`, `action`, `success`, `warning`, `taxonomy`, `text`.

## Gallery Matrix

Use for screenshots, visualizations, diagrams, UI states, and generated media.

Density: variable. Use one large featured item plus smaller supporting items when one screenshot carries the concept.

Tokens: `panel`, `border`, `text-soft`, `text-muted`.

## Lab Stage

Use for interactive modules, generators, metadata inspectors, simulators, and concept explainers.

Density: high for controls, medium for explanation.

Tokens: `panel-blue`, `focus`, `action`, `codeBackground`, `warning`.

## Segmented Explainer

Use for several peer concepts that would feel heavy if stacked: governance/release/metadata, inputs/relationships/outputs, mission/infrastructure/preservation.

Density: medium. This is an inline section switcher, not full page navigation.

Tokens: `panel`, `border-soft`, `action`, `text-soft`.

## Resource Shelf

Use for guides, templates, docs, external/internal references, downloads, examples, and reusable artifacts.

Density: medium-high. Each item should expose type, focus, and status.

Tokens: `panel`, `taxonomy`, `verified`, `archive`, `text-muted`.

## Acceptance Rules

- Every page should have one primary pattern and no more than two secondary patterns.
- Use accents only when the pattern needs action, state, status, priority, verification, taxonomy, or active navigation.
- Prefer compact operational rhythm over marketing spacing.
- The technical grid and dark canvas are brand assets; do not replace them with arbitrary page backgrounds.
