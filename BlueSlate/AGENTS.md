# Blue Slate Instructions

Inherit [drive instructions](D:/AGENTS.md), then read `README.md`, `BlueSlate.manifest.toml`, and `Project-README.md` before changing Blue Slate material. Consult City Hall records before changing promotion status.

## Role

Blue Slate is a candidate-active Aptlantis visual-system standard. It is related to NeonInk but does not replace NeonInk or SESM.

## Local Rules

- Treat `spec\tokens\BlueSlate.Tokens.toml` as the current source of truth; generated translations live in `generated\`.
- Keep generated or translated resources aligned with the token source.
- Preserve framework-specific starter packs as pilot implementation resources.
- Describe Blue Slate as candidate active after the 2026-07-25 City Hall promotion record.
- When a project adopts Blue Slate, record that adoption as `pilot`, `active`, or `project-profile` according to the project's current state.
- Read `Migration-0.5.md` before migrating legacy JSON/CSS consumers or claiming framework coverage.
- Use `skills/aptlantis-blue-slate/SKILL.md` for comprehensive theming, layout, adapter, asset and validation work.
- City Hall is the active authority. The desktop tree is a reviewed source workspace; its manifest points to the canonical destination, not a second active standard.
- Run compiler freshness, conversion and declared contrast checks for token/output changes; record runtime evidence separately.

