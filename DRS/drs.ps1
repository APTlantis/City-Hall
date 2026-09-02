#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Desktop Application Release Standard - CLI helper

.DESCRIPTION
    drs validates, verifies, and scaffolds DRS-compliant desktop application releases.

.PARAMETER Command
    new            Scaffold a new DRS-compliant project
    validate       Check that all required manifest fields are present
    verify-manifest  Check manifest field consistency without reading artifact files
    check-release  Full release readiness check (manifest + artifact + docs)
    hash           Compute SHA-256 for a release artifact; add --blake3 to also compute BLAKE3 when available
    init-docs      Copy all doc templates to docs/ with the project name applied
    help           Show this help

.EXAMPLE
    .\drs.ps1 new MyApp
    .\drs.ps1 check-release
    .\drs.ps1 hash artifacts\installer\MyApp-1.0.0.0-win-x64.msi
    .\drs.ps1 hash artifacts\installer\MyApp-1.0.0.0-win-x64.msi --blake3
    .\drs.ps1 verify-manifest
#>

param(
    [Parameter(Position = 0)]
    [string]$Command = 'help',

    [Parameter(Position = 1)]
    [string]$Arg1 = '',

    [Parameter(Position = 2)]
    [string]$Arg2 = ''
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$script:DrsExitCode = 0

# -----------------------------------------------------------------------------
# OUTPUT HELPERS
# -----------------------------------------------------------------------------

$script:CheckResults = [System.Collections.Generic.List[hashtable]]::new()

function Write-DrsHeader([string]$Title) {
    Write-Host ''
    Write-Host "  drs $Title" -ForegroundColor Cyan
    Write-Host "  $('-' * 58)" -ForegroundColor DarkGray
}

function Write-DrsSection([string]$Name) {
    Write-Host ''
    Write-Host "  $Name" -ForegroundColor DarkGray
}

function Write-Pass([string]$Label, [string]$Detail = '') {
    Write-Host "    [PASS] $Label" -ForegroundColor Green
    if ($Detail) { Write-Host "           $Detail" -ForegroundColor DarkGray }
    $script:CheckResults.Add(@{ Status = 'PASS'; Label = $Label })
}

function Write-Fail([string]$Label, [string]$Detail = '') {
    Write-Host "    [FAIL] $Label" -ForegroundColor Red
    if ($Detail) { Write-Host "           $Detail" -ForegroundColor DarkGray }
    $script:CheckResults.Add(@{ Status = 'FAIL'; Label = $Label })
}

function Write-Warn([string]$Label, [string]$Detail = '') {
    Write-Host "    [WARN] $Label" -ForegroundColor Yellow
    if ($Detail) { Write-Host "           $Detail" -ForegroundColor DarkGray }
    $script:CheckResults.Add(@{ Status = 'WARN'; Label = $Label })
}

function Write-Skip([string]$Label, [string]$Detail = '') {
    Write-Host "    [SKIP] $Label" -ForegroundColor DarkGray
    if ($Detail) { Write-Host "           $Detail" -ForegroundColor DarkGray }
}

function Set-DrsExitCode([int]$Code) {
    if ($Code -gt $script:DrsExitCode) {
        $script:DrsExitCode = $Code
    }
}

function Write-DrsFooter {
    $passed = @($script:CheckResults | Where-Object { $_.Status -eq 'PASS' }).Count
    $failed = @($script:CheckResults | Where-Object { $_.Status -eq 'FAIL' }).Count
    $warned = @($script:CheckResults | Where-Object { $_.Status -eq 'WARN' }).Count

    Write-Host ''
    Write-Host "  $('-' * 58)" -ForegroundColor DarkGray

    if ($failed -gt 0) {
        Write-Host "  RESULT: $passed passed | $failed failed | $warned warnings" -ForegroundColor Red
        Write-Host "          Release is BLOCKED" -ForegroundColor Red
        Set-DrsExitCode 1
    } elseif ($warned -gt 0) {
        Write-Host "  RESULT: $passed passed | $failed failed | $warned warnings" -ForegroundColor Yellow
        Write-Host "          Release is READY (with warnings)" -ForegroundColor Yellow
    } else {
        Write-Host "  RESULT: $passed passed | $failed failed | $warned warnings" -ForegroundColor Green
        Write-Host "          Release is READY" -ForegroundColor Green
    }

    Write-Host "  $('-' * 58)" -ForegroundColor DarkGray
    Write-Host ''

    return $failed -eq 0
}

# -----------------------------------------------------------------------------
# TOML READER  (flat section-based - sufficient for DRS manifests)
# Keys are stored as "section.key" or "section.sub.key" strings.
# -----------------------------------------------------------------------------

function Read-ManifestToml([string]$Path) {
    $data    = @{}
    $section = ''

    foreach ($raw in Get-Content $Path) {
        $line = $raw.Trim()

        if ($line -eq '' -or $line.StartsWith('#')) { continue }

        # Section header: [section] or [section.subsection]
        if ($line -match '^\[([a-zA-Z0-9_.]+)\]$') {
            $section = $matches[1]
            continue
        }

        # Key = "string value"
        if ($line -match '^([a-zA-Z0-9_]+)\s*=\s*"([^"]*)"') {
            $k = if ($section) { "$section.$($matches[1])" } else { $matches[1] }
            $data[$k] = $matches[2]
            continue
        }

        # Key = integer
        if ($line -match '^([a-zA-Z0-9_]+)\s*=\s*(-?\d+)$') {
            $k = if ($section) { "$section.$($matches[1])" } else { $matches[1] }
            $data[$k] = [int]$matches[2]
            continue
        }

        # Key = true | false
        if ($line -match '^([a-zA-Z0-9_]+)\s*=\s*(true|false)$') {
            $k = if ($section) { "$section.$($matches[1])" } else { $matches[1] }
            $data[$k] = ($matches[2] -eq 'true')
            continue
        }

        # Key = [...] - skip arrays (not needed for release checks)
    }

    return $data
}

# -----------------------------------------------------------------------------
# MANIFEST FINDER
# -----------------------------------------------------------------------------

function Find-Manifest {
    $manifests = @(Get-ChildItem -Filter '*.manifest.toml' -ErrorAction SilentlyContinue |
                   Where-Object { $_.Name -notlike '*.schema.toml' })

    if ($manifests.Count -eq 0) {
        Write-Host ''
        Write-Host "  No *.manifest.toml found in current directory." -ForegroundColor Red
        Write-Host "  Run 'drs new <AppName>' to scaffold a new project." -ForegroundColor DarkGray
        Write-Host ''
        Set-DrsExitCode 2
        return $null
    }

    if ($manifests.Count -gt 1) {
        Write-Host ''
        Write-Host "  Multiple manifest files found. Specify one:" -ForegroundColor Yellow
        $manifests | ForEach-Object { Write-Host "    $($_.Name)" -ForegroundColor DarkGray }
        Write-Host ''
        Set-DrsExitCode 2
        return $null
    }

    return $manifests[0].FullName
}

function Get-TemplatesDir {
    $candidate = Join-Path $PSScriptRoot 'templates'
    if (Test-Path $candidate) { return $candidate }

    Write-Host "  Templates directory not found at: $candidate" -ForegroundColor Red
    Write-Host "  Run drs.ps1 from the DRS standard directory (alongside templates/)." -ForegroundColor DarkGray
    Set-DrsExitCode 2
    return $null
}

function Get-Blake3Tool {
    $candidate = Get-Command b3sum -ErrorAction SilentlyContinue
    if ($candidate) { return $candidate.Source }
    $candidate = Get-Command blake3 -ErrorAction SilentlyContinue
    if ($candidate) { return $candidate.Source }
    return $null
}

function Get-Blake3Hash([string]$FilePath) {
    $tool = Get-Blake3Tool
    if (-not $tool) { return $null }
    $output = & $tool $FilePath
    if (-not $output) { return $null }
    return (($output | Select-Object -First 1) -split '\s+')[0].ToUpperInvariant()
}

# -----------------------------------------------------------------------------
# COMMAND: hash
# -----------------------------------------------------------------------------

function Invoke-DrsHash([string]$FilePath, [string]$Mode = '') {
    if (-not $FilePath) {
        Write-Host ''
        Write-Host "  Usage: drs hash <path-to-artifact>" -ForegroundColor Yellow
        Write-Host ''
        Set-DrsExitCode 2
        return
    }

    if (-not (Test-Path $FilePath)) {
        Write-Host ''
        Write-Host "  File not found: $FilePath" -ForegroundColor Red
        Write-Host ''
        Set-DrsExitCode 1
        return
    }

    $item   = Get-Item $FilePath
    $sha256 = (Get-FileHash $FilePath -Algorithm SHA256).Hash
    $size   = $item.Length
    $includeBlake3 = $Mode -eq '--blake3'
    $blake3 = if ($includeBlake3) { Get-Blake3Hash $FilePath } else { $null }

    Write-Host ''
    Write-Host "  File:    $($item.Name)" -ForegroundColor Cyan
    Write-Host "  Size:    $size bytes"
    Write-Host "  SHA-256: $sha256" -ForegroundColor Green
    if ($includeBlake3) {
        if ($blake3) {
            Write-Host "  BLAKE3:  $blake3" -ForegroundColor Green
        } else {
            Write-Host "  BLAKE3:  not computed - install b3sum or blake3 and rerun with --blake3" -ForegroundColor Yellow
        }
    }
    Write-Host ''
    Write-Host "  Manifest snippet:" -ForegroundColor DarkGray
    Write-Host "    size_bytes = $size"
    Write-Host "    sha256     = `"$sha256`""
    if ($includeBlake3 -and $blake3) {
        Write-Host "    blake3     = `"$blake3`""
    }
    Write-Host ''
}

