# Blue Slate token contract

Schema identifier: `aptlantis.blue-slate.tokens`, schema version `1.0`. Suite/source version: `0.5.0`.

The source is UTF-8 TOML parsed with Python 3.11+ `tomllib`. Duplicate keys/tables and invalid TOML fail. `tools/compile_blueslate.py` is the executable source contract, not a generic theme TOML converter.

- `[meta]` identifies schema, semantic version, name, source format and `dark-only` theme mode.
- `[policy]` declares canonical layers, framework boundaries and migration policy.
- `[palette.<name>]` contains six-digit sRGB `hex`, an `oklch(L C H)` representation and a nonempty `role`. Neither color representation replaces the other. `Test-ColorConversions.js` independently verifies the conversion of all 27 palette entries.
- `[semantic.*]`, `[component.*]`, `[foundation.*]` and `[typography]` contain scalar values or whole-value references such as `{semantic.surface.panel}`. References may target only canonical layers. Missing references, table-valued references and cycles fail across every emitted layer and adapter.
- `[framework.tailwind]` and `[framework.siyuan]` map target names to canonical references. These tables do not define new canonical roles.
- `[audit.pairs]` contains nonempty `normal-text` and `indicators` arrays of `foreground.path|background.path`. The current audit requires opaque palette-backed colors. Literal OKLCH and alpha composites require separate rendered analysis.

The compiler emits exactly four UTF-8, LF-terminated files under an explicit output directory. `--check` compares their exact bytes without creating directories or rewriting stale files. Whitespace drift is reported intentionally. It validates references and source shape, not CSS grammar, host variable support, accessibility of all states, or native runtime behavior.

Inline OKLCH expressions in link-hover, translucent borders and elevation remain preserved source values; they are outside the 27 exact palette conversion checks. Do not infer that all literal expressions are palette-derived or automatically contrast-verified.

The older `BlueSlate.Tokens.json` and `.css` beside this file remain frozen v0.3 consumer interfaces. Current JSON/CSS translations live under `generated/`. See `Migration-0.5.md` before changing an existing adopter's import or parser.
