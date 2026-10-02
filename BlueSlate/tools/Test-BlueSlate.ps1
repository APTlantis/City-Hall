[CmdletBinding()]
param([string]$Root = (Join-Path $PSScriptRoot ".."))
Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"
$compiler = Join-Path $Root "tools\Compile-BlueSlate.ps1"
& $compiler -TokenSource (Join-Path $Root 'spec\tokens\BlueSlate.Tokens.toml') -OutputRoot (Join-Path $Root 'generated') -Check
& node (Join-Path $Root 'tools\Test-ColorConversions.js') (Join-Path $Root 'spec\tokens\BlueSlate.Tokens.toml')
if ($LASTEXITCODE -ne 0) { throw 'Color conversion validation failed.' }
$generated = Join-Path $Root "generated"
foreach ($file in 'BlueSlate.Tokens.css','BlueSlate.Tailwind.css','BlueSlate.SiYuan.css','BlueSlate.Tokens.json') {
    if (!(Test-Path -LiteralPath (Join-Path $generated $file))) { throw "Missing generated artifact: $file" }
}
$tokens = Get-Content -Raw (Join-Path $generated 'BlueSlate.Tokens.json') | ConvertFrom-Json
if ($tokens.canonicalSource -ne 'BlueSlate.Tokens.toml' -or $tokens.themeMode -ne 'dark-only') { throw 'Generated JSON is not a TOML-derived dark-only compatibility export.' }
if ((Get-Content -Raw (Join-Path $generated 'BlueSlate.SiYuan.css')) -notmatch '--b3-theme-primary') { throw 'SiYuan adapter is missing its required primary mapping.' }
if ((Get-Content -Raw (Join-Path $generated 'BlueSlate.Tailwind.css')) -notmatch '--color-bs-primary') { throw 'Tailwind translation is missing its required primary mapping.' }
Write-Output 'BlueSlate compiler contract, generated artifacts, and target coverage passed.'