# -----------------------------------------------------------------------------
# COMMAND: validate
# -----------------------------------------------------------------------------

function Invoke-DrsValidate {
    $manifestPath = Find-Manifest
    if (-not $manifestPath) { return }

    Write-DrsHeader 'validate'
    Write-Host "  Manifest: $(Split-Path $manifestPath -Leaf)" -ForegroundColor DarkGray

    $m = Read-ManifestToml $manifestPath

    $required = @(
        'project.id',
        'project.title',
        'project.type',
        'project.stage',
        'project.version',
        'metadata.created',
        'metadata.language_primary',
        'runtime.platform',
        'release.version',
        'release.name',
        'release.date',
        'release.installer.path',
        'release.installer.runtime',
        'release.installer.package_version',
        'release.installer.sha256',
        'release.installer.signing',
        'release.verified.date',
        'release.verified.tests',
        'release.verified.installer_build',
        'documentation.release_notes'
    )

    $missing = 0
    Write-Host ''

    foreach ($field in $required) {
        $val = $m[$field]
        if ($null -eq $val -or "$val".Trim() -eq '') {
            Write-Host "    [MISS] $field" -ForegroundColor Red
            $missing++
        } else {
            $display = if ("$val".Length -gt 60) { "$val".Substring(0, 57) + '...' } else { $val }
            Write-Host "    [OK]   $field" -ForegroundColor Green
            Write-Host "           $display" -ForegroundColor DarkGray
        }
    }

    Write-Host ''
    if ($missing -eq 0) {
        Write-Host "  All required fields are present." -ForegroundColor Green
    } else {
        Write-Host "  $missing required field(s) missing or empty." -ForegroundColor Red
        Set-DrsExitCode 1
    }
    Write-Host ''
}

