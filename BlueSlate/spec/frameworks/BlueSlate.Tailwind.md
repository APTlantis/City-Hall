# Blue-Slate Tailwind Profile

Target: Tailwind v4 CSS-first projects, especially Vite/React/Tauri apps and Aptlantis project pages.

Primary files:

- `aptlantis-blue-slate.tailwind.css`
- `spec/tokens/BlueSlate.Tokens.css`
- `spec/tokens/BlueSlate.Tokens.json`

## Implementation Rules

- Import `aptlantis-blue-slate.tailwind.css` as the app's main Tailwind input or from the app CSS entrypoint.
- Keep token names stable. Add semantic aliases before adding new raw colors.
- Use `atl-*` classes for reusable Blue-Slate primitives and ordinary Tailwind utilities for local layout.
- Use the signal accent classes only for meaningful state.

## Required Surface Classes

The Tailwind profile should provide:

- `atl-shell` for the global canvas and technical grid.
- `atl-container` for constrained page width.
- `atl-panel`, `atl-card`, and `atl-card-soft` for structured surfaces.
- `atl-button`, `atl-button-secondary`, `atl-button-warning`, and `atl-button-ghost` for actions.
- `atl-chip-*` for verified, warning, taxonomy, archive, active, and neutral status.
- `atl-code` plus Prism/Okaidia-compatible token colors.
- `atl-form-field`, `atl-input`, `atl-checkbox-row`, and `atl-command-output` for command builders.
- `atl-tabs` and `atl-tab-active` for project/detail navigation.
- `atl-evidence-grid` and `atl-evidence-item` for proof surfaces.

## Page Shell Recipe

Use this recipe for project detail pages:

```html
<main class="atl-shell">
  <section class="atl-container py-10">
    <article class="atl-panel atl-ornament p-8">
      <p class="atl-eyebrow">Project / Evidence</p>
      <h1 class="atl-title">Project Name</h1>
      <p class="atl-subtitle">Short operational description.</p>
      <div class="atl-signal-row">
        <span class="atl-chip-active">Active-core</span>
        <span class="atl-chip-warning">Paused</span>
        <span class="atl-chip-taxonomy">CTS</span>
      </div>
    </article>
  </section>
</main>
```

## Prism/Okaidia

Okaidia works well with the system because it keeps code surfaces dark and high-contrast. Override Prism tokens only enough to connect them to Blue-Slate:

- keyword/function: cyan
- string/attr-value: green
- number/boolean: brass
- punctuation/operator: pale mist
- comment: mist grey
- deleted/error: amber

## Visual QA

Check that primary actions, active tabs, warning notes, status chips, and generated-command blocks are visibly distinct from neutral panels. If a page feels technically correct but inert, add semantic signal accents before changing layout.
