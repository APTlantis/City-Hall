# Evaluation Run Record

## Purpose

Evaluate whether a candidate standards-health audit detects required documentation artifacts across the City Hall standard suite.

## Inputs

- Workspace root: `D:\010-CITY-HALL`
- Standard directories: top-level directories with matching `{DirectoryName}.manifest.toml`
- Required artifacts: README, primary specification, manifest, adoption guide, validation checklist, changelog, examples directory

## Tools and Versions

- Tool: `WGS/tools/city_hall_audit.py`
- Runtime: Python 3 with standard-library TOML parsing
- Governing standards: AAS, WGS, SFDS

## Command / Procedure

```powershell
python WGS/tools/city_hall_audit.py --root D:\010-CITY-HALL
```

## Metrics

- Standards inspected: 14
- Required artifact categories per standard: 7
- Pass count: recorded by audit output
- Warning count: recorded by audit output
- Fail count: recorded by audit output

## Outputs

- Console audit report
- Optional generated health record under `WGS/examples/`
- Follow-up tasks captured under ATS when gaps are found

## Interpretation

The audit is a suite-health check. A passing result means the standard directories satisfy the expected SFDS/WGS documentation scaffold. It does not prove that every standard is mature, stable, or semantically complete.

## Limitations

- The audit checks artifact presence and manifest/changelog consistency, not prose quality.
- Link checking is limited to manifest-declared artifacts unless expanded.
- Template and schema quality still require human review.
