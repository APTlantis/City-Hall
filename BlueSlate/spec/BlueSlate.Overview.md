# Blue Slate Overview Specification

Version: 0.5.0  
Status: candidate-active local standard  
Canonical token source: `spec/tokens/BlueSlate.Tokens.toml`

This is the integrated overview of the Blue Slate visual system. It explains how the token source, visual rules, page sections, layout patterns, component states, and framework profiles fit together.

It is an overview and operating contract, not a replacement for the machine-readable token source. The TOML remains authoritative for token names and values. `BlueSlate.DesignSystem.md` remains the concise design rationale, and `BlueSlate.LayoutPatterns.md` remains the focused pattern catalog.

## 1. Scope and role

Blue Slate is the Aptlantis visual-system standard for local-first tools, archival project pages, evidence dashboards, command surfaces, documentation tools, and Windows desktop utilities.

Blue Slate governs:

- semantic color and foundation tokens;
- visual hierarchy, surfaces, borders, density, and interaction states;
- reusable page and application-shell shapes;
- evidence-first presentation of records, outputs, status, and provenance;
- framework translations and starter-pack implementation guidance.

Blue Slate does not govern product meaning, domain metadata, project readiness, or release approval. WGS, PPS, DRS, CTS, WDS, NeonInk, and SESM retain their adjacent responsibilities. A project must explicitly adopt Blue Slate and record whether the adoption is `pilot`, `active`, or `project-profile`.

## 2. Governing principles

### 2.1 Neutral structure, meaningful signal

The interface is predominantly blue-black neutral structure, with signal colors reserved for action, focus, status, proof, taxonomy, priority, or risk. As a working proportion, keep roughly 85 percent of the surface neutral and 15 percent signal-bearing.

### 2.2 Evidence before decoration

Screens should make source, state, relationship, and output legible. A checksum, file status, command result, validation state, or provenance note is a first-class visual object. Do not add an accent merely to make an otherwise empty panel interesting.

### 2.3 Semantic tokens before raw colors

Use a semantic or component token whenever one exists. Raw palette values belong in the canonical token source or in a documented project profile; they should not be scattered through application styles.

### 2.4 Persistent hierarchy

The resting screen must communicate role through surface, spacing, typography, and boundary—not only through hover, focus, selection, or animation. Interaction states clarify an existing hierarchy; they do not create the entire hierarchy.

### 2.5 Compact operational rhythm

Blue Slate favors working density over marketing whitespace. Compact does not mean cramped: group related facts, keep labels close to values, and provide enough separation for scanning and keyboard use.

### 2.6 One dark theme

Blue Slate is dark-only. This version does not define a light palette or a user-selectable color-mode switch. Framework profiles may translate the same dark contract, but they may not silently introduce a competing canonical theme.

## 3. Authority and reading order

| Concern | Authoritative document | Use this overview for |
| --- | --- | --- |
| Token names and values | `spec/tokens/BlueSlate.Tokens.toml` | Layer meaning and usage rules |
| Design intent and rationale | `spec/BlueSlate.DesignSystem.md` | Integrated interpretation |
| Page and content patterns | `spec/layout/BlueSlate.LayoutPatterns.md` | Pattern choice and section anatomy |
| Framework mechanics | `spec/frameworks/` | Translation-specific implementation |
| Assets and visual evidence | `spec/assets/BlueSlate.Assets.md`, `spec/references/` | Source and provenance boundaries |
| Adoption and validation | `Adoption-Guide.md`, `Validation-Checklist.md` | Project onboarding and checks |

When documents appear to disagree, resolve the disagreement in this order:

1. Confirm the token path in the TOML.
2. Preserve the semantic role and dark-only policy.
3. Treat framework names as adapters, never as new canonical roles.
4. Record an intentional exception in the adopting project's profile.

## 4. Token architecture

The token source has five canonical layers:

