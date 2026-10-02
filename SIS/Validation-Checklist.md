# SIS Validation Checklist

This checklist validates service and infrastructure readiness under SIS. SFDS suite conformance for SIS is tracked by `SIS.manifest.toml` and the SIS suite map.

- [ ] `SIS.manifest.toml` exists and describes the standard suite.
- [ ] README explains SIS's role in City Hall.
- [ ] Primary specification states the service and infrastructure rules.
- [ ] Adoption guide exists.
- [ ] Validation checklist exists.
- [ ] Changelog exists.
- [ ] Templates exist for service manifest, runbook, health check, and resource constraints.
- [ ] Examples exist for at least one local API service and one workspace cache or infrastructure service.

Specific to SIS-governed services:

- [ ] Service manifest exists.
- [ ] Project class is `service` or `infrastructure`, or the service role is otherwise justified.
- [ ] Start command is documented.
- [ ] Stop command is documented.
- [ ] Restart behavior is documented.
- [ ] Graceful shutdown behavior is documented.
- [ ] Machine-readable health check exists or a documented exception is recorded.
- [ ] Health statuses include `healthy`, `degraded`, `offline`, or `unknown`.
- [ ] Ports, protocols, and bind addresses are declared.
- [ ] Port conflict behavior is documented.
- [ ] State paths are declared.
- [ ] Cache paths are declared.
- [ ] Log paths are declared.
- [ ] Log rotation or retention policy exists.
- [ ] Cache growth limit or cleanup trigger exists.
- [ ] Recovery procedure exists.
- [ ] Dependencies are declared.
- [ ] Agent-safe operating rules are documented.
- [ ] Known failure modes are recorded.
