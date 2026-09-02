# Blue Slate Bootstrap 5.3 Profile

Target: local-first Bootstrap 5.3 interfaces, including Tauri/Vite desktop shells and evidence-heavy internal tools.

## Installation and Order

Bundle Bootstrap 5.3 locally with the application. Load its CSS first, then load `starter-packs/bootstrap53/aptlantis-blue-slate.bootstrap53.css`. The profile is one dark theme; it does not add a theme switch or a light palette.

```html
<link rel="stylesheet" href="./bootstrap.min.css" />
<link rel="stylesheet" href="./aptlantis-blue-slate.bootstrap53.css" />
```

## Translation Boundary

`spec/tokens/BlueSlate.Tokens.json` remains the framework-neutral source of truth. Bootstrap variables are compatibility variables that translate its roles for Bootstrap 5.3; Bootstrap-specific ramps, RGB channels, subtle backgrounds, text-emphasis values, and internal aliases are profile values rather than new global Blue Slate raw tokens.

| Blue Slate role | Bootstrap family |
| --- | --- |
| canvas, canvas-recessed, panel, overlay | body, secondary, tertiary, modal/popover surfaces |
| content primary/secondary/tertiary and structure borders | body, emphasis, secondary/tertiary text and border variables |
| intent primary/secondary/success/info/warning/danger/light/dark | contextual color, RGB, emphasis, subtle-background, and subtle-border variables |
| interaction focus and action | link, button focus ring, active control treatment |
| validation valid/invalid | Bootstrap form feedback and border variables |
| foundation radii and elevation | border-radius, box-shadow, and focus-ring variables |

The following are intentional Bootstrap compatibility aliases: `--bs-blue`, `--bs-indigo`, `--bs-purple`, `--bs-red`, `--bs-orange`, `--bs-yellow`, `--bs-green`, `--bs-teal`, `--bs-cyan`, the neutral `--bs-gray-*` ramp, all `*-rgb` variables, and contextual emphasis/subtle variables. They exist because Bootstrap components require them; they do not expand the framework-neutral contract.

## Implementation Rules

- Use Bootstrap components and utility layout normally, but choose contextual classes only for their declared semantic intent.
- Use `primary` for the current action, `success` for healthy/completed state, `warning` for risk or preflight attention, `danger` for errors/destructive action, `info` for taxonomy/special state, and `secondary`/`dark` for neutral structure.
- Do not use color as the sole status signal. Include visible labels, icons, or text for badges, alerts, validation, and progress.
- Preserve Bootstrap keyboard behavior. Focus must remain visible on links, buttons, inputs, navigation, and custom controls.
- Keep the bundled Bootstrap version at 5.3.x. Revalidate the profile before upgrading to a new Bootstrap major version.

## Starter Example

`starter-packs/bootstrap53/sample-surface.html` covers the required state matrix. It expects a local `bootstrap.min.css` copy beside the profile CSS; it intentionally does not embed a CDN dependency.

## Profile Validation

At desktop width, inspect card, navigation, table, badge, button default/hover/focus/active/disabled, valid/invalid/disabled form fields, alerts, progress, and code. Check normal text at 4.5:1 minimum and large text/non-text interactive indicators at 3:1 minimum against their actual rendered backgrounds.
