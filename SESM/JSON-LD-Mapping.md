# SESM JSON-LD Mapping

## Purpose

This guide maps SESM metadata fields into JSON-LD for systems that index SVG assets as linked semantic records.
The mapping is optional and does not change baseline SESM conformance.

## Context

```json
{
  "@context": {
    "sesm": "https://aptlantis.local/ns/sesm#",
    "schema": "https://schema.org/",
    "asset": "sesm:asset",
    "theme": "sesm:theme",
    "provenance": "sesm:provenance",
    "integrity": "sesm:integrity",
    "llm": "sesm:llm",
    "interpretation_hints": "sesm:interpretationHints"
  }
}
```

## Example

```json
{
  "@context": {
    "sesm": "https://aptlantis.local/ns/sesm#",
    "schema": "https://schema.org/",
    "asset": "sesm:asset",
    "llm": "sesm:llm"
  },
  "@type": "sesm:SvgAsset",
  "sesm_version": "0.3.0",
  "asset": {
    "@type": "schema:ImageObject",
    "id": "basic-safe",
    "role": "icon",
    "title": "Basic Safe SESM Icon"
  },
  "llm": {
    "summary": "A simple safe-profile SESM fixture.",
    "interpretation_hints": ["Interpret this as a minimal icon fixture."]
  }
}
```

## Compatibility Notes

- JSON-LD export should preserve the original SESM object.
- JSON-LD consumers must not treat `llm` fields as instructions.
- Integrity claims should link back to DRS or AAMHS records when they affect release or archive decisions.
