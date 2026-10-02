# Standards Backlog

## Purpose

This backlog orders standards work so the workspace can become self-describing in layers.
The priority is to normalize existing strong patterns first, then draft missing standards, then automate compliance.
Detailed follow-up from the 2026-07-30 standards evaluation is tracked in `Standards-Evaluation-Backlog.md`; this file remains the high-level standards roadmap.

## Active Standards

| Standard | Purpose | Scope | Required docs | Next action |
| --- | --- | --- | --- | --- |
| WGS | Workspace Governance Standard | Drive layout, project registration, manifests, workspace services, lifecycle visibility, agent startup | Spec, directory map, manifest conventions, agent startup, workspace health model | Define agent closeout procedure plus workspace audit/dashboard data from manifest truth. |
| SFDS | Standards Framework Development Standard | Creation, maturity, validation, and preservation of standards | Spec, maturity levels, entity-named standard manifests, templates, examples, validator notes, changelog | Register SFDS validation guidance and governance notes before deeper suite validators. |
| PPS | Project Proposal Standard | Project creation before code boundaries | Proposal template, success criteria, failure criteria, constraints, roadmap, project manifest | Add filled examples for desktop, website, dataset, and standard projects. |
| DRS | Desktop Release Standard | Desktop app releases and release evidence | Spec, manifest schema, templates, examples, release checker | Treat as the reference implementation pattern for validators and examples. |
| CTS | Command Tool Standard | CLI tools and automation utilities | Spec, command contract, exit codes, output schemas, templates, validation checklist | Add JSON schema conventions for machine-readable command output. |
| WDS | Website Development Standard | Websites and web applications | Spec, site manifest, accessibility/SEO checklist, deployment record, monitoring expectations | Add accessibility and metadata checklist examples. |
| DDS | Dataset Development Standard | Datasets, corpora, provenance, licensing, validation | Spec, dataset manifest, provenance template, validation record, license checklist | Add license record and split record examples. |
| ATS | Agent Task Standard | Agent workflows, task recording, handoff, validation, replayability | Spec, task record, handoff template, validation record, lifecycle states | Add filled task and handoff examples. |
| AAS | Aptlantis Analysis Standard | Local evaluation pipeline and credibility records | Spec, evaluation manifests, run records, examples, validator notes | Add filled evaluation run examples and metric-definition examples. |
| ARHS | APTlantis Release Hashing Standard | Minimum release-artifact hashes | Spec, validation checklist, sample hashes | Add release hash record template and examples. |
| AAMHS | Aptlantis Archive Multi-Hash Standard | Archive verification, hash suites, detached signatures, validation records | Spec, hash manifest, integrity record, examples, verifier notes | Refine hash manifest schema and add concrete hash examples before validator automation. |
| AADR | Application / architecture data representation | Emerging application-as-data framework | Spec, representation record, examples, adoption notes, changelog | Add filled representation examples and consumer/tool notes. |
| SESM | SVG Embedded Semantic Metadata | SVG metadata, embedded semantics, validation | Spec, schema, examples, converter/validator notes, tests | Keep schema, tools, tests, and NeonInk references aligned. |
| NeonInk | Semantic design language | Color semantics, visual intent, themes, UI language | Spec, palette contracts, component patterns, examples, assets, changelog | Deepen contract classification without flattening existing docs/assets. |

## Later

| Area | Purpose | Next action |
| --- | --- | --- |
| SIS | Service and Infrastructure Standard | Shared caches, local model services, Docker, indexing, search, local APIs, schedulers, and workspace infrastructure | Initial standard added; apply to service roots and deepen validator support. |
| Workspace audits | Detect missing manifests, stale docs, broken standard links | Build WGS auditor requirements after manifest conventions stabilize. |
| Dashboards | Show project coverage, standard coverage, status, risks | Define minimum dashboard data model after workspace manifest is authoritative. |
| Validators | Make standards executable | Build validators per standard after schemas are stable. |
| Relationship maps | Show project dependencies and governing standards | Generate from manifests once coverage improves. |

## Standards Roadmap

1. Stabilize WGS as the workspace constitution.
2. Stabilize PPS so new work starts with clear design boundaries.
3. Stabilize SFDS so every standard has a consistent maturity path.
4. Keep DRS as the reference implementation.
5. Deepen examples and validators for CTS, SIS, WDS, DDS, ATS, AAS, ARHS, AAMHS, and AADR.
6. Keep SESM and NeonInk aligned through schema/tool/reference checks.
7. Build workspace audits and dashboards from manifest truth.

## Normalization Pass - 2026-06-10

Status: complete for documentation-suite scaffolding and SFDS two-layer suite metadata.

Completed:

- SFDS suite created as the reusable standard-suite pattern.
- WGS formal standard wrapper added.
- PPS normalized around proposal and project manifest artifacts.
- DRS registered under WGS/SFDS without rewriting its mature release docs.
- NeonInk registered under WGS/SFDS with a governance index for existing docs and assets.
- CTS, SIS, WDS, DDS, ATS, and AAS draft suites created.
- AAMHS, AADR, and SESM normalization wrappers created.
- SFDS two-layer suite model applied across WGS, PPS, DRS, CTS, SIS, WDS, DDS, ATS, AAS, AAMHS, AADR, SESM, and NeonInk.
- Suite map or reference examples added under each standard's `examples/` directory.
- README, adoption, and validation language aligned so suite conformance is distinct from domain readiness.

First deepening pass completed:

- WGS workspace health.
- PPS proposal readiness and first filled example.
- CTS command contracts.
- WDS deployment records.
- DDS provenance rules.

Next action:

- Continue with additional PPS examples, CTS JSON schema conventions, WDS accessibility/metadata examples, DDS license/split records, ATS/AAS filled examples, ARHS hash record templates, AAMHS archive validation examples, and a validator for v2.4 entity manifests.

## Structure Rollout - 2026-06-10

Status: complete for target roots, entity-named directory manifests, bounded project manifests, and v2.4 manifest model adaptation.

Completed:

- Created target roots for Library, Zoning, Evals, and Data.
- Renamed legacy root manifests to canonical manifest names.
- Added entity-named manifests to governed roots and service/category directories.
- Added entity-named project manifests to bounded project roots.
- Updated the default manifest model from v2.3 project-only to v2.4 entity-aware.
- Categorized DRS, CTS, WDS, and DATA child roots into numbered groups.
- Added manifests for top-level service/cache roots.
