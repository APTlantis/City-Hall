# SESM Conformance

## Normative Keywords

The key words `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, and `MAY` are to be interpreted as described in RFC 2119 and RFC 8174 when, and only when, they appear in all capitals.

## Document Classes

SESM documents use four classes of material:

- Normative requirements define conformance.
- Recommendations describe expected best practice.
- Examples are illustrative and non-normative.
- Implementation notes explain one possible way to satisfy requirements.

If examples conflict with normative requirements, the normative requirements win.

## SESM Metadata Conformance

A SESM metadata block conforms when:

- it is a JSON object;
- it contains `sesm_version`;
- it validates against `svg_asset.schema.json` or a documented compatible profile;
- it does not claim authority beyond asset-level metadata;
- it does not contain credentials, secrets, or private operational data.

Unknown fields MAY be ignored by consumers unless a stricter profile says otherwise.

## SESM-Safe SVG Conformance

An SVG conforms to the SESM safe profile only when:

- it is parseable SVG XML;
- it contains no more than one `<metadata id="sesm">` block;
- its SESM block conforms;
- it contains no `<script>` elements;
- it contains no event handler attributes;
- it contains no `javascript:` URLs;
- it contains no agent command authority;
- it contains no credential requests;
- it contains no hidden payloads intended to evade review.

Schema validation alone is not enough to claim `sesm-safe`.

## Consumer Conformance

A SESM consumer conforms when it:

- parses SESM metadata as data only;
- treats SESM metadata as untrusted input;
- does not execute SESM text;
- does not treat SESM text as agent command authority;
- does not let SESM override user instructions, system policy, or tool safety rules;
- ignores unknown fields unless intentionally supported;
- reports validation errors clearly enough for authors to fix them.

## Validator Conformance

A SESM validator conforms when it implements the required checks in `VALIDATOR-RULES.md`.

A validator claiming safe-profile support MUST distinguish:

- `sesm-valid`
- `sesm-safe`
- `sesm-unsafe`
- `sesm-unverified`

A lightweight adopter harness is documented in `tests/CONFORMANCE-HARNESS.md`.

## Versioning

The public SESM candidate suite version is currently `0.3.0`.

The embedded `sesm_version` field identifies the metadata profile used by an SVG. Existing `0.2.0` metadata remains part of the candidate compatibility history, but new public-review examples SHOULD use `0.3.0` after the `llm.interpretation_hints` vocabulary update.
Compatibility fixtures are preserved under `fixtures/compatibility/`.

## Extension Conformance

Vendor or project-specific extensions SHOULD live under `extra`.

Extensions MUST NOT:

- weaken safe-profile requirements;
- request credentials or privileged actions;
- redefine SESM fields incompatibly;
- claim browser, crawler, archive, or agent authority.
