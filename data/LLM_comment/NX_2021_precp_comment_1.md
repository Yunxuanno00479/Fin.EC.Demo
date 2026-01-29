## Change Point at Transcript 84.139s

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **No.**
- If No: classify the shift as one of {topic boundary, procedural transition, risk management pivot, metric disclosure}. **Procedural transition.**
- One sentence explaining why this is a tracked departure from the prior narrative trajectory, based on excerpts.  
  The discourse moves from **disclaimer/non-GAAP reconciliation logistics** (“*please see our earnings release issued yesterday*”) to **formal results delivery** (“*We reported revenue of $230.1 million…*”), constituting a tracked transition into the quantified performance narrative.

### B. Soft vs Hard Information Shift — Required
- Label: **Soft→Hard.**
- Justification: cite numeric cue hint + excerpt evidence.  
  **Numeric cue hint:** Before_has_numeric_cue=False; After_has_numeric_cue=True, consistent with the shift from procedural language to numeric disclosure (“*$230.1 million… increase of 17.1 percent… compared to $196.6 million*”).

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before=-2e-05, delta_after=0.99998, slope_pattern=Steepening (higher information injection intensity).**
- Interpret: **Steepening** indicates a marked increase in accumulated communication intensity, consistent with a transition into dense, metric-heavy reporting.

### D. Local Responses vs Session Baseline — Required
- Focus ONLY on the provided Local Evidence and Local-vs-Baseline Deviation.
- **Local Market Evidence Status: Available.**
  - ONE local observation: **Quote_Revision_Frequency local_max=18** within the local window.
  - ONE deviation-table highlight: **Quote_Volatility is above baseline** (local_mean_minus_baseline_mean = **+6.4177**).
- **Regular session context:** Given higher typical intraday liquidity and tighter quoting norms in Regular trading, the observed **above-baseline quote volatility** is notable relative to the session baseline dispersion, even as other microstructure metrics should be interpreted within Regular-session variability.

---

## Change Point at Transcript 544.524s

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **No.**
- If No: classify the shift as one of {topic boundary, procedural transition, risk management pivot, metric disclosure}. **Risk management pivot.**
- One sentence explaining why this is a tracked departure from the prior narrative trajectory, based on excerpts.  
  The narrative shifts from **supportive demand framing** (“*being favorably impacted…*”) to an explicit **headwind acknowledgement** (“*we… see some challenging headwinds*”), representing a tracked turn toward risk-oriented commentary.

### B. Soft vs Hard Information Shift — Required
- Label: **Soft→Soft.**
- Justification: cite numeric cue hint + excerpt evidence.  
  **Numeric cue hint:** Before_has_numeric_cue=False; After_has_numeric_cue=False, with both sides expressed qualitatively (from discretionary income reallocation tailwinds to “*challenging headwinds*” and “*increased inflationary pressures*”) without numeric metrics.

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before=1.0, delta_after=-0.99954, slope_pattern=Similar slope (stable accumulation intensity).**
- Interpret: **Stable** accumulation intensity suggests that the communication continues at comparable momentum, albeit with a pronounced tonal sign change reflected in the deltas.

### D. Local Responses vs Session Baseline — Required
- Focus ONLY on the provided Local Evidence and Local-vs-Baseline Deviation.
- **Local Market Evidence Status: Available.**
  - ONE local observation: **Quote_Revision_Frequency local_max=46** in the local window.
  - ONE deviation-table highlight: **Quote_Revision_Frequency is above baseline** (local_mean_minus_baseline_mean = **+19.098**).
- **Regular session context:** In Regular trading, a **materially above-baseline quote revision frequency** aligns with heightened contemporaneous quoting activity relative to the higher-liquidity baseline, though the interpretation should remain distributional (i.e., elevated vs typical) rather than causal.

---

## Change Point at Transcript 630.774s

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **No.**
- If No: classify the shift as one of {topic boundary, procedural transition, risk management pivot, metric disclosure}. **Procedural transition.**
- One sentence explaining why this is a tracked departure from the prior narrative trajectory, based on excerpts.  
  The speaker closes a discussion of operational constraints (“*high levels of overtime, extended lead times… customer allocations*”) and then explicitly re-anchors the structure (“*I will now provide my comments on performance by segment*”), marking a tracked transition into segment-level reporting.

### B. Soft vs Hard Information Shift — Required
- Label: **Soft→Soft.**
- Justification: cite numeric cue hint + excerpt evidence.  
  **Numeric cue hint:** Before_has_numeric_cue=False; After_has_numeric_cue=False; the boundary itself is framed procedurally and qualitatively (shifting from operational challenges to the announcement of segment commentary) without immediate numeric disclosure in the change-point excerpts.

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before=-0.99828, delta_after=-1e-05, slope_pattern=Flattening (stabilization/procedural transition).**
- Interpret: **Flattening** corresponds to reduced accumulated communication intensity at the boundary, consistent with a transitional sentence that resets the narrative structure before subsequent detail.

### D. Local Responses vs Session Baseline — Required
- Focus ONLY on the provided Local Evidence and Local-vs-Baseline Deviation.
- **Local Market Evidence Status: Available.**
  - ONE local observation: **Quote_Revision_Frequency local_max=33** during the local window.
  - ONE deviation-table highlight: **Trade_Volume is below baseline** (local_mean_minus_baseline_mean = **-224.392** shares).
- **Regular session context:** Because Regular trading typically features higher baseline volume, the **below-baseline local trading volume** is consistent with relatively muted trade printing in that window, even while spreads and quote activity may still exhibit substantial cross-bin dispersion in Regular-session data.