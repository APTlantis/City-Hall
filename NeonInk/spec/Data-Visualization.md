# Data visualization contract

## Choose the encoding from the question

| Question | Preferred starting point | Required caution |
| --- | --- | --- |
| Compare categories | Sorted bars or dot plot | Bars start at zero; explain sort order |
| Change over time | Line or small multiples | Real time spacing; gaps for missing periods |
| Distribution | Histogram, box plot, points | Bins/sample size; explain summary statistic |
| Relationship | Scatterplot | Units, sample size, uncertainty; no causal claim from correlation |
| Part to whole | Stacked bar or simple labeled share | Common denominator; totals and rounding |
| Ordered intensity | Sequential heatmap | Ordered numeric legend; no rainbow scale |
| Deviation from a meaningful center | Diverging bars/heatmap | Explicit center, domain, and sign meaning |
| Process/provenance | Flow diagram | Named nodes and edges; width encodes quantity only if scaled |

Use position/length for precise comparisons. Avoid 3D charts, decorative area encodings, dual axes without strong justification, and smooth curves that imply unobserved measurements. Nonzero line-chart axes must be obvious. Log scales need positive data, clear labeling, and explanation of the transformation.

## Scale contract

`categorical` is a stable ordered set of five distinct role-independent series colors. Persist category-to-color assignments across filters, pages, and exports; also persist labels and marker shapes. Do not recycle a hidden category's color for a different category.

`sequential-cyan` contains five explicitly ordered stops of increasing OKLCH lightness. Use discrete bins with published boundaries by default. Continuous scales must document their interpolation, domain, clipping and out-of-range behavior; new interpolated colors need gamut and adjacency checks.

`diverging` runs violet → pale neutral → cyan, with a meaningful middle value. Its center is the highest-lightness stop, not a missing-data color. Use symmetric domains when comparing equal signed magnitudes; if asymmetric, document why. Labels `below` and `above` describe position relative to the center, not benefit or harm.

Zero, missing, unavailable, censored, and suppressed values are distinct. Missing is a gap/hatch plus text. Suppressed data must not be recoverable through tooltip or table. Distinguish estimate from observation with a dashed line or interval and a clear note.

## Numerical and editorial integrity

Show units, time zone where material, period, population/denominator, sample size, aggregation, and source/as-of date. Percent change and percentage-point difference are different measures. Show uncertainty where known; say when it is unknown. Do not add fabricated error bars. Preserve negative signs and enough precision to compare without implying false precision. Explain exclusion, weighting, normalization and rounding when they affect interpretation.

Use factual or qualified chart titles. A green badge requires a named check with evidence; a rising line alone cannot earn it. Do not infer quality from completeness. Synthetic fixtures must be labeled in every exported view and must never be presented as production metrics.

## Accessible interaction and exports

Direct labels are preferred when space permits. Otherwise keep the legend adjacent in the same reading order as the marks. Tables expose the same filtered population and units as the chart. Tooltip-only source notes are not acceptable. Provide a summary that communicates the finding and limitation, plus values in accessible form. Review actual output at target size and in grayscale; grayscale is a diagnostic, not proof of color-vision accessibility.
