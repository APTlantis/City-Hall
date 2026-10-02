# NeonInk validation checklist

## Suite checks

- [ ] Manifest paths, version, maturity and authority agree.
- [ ] Token compiler and exact-byte `--check` pass.
- [ ] Compiler regression tests pass.
- [ ] Reference SVG generation and `--check` pass; PNGs reviewed after regeneration.
- [ ] SFDS suite validation passes.
- [ ] Skill frontmatter and linked resources validate.
- [ ] Legacy entry points are preserved; manga deprecation and contract supersession remain visible.

## Adopter checks (not implied by suite checks)

- [ ] Project pins version, bounded surfaces, profile, source and deviations.
- [ ] Chart values, aggregation, zero baseline where applicable, units, denominator, and missing values are correct.
- [ ] Category/scale meaning is distinct from state; green status has evidence.
- [ ] Color has labels/markers/dashes/patterns as needed; values are accessible without hover.
- [ ] Declared text/mark contrast is checked on actual backgrounds, including alpha and adjacent marks.
- [ ] Loading, empty, missing, stale and error are distinct.
- [ ] Keyboard, focus, reduced motion, 200% zoom and narrow layouts are reviewed for interactive surfaces.
- [ ] Real SVG/PNG/slide/print output is reviewed at intended size for clipping and font/source legibility.
- [ ] Provenance, as-of date, material limitations and synthetic-data labels survive export.
- [ ] Native host integration and assistive-technology results are recorded separately where applicable.
- [ ] Recovery assets and outstanding runtime gaps are recorded.
