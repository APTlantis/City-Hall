# Blue Slate Validation Checklist

This checklist separates Blue Slate suite validation from adopter validation.

## Suite Validation

- [ ] `README.md` explains the standard's role and read path.
- [ ] `spec/BlueSlate.DesignSystem.md` is the primary specification.
- [ ] `spec/BlueSlate.Overview.md` integrates token, section-anatomy, pattern, state, and conformance guidance.
- [ ] `BlueSlate.manifest.toml` describes the standard suite.
- [ ] `Adoption-Guide.md` exists.
- [ ] `Validation-Checklist.md` exists.
- [ ] `CHANGELOG.md` records version and promotion history.
- [ ] `spec/tokens/BlueSlate.Tokens.toml` parses successfully and is the sole canonical token source.
- [ ] Generated CSS, Tailwind, SiYuan, and JSON compatibility outputs identify the TOML source/version.
- [ ] `tools/Audit-BlueSlate.ps1` reports declared contrast pairs and unresolved schema references.
- [ ] CSS and framework translations identify the token source they follow.
- [ ] Each Bootstrap 5.3 compatibility variable maps to a canonical semantic/raw role or is documented as a Bootstrap-required alias.
- [ ] Bootstrap starter example is registered and covers the documented state matrix.
- [ ] NeonInk and SESM relationships are documented.
- [ ] Known gaps are recorded instead of hidden.
- [ ] `tools/compile_blueslate.py --check` passes without creating or changing generated files.
- [ ] Compiler negative regressions and `tools/validate_suite.py` pass.
- [ ] SFDS suite validation passes for the canonical destination.
- [ ] `Migration-0.5.md` preserves legacy consumer paths and accurately describes partial profiles.
- [ ] The comprehensive skill's references resolve and its frontmatter validator passes.

Current execution evidence is recorded in `reports/Review-2026-09-27.md`. This reusable checklist is not itself a completed audit record.

## Adopter Validation

- [ ] The project explicitly records Blue Slate adoption.
- [ ] Adoption level is stated: `pilot`, `active`, or `project-profile`.
- [ ] Token source version is recorded.
- [ ] The implementation uses semantic tokens before raw colors.
- [ ] Accent colors carry state, hierarchy, action, proof, or risk.
- [ ] Primary and secondary layout patterns are named.
- [ ] Framework-specific notes are followed or deviations are documented.
- [ ] Accessibility and contrast issues are checked for the adopted surface.
- [ ] Bootstrap adopters record Bootstrap 5.3.x, Blue Slate token version, and local overrides.
- [ ] Bootstrap adopters check cards, navigation, tables, badges, buttons, forms, alerts, progress, and code at desktop width.
- [ ] Button default/hover/focus/active/disabled and valid/invalid/disabled field states are visibly distinct and keyboard focus is visible.
- [ ] Normal text meets 4.5:1 minimum contrast; large text and non-text interactive indicators meet 3:1 minimum.
- [ ] Project-specific additions are recorded as local profile decisions.

## Candidate-Active Gaps

- [ ] More real adopter evidence is needed before stable maturity.
- [ ] The Bootstrap 5.3 profile needs rendered adopter evidence before stable maturity.
- [ ] Native and SiYuan adopter state evidence is still needed; NeonInk remains independently governed.
