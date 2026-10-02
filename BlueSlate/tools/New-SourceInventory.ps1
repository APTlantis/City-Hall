[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)][string]$SourceRoot,
    [string]$OutputPath = (Join-Path $PSScriptRoot "..\reports\stylesheet-mapping-ledger.toml")
)
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
New-Item -ItemType Directory -Force -Path (Split-Path -Parent $OutputPath) | Out-Null
$lines = [Collections.Generic.List[string]]::new()
$lines.Add('# Generated evidence inventory. It does not alter input stylesheets.')
$lines.Add('[inventory]'); $lines.Add(('source_root = "{0}"' -f (Resolve-Path -LiteralPath $SourceRoot).Path.Replace('\','/'))); $lines.Add("generated_at = `"$([DateTime]::UtcNow.ToString('o'))`"")
foreach ($file in Get-ChildItem -LiteralPath $SourceRoot -Filter '*.css' | Sort-Object Name) {
    $content = Get-Content -Raw -LiteralPath $file.FullName
    $variables = [regex]::Matches($content, '--[A-Za-z0-9_-]+') | ForEach-Object Value | Sort-Object -Unique
    $colors = [regex]::Matches($content, '(?i)(?<![\w])#[0-9a-f]{3,8}(?![\w])|oklch\([^)]*\)') | ForEach-Object Value | Sort-Object -Unique
    $lines.Add(''); $lines.Add(('[source."{0}"]' -f $file.BaseName)); $lines.Add(('path = "{0}"' -f $file.FullName.Replace('\','/'))); $lines.Add("variables = $($variables.Count)"); $lines.Add("color_literals = $($colors.Count)")
    foreach ($variable in $variables) {
        $status = if ($variable -like '--bs-*' -or $variable -like '--b3-*') { 'compatibility-candidate' } elseif ($variable -like '--apt-*' -or $variable -like '--atl-*') { 'local-profile-candidate' } else { 'unresolved' }
        $lines.Add(('[[source."{0}".entry]]' -f $file.BaseName)); $lines.Add('kind = "variable"'); $lines.Add(('value = "{0}"' -f $variable)); $lines.Add(('status = "{0}"' -f $status))
    }
    foreach ($color in $colors) {
        $status = 'unresolved' # A color match alone does not establish a semantic mapping.
        $lines.Add(('[[source."{0}".entry]]' -f $file.BaseName)); $lines.Add('kind = "color-literal"'); $lines.Add(('value = "{0}"' -f $color)); $lines.Add(('status = "{0}"' -f $status))
    }
}
[IO.File]::WriteAllLines($OutputPath, $lines)
Write-Output "Wrote evidence ledger: $OutputPath"
