[CmdletBinding()]
param([string]$Root = (Join-Path $PSScriptRoot ".."))
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$css = Get-Content -Raw (Join-Path $Root 'starter-packs\bootstrap53\aptlantis-blue-slate.bootstrap53.css')
$profile = Get-Content -Raw (Join-Path $Root 'spec\frameworks\BlueSlate.Bootstrap53.md')
$sample = Get-Content -Raw (Join-Path $Root 'starter-packs\bootstrap53\sample-surface.html')
$properties = [regex]::Matches($css, '--bs-[a-z0-9-]+\s*:') | ForEach-Object Value | Sort-Object -Unique
if ($properties.Count -lt 100) { throw 'The legacy Bootstrap evidence profile unexpectedly has fewer than 100 mapped properties.' }
if ($profile -notmatch 'compatibility aliases') { throw 'The Bootstrap profile does not document its compatibility boundary.' }
$missing = @('card','navbar','table','badge','btn-primary','disabled','is-valid','is-invalid','alert','progress','<code>') | Where-Object { $sample -notmatch [regex]::Escape($_) }
if ($missing) { throw "Legacy Bootstrap state specimen is missing: $($missing -join ', ')" }
Write-Output "Validated $($properties.Count) legacy Bootstrap 5.3 properties and state-specimen markers as non-canonical evidence."
