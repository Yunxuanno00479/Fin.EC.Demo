## Change Point at Transcript 173.407s

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **Yes.**
- Forward-looking phrase(s): **“what we're seeing now and expect going forward”**.
- This is tracked because the narrative transitions from introductory/procedural opening (“Good afternoon, everyone.”) to an outline that explicitly frames subsequent remarks around current conditions and forward-looking expectations.

### B. Soft vs Hard Information Shift — Required
- Label: **Soft→Soft.**
- Justification: **Numeric cue hint: Before_has_numeric_cue=False; After_has_numeric_cue=False.** The after-excerpt is agenda/expectations language (“brief review… discuss what we're seeing now and expect going forward”), without quantification.

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before=0.00017; delta_after=-0.0; slope_pattern=Flattening (stabilization/procedural transition).**
- Interpret: **Flattening** is consistent with a stabilization phase in cumulative tone, aligned with procedural framing rather than incremental information injection at this moment.

### D. Local Responses vs Session Baseline — Required
- Local Market Evidence Status: **Available.**
  - One local observation: **Trade_Count=11 and Trade_Volume=2,061 shares at 2021/06/14 16:32:55 ET** within the window.
  - One deviation-table highlight: **Trade_Volume local_mean_minus_baseline_mean = 17.2354** (above baseline mean).
- After-Hours context: In an **After-Hours** session, liquidity is comparatively thin and spreads can be wider; accordingly, **moderate absolute trade volume (and modestly higher-than-baseline averages)** can be meaningful relative to the session baseline, without implying any causal linkage to the transcript shift.


## Change Point at Transcript 398.551s

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **No.**
- If No: classify the shift as one of {topic boundary, procedural transition, risk management pivot, metric disclosure}. **Risk management pivot.**
- This is tracked because the discourse moves from tentative improvement language (“spending is beginning to slowly improve”) to constraints/diagnostics around delayed unlocking and carrier reexamination (“delay… carriers reexamining their deployment plans”), representing a departure toward issue-framing and uncertainty management.

### B. Soft vs Hard Information Shift — Required
- Label: **Soft→Soft.**
- Justification: **Numeric cue hint: Before_has_numeric_cue=False; After_has_numeric_cue=False.** The content remains qualitative (deployment plan reexamination, performance issues, C-band), without numeric disclosure.

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before=-0.12008; delta_after=-0.99145; slope_pattern=Steepening (higher information injection intensity).**
- Interpret: **Steepening** indicates a sharper change in accumulated tone momentum, consistent with a denser insertion of cautionary/constraint-oriented discussion into the accumulated communication path.

### D. Local Responses vs Session Baseline — Required
- Local Market Evidence Status: **Available.**
  - One local observation: **Quote_Revision_Frequency local_max=8** (peak check) in the window.
  - One deviation-table highlight: **Quote_Volatility local_mean_minus_baseline_mean = 2.79273** (elevated versus baseline mean).
- After-Hours context: In **After-Hours** trading, higher dispersion in quote-based measures is commonly observed; here, the **above-baseline quote volatility and modestly higher quote revision frequency** are temporally aligned with the packet’s shift into delay/constraint discussion, while remaining within an environment of limited depth.


## Change Point at Transcript 440.351s

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **Yes.**
- Forward-looking phrase(s): **“ongoing discussions regarding future deployments”**; also aligned with **“So as spend normalizes and increases… we can scale rapidly… positioned to benefit.”**
- This is tracked because the narrative pivots from a generalized positioning/backlog statement to operational forward-looking engagement (active shipping plus future deployment discussions), sharpening the prospective orientation of the small-cell commentary.

### B. Soft vs Hard Information Shift — Required
- Label: **Soft→Soft.**
- Justification: **Numeric cue hint: Before_has_numeric_cue=False; After_has_numeric_cue=False.** The after-excerpt describes activity status and discussions (“actively shipping… ongoing discussions”), without explicit numeric metrics.

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before=1.0; delta_after=2e-05; slope_pattern=Flattening (stabilization/procedural transition).**
- Interpret: **Flattening** suggests that, after a high positive increment just before the change point, the cumulative tone momentum stabilizes; this is consistent with consolidation/continuation language rather than a further ramp in information injection at the immediate boundary.

### D. Local Responses vs Session Baseline — Required
- Local Market Evidence Status: **Available.**
  - One local observation: **Quote_Revision_Frequency local_max=5** (peak check) in the window.
  - One deviation-table highlight: **Quote_Volatility local_mean_minus_baseline_mean = 6.17273** (substantially above baseline mean).
- After-Hours context: Given **After-Hours** baseline conditions (lower liquidity; wider spreads expected), the **notably higher quote-volatility proxy versus baseline** is observed alongside this forward-looking operational update; this should be interpreted as heightened microstructure variability in a thin session rather than as a directional or causal effect.