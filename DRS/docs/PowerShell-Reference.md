# DRS — PowerShell Release Reference

Copy-pasteable PowerShell commands for common release tasks. All commands assume PowerShell 7+.

---

## Artifact Integrity

### Compute SHA-256 (manifest and release note format)

```powershell
(Get-FileHash ".\artifacts\installer\AppName-1.0.0.0-win-x64.msi" -Algorithm SHA256).Hash
```

Output is uppercase hex — paste directly into the manifest and release note.

### Compute SHA-256 plus optional BLAKE3

```powershell
.\drs.ps1 hash ".\artifacts\installer\AppName-1.0.0.0-win-x64.msi" --blake3
```

DRS requires SHA-256 as the minimum integrity record.
BLAKE3 is optional and useful for security-sensitive releases or internal archive workflows that already use a trusted BLAKE3 tool.
Install `b3sum` or `blake3` before using this mode.

### Compute SHA-256 and display manifest snippet

```powershell
$file = Get-Item ".\artifacts\installer\AppName-1.0.0.0-win-x64.msi"
$hash = (Get-FileHash $file.FullName -Algorithm SHA256).Hash
Write-Host "size_bytes = $($file.Length)"
Write-Host "sha256     = `"$hash`""
```

### Get file size in bytes

```powershell
(Get-Item ".\artifacts\installer\AppName-1.0.0.0-win-x64.msi").Length
```

### Verify hash against manifest value

```powershell
$expected = "PASTE-HASH-FROM-MANIFEST-HERE"
$actual   = (Get-FileHash ".\artifacts\installer\AppName-1.0.0.0-win-x64.msi" -Algorithm SHA256).Hash
if ($actual -eq $expected) { Write-Host "MATCH" -ForegroundColor Green }
else                        { Write-Host "MISMATCH — do not release" -ForegroundColor Red }
```

---

## Build and Test

### Clean restore and Release build

```powershell
dotnet restore --locked-mode && dotnet build -c Release
```

### Full test run with recorded output

```powershell
dotnet test -c Release --logger "console;verbosity=normal" | Tee-Object -FilePath "release-evidence\vX.Y.Z\test.log"
```

### Extract test pass count from output

```powershell
dotnet test -c Release | Select-String 'passed'
```

### Publish win-x64

```powershell
dotnet publish src\AppName\AppName.csproj `
  -c Release `
  -r win-x64 `
  --self-contained false `
  -o artifacts\publish\win-x64
```

---

## Evidence Capture

### Record file hash to evidence folder

```powershell
$version = "1.0.0"
$artifact = ".\artifacts\installer\AppName-$version.0-win-x64.msi"
New-Item -ItemType Directory -Force -Path "release-evidence\v$version" | Out-Null
$item = Get-Item $artifact
$hash = (Get-FileHash $artifact -Algorithm SHA256).Hash
@"
File:      $($item.Name)
Size:      $($item.Length) bytes
SHA-256:   $hash
Computed:  $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')
"@ | Set-Content "release-evidence\v$version\filehash.txt"
Write-Host "Written to release-evidence\v$version\filehash.txt"
```

### Record build result to evidence folder

```powershell
$version = "1.0.0"
New-Item -ItemType Directory -Force -Path "release-evidence\v$version" | Out-Null
dotnet build -c Release 2>&1 | Tee-Object -FilePath "release-evidence\v$version\build.log"
```

### Record test result to evidence folder

```powershell
$version = "1.0.0"
dotnet test -c Release --logger "console;verbosity=normal" 2>&1 |
  Tee-Object -FilePath "release-evidence\v$version\test.log"
```

---

## Manifest Checks

### Check that version in manifest matches assembly version

```powershell
# Read manifest version (naive line search)
$manifestVersion = (Get-Content ".\AppName.manifest.toml" |
  Select-String -Pattern '^version\s*=\s*"(.+)"' |
  Select-Object -First 1).Matches[0].Groups[1].Value

