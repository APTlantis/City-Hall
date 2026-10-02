# NeonInk data presentation system

Version 0.2.0 · Candidate active · 2026-09-27

## Purpose and authority

NeonInk presents data through reports, analytical stories, charts, dataset profiles, diagrams, slides, and portable visual artifacts. Blue Slate is the house theme for dense operational applications. A Blue Slate application can host a bounded NeonInk report or export: preserve the host's navigation, controls, density, and keyboard behavior, and apply NeonInk inside the presentation region.

This specification supersedes `Docs/` for new NeonInk work. The old whole-brand mandate, website campaigns, manga geometry, and desktop default are retired. Existing adopters may retain pinned historical contracts until deliberately migrated. City Hall's active SESM suite governs embedded metadata; the local historical SESM document does not override it.

The suite is usable for pilots. It is not proven stable, universally accessible, or deployed into an application merely because its compiler passes.

## Visual identity

Keep the dark ink canvas, crisp cyan orientation, violet process language, magenta discovery, and restrained semantic accents. A presentation should have one clear question and one dominant visual argument. Use generous plot space and concise annotations, with enough metadata to inspect the result. Avoid luminous chrome, gradient-filled text, decorative circuitry, and ornamental cards around every sentence.

The visual hierarchy is: question or finding; chart or artifact; interpretation and caveat; source and method. Prefer direct labels and shared alignment. NeonInk can be vivid without becoming a poster. Decorative imagery is optional and carries no authority; manga is deprecated and excluded from current examples.

## Token layers

1. `spec/tokens/NeonInk.Tokens.toml` owns opaque palette values, their exact sRGB hex and equivalent OKLCH coordinates, semantic aliases, chart scales, and contrast pairs.
2. Semantic aliases express the intended use: `text`, `muted`, `danger`, `focus`, `panel`, and so on. Components use these before raw palette entries.
3. Framework and chart adapters translate the same roles. They do not become new palette authorities.
4. `generated/` contains reproducible translations. Do not hand-edit them or sample token values from reference images.

Original v0.1.1 colors remain exact. `danger` maps to the existing lighter blocked/risk color because the original critical red is only 4.439:1 against `raised`. The original critical red remains available for sufficiently contrasted marks, borders, and approved pairs. `text-faint` is a border resource, not normal-sized text. Expanded legacy roles are preserved resources, not blanket accessibility approvals.

Use the generated color representation table for all hex/OKLCH pairs. There is one dark screen profile. Print/export may use a separately tested paper profile; simply inverting lightness is not an approved light theme.

## Meaning, state, and data are separate

| Channel | Purpose | Example |
| --- | --- | --- |
| Artifact role | What this represents | Violet process rail on a pipeline diagram |
| State | What is currently known | Labeled risk badge on a failed process |
| Data encoding | Which series/value is plotted | Cyan series A, violet series B, explicit legend |

Cyan orients; violet explains process; magenta highlights discovery; orange denotes building; indigo marks experimentation. Yellow calls attention to caveats. Green status requires an evidence reference and check date. Red status denotes failure, risk, blocking, or deprecation. A chart's signed difference is not automatically good or bad: use the neutral-centered violet/cyan diverging scale unless the domain explicitly defines desirability.

Within a chart, the legend defines categorical meaning. Reserve red/green status semantics outside the plot; use the five-series categorical set for ordinary comparisons. Do not imply five colors are distinguishable for every viewer. Pair hue with labels, marker shapes, dashes, position, or patterns. Above five series, prefer small multiples or selection.

## Typography and spacing

Use the host's established sans-serif if it is legible; portable examples use Segoe UI, Arial, sans-serif. Numeric values use tabular figures. Use a monospace face for identifiers only. Never require an unavailable commercial font.

