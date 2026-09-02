# Blue-Slate Assets

## Standard Baseline

Blue-Slate uses Material Symbols plus Aptos as the default bundled asset baseline.

Font stacks:

```text
Display: Aptos Display, Segoe UI Variable Display, Segoe UI, system-ui, sans-serif
UI sans: Aptos, Segoe UI Variable Text, Segoe UI, system-ui, sans-serif
Mono: Cascadia Code, Cascadia Mono, JetBrains Mono, SFMono-Regular, Consolas, monospace
Optional web fallback: Inter
```

## Icons

Default icon set: Material Symbols.

Use icons for:

- action buttons
- project metadata
- file/resource types
- status chips
- navigation tabs
- command-builder operations
- evidence categories

Do not use icons as decorative filler. Every icon should clarify type, state, or action.

## Bundling

Blue-Slate apps are usually local-first. Bundle required icon/font assets with the app where licensing permits. Avoid runtime CDN dependencies for core UI.

Suggested app-local path:

```text
public/assets/blue-slate/
  fonts/
  icons/
  boards/
  textures/
```

## Visual Motifs

Approved motifs:

- technical grid
- thin-line compass/target marks
- starfield/depth texture
- circuit traces
- ocean flow
- SGML/markup fragments
- signal glow

Use these at low opacity. They should never compete with content.

## Current Source Boards

- Canonical: `AptlantisBlue-Slate.png`
- Supporting: `AptlantisBlue-Slate-1.png`
- Sanity checks: `SanityCheck-1.png`, `SanityCheck-2.png`
- Desktop code surfaces: `Structra-JSON.png`, `Structra-TOML.png`
