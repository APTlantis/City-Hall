# APTlantis Release Hashing Standard Validation Checklist

- [ ] `ARHS.manifest.toml` exists and describes the standard suite.
- [ ] Required suite docs exist.
- [ ] Scope is clear.
- [ ] Non-goals are clear.
- [ ] Adopter schemas or manifest templates are separate from the standard-suite manifest.
- [ ] Templates exist or are explicitly deferred.
- [ ] Examples exist or are explicitly deferred.
- [ ] Validation procedure is documented.
- [ ] Known gaps are recorded.

Specific to ARHS:
- [ ] Hashes provided include SHA256.
- [ ] Hashes provided include BLAKE3-256.
- [ ] Hashes provided include KT128.
- [ ] Provided hashes correctly verify the artifact.
- [ ] Hash record names the exact artifact filename.
- [ ] Artifact size is recorded when known.
- [ ] Hash generation tool/command is recorded when practical.
- [ ] Public release records identify distribution channel and signing/provenance authority.
- [ ] Release document and hash record agree on artifact name and version.
- [ ] Hashes were computed from the final packaged artifact.
- [ ] AAMHS signatures are not described as a replacement for distribution-channel signing.