| Layer | Purpose | Examples |
| --- | --- | --- |
| `palette` | Stable named source colors with exact hex and OKLCH | `abyss`, `electric-cyan`, `verified` |
| `semantic` | Meaning shared across products | `surface.panel`, `content.primary`, `intent.warning` |
| `component` | Roles consumed by recurring controls and content forms | `button.primary-background`, `code.keyword` |
| `foundation` | Geometry and visual mechanics | radius, spacing, elevation, focus ring |
| `typography` | Font-family stacks by reading role | display, sans, mono |

Framework maps under `[framework.*]` are compatibility translations only. Generated CSS, Tailwind, SiYuan, and JSON artifacts must identify the TOML source and version that produced them.

### 4.1 Semantic role families

The semantic contract is organized as follows:

- Surfaces: `canvas`, `canvas-recessed`, `panel`, `panel-raised`, `panel-accent`, `overlay`, `popover`, `input`, `table`, `disabled`.
- Content: `primary`, `emphasis`, `secondary`, `tertiary`, `disabled`, `link`, `link-hover`, `code`, `code-accent`.
- Structure: `border`, `border-soft`, `border-strong`, `border-translucent`.
- Intent: `primary`, `secondary`, `success`, `info`, `warning`, `danger`, `attention`, `taxonomy`, `archive`, `verified`.
- Interaction: `action`, `action-secondary`, `hover`, `active`, `disabled`, `focus`.
- Validation: `valid`, `valid-border`, `invalid`, `invalid-border`.

### 4.2 Accent meanings

| Accent family | Meaning |
| --- | --- |
| Cyan / arctic | Focus, primary action, active navigation, live interaction |
| Teal | Selected technical surface, secondary action, data emphasis |
| Amber / brass | Warning, priority, preflight note, command attention |
| Violet / indigo | Taxonomy, special state, archive, vault, classification |
| Green | Healthy, verified, successful, complete |
| Pink | Editorial code or differentiated signal detail |

Every status accent needs a non-color cue such as a label, icon, value, or shape. If an accent has no semantic job, use a neutral surface or border.

## 5. Standard surface anatomy

This section supplies the section-specific contract that the layout catalog intentionally does not repeat in full. A page may omit a section when its purpose does not require it, but it should not invent a competing hierarchy without documenting a project profile.

### 5.1 Global frame

The frame establishes the Blue Slate environment:

- deep canvas or recessed canvas background;
- restrained technical grid or texture, when useful;
- readable outer margins and a bounded content measure;
- one clear active route or task signal;
- no decorative gradient or bright border that competes with content.

The frame is not a content card. It should remain visually quieter than the primary work surface.

### 5.2 Orientation header

The header answers “where am I and what is this for?” It contains, as applicable:

- eyebrow, area, or product context;
- page title;
- one-sentence purpose or status summary;
- optional primary action;
- optional compact metadata such as version, source, or lifecycle state.

Keep the title and purpose together. Put secondary metadata near the header but do not let it displace the purpose statement.

### 5.3 Navigation and context rail

Use navigation to expose route, scope, or nearby concepts—not to repeat every document name. The active item uses a persistent surface or boundary plus a cyan/teal signal. A context rail may contain:

- section navigation;
- filters or scope selectors;
- related records;
- “what is loaded?” or “why is this sparse?” explanations.

Do not use a rail as a dumping ground for controls that belong to the primary workflow.

### 5.4 Primary work section

This is the page’s main answer, operation, comparison, or visual. It should be the largest or clearest region and should use the page’s primary pattern. It contains:

- a local heading that names the job of the section;
- the minimum explanatory text needed to interpret the content;
- the central records, controls, visualization, or generated output;
- an explicit empty, loading, or error state when the expected content is absent.

The primary work section must be understandable without inspecting hover states or opening a secondary panel.

### 5.5 Supporting section

Supporting content adds context without competing with the primary work. It may contain assumptions, a short explanation, related resources, a legend, or a next step. Use a quieter surface and lower density than the primary section.

