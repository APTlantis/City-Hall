# Implementation profiles

These are translation guidance, not tested integrations with every named framework.

## CSS and React

Use generated CSS in a standalone report. For embedding, transform the two generated selectors `:root, .neonink` to `.neonink` in a build adapter and record that transformation; never edit the generated canonical file. Scope component rules beneath `.neonink`. React uses the same CSS variables and semantic HTML. Keep actual buttons, tables, headings, labels and focus behavior. Avoid replacing a working component library for theme reasons.

```css
.neonink { color: var(--ni-text); background: var(--ni-canvas); }
.neonink .report-panel { background: var(--ni-panel); padding: 24px; border-radius: 8px; }
.neonink :focus-visible { outline: 2px solid var(--ni-focus); outline-offset: 3px; }
.neonink .source { color: var(--ni-muted); }
```

## SVG and chart libraries

For standalone SVG, resolve the generated JSON palette to hex; do not rely on CSS variables surviving export. Include title/description, visible legends and source, and accessible adjacent data. For canvas charts, provide semantic HTML summary/table outside the canvas. Bind stable series keys to the categorical scale, and expose values without hover. Library defaults for smoothing, interpolation, missing values and axes must be reviewed explicitly.

## Tailwind

Map project utilities to the generated semantic variables through the project's installed Tailwind version and existing configuration. Do not assume v3 and v4 configuration syntax is interchangeable. Utilities are adapters, not canonical tokens. Keep a scoped report boundary when the host is Blue Slate.

## Native WPF/WinUI and desktop hosts

Use the hex values from the generated JSON to create native color/brush resources for the presentation region. Preserve host controls, high-contrast behavior, DPI layout, automation names and keyboard navigation. A web/SVG reference is not native runtime evidence. Record mapping and verify at real DPI and export size before adoption.

## Slides, print, and raster

Use sRGB outputs with embedded/declared profiles when supported by the export tool. Convert text to accessible editable text where the format allows; retain a data table or accompanying notes. The dark profile is suited to screens; paper output needs an explicitly reviewed paper treatment. Verify exported page dimensions, clipping, font substitution, units and source legibility. Do not call a PNG an editable slide template.
