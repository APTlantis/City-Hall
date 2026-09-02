# Proposal To Delivery Handoff Example

## Purpose

This example shows a PPS proposal progressing from initial intent to delivery-standard execution.

## Project

- Name: Manifest Audit
- Type: CLI tool
- Proposal standard: PPS
- Workspace standard: WGS
- Delivery standard: CTS

## Step 1: Sketch

The operator records a project spark:

```text
Need a small command that checks standard manifests for missing suite artifacts.
```

PPS state: `sketch`
WGS lifecycle: `concept`

## Step 2: Draft

The proposal adds problem statement, mission, design boundaries, success and failure criteria, and likely delivery standard.

PPS state: `draft`
WGS lifecycle: `planning`

## Step 3: Ready

The proposal becomes ready when output behavior is scoped, destructive behavior is declared not applicable, exit-code expectations are known, and the first roadmap phase is limited to manifest inspection.

PPS state: `ready`
WGS lifecycle: `active`

## Step 4: Delivery Standard Handoff

CTS takes over execution details:

- command contract;
- help output;
- stdout/stderr behavior;
- JSON envelope;
- exit-code table;
- release checklist.

PPS remains the north-star document.
CTS governs the command behavior.
WGS records project placement and lifecycle.
