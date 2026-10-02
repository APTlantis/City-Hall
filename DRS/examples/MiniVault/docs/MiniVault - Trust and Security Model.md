# MiniVault — Trust and Security Model

**Version:** MiniVault v0.1.0
**Document status:** Current
**Last updated:** 2026-06-04

MiniVault is a local-first application. It stores secrets on the local machine, encrypted with a key derived from the user's passphrase. It makes no network connections. This document describes what MiniVault trusts, what it protects, and what it explicitly does not address.

This trust model is honest about its scope. It covers what was designed and tested. It does not make claims beyond that.

---

## Scope

This document covers:

* How vault data is encrypted and where it is stored
* What happens to key material during a session
* What network connections MiniVault makes (none)
* What the installer and uninstaller touch
* Known security limitations of this release

This document does not cover:

* The security of the Windows operating system or user account
* Physical access attacks
* The security of any other application that might read `%APPDATA%\MiniVault`

---

## Data Classification

| Data | Sensitivity | Location | Protection |
|------|-------------|----------|-----------|
| Vault secrets (values) | High | `%APPDATA%\MiniVault\vault.mv` (encrypted) | AES-256-GCM; key never written to disk |
| Vault secret names | Medium | `%APPDATA%\MiniVault\vault.mv` (encrypted) | Same — names are part of the ciphertext |
| Passphrase | Critical | Memory only during unlock | Never stored anywhere |
| Derived encryption key | Critical | Memory only during session | Held in a `SecureString`; never written to disk |
| Application settings | Low | `%APPDATA%\MiniVault\settings.json` | Plaintext — contains no secrets |

---

## Trust Boundaries

### What MiniVault trusts

* The Windows operating system and its memory protection
* The authenticated user who launched the application
* Files in the install directory at `%LOCALAPPDATA%\Programs\MiniVault` (assumed to be the unchanged installer artifact — see SHA-256 in release note)

### What MiniVault does not trust

* The vault file at `%APPDATA%\MiniVault\vault.mv` — format and MAC are validated before any data is read
* Settings file at `%APPDATA%\MiniVault\settings.json` — validated against a schema before use
* Clipboard contents — treated as untrusted input in all paste operations

---

## Cryptographic Primitives

| Primitive | Algorithm | Parameters | Usage | Library |
|-----------|-----------|-----------|-------|---------|
| Symmetric encryption | AES-256-GCM | 256-bit key, 96-bit nonce, 128-bit tag | Vault data at rest | `System.Security.Cryptography.AesGcm` (.NET 9 inbox) |
| Key derivation | PBKDF2-HMAC-SHA256 | 600,000 iterations, 32-byte salt, 32-byte output | Passphrase → encryption key | `System.Security.Cryptography.Rfc2898DeriveBytes` (.NET 9 inbox) |
| Random number generation | OS-backed CSPRNG | — | Salt generation, nonce generation | `System.Security.Cryptography.RandomNumberGenerator` |

No third-party cryptographic library is used. All primitives are from the inbox .NET 9 `System.Security.Cryptography` namespace.

---

## Session Lifecycle

**Vault locked (default state):** Key material does not exist in memory. The vault file is not open. No secrets are accessible.

**Unlock:** User provides passphrase. Key is derived using PBKDF2. AES-GCM authentication tag is verified. If verification fails, the vault is not opened — the wrong passphrase and a tampered vault are indistinguishable at this layer by design.

**Vault unlocked:** Key is held in memory in a `SecureString`. Secrets are decrypted on demand, not all at once. Plaintext secret values are held in memory only as long as the UI needs them.

**Lock:** `SecureString` is disposed. GC collection of key material is not guaranteed to be immediate — this is a known limitation (see Known Limitations below).

**Exit:** Application terminates normally. OS reclaims process memory.

---

## Network Behavior

MiniVault is fully offline. It makes no network connections of any kind.

Any unexpected outbound connection from the MiniVault process is a defect and should be reported. Operators can verify this using the network monitoring command in the PowerShell reference guide.

---

## Installer and Uninstaller Behavior

**Install:** Places application files in `%LOCALAPPDATA%\Programs\MiniVault`. Does not create the vault or data directory — first-run behavior creates those.

**Uninstall:** Removes application files from the install directory only. Does not delete `%APPDATA%\MiniVault`. User data is never touched by the uninstaller. This was verified as part of the v0.1.0 release checklist.

---

## Known Limitations

* **No third-party security audit.** This release has not been reviewed by an external security professional. It should not be used to protect secrets where a security audit would be required.

* **Key material persistence after lock.** The derived encryption key is held in a `SecureString`. After vault lock, the key is disposed, but .NET's garbage collector does not guarantee immediate memory reclamation. Key material may persist in process memory for an indeterminate period after lock. This is acceptable for v0.1.0 but is a known gap.

* **No passphrase strength enforcement.** MiniVault accepts any passphrase, including weak ones. The security of the vault depends entirely on the strength of the passphrase chosen by the user.

* **No in-app backup.** The vault file is a single file. If it is deleted or corrupted, all secrets are lost. The operator is responsible for backing up `%APPDATA%\MiniVault\vault.mv`.

* **PBKDF2 iteration count is fixed at 600,000.** This count is appropriate as of 2026. It will need to be reviewed and increased in future releases as hardware improves.

---

## Audit and Review Status

| Review Type | Status | Date | Reviewer |
|-------------|--------|------|---------|
| Internal review | Completed | 2026-06-04 | H. Schumann |
| Third-party audit | Not performed | — | N/A |
| Penetration test | Not performed | — | N/A |

This release does not claim production readiness. A third-party audit is planned before any production or public release.
