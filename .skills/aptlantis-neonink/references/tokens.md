# Token and standard maintenance

TOML is the editable source. CSS/JSON and the representation/contrast reports are generated. Read the token contract before editing; the compiler requires paired hex/OKLCH coordinates, direct semantic references and in-gamut sRGB values.

Run the compiler, read-only freshness check and regression tests. If a contrast pair fails, preserve the legacy palette and choose a suitable semantic alias or explicitly restricted role. Never lower the contrast threshold to make the test pass. Review alpha/gradient combinations in the actual rendered context because the opaque audit does not cover them.

For a changed palette, include every changed value in a Before/After table with hex and OKLCH. Regenerate reference SVGs and PNG previews and inspect them. Record new roles, restrictions, source version and adopter migration choices. Retain historical evidence and versioned consumer contracts.

Use SFDS for maturity and suite structure; Candidate remains Candidate until real adopter and accessibility evidence supports promotion. Preserve the distinction among source, generated translations, static checks, reviewed references, and verified runtime behavior.
