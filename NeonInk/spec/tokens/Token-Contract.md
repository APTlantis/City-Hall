# Token contract

Schema: `aptlantis.neonink.tokens/1`; suite version: 0.2.0. Python 3.11+ standard library is sufficient.

The TOML source is authoritative. `[palette.*]` carries uppercase six-digit sRGB hex, an OKLCH numeric triple `[L, C, H]`, and a role. Preserved colors come from the JSON palette in the historical core specification. New ordered scale stops are explicitly labeled. The compiler verifies the paired representations within 0.000002 per coordinate and permits only 0.00001 linear-RGB roundoff at the gamut boundary. It fails on mismatches rather than silently retuning a color.

`[semantic]` maps CSS-safe role names directly to palette keys. Alias chains are intentionally unsupported; invalid/missing targets fail. `[scales]` stores palette-key arrays. Sequential scales require strictly increasing lightness. `[contrast].pairs` stores `foreground-role|background-role|minimum` for opaque pairs. Supported minima are 3, 4.5, or 7. Values are checked without rounding before pass/fail.

## Commands

```powershell
python tools/compile_neonink.py
python tools/compile_neonink.py --check
python tools/test_compiler.py
python tools/render_references.py
python tools/render_references.py --check
```

Use an explicit Python executable if it is not on PATH. `--source` and `--output` support isolated builds. Compilation emits CSS with sRGB fallbacks and an OKLCH `@supports` override, resolved-source JSON for tools, an opaque contrast report, and the complete Before/After representation table. `--check` reads and compares exact UTF-8 bytes, writes nothing, and fails for missing or stale outputs.

Six decimal coordinates preserve exact-color migration more closely than presentation-rounded three-decimal values. Hex remains visible for chart/native/export consumers. This is an equivalent representation migration, not a palette redesign. Consult [CSS Color 4](https://www.w3.org/TR/css-color-4/) for OKLCH mechanics. Lightness is not WCAG luminance; use the declared contrast calculations and actual rendering checks.

For a new OKLCH scale, hold hue deliberate, choose a monotonic lightness path, reduce chroma to fit the target gamut when needed, then review adjacent marks and labels. Store the final sRGB fallback with its equivalent OKLCH coordinates. Wide-gamut/P3-only colors, alpha colors, and auto-generated light themes are outside this version's compiler contract.

The audit covers semantic aliases, not every possible pair of preserved legacy palette colors. Alpha overlays and gradients require their actual composited backgrounds. Do not weaken a threshold to conceal a failure; choose a role approved for the intended surface or document a distinct restricted use.
