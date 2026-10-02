# Agent Task Standard

## Status

Candidate v0.2.1.

ATS governs agent work as a recoverable record.
It makes agent tasks auditable, resumable, handoff-ready, and replayable enough that another human or agent can understand what happened without reconstructing the whole session from memory.

## Scope

ATS governs agent task recording, lifecycle states, context capture, action summaries, files inspected or changed, validation evidence, blockers, handoff notes, and replayability.

ATS applies when agent work is substantial, crosses files or standards, changes governed records, or may need to be resumed later.

## Does Not Govern

ATS does not govern workspace root placement, project proposal content, release packaging, command output contracts, or analysis metric definitions.
Those belong to WGS, PPS, DRS, CTS, and AAS.

## Relationship to WGS

WGS defines how an agent orients in the workspace.
ATS defines how the agent records the task after orientation.

An ATS task record should name the WGS entry points that were read, including the workspace manifest, nearest directory manifest, project manifest, and governing standard when applicable.

## Relationship to PPS and AAS

PPS supplies the project intent boundary when agent work changes project scope.
AAS supplies evaluation and analysis evidence when the agent performs measured analysis.
ATS records the task history, handoff state, and validation summary that make the work resumable.

## Required Task Artifacts

- Task record.
- Starting context.
- Goal and success criteria.
- Governing standard.
- Actions taken.
- Files inspected or changed.
- Decisions made.
- Validation performed.
- Known gaps or blockers.
- Handoff note when work remains.

## Task Lifecycle States

| State | Meaning |
| --- | --- |
| `planned` | Goal and context are recorded, but work has not started. |
| `active` | Work is underway. |
| `validating` | Changes are complete enough to verify. |
| `handoff` | Work cannot finish in the current session and needs transfer context. |
| `blocked` | Work cannot safely proceed without missing input, access, or a decision. |
| `complete` | Goal is satisfied and validation is recorded. |
| `superseded` | Task was replaced by a newer task or different plan. |

Every substantial agent task should have exactly one current state.

## Starting Context

Starting context records what the agent knew before changing anything.

It should include:

- User request.
- Workspace path.
- Relevant manifests.
- Governing standards.
- Files or references read first.
- Known dirty worktree state, if relevant.
- Assumptions and constraints.

Starting context prevents a later maintainer from confusing discovered facts with post-hoc explanation.

## Action Record

The action record should summarize work at the level another agent needs to resume safely.

It should include:

- Files inspected.
- Files changed.
- Tools or commands run.
- Important outputs.
- Decisions made.
- Alternatives rejected when the reason matters.
- User instructions that changed the task.

The action record is not a transcript.
It is a high-signal operational history.

## Validation Record

Validation must say what was checked and what the result was.

Examples:

- Manifest files parsed successfully.
- Changelog version matches manifest version.
- Tests passed.
- `git diff --check` passed.
- Browser or visual checks were performed.
- Validation could not be run and why.

A task is not complete if validation is absent and the reason is not recorded.

## Handoff Note

A handoff note is required when:

- Work remains.
- A blocker exists.
- A decision is pending.
- Validation failed.
- The next agent must preserve a fragile assumption.
- The worktree contains relevant unstaged changes.

The handoff note must include:

- Current state.
- What was completed.
- What remains.
- Known blockers.
- Files most likely to matter next.
- Next safe action.

## Replayability

An ATS record is replayable when another agent can answer:

- What was the goal?
- What context was read first?
- What changed?
- Why did it change?
- How was it validated?
- What remains unsafe or incomplete?

Replayability does not require full command transcripts.
It requires enough structured context to avoid repeating discovery work or accidentally undoing intentional changes.

## Agent Drift Controls

Agents must not use a task record to broaden scope silently.

When work starts drifting, the task record should identify whether the next safe action is:

- Continue under the existing goal.
- Update the PPS proposal.
- Consult a governing standard.
- Ask for a human decision.
- Create a follow-up task.

## Completion Criteria

An agent task is complete when:

- The requested goal is satisfied.
- Relevant files and decisions are recorded.
- Validation is recorded.
- Remaining risks or gaps are stated.
- No required handoff is missing.

## Example

Use `templates/Agent-Task-Record.md` for the task record and `templates/Handoff-Note.md` when work remains.
