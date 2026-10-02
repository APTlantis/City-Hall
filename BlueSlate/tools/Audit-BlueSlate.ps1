[CmdletBinding()]
param(
    [string]$Root = (Join-Path $PSScriptRoot ".."),
    [string]$ReportPath = (Join-Path $PSScriptRoot "..\reports\theme-audit.md")
)
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
& (Join-Path $Root 'tools\Test-BlueSlate.ps1') -Root $Root
$json = Get-Content -Raw (Join-Path $Root 'generated\BlueSlate.Tokens.json') | ConvertFrom-Json
function Get-PathValue($node, [string]$path) { foreach($part in $path.Split('.')) { $node = $node.$part; if ($null -eq $node) { throw "Unresolved token: $path" } }; $node }
function Resolve-Hex([string]$path) { $value = Get-PathValue $json $path; while ($value -is [string] -and $value -match '^\{([^}]+)\}$') { $value = Get-PathValue $json $Matches[1] }; if ($value.hex) { return $value.hex }; throw "Token is not a palette color: $path" }
function Get-Contrast([string]$a,[string]$b) { function Get-Lum($hex) { $channels = @((0, 2, 4) | ForEach-Object { [Convert]::ToInt32($hex.Substring($_ + 1,2),16) / 255 }); $linear = @($channels | ForEach-Object { if ($_ -le .04045) { $_ / 12.92 } else { [Math]::Pow((($_ + .055) / 1.055), 2.4) } }); return .2126*$linear[0]+.7152*$linear[1]+.0722*$linear[2] }; $l = @((Get-Lum $a), (Get-Lum $b)) | Sort-Object -Descending; return ($l[0]+.05)/($l[1]+.05) }
$source = Get-Content -Raw (Join-Path $Root 'spec\tokens\BlueSlate.Tokens.toml')
$rows = [Collections.Generic.List[string]]::new(); $rows.Add('# BlueSlate theme audit'); $rows.Add(''); $rows.Add("Source: `spec/tokens/BlueSlate.Tokens.toml` v$($json.version). Exact-migration audit; no token values were changed."); $rows.Add(''); $rows.Add('| Pair | Contrast | Threshold | Result |'); $rows.Add('| --- | ---: | ---: | --- |')
$failed = @()
foreach ($group in @(@{ Name='normal-text'; Threshold=4.5 }, @{ Name='indicators'; Threshold=3.0 })) {
    $match = [regex]::Match($source, "(?s)$($group.Name)\s*=\s*\[(.*?)\]")
    if (!$match.Success) { throw "Audit pair group missing: $($group.Name)" }
    foreach ($pair in [regex]::Matches($match.Groups[1].Value, '"([^"]+)"')) {
        $parts = $pair.Groups[1].Value.Split('|'); $ratio = Get-Contrast (Resolve-Hex $parts[0]) (Resolve-Hex $parts[1]); $pass = $ratio -ge $group.Threshold; $result = if ($pass) { 'pass' } else { 'review' }; $rows.Add("| ``$($parts[0])`` on ``$($parts[1])`` | $([Math]::Round($ratio,2)):1 | $($group.Threshold):1 | $result |"); if (!$pass) { $failed += $pair.Groups[1].Value }
    }
}
$rows.Add(''); $rows.Add('## Scope'); $rows.Add(''); $rows.Add('- All 27 palette pairs pass the independent exact sRGB-to-OKLCH conversion check. Inline OKLCH expressions and alpha composites are not covered by that conversion check.')
$rows.Add('- These eight declared opaque pairs do not establish full component, disabled, alpha-blended, or runtime contrast compliance.')
$rows.Add('- Framework aliases are generated only under declared Tailwind and SiYuan maps; Bootstrap remains legacy evidence.')
New-Item -ItemType Directory -Force -Path (Split-Path -Parent $ReportPath) | Out-Null; [IO.File]::WriteAllLines($ReportPath,$rows)
if ($failed.Count) { throw "Contrast review required: $($failed -join ', ')" }; Write-Output "Audit passed: $ReportPath"
