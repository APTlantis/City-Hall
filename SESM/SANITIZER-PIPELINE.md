# SESM Sanitizer Pipeline

## Purpose

SESM safe-profile validation is a metadata and SVG safety gate.
It does not replace an independent SVG sanitizer when assets will be displayed in browsers, indexed by crawlers, or accepted from untrusted sources.

## Recommended Pipeline

1. Treat the SVG as untrusted input.
2. Run an independent SVG sanitizer appropriate to the deployment surface.
3. Run SESM safe-profile validation:

```powershell
python SESM\Validate-SESM-Safe.py SESM\fixtures\valid\basic-safe.svg --safe-profile --json
```

4. Reject assets with `status: "error"` or `profile: "sesm-unsafe"`.
5. Review assets with `status: "warning"` or `profile: "sesm-unverified"`.
6. Store sanitized assets and validation output as release or ingestion evidence when the workflow is archival, public, or automated.

## Sanitizer Expectations

A sanitizer should remove or block browser-executable or remote-loading SVG behavior, including:

- script elements;
- event handler attributes;
- JavaScript URLs;
- unsafe data URLs;
- remote resource loads;
- foreign-object content when not explicitly allowed by the adopter;
- active animation or interaction features when the display surface does not need them.

## Division Of Responsibility

| Layer | Responsibility |
| --- | --- |
| SVG sanitizer | Browser and renderer safety. |
| SESM safe-profile validator | SESM metadata validity, forbidden SESM authority, and SESM-specific safe-profile checks. |
| Adopter ingestion policy | File size limits, trust source, quarantine, storage, review, and publication rules. |

SESM validation should run after sanitization when the sanitizer preserves metadata.
If the sanitizer removes `<metadata id="sesm">`, run SESM validation before sanitization for review evidence and again after sanitization to confirm the final published asset state.
