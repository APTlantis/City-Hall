# Dataset Development Standard

## Status

Candidate v0.2.1.

## Scope

DDS governs datasets, training corpora, metadata, provenance, licensing, validation, splits, hashes, storage notes, and usage constraints.

## Does Not Govern

DDS does not govern model training procedure, website deployment, desktop releases, or workspace root policy.

## Required Dataset Artifacts

- Dataset manifest.
- Provenance record.
- License record.
- Validation record.
- Split description when applicable.
- Integrity hashes when preserving or releasing.
- Usage notes and known limitations.
- Data dictionary or schema notes when fields are structured.
- Review or refresh note for living datasets.

## Relationship to PPS and WGS

PPS defines why the dataset exists, who needs it, what success means, and what use cases are out of scope.
WGS registers the dataset project, lifecycle state, workspace placement, and relationships.
DDS governs source provenance, licensing, transformations, validation, splits, integrity, limitations, and release readiness.

## Provenance Requirements

Every dataset must say where it came from, how it changed, and what may be done with it.

Minimum provenance record:

- Source names and locations.
- Collection date or date range.
- Collection method.
- Transformation steps.
- Removed or filtered records.
- License and usage constraints.
- Validation method and result.
- Known limitations.
- Maintainer and review date.

Provenance must be specific enough that a future maintainer can distinguish original source data from transformed, filtered, generated, or manually corrected data.

## Dataset Readiness Levels

| Level | Meaning |
| --- | --- |
| `raw` | Sources are captured but not cleaned or validated. |
| `working` | Transformations are in progress and validation is incomplete. |
| `candidate` | Manifest, provenance, license, validation, and limitations are recorded. |
| `released` | Integrity hashes and release location are recorded. |
| `archived` | Dataset is preserved for reference and no longer actively updated. |

## Dataset Classes

| Class | Meaning |
| --- | --- |
| `source-capture` | Raw collected source material. |
| `working-corpus` | In-progress cleaned or transformed corpus. |
| `training-corpus` | Dataset intended for model training or fine-tuning. |
| `evaluation-set` | Dataset intended for benchmark or evaluation use. |
| `reference-archive` | Preserved dataset used for recovery, reproducibility, or historical reference. |
| `derived-dataset` | Dataset produced from one or more prior datasets. |

Dataset manifests should identify the closest class.
Derived datasets must link to source datasets or provenance records.

## Validation Rules

- Validation must describe the checks performed, not only say "passed".
- Any split must record method, seed if applicable, and counts.
- Any preserved or released artifact must have an integrity hash.
- License uncertainty is a blocker for public release.
- Known limitations must be written for future users, not just current maintainers.
- Field-level schemas or data dictionaries are required when consumers depend on column or key meanings.
- Generated data must be labeled as generated and must record the generation method.
- Personally identifiable, sensitive, restricted, or licensed data must record handling constraints.

## Split Rules

Splits must record:

- Split names.
- Counts.
- Method.
- Seed, if randomization was used.
- Stratification or grouping rules, if any.
- Leakage risks.

Evaluation sets must be protected from accidental training use.

## Integrity and Preservation

Released or archived datasets must record integrity hashes for preserved artifacts.

Use the workspace integrity standard that fits the release context:

- AAMHS for archive integrity records.
- ARHS for release artifact hash requirements.
- DDS provenance records for dataset-specific source and transformation evidence.

## Release Blockers

A DDS-governed dataset is blocked from release when:

- Source provenance is missing.
- License or usage rights are unknown.
- Validation procedure is missing or only says "passed".
- Known limitations are absent.
- Splits are undocumented when consumers depend on them.
- Released artifacts lack integrity hashes.
- Sensitive or restricted data handling constraints are unknown.
- Derived data cannot be traced back to sources.
