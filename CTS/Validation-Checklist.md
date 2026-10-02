# CTS Validation Checklist

This checklist validates command-tool readiness under CTS. SFDS suite conformance for CTS is tracked by `CTS.manifest.toml` and the CTS suite map.

- [ ] Commands are documented.
- [ ] Exit codes are documented.
- [ ] `--help` or equivalent exists.
- [ ] JSON or structured output is stable when provided.
- [ ] JSON examples validate against the CTS envelope using `tools/cts_validate.py` or equivalent review.
- [ ] stderr is used for diagnostics, not normal data output.
- [ ] Automation examples exist.
- [ ] Release checklist is complete.
- [ ] stdout/stderr behavior is documented.
- [ ] Machine-readable output mode avoids progress text on stdout.
- [ ] Stable fields are identified for automation consumers.
- [ ] Command stability level is assigned for public commands.
- [ ] Breaking CLI changes are versioned or have a migration note.
- [ ] Command-specific `data` payload fields follow `JSON-Data-Payload-Guidance.md` or document an exception.
- [ ] Destructive commands document preview, confirmation, and recovery behavior.
- [ ] `--quiet` does not hide failures.
- [ ] `--verbose` does not change machine-readable output shape.
