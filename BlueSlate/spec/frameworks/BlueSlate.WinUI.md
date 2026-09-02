# Blue-Slate WinUI Pack

Target: WinUI 3 / Windows App SDK applications.

WinUI should share the same token values as WPF, but not the same implementation files. WinUI uses theme resources, control styles, visual states, acrylic/mica decisions, and Windows App SDK conventions that should remain native.

## Pack Structure

```text
Aptlantis.UI.WinUI/
  Themes/
    BlueSlate.Colors.xaml
    BlueSlate.Brushes.xaml
    BlueSlate.Typography.xaml
    BlueSlate.Controls.xaml
    BlueSlate.Window.xaml
    BlueSlate.xaml
  Samples/
    BlueSlate.OperationalShell.xaml
  README.md
```

## Resource Rules

- Define `Color` resources from `BlueSlate.Tokens.json`.
- Define semantic brushes for background, panel, border, text, action, focus, warning, taxonomy, archive, success, and verified.
- Preserve WinUI visual states for pointer over, pressed, disabled, selected, focused, and checked.
- Use Material Symbols only where the app has bundled the font; otherwise fall back to WinUI symbol/icon primitives.

## Control Priority

1. `Button` and `AppBarButton`
2. `TextBox` and `NumberBox`
3. `ComboBox`
4. `NavigationView`
5. `TabView`
6. `TreeView`
7. `ListView`
8. `DataGrid` or chosen grid package
9. `InfoBar`
10. Window/title bar shell

## Shell Guidance

Use a compact operational shell rather than a marketing layout:

- Thin top command bar.
- Left navigation or tree when the task has structure.
- Right or bottom evidence/code panel when output matters.
- Status strip for validation, readiness, and connection state.

## Difference From WPF

Do not copy WPF templates into WinUI. Translate tokens and behavior intent only. WinUI control visual states, theme-resource lookup, and title-bar handling must be implemented with WinUI-native patterns.
