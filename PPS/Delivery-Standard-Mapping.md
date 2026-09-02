# PPS Delivery Standard Mapping

## Purpose

PPS defines project intent before implementation.
This mapping helps decide which delivery standard owns the next execution contract after a proposal is approved.

| Project shape | Delivery standard | Handoff expectation |
| --- | --- | --- |
| Desktop application | DRS | Release manifest, release note, checklist, artifact hashes, trust/security notes as needed. |
| Command-line tool | CTS | Command contract, human/machine output examples, exit-code table, JSON envelope. |
| Service or infrastructure process | SIS | Service contract, runtime/deployment expectations, health checks, operations notes. |
| Website or hosted UI | WDS | Site manifest, routes, metadata, accessibility, deployment record, publication approval. |
| Dataset or data snapshot | DDS | Dataset manifest, provenance, license, integrity, distribution evidence. |
| Library or SDK | LDS | Library interface note, semver policy, adopter examples, compatibility evidence. |

When a project has multiple surfaces, split the handoff by deliverable.
For example, a core library can use LDS while its companion CLI uses CTS.
