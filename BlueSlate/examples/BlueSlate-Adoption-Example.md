# Blue Slate Adoption Example

This example shows the minimum documentation footprint for a project adopting Blue Slate while the standard is candidate active.

## Project Manifest Entry

```toml
[governance.visual_system]
standard = "Blue Slate"
standard_path = "D:\\.city_hall\\BlueSlate\\README.md"
adoption_level = "pilot"
standard_version = "0.5.0"
token_source_version = "0.5.0"
profile = "WPF-pilot"
primary_layout = "Split Console"
secondary_layouts = ["Evidence Grid"]
validation_state = "planned"
local_deviations = []
known_gaps = ["Native control states and keyboard traversal need runtime verification."]
token_source = "D:\\.city_hall\\BlueSlate\\spec\\tokens\\BlueSlate.Tokens.toml"
```

## Project README Note

The project uses Blue Slate for visual tokens, layout rhythm, component density, and design-to-implementation handoff. Any local visual departures should be recorded as project-specific profile decisions rather than edits to the standard.

## Validation

Before closeout, compare screens or mockups against `Validation-Checklist.md`, confirm the token source is still current, and record unresolved gaps in the project closeout notes.
