# [AppName] — Integrity Validation Matrix

**Version:** [AppName] v[X.Y.Z]
**Last updated:** [YYYY-MM-DD]

This document defines what a healthy application state looks like, how to detect drift from that state, and what repair actions are available. It is the reference for any verification or repair workflow within the application.

---

## Purpose

An integrity validation matrix answers three questions for each inspectable component:

1. **What is the expected state?** — what "healthy" looks like
2. **How is drift detected?** — the check that reveals a problem
3. **What is the repair action?** — what the application does, and whether it requires operator approval

---

## Severity Levels

| Level | Meaning | Default Action |
|-------|---------|---------------|
| Critical | Application cannot function safely; data may be at risk | Block launch or operation |
| High | Core functionality is impaired | Warn operator; offer repair |
| Medium | Degraded state; partial functionality may be affected | Log; surface in health UI |
| Low | Minor inconsistency; no functional impact | Log only |

---

## Component: [e.g. Data Directory]

| Check | Expected State | Detection Method | Severity if Failed | Repair Action | Requires Approval |
|-------|---------------|------------------|--------------------|---------------|-------------------|
| [e.g. Data directory exists] | [e.g. `%APPDATA%\AppName\` exists] | [e.g. `Directory.Exists()` on startup] | High | [e.g. Create directory] | No |
| [e.g. Settings file is valid JSON] | [e.g. Parses without exception, passes schema validation] | [e.g. `JsonDocument.Parse()` on startup] | Medium | [e.g. Reset to defaults; back up corrupt file] | No |

---

## Component: [e.g. Vault / Data Store]

| Check | Expected State | Detection Method | Severity if Failed | Repair Action | Requires Approval |
|-------|---------------|------------------|--------------------|---------------|-------------------|
| [e.g. Vault file exists] | [e.g. `vault.db` exists in data directory] | [e.g. `File.Exists()` before unlock attempt] | High | [e.g. Offer to initialize a new vault] | Yes |
| [e.g. Vault schema version] | [e.g. Schema version matches application expectation] | [e.g. Read header on open] | Critical | [e.g. Block open; display migration instructions] | Yes |
| [e.g. Vault MAC valid] | [e.g. AEAD authentication tag verifies] | [e.g. Checked during decryption] | Critical | [e.g. Block open; do not attempt to read ciphertext] | N/A — cannot repair |

---

## Component: [e.g. Application Binaries]

| Check | Expected State | Detection Method | Severity if Failed | Repair Action | Requires Approval |
|-------|---------------|------------------|--------------------|---------------|-------------------|
| [e.g. Core DLLs present] | [e.g. All assemblies in install directory] | [e.g. Checked at launch] | Critical | [e.g. Prompt user to reinstall] | Yes |

---

## Repair Log

[AppName] logs repair actions to: `[path/to/repair-log.jsonl]`

Each entry records:
* Timestamp (ISO 8601)
* Check that failed
* Severity
* Repair action taken
* Whether operator approval was granted

The repair log is append-only. Entries are never deleted.

---

## What Cannot Be Repaired

These conditions represent irrecoverable state. The application does not attempt repair:

* [e.g. Corrupted vault ciphertext — decryption failure cannot be reversed; data recovery requires a backup]
* [e.g. Missing encryption key — the key is never stored on disk; it cannot be reconstructed]

In these cases the application surfaces a clear error and does not modify any data.

---

## Verification Command

[If the application exposes a CLI verification mode, document it here.]

```powershell
# Run integrity verification and exit with code 0 (pass) or 1 (fail)
[AppName].exe verify

# Exit with non-zero if any check at or above the specified severity fails
[AppName].exe verify --fail-on medium
```

---

## Change Log

| Version | Change | Date |
|---------|--------|------|
| v[X.Y.Z] | Initial matrix | [YYYY-MM-DD] |
