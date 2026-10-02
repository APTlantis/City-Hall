# Dataset Split Record

## Dataset

- Name: Standards Health Dataset
- Version: `2026.06.11`
- Class: evaluation dataset

## Split Purpose

- Training: not applicable
- Validation: compare audit behavior across candidate standards
- Test: verify audit behavior against reference DRS and stable SFDS
- Holdout: reserved future standards normalization snapshots

## Split Method

- Method: deterministic grouping by standard maturity and artifact category
- Seed: not applicable
- Stratification: maturity state and standard family
- Leakage controls: generated health records are not used to define the pass criteria they are tested against

## Counts

| Split | Rows | Files | Notes |
| --- | ---: | ---: | --- |
| train | 0 | 0 | Not used. |
| validation | 84 | 1 | Candidate standard artifact checks. |
| test | 14 | 1 | SFDS and DRS reference checks. |
| holdout | 0 | 0 | Reserved for future snapshots. |

## Validation

- Checked by: City Hall maintainer
- Checked on: `2026-06-11`
- Result: partial
- Known limits: Example counts demonstrate record shape and are not a committed production dataset snapshot.
