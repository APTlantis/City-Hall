# Layout and UI work

Read the suite overview for section anatomy and the layout catalog for pattern selection. Start from the operator's task and content relationships:

| Job | Pattern |
| --- | --- |
| Explain a standard or record | Dossier Stack |
| Summarize peer ideas | Pillar Grid |
| Relate source to output | Split Console |
| Inspect proof, files or checks | Evidence Grid |
| Perform staged operations | Workflow Rail |
| Monitor meaningful metrics | Instrument Panel |
| Inspect screenshots or diagrams | Gallery Matrix |
| Operate an interactive experiment | Lab Stage |
| Switch among peer explanations | Segmented Explainer |
| Browse guides and resources | Resource Shelf |

Use only the sections the task needs: orientation header, navigation/context rail, primary work, supporting explanation, evidence/provenance, action/workflow, status and continuation. Keep the primary work intelligible without hover or hidden panels. Labels and values stay together; dense tables retain column meaning and alignment. Expose evidence source/state/version when it helps the operator assess a claim.

Use deep canvas, layered neutral panels, quiet borders and readable pale text. Roughly 85/15 neutral/signal is design guidance, not a pixel quota. Cyan/arctic signals focus and action; teal technical emphasis; amber/brass warning and attention; violet/indigo taxonomy/archive; green success/verification; danger denotes errors/destructive intent. Status always has a non-color cue. A decorative “verified” badge must never substitute for actual validation.

Inspect `spec/mockups/Blue Slate Bootstrap Theme Board.png` for component density, states and surface hierarchy and `blue-slate-semantic-swatches.png` for the current palette. The two older overview/mockup images show lineage and composition, not current measured values. Typography stacks come from TOML; the suite does not bundle the fonts.

Cover default, hover, keyboard focus, active and disabled controls; default/focused/valid/invalid/disabled fields; loading, empty, error and unavailable content. Preserve visible focus, accessible names, heading hierarchy, reduced-motion preferences and explanations of unavailable actions. On narrow screens stack source before output, keep collapsed navigation reachable, and retain evidence labels rather than hiding essential content.

Validate actual foreground/background combinations: 4.5:1 for normal text, 3:1 for large text and non-text interactive indicators. Source-pair audits do not cover alpha composites, overlays or every component state. Compare resting desktop and narrow views, keyboard traversal and state transitions in the actual host. Report a static specimen as a specimen, never as proof of a working product.