Supporting sections should answer one of three questions: “How do I read this?”, “What relates to this?”, or “What can I do next?” If they answer none, remove or defer them.

### 5.6 Evidence and provenance section

Evidence sections make claims inspectable. A useful evidence item exposes:

- item type or role;
- human-readable title;
- source or path;
- current state;
- timestamp or version when relevant;
- relationship to the page’s main subject;
- action such as inspect, open, compare, or verify.

Use `Evidence Grid`, `Resource Shelf`, or a compact table. Do not imply verification merely because a file exists; distinguish observed, generated, validated, and runtime-verified states.

### 5.7 Action and workflow section

Actions should be grouped by task and ordered by consequence:

1. primary action;
2. safe secondary action;
3. inspection or preview action;
4. destructive or irreversible action, visually separated and explicitly labeled.

Workflow sections expose stages, inputs, outputs, and the current step. A button label should describe the result (`Validate manifest`, `Open source`, `Generate preview`) rather than a vague gesture (`Continue`, `Do it`).

### 5.8 Status and validation section

Status communicates a condition, not a decoration. Pair each state with a label and, where useful, a value or explanation. The minimum state vocabulary is:

- neutral or not evaluated;
- active or in progress;
- attention or preflight;
- warning or blocked;
- invalid or failed;
- verified or complete;
- unavailable or disabled.

Use stable structure so a state change does not move the surrounding content unnecessarily.

### 5.9 Footer and continuation

The footer closes the surface with provenance, version, related links, or the next meaningful route. It should not become a second navigation system. For operational tools, a compact status strip may replace a traditional footer when it exposes current source, sync state, or validation result.

## 6. Layout pattern contract

Choose one primary pattern per page or surface and no more than two secondary patterns. The patterns describe content relationships, not a mandatory component library.

| Pattern | Use when | Required anatomy | Avoid |
| --- | --- | --- | --- |
| Dossier Stack | Explaining a standard, policy, FAQ, or trust note | orientation header, ordered prose sections, evidence/related links | long undifferentiated text |
| Pillar Grid | Summarizing a small set of peer ideas | short header, balanced cards, one fact per card | unequal card walls and tiny paragraphs |
| Split Console | Relating input to output or explanation to command result | source pane, output pane, shared context, clear action | unrelated dashboard tiles |
| Evidence Grid | Showing files, checks, screenshots, or verification records | scannable item cards, state, source, inspect action | decorative gallery treatment |
| Workflow Rail | Showing a staged operator flow | ordered stages, current step, inputs, outputs, recovery note | progress without actionable state |
| Instrument Panel | Monitoring health, readiness, or quality gates | headline metric, supporting metrics, state legend, detail path | numbers without interpretation |
| Gallery Matrix | Showing screenshots, diagrams, or visual states | one featured item, supporting items, captions, source | image-only meaning |
| Lab Stage | Teaching or operating an interactive module | controls, live result, explanation, reset/error path | controls with no visible result |
| Segmented Explainer | Switching among a few peer concepts | visible selected segment, stable content region, accessible labels | using it as primary site navigation |
| Resource Shelf | Organizing guides, templates, downloads, or references | type, title, purpose, status, source/action | anonymous link lists |

Pattern tokens must come from the shared semantic/component contract. A pattern may introduce local layout measurements, but it should not introduce a new color meaning without a token review.

## 7. Component and state rules

### 7.1 Panels and cards

Use `panel` for grouped content, `panel-raised` for a deliberately elevated or primary group, and `panel-accent` for a technical or selected context. Use borders and spacing to establish hierarchy before adding glow or saturated fills.

### 7.2 Buttons and links

Primary controls use the primary action path. Secondary controls use teal or a quiet neutral treatment. Destructive actions use danger and explicit language. Links remain identifiable without relying on hover alone.

### 7.3 Inputs and tables