# -----------------------------------------------------------------------------
# COMMAND: verify-manifest
# -----------------------------------------------------------------------------

function Invoke-DrsVerifyManifest {
    $manifestPath = Find-Manifest
    if (-not $manifestPath) { return }

    $script:CheckResults = [System.Collections.Generic.List[hashtable]]::new()
    $m = Read-ManifestToml $manifestPath

    Write-DrsHeader 'verify-manifest'
    Write-Host "  Manifest: $(Split-Path $manifestPath -Leaf)" -ForegroundColor DarkGray

    # Version consistency
    Write-DrsSection 'VERSION'

    $pv  = $m['project.version']
    $rv  = $m['release.version']
    $pv4 = $m['release.installer.package_version']

    if ($pv -and $rv -and $pv -eq $rv) {
        Write-Pass 'project.version matches release.version' "$pv"
    } else {
        Write-Fail 'Version mismatch' "project.version=[$pv]  release.version=[$rv]"
    }

    if ($pv -and $pv4) {
        if ($pv4 -eq "$pv.0") {
            Write-Pass 'package_version is correct four-part form' "$pv -> $pv4"
        } else {
            Write-Warn 'package_version may be wrong' "Expected $pv.0  Got $pv4"
        }
    }

    # Release status
    $status = $m['release.status']
    if ($status) {
        switch ($status) {
            'published'  { Write-Pass  "Release status: published" }
            'local-verified' { Write-Pass  "Release status: local-verified (not publicly published)" }
            'candidate'  { Write-Warn  "Release status: candidate (not yet published)" }
            'draft'      { Write-Fail  "Release status: draft - not ready for release" }
            'superseded' { Write-Warn  "Release status: superseded - not the current release" }
            'withdrawn'  { Write-Fail  "Release status: withdrawn - this release has been retracted" }
            default      { Write-Warn  "Release status: '$status' (unrecognized)" }
        }
    } else {
        Write-Warn 'release.status not set' "Add: status = 'local-verified' or 'published'"
    }

    # Required fields check
    Write-DrsSection 'REQUIRED FIELDS'

    $checks = [ordered]@{
        'release.name'                     = 'Release name'
        'release.date'                     = 'Release date'
        'release.installer.sha256'         = 'SHA-256 hash'
        'release.installer.signing'        = 'Signing status'
        'release.verified.date'            = 'Verification date'
        'release.verified.tests'           = 'Test result'
        'release.verified.installer_build' = 'Installer build result'
        'documentation.release_notes'      = 'Release notes path'
    }

    foreach ($field in $checks.Keys) {
        $val = $m[$field]
        if ($val -and "$val".Trim() -ne '') {
            Write-Pass "$($checks[$field])" "$val"
        } else {
            Write-Fail "$($checks[$field]) is empty" "manifest field: $field"
        }
    }

    # SHA-256 format
    Write-DrsSection 'HASH FORMAT'

    $hash = $m['release.installer.sha256']
    if ($hash) {
        if ($hash -match '^[A-F0-9]{64}$') {
            Write-Pass 'SHA-256 format: 64-char uppercase hex' "$($hash.Substring(0,8))...$($hash.Substring(56))"
        } elseif ($hash -match '^[a-f0-9]{64}$') {
            Write-Fail 'SHA-256 must be uppercase' 'Convert to uppercase: $hash.ToUpper()'
        } else {
            Write-Fail 'SHA-256 format invalid' "Length: $($hash.Length) chars (expected 64). Valid chars: A-F, 0-9"
        }
    }

    Write-DrsFooter | Out-Null
}

