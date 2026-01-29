## Change Point at Transcript 116.275s (and Dimension Unavailable)

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **No.**
- If Yes: **Unavailable.**
- If No: **procedural transition.**
- The packet marks a handoff from measurement/disclosure framing (“**A reconciliation between GAAP and non-GAAP measures…**”) to speaker transition (“**I’ll now turn the call over to Hawk.**”), representing a tracked departure from compliance-oriented setup toward the start of substantive prepared remarks.

### B. Soft vs Hard Information Shift — Required
- Label: **Soft→Soft.**
- Justification: **Numeric cue hint** indicates **no numeric cues** both before and after; excerpts are procedural/disclosure statements (“**reconciliation between GAAP and non-GAAP measures…**”; “**turn the call over…**”) rather than quantified performance metrics.

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before = -3e-05; delta_after = -0.00387; slope_pattern = Steepening (higher information injection intensity)**.
- Interpret: **Steepening** is observed, indicating a higher-rate change in cumulative tone around the transition into the CEO segment, consistent with an intensification in accumulated communication momentum at the boundary.

### D. Local Responses vs Session Baseline — Required
- Focus ONLY on the provided Local Evidence and Local-vs-Baseline Deviation.
- Local Market Evidence Status: **Available.**
  - ONE local observation: Within the 17:00:51–17:03:52 ET window, the sample shows **1 trade with Trade_Volume = 2 shares at 17:03:24 ET** (other microstructure fields **Unavailable in provided data** / reported as nan).
  - ONE deviation-table highlight: **Trade_Count local_mean_minus_baseline_mean = -0.853659** (and **Trade_Volume = -135.171** shares).
- After-Hours context: In an **After-Hours** session, low trade counts can still be informative relative to a limited-liquidity baseline; here, the local window is **below the session baseline on average** for trades/volume, while spread/quote-related measures are **Unavailable in provided data** locally (nan), limiting inference to the trade-based deviations only.

---

## Change Point at Transcript 966.091s (and Dimension Unavailable)

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **No.**
- If Yes: **Unavailable.**
- If No: **topic boundary.**
- The packet transitions from operating profitability metrics (“**Operating profit was up 10% year on year…**” and “**Operating margin was 70% in Q2…**”) to a new accounting topic signpost (“**Moving to cash flow.**”), constituting a tracked departure from margin discussion into cash flow reporting.

### B. Soft vs Hard Information Shift — Required
- Label: **Hard→Soft.**
- Justification: The **numeric cue hint** flags **numeric cues before** (e.g., “**up 10% year on year**,” “**Operating margin was 70%… up 360 basis points**”) and **no numeric cue after** (“**Moving to cash flow.**”), indicating a shift from quantified performance disclosure to a transitional framing sentence.

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before = 1.0; delta_after = -0.00038; slope_pattern = Flattening (stabilization/procedural transition)**.
- Interpret: **Flattening** is observed, consistent with a stabilization in accumulated communication intensity at the point where the narrative moves from dense numeric margin reporting to a procedural bridge into the next topic.

### D. Local Responses vs Session Baseline — Required
- Focus ONLY on the provided Local Evidence and Local-vs-Baseline Deviation.
- Local Market Evidence Status: **Available.**
  - ONE local observation: In the 17:14:59–17:17:33 ET window, the local maximum reported trade activity is **Trade_Count = 3 and Trade_Volume = 470 shares at 17:17:21 ET** (spread/quote fields **Unavailable in provided data** / nan).
  - ONE deviation-table highlight: **Trade_Volume local_mean_minus_baseline_mean = -74.5457** shares (with **Trade_Count = -0.603659**).
- After-Hours context: With **After-Hours** liquidity typically thinner and more variable, the local window exhibits **sub-baseline average** trading activity despite a discrete higher-volume bin (470 shares); spread/quote-based response measures remain **Unavailable in provided data** locally (nan), so the comparison is restricted to trade-count/volume deviations.