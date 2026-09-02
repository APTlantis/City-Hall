# Blue-Slate Tauri / Vite / React Profile

Target: local-first desktop/web hybrid apps built with Tauri, Vite, React, and Tailwind.

## Baseline Stack

- Tailwind v4 CSS-first theme from `aptlantis-blue-slate.tailwind.css`.
- Local Material Symbols font assets.
- Aptos / Segoe / system font stack.
- Prism with Okaidia-compatible token overrides for code surfaces.
- Mermaid bundled locally when diagrams are part of the app.

## App Shape

Use the first screen as the tool itself. Do not insert a marketing landing page before the actual workflow.

Recommended shell:

```text
Top command bar
Primary work area
Left rail or tabs when structure is needed
Evidence/code/output panel
Bottom status strip
```

## Expected Components

- Project or tool hero panel when context is needed.
- Tabs for Overview, Usage, Screenshots, Builder, Evidence, Releases.
- Evidence Grid for manifests, hashes, generated files, and verification.
- Command Builder for local CLI workflows.
- Code Panel for generated command, JSON, TOML, logs, and Mermaid source.
- Status Chips for lifecycle, active-core, verified, warning, taxonomy, archive.
- Instrument Panel for readiness, health, test coverage, data quality, and last run.

## Local Asset Rules

- Bundle icons and fonts with the app instead of using CDN URLs.
- Keep the app functional offline.
- Keep image and screenshot references deterministic.
- Use `public/assets/blue-slate/` or an equivalent app-local path for bundled design assets.

## Accessibility Rules

- Do not rely on color alone for warnings, success, or active states.
- Pair chips with text labels.
- Keep focus rings visible with cyan/arctic tokens.
- Preserve keyboard navigation for tabs, forms, command builders, and copy buttons.
