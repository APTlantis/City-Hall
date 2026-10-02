# Blue Slate Changelog

## 0.5.0 - 2026-09-27

- Adopted the reviewed desktop v0.4.x token, overview, layout, specimen and tooling work into City Hall; preserved all 27 palette values and existing semantic/component/foundation/typography values.
- Made TOML the editable token authority; retained the v0.3 JSON/CSS interfaces at their original paths with an explicit migration guide.
- Consolidated duplicate references, cataloged the two supplied visual boards, and moved the palette extractor to tools without treating extraction output as canonical tokens.
- Replaced the permissive compiler parser with Python's TOML parser, added true read-only generated freshness checks, propagated conversion failures, and added negative regression coverage.
- Corrected profile coverage, missing-file claims, adoption levels and stylesheet-inventory boundaries; Bootstrap remains a preserved v0.3 compatibility profile.
- Added an adopter template, suite map, source contract, directory review and comprehensive `aptlantis-blue-slate` skill replacing the two fragments.
- Registered Candidate v0.5.0 in the WGS roadmap. Candidate-active maturity is retained pending representative adopter/runtime evidence; no live application deployment is claimed.

## 0.4.1 - 2026-09-16

- Corrected the exact sRGB-to-OKLCH conversion values and added a regression check for every palette entry.
- Reaffirmed the canonical dual-representation contract: hex is retained beside OKLCH in the matrix and generated CSS.
- Reworked the specimen around actual BlueSlate portal, Filing Cabinet, and SiYuan contexts rather than a generic dashboard.

## 0.4.0 - 2026-09-16

- Replaced the JSON canonical token source with an OKLCH-first TOML matrix while retaining exact sRGB fallback values and a generated JSON compatibility export.
- Added deterministic CSS, Tailwind v4, and SiYuan translations; Bootstrap remains legacy profile evidence rather than a canonical target.
- Added source stylesheet inventory, theme audit, framework-neutral specimen, and semantic swatch-board tooling.

## 0.3.0 - 2026-09-02

- Expanded the framework-neutral semantic contract with operational surface, content, structure, intent, interaction, validation, elevation, radius, spacing, and focus roles while preserving existing palette values.
- Added the maintained single-dark-theme Bootstrap 5.3 profile, local root-variable translation, and component-state starter example.
- Defined the boundary between canonical Blue Slate semantics and Bootstrap-required compatibility aliases; existing profiles remain valid and may adopt the new roles incrementally.
- Updated adoption and validation guidance for Bootstrap version recording, state coverage, contrast, and visible keyboard focus.
- Preserved `D:\.zoning\blue-slate-bootstrap` as dated source evidence rather than treating it as canonical authority.

## Unreleased - 2026-08-20

- Normalized the active library manifest to `BlueSlate.manifest.toml` with SFDS-required `[standard]` and `[governance]` metadata while preserving the Blue Slate / blue.slate product identity.
- Removed the nonexistent `apps` artifact reference from the active manifest and kept `spec/mockups` as the visual-reference artifact.
- Updated active path references from `D:\.city_hall\blue.slate` to the physical `D:\.city_hall\BlueSlate` directory.

## 0.2.0 - 2026-07-25

- Promoted Blue Slate to candidate-active standard-suite status.
- Added README, adoption guide, validation checklist, and promotion history.
- Clarified relationship to NeonInk lineage and SESM.
- Preserved token source, layout patterns, framework notes, starter packs, screenshots, and mockups.

## 0.1.0 - 2026-07-22

- Onboarded Blue Slate as an incubating visual-system project with tokens, mockups, framework notes, and starter packs.
