# NeonInk integrated overview

NeonInk 0.2.0 is the expressive data-presentation companion to Blue Slate's operational UI. A typical report moves from a question, through evidence, to a qualified interpretation.

## Reading and implementation path

1. [Design system](NeonInk.DesignSystem.md): authority, meaning, typography, components, states, and accessibility.
2. [Data visualization](Data-Visualization.md): chart choice, scale semantics, numerical integrity.
3. [Layout patterns](layout/NeonInk.LayoutPatterns.md): analytical report, dataset profile, explanatory plate.
4. [Token contract](tokens/Token-Contract.md) and [TOML](tokens/NeonInk.Tokens.toml): exact colors and approved pairings.
5. [Framework profiles](frameworks/NeonInk.Profiles.md): CSS, React, chart libraries, native hosts, print/slides.
6. [Reference catalog](references/Reference-Catalog.md): generated vector boards and PNG previews.
7. [Adoption guide](../Adoption-Guide.md): pinning, verification, and recovery.

## Surface anatomy

| Region | Content | Visual treatment |
| --- | --- | --- |
| Context | Report identity, period, source | Muted text, small type, no status implication |
| Argument | Question/finding and chart | Large plot, concise headline, one accent emphasis |
| Explanation | Units, denominator, caveat | Visible body text, explicit callout when material |
| Evidence | Source, method, table, as-of date | Readable metadata, durable links, no decorative badges |

The chart scale is independent of the artifact's state. A violet pipeline can contain a cyan data series and a labeled danger badge. Scope CSS to `.neonink` inside an existing app and preserve its Blue Slate shell.

## Evidence boundary

Generated tokens and reference boards demonstrate the contract. Compiler and regression checks verify declared invariants. They do not establish real adopter behavior, data quality, assistive-technology success, native runtime integration, or stable maturity. Pilot those separately before promotion.
