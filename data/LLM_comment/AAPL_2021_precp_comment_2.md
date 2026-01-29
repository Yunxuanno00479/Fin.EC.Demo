## Change Point at Transcript 102.945s

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **No.**
- If No: **procedural transition.**
- This packet marks a tracked departure from opening formalities (“Good afternoon…”) into substantive performance framing and record-setting outcomes (“another strong quarter… set new March quarter records…”), indicating a clear narrative regime change from introductions to results discussion.

### B. Soft vs Hard Information Shift — Required
- Label: **Soft→Hard.**
- Justification: Numeric cue hint indicates **Before_has_numeric_cue=False; After_has_numeric_cue=False** (Unavailable for classification by cue flag), but the after-side excerpt introduces hard performance claims with embedded quantities: “**records for both revenue and earnings… by 54%**,” shifting from non-quantified greeting language to metric-oriented disclosure.

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before=1.0; delta_after=1.0; slope_pattern=Similar slope (stable accumulation intensity).**
- Interpret: **Stable** accumulation suggests continuity in tone momentum despite the structural move into results, consistent with steady information injection rather than an abrupt acceleration.

### D. Local Responses vs Session Baseline — Required
- Local Market Evidence Status: **Available.**
  - One local observation: **Quote_Revision_Frequency local_max=109** in the local window.
  - One deviation-table highlight: **Quote_Revision_Frequency local_mean_minus_baseline_mean = -276.24** (local quote updating lower than the After-Hours baseline mean).
- After-Hours context: Even with lower activity relative to the session baseline (e.g., negative deviations in **Trade_Count** and **Trade_Volume**), such prints can remain informative in a thin-liquidity environment where wider spreads and intermittent quoting are commonly observed; here, the main contrast is subdued quote revision intensity alongside an observed local maximum of 109 within the window.


## Change Point at Transcript 570.819s

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **Yes.**
- If Yes: quote the phrase(s) indicating forward-looking guidance.
  - “**Over the next five years, we will invest $430 billion, creating 20,000 jobs in the process.**”
- This is tracked because the narrative moves from a general commitment statement (“expanded and accelerated our commitment to the U.S.”) into a time-bounded, quantified multi-year investment plan, representing a forward-looking specificity shift in the presentation trajectory.

### B. Soft vs Hard Information Shift — Required
- Label: **Soft→Hard.**
- Justification: Numeric cue hint indicates **Before_has_numeric_cue=False; After_has_numeric_cue=True**, consistent with the after-side quantified guidance: “**$430 billion… 20,000 jobs… over the next five years**.”

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before=-0.87946; delta_after=2e-05; slope_pattern=Flattening (stabilization/procedural transition).**
- Interpret: **Flattening** indicates a reduction in tone-momentum acceleration around the change point, consistent with stabilized accumulated communication intensity even as the content becomes more numerically anchored.

### D. Local Responses vs Session Baseline — Required
- Local Market Evidence Status: **Available.**
  - One local observation: **Quote_Revision_Frequency local_max=95** in the local window.
  - One deviation-table highlight: **Trade_Volume local_mean_minus_baseline_mean = -4840.6** (lower trading volume than the After-Hours session baseline mean).
- After-Hours context: The local window is characterized by below-baseline trading and quote revision intensity (negative deviations for **Trade_Count** and **Quote_Revision_Frequency**), which is not unusual after-hours; the observed local quote revision maximum (95) occurs alongside generally thinner participation relative to the session baseline distribution.


## Change Point at Transcript 770.757s

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **No.**
- If No: **metric disclosure.**
- This packet is tracked as a departure from broad geographic growth characterization (“growth of at least 35%…”) into a specific line-item revenue disclosure (“**Products revenue… $72.7 billion, up 62%**”), tightening the narrative from general performance breadth to a focal quantified metric.

### B. Soft vs Hard Information Shift — Required
- Label: **Hard→Hard.**
- Justification: Numeric cue hint indicates **Before_has_numeric_cue=True; After_has_numeric_cue=False** (Unavailable alignment by cue flag), but both sides contain explicit numeric disclosures in the excerpts/window: before references “**at least 35%**,” and the change-point sentence states “**$72.7 billion, up 62%**,” indicating continued hard information mode.

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before=1.0; delta_after=1.0; slope_pattern=Similar slope (stable accumulation intensity).**
- Interpret: **Stable** intensity suggests the cumulative tone momentum continues at a steady rate through the metric refinement, consistent with ongoing, evenly paced quantitative reporting.

### D. Local Responses vs Session Baseline — Required
- Local Market Evidence Status: **Available.**
  - One local observation: **Quote_Revision_Frequency local_max=90** in the local window.
  - One deviation-table highlight: **Order_Book_Imbalance local_mean_minus_baseline_mean = 0.13591** (more positive imbalance relative to the After-Hours baseline mean).
- After-Hours context: While **Trade_Count** and **Trade_Volume** are below baseline on average in this window, the comparatively more positive order book imbalance is observed alongside the revenue metric disclosure; in after-hours conditions, such imbalance deviations can be notable even when aggregate activity remains below the session’s higher-variance baseline.


## Change Point at Transcript 1299.309s

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **Yes.**
- If Yes: quote the phrase(s) indicating forward-looking guidance.
  - “**Our board has authorized an additional $90 billion for share repurchases.**”
  - “**We’re also raising our dividend by 7% to 22 cents per share, and we continue to plan for annual increases in the dividend going forward.**”
- This packet is tracked because the narrative transitions from confidence framing (“confidence… today and into the future”) into explicit capital return authorizations and an ongoing dividend-growth plan, representing a forward-looking policy commitment in shareholder returns.

### B. Soft vs Hard Information Shift — Required
- Label: **Soft→Hard.**
- Justification: Numeric cue hint indicates **Before_has_numeric_cue=False; After_has_numeric_cue=True**, aligned with quantified authorizations and per-share figures: “**$90 billion**,” “**7%**,” “**22 cents per share**.”

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before=3e-05; delta_after=1.0; slope_pattern=Steepening (higher information injection intensity).**
- Interpret: **Steepening** indicates a marked increase in accumulated communication intensity, consistent with a higher-density injection of salient, decision-relevant numeric commitments at this point in the presentation.

### D. Local Responses vs Session Baseline — Required
- Local Market Evidence Status: **Available.**
  - One local observation: **Quote_Revision_Frequency local_max=128** in the local window.
  - One deviation-table highlight: **Bid_Ask_Spread local_mean_minus_baseline_mean = 0.0157885** (wider spread on average than the After-Hours baseline mean; dispersion only).
- After-Hours context: The window shows wider spreads relative to baseline alongside below-baseline **Trade_Count** and **Trade_Volume** on average; in after-hours trading, such spread widening is commonly observed and can be meaningfully interpreted relative to the thinner-liquidity baseline when it co-occurs with high-salience capital return disclosures.