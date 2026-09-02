# [AppName] — Trust and Security Model

**Version:** [AppName] v[X.Y.Z]
**Document status:** [Draft / Under review / Current]
**Last updated:** [YYYY-MM-DD]

This document describes how [AppName] handles sensitive data, what it trusts, and what it deliberately does not do. It is a living reference that should be updated when security-relevant behavior changes.

An incomplete trust model that states what it covers is more useful than no trust model.

---

## Scope

This document covers:

* [Area 1 — e.g. how user credentials are stored]
* [Area 2 — e.g. how data is encrypted at rest]
* [Area 3 — e.g. what network connections the application makes]

This document does not cover:

* [Out-of-scope area — e.g. the operating system's security posture]
* [Out-of-scope area — e.g. network infrastructure between the user and any services]

---

## Data Classification

| Data Type | Sensitivity | Where Stored | How Protected |
|-----------|-------------|--------------|---------------|
| [e.g. User credentials] | High | [e.g. Windows Credential Manager] | [e.g. OS-managed, never written to disk by this application] |
| [e.g. Application settings] | Low | [e.g. %APPDATA%\AppName\settings.json] | [e.g. plaintext — contains no secrets] |
| [e.g. Vault data] | High | [e.g. %APPDATA%\AppName\vault.db] | [e.g. AES-256-GCM, key derived from user passphrase] |

---

## Trust Boundaries

### What [AppName] trusts

* [e.g. The Windows operating system and its security primitives (DPAPI, Credential Manager)]
* [e.g. The user who launched the application — no multi-user isolation within a single OS session]
* [e.g. Files in the install directory — assumed to be the unchanged build artifact]

### What [AppName] does not trust

* [e.g. Files in the data directory — format validation is enforced on read]
* [e.g. External network sources — application is fully offline; any unexpected network call is a defect]
* [e.g. Clipboard contents — treated as untrusted input]

---

## Cryptographic Primitives

| Primitive | Algorithm | Key Size | Usage | Library |
|-----------|-----------|----------|-------|---------|
| [e.g. Symmetric encryption] | [e.g. AES-256-GCM] | [e.g. 256-bit] | [e.g. Vault data at rest] | [e.g. System.Security.Cryptography] |
| [e.g. Key derivation] | [e.g. PBKDF2-HMAC-SHA256] | — | [e.g. Passphrase to encryption key] | [e.g. System.Security.Cryptography] |
| [e.g. Hash] | [e.g. SHA-256] | — | [e.g. Artifact integrity] | [e.g. System.Security.Cryptography] |

If no cryptographic primitives are used: state that explicitly. "This application does not use cryptography."

---

## Sensitive Operations

### [Operation name — e.g. Vault unlock]

**What happens:** [Plain description of what the operation does]

**Input:** [What the user or system provides]

**Output:** [What is produced or changed]

**Failure behavior:** [What happens if the operation fails — e.g. "key material is zeroed, vault is not opened"]

**Audit:** [Whether and how this operation is logged — e.g. "unlock attempts are not logged"]

---

## Data Retention and Deletion

* **Uninstall behavior:** [e.g. "The installer removes application binaries only. User data at %APPDATA%\AppName is not deleted."]
* **Data deletion:** [e.g. "User data can only be deleted manually. No in-app delete-all function exists."]
* **Temporary files:** [e.g. "No temporary files are written outside the application data directory."]
* **Clipboard:** [e.g. "Clipboard contents are cleared after N seconds when sensitive data is copied."]

---

## Network Behavior

[AppName] is: [**fully offline** / **network-aware** / **always-connected**]

[If offline: "This application makes no network connections. Any unexpected outbound connection from this process is a defect and should be reported."]

[If network-aware: List all outbound connections by destination, protocol, and purpose.]

---

## Known Limitations and Gaps

This section is honest about what the current security model does not address.

* [e.g. "This application has not undergone a third-party security audit."]
* [e.g. "Key material may remain in memory after vault lock if the GC has not collected it."]
* [e.g. "Log files are not encrypted and may contain metadata about user activity."]

---

## Audit and Review Status

| Review Type | Status | Date | Reviewer |
|-------------|--------|------|---------|
| Internal review | [Completed / Pending / Not performed] | [YYYY-MM-DD] | [Name] |
| Third-party audit | [Completed / Pending / Not performed] | [YYYY-MM-DD] | [Firm or N/A] |
| Penetration test | [Completed / Pending / Not performed] | [YYYY-MM-DD] | [Firm or N/A] |

> Do not claim production readiness in a release note without a security review on record.

---

## Change Log

| Version | Change | Date |
|---------|--------|------|
| v[X.Y.Z] | Initial document | [YYYY-MM-DD] |
