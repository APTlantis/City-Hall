# Aptlantis Analysis Standard (AAS)

![Standard](https://img.shields.io/badge/analysis%20standard-AAS%20v0.2-blue)
![Manifest](https://img.shields.io/badge/manifest-TOML-orange)
![Evidence](https://img.shields.io/badge/evidence-run%20records-green)
![Evaluation](https://img.shields.io/badge/evaluation-local%20pipeline-purple)
![Status](https://img.shields.io/badge/status-candidate-lightgrey)

AAS governs local evaluation pipelines, credibility records, run evidence, metric definitions, interpretation boundaries, and analysis outputs.

## Document Suite

| File | Purpose |
| --- | --- |
| `Aptlantis Analysis Standard.md` | Primary AAS specification. |
| `AAS.manifest.toml` | Standard manifest. |
| `templates/Evaluation-Run-Record.md` | Evaluation run template. |
| `templates/Analysis-Manifest.toml` | Analysis manifest template. |
| `Adoption-Guide.md` | AAS adoption procedure. |
| `Validation-Checklist.md` | Evaluation readiness checklist. |
| `CHANGELOG.md` | AAS version history. |

## SFDS Suite Model

`AAS.manifest.toml` describes AAS as a standard suite.
The templates in `templates/` describe analysis manifests and evaluation run records governed by AAS.

## Core Rule

An analysis result is not decision-ready until inputs, tools, environment, metrics, outputs, limitations, and interpretation boundaries are recorded.
