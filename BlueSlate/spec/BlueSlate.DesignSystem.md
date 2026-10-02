# Blue-Slate Design System

Version: 0.5.0
Status: candidate-active local standard
Visual references: `spec/mockups/Blue Slate Bootstrap Theme Board.png` and `spec/mockups/blue-slate-semantic-swatches.png`

Blue-Slate is the Aptlantis house system for local-first tools, archival project pages, command surfaces, evidence dashboards, and Windows desktop utilities. It is not a broad public design framework. It is a compact, opinionated standard for the products this workspace tends to produce.

## Design Intent

Blue-Slate should feel dark, technical, archival, maritime, precise, calm, and evidence-driven. The base interface is mostly neutral blue-black structure. Signal colors are injected only when they communicate state, hierarchy, proof, action, or risk.

The governing ratio is:

- Base neutrals: about 85 percent of the interface.
- Signal accents: about 15 percent of the interface.

This ratio fixes the earlier problem where pages were navigable and organized but too even-toned. A screen should never depend on color noise, but important actions and states must have enough contrast to be found quickly.

## Canonical Sources

Use the reviewed Bootstrap Theme Board for visual hierarchy, density, component states, and framework treatment, and the semantic swatch board for the current palette. Exact token names and values come from TOML: raster labels, Bootstrap-specific ramps, and older mockups do not override that matrix. The asset catalog records these roles and preserved lineage.

The extracted palette files are source material, not direct implementation standards. Do not import their generated Tailwind scales wholesale; they contain duplicate names, extra blues, and warm families that would compete with the primary system if treated as peers.

## Token Model

The system has five canonical token layers plus framework translations:

1. Raw palette tokens: stable named color values.
2. Semantic tokens: UI meanings such as background, panel, text, border, action, warning, success, taxonomy, and focus.
3. Component tokens: values consumed by buttons, chips, cards, code blocks, forms, tabs, windows, and evidence panels.
4. Foundation tokens: radii, spacing, elevation, and focus metrics.
5. Typography tokens: display, sans, and mono stacks.

Framework translations: generated neutral CSS, Tailwind aliases, a SiYuan compatibility adapter, XAML resources, and Tauri/React usage patterns.

The canonical machine-readable token source is `spec/tokens/BlueSlate.Tokens.toml`. Each palette role deliberately carries exact sRGB hex and OKLCH values; CSS consumers use the generated `generated/BlueSlate.Tokens.css` translation, including both explicit `-hex` and `-oklch` custom properties.

## Expanded Semantic Contract

Semantic tokens now distinguish the operational conditions that desktop interfaces need to communicate:

| Group | Roles |
| --- | --- |
| Surfaces | canvas, recessed canvas, panel, raised panel, accent panel, overlay, popover, input, table, disabled |
| Content | primary, emphasis, secondary, tertiary, disabled, link, link-hover, code, code-accent |
| Structure | standard, soft, strong, and translucent borders |
| Intent | primary, secondary, success, info, warning, danger, attention, taxonomy, archive, verified |
| Interaction | action, secondary action, hover, active, disabled, and focus |
| Validation | valid/valid-border and invalid/invalid-border |
| Foundation | radii, elevation, spacing, and focus-ring metrics |

Use these roles before raw palette tokens. A framework may expose compatibility aliases or more detailed component variables, but it must map them back to this contract rather than making framework names canonical.

## Interaction, Status, and Accessibility

- Default, hover, focus, active, disabled, valid, and invalid states must remain distinguishable at normal working density.
- Focus uses the cyan/arctic semantic path and must be visible by keyboard, not inferred from hover styling.
- Intent color communicates meaning only with a text label, icon, or other non-color cue for status and validation.
- Check normal text at 4.5:1 minimum and large text or non-text interactive indicators at 3:1 minimum against the rendered surface.
- Disabled state communicates unavailable action without erasing legibility or the reason it is unavailable.

## Accent Semantics

Use accents sparingly and consistently:

| Accent | Use |
| --- | --- |
| Cyan / electric | Focus, primary actions, active navigation, glow, live interaction |
| Teal | Selected technical surfaces, secondary emphasis, data surfaces |
| Amber / brass | Warnings, priority, preflight notes, attention |
| Violet / indigo | Taxonomy, special states, vault/archive markers |
| Green | Verified, success, healthy, complete |

Avoid using accents as decoration. If an accent does not carry meaning, use a neutral token instead.

## Surface Rules

- Use `semantic.surface.canvas` and `semantic.surface.canvas-recessed` for the app canvas.
- Use `semantic.surface.panel`, `semantic.surface.panel-raised`, and `semantic.surface.panel-accent` for grouped UI.
- Use `semantic.structure.border` and `semantic.structure.border-soft` for structure before using bright outlines.
- Use `semantic.content.primary`, `semantic.content.secondary`, and `semantic.content.tertiary` to create hierarchy before reaching for accent color.
- Reserve `semantic.interaction.action` and `semantic.interaction.focus` for controls that need user attention.
- Reserve `semantic.intent.warning`, `semantic.intent.success`, and `semantic.intent.taxonomy` for meaningful status states.

## Do / Avoid

Do:

- Use evidence grids, code surfaces, status chips, and command panels as first-class visual forms.
- Keep density compact for operational tools.
- Use cyan to orient the user toward the active task.
- Use warm amber only for risk, warning, priority, or command-output attention.
- Keep screenshots, generated boards, and palette extracts traceable through `reports/source-inventory-2026-09-27.json` and the asset catalog.

Avoid:

- All-neutral screens where nothing has priority.
- Decorative accent scatter.
- Multiple competing blue scales.
- Large generic marketing layouts for tools that should feel operational.
- Treating WPF, WinUI, and Tailwind as interchangeable. They share tokens, not implementation mechanics.

## Required Companion Specs

- Integrated overview and section anatomy: `spec/BlueSlate.Overview.md`
- Layout vocabulary: `spec/layout/BlueSlate.LayoutPatterns.md`
- Tailwind translation: `spec/frameworks/BlueSlate.Tailwind.md`
- WPF translation: `spec/frameworks/BlueSlate.WPF.md`
- WinUI translation: `spec/frameworks/BlueSlate.WinUI.md`
- Tauri/React profile: `spec/frameworks/BlueSlate.TauriReact.md`
- Bootstrap 5.3 profile: `spec/frameworks/BlueSlate.Bootstrap53.md`
- Asset baseline: `spec/assets/BlueSlate.Assets.md`

## Framework Boundary and Compatibility

Framework profiles share the token source and semantic meaning, not implementation mechanics. Bootstrap 5.3 is a preserved v0.3 compatibility profile that supplies its required contextual families, RGB channels, subtle variants, and component aliases; those values are translation details and may differ from framework-neutral defaults. Existing adopter profiles remain usable at their recorded versions. Starter packs are partial pilots, not evidence of complete control coverage; see the framework coverage matrix in Migration-0.5.md.

Blue Slate is deliberately single-theme dark. This version does not introduce a light palette or a color-mode switch.
