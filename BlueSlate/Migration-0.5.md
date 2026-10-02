# Blue Slate 0.5 adoption and compatibility

Date: 2026-09-27. Suite version: 0.5.0. Maturity: Candidate; lifecycle: candidate-active.

This release adopts the reviewed desktop work into `D:\.city_hall\BlueSlate`. The desktop source remains at its exact physical path, `C:\Users\Administrator\Desktop\BlueSlate\BlueSlate`. It was developed outside zoning; this explicit review and adoption records that provenance without pretending it was a registered zoning project.

## Authority

The City Hall `spec/tokens/BlueSlate.Tokens.toml` is the single editable token authority. The design-system specification, overview, layout catalog and asset catalog govern their respective concerns. The Bootstrap Theme Board and semantic swatches are adopted visual references. Exact values come from TOML when raster labels, old boards, or framework ramps differ.

The duplicate TOML, layout document and swatch board formerly under `skills/` were byte-identical to the `spec/` copies and were consolidated. The Bootstrap board moved to `spec/mockups/`; `PaletteGenerator32.ps1` moved to `tools/`. The two fragment skills are superseded by `skills/aptlantis-blue-slate`. Their original bytes are preserved in the desktop recovery archive described in the review report.

## Version choice

0.5.0 adds the reviewed overview/layout guidance, source tooling, validation, asset provenance, adopter record and comprehensive skill to City's v0.3.0 suite, incorporating the desktop's v0.4.0 and v0.4.1 work. All 27 desktop palette entries, roles, semantic/component values, foundation and typography values are preserved; only source version metadata changes. Compatibility interfaces remain available, so this is a pre-1.0 minor release rather than a forced adopter migration.

## Consumer paths

| Interface | Status | Migration |
| --- | --- | --- |
| `spec/tokens/BlueSlate.Tokens.toml` | Current editable source, 0.5.0 | Edit here, compile, validate, then publish chosen outputs. |
| `generated/BlueSlate.Tokens.css` | Current neutral CSS | Uses `--bs-semantic-*`, `--bs-component-*`, palette `-hex`/`-oklch` and foundation tokens. |
| `generated/BlueSlate.Tokens.json` | Current TOML-shaped export | Hyphenated palette keys and grouped references; not schema-compatible with the v0.3 JSON. |
| `spec/tokens/BlueSlate.Tokens.json` | Frozen v0.3 legacy interface | Preserved byte-for-byte for old consumers; never edit or overwrite it with new-schema output. |
| `spec/tokens/BlueSlate.Tokens.css` | Frozen v0.3 legacy CSS | Preserved byte-for-byte; migrate selectors and roles deliberately instead of changing imports alone. |

The new CSS carries exact hex alongside OKLCH, but semantic declarations use OKLCH. It is not an automatic fallback stylesheet for old renderers. For hex-only targets, resolve semantic roles through the palette's `hex` value in an explicit adapter. JSON exports preserve token references; consumers needing resolved values must resolve them, not treat `{semantic...}` as a color.

## Framework coverage

| Target | Supplied implementation | Remaining boundary |
| --- | --- | --- |
| Neutral CSS | Deterministic current token translation and static HTML specimen | Specimen is illustrative; no product behavior or adopter verification is implied. |
| Tailwind v4 | Six generated color aliases with neutral CSS import | Build input, not directly browser-ready CSS. `atl-*` classes in the markup recipe are app-owned suggestions. `sample-built.css` must be produced by the adopter. |
| Tauri/React | Stack and component guidance | No runnable Tauri project or React component library shipped. |
| SiYuan | 22 `--b3-*` mappings | Partial adapter. Verify actual supported variables, hover behavior, states and CSS loading in the target SiYuan version. |
| WPF | Colors, brushes, merged entry dictionary, shell sample and Filing Cabinet pilot | Partial resources, not complete templates or runtime proof. Pilot-specific colors such as `Danger=#FF5C77` and dim surfaces remain recorded local deviations, not canonical changes. |
| WinUI | One resource dictionary and shell sample | Partial resources; proposed multi-file architecture and native control states are not implemented here. |
| Bootstrap 5.3 | Frozen v0.3 CSS, state markup, alias/contrast checker | Legacy compatibility evidence, not a current compiler target. Supply local Bootstrap CSS; rendered interaction and alpha-composite contrast remain adopter checks. |

New framework work, including JetBrains or Carbon, starts with a role-to-target adapter. It does not introduce framework names into canonical token layers. Preserve the host framework's component anatomy, keyboard behavior, accessibility and native resource mechanics.

## Maturity decision

SFDS distinguishes suite structure from adopter/domain validation. This release supplies a navigable specification, templates, examples, source contract and executable checks. Stable is not claimed: partial native/SiYuan profiles and Bootstrap still need representative runtime state and adoption evidence. A board, generated output, XML parse or passing source audit is not evidence that a live app behaves correctly.

For the next maturity review, record real adopters with version/profile, representative screens, default/hover/focus/active/disabled and form states, contrast on rendered backgrounds, keyboard traversal, responsive behavior and local deviations. Scope the promotion to the coverage actually demonstrated. NeonInk and SESM remain independent adjacent standards; merging them is not required for Blue Slate maturity.

## 2026-10-02 gap-analysis review

Inspected compiler and adapter inputs explicitly use TOML or current generated JSON. No silent directory-scanning fallback to legacy JSON was found. Retaining the frozen v0.3 interfaces does not give them current authority. They remain pinned compatibility resources at their original paths; moving them would break documented consumers without proving a fix. New adapters must choose TOML or generated translations explicitly. External consumer misuse remains an adopter audit item.
