# Blue-Slate Tauri React Starter Notes

Use this folder as the seed profile for Tauri + Vite + React apps.

## Required app imports

```css
@import "../../aptlantis-blue-slate.tailwind.css";
```

For app-local copies, place the theme under `src/styles/blue-slate.css` and import it from `src/main.css`.

## Suggested component folders

```text
src/
  components/
    blue-slate/
      AppShell.tsx
      StatusChip.tsx
      EvidenceGrid.tsx
      CommandBuilder.tsx
      CodePanel.tsx
      Tabs.tsx
  styles/
    blue-slate.css
public/
  assets/
    blue-slate/
      fonts/
      icons/
      boards/
```

## Component contract

- `StatusChip` supports `active`, `warning`, `taxonomy`, `archive`, `verified`, and `neutral`.
- `EvidenceGrid` renders compact file/proof cards.
- `CommandBuilder` uses `atl-form-field`, `atl-input`, `atl-checkbox-row`, and `atl-command-output`.
- `CodePanel` uses `atl-code` and Prism/Okaidia token mappings.
- `Tabs` uses `atl-tabs`, `atl-tab`, and `atl-tab-active`.
