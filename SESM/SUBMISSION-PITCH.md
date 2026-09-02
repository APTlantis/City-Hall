# SESM Submission Pitch

## Short Pitch

SESM is a non-executable semantic SVG metadata profile. It embeds a small JSON metadata block inside the existing SVG `<metadata>` element so standalone SVG assets can carry public, asset-level identity, provenance, interpretation, crawler, archive, theme, and integrity context.

SESM does not make arbitrary SVG safe. SESM-safe SVG means non-executable SVG plus a valid SESM metadata block.

## Suggested Outreach Framing

Use this framing for external review:

> I am looking for review on SESM, a candidate safe profile for embedding non-executable semantic metadata in SVG assets. It includes an explainer, safe profile, threat model, privacy considerations, validator rules, reference implementation, and fixture corpus. The main review questions are whether the metadata model is useful, whether the safety boundary is clear, and whether the validator behavior is practical for crawlers, archives, design systems, and AI-adjacent tooling.

Avoid opening with:

> Please adopt my standard.

Start with review, not adoption.

## Review Audiences

Potential review audiences:

- WICG for lightweight web-platform incubation discussion.
- W3C SVG or related groups if the proposal becomes SVG-ecosystem relevant.
- W3C TAG-adjacent reviewers if broader web architecture questions emerge.
- Google Search or structured data reviewers for asset-level indexing use cases.
- Chrome or browser security reviewers only where SVG safety behavior is implicated.
- Internet Archive, library, and preservation communities for long-term asset context.
- Design-system and developer-tooling communities for generated SVG asset workflows.

## What Reviewers Should Read First

1. `EXPLAINER.md`
2. `SAFE-PROFILE.md`
3. `THREAT-MODEL.md`
4. `PRIVACY.md`
5. `CONFORMANCE.md`
6. `VALIDATOR-RULES.md`
7. `REFERENCE-IMPLEMENTATION.md`

## Questions To Ask Reviewers

- Is the asset-level metadata use case clear and distinct from JSON-LD?
- Is the relationship between embedded metadata and sidecar files clear?
- Is the SESM safe profile strict enough for broad ingestion?
- Are privacy risks and covert tracking risks sufficiently addressed?
- Is `llm.interpretation_hints` clearly non-authoritative?
- Are the validator labels and exit codes practical?
- What fields should be removed, renamed, or constrained before wider review?

## Non-Claims

Do not claim that SESM:

- is a browser feature;
- changes SVG rendering;
- makes arbitrary SVG safe;
- grants crawler permission;
- grants AI training permission;
- replaces JSON-LD;
- replaces sidecar files;
- replaces SVG sanitization;
- has been adopted by a standards body.

## Success Criteria For First Review

The first successful external review should produce:

- safety feedback;
- privacy feedback;
- vocabulary feedback;
- validator feedback;
- suggested venues for continued incubation;
- at least one independent implementation or validator review path.
