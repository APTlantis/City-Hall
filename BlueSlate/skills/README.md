# Blue Slate agent scope

Use [aptlantis-blue-slate](aptlantis-blue-slate/SKILL.md). It replaces the former `theme-auditor` and `aptlantis-theme-compiler` fragments.

Token and layout authority lives under `../spec/`; visual boards live under `../spec/mockups/`; the image palette extractor lives at `../tools/PaletteGenerator32.ps1`. Their prior locations and hashes are recorded in the release review. Do not recreate competing copies inside the skill.

This directory is the authored skill source requested for this suite. It is not automatically installed in a global agent skill registry. Invoke its SKILL.md explicitly or install through the agent host's normal mechanism when requested.
