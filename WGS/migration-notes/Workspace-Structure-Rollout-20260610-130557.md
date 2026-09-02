# Workspace Structure Rollout 20260610-130557

## Summary

Implemented manifest-first workspace structure rollout for top-level governed roots, canonical manifest names, safest root renames, DPW service manifests, and project manifests under project-class roots.

## Root Moves

| Source | Target | Result | Reason |
| --- | --- | --- | --- |
| `D:\LIBRARY` | `D:\020-LIBRARY` | moved | Normalize document nexus root numbering. |
| `D:\980-EVALS` | `D:\970-EVALS` | moved | Normalize evaluation root numbering. |
| `D:\970-DATA` | `D:\980-DATA` | moved | Normalize data root numbering. |
| missing | `D:\030-ZONING` | created | Initial project scaffolding area. |

## Legacy Manifest Renames

| Source | Target | Result | Meaning |
| --- | --- | --- | --- |
| `D:\010-CITY-HALL\00-RULES.manifest.toml` | `D:\010-CITY-HALL\DIRECTORY.manifest.toml` | renamed | City Hall root directory manifest. |
| `D:\100-DRS\100-DRS.manifest.toml` | `D:\100-DRS\DIRECTORY.manifest.toml` | renamed | DRS class root directory manifest. |
| `D:\020-LIBRARY\DocHub.manifest.toml` | `D:\020-LIBRARY\DocHub.manifest.toml` | entity-renamed | DocHub project manifest preserved after Library migration; the old generic duplicate was archived separately. |

## DRS Project Categorization

| Source | Target | Result | Reason |
| --- | --- | --- | --- |
| `D:\100-DRS\Aegis` | `D:\100-DRS\110-CRYPTO\Aegis` | moved | Known crypto/security desktop project. |
| `D:\100-DRS\FileCabinet` | `D:\100-DRS\120-STORAGE\FileCabinet` | moved | Known storage desktop project. |

## Safety Classification

- Root moves were performed only when the target path did not already exist.
- Legacy manifests were renamed only when the canonical target manifest did not already exist.
- Cache/service roots under `.ollama` and `.hf` were not moved; DPW cache locations were documented separately.
- Generated project manifests include known gaps requiring project-specific review.
