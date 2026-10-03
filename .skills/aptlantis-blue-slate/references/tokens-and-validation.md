# Tokens, compilation and audit

Use the selected suite's `spec/tokens/Token-Contract.md` and TOML. Canonical layers are palette, semantic, component, foundation and typography. Each palette entry keeps exact hex, OKLCH and its role. Reusable meaning belongs in semantic tokens, recurring controls in component tokens, geometry in foundation, target-specific names in framework adapters and one-off decisions in the adopter's profile.

Run from the selected suite root (Python 3.11+, PowerShell 7, Node.js):

```powershell
python tools/compile_blueslate.py --check
pwsh -NoProfile -ExecutionPolicy Bypass -File tools/Test-BlueSlate.ps1
```

`--check` is read-only and fails if any generated output is missing or differs. For authorized generation, run `python tools/compile_blueslate.py`. Alternate sources and outputs require both `--source <source.toml>` and `--output <target-directory>` so an adopter variant cannot overwrite the standard's generated files accidentally. PowerShell users can call `tools/Compile-BlueSlate.ps1 -TokenSource ... -OutputRoot ...`; set `BLUESLATE_PYTHON` or pass `-PythonExecutable` when Python is outside PATH.

The four outputs are neutral CSS, Tailwind v4 input, a partial SiYuan CSS adapter and TOML-shaped JSON. Every generated file identifies its source/version. Hex values remain available but semantic CSS uses OKLCH; unsupported renderers need an explicit hex adapter. Do not hand-edit generated files or treat the current JSON as the old v0.3 schema.

For audit, also run `tools/Audit-BlueSlate.ps1 -Root <suite-root> -ReportPath <report-path>`. This writes the requested report. Eight declared opaque color pairs are checked at 4.5:1 normal text and 3:1 indicators. Native command failures propagate. The exact conversion test covers the palette; inline OKLCH expressions, translucent borders and elevation require separate evaluation. Read findings before claiming conformance.

For supplied stylesheets, `tools/New-SourceInventory.ps1 -SourceRoot <directory> -OutputPath <ledger.toml>` scans the directory's CSS files without changing them. Prefixes only suggest compatibility/local-profile candidates. An unresolved color or an exact palette match does not establish semantic correctness. Record a role mapping and disposition before treating coverage as complete.

After compiler changes, run `python tools/test_compiler.py`, `python tools/validate_suite.py` and the suite checks. For a new framework, enumerate its needed variables/resource keys and map them to canonical roles before implementing the adapter. Preserve selected colors during audits and exact conversions; if retuning is necessary, explain the failing usage and implement only the authorized design adjustment with regenerated outputs and appropriate rendered checks.
