# City Hall framework remediation â€” 2026-10-02

## Result and scope

Implemented verified canonical fixes from the supplied gap analysis. No candidate suite was promoted. SFDS and DRS now use 2.0.0 because prospective promotion requirements and release-readiness requirements changed; the existing stable/reference maturity labels are retained as historical decisions, not newly certified production adoption. Other suite versions remain unchanged for additive maintenance tools and documentation.

The original analysis mixed current facts, deliberately incomplete teaching examples, and hypothetical failures. This review inspected physical source and ran checks. It does not establish ecosystem-wide compliance, new shipping releases, live public deployment, or completed model evaluations.

## Implemented changes

| Requested action | Result and evidence boundary |
| --- | --- |
| Formal promotion gate | [SFDS gate](../../SFDS/Promotion-Gate.md), template and checker require two distinct non-teaching production adopters, dated schema/runtime logs and named approval. Reviewer must inspect actual contents and independence. Existing suites are not retroactively promoted or recertified. |
| Candidate audit | All 16 suites pass SFDS structural checks. [Observed evaluation](../../AAS/reports/Suite-Evaluation-2026-10-02-Completed.json) records 16/16 and input-manifest hashes. No missing registered artifacts were detected; this does not establish schema semantics or adopter execution. |
| AAS executed evidence | New suite-snapshot evaluator requires a nonzero denominator and records execution/findings, rather than treating a blank teaching record as a run. It refuses to overwrite saved evidence. This is deterministic structural analysis, not execution of external model-backed projects. |
| DRS stage gate | `check-release` invokes the Python evidence gate and fails on pending/missing stages, missing dated logs, changed artifact bytes, unavailable declared BLAKE3 verification, or absent shipping artifact. Stage records bind the installer SHA256. Migration needs pass or a named justified dated waiver. Build/test packaging remains possible before installation tests. |
| WDS automation helper | New deployment gate combines the existing route and HTML smoke tools, using an explicit current route inventory and saving observations. Caller must wire it into the adopter deployment pipeline. Rendered focus/contrast/keyboard tests remain host-specific work. |
| NeonInk authority | Canonical manifest already declares 0.2.0, candidate-active status and candidate maturity. Governance-Index already supersedes Docs. Root review metadata remains correct with maturity `candidate`; candidate-active is status. New canonical catalog reflects current facts. Historical documents are preserved. |
| SESM filename | Renamed the actual root file to `SESM/SESM-v0.3.0.md`, updated active discovery references, and preserved identical original bytes under `SESM/references/history/2026-10-02/SESM-v0.2.md`. Historical changelogs retain their original paths. Metadata 0.2.0 compatibility remains unchanged. |
| Blue Slate legacy tokens | Inspected tools explicitly load canonical TOML or current generated JSON. No silent scanning/fallback defect was found. Frozen v0.3 JSON/CSS remain at documented compatibility paths; moving/deleting would break pinned consumers. Added an explicit review note. Canonical and generated token bytes are unchanged. |
| Safe SVG ingestion | New helper validates and extracts the same byte snapshot, emitting metadata only for status ok/profile sesm-safe. Unsafe vectors and warnings fail closed. The JavaScript regex parser is labeled a teaching extractor, not a safety gate. External pipelines still need to adopt the helper. |
| Scheduled catalog audit | New optional catalog check covers ids, version, status, maturity, manifest path and declared lifecycle/review dates. [Reviewed snapshot](../catalog/city-hall.json) and GitHub workflow template are saved. When activated, weekly failed scheduled runs open at most one matching alert issue. No modification-time equality rule is used. Workflow is staged only by user request; activation and GitHub execution remain pending. |

## Corrections to the supplied analysis

- Candidate maturity does not by itself prove production misuse or permanent stagnation. Fourteen suites remain candidate; individual adoption claims require their own evidence.
- The existing AAS example is a historical teaching record. Its missing execution is not evidence that all analysis projects have zero findings. A valid executed run can observe zero errors; inventing findings would invalidate it.
- `DRS/templates/Integrity-Validation-Matrix.md` is an application-health/repair matrix, not the claimed five-stage execution table. The new release-stage record is separate and machine-readable.
- A specification filename does not select schema validation behavior. SESM already documents current 0.3.0 and compatible historical 0.2.0 metadata.
- Blue Slate has one editable authority plus documented frozen compatibility interfaces. Presence of legacy JSON is not proof of compiler misuse.
- WDS HTML regex smoke checks cannot prove rendered keyboard states or OKLCH contrast. Route counts must come from current adopter inventories rather than assuming the report's 22 is still exhaustive.
- Hash examples demonstrate format; signature and recovery claims need actual archive inputs, keys/trust records and restore observations. Nothing in this maintenance pass supplies them.

## Verification

- SFDS structure: 16 suites pass, no warnings/errors.
- Canonical audit plus reviewed catalog: 17 scopes pass.
- Nine framework regression tests pass, including an actual PowerShell `check-release` failure for incomplete evidence.
- Eight existing SESM safe-profile tests pass; the new ingestion tests also reject script, event-handler, javascript-url and bad-json before emitting metadata.
- Blue Slate and NeonInk compiler freshness checks pass without regeneration.
- Named structural evaluation is executed with manifest hashes and denominator 16. Test logs and audit results are stored in this report directory. Synthetic pass fixtures exercise gate mechanics only; they are not promotion or shipping evidence.

## Remaining work

See [the dated backlog section](../Standards-Evaluation-Backlog.md). External website catalog/public snapshots, adopter deployment hooks, actual UI execution, model-backed evaluation projects, archive recovery/signatures, production promotion reviews and GitHub execution remain separate tasks with explicit evidence requirements.

The external site catalog inspected at `A:\aptlantis.net\public\data\city-hall.json` still declares NeonInk 0.1.6 and lacks maturity fields; it was not modified or deployed here. The workflow checks the canonical reviewed snapshot, not live website freshness. Public synchronization must preserve its curated descriptions and reviewed public-source ownership.

## Recovery and discovery

README, WORKSHOP-MAP, root manifest, relevant suite maps, changelogs, templates and validation guidance were updated. No workspace identities, placements or portfolio registrations changed; `D:\INDEX.md` and `D:\Development.manifest.toml` still resolve these same suites and need no path/identity update. They were inspected but not edited. Existing unrelated `.idea/workspace.xml`, `.gitignore` and Python cache changes were preserved. Git push is authorized separately by the user; deployment, release and external issue creation have not occurred. The user reinitialized Git during this pass and requested branch Cobra; original Git status is not the final status.

The first evaluation observed 15/16: the AAS manifest prematurely registered the not-yet-created run file. Registration now points to the existing reports directory. The failed run remains preserved as `AAS/reports/Suite-Evaluation-2026-10-02.json`; the completed rerun is separate.

The ingestion helper requires the full jsonschema engine and fails closed when unavailable. Regression checks used temporary dependencies for the exact bundled Python 3.12 runtime; package versions are in verification-environment.txt. Install SESM/requirements-ingestion.txt in the adopter runtime. No project Python installation was modified.
