# NeonInk layout patterns

## Analytical report

Use for one decision or question: context line → finding headline → large chart with units → comparison/annotation → source, method, caveat, and table. A secondary chart should answer a supporting question. Avoid a grid of unrelated KPI cards. Desktop may use an 8/4 split for chart and interpretation; below roughly 800 px, stack in reading order. Keep export composition legible without interactive tooltips.

## Dataset profile

Use for understanding a corpus: identity and version → scope/count/period → coverage distribution → schema sample → quality limitations → provenance/license/access. Distinguish total records from eligible records. Show a count with its collection window and denominator. Status labels require actual evidence. The fixture board shows coverage, not a claim of corpus readiness.

## Explanatory plate

Use for a process, method, or scale: question → 3–5 labeled steps or visual examples → legend → takeaway and limitations. Arrows describe a named relationship. Rectangular geometry and consistent alignment replace the former manga panel language. Use contrasting boundaries and text; glow never carries an essential edge.

## Narrative slide or static export

One primary message per frame; chart consumes most of the frame. Use larger type appropriate to viewing distance, with source still legible. Preserve data units and caveats in the exported frame. SVG gives resolution-independent geometry, PNG gives a portable preview; neither substitutes for a companion table when data access is needed. Print requires its own color/contrast review.

## Embedded presentation in a Blue Slate app

Keep shell, sidebar, dialogs, controls, editing tables, and task status with the host theme. Place report content in an explicitly scoped `.neonink` region. Use the host component library's controls and keyboard behavior. A report export may be fully NeonInk. Do not globally import `:root` tokens into an existing app without reviewing cascade ownership; use the scoped token variant described in the framework profile.
