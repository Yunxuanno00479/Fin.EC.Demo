## Change Point at Transcript 525.007s

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **Yes.**
- If Yes: quote the phrase(s) indicating forward-looking guidance.
  - “**we expect the same through the end of our fiscal year**.”
- One sentence explaining why this is a tracked departure from the prior narrative trajectory, based on excerpts.
  - The narrative moves from a retrospective reminder about prior commentary on glass shortages (“We mentioned on a Q2 call…”) to an explicitly forward-looking continuation statement and then broadens into ongoing quarter-wide operational headwinds (“material shortages continue…”), representing a tracked turn in temporal framing and scope.

### B. Soft vs Hard Information Shift — Required
- Label: **Soft→Soft.**
- Justification: cite numeric cue hint + excerpt evidence.
  - Numeric cue hint indicates **Before_has_numeric_cue=False; After_has_numeric_cue=False**, and the excerpts emphasize qualitative operational constraints (“glass shortages…”, “material shortages… major operational headwind”) rather than quantified metrics.

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before=-0.00032, delta_after=-1.0, slope_pattern=Steepening (higher information injection intensity)**.
- Interpret: **Steepening**, consistent with increased Accumulated Communication intensity, as the cumulative tone shifts more sharply negative while the speaker consolidates multiple constraint statements into a denser headwind-oriented passage.

### D. Local Responses vs Session Baseline — Required
- Focus ONLY on the provided Local Evidence and Local-vs-Baseline Deviation.
- Local Market Evidence Status: **Available.**
  - ONE local observation: Trade activity is intermittently observed, including **2021/09/03 11:08:43 ET: Trade_Count=3 and Trade_Volume=46** within the local window.
  - ONE deviation-table highlight: **Trade_Volume local_mean_minus_baseline_mean = -291.036** (and Trade_Count = -2.95317), indicating local trading activity is below the Regular-session baseline.
- Regular-session context: In **Regular** hours, higher baseline liquidity is typical; therefore, the observed local trade counts/volumes appear **sub-baseline relative to the panel mean**, while spread/quote measures are **Unavailable** locally (nan), limiting microstructure granularity at this change point.


## Change Point at Transcript 603.073s

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **No.**
- If No: classify the shift as one of {topic boundary, procedural transition, risk management pivot, metric disclosure}.
  - **Topic boundary.**
- One sentence explaining why this is a tracked departure from the prior narrative trajectory, based on excerpts.
  - The content pivots from profitability timing language (“However, we do expect to see improved profitability…”) to a new constraint theme centered on labor conditions and staffing needs (“The labor market continues to be tight…”), marking a tracked topic re-anchoring within the presentation.

### B. Soft vs Hard Information Shift — Required
- Label: **Soft→Hard.**
- Justification: cite numeric cue hint + excerpt evidence.
  - Numeric cue hint indicates **Before_has_numeric_cue=False; After_has_numeric_cue=True**, and the after-side introduces a concrete magnitude: “**fill over 400 open positions**,” moving from qualitative profitability commentary to quantified operational disclosure.

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before=-0.4447, delta_after=0.94785, slope_pattern=Steepening (higher information injection intensity)**.
- Interpret: **Steepening**, consistent with heightened Accumulated Communication intensity as the tone momentum shifts sharply in the post-change segment while introducing specific staffing figures and remediation actions (e.g., wage increases).

### D. Local Responses vs Session Baseline — Required
- Focus ONLY on the provided Local Evidence and Local-vs-Baseline Deviation.
- Local Market Evidence Status: **Available.**
  - ONE local observation: The local window shows **persistent minimal trading per bin**, e.g., **2021/09/03 11:10:36 ET: Trade_Count=1 and Trade_Volume=2**.
  - ONE deviation-table highlight: **Trade_Count local_mean_minus_baseline_mean = -3.61983** (and Trade_Volume = -305.902), indicating sub-baseline trading relative to the Regular-session panel.
- Regular-session context: Given **Regular** trading’s typically higher activity, the local response profile appears **muted versus baseline**; additionally, quote/spread fields are largely **Unavailable (nan)** in the local evidence, constraining inference about contemporaneous quoting dynamics at this packet.


## Change Point at Transcript 852.998s

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **No.**
- If No: classify the shift as one of {topic boundary, procedural transition, risk management pivot, metric disclosure}.
  - **Metric disclosure.**
