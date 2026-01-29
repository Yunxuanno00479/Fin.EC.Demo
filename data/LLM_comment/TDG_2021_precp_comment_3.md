## Change Point at Transcript 396.204s (and Dimension Unavailable)

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **No.**
- If No: **metric disclosure.**
- Tracked departure rationale (excerpt-based): The narrative pivots from a backward-looking integration milestone with a numeric time anchor (“**For the first roughly 18 months**… integrated Esterline Technologies…”) to a new, time-bucketed performance framing (“**For the second roughly 18 months**… dealt with the unprecedented COVID-19 generated downturn…”), marking a discrete re-segmentation of the CEO-transition summary into sequential, comparable phases.

### B. Soft vs Hard Information Shift — Required
- Label: **Hard→Soft.**
- Justification: The **numeric cue hint** flags a quantitative/time-structured marker in the pre-change excerpt (**Before_has_numeric_cue=True**: “**first roughly 18 months**”), while the post-change excerpt is qualitative evaluative language (**After_has_numeric_cue=False**: “**They responded quickly and effectively.**”).

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before = -1.0; delta_after = 0.99956; slope_pattern = Similar slope (stable accumulation intensity).**
- Interpret: **Stable** accumulated communication intensity, with the packet reflecting a tonal inflection but not a clear steepening/flattening of cumulative tone momentum.

### D. Local Responses vs Session Baseline — Required
- Local Market Evidence Status: **Available.**
  - One local observation: **Quote_Revision_Frequency local_max = 29** within the local window.
  - One deviation-table highlight: **Trade_Volume local_mean_minus_baseline_mean = 190.247** (shares per bin).
- Regular-session context: In **Regular** trading hours, baseline activity is typically higher and more dispersed; against that backdrop, the local window shows **above-baseline quoting intensity and trade volume** co-occurring with the transcript inflection, while bid–ask spread is reported as dispersion only (negatives present; no sign interpretation).


## Change Point at Transcript 451.629s (and Dimension Unavailable)

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **No.**
- If No: **procedural transition.**
- Tracked departure rationale (excerpt-based): The change point coincides with a speaker handoff and opening remark (“**Now let me hand it over to Kevin.**” → “**Thanks, Nick.**”), representing a discrete transition from chair commentary to CEO-led presentation, with subsequent content moving into prepared acknowledgements and then toward business review.

### B. Soft vs Hard Information Shift — Required
- Label: **Soft→Soft.**
- Justification: Both sides are non-quantitative and interpersonal/procedural (numeric cue hints: **Before_has_numeric_cue=False; After_has_numeric_cue=False**), moving from handoff language to qualitative appreciation (“**personally thank Nick… over the last seven years**”).

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before = 0.01843; delta_after = 0.183; slope_pattern = Steepening (higher information injection intensity).**
- Interpret: **Steepening** suggests higher accumulated communication intensity immediately after the transition, consistent with a reset into a more content-bearing CEO segment (even though the immediate excerpt remains soft information).

### D. Local Responses vs Session Baseline — Required
- Local Market Evidence Status: **Available.**
  - One local observation: **Quote_Revision_Frequency local_max = 29** within the local window.
  - One deviation-table highlight: **Quote_Revision_Frequency local_mean_minus_baseline_mean = 9.07143** (quote updates per bin).
- Regular-session context: During the **Regular** session, liquidity is generally deeper and response metrics exhibit material dispersion; here, the post-transition window is **temporally aligned with above-baseline quote update activity and higher trade volume** (Trade_Volume local_mean_minus_baseline_mean = **265.736**), while spread is again treated as dispersion-only due to negative values in the series.