Inputs use a recessed surface, readable text, visible border, and distinct valid/invalid treatment. Tables use structure for scanning: header hierarchy, row rhythm, alignment, and meaningful emphasis—not a grid of equally bright lines.

### 7.4 Code and command surfaces

Code is a distinct recessed surface with mono typography and restrained syntax accents. Command output should expose execution state, source, and result; do not style all output as success.

### 7.5 Chips, badges, and alerts

Chips summarize a known state or classification. Alerts explain a condition that requires attention. Neither should be used as generic decoration. Always include text or an accessible label for the meaning.

### 7.6 Required state matrix

Interactive controls should visibly distinguish default, hover, focus, active, and disabled. Form fields should distinguish default, focused, valid, invalid, and disabled. Async or operational surfaces should also expose loading, empty, unavailable, and error states.

## 8. Responsive and density behavior

Responsive behavior preserves relationships rather than merely shrinking everything.

- Keep the primary work visible first.
- Collapse context rails only when their contents remain reachable and their scope is still clear.
- Stack split consoles in source-then-output order on narrow screens.
- Preserve evidence item labels and state; truncate secondary paths only with an inspect affordance.
- Keep touch targets and keyboard focus areas large enough for reliable operation.
- Let dense tables become a structured list or horizontal scroll region rather than hiding columns silently.
- Reduce decorative grid intensity before reducing text contrast.

## 9. Accessibility and meaning

- Normal text meets a 4.5:1 contrast minimum against its rendered surface.
- Large text and non-text interactive indicators meet a 3:1 minimum.
- Focus uses the cyan/arctic path and remains visible by keyboard.
- Color is never the only status or validation cue.
- Respect reduced-motion preferences; state changes remain understandable without animation.
- Heading order follows the information hierarchy.
- Interactive elements have names that describe their action or destination.
- Error, empty, loading, and unavailable states explain what happened and what the operator can do next.

## 10. Framework boundary

Framework profiles share semantics, not implementation mechanics. Use the relevant profile for CSS/Tailwind, Tauri/React, SiYuan, WinUI, WPF, or Bootstrap 5.3. Generated neutral outputs and starter packs are implementation aids; they do not override the TOML source.

Framework-specific aliases are allowed when the target requires them. Each alias must map back to a canonical semantic, component, foundation, or typography role. A framework profile must document any target-specific limitation, fallback, or deviation.

## 11. Adoption and conformance

An adopter records:

- Blue Slate adoption level;
- token source version;
- framework profile;
- primary and secondary layout patterns;
- project-specific additions or deviations;
- contrast, keyboard-focus, and state-coverage checks;
- known gaps and deferred cleanup.

Suite conformance means the token source, generated outputs, design documents, profiles, starter packs, and validation records remain aligned. It does not mean every adopter has identical markup or component code.

## 12. Change boundary

Additions belong in the smallest authoritative layer:

- a new stable color value: `palette`;
- a reusable meaning: `semantic`;
- a recurring control role: `component`;
- geometry or visual mechanics: `foundation`;
- a target-framework name: adapter map only;
- a page/content relationship: layout pattern or section guidance;
- a project-specific exception: adopter profile.

Do not add a token to solve a one-off spacing problem, rename an existing semantic role solely for a framework, or silently retune palette values. Changes to token names, values, theme mode, or semantic meaning require regenerated outputs and corresponding validation evidence.

## Related documents

- `spec/tokens/BlueSlate.Tokens.toml` — canonical token source.
- `spec/BlueSlate.DesignSystem.md` — concise design rationale and semantic contract.
- `spec/layout/BlueSlate.LayoutPatterns.md` — focused pattern catalog.
- `spec/frameworks/` — target-specific implementation profiles.
- `spec/assets/BlueSlate.Assets.md` — asset and visual-reference boundaries.
- `Adoption-Guide.md` — adopter workflow.
- `Validation-Checklist.md` — suite and adopter checks.