- One sentence explaining why this is a tracked departure from the prior narrative trajectory, based on excerpts.
  - The narrative transitions from a favorable qualitative performance attribution (“solid revenue growth”) to a more granular and comparatively adverse profitability metric statement (“Adjusted EBIT… less than prior year”) and margin-pressure framing (“timing lag… pressure on margin percentage”), constituting a tracked shift in evaluative emphasis.

### B. Soft vs Hard Information Shift — Required
- Label: **Soft→Hard.**
- Justification: cite numeric cue hint + excerpt evidence.
  - While the numeric cue hint for the provided excerpts is **Before_has_numeric_cue=False; After_has_numeric_cue=False**, the immediate post-marker text in the packet contains explicit numeric disclosure: “**Adjusted EBIT… was 2.5 million… 0.6 million less than prior year**,” indicating a move into hard, quantified reporting alongside margin-pressure language.

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before=-0.99989, delta_after=-0.99996, slope_pattern=Similar slope (stable accumulation intensity)**.
- Interpret: **Stable**, suggesting the Accumulated Communication intensity is maintained rather than escalated; the packet continues a consistent cadence of constraint/metric statements without a material change in tone momentum slope.

### D. Local Responses vs Session Baseline — Required
- Focus ONLY on the provided Local Evidence and Local-vs-Baseline Deviation.
- Local Market Evidence Status: **Available.**
  - ONE local observation: The local peak check reports **Quote_Revision_Frequency local_max=9** (with sample evidence at **11:13:00 ET: Quote_Revision_Frequency=9**).
  - ONE deviation-table highlight: **Bid_Ask_Spread local_mean_minus_baseline_mean = 0.112673** (dispersion context only), while **Trade_Volume local_mean_minus_baseline_mean = -136.417** indicates sub-baseline trading volume.
- Regular-session context: In **Regular** hours, both quoting and trading baselines are higher and more variable; here, the packet aligns with **some observed quote updating (local max present)** alongside **below-baseline trade volume**, and spread comparison is reported only via the deviation statistic (local spread observations are present but should be interpreted cautiously given baseline spread mean is negative).


## Change Point at Transcript 899.575s

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **Yes.**
- If Yes: quote the phrase(s) indicating forward-looking guidance.
  - “**when hardwood prices flatten or drop, we can expect to realize margin expansion at that time**.”
- One sentence explaining why this is a tracked departure from the prior narrative trajectory, based on excerpts.
  - The packet moves from a retrospective/adjusted-performance framing (“if we adjust for this inflation… margin expansion…”) into a conditional forward-looking margin realization statement tied to future input-price dynamics, representing a tracked temporal reorientation to prospective outcomes.

### B. Soft vs Hard Information Shift — Required
- Label: **Hard→Soft.**
- Justification: cite numeric cue hint + excerpt evidence.
  - Numeric cue hint indicates **Before_has_numeric_cue=True; After_has_numeric_cue=False**: the “before” includes quantified performance framing (“**approximately 400 basis points**”), while the “after” shifts to conditional qualitative guidance about future margin expansion contingent on hardwood price movements.

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before=1.0, delta_after=1.0, slope_pattern=Similar slope (stable accumulation intensity)**.
- Interpret: **Stable**, indicating steady Accumulated Communication intensity; the forward-looking conditional statement is delivered without an observable change in tone momentum slope proxy.

### D. Local Responses vs Session Baseline — Required
- Focus ONLY on the provided Local Evidence and Local-vs-Baseline Deviation.
- Local Market Evidence Status: **Available.**
  - ONE local observation: A notable trade print appears in the sample at **2021/09/03 11:14:31 ET: Trade_Count=7 and Trade_Volume=503** within the local window.
  - ONE deviation-table highlight: **Bid_Ask_Spread local_mean_minus_baseline_mean = 0.112584** (dispersion context only), and **Trade_Volume local_mean_minus_baseline_mean = -117.102** indicates that, on average, volume remains below the Regular-session baseline despite the localized higher-volume bin.
- Regular-session context: During **Regular** trading, volume and quoting are typically higher with substantial dispersion; this packet shows **episodic trade concentration** alongside **sub-baseline average volume**, and the quote activity indicators are comparatively limited (Quote_Revision_Frequency deviation is negative and local peak check reports **local_max=5**).