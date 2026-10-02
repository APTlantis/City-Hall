# Adopting NeonInk 0.2

Choose NeonInk for reports, charts, dataset profiles, explanatory diagrams, presentation slides and portable data artifacts. Keep Blue Slate for the operational host. Existing historical adopters may remain pinned; read the migration record before changing imports.

1. Read the design system, data visualization contract and relevant layout/profile.
2. Record the suite version, source, presentation boundary and host theme using the adoption template.
3. Compile or consume the versioned generated tokens. Scope embedded CSS. Keep category identity separate from status.
4. Build the chart with its summary/table and visible units, period, source, denominator and limitations.
5. Verify exact data values, token freshness, accessibility, responsive behavior, and the actual export/runtime in the intended host.
6. Record results, deviations, owner, outstanding gaps and rollback assets. A pilot can proceed with documented limits; do not label it stable without evidence.

## Agent skill

The canonical skill is `skills/aptlantis-neonink/`. Its entrypoint resolves resources against the chosen suite root, so a synchronized installed copy can live under the user's skills directory. Keep the suite version/provenance visible. Creating the canonical skill does not by itself install it globally or migrate other apps.

## Minimum evidence

Record a real source dataset or label the fixture synthetic. Include one reviewed target-size image/export, one accessible value representation, relevant keyboard/zoom checks, and a readable source/limitations note. Native adapters need native runtime evidence; an SVG preview does not establish it.
