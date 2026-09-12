# Aptlantis Analysis Standard

## Status

Candidate v0.2.1.

AAS governs analysis and evaluation work that must be credible, reproducible, interpretable, and recoverable.

## Scope

AAS governs local evaluation pipelines, analysis manifests, run records, input references, tool and environment records, metric definitions, outputs, comparisons, limitations, interpretation notes, and credibility checks.

## Does Not Govern

AAS does not govern dataset licensing, model training recipes, agent task handoffs, website deployment, or workspace placement.
Those responsibilities belong to DDS, project-specific training plans, ATS, WDS, and WGS.

## Core Philosophy

An analysis result is not credible because it produced a number.
It is credible when another maintainer can identify the inputs, tools, assumptions, metrics, limitations, and interpretation boundary.

## Relationship to DDS

DDS governs dataset provenance, licensing, splits, validation, and usage constraints.
AAS consumes DDS-governed datasets and records how they were used in an analysis or evaluation run.

An AAS run must not hide DDS uncertainty.
If dataset provenance, license, split, or validation status is incomplete, the analysis must record that limitation.

## Relationship to ATS and WGS

ATS records agent task history and handoff.
AAS records analysis evidence and interpretation.
WGS registers the project, workspace location, lifecycle state, and governing standards.

When an agent performs analysis, use ATS for task replayability and AAS for analytical credibility.

## Required Analysis Artifacts

- Analysis manifest.
- Evaluation run record.
- Input dataset references.
- Tool and version references.
- Environment record.
- Command or procedure record.
- Metric definitions.
- Outputs and result locations.
- Comparison baseline when applicable.
- Limitations and interpretation notes.
- Follow-up questions or recommended next checks.

## Analysis Manifest

The analysis manifest is the machine-readable record of the analysis setup.

It should identify:

- Analysis id and title.
- Purpose.
- Owner or maintainer.
- Inputs.
- Tools.
- Environment.
- Metrics.
- Output paths.
- Governing standards.
- Known limitations.
- Agent read-first notes.

## Evaluation Run Record

The run record is the evidence that a specific evaluation happened.

It should include:

- Date and time.
- Runner or operator.
- Command or procedure.
- Input versions.
- Tool versions.
- Environment details.
- Raw outputs or output locations.
- Metric values.
- Warnings, failures, or skipped checks.
- Interpretation summary.

## Metric Rules

Every reported metric must define:

- Name.
- Unit.
- Calculation method.
- Denominator or population.
- Time window, if applicable.
- Exclusions.
- Known caveats.

Metrics without definitions are not analysis evidence.
They are notes.

## Comparison Rules

When an analysis compares results, it must identify:

- Baseline.
- Candidate or changed condition.
- Difference being tested.
- Expected direction, if known.
- Whether the comparison is descriptive or decision-grade.

Do not present exploratory comparisons as proof.

## Interpretation Boundary

Every AAS result must say what the result does and does not support.

Interpretation notes should distinguish:

- Observed facts.
- Inferences.
- Assumptions.
- Limitations.
- Recommended next checks.

If the analysis cannot support a decision, say so directly.

## Readiness Levels

| Level | Meaning |
| --- | --- |
| `draft` | Inputs or procedures are still incomplete. |
| `reproducible` | Inputs, commands, tools, and outputs are recorded enough to rerun. |
| `interpretable` | Metrics, assumptions, limitations, and interpretation boundary are documented. |
| `decision-ready` | Evidence is sufficient for the stated decision and caveats are explicit. |
| `archived` | Run is preserved for historical reference and not expected to be updated. |

## Credibility Checks

An AAS analysis should check:

- Inputs exist and are identifiable.
- Dataset constraints are known.
- Tool versions are recorded.
- Metrics are defined.
- Outputs are preserved.
- Limitations are explicit.
- Interpretation does not exceed evidence.
- Comparison baselines are named.

## Release Blockers

An analysis is blocked from decision-ready status when:

- Inputs cannot be identified.
- Tool or environment details are missing.
- Metric definitions are absent.
- Outputs are not preserved.
- Dataset limitations are unknown or hidden.
- Interpretation overclaims the evidence.
- Comparison baselines are missing.

## Example

Use `templates/Analysis-Manifest.toml` for the setup record and `templates/Evaluation-Run-Record.md` for the run evidence.
