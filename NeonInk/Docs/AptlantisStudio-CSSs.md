## `aptlantis-studio-theme.json`

```json
{
  "name": "Aptlantis Studio — Neon Ink",
  "version": "0.1.0",
  "philosophy": "Dark archival interface with manga/cyberpunk accents for small-model dataset creation.",
  "colors": {
    "background": {
      "void": "#050816",
      "base": "#0B0F1A",
      "panel": "#111827",
      "panelRaised": "#162033",
      "panelSoft": "#0F172A"
    },
    "text": {
      "primary": "#E5E7EB",
      "secondary": "#CBD5E1",
      "muted": "#94A3B8",
      "faint": "#64748B",
      "inverse": "#050816"
    },
    "accent": {
      "cyan": "#22D3EE",
      "violet": "#A78BFA",
      "magenta": "#F472B6",
      "green": "#84CC16",
      "orange": "#F97316",
      "red": "#F43F5E",
      "yellow": "#FACC15"
    },
    "border": {
      "dim": "#1E293B",
      "normal": "#334155",
      "cyan": "#155E75",
      "violet": "#6D28D9",
      "magenta": "#BE185D"
    },
    "state": {
      "idle": "#334155",
      "active": "#22D3EE",
      "running": "#A78BFA",
      "complete": "#84CC16",
      "warning": "#FACC15",
      "error": "#F43F5E",
      "archived": "#64748B",
      "experimental": "#F472B6"
    },
    "datasetType": {
      "code": "#22D3EE",
      "rpg": "#A78BFA",
      "creative": "#F472B6",
      "language": "#38BDF8",
      "tools": "#84CC16",
      "archive": "#94A3B8",
      "rust": "#F97316",
      "lore": "#A855F7"
    }
  },
  "glow": {
    "idle": "0 0 0 rgba(34, 211, 238, 0)",
    "soft": "0 0 16px rgba(34, 211, 238, 0.28)",
    "active": "0 0 24px rgba(34, 211, 238, 0.45)",
    "violet": "0 0 24px rgba(167, 139, 250, 0.42)",
    "magenta": "0 0 24px rgba(244, 114, 182, 0.42)",
    "danger": "0 0 24px rgba(244, 63, 94, 0.45)"
  },
  "radius": {
    "sm": "0.375rem",
    "md": "0.625rem",
    "lg": "0.875rem",
    "xl": "1.25rem"
  }
}
```

## Tailwind config extension

```js
export default {
  theme: {
    extend: {
      colors: {
        studio: {
          void: "#050816",
          base: "#0B0F1A",
          panel: "#111827",
          raised: "#162033",
          soft: "#0F172A",
          text: "#E5E7EB",
          muted: "#94A3B8",
          faint: "#64748B",
          cyan: "#22D3EE",
          violet: "#A78BFA",
          magenta: "#F472B6",
          green: "#84CC16",
          orange: "#F97316",
          red: "#F43F5E",
          yellow: "#FACC15"
        }
      },
      boxShadow: {
        "glow-idle": "0 0 0 rgba(34, 211, 238, 0)",
        "glow-soft": "0 0 16px rgba(34, 211, 238, 0.28)",
        "glow-active": "0 0 24px rgba(34, 211, 238, 0.45)",
        "glow-violet": "0 0 24px rgba(167, 139, 250, 0.42)",
        "glow-magenta": "0 0 24px rgba(244, 114, 182, 0.42)",
        "panel": "0 8px 30px rgba(0, 0, 0, 0.35)"
      },
      fontFamily: {
        mono: ["JetBrains Mono", "Cascadia Code", "monospace"],
        display: ["Rajdhani", "Orbitron", "system-ui", "sans-serif"]
      }
    }
  }
};
```

## Core component pattern

```html
<section class="bg-studio-panel border border-studio-cyan/30 shadow-panel shadow-glow-soft rounded-xl p-5">
  <div class="flex items-center justify-between border-b border-studio-cyan/20 pb-3 mb-4">
    <h2 class="font-display text-studio-cyan uppercase tracking-wider">Featured Dataset</h2>
    <span class="text-xs text-studio-green border border-studio-green/40 px-2 py-1 rounded">ACTIVE</span>
  </div>

  <h3 class="text-studio-text text-2xl font-bold">Rust Code Corpus</h3>
  <p class="text-studio-muted mt-2">
    High quality Rust source, docs, examples, and crate metadata prepared for small-model fine tuning.
  </p>
</section>
```

## Semantic glow classes

```html
<!-- idle dataset -->
<div class="border border-studio-faint/30 shadow-glow-idle"></div>

<!-- active dataset -->
<div class="border border-studio-cyan/40 shadow-glow-soft"></div>

<!-- running pipeline -->
<div class="border border-studio-violet/50 shadow-glow-violet"></div>

<!-- experimental dataset -->
<div class="border border-studio-magenta/50 shadow-glow-magenta"></div>

<!-- failed pipeline -->
<div class="border border-studio-red/50 shadow-glow-danger"></div>
```

## My suggested identity rule

Use **cyan as structure**, **violet as process**, and **magenta as discovery**.

| Meaning                                 | Color   |
| --------------------------------------- | ------- |
| Navigation / links / structure          | Cyan    |
| Pipelines / generation / transformation | Violet  |
| New / featured / creative               | Magenta |
| Complete / verified                     | Green   |
| Warning / needs review                  | Yellow  |
| Rust / code heat                        | Orange  |
| Error / failed validation               | Red     |

This gives Aptlantis Studio a real visual language instead of just “pretty colors.”
