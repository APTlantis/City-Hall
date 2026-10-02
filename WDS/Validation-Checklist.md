# WDS Validation Checklist

This checklist validates website readiness under WDS. SFDS suite conformance for WDS is tracked by `WDS.manifest.toml` and the WDS suite map.

- [ ] Site manifest exists.
- [ ] Site manifest passes `tools/wds_validate.py` or equivalent review.
- [ ] Build and deployment commands are documented.
- [ ] Accessibility review is complete.
- [ ] SEO metadata is present.
- [ ] Structured metadata is present where useful.
- [ ] Static assets have an organization rule.
- [ ] Monitoring or uptime expectation is documented.
- [ ] Deployment record identifies version or commit, target, environment, and verification.
- [ ] Key routes are listed and checked after deployment.
- [ ] Key routes are checked with `tools/route_check.py` or equivalent evidence.
- [ ] Rollback or restore expectation is documented.
- [ ] Environment level is identified: local, preview, production, or archived.
- [ ] Production publication has post-deploy route checks.
- [ ] Published state follows `Publication-Approval-Flow.md`.
- [ ] Accessibility findings are recorded before publication.
- [ ] Accessibility and metadata smoke checks run with `tools/accessibility_smoke.py` or equivalent evidence.
- [ ] Monitoring expectation states active, manual, or intentionally unmanaged.
- [ ] Required legal, license, privacy, or attribution content is present when applicable.
