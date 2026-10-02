# NeonInk 0.2 migration — 2026-09-27

## Deliberate redirection

The user established Blue Slate as the house theme for dense technical applications and NeonInk as the data-presentation system. Version 0.2.0 replaces the old all-UI/whole-brand scope for new work. Maturity remains Candidate; `candidate-active` makes that explicit and replaces the README's unsupported “mostly-stable / 75%” language.

`spec/NeonInk.DesignSystem.md` supersedes the previous primary `Docs/NeonInk-v0.1.1.md`. The old NIPC, AIC, APGC, TagTheme, CSS, architecture, and component documents are historical contracts for pinned older adopters. Their original content remains intact. New work uses the integrated 0.2 specification; port useful legacy rules deliberately rather than inheriting conflicting website assumptions.

## Palette migration

All 49 named entries from the v0.1.1 embedded background/text/semantic palette retain their exact hex values. They now have verified equivalent OKLCH coordinates in TOML. Ten additional named scale stops serve ordered data encodings. Semantic `danger` selects the existing `#FB7185` risk color for readable text across the four supported dark surfaces; `#F43F5E` remains unchanged in the palette. No old CSS consumer namespace is silently replaced: new adapters use `--ni-*`. The generated representation table records every color.

## Deprecation and preservation

The entire `manga/` tree, including images and JSON sidecars, is deprecated and excluded from active examples, skill guidance and future visual identity. No files are deleted or moved. Old `assets/` screenshots, logos, mockups, mindmaps and infographics remain historical website evidence; none establish current token values. `Docs/pdf` and `Docs/pptx` are archived document exports, not current specifications. `schema.jsonld` remains legacy descriptive metadata, not a validator or adopter schema.

Pre-change entry points are byte-preserved under `references/history/2026-09-27-pre-v0.2/`. Directory names and dated historical paths stay intact. Empty `HTML/` and `public/` directories and editor configuration do not become active examples by proximity.

## Adopter procedure and recovery

Pin the previous version, record imports and output artifacts, then scope a pilot report. Adopt new semantic aliases and approved chart scales; preserve the host shell. Compare real output, keyboard behavior, exports and source notes. Record deviations and evidence using the adoption template. To recover, restore the previous pinned consumer assets and configuration; historical suite files alone are not a substitute for an adopter backup.

No existing application was rethemed, no website was deployed, and no prior adopter was automatically migrated by this suite revision.
