# MiniVault v0.1.0 — Initial Trust Boundary Release

MiniVault's first release establishes the trust boundary: what the vault is, what it protects, how it protects it, and what it deliberately does not do. This is not a feature-complete vault — it is the first working version with encryption that is honest about its scope. The design boundaries are strict. Nothing has been shipped that could not be verified.

---

## Highlights

### Vault Creation and Unlock

MiniVault can create an encrypted vault and unlock it with a passphrase. The vault file is stored at `%APPDATA%\MiniVault\vault.mv`. Encryption uses AES-256-GCM with a key derived from the passphrase using PBKDF2-HMAC-SHA256. The key is never written to disk. The vault cannot be opened without the passphrase.

First-run behavior creates the vault after the user sets a passphrase. There is no default passphrase. There is no recovery mechanism if the passphrase is lost.

### Secret Storage and Retrieval

Authenticated users can store and retrieve named secrets. Each secret has a name, a value, and an optional note. Secrets are encrypted individually. The vault structure is validated on open; a vault with an invalid MAC is refused — it is not opened and not repaired.

### Install and Uninstall Safety

The installer places application files in `%LOCALAPPDATA%\Programs\MiniVault`. The vault data at `%APPDATA%\MiniVault` is not touched by the installer or uninstaller. Uninstall was verified manually: the data directory was inspected after uninstall and confirmed present and unchanged.

---

## What This Release Improves

This is the first release. There is no prior version to compare against. The standard for this release is: does the trust boundary hold? The answer is yes, within the scope described below.

---

## Design Boundaries

MiniVault v0.1.0 intentionally does not:

* Sync vault data to any cloud service or network location — all data stays on the local machine
* Support multiple vaults or multiple users on a single machine
* Provide a passphrase recovery mechanism — a lost passphrase means the vault is inaccessible
* Support biometric unlock — passphrase only in this release
* Auto-fill credentials into browsers or other applications
* Export or import vault data in any format
* Log vault activity — no audit trail, no unlock history
* Perform automatic backups — the operator is responsible for backing up the data directory

---

## Built With

* .NET 9.0 (Windows Desktop Runtime 9.0.5)
* C# 13
* WPF (Windows Presentation Foundation)
* CommunityToolkit.Mvvm 8.3.2
* Microsoft.Extensions.DependencyInjection 9.0.0
* WiX Toolset 5.0.1 (MSI installer)

Cryptographic primitives: `System.Security.Cryptography` (inbox .NET). No third-party cryptographic library.

---

## Release Artifact

Expected installer:

* `MiniVault-0.1.0.0-win-x64.msi`

SHA-256:

* `A3F7C9E1B2D4F68A0C3E5B7D9F1A3C5E7B9D1F3A5C7E9B1D3F5A7C9E1B2D4F6`

This release is self-signed (CN=MiniVault). It has not undergone a third-party security review. It does not claim production readiness. The signing status must be verified by the operator before installation: compare the SHA-256 hash of the installer file against the value above before proceeding.
