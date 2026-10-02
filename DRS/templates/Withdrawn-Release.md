# [AppName] v[X.Y.Z] — WITHDRAWN

**Withdrawn on:** [YYYY-MM-DD]
**Original publish date:** [YYYY-MM-DD]
**Replaced by:** [AppName vX.Y.Z, if a replacement exists — or "No replacement; see advisory"]
**Severity:** [Critical / High / Medium]

> This release has been withdrawn. The original release note is preserved below, annotated with the reason for withdrawal. Do not install this artifact.

---

## Reason for Withdrawal

[One paragraph explaining exactly why this release was withdrawn. Be specific and factual. Do not use vague language like "quality issues." State what was wrong, what the impact was, and whether any user data or systems were affected.]

**Category:** [Hash incorrect / Installer damages data / Unsupported security claim / Critical defect / Other]

**User impact:** [Who is affected and how. If no users installed this release, state that explicitly.]

---

## Affected Artifact

* **Installer:** `[AppName]-[X.Y.Z.0]-win-x64.[ext]`
* **SHA-256:** `[ORIGINAL HASH — now suspect if hash was incorrect]`
* **Status:** Do not install. Do not use.

---

## Remediation Instructions

[If users installed this release, what should they do? Options:]

* [If data corruption risk: "Back up [data path] before taking any action."]
* [If safe to upgrade: "Install [AppName] vX.Y.Z (or later), which supersedes this release."]
* [If no upgrade exists: "Uninstall [AppName]. Data at [data path] was not affected."]
* [If data was corrupted: "Contact [maintainer] before taking any action."]

---

## Manifest Update

The project manifest (`[AppName].manifest.toml`) has been updated:

```
[release]
status = "withdrawn"
```

The replacement release (if applicable) has a new manifest entry under `release.version`.

---

## Post-Withdrawal Review

| Item | Finding |
|------|---------|
| Root cause | [What caused the defect or error] |
| Detection method | [How the problem was discovered] |
| Time between release and withdrawal | [N hours / N days] |
| Users affected | [N users / No known installs] |
| Process gap identified | [What in the release process failed to catch this] |
| Process change | [What will be added to the checklist or standard to prevent recurrence] |

---

## Original Release Note (Preserved)

> The following is the original release note for [AppName] v[X.Y.Z], preserved for the historical record. It is annotated where claims are no longer accurate.

[Paste the original release note here, unchanged. Add inline annotations in blockquotes where necessary.]

---

*This withdrawal document is part of the [AppName] release record and should be stored in `docs/` alongside the original release note.*
