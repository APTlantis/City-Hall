# [AppName] v[X.Y.Z] — [Release Theme Name]

[One paragraph: what this release is about and why it exists. The tone is honest about scope.
Do not oversell a patch as a feature release. Do not summarize git commits — group by meaning.
Write this paragraph before or simultaneously with the final build, not after.]

---

## Highlights

### [Feature or Change Area Name]

[Plain description. What changed, why it matters, what the operator can now do or observe.
Write for someone who has not seen the code and does not know what was broken.]

### [Second Feature or Change Area]

[Repeat for each meaningful change. A patch release may have only one Highlights section.]

---

## What This Release Improves

[Optional for patches. For minor releases: a short paragraph connecting the highlights to the
broader direction of the project. This is not a changelog — it is a statement of intent.]

---

## Design Boundaries

[AppName] v[X.Y.Z] intentionally does not:

* [Thing that was considered but scoped out of this release]
* [Behavior that operators might expect but is deliberately absent]
* [Complexity that will be addressed in a future release]
* [Dependency or integration that was evaluated and deferred]

> This section is required. There are always design boundaries.
> Do not omit it because "there are no limits."

---

## Built With

* [Framework and version — e.g. .NET 9.0]
* [Language — e.g. C# 13]
* [Runtime — e.g. Windows Desktop Runtime 9.0.x]
* [Installer toolchain — e.g. WiX Toolset v5.x]
* [Other notable dependencies]

---

## Release Artifact

Expected installer:

* `[AppName]-[X.Y.Z.0]-win-x64.[ext]`

SHA-256:

* `[UPPERCASE HEX SHA-256 HASH — NO SEPARATORS]`

[Optional: BLAKE3 hash if applicable. For publishable artifacts, attach the ARHS `.hashmanifest.toml`.]

[Distribution and signing/provenance statement — e.g. "Distribution: microsoft-store-msix. Signing: microsoft-store-signed." For development builds, state that sideloaded self-signed MSIX packages are non-production.]

---

## Required Fields Checklist

Before publishing this release note, confirm:

- [ ] Version number matches project manifest (`*.manifest.toml`) and assembly version
- [ ] Theme name is present and accurately reflects the actual scope of the release
- [ ] At least one Highlights section with a plain-language description
- [ ] Design Boundaries section with at least two entries
- [ ] Built With section lists all notable dependencies
- [ ] Release Artifact section contains the exact installer filename
- [ ] SHA-256 hash is present, uppercase, no separators
- [ ] SHA-256 hash matches the artifact file on disk
- [ ] Distribution and signing/provenance status are stated explicitly
- [ ] This file is in `docs/` and included in the build publish output

> Remove this checklist section before publishing.

---

## Prohibited Content

> Before publishing, verify none of the following appear in this document.
> Remove this section after review.

- Do not claim production readiness without a security review on record
- Do not omit Design Boundaries because "there are no limits"
- Do not write this as a commit log — group by meaning, not by change
- Do not list changes that did not ship in this version
