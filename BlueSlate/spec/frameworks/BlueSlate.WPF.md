# Blue-Slate WPF Pack

Target: WPF desktop applications that need a native ResourceDictionary implementation, not a direct Tailwind port.

## Intended Pack Structure

This is the target architecture, not a claim that every dictionary below is shipped. The actual pilot files and runtime gaps are listed in `Migration-0.5.md`.

```text
Aptlantis.UI.Wpf/
  Themes/
    Aptlantis.BlueSlate.Colors.xaml
    Aptlantis.BlueSlate.Brushes.xaml
    Aptlantis.BlueSlate.Typography.xaml
    Aptlantis.BlueSlate.Effects.xaml
    Aptlantis.BlueSlate.Controls.xaml
    Aptlantis.BlueSlate.Window.xaml
    Aptlantis.BlueSlate.xaml
  Samples/
    BlueSlate.StructraShell.xaml
  README.md
```

`Aptlantis.BlueSlate.xaml` should merge the other dictionaries and be the only file app projects need to import.

## Resource Layers

- Colors: raw `Color` resources matching the canonical `BlueSlate.Tokens.toml` palette.
- Brushes: semantic `SolidColorBrush`, gradient, and drawing-brush resources.
- Typography: font family, size, weight, and line-height resources.
- Effects: glow, inset-light approximations, panel shadows, focus rings.
- Controls: complete templates for core controls.
- Window: `WindowChrome`, title bar, command bar, resize-safe shell, status bar.

## Control Priority

Implement in this order:

1. `Button`
2. `TextBox`
3. `ComboBox`
4. `TabControl`
5. `TreeView`
6. `ListBox`
7. `DataGrid`
8. `GroupBox`
9. `ScrollBar`
10. `Window`

Default WPF controls will not carry this theme by color changes alone. Buttons, tabs, tree items, data grids, and scrollbars need templates.

## Sample Shell

The first sample should mimic a Structra-style utility:

```text
Top command bar
Left structure tree
Middle field inspector
Right output/code preview
Bottom validation/status bar
```

This stress-tests the controls Blue-Slate apps actually need: panes, toolbar buttons, inputs, toggles, tabs, tree rows, code surfaces, scrollbars, and status states.

## Native Translation Notes

- Use `DrawingBrush` for the technical grid background.
- Use nested `Border` elements for card/panel depth.
- Use `DropShadowEffect` sparingly for focused panels and command bars.
- Use `WindowChrome` instead of a pasted-on default title bar.
- Keep accent brushes semantic: action, focus, warning, taxonomy, archive, success, verified.
