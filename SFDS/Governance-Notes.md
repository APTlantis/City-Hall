# SFDS Governance Notes

## Purpose

These notes record policy clarifications for maintaining SFDS-governed standard suites.
They preserve decisions that affect how standards are normalized, validated, and promoted without changing the primary specification each time a maintenance rule is clarified.

## Decision Notes

### Suite Manifest Is Not an Adopter Manifest

`[StandardName].manifest.toml` describes the standard suite itself.
Domain-specific adopter manifests, schemas, or templates must live beside the suite manifest and be registered under `adopter_artifacts`.

This preserves the two-layer model and prevents tools from mistaking a standard for a project that adopts it.

### Validators May Be Manual Guidance Before They Are Executable Tools

SFDS treats validation guidance as valid validation support when compliance requires reviewer judgment.
Executable validators are preferred when checks are mechanical, but standards may register manual procedures when maturity, compatibility, scope, or governance boundaries require human review.

### Mature Existing Standards Should Be Wrapped, Not Rewritten

Standards that predate SFDS may already contain useful domain authority.
Normalization should add suite structure, manifests, examples, validation separation, and governance notes while preserving proven domain rules.

### Stable Means No Known Stability Blockers

Stable does not mean no future improvements remain.
A stable standard may still have optional validator automation, examples, or schema tightening planned, provided it has no unresolved blocker against its current conformance level.

### Reference Examples Should Be Concrete

Reference examples should point to filled artifacts or real suite patterns.
They should not be purely aspirational examples unless explicitly labeled as candidate or illustrative.

## Policy Use

Use these notes when:

- Reviewing whether a standard can claim candidate, stable, or reference maturity.
- Deciding whether a validator must be executable or may remain manual.
- Normalizing an older standard without erasing its existing authority.
- Resolving confusion between suite artifacts and adopter-facing artifacts.
