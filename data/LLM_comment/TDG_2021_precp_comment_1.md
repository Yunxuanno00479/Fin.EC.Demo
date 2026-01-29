## Change Point at Transcript 552.091s

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **Yes.**
- Forward-looking phrase(s):
  - “**I’ll also comment on fiscal 2021 outlook** and some COVID-19 related topics.”
- This packet is tracked as a departure because it moves from a speaker handoff/procedural close (“Thanks, Nick.”) into an explicitly structured agenda that includes forward-looking outlook content, re-orienting the narrative from transition to planned guidance-oriented discussion.

### B. Soft vs Hard Information Shift — Required
- Label: **Soft→Hard.**
- Justification: Numeric cue hint indicates an increase in hard-information likelihood (**Before_has_numeric_cue=False; After_has_numeric_cue=True**), and the after-excerpt explicitly signals “fiscal 2021 outlook,” which commonly accompanies quantified outlook framing even if the excerpted sentence itself is not numeric.

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before: -0.0; delta_after: -0.0; slope_pattern: Similar slope (stable accumulation intensity)**.
- Interpret: **Stable** accumulation intensity; the change point reflects a **structural re-framing** of content categories rather than a measurable steepening in cumulative tone momentum at this boundary.

### D. Local Responses vs Session Baseline — Required
- Local Market Evidence Status: **Available** (11:08:23–11:10:52 ET).
  - One local observation: **Quote_Revision_Frequency local_max = 9** within the window.
  - One deviation-table highlight: **Bid_Ask_Spread local_mean_minus_baseline_mean = 0.159053** (dispersion/range only).
- Regular-session context: during **Regular** trading hours, higher baseline activity is typical; here, the deviation table indicates **local trading activity measures below baseline on average** (e.g., Trade_Volume mean-minus-baseline is negative), alongside a **positive spread deviation**, which is observed contemporaneously with the transcript’s pivot into structured outlook commentary (no causal attribution).

---

## Change Point at Transcript 819.007s

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **No.**
- If No: classify the shift as one of {topic boundary, procedural transition, risk management pivot, metric disclosure}.  
  - Classification: **risk management pivot**.
- This packet is tracked because it shifts from a descriptive setup about pre-disruption conditions (“Business jet utilization data was pointing to stagnant growth…”) into explicit uncertainty framing (“outlook… remains unpredictable”), marking a clear departure toward risk/visibility constraints in the narrative trajectory.

### B. Soft vs Hard Information Shift — Required
- Label: **Soft→Soft.**
- Justification: Numeric cue hint indicates no numeric emphasis on either side (**Before_has_numeric_cue=False; After_has_numeric_cue=False**); the excerpts are qualitative and uncertainty-focused (e.g., “**outlook… remains unpredictable**,” “**difficult to foresee**”), without new quantitative disclosure at the boundary.

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before: -0.99999; delta_after: -0.99981; slope_pattern: Similar slope (stable accumulation intensity)**.
- Interpret: **Stable** accumulation intensity; despite the thematic pivot toward uncertainty, the cumulative tone momentum does not display a discrete steepening/flattening at the change point under the provided proxy.

### D. Local Responses vs Session Baseline — Required
- Local Market Evidence Status: **Available** (11:12:20–11:15:31 ET).
  - One local observation: **Quote_Revision_Frequency local_max = 6** (single observed bin for this metric in-window).
  - One deviation-table highlight: **Trade_Count local_mean_minus_baseline_mean = -1.23787** (local trading counts below the Regular-session mean).
- Regular-session context: given the **Regular** trading baseline (typically higher and more variable), the deviation table indicates the local window is **below baseline** for multiple activity proxies (e.g., Trade_Volume mean-minus-baseline is negative), while **Bid_Ask_Spread deviation is positive (0.212083; dispersion/range only)**; these response patterns are observed alongside the transcript’s uncertainty/visibility reframing, without implying causality.