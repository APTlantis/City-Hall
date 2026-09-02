# Blue Slate Adoption Guide

Use Blue Slate when an Aptlantis project needs a local-first, operational visual system for project pages, evidence dashboards, command surfaces, desktop utilities, or documentation tools.

## Adoption Steps

1. Confirm the project has WGS identity records and, when needed, PPS intent records.
2. Record Blue Slate in the project manifest or README as a visual-system dependency.
3. State the adoption level: `pilot`, `active`, or `project-profile`.
4. Use `spec/tokens/BlueSlate.Tokens.json` as the token source of truth.
5. Use semantic tokens before adding raw colors.
6. Choose the relevant framework profile from `spec/frameworks/`.
7. Use one primary layout pattern from `spec/layout/BlueSlate.LayoutPatterns.md` and no more than two secondary patterns per page or surface.
8. Record any local deviations, missing tokens, or project-specific accessibility findings.

## Bootstrap 5.3 Adoption

For Bootstrap 5.3 adopters:

1. Bundle Bootstrap 5.3.x locally and load `starter-packs/bootstrap53/aptlantis-blue-slate.bootstrap53.css` after it.
2. Record `BlueSlate.Bootstrap53` as the framework profile and `0.3.0` as the token source version.
3. Use semantic contextual components for declared intent, not decorative color.
4. Review the state matrix in `starter-packs/bootstrap53/sample-surface.html`; document any component override or local profile decision.
5. Complete contrast and keyboard-focus checks on the rendered adopter surface.

## Adoption Levels

| Level | Meaning |
| --- | --- |
| `pilot` | The project is testing Blue Slate and may diverge while the fit is evaluated. |
| `active` | The project treats Blue Slate as its visual-system baseline. |
| `project-profile` | The project uses Blue Slate tokens and rules with documented local additions or constraints. |

## Relationship To Adjacent Standards

- WGS governs workspace placement, manifests, and project registration.
- PPS governs project intent and readiness.
- NeonInk provides visual-language lineage and broader semantic color context.
- SESM governs embedded semantic metadata in SVG assets.
- WDS, DRS, and CTS govern delivery-specific behavior when the Blue Slate surface is a website, desktop app, or command tool.

## Adoption Record

An adopting project should record:

- adoption level,
- token source version,
- framework profile used,
- Bootstrap version when the Bootstrap profile is used,
- primary layout pattern,
- local deviations,
- accessibility/contrast and state-coverage checks performed,
- known gaps or deferred visual cleanup.
