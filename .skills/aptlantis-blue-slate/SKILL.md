---
name: aptlantis-blue-slate
description: Design, implement, compile, or audit Blue Slate themes and operational layouts, map semantic tokens into framework profiles, and maintain Blue Slate assets and adoption records. Use for work explicitly adopting the Aptlantis Blue Slate visual system or updating its standard.
---

# Aptlantis Blue Slate

Use Blue Slate as a semantic visual system: palette and theme, persistent hierarchy, page and app-shell anatomy, layout patterns, controls and states, typography, density, accessibility, assets and implementation evidence.

## Locate authority and the task

The active standard is `D:\.city_hall\BlueSlate`. Read its `AGENTS.md`, `README.md`, `BlueSlate.manifest.toml` and the adopting project's instructions. Canonical token values are in `spec/tokens/BlueSlate.Tokens.toml`; visual and layout rules are in `spec/BlueSlate.DesignSystem.md`, `spec/BlueSlate.Overview.md` and `spec/layout/BlueSlate.LayoutPatterns.md`.

Infer the target project, framework and requested operation from the current task and files. Ask only for missing information that changes the work. On a machine without City Hall, use an explicitly supplied versioned Blue Slate suite and state its provenance; do not silently elevate the desktop source workspace or a raster board into a second standard. This skill can be installed separately: resolve suite resources against the chosen suite root, not the skill's installation directory.

## Work paths

- For a new surface, layout revision or visual review, read [layout and UI](references/layout-and-ui.md), then only the relevant framework profile.
- For token changes, compilation, theme mapping or an audit, read [tokens and validation](references/tokens-and-validation.md). Audits report findings without silently retuning colors; authorized fixes may proceed within the user's scope.
- For a framework port or existing adopter migration, read [framework adapters](references/framework-adapters.md) and the suite's `Migration-0.5.md`.
- For logos, embedded SVG metadata, source boards or image palettes, read [assets and SESM](references/assets-and-sesm.md).
- For a standard release, promotion or maintenance pass, read [standard maintenance](references/standard-maintenance.md).

## Shared decisions

Keep the single dark theme unless the user is deliberately changing the standard. Preserve exact palette values during migration. Use semantic/component roles before raw colors; framework keys belong in adapters. Read the current source rather than memorizing old aliases or copying a theme board's uncertain numeric labels.

Build resting-screen hierarchy with surface, typography, spacing and boundaries. Accents carry action, state, proof, taxonomy or risk. Choose one primary layout pattern and at most two secondary patterns; do not apply a dashboard composition to every task.

Honor native framework accessibility and interaction behavior. Prefer the project's existing component system and assets where its adoption profile requires them. Blue Slate does not justify replacing Carbon anatomy, native control states or working keyboard behavior with decorative replicas.

Distinguish observed, generated, validated and runtime-verified evidence. Report the files changed, token/profile version, relevant checks, local deviations and remaining runtime gaps. A standards update or skill invocation does not itself authorize installation into unrelated live applications, publication, or global skill registration.
