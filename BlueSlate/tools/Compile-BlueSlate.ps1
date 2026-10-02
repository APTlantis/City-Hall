[CmdletBinding()]
param(
    [string]$TokenSource = (Join-Path $PSScriptRoot '..\spec\tokens\BlueSlate.Tokens.toml'),
    [string]$OutputRoot = (Join-Path $PSScriptRoot '..\generated'),
    [string]$PythonExecutable = $(if ($env:BLUESLATE_PYTHON) { $env:BLUESLATE_PYTHON } else { 'python' }),
    [switch]$Check
)
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$arguments = @((Join-Path $PSScriptRoot 'compile_blueslate.py'), '--source', $TokenSource, '--output', $OutputRoot)
if ($Check) { $arguments += '--check' }
& $PythonExecutable @arguments
if ($LASTEXITCODE -ne 0) { throw "Blue Slate compiler failed with exit code $LASTEXITCODE" }
