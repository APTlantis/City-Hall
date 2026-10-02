# PPS To WGS Lifecycle Mapping

## Purpose

This note maps PPS proposal readiness to WGS lifecycle states.
It is the handoff rule between project intent and workspace registration.

## Mapping

| PPS readiness | WGS lifecycle | Meaning |
| --- | --- | --- |
| `sketch` | `concept` | Idea exists, but broad implementation should not begin. |
| `draft` | `planning` | Required sections exist, but risks, standards, or boundaries still need review. |
| `ready` | `active` | Proposal boundary is clear enough for implementation under the chosen delivery standard. |
| `rework` | `paused` or `planning` | Existing project has drifted; broad work pauses until intent is refreshed. |

## Transition Rules

- A project may move from WGS `concept` to `planning` when a PPS proposal skeleton exists.
- A project may move from WGS `planning` to `active` only when PPS readiness is `ready`.
- A project in `active` should move back to `planning` or `paused` when the proposal no longer matches reality.
- A project may stay `archived` when PPS is used only to preserve historical intent.

## Registration Rule

The project manifest should record:

- PPS proposal path;
- WGS lifecycle state;
- delivery standard;
- known proposal gaps;
- agent read-first notes.

WGS owns the final workspace placement and registration.
PPS owns the clarity of the project intent before that placement becomes active implementation work.