# -----------------------------------------------------------------------------
# COMMAND: check-release
# -----------------------------------------------------------------------------

function Invoke-DrsCheckRelease {
    $manifestPath = Find-Manifest
    if (-not $manifestPath) { return }

    $script:CheckResults = [System.Collections.Generic.List[hashtable]]::new()
    $m = Read-ManifestToml $manifestPath

    $projectVersion = $m['project.version']
    $releaseVersion = $m['release.version']
    $releaseName    = $m['release.name']
    $releaseStatus  = $m['release.status']
    $installerPath  = $m['release.installer.path']
    $sha256         = $m['release.installer.sha256']
    $blake3         = $m['release.installer.blake3']
    $signing        = $m['release.installer.signing']
    $pkgVersion     = $m['release.installer.package_version']
    $relNotes       = $m['documentation.release_notes']
    $checklist      = $m['documentation.release_checklist']
    $trustModel     = $m['documentation.trust_model']

    Write-DrsHeader 'check-release'
    Write-Host "  Manifest: $(Split-Path $manifestPath -Leaf)" -ForegroundColor DarkGray
    Write-Host "  Project:  $releaseName" -ForegroundColor DarkGray
    Write-Host "  Date:     $($m['release.date'])" -ForegroundColor DarkGray

    # -- VERSION --------------------------------------------------------------
    Write-DrsSection 'VERSION'

    if ($projectVersion -and $releaseVersion -and $projectVersion -eq $releaseVersion) {
        Write-Pass 'project.version matches release.version' "$projectVersion == $releaseVersion"
    } else {
        Write-Fail 'Version mismatch' "project.version=[$projectVersion]  release.version=[$releaseVersion]"
    }

    if ($releaseStatus) {
        switch ($releaseStatus) {
            'published'  { Write-Pass  "Release status: published" }
            'local-verified' { Write-Pass  "Release status: local-verified (not publicly published)" }
            'candidate'  { Write-Warn  "Release status: candidate - publish when all checks pass" }
            'draft'      { Write-Fail  "Release status: draft - manifest must be finalised before release" }
            'superseded' { Write-Warn  "Release status: superseded - this is not the current release" }
            'withdrawn'  { Write-Fail  "Release status: withdrawn - this release has been retracted" }
            default      { Write-Warn  "Release status: '$releaseStatus' (unrecognized value)" }
        }
    } else {
        Write-Warn 'release.status not set' "Add: status = 'local-verified' or 'published'"
    }

    # -- ARTIFACT -------------------------------------------------------------
    Write-DrsSection 'ARTIFACT'

    $installerExists = $false

    if ($installerPath) {
        if (Test-Path $installerPath) {
            $item = Get-Item $installerPath
            Write-Pass 'Installer file exists' "$installerPath ($($item.Length) bytes)"
            $installerExists = $true
        } else {
            Write-Fail 'Installer file not found' $installerPath
        }
    } else {
        Write-Fail 'release.installer.path is empty'
    }

    # Filename convention
    if ($installerPath -and $pkgVersion) {
        $filename = Split-Path $installerPath -Leaf
        $appTitle = ($m['project.title'] -replace '\s+', '')
        $pattern  = "^$([regex]::Escape($appTitle))-$([regex]::Escape($pkgVersion))-win-(x64|arm64|x86)\.(msi|msix|exe)$"
        if ($filename -match $pattern) {
            Write-Pass 'Filename follows naming convention' $filename
        } else {
            Write-Warn 'Filename may not follow convention' "Expected: $appTitle-$pkgVersion-win-x64.[msi|msix|exe]  Got: $filename"
        }
    }

    # Hash verification
    if ($installerExists -and $sha256) {
        $actualHash = (Get-FileHash $installerPath -Algorithm SHA256).Hash
        if ($actualHash -eq $sha256.ToUpper()) {
            Write-Pass 'SHA-256 hash matches artifact' "$($sha256.Substring(0,8))...$($sha256.Substring(56))"
        } else {
            Write-Fail 'SHA-256 hash mismatch - do not release' "Manifest: $sha256`n           Actual:   $actualHash"
        }
    } elseif (-not $sha256) {
        Write-Fail 'release.installer.sha256 is empty - hash is required'
    } elseif (-not $installerExists) {
        Write-Skip 'SHA-256 verification skipped (installer not found)'
    }

    if ($installerExists -and $blake3) {
        $actualBlake3 = Get-Blake3Hash $installerPath
        if ($actualBlake3) {
            if ($actualBlake3 -eq $blake3.ToUpper()) {
                Write-Pass 'BLAKE3 hash matches artifact' "$($blake3.Substring(0,8))...$($blake3.Substring($blake3.Length - 8))"
            } else {
                Write-Fail 'BLAKE3 hash mismatch - do not release' "Manifest: $blake3`n           Actual:   $actualBlake3"
            }
        } else {
            Write-Warn 'BLAKE3 verification skipped' 'Install b3sum or blake3 to verify release.installer.blake3'
        }
    } elseif ($installerExists) {
        Write-Skip 'BLAKE3 verification skipped' 'No release.installer.blake3 value recorded'
    }

    # -- SIGNING ---------------------------------------------------------------
    Write-DrsSection 'SIGNING'

    if (-not $signing -or $signing.Trim() -eq '') {
        Write-Fail 'Signing status not recorded' "Set release.installer.signing - never leave this empty"
    } elseif ($signing -eq 'unsigned') {
        Write-Warn 'Installer is unsigned' 'State this explicitly in the release note'
    } elseif ($signing -match '^self-signed') {
        Write-Warn 'Installer is self-signed (not code-signed)' $signing
    } elseif ($signing -match '^code-signed') {
        Write-Pass 'Installer is code-signed' $signing
    } else {
        Write-Pass 'Signing status recorded' $signing
    }

    # -- DOCUMENTATION ---------------------------------------------------------
    Write-DrsSection 'DOCUMENTATION'

    # Release note
    $noteExists = $false
    if ($relNotes) {
        if (Test-Path $relNotes) {
            Write-Pass 'Release note exists' $relNotes
            $noteExists = $true
        } else {
            Write-Fail 'Release note not found' $relNotes
        }
    } else {
        Write-Fail 'documentation.release_notes is empty'
    }

    if ($noteExists) {
        $note = Get-Content $relNotes -Raw -ErrorAction SilentlyContinue

        if ($releaseVersion -and $note -match [regex]::Escape($releaseVersion)) {
            Write-Pass "Version string present in release note" "v$releaseVersion"
        } else {
            Write-Fail 'Version string not found in release note' "Expected: $releaseVersion"
        }

        if ($sha256 -and $sha256.Length -ge 16 -and $note -match [regex]::Escape($sha256.Substring(0, 16))) {
            Write-Pass 'SHA-256 hash present in release note'
        } elseif ($sha256) {
            Write-Fail 'SHA-256 hash not found in release note' 'Add full hash under Release Artifact'
        }

        if ($note -match '## Design Boundaries') {
            Write-Pass 'Design Boundaries section present'
        } else {
            Write-Fail 'Design Boundaries section missing from release note'
        }

        # Production claim check
        if ($note -match 'production[- ]ready|ready for production') {
            if ($trustModel -and (Test-Path $trustModel)) {
                Write-Warn 'Release note contains production readiness claim - ensure security review is on record'
            } else {
                Write-Fail 'Release note claims production readiness but no trust model / security review found'
            }
        }
    }

    # Checklist
    if ($checklist) {
        if (Test-Path $checklist) {
            Write-Pass 'Release checklist exists' $checklist
            $cl = Get-Content $checklist -Raw -ErrorAction SilentlyContinue
            $vBlock = "## v$releaseVersion"
            if ($cl -match [regex]::Escape($vBlock)) {
                Write-Pass "Per-version verification block present" $vBlock
            } else {
                Write-Warn "Per-version block not found in checklist" "Expected: $vBlock"
            }
        } else {
            Write-Fail 'Release checklist not found' $checklist
        }
    } else {
        Write-Warn 'documentation.release_checklist is empty' 'Set path in manifest'
    }

    # -- DOCS IN PUBLISH OUTPUT ------------------------------------------------
    Write-DrsSection 'PUBLISH OUTPUT'

    $publishDocs = 'artifacts\publish\win-x64\docs'
    if (Test-Path $publishDocs) {
        Write-Pass 'docs/ present in publish output' $publishDocs
        # Check current release note is there
        if ($relNotes) {
            $noteName    = Split-Path $relNotes -Leaf
            $publishNote = Join-Path $publishDocs $noteName
            if (Test-Path $publishNote) {
                Write-Pass 'Current release note present in publish docs'
            } else {
                Write-Warn 'Current release note not found in publish docs' "Expected: $publishNote"
            }
        }
    } else {
        Write-Warn 'docs/ not found in publish output' "Expected: $publishDocs - ensure build script copies docs/"
    }

    Write-DrsFooter | Out-Null
}

