[CmdletBinding()]
param(
    [string]$TokenCss = (Join-Path $PSScriptRoot "..\generated\BlueSlate.Tokens.css"),
    [string]$TokenJson = (Join-Path $PSScriptRoot "..\generated\BlueSlate.Tokens.json"),
    [string]$OutputPath = (Join-Path $PSScriptRoot "..\spec\mockups\blue-slate-semantic-swatches.png")
)
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$magick = (Get-Command magick -ErrorAction Stop).Source
$tokens = Get-Content -Raw $TokenJson | ConvertFrom-Json
$colors = @($tokens.palette.PSObject.Properties)
if ($colors.Count -lt 20) { throw 'Expected generated palette tokens before rendering the board.' }
$cells = [Collections.Generic.List[string]]::new(); $index = 0
foreach ($match in $colors) {
    $x = 36 + (($index % 3) * 360); $y = 120 + ([math]::Floor($index / 3) * 116); $name = $match.Name; $color = $match.Value.oklch; $hex = $match.Value.hex
    $lightness = [double]([regex]::Match($color, '^oklch\(([0-9.]+)').Groups[1].Value); $label = if ($lightness -gt .65) { '#050913' } else { '#E1E7DB' }
    $cells.Add("<rect x='$x' y='$y' width='324' height='84' rx='12' fill='$hex'/><text x='$($x+16)' y='$($y+32)' fill='$label' font-size='20' font-family='Segoe UI'>$name</text><text x='$($x+16)' y='$($y+60)' fill='$label' font-size='13' font-family='Consolas'>$color</text>")
    $index++
}
$height = 120 + ([math]::Ceiling($colors.Count / 3) * 116) + 36
$svg = "<svg xmlns='http://www.w3.org/2000/svg' width='1152' height='$height' viewBox='0 0 1152 $height'><rect width='100%' height='100%' fill='#050913'/><text x='36' y='52' fill='#E1E7DB' font-size='32' font-family='Segoe UI'>Blue Slate semantic palette</text><text x='36' y='82' fill='#B9C9C5' font-size='16' font-family='Segoe UI'>Dual source values: exact sRGB hex plus OKLCH.</text>$($cells -join '')</svg>"
$temp = Join-Path ([IO.Path]::GetTempPath()) ("blueslate-" + [guid]::NewGuid().ToString('N') + '.svg')
try {
    [IO.File]::WriteAllText($temp, $svg)
    & $magick $temp $OutputPath
    if ($LASTEXITCODE -ne 0 -or !(Test-Path -LiteralPath $OutputPath)) { throw 'Swatch rendering failed.' }
} finally {
    if (Test-Path -LiteralPath $temp) { Remove-Item -LiteralPath $temp }
}
Write-Output "Rendered $OutputPath"
