# D:\ Development Workspace Instructions

This file is the drive-wide instruction layer. Read `D:\Development.manifest.toml` and `D:\INDEX.md`, then inherit the nearest portfolio and project `AGENTS.md` files in path order.
If `D:\Development.manifest.toml` is missing in a future pass, record that as root governance drift instead of inferring it from historical references.

## Authority order

1. The user's current request.
2. The nearest active `AGENTS.md` files from workspace to project.
3. Entity-named manifests and project proposal/readme records.
4. Canonical standards under `D:\.library\aptlantis_core`.
5. Existing source, tests, artifacts, and verified operational evidence.
6. Historical, incubating, or non-promoted references, including City Hall-only drafts and `D:\.zoning` candidates.

When documents disagree, do not silently blend them. Prefer the narrower active instruction and verified current state; record consequential drift.

## Canonical standards currently in use

- [Workspace Governance Standard](D:/.library/aptlantis_core/WGS/README.md)
- [Standards Framework Development Standard](D:/.library/aptlantis_core/SFDS/README.md)
- [Project Proposal Standard](D:/.library/aptlantis_core/PPS/README.md)
- [Library Development Standard](D:/.library/aptlantis_core/LDS/README.md)
- [Command Tool Standard](D:/.library/aptlantis_core/CTS/README.md)
- [Desktop Application Release Standard](D:/.library/aptlantis_core/DRS/README.md)
- [Website Development Standard](D:/.library/aptlantis_core/WDS/README.md)
- [Aptlantis Release Hashing Standard](D:/.library/aptlantis_core/ARHS/README.md)
- [Archive Multi-Hash Standard](D:/.library/aptlantis_core/AAMHS/README.md)
- [SVG Embedded Semantic Metadata](D:/.library/aptlantis_core/SESM/README.md)
- [Blue Slate Visual System](D:/.library/aptlantis_core/BlueSlate/README.md)
- [Blank governance templates](D:/.library/aptlantis_core/Blanks)

`D:\.library\aptlantis_core` is the canonical active standards library for standards and adopted governance overview material that already govern projects. `D:\.city_hall` is the standards workshop and sandbox for incubation, experimentation, historical lineage, review, archive, and promotion. City Hall-only drafts, historical references, and zoning candidates do not govern active projects until deliberately promoted into `aptlantis_core` or explicitly adopted by a governing standard.
NeonInk lineage currently remains City Hall material unless promoted into `D:\.library\aptlantis_core`.
`D:\.zoning` is the general intake and incubation area for rough project and standard ideas before PPS/WGS onboarding, standard assignment, promotion, and relocation.

## Required project records

- Portfolios and governed containers use `AGENTS.md` plus `[DirectoryName].manifest.toml`.
- Projects use `AGENTS.md`, `[ProjectName].manifest.toml`, and `Project-README.md`.
- New or substantially redirected projects also use PPS proposal documentation before broad implementation.
- Manifest and directory names preserve the project's exact casing.

## Change safety

- Inspect current source, manifests, documentation, tests, and artifacts before changing lifecycle or release claims.
- Preserve unrelated user changes and historical evidence.
- Do not move or delete governed work without checking parent/child registration and references.
- Keep credentials, secrets, and private endpoints out of source and governance records.
- Treat destructive operations, migrations, and broad rewrites as explicit work requiring visible boundaries and verification.

## Verification and release honesty

- A passing build does not establish release readiness.
- Verify the actual shipping artifact, version, hashes, installation, launch, documentation, and recovery behavior before a release claim.
- Record failures and blockers plainly.
- Update parent manifests, INDEX entries, proposals, and agent instructions when identity, scope, or authority changes.

## Agent closeout

Substantial changes are not complete until recovery documents are updated.
After changing projects, standards, root structure, lifecycle state, promotion state, authority, or discovery paths, update the direct records beside the changed entity and the extended navigation records that let future agents find it.

Direct records include manifests, `AGENTS.md`, `Project-README.md`, README files, changelogs, validation checklists, release notes, adoption notes, and standard-specific records.
Extended records include `D:\INDEX.md`, `D:\Development.manifest.toml` when present, parent manifests, library README/maps, City Hall README/workshop maps, WGS responsibility matrices, inventories, target maps, standards registries, and promotion notes.
If a direct or extended record does not need changes, say so in the handoff; if it should change but cannot be updated, record the gap plainly.
