# Blue-Slate Layout Patterns

These patterns define the reusable content shapes for Aptlantis pages and tools. They are layout decisions, not generic components. Each pattern should consume generated translations from the shared `spec/tokens/BlueSlate.Tokens.toml` source.

For the fuller section-by-section anatomy of a Blue Slate surface—including orientation headers, supporting sections, evidence/provenance, workflow, status, and continuation regions—see `spec/BlueSlate.Overview.md`. This document stays focused on choosing and applying the pattern itself.

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

Tokens: `semantic.surface.panel`, `semantic.structure.border-soft`, `semantic.content.primary`, `semantic.content.secondary`, occasional `semantic.interaction.action` for inline links.

## Pillar Grid

Use when the page must be understood in about ten seconds: mission, system, longevity; governance, standards, evidence; constraint, experiment, lesson.

Density: medium-high. Keep card heights balanced.

Tokens: `semantic.surface.panel`, `semantic.surface.panel-raised`, `semantic.structure.border`, `semantic.content.primary`, `semantic.content.tertiary`.

## Split Console

Use for source-to-output relationships: explanation plus terminal output, inputs plus generated artifact, architecture plus manifest, command settings plus generated command.

Density: high. This should feel like an embedded instrument.

Tokens: `semantic.surface.panel-accent`, `component.code.background`, `component.code.foreground`, `semantic.structure.border`, `semantic.interaction.action-secondary`, `semantic.intent.attention`.

## Evidence Grid

Use for manifests, checksums, screenshots, generated files, release notes, downloadable resources, and verification records.

Density: high. Cards should be smaller, file-like, and scannable.

Tokens: `semantic.surface.panel`, `semantic.structure.border-soft`, `semantic.content.secondary`, `semantic.intent.verified`, `semantic.intent.taxonomy`.

## Workflow Rail

Use for operator workflows, import/export paths, migration plans, release pipelines, and staged repair flows.

Density: medium. Number badges should help scanning without becoming decorative.

Tokens: `semantic.interaction.action`, `semantic.intent.attention`, `semantic.structure.border`, `semantic.content.primary`, `semantic.content.tertiary`.

## Instrument Panel

Use for dashboards, status summaries, quality gates, readiness scores, project health, and governance maturity.

Density: high. Use sparingly because numbers imply importance.

Tokens: `semantic.surface.panel-raised`, `semantic.interaction.action`, `semantic.intent.success`, `semantic.intent.warning`, `semantic.intent.taxonomy`, `semantic.content.primary`.

## Gallery Matrix

Use for screenshots, visualizations, diagrams, UI states, and generated media.

Density: variable. Use one large featured item plus smaller supporting items when one screenshot carries the concept.

Tokens: `semantic.surface.panel`, `semantic.structure.border`, `semantic.content.secondary`, `semantic.content.tertiary`.

## Lab Stage

Use for interactive modules, generators, metadata inspectors, simulators, and concept explainers.

Density: high for controls, medium for explanation.

Tokens: `semantic.surface.panel-accent`, `semantic.interaction.focus`, `semantic.interaction.action`, `component.code.background`, `semantic.intent.warning`.

## Segmented Explainer

Use for several peer concepts that would feel heavy if stacked: governance/release/metadata, inputs/relationships/outputs, mission/infrastructure/preservation.

Density: medium. This is an inline section switcher, not full page navigation.

Tokens: `semantic.surface.panel`, `semantic.structure.border-soft`, `semantic.interaction.action`, `semantic.content.secondary`.

## Resource Shelf

Use for guides, templates, docs, external/internal references, downloads, examples, and reusable artifacts.

Density: medium-high. Each item should expose type, focus, and status.

Tokens: `semantic.surface.panel`, `semantic.intent.taxonomy`, `semantic.intent.verified`, `semantic.intent.archive`, `semantic.content.tertiary`.

## Acceptance Rules

- Every page should have one primary pattern and no more than two secondary patterns.
- Use accents only when the pattern needs action, state, status, priority, verification, taxonomy, or active navigation.
- Prefer compact operational rhythm over marketing spacing.
- The technical grid and dark canvas are brand assets; do not replace them with arbitrary page backgrounds.
