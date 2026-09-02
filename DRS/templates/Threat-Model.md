# [AppName] — Threat Model

**Version:** [AppName] v[X.Y.Z]
**Document status:** [Draft / Under review / Current]
**Last updated:** [YYYY-MM-DD]

This document describes the attack surface, trust boundaries, and known limitations of [AppName]. It is the basis for security claims made in release notes and the trust model.

> A threat model does not need to be comprehensive at creation. It should be honest about its current scope. An incomplete threat model that states what it covers is more useful than no threat model.

---

## System Overview

[One paragraph: what [AppName] does, where it runs, and what data it touches. This is the context for every threat analysis that follows.]

**Deployment model:** [e.g. Single-user, local Windows desktop application. No network connectivity. No server component.]

**Trust perimeter:** [e.g. The application runs within a single user session. It trusts the OS and the authenticated user. It does not trust any data read from disk beyond format validation.]

---

## Assets

Assets are what an attacker would want to compromise, steal, or destroy.

| Asset | Sensitivity | Description |
|-------|-------------|-------------|
| [e.g. Vault data] | High | [e.g. Encrypted user records stored in %APPDATA%\AppName\vault.db] |
| [e.g. Encryption key] | Critical | [e.g. Derived from user passphrase, held in memory during session, never written to disk] |
| [e.g. Application settings] | Low | [e.g. Non-sensitive configuration in %APPDATA%\AppName\settings.json] |
| [e.g. Application binaries] | Medium | [e.g. Could be replaced to deliver a trojanized version] |

---

## Trust Boundaries

```
┌─────────────────────────────────────────────┐
│  Windows OS (trusted)                       │
│  ┌─────────────────────────────────────┐    │
│  │  User Session (trusted)             │    │
│  │  ┌─────────────────────────────┐    │    │
│  │  │  [AppName] Process          │    │    │
│  │  │                             │    │    │
│  │  │  ┌────────────┐             │    │    │
│  │  │  │ Memory     │             │    │    │
│  │  │  │ (key mat.) │             │    │    │
│  │  │  └────────────┘             │    │    │
│  │  └─────────────────────────────┘    │    │
│  │                                     │    │
│  │  %APPDATA%\AppName\ (semi-trusted)  │    │
│  └─────────────────────────────────────┘    │
└─────────────────────────────────────────────┘
```

[Adjust the diagram to reflect the actual architecture. Identify where trust changes.]

---

## Threat Enumeration

For each threat, rate likelihood (Low / Medium / High) and impact (Low / Medium / High / Critical) given the current mitigations.

### T1 — [Threat name, e.g. Vault data exfiltration by local attacker]

**Category:** [e.g. Information disclosure]
**Attacker position:** [e.g. Local user with access to %APPDATA%]
**Attack vector:** [e.g. Copy vault.db from %APPDATA%\AppName\vault.db]

**Mitigations:**
* [e.g. Vault is encrypted with AES-256-GCM; the key is not stored on disk]
* [e.g. An attacker without the passphrase cannot decrypt the vault]

**Residual risk:** [e.g. Low — vault data is ciphertext without the key material]
**Likelihood:** [Low / Medium / High]
**Impact:** [Low / Medium / High / Critical]
**Accepted:** [Yes / No — if No, describe the planned mitigation]

---

### T2 — [Threat name, e.g. Binary replacement (supply chain)]

**Category:** [e.g. Tampering, elevation of privilege]
**Attacker position:** [e.g. Write access to the install directory]
**Attack vector:** [e.g. Replace application DLLs with malicious versions]

**Mitigations:**
* [e.g. Installation requires elevation; normal user sessions cannot modify install directory]
* [e.g. Installer artifact hash is published in the release note — operators can verify before installing]

**Residual risk:** [e.g. Medium — administrator accounts can still replace binaries; no runtime integrity verification]
**Likelihood:** Low
**Impact:** Critical
**Accepted:** [Yes / No]

---

### T3 — [Add additional threats]

[Repeat the above structure for each identified threat.]

---

## Out of Scope

The following are explicitly out of scope for this threat model:

* [e.g. Physical access attacks — the threat model assumes the user's machine is not physically compromised]
* [e.g. OS-level exploits — the threat model assumes the OS is not compromised]
* [e.g. Network attacks — this application is fully offline and makes no network connections]

---

## Known Gaps

Security properties that are not yet addressed and are accepted as known gaps:

* [e.g. "No runtime integrity check of application binaries after installation."]
* [e.g. "Key material may persist in memory after vault lock until garbage collected."]
* [e.g. "Log files are not encrypted; they may contain metadata about user activity."]

---

## Assumptions

This threat model is valid only under the following assumptions:

* [e.g. The operating system has not been compromised]
* [e.g. The user's account password is not known to the attacker]
* [e.g. The installer was obtained from the verified release artifact with a confirmed SHA-256 hash]

---

## Revision History

| Version | Change | Date |
|---------|--------|------|
| v[X.Y.Z] | Initial threat model | [YYYY-MM-DD] |