# -----------------------------------------------------------------------------
# COMMAND: new
# -----------------------------------------------------------------------------

function Invoke-DrsNew([string]$AppName) {
    if (-not $AppName) {
        Write-Host ''
        Write-Host "  Usage: drs new <AppName>" -ForegroundColor Yellow
        Write-Host ''
        Set-DrsExitCode 2
        return
    }

    $templatesDir = Get-TemplatesDir
    if (-not $templatesDir) { return }

    $projectDir = Join-Path (Get-Location) $AppName
    if (Test-Path $projectDir) {
        Write-Host ''
        Write-Host "  Directory already exists: $projectDir" -ForegroundColor Red
        Write-Host ''
        Set-DrsExitCode 1
        return
    }

    Write-Host ''
    Write-Host "  Scaffolding $AppName..." -ForegroundColor Cyan
    Write-Host ''

    New-Item -ItemType Directory -Path $projectDir | Out-Null
    New-Item -ItemType Directory -Path (Join-Path $projectDir 'docs') | Out-Null
    New-Item -ItemType Directory -Path (Join-Path $projectDir 'artifacts' 'installer') -Force | Out-Null

    # Manifest
    $manifestSrc  = Join-Path $templatesDir 'ProjectName.manifest.toml'
    $manifestDest = Join-Path $projectDir "$AppName.manifest.toml"
    if (Test-Path $manifestSrc) {
        $appLower = $AppName.ToLower()
        (Get-Content $manifestSrc) `
            -replace '"appname"',      "`"$appLower`"" `
            -replace '"App Name"',     "`"$AppName`"" `
            -replace '"AppName v',     "`"$AppName v" `
            -replace '"AppName',       "`"$AppName" `
            -replace 'AppName-',       "$AppName-" `
            -replace 'AppName\.manifest', "$AppName.manifest" |
          Set-Content $manifestDest
        Write-Host "    Created: $AppName.manifest.toml" -ForegroundColor Green
    }

    # Checklist
    $clSrc  = Join-Path $templatesDir 'Release-Checklist.md'
    $clDest = Join-Path $projectDir 'docs' "$AppName - Release Checklist.md"
    if (Test-Path $clSrc) {
        (Get-Content $clSrc) -replace '\[AppName\]', $AppName | Set-Content $clDest
        Write-Host "    Created: docs/$AppName - Release Checklist.md" -ForegroundColor Green
    }

    Write-Host ''
    Write-Host "  Next steps:" -ForegroundColor Cyan
    Write-Host "    1. cd $AppName"
    Write-Host "    2. Fill in $AppName.manifest.toml (project.id, description, metadata)"
    Write-Host "    3. Write your first release note BEFORE coding begins:"
    Write-Host "       Copy templates/Release-Note.md -> docs/$AppName v0.1.0.md"
    Write-Host "    4. Run 'drs validate' to verify the manifest"
    Write-Host ''
}

# -----------------------------------------------------------------------------
# COMMAND: init-docs
# -----------------------------------------------------------------------------

function Invoke-DrsInitDocs {
    $manifestPath = Find-Manifest
    if (-not $manifestPath) { return }

    $templatesDir = Get-TemplatesDir
    if (-not $templatesDir) { return }

    $m       = Read-ManifestToml $manifestPath
    $appName = $m['project.title'] -replace '\s+', ''
    if (-not $appName) { $appName = 'AppName' }

    $docsDir = 'docs'
    if (-not (Test-Path $docsDir)) {
        New-Item -ItemType Directory -Path $docsDir | Out-Null
        Write-Host "  Created docs/" -ForegroundColor Green
    }

    Write-Host ''
    Write-Host "  Copying templates to docs/ for $appName..." -ForegroundColor Cyan
    Write-Host ''

    $templates = [ordered]@{
        'Release-Note.md'                = "$appName v0.1.0.md"
        'Trust-Security-Model.md'        = "$appName - Trust and Security Model.md"
        'Dependency-Provenance.md'       = "$appName - Dependency Provenance.md"
        'Build-Reproducibility-Guide.md' = "$appName - Build Reproducibility Guide.md"
        'Threat-Model.md'                = "$appName - Threat Model.md"
        'Integrity-Validation-Matrix.md' = "$appName - Integrity Validation Matrix.md"
        'Data-Migration-Contract.md'     = "$appName - Data Migration Contract.md"
    }

    foreach ($src in $templates.Keys) {
        $srcPath  = Join-Path $templatesDir $src
        $destName = $templates[$src]
        $destPath = Join-Path $docsDir $destName
        if (Test-Path $srcPath) {
            if (Test-Path $destPath) {
                Write-Host "    [SKIP] $destName (already exists)" -ForegroundColor DarkGray
            } else {
                (Get-Content $srcPath) -replace '\[AppName\]', $appName | Set-Content $destPath
                Write-Host "    [COPY] $destName" -ForegroundColor Green
            }
        } else {
            Write-Host "    [MISS] $src not found in templates/" -ForegroundColor Yellow
        }
    }

    Write-Host ''
    Write-Host "  Update documentation.* paths in the manifest to point to the new files." -ForegroundColor DarkGray
    Write-Host ''
}

# -----------------------------------------------------------------------------
# HELP
# -----------------------------------------------------------------------------

function Show-Help {
    Write-Host ''
    Write-Host '  drs - Desktop Application Release Standard CLI' -ForegroundColor Cyan
    Write-Host ''
    Write-Host '  Commands:' -ForegroundColor DarkGray
    Write-Host '    new <AppName>      Scaffold a new DRS-compliant project'
    Write-Host '    validate           Check all required manifest fields are present'
    Write-Host '    verify-manifest    Check manifest field consistency'
    Write-Host '    check-release      Full release readiness check (manifest + artifact + docs)'
    Write-Host '    hash <path>        Compute SHA-256 for a release artifact'
    Write-Host '    hash <path> --blake3  Compute SHA-256 plus BLAKE3 when b3sum or blake3 is available'
    Write-Host '    init-docs          Copy doc templates to docs/ with project name applied'
    Write-Host '    help               Show this help'
    Write-Host ''
    Write-Host '  Examples:' -ForegroundColor DarkGray
    Write-Host '    .\drs.ps1 new MyApp'
    Write-Host '    .\drs.ps1 validate'
    Write-Host '    .\drs.ps1 check-release'
    Write-Host '    .\drs.ps1 hash artifacts\installer\MyApp-1.0.0.0-win-x64.msi'
    Write-Host '    .\drs.ps1 hash artifacts\installer\MyApp-1.0.0.0-win-x64.msi --blake3'
    Write-Host '    .\drs.ps1 init-docs'
    Write-Host ''
    Write-Host '  Typical release workflow:' -ForegroundColor DarkGray
    Write-Host '    1. drs verify-manifest     (check fields before building)'
    Write-Host '    2. [build installer]'
    Write-Host '    3. drs hash <installer>    (get SHA-256 for manifest and release note)'
    Write-Host '    4. [update manifest + release note with hash]'
    Write-Host '    5. drs check-release       (full gate before publishing)'
    Write-Host ''
}

# -----------------------------------------------------------------------------
# DISPATCH
# -----------------------------------------------------------------------------

switch ($Command.ToLower()) {
    'new'              { Invoke-DrsNew $Arg1 }
    'validate'         { Invoke-DrsValidate }
    'verify-manifest'  { Invoke-DrsVerifyManifest }
    'check-release'    { Invoke-DrsCheckRelease }
    'hash'             { Invoke-DrsHash $Arg1 $Arg2 }
    'init-docs'        { Invoke-DrsInitDocs }
    'help'             { Show-Help }
    default            { Show-Help; Set-DrsExitCode 2 }
}

exit $script:DrsExitCode
