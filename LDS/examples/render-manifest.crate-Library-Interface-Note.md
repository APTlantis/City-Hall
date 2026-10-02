# render-manifest.crate Library Interface Note

Example status: candidate adopter example for LDS v0.2.0.

This is an example adopter-facing record for the proposed `render-manifest.crate` family. It is evidence from intake and planning, not proof of an implemented API.

## Library Surface

Expected library crates:

- `manifest-render-core`
- `manifest-render-schema`
- `manifest-render-html`

Expected public model:

- parse structured TOML records,
- validate record shape and presentation intent,
- produce a renderer-neutral document model,
- expose renderer extension contracts for outputs such as HTML, Markdown, React, CLI output, or service responses.

The exact Rust API is speculative until implementation begins.

## Stability Level

`experimental`

The public API does not exist yet. Breaking changes are expected while the PPS proposal remains draft and the first implementation phase has not started.

## Versioning And Breaking Changes

No versioning policy can be enforced until the first crate version exists.

Before this project can claim `interface-stable`, it must record:

- crate names,
- public modules and entry points,
- supported input/output model,
- extension traits or interfaces,
- minimum supported Rust version,
- changelog location,
- breaking-change policy.

## Extension Contracts

Potential extension point: renderer interface or trait for converting the normalized document model into HTML, Markdown, React-ready JSON, CLI output, or service responses.

This remains speculative until the core model exists.

## Known Consumers

Known candidate consumers:

- future CLI surface governed by CTS,
- future Axum/service surface governed by SIS,
- project pages or documentation surfaces that need manifest-driven rendering.

No real consumers exist yet.

## Companion Crates

| Crate | Standard |
| --- | --- |
| `manifest-render-core` | LDS |
| `manifest-render-schema` | LDS |
| `manifest-render-html` | LDS |
| `manifest-render-cli` | CTS |
| `manifest-render-axum` | SIS |

## Known Gaps

- No source code exists yet.
- Public API is speculative.
- Versioning policy is deferred until the first crate exists.
- LDS itself may need refinement after this candidate adopter encounters real implementation pressure.
