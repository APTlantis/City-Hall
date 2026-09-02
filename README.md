# Aptlantis City Hall

![Standards](https://img.shields.io/badge/standards-active-green)
![Governance](https://img.shields.io/badge/governance-canonical-blue)
![WGS](https://img.shields.io/badge/WGS-workspace%20authority-purple)

`D:\.city_hall` is the canonical active standards resource for the Aptlantis development drive.
It holds the standards, templates, maps, and adopted governance reference material that are solid enough to guide active work.

`D:\.city_hall\City Planning` is the development workshop for standards: incubation, experiments, promotion review, historical lineage, and preserved planning records live there.
City Planning drafts do not govern active projects until they are deliberately adopted by an active City Hall standard.

The root drive manifest, `D:\Development.manifest.toml`, was restored on 2026-08-20 as the machine-readable root registry.
If it is missing in a future pass, agents should record that drift and use `D:\AGENTS.md`, `D:\INDEX.md`, this City Hall README, and the relevant active suite manifests as the practical recovery path.

## Start Here

For active Aptlantis governance:

1. `D:\AGENTS.md`
2. `D:\INDEX.md`
3. this README
4. `WORKSHOP-MAP.md`
5. the relevant active standard suite below

For standards incubation, historical comparison, or promotion review, use `D:\.city_hall\City Planning` after reading this active City Hall record first.

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
| `ARHS` | Aptlantis Release Hashing Standard | Single-artifact release hash manifests and release distribution/signing provenance records. |
| `AAMHS` | Aptlantis Archive Multi-Hash Standard | Archive preservation integrity records, validation procedures, and detached archive signatures. |
| `SESM` | SVG Embedded Semantic Metadata | Safe semantic metadata embedded in SVG assets. |
| `blue.slate` | Blue Slate Visual System | Aptlantis design tokens, operational surfaces, layout patterns, and framework profiles. |
| `Blanks` | Blank governance templates | Entity-named manifest and README templates for governed work. |

## Adopted Overview Material

The following overview materials are maintained here because they describe active, adopted Aptlantis governance rather than City Planning-only experimentation:

- `WORKSHOP-MAP.md` - guided map of active standards, related project areas, and reading paths.
- `City Hall Operational Case Study.md` - maintainable source for the revised library-facing case study.
- `City Hall Operational Case Study.pdf` - adopted evidence record showing the governance system operating end to end.

City Planning may keep reference copies or pointers for workshop continuity, but this City Hall copy is the active navigation target for agents looking for solid standards.

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

Use City Planning when the question is, "How did this standard develop, what is still experimental, or what should be promoted next?"

When these records disagree, prefer:

1. the user's current request
2. nearest active `AGENTS.md`
3. entity-named manifests and project README/proposal records
4. active standards under City Hall
5. verified current source, tests, artifacts, and evidence
6. City Planning-only drafts, references, and preserved planning material
