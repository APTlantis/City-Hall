# Aptlantis City Hall

![Standards](https://img.shields.io/badge/standards-active-green)
![Governance](https://img.shields.io/badge/governance-canonical-blue)
![WGS](https://img.shields.io/badge/WGS-workspace%20authority-purple)

`D:\.city_hall` is the canonical active standards resource for the Aptlantis development drive.
It holds the standards, templates, maps, and adopted governance reference material that are solid enough to guide active work.

The root drive manifest, `D:\Development.manifest.toml`, is the machine-readable root registry.
If it is missing in a future pass, agents should record that drift and use `D:\AGENTS.md`, `D:\INDEX.md`, this City Hall README, and the relevant active suite manifests as the practical recovery path.

## Start Here

For active Aptlantis governance:

1. `D:\AGENTS.md`
2. `D:\INDEX.md`
3. this README
4. `WORKSHOP-MAP.md`
5. the relevant active standard suite below

## Active Standards

| Folder | Standard | Role |
| --- | --- | --- |
| `WGS` | Workspace Governance Standard | Workspace roots, manifests, lifecycle visibility, agent orientation, authority, and closeout. |
| `SFDS` | Standards Framework Development Standard | Standard-suite structure, maturity, validation, adoption, promotion, and preservation. |
| `PPS` | Project Proposal Standard | Project intent, responsibility posture, boundaries, constraints, risks, success, failure, version completion shape, and roadmap framing. |
| `LDS` | Library Development Standard | Libraries, crates, packages, SDKs, public APIs, stability, compatibility, and consumers. |
| `CTS` | Command Tool Standard | CLI contracts, streams, JSON envelopes, exit codes, automation behavior, and command safety. |
| `DRS` | Desktop Application Release Standard | Desktop build, packaging, release evidence, artifact verification, and distribution policy. |
| `WDS` | Website Development Standard | Website and web-application manifests, deployments, routes, accessibility, rollback, and monitoring. |
| `SIS` | Service and Infrastructure Standard | Local services, daemons, APIs, health checks, ports, logs, resource bounds, and recovery. |
| `DDS` | Dataset Development Standard | Dataset provenance, licensing, splits, validation, integrity, schemas, and release readiness. |
| `AAS` | Aptlantis Analysis Standard | Analysis manifests, evaluation records, metrics, comparisons, and interpretation boundaries. |
| `ATS` | Agent Task Standard | Replayable task records, handoffs, validation summaries, blockers, and agent-work context. |
| `ARHS` | Aptlantis Release Hashing Standard | Single-artifact release hash manifests and release distribution/signing provenance records. |
| `AAMHS` | Aptlantis Archive Multi-Hash Standard | Archive preservation integrity records, validation procedures, and detached archive signatures. |
| `SESM` | SVG Embedded Semantic Metadata | Safe semantic metadata embedded in SVG assets. |
| `NeonInk` | [NeonInk Data Presentation System](NeonInk/README.md) | Candidate v0.2.0: data presentation, charts, OKLCH tokens, reference images and [agent skill](NeonInk/skills/aptlantis-neonink/SKILL.md). Blue Slate remains the operational application theme. |
| `BlueSlate` | [Blue Slate Visual System](BlueSlate/README.md) | Candidate v0.5.0: semantic tokens, operational layouts, framework profiles and [comprehensive agent skill](BlueSlate/skills/aptlantis-blue-slate/SKILL.md). |
| `.blank-forms` | Blank governance templates | Entity-named manifest and README templates for governed work. |

## Adopted Overview Material

The following overview materials are maintained here because they describe active, adopted Aptlantis governance:

- `WORKSHOP-MAP.md` - guided map of active standards, related project areas, and reading paths.
- `City Hall Operational Case Study.md` - maintainable source for the revised library-facing case study.
- `City Hall Operational Case Study.pdf` - adopted evidence record showing the governance system operating end to end.

## Release and Integrity Boundaries

- Public Windows GUI applications default to MSIX submitted through the Microsoft Store; Microsoft signs the Store package.
- Windows GUI development builds may use MSIX sideload packages signed with a self-signed development certificate and documented as non-production.
- Direct MSI/EXE or non-Store GUI distribution is allowed only when documented; signing should be CA/Trusted Signing or clearly internal/private.
- Cross-platform CLIs use GitHub releases, package registries, or language ecosystems.
- Windows CLI ZIP or portable binaries may include ARHS `.hashmanifest.toml` evidence; Authenticode signing is optional unless the channel requires it.
- Rust, Python, Go, and similar language-tool releases rely primarily on ecosystem provenance plus release hash evidence, not MSIX.
- ArchiveHasher and `manifest-signer.exe` remain AAMHS archive-preservation tooling. They do not replace Microsoft Store signing or platform package signatures.

## Governance Boundary

Use City Hall when the question is, "What governs active work now?"

When records disagree, prefer:

1. the user's current request
2. nearest active `AGENTS.md`
3. entity-named manifests and project README/proposal records
4. active standards under City Hall
5. verified current source, tests, artifacts, and evidence
6. dated migration records and historical notes

## Framework hardening review — 2026-10-02

[The remediation record](WGS/reports/Framework-Gap-Remediation-2026-10-02.md) records verified fixes, disputed claims and remaining adopter work. SFDS 2.0 introduces prospective promotion gates; DRS 2.0 requires exact-artifact stage evidence for release readiness. Existing maturity labels are retained without new promotion claims. [The backlog](WGS/Standards-Evaluation-Backlog.md) tracks outstanding evidence. [The reviewed catalog](WGS/catalog/city-hall.json) preserves suite identity separately from public website publication.
