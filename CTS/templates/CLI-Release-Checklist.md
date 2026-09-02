# CLI Release Checklist

- [ ] Command contracts updated.
- [ ] Exit codes documented.
- [ ] Help output reviewed.
- [ ] Machine-readable output validated.
- [ ] stdout contains only documented data in machine-readable mode.
- [ ] stderr contains diagnostics, warnings, progress, and errors.
- [ ] Exit code behavior tested for success, invalid usage, missing input, and validation failure.
- [ ] Automation examples tested.
- [ ] Version recorded in manifest.
- [ ] Distribution channel recorded (GitHub release, package ecosystem, Windows portable ZIP, package manager, or internal).
- [ ] ARHS `.hashmanifest.toml` generated for publishable binary/archive artifacts.
- [ ] Signing/provenance authority recorded when public.
- [ ] ArchiveHasher or `manifest-signer.exe` is used only for AAMHS archive-preservation signing, not as normal release signing.
