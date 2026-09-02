# SFDS Validation Guidance

## Purpose

This guidance defines the manual validation procedure for SFDS-governed standard suites.
It is registered as SFDS validation support because SFDS compliance is currently checked by document review and suite-shape inspection rather than by a dedicated executable validator.

## Validation Boundary

SFDS validation checks the standard suite.
It does not prove that an adopter project satisfies the domain rules of that standard.

For example:

- SFDS can check that WDS has a README, specification, manifest, adoption guide, validation checklist, changelog, templates, and examples.
- WDS itself must check whether a website has valid routes, metadata, deployment evidence, and accessibility review.

## Manual Validation Procedure

1. Confirm the suite entrypoint.
   - `README.md` exists.
   - The README states the standard's City Hall role.
   - The README identifies the primary specification.
   - The README separates suite-governance artifacts from adopter-facing artifacts.

2. Confirm the primary specification.
   - The specification exists at the path declared in `[artifacts].specification`.
   - Scope and non-goals are explicit.
   - Validation expectations are documented.
   - Compatibility and versioning policy are documented.
   - WGS and adjacent-standard relationships are stated when relevant.

3. Confirm the suite manifest.
   - `[StandardName].manifest.toml` exists.
   - The manifest describes the standard suite, not an adopter project.
   - The manifest declares required suite artifacts.
   - Declared artifacts resolve to existing files or directories.
   - Adopter schemas and templates are listed under `adopter_artifacts`, not confused with the suite manifest.

4. Confirm required suite artifacts.
   - `Adoption-Guide.md` exists.
   - `Validation-Checklist.md` exists.
   - `CHANGELOG.md` exists.
   - Templates, schemas, examples, validators, and governance notes are present or explicitly deferred.

5. Confirm evidence for maturity.
   - Draft standards have clear scope and enough structure for review.
   - Candidate standards have templates or examples that let an adopter test the standard.
   - Stable standards have no unresolved stability blockers.
   - Reference standards have real examples, validation evidence, or known adopters.

6. Confirm preservation and compatibility.
   - Version changes are reflected in the changelog.
   - Deprecated artifacts remain discoverable or have migration notes.
   - Existing mature domain rules were not rewritten merely to normalize suite shape.

## Suggested Local Checks

Use these as supporting evidence during manual review:

```powershell
python SFDS/tools/sfds_validate.py SFDS WGS DRS CTS WDS PPS SESM AAMHS LDS --json
python WGS/tools/city_hall_audit.py --root D:/.city_hall
python WGS/tools/city_hall_audit.py --root D:/.city_hall --format jsonl
```

The SFDS validator confirms required suite shape, manifest vocabulary, and registered artifact paths.
The WGS audit can confirm broader City Hall file presence and manifest references.
Neither executable check replaces SFDS reviewer judgment about scope clarity, compatibility policy, adopter usability, or maturity evidence.

## Pass Criteria

An SFDS-governed standard suite passes manual validation when:

- Required suite artifacts exist and are discoverable.
- The suite manifest accurately registers those artifacts.
- The standard distinguishes suite validation from domain validation.
- Maturity claims are supported by examples, validators, adopter evidence, or explicit deferrals.
- No stability blocker from the SFDS primary specification remains unresolved.

## Failure Criteria

A standard suite fails SFDS validation when:

- The primary specification is missing or not authoritative.
- Required artifacts are missing without explicit deferral.
- The suite manifest describes an adopter project instead of the standard suite.
- Suite validation and domain validation are blurred.
- Compatibility or versioning expectations are absent for a stable or reference standard.
- Declared artifacts do not resolve.
