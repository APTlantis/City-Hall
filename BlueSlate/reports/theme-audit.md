# BlueSlate theme audit

Source: spec/tokens/BlueSlate.Tokens.toml v0.5.0. Exact-migration audit; no token values were changed.

| Pair | Contrast | Threshold | Result |
| --- | ---: | ---: | --- |
| `semantic.content.primary` on `semantic.surface.canvas` | 15.79:1 | 4.5:1 | pass |
| `semantic.content.secondary` on `semantic.surface.canvas` | 11.59:1 | 4.5:1 | pass |
| `semantic.content.tertiary` on `semantic.surface.canvas-recessed` | 6.87:1 | 4.5:1 | pass |
| `semantic.content.link` on `semantic.surface.canvas` | 14.88:1 | 4.5:1 | pass |
| `semantic.intent.primary` on `semantic.surface.canvas` | 11.63:1 | 3:1 | pass |
| `semantic.intent.success` on `semantic.surface.canvas-recessed` | 9.44:1 | 3:1 | pass |
| `semantic.intent.warning` on `semantic.surface.canvas-recessed` | 7.61:1 | 3:1 | pass |
| `semantic.intent.danger` on `semantic.surface.canvas-recessed` | 6.03:1 | 3:1 | pass |

## Scope

- All 27 palette pairs pass the independent exact sRGB-to-OKLCH conversion check. Inline OKLCH expressions and alpha composites are not covered by that conversion check.
- These eight declared opaque pairs do not establish full component, disabled, alpha-blended, or runtime contrast compliance.
- Framework aliases are generated only under declared Tailwind and SiYuan maps; Bootstrap remains legacy evidence.
