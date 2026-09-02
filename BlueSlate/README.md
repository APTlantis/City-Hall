# Blue Slate Visual System

![Standard](https://img.shields.io/badge/visual%20system-blue.slate%20v0.2.0-blue)
![Manifest](https://img.shields.io/badge/manifest-entity--named%20TOML-orange)
![Scope](https://img.shields.io/badge/scope-design%20tokens%20and%20layout-green)
![Status](https://img.shields.io/badge/status-candidate--active-lightgrey)

Blue Slate is the Aptlantis visual-system standard for local-first tools, archival project pages, evidence dashboards, command surfaces, and Windows desktop utilities.

It is candidate active: projects may adopt it deliberately, but each adoption should record whether it is a pilot, an active dependency, or a project-specific profile.

## Document Suite

| File | Purpose |
| --- | --- |
| `spec/BlueSlate.DesignSystem.md` | Primary visual-system specification. |
| `BlueSlate.manifest.toml` | Standard suite manifest. |
| `Adoption-Guide.md` | How projects adopt Blue Slate. |
| `Validation-Checklist.md` | Suite and adopter validation checklist. |
| `CHANGELOG.md` | Version and promotion history. |
| `spec/tokens/BlueSlate.Tokens.json` | Canonical token source. |
| `spec/tokens/BlueSlate.Tokens.css` | CSS token translation. |
| `spec/layout/BlueSlate.LayoutPatterns.md` | Reusable layout vocabulary. |
| `spec/frameworks/` | Tailwind, Tauri/React, WinUI, and WPF implementation notes. |
| `starter-packs/` | Pilot implementation resources. |
| `apps/`, `spec/mockups/` | Visual references and screenshots. |

## Role

Blue Slate governs Aptlantis visual-system decisions when a project explicitly adopts it:

- semantic color tokens and token translation,
- layout patterns for operational project surfaces,
- framework-specific implementation profiles,
- evidence-first visual treatment for project pages, tools, dashboards, and desktop utilities.

Blue Slate does not replace NeonInk or SESM.
NeonInk remains the broader visual-language lineage, while SESM governs embedded semantic metadata in SVG assets.

## Read First

1. `README.md`
2. `spec/BlueSlate.DesignSystem.md`
3. `spec/tokens/BlueSlate.Tokens.json`
4. `Adoption-Guide.md`
5. `Validation-Checklist.md`

## Maturity

Candidate active v0.2.0.

The token source, layout vocabulary, framework notes, and starter packs are usable for active work, but Blue Slate still needs more real adopter evidence before being called stable or reference.
