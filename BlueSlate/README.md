# Blue Slate Visual System

![Standard](https://img.shields.io/badge/visual%20system-blue.slate%20v0.5.0-blue)
![Manifest](https://img.shields.io/badge/manifest-entity--named%20TOML-orange)
![Scope](https://img.shields.io/badge/scope-design%20tokens%20and%20layout-green)
![Status](https://img.shields.io/badge/status-candidate--active-lightgrey)

Blue Slate is the Aptlantis visual-system standard for local-first tools, archival project pages, evidence dashboards, command surfaces, and Windows desktop utilities.

It is candidate active: projects may adopt it deliberately, but each adoption should record whether it is a pilot, an active dependency, or a project-specific profile.

## Document Suite

| File | Purpose |
| --- | --- |
| `spec/BlueSlate.DesignSystem.md` | Primary visual-system specification. |
| `spec/BlueSlate.Overview.md` | Integrated overview: token layers, page-section anatomy, patterns, states, and conformance rules. |
| `BlueSlate.manifest.toml` | Standard suite manifest. |
| `Adoption-Guide.md` | How projects adopt Blue Slate. |
| `Validation-Checklist.md` | Suite and adopter validation checklist. |
| `CHANGELOG.md` | Version and promotion history. |
| `Migration-0.5.md` | Source authority, preserved v0.3 interfaces, and migration choices. |
| `spec/tokens/Token-Contract.md` | Token structure and executable validation contract. |
| `templates/BlueSlate-Adoption.toml` | Adopter record template. |
| `examples/BlueSlate-Suite-Map.md` | Suite and domain artifact map. |
| `skills/aptlantis-blue-slate/SKILL.md` | Comprehensive agent workflow. |
| `reports/Review-2026-09-27.md` | Directory review, maturity decision, verification, and recovery. |
| `spec/tokens/BlueSlate.Tokens.toml` | Canonical dual-representation token source: exact hex plus OKLCH. |
| `generated/BlueSlate.Tokens.css` | Generated framework-neutral CSS token translation. |
| `spec/layout/BlueSlate.LayoutPatterns.md` | Reusable layout vocabulary. |
| `spec/frameworks/` | Tailwind, Tauri/React, SiYuan, WinUI, WPF, and legacy Bootstrap implementation boundaries. |
| `spec/frameworks/BlueSlate.Bootstrap53.md` | Bootstrap 5.3 translation profile. |
| `spec/frameworks/validate_bootstrap53_profile.py` | Checks the Bootstrap profile's token/alias mapping boundary. |
| `starter-packs/` | Pilot implementation resources, including a Bootstrap 5.3 state example. |
| `spec/mockups/` | Reviewed visual boards and historical mockups; see the asset catalog. |

## Role

Blue Slate governs Aptlantis visual-system decisions when a project explicitly adopts it:

- semantic color tokens and token translation,
- layout patterns for operational project surfaces,
- framework-specific implementation profiles,
- evidence-first visual treatment for project pages, tools, dashboards, and desktop utilities.

Blue Slate does not replace NeonInk or SESM.
[NeonInk v0.2](../NeonInk/README.md) is the data-presentation companion for charts, reports, dataset profiles and visual artifacts. Blue Slate is the house theme for dense operational applications; embedded NeonInk presentations preserve the host shell. SESM governs embedded semantic metadata in SVG assets.

## Read First

1. `README.md`
2. `spec/BlueSlate.Overview.md`
3. `spec/BlueSlate.DesignSystem.md`
4. `spec/tokens/BlueSlate.Tokens.toml`
5. `spec/layout/BlueSlate.LayoutPatterns.md`
6. the relevant framework profile, including `BlueSlate.Bootstrap53.md` for Bootstrap 5.3
7. `Adoption-Guide.md`
8. `Validation-Checklist.md`

## Maturity

Candidate active v0.5.0.

The token source, layout vocabulary, framework notes, and starter packs are usable for active work, but Blue Slate still needs more real adopter evidence before being called stable or reference. Run `tools/Compile-BlueSlate.ps1`, then `tools/Audit-BlueSlate.ps1` before adopting a generated output.

## Compile and validate

Requires Python 3.11+, PowerShell 7, and Node.js. ImageMagick is optional for board/palette generation. No third-party Python package is required by the compiler.

```powershell
python tools/compile_blueslate.py
python tools/compile_blueslate.py --check
pwsh -NoProfile -ExecutionPolicy Bypass -File tools/Test-BlueSlate.ps1
pwsh -NoProfile -ExecutionPolicy Bypass -File tools/Audit-BlueSlate.ps1
python tools/test_compiler.py
python tools/validate_suite.py
python spec/frameworks/validate_bootstrap53_profile.py
```

For a Python executable outside PATH, set `BLUESLATE_PYTHON` to its absolute path for the PowerShell wrappers. The compiler also accepts `--source` and `--output`; `--check` performs no writes and fails for missing or stale outputs. The audit writes only its named report after checks pass.

City Hall is the active authority. The desktop tree is the reviewed source workspace for this release, not a second governing standard. Future work can be staged in zoning without moving or renaming this preserved workspace.
