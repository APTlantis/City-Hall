# Blue Slate Validation Checklist

This checklist separates Blue Slate suite validation from adopter validation.

## Suite Validation

- [ ] `README.md` explains the standard's role and read path.
- [ ] `spec/BlueSlate.DesignSystem.md` is the primary specification.
- [ ] `BlueSlate.manifest.toml` describes the standard suite.
- [ ] `Adoption-Guide.md` exists.
- [ ] `Validation-Checklist.md` exists.
- [ ] `CHANGELOG.md` records version and promotion history.
- [ ] `spec/tokens/BlueSlate.Tokens.json` parses successfully.
- [ ] CSS and framework translations identify the token source they follow.
- [ ] NeonInk and SESM relationships are documented.
- [ ] Known gaps are recorded instead of hidden.

## Adopter Validation

- [ ] The project explicitly records Blue Slate adoption.
- [ ] Adoption level is stated: `pilot`, `active`, or `project-profile`.
- [ ] Token source version is recorded.
- [ ] The implementation uses semantic tokens before raw colors.
- [ ] Accent colors carry state, hierarchy, action, proof, or risk.
- [ ] Primary and secondary layout patterns are named.
- [ ] Framework-specific notes are followed or deviations are documented.
- [ ] Accessibility and contrast issues are checked for the adopted surface.
- [ ] Project-specific additions are recorded as local profile decisions.

## Candidate-Active Gaps

- [ ] More real adopter evidence is needed before stable maturity.
- [ ] Automated token/profile validation is not yet provided.
- [ ] NeonInk lineage is documented, but not fully merged into a single promoted visual-language standard.
