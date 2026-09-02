# Blue-Slate Design System

Version: 0.1.0
Status: formalized local standard
Canonical board: `AptlantisBlue-Slate.png`

Blue-Slate is the Aptlantis house system for local-first tools, archival project pages, command surfaces, evidence dashboards, and Windows desktop utilities. It is not a broad public design framework. It is a compact, opinionated standard for the products this workspace tends to produce.

## Design Intent

Blue-Slate should feel dark, technical, archival, maritime, precise, calm, and evidence-driven. The base interface is mostly neutral blue-black structure. Signal colors are injected only when they communicate state, hierarchy, proof, action, or risk.

The governing ratio is:

- Base neutrals: about 85 percent of the interface.
- Signal accents: about 15 percent of the interface.

This ratio fixes the earlier problem where pages were navigable and organized but too even-toned. A screen should never depend on color noise, but important actions and states must have enough contrast to be found quickly.

## Canonical Sources

Use `AptlantisBlue-Slate.png` as the canonical visual reference because it includes the expanded accent revision. Use `AptlantisBlue-Slate-1.png`, existing project screenshots, and extracted palettes as supporting evidence.

The extracted palette files are source material, not direct implementation standards. Do not import their generated Tailwind scales wholesale; they contain duplicate names, extra blues, and warm families that would compete with the primary system if treated as peers.

## Token Model

The system has four token layers:

1. Raw palette tokens: stable named color values.
2. Semantic tokens: UI meanings such as background, panel, text, border, action, warning, success, taxonomy, and focus.
3. Component tokens: values consumed by buttons, chips, cards, code blocks, forms, tabs, windows, and evidence panels.
4. Framework translations: Tailwind CSS variables/classes, XAML resources, WinUI resources, and Tauri/React usage patterns.

The canonical machine-readable token source is `spec/tokens/BlueSlate.Tokens.json`. CSS consumers can start from `spec/tokens/BlueSlate.Tokens.css`.

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

- Use `background` and `background-soft` for the app canvas.
- Use `panel`, `panel-raised`, and `panel-blue` for grouped UI.
- Use `border` and `border-soft` for structure before using bright outlines.
- Use `text`, `text-soft`, and `text-muted` to create hierarchy before reaching for accent color.
- Reserve `action` and `focus` for controls that need user attention.
- Reserve `warning`, `success`, and `taxonomy` for meaningful status states.

## Do / Avoid

Do:

- Use evidence grids, code surfaces, status chips, and command panels as first-class visual forms.
- Keep density compact for operational tools.
- Use cyan to orient the user toward the active task.
- Use warm amber only for risk, warning, priority, or command-output attention.
- Keep screenshots, generated boards, and palette extracts traceable through `references/source-manifest.json`.

Avoid:

- All-neutral screens where nothing has priority.
- Decorative accent scatter.
- Multiple competing blue scales.
- Large generic marketing layouts for tools that should feel operational.
- Treating WPF, WinUI, and Tailwind as interchangeable. They share tokens, not implementation mechanics.

## Required Companion Specs

- Layout vocabulary: `spec/layout/BlueSlate.LayoutPatterns.md`
- Tailwind translation: `spec/frameworks/BlueSlate.Tailwind.md`
- WPF translation: `spec/frameworks/BlueSlate.WPF.md`
- WinUI translation: `spec/frameworks/BlueSlate.WinUI.md`
- Tauri/React profile: `spec/frameworks/BlueSlate.TauriReact.md`
- Asset baseline: `spec/assets/BlueSlate.Assets.md`
