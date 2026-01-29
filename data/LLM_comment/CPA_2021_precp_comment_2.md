## Change Point at Transcript 242.043s

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **No.**
- If No: **topic boundary.**
- One-sentence why tracked: The narrative pivots from constraint-focused pandemic restrictions (“**Due to the increase in COVID-19 cases… increased travel restrictions…**”) to a contrasting demand/capacity recovery frame (“**markets without significant restrictions… have continued to recover… increase capacity… growing load factors**”), constituting a discrete departure in the direction of the operating environment discussion.

### B. Soft vs Hard Information Shift — Required
- Label: **Hard→Soft.**
- Justification: Numeric cue presence changes from **Before_has_numeric_cue=True** to **After_has_numeric_cue=False**, while the excerpt shifts from constraint/conditions toward qualitative recovery language (“**have continued to recover**”) and operational narrative (“**allowed us to increase capacity…**”) without an explicit numeric value in the after-excerpt.

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before = -0.01002; delta_after = 1.0; slope_pattern = Steepening (higher information injection intensity).**
- Interpret: **Steepening** is observed, consistent with a higher-rate accumulation of tone momentum (cumulative tone) around the recovery-oriented reframing in the Presentation stream (Accumulated Communication).

### D. Local Responses vs Session Baseline — Required
- Local Market Evidence Status: **Available.**
  - One local observation: **Quote_Revision_Frequency local_max = 50** within the local window, indicating an identifiable local peak check in quote update activity.
  - One deviation-table highlight: **Quote_Revision_Frequency local_mean_minus_baseline_mean = +1.32692**, indicating locally higher quote revision frequency relative to the session baseline mean.
- Regular-session context: In **Regular** trading hours, higher baseline activity is typical; accordingly, the observed local uplift in quote revisions is best interpreted in relation to inherently higher dispersion and variability of microstructure measures during this session (and not as an outsized absolute shift).  
- Bid-ask spread note: Local Bid_Ask_Spread exhibits negative values in the local distribution (min = **-2**); per constraint, only **dispersion/range** is noted (range **[-2, 2]**), without interpreting sign.

---

## Change Point at Transcript 670.160s

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **No.**
- If No: **topic boundary.**
- One-sentence why tracked: The speaker transitions from liquidity/balance-sheet quantification (“**$345 million… total liquidity… more than $1.6 billion**”) and debt level positioning (“**$1.6 billion in debt and lease liabilities**”) to fleet actions and composition (“**Turning now to our fleet… sale and delivery of three Embraer 190s… delivered the last remaining…**”), representing a tracked re-segmentation of the Presentation narrative.

### B. Soft vs Hard Information Shift — Required
- Label: **Hard→Hard.**
- Justification: Numeric cue presence remains **True→True**, with continued quantitative disclosure before and after the change point (e.g., “**$1.6 billion in debt and lease liabilities**”; “**sale and delivery of three Embraer 190s**”), indicating sustained reliance on count/amount-based information.

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before = -0.0; delta_after = -0.0; slope_pattern = Similar slope (stable accumulation intensity).**
- Interpret: **Stable** accumulation intensity is observed, suggesting that the change point is predominantly structural (reallocation across reporting topics) rather than an intensification/attenuation in cumulative tone momentum (Accumulated Communication).

### D. Local Responses vs Session Baseline — Required
- Local Market Evidence Status: **Available.**
  - One local observation: **Quote_Revision_Frequency local_max = 102**, matching the upper end of observed quote revision rates in the local window.
  - One deviation-table highlight: **Quote_Revision_Frequency local_mean_minus_baseline_mean = +22.5769**, indicating materially higher quote revision frequency relative to the Regular-session baseline mean.
- Regular-session context: Because this is a **Regular** session with comparatively higher baseline liquidity and quote activity, the salient feature is the *relative* elevation in quote revisions (alongside expected dispersion), while other local deviations (e.g., Trade_Count mean deviation **-1.18306**; Trade_Volume mean deviation **-100.357**) indicate that heightened quote-updating co-occurs with lower trade-side averages in this local window when benchmarked to the session baseline.