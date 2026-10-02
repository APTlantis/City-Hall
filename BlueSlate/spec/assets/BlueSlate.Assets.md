# Blue-Slate Assets

## Standard Baseline

Blue-Slate prefers Material Symbols plus Aptos where available and licensed. This suite does not ship font or icon binaries; use the declared fallbacks or a host framework's native assets.

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

## Reviewed visual references

| File under spec/mockups | Authority and use |
| --- | --- |
| `Blue Slate Bootstrap Theme Board.png` | User-designated visual reference for dense surfaces, hierarchy, typography, component anatomy and states. Bootstrap ramps and raster labels remain profile evidence. |
| `blue-slate-semantic-swatches.png` | User-designated palette reference, generated from the 27-color TOML palette. The TOML provides exact values. |
| `blue.slate_overview.png` | Preserved early overview; useful visual lineage, not current numeric token authority. |
| `blue.slate_mockups.png` | Preserved project/command/native shell compositions; not runtime screenshots or adopter verification. |

Former filenames `AptlantisBlue-Slate.png`, `AptlantisBlue-Slate-1.png`, `SanityCheck-1.png`, `SanityCheck-2.png`, `Structra-JSON.png`, and `Structra-TOML.png` are historical references not present in this reviewed tree. They are not required inputs.

The board's reduced-motion, non-color status, clear focus, restrained texture, and readable dense tables inform implementation. Numeric typography scales and framework-specific chart colors require an explicit adapter or project profile; do not transcribe uncertain raster text as new canonical values.

## Logos and embedded metadata

Use the current tools under `D:\CTS\Aptlantis Logos\scripts` for conversion and embedding. Read that project's `AGENTS.md` and `scripts/help.md` first. `D:\.city_hall\SESM` owns the metadata schema, conformance, privacy and safe profile. The Aptlantis Logos CLI differs from the reference CLI shipped inside SESM; do not mix flags. See the comprehensive skill's asset workflow.

Image-derived palettes, including the preserved HolyC example, are candidate extraction evidence. `tools/PaletteGenerator32.ps1` emits a different theme TOML format; it cannot replace `spec/tokens/BlueSlate.Tokens.toml` directly.