| Role | Screen default | Guidance |
| --- | --- | --- |
| Report title | 32–40 px, weight 600–700 | Short, wraps naturally |
| Section heading | 22–28 px, weight 600 | Describes the question |
| Key figure | 36–56 px, tabular | Unit and denominator adjacent |
| Body/annotation | 16–18 px, line height 1.5 | Explain the finding |
| Axis/table/source | 14–16 px, line height 1.4 | Never shrink to fit dense data |

Use a 4 px spacing unit: 8 for related labels, 16 within a panel, 24 between chart blocks, 32–48 between report sections. Reading width is roughly 65–80 characters; chart regions may be wider. Default corner radius is 8 px, with 1 px boundaries. Essential control boundaries use `border`; subtle surface differences alone do not identify interactive controls.

## Components and states

- **Finding block:** sentence headline, value with unit, baseline/period, and evidence note. A percent requires its denominator. Avoid orphan KPI tiles.
- **Chart frame:** title, summary, plotted region, axes/units, directly associated legend, notes, source and date, and a usable table or textual equivalent.
- **Dataset profile:** coverage, schema/version, row count, collection window, quality limitations, license/source, and meaningful destination. A count alone is not quality evidence.
- **Evidence callout:** compact semantic rail, explicit status word, claim, reference, checked date. Missing evidence is `unknown`, not success.
- **Legend/filter:** visible labels and selected state beyond color, keyboard operable where interactive, stable series identity after sorting/filtering.
- **Table:** aligned numeric columns, header associations, units in headers, visible missing-value notation, row focus/selection distinct from semantic status.

Loading names the operation; empty distinguishes zero results from no observations; error explains the unavailable result and recovery; stale shows the actual as-of date; missing uses a gap or hatch and `No data`, never zero. Focus uses a visible 2 px cyan outline with offset. Selection includes text/checkmark/border. Hover must not be the only way to read a value. Disabled state preserves label readability where practical and is not a synonym for missing data.

## Motion and interaction

Static presentation is the default. If motion helps show an update, use brief 120–200 ms transitions with no looping glow, flashing, or animated number counting. Respect reduced motion. Filters and tabs require accessible names, native keyboard behavior, and visible focus. Charts should expose values through focus/click or a table as well as hover.

At narrow widths, stack the interpretation below the plot, wrap legends, and use smaller multiples. Preserve a readable minimum plot width inside a labeled scroll region if necessary. At 200% zoom, keep source notes, controls, and data access available. Do not solve overflow by shrinking all text or hiding the caveat.

## Accessibility and color

Use WCAG 2.2 AA as the adoption target: normal text at least 4.5:1; large text at least 3:1; essential graphical objects and control indicators at least 3:1 against adjacent colors where applicable. The suite uses 4.5:1 for its declared text pairs. Color must have a redundant cue. Contrast is calculated from displayed relative luminance, not the difference between OKLCH L values. Alpha, gradients, antialiasing, and adjacent chart marks require rendered review.

The darkest sequential stops may not contrast against the canvas; add a contrasting outline, value label, table, or another sufficient representation. Grid lines may be subtle only when nonessential. Do not claim CVD safety, APCA compliance, or full WCAG conformance from the token audit.

References: [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [non-text contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html), [CSS Color 4](https://www.w3.org/TR/css-color-4/). These define accessibility and color mechanics; the NeonInk presentation choices are local design policy.

## Exports and metadata

SVG references include a title and description; informative SVG embedded in HTML needs a meaningful accessible name. Standalone raster or slide exports keep visible title, units, legend, source, date, and limitations. An accompanying table or description is required where the image alone is insufficient. Public exports exclude private endpoints and credentials. Use active SESM when embedded artifact identity/provenance is required; do not invent SESM conformance from SVG title/description alone.

## Completion and adoption

An adopter records suite version, bounded surfaces, profile, data source, deviations, tests, and runtime/export evidence. Completion requires token freshness, correct data encoding, non-color cues, actual-size visual inspection, keyboard/zoom checks for interactive surfaces, and exported artifact review. See the adoption guide, layout patterns, token contract, and validation checklist for the reproducible path.
