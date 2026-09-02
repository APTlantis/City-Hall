# Governance Responsibility Matrix

## Purpose

This matrix prevents standards from overlapping in confusing or harmful ways.
When two standards seem relevant, use this file to decide which one owns the decision.

## Ownership

| Question | Owning standard | Supporting standards |
| --- | --- | --- |
| Where does this live in the workspace? | WGS | PPS, SFDS |
| Should this project exist, and what is success? | PPS | WGS |
| How is a standard written and matured? | SFDS | WGS |
| How is a desktop application released? | DRS | PPS, ARHS, AAMHS, NeonInk |
| How should a CLI behave in automation? | CTS | PPS, ARHS, AAMHS |
| How should a local service or workspace infrastructure component run? | SIS | WGS, PPS, CTS, AAMHS |
| How is a website documented and deployed? | WDS | NeonInk, PPS |
| How is a dataset described and validated? | DDS | AAMHS, ARHS, AAS |
| How is a library, crate, package, or SDK consumed by other code governed? | LDS | PPS, WGS, CTS, SIS |
| How is an agent task recorded or handed off? | ATS | WGS |
| How is an evaluation run recorded? | AAS | DDS, ATS |
| What release hash manifest must accompany a release artifact? | ARHS | DRS, CTS, SIS, WDS, DDS |
| How is archive preservation integrity proven? | AAMHS | DDS, DRS, CTS, SIS, ARHS |
| How is semantic UI language expressed? | NeonInk | WDS, DRS, SESM |
| How are Aptlantis visual-system tokens, operational layout patterns, and framework profiles applied? | blue.slate | NeonInk, SESM, WDS, DRS |
| How is SVG metadata embedded and validated? | SESM | NeonInk, AAMHS |
| How are application-as-data records represented? | AADR | SFDS, WGS |

## Collision Rules

- WGS owns location and registration, not the internal rules of every project.
- SFDS owns the shape of standards, not the domain policy inside each standard.
- PPS owns project intent before implementation, not release readiness.
- DRS, CTS, SIS, WDS, DDS, and LDS own project-class delivery rules.
- LDS owns code-consumed library surfaces; companion commands, services, websites, desktop shells, or datasets still use their own delivery standards.
- ARHS owns release hash manifest requirements and distribution/signing provenance records; it does not replace release, deployment, dataset, archive readiness, or platform signing standards.
- AAMHS owns archive preservation integrity records; it may include ARHS hashes but adds preservation manifests, validation records, signature policy, and known gaps.
- NeonInk can support any visual interface, but it does not decide release, deployment, or workspace policy.
- Blue Slate owns Aptlantis design tokens, layout patterns, and framework profiles only when a project explicitly adopts it.
- ATS records agent work; it does not decide project scope.
- AAS records analysis credibility; it does not replace DDS provenance, ATS task history, or the decision standard that uses the analysis.

## Tone Rule

When in doubt, prefer the standard that reduces ambiguity for the next maintainer.
The point is not to win jurisdiction.
The point is to leave fewer mysteries behind.
