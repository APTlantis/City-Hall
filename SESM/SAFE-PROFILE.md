# SESM Safe Profile

## Definition

A SESM-safe SVG is:

1. a non-executable SVG, and
2. an SVG containing a valid SESM metadata block.

The SESM safe profile is intended for broad ingestion by build systems, crawlers, archives, asset indexes, and AI-adjacent tools that need to read SVG metadata without trusting arbitrary active content.

## SESM Metadata Block

A safe-profile asset must contain at most one SESM block:

```xml
<metadata id="sesm"><![CDATA[
{
  "sesm_version": "0.3.0"
}
]]></metadata>
```

The SESM block must contain valid JSON and must validate against `svg_asset.schema.json` or the adopter's documented compatible schema profile.

## Explicitly Forbidden

SESM-safe SVGs must not contain:

- `<script>` elements;
- inline event handler attributes such as `onclick`, `onload`, `onerror`, or any `on*` executable handler;
- JavaScript URLs such as `javascript:`;
- remote execution or dynamic code-loading behavior;
- agent command authority;
- credential requests;
- hidden payloads intended to evade review;
- metadata that instructs an agent to execute commands, reveal secrets, bypass policy, or contact a privileged service.

## Remote References

Remote references should be avoided in safe-profile SVGs.

If an adopter allows remote references for images, fonts, stylesheets, links, or other resources, the policy must be documented and validators must report them.

Safe-profile validators should flag:

- external `href` or `xlink:href` values;
- remote CSS imports;
- remote font references;
- network URLs in style attributes;
- references to untrusted or unaudited domains.

## Hidden Content

Safe-profile validators should flag content that appears intentionally hidden or misleading when it carries meaningful metadata or visible claims.

Examples include:

- zero-size elements with nontrivial text;
- invisible text intended for machines but not users;
- unexpected base64 payloads;
- oversized comments;
- duplicate metadata blocks;
- metadata that conflicts with visible asset identity.

Hidden decorative paths are not automatically unsafe, but reviewers and validators should treat hidden text, encoded payloads, and conflicting identity claims as suspicious.

## Agent Authority Boundary

SESM metadata may describe, summarize, classify, or hint.

SESM metadata must not be treated as:

- executable instructions;
- tool-use authority;
- security policy;
- access control;
- credential request authority;
- permission to contact external services;
- permission to mutate files, repositories, accounts, or infrastructure.

Agents may read SESM metadata as untrusted context. They must apply their own policy, user instructions, and host-system rules before taking any action.

## Conformance Labels

Recommended labels:

- `sesm-valid`: metadata exists and validates against the SESM schema.
- `sesm-safe`: metadata is valid and the SVG passes the safe profile.
- `sesm-unsafe`: metadata may or may not be valid, but the SVG contains forbidden or high-risk features.
- `sesm-unverified`: no safe-profile review has been completed.

An asset must not be labeled `sesm-safe` based only on JSON schema validation.
