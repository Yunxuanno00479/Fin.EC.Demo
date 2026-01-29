## Change Point at Transcript 402.925s (and Dimension Unavailable)

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **No.**
- If No: **procedural transition.**
- This change point is tracked because the narrative departs from CFO seasonality/framing (“*The first quarter of each year is typically the low-water mark…*”) into a handoff (“*I'll now turn the call over to George for his prepared remarks.*” / “*Thanks, Scott.*”), marking a speaker and section-flow boundary rather than a content expansion.

### B. Soft vs Hard Information Shift — Required
- Label: **Soft→Soft.**
- Justification: **Numeric cue hint** indicates no numeric cues on either side (Before_has_numeric_cue=False; After_has_numeric_cue=False), and the excerpts are procedural/qualitative (“*I'll now turn the call over…*” / “*Thanks, Scott.*”) rather than metric disclosure.

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before = -0.00082; delta_after = 0.02875; slope_pattern = Steepening (higher information injection intensity).**
- Interpret: **Steepening**, indicating a mild uptick in accumulated tone momentum immediately after the transition, consistent with a shift into a new speaker’s prepared remarks (higher incremental tone injection, without asserting any market impact).

### D. Local Responses vs Session Baseline — Required
- Local Market Evidence Status: **Available.**
  - One local observation: **Quote_Revision_Frequency local peak check = 19** (local_max=19).
  - One deviation-table highlight: **Trade_Volume local_mean_minus_baseline_mean = -62.3841 shares** (below the Regular-session baseline mean).
- Regular-session context: With **Regular** trading as the baseline (higher typical activity and tighter competition for attention), the local window shows **lower trade activity than baseline alongside slightly higher average spread** (Bid_Ask_Spread deviation **+0.0623**), a configuration that is observed around the procedural handoff and is best interpreted relative to the higher dispersion/variability typical of Regular hours.


## Change Point at Transcript 493.437s (and Dimension Unavailable)

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **No.**
- If No: **topic boundary.**
- This change point is tracked because the narrative shifts from a framing transition into macro “color” (“*Before providing comments on segment results, I will give some additional color…*”) to a substantive macro/COVID discussion (“*As we enter 2021… optimism…*” followed by “*the battle against COVID is far from over…*”), representing a clear repositioning of the narrative focus.

### B. Soft vs Hard Information Shift — Required
- Label: **Hard→Soft.**
- Justification: The **numeric cue hint** signals a numeric/structured setup immediately before (Before_has_numeric_cue=True) but the post-change excerpt is qualitative macro commentary (After_has_numeric_cue=False), e.g., “*optimism and hope…*” and “*battle against COVID is far from over…*,” without explicit numeric anchors in the provided after-excerpt.

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before = 0.84199; delta_after = -0.99998; slope_pattern = Similar slope (stable accumulation intensity).**
- Interpret: **Stable** accumulation intensity at the change point (despite the sign flip in deltas), suggesting the tracked shift is primarily **directional in tone** rather than an increase in the rate of tone accumulation.

### D. Local Responses vs Session Baseline — Required
- Local Market Evidence Status: **Available.**
  - One local observation: **Quote_Revision_Frequency local peak check = 11** (local_max=11).
  - One deviation-table highlight: **Quote_Revision_Frequency local_mean_minus_baseline_mean = -16.0714** (notably below the Regular-session baseline mean).
- Regular-session context: In **Regular** hours, where baseline quote updating and trading are typically higher, the local window is characterized by **sub-baseline quote revision frequency and sub-baseline trading activity** (e.g., Trade_Volume deviation **-108.67**), observed alongside the transition into macro risk narrative; this co-occurrence should be read against the higher normal dispersion of Regular-session microstructure indicators.


## Change Point at Transcript 603.941s (and Dimension Unavailable)

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **Yes.**
- If Yes: quote the phrase(s) indicating forward-looking guidance.
  - “*Although we continue to watch for a pullback in demand due to inflationary pressures, we are not seeing signs of this at this time.*”
- One sentence explaining why this is a tracked departure from the prior narrative trajectory, based on excerpts.  
  - The change point is tracked because the narrative moves from a contemporaneous demand-strength assertion (“*demand continues to be strong across all segments*”) into explicitly forward-looking monitoring/expectations language regarding inflation and demand pullback risk (“*continue to watch… we are not seeing signs… at this time*”).

### B. Soft vs Hard Information Shift — Required
- Label: **Soft→Soft.**
- Justification: **Numeric cue hint** indicates no numeric cues on either side (Before_has_numeric_cue=False; After_has_numeric_cue=False); the shift is qualitative assessment/monitoring language rather than a metric disclosure in the immediate before/after excerpts.

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before = 1.0; delta_after = -0.96926; slope_pattern = Similar slope (stable accumulation intensity).**
- Interpret: **Stable** accumulation intensity, indicating the inflection reflects a **reorientation in message content (forward-looking risk monitoring)** rather than a higher rate of tone accumulation.

### D. Local Responses vs Session Baseline — Required
- Local Market Evidence Status: **Available.**
  - One local observation: **Quote_Revision_Frequency local peak check = 30** (local_max=30).
  - One deviation-table highlight: **Order_Book_Imbalance local_mean_minus_baseline_mean = -0.156323** (local imbalance lower than the Regular-session baseline mean).
- Regular-session context: During **Regular** trading (higher baseline activity; substantial dispersion), the window around this forward-looking demand/risk-monitoring language shows **a local quote-revision peak within the window** (local_max=30) while, on average, **quote revision frequency is below baseline** (deviation **-8.2381**) and **trade counts are modestly below baseline** (Trade_Count deviation **-0.4440**), a pattern observed alongside the narrative’s transition toward conditional demand commentary.