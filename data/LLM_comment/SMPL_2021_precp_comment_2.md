## Change Point at Transcript 361.555s

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **No.**
- If No: **metric disclosure.**
- The packet departs from the prior narrative trajectory by moving from quantified point-of-sale deterioration (“**retail takeaway was off 5.7%**”) to a qualitatively framed assessment of channel support (“**retailer support…was solid**”), changing the informational modality and emphasis.

### B. Soft vs Hard Information Shift — Required
- Label: **Hard→Soft.**
- Justification: the “before” excerpt contains a clear numeric cue (“**off 5.7%**”), whereas the “after” excerpt is qualitative and attributive (“**retailer support…was solid**”; “**merchandising and display was greater than last year**”) with **After_has_numeric_cue=False**.

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before=0.99803; delta_after=1.0; slope_pattern=Similar slope (stable accumulation intensity).**
- Interpret: **Stable** accumulation suggests a broadly unchanged pace of information injection, notwithstanding the shift from quantified performance to qualitative channel commentary.

### D. Local Responses vs Session Baseline — Required
- Local Market Evidence Status: **Available.**
  - One local observation: **Quote_Revision_Frequency local_max=2** (sample shows **Quote_Revision_Frequency=2** and **Quote_Volatility=3.992** at 08:37:00).
  - One deviation-table highlight: **Quote_Revision_Frequency local_mean_minus_baseline_mean = -13.6364** (below the pre-market baseline mean of 15.6364).
- Pre-Market context: with **limited liquidity baseline** in pre-market trading, the observed local response is most interpretable as **subdued quote updating relative to baseline**, alongside lower quote volatility (deviation **-2.07543**); trade-side fields are **Unavailable in provided data** for this window.

---

## Change Point at Transcript 674.099s

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **No.**
- If No: **procedural transition.**
- The tracked departure is a handoff boundary from CEO outlook language (“**third quarter is off to a fast start**… plans and initiatives…”) to process/navigation (“**Now I’ll turn the call over to Todd**”), re-segmenting the presentation from operational commentary toward financial detail delivery.

### B. Soft vs Hard Information Shift — Required
- Label: **Soft→Soft.**
- Justification: both excerpts are non-numeric (Before_has_numeric_cue=False; After_has_numeric_cue=False) and consist of qualitative framing and protocol (“**fast start**… **executing well**” vs “**turn the call over**”; “**good morning**”), indicating no hard-number disclosure at the inflection itself.

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before=-0.00029; delta_after=0.20308; slope_pattern=Steepening (higher information injection intensity).**
- Interpret: **Steepening** indicates a higher accumulation pace immediately after the transition, consistent with the transcript’s nearby movement into finance-review content (e.g., net sales discussion follows within seconds).

### D. Local Responses vs Session Baseline — Required
- Local Market Evidence Status: **Available.**
  - One local observation: **Quote_Revision_Frequency local_max=2** (sample includes **Quote_Revision_Frequency=2** and **Quote_Volatility=3.886** at 08:42:00).
  - One deviation-table highlight: **Bid_Ask_Spread local_mean_minus_baseline_mean = 0.118777** (local spreads higher than the pre-market baseline mean), while **Quote_Revision_Frequency deviation = -13.6364** remains below baseline.
- Pre-Market context: given **limited liquidity baseline**, wider spreads are commonly observed; here, the local window is characterized by **wider quoted dispersion alongside reduced quote updating** relative to baseline, with trade activity **Unavailable in provided data** in this window.

---

## Change Point at Transcript 1343.223s

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **Yes.**
- If Yes: quote the phrase(s) indicating forward-looking guidance.
  - “**continues to anticipate adjusted EBDA margin expansion**”
  - “**are expected to more than offset**”
- This is tracked as a departure because the packet shifts from a margin-level expectation framed relative to the prior year (“gross margin… **expected to be slightly lower**”) to a forward-looking margin-bridge statement enumerating offsets (synergies, SG&A controls vs inflation/comp/merchandising), altering the structure of guidance from level-setting to mechanism/offset framing.

### B. Soft vs Hard Information Shift — Required
- Label: **Hard→Hard.**
- Justification: both sides are guidance statements embedded in numerically anchored financial discussion (Before_has_numeric_cue=True; After_has_numeric_cue=True), and the immediate “after” excerpt provides explicit numeric guidance (“**EPS…in the range of $1.07 to $1.11 versus $0.91**”), reinforcing a continued hard-information regime around the inflection.

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before=1.0; delta_after=0.00002; slope_pattern=Flattening (stabilization/procedural transition).**
- Interpret: **Flattening** indicates a reduced incremental tone accumulation immediately after the change point, consistent with a stabilization in the accumulation trajectory even as guidance continues.

### D. Local Responses vs Session Baseline — Required
- Local Market Evidence Status: **Available.**
  - One local observation: **Quote_Revision_Frequency local_max=1** (sample includes **Quote_Revision_Frequency=1** at 08:51:00).
  - One deviation-table highlight: **Quote_Revision_Frequency local_mean_minus_baseline_mean = -14.6364** (materially below baseline), while **Bid_Ask_Spread deviation = 0.116777** indicates wider local spreads than baseline.
- Pre-Market context: under **limited liquidity baseline**, the local window shows **muted quote updating relative to baseline** alongside **wider spread levels**, with trade metrics **Unavailable in provided data**; this combination is temporally aligned with the guidance/offset framing but should be interpreted cautiously given sparse local observations.