# Read assembly version
$assemblyVersion = [System.Reflection.AssemblyName]::GetAssemblyName(
  ".\artifacts\publish\win-x64\AppName.dll"
).Version.ToString(3)

if ($manifestVersion -eq $assemblyVersion) {
  Write-Host "Version match: $manifestVersion" -ForegroundColor Green
} else {
  Write-Host "MISMATCH — manifest: $manifestVersion, assembly: $assemblyVersion" -ForegroundColor Red
}
```

### Quick manifest field dump

```powershell
Get-Content ".\AppName.manifest.toml" |
  Where-Object { $_ -match '^\s*(version|sha256|signing|status|date)\s*=' }
```

---

## Network Verification (offline apps)

### Monitor outbound connections during app launch

Run the application, then check for unexpected connections:

```powershell
# Before launching — capture baseline
$before = Get-NetTCPConnection -State Established

# Launch the application
Start-Process ".\artifacts\publish\win-x64\AppName.exe"
Start-Sleep -Seconds 5

# After launch — compare
$after  = Get-NetTCPConnection -State Established
$new    = Compare-Object $before $after -Property LocalPort, RemoteAddress, RemotePort |
          Where-Object { $_.SideIndicator -eq '=>' }

if ($new) {
  Write-Host "New connections detected — investigate:" -ForegroundColor Yellow
  $new | Format-Table
} else {
  Write-Host "No new outbound connections observed." -ForegroundColor Green
}
```

---

## Installer Verification

### Check installer file is not zero bytes

```powershell
$size = (Get-Item ".\artifacts\installer\AppName-1.0.0.0-win-x64.msi").Length
if ($size -gt 0) { Write-Host "Size: $size bytes" -ForegroundColor Green }
else             { Write-Host "File is empty" -ForegroundColor Red }
```

### Verify docs folder exists in publish output

```powershell
$docsPath = ".\artifacts\publish\win-x64\docs"
if (Test-Path $docsPath) {
  Write-Host "docs/ present:" -ForegroundColor Green
  Get-ChildItem $docsPath | Select-Object Name
} else {
  Write-Host "docs/ not found in publish output — check build script" -ForegroundColor Red
}
```

### Verify current release note is present in publish docs

```powershell
$version  = "1.0.0"
$notePath = ".\artifacts\publish\win-x64\docs\AppName v$version.md"
if (Test-Path $notePath) { Write-Host "Release note present" -ForegroundColor Green }
else                     { Write-Host "Release note missing from publish output" -ForegroundColor Red }
```

---

## Signing

### Check if MSI is signed (requires signtool or Get-AuthenticodeSignature)

```powershell
$sig = Get-AuthenticodeSignature ".\artifacts\installer\AppName-1.0.0.0-win-x64.msi"
Write-Host "Status:  $($sig.Status)"
Write-Host "Subject: $($sig.SignerCertificate?.Subject)"
```

Expected for a self-signed build: `Status: UnknownError` or `NotSigned`. Record whatever it returns as the signing status in the release note and manifest.

---

## Release Readiness One-Liner

Run all critical checks in sequence. Pipe to a log file if needed.

```powershell
$artifact = ".\artifacts\installer\AppName-1.0.0.0-win-x64.msi"
$hash     = "PASTE-EXPECTED-HASH-HERE"

Write-Host "=== DRS Release Readiness Check ===" -ForegroundColor Cyan
Write-Host "1. Artifact exists:  $(Test-Path $artifact)"
Write-Host "2. Hash match:       $((Get-FileHash $artifact -Algorithm SHA256).Hash -eq $hash)"
Write-Host "3. Docs present:     $(Test-Path '.\artifacts\publish\win-x64\docs')"
Write-Host "4. Tests:            $(dotnet test -c Release --no-build 2>&1 | Select-String 'passed' | Select-Object -Last 1)"
```
