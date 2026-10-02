# Prospective maturity promotion gate

Adopted 2026-10-02 for future candidate-to-stable/reference reviews. Existing maturity declarations remain dated evidence under their original review rules; this gate does not recertify them. Candidate-active is a lifecycle status, while candidate is a maturity level.

A new promotion requires complete suite anatomy, zero errors in applicable schema/linter checks, two independent non-teaching production adopters, and dated observed runtime evidence for the proposed coverage. Run `sfds_validate.py` first, then `promotion_review.py SUITE RECORD.toml`. The validator checks records and referenced nonempty files; a named reviewer must verify their contents, independence, version alignment and scope. File presence and self-declared pass fields do not establish compliance.

Runtime evidence means observed execution of the governed workflow. For document-oriented standards this can be an executed governance/adoption workflow; browser or application execution is needed only where the domain requires it. No standard is promoted automatically.

Use [the record template](templates/Promotion-Review.toml). Paths resolve relative to the review record. Store production evidence separately from teaching examples. Missing evidence remains a blocker, never a synthetic pass. Reference promotion also requires the existing reference conformance expectations.

Compatibility: this is an explicit migration of prospective promotion rules, not a new required field in existing suite manifests. Existing adoption contracts and stable/reference declarations are retained. Future reviewers must use this gate.
