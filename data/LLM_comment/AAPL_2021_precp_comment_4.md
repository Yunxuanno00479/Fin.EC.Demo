## Change Point at Transcript 110.797s

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **Yes.**
- Forward-looking guidance phrase(s): **“Today, much has changed, profoundly so… we are encouraged by progress around the world.”**
- This packet is tracked because the narrative shifts from retrospective framing of prior-year uncertainty (**“A year ago… atmosphere of uncertainty”**) to a present-to-forward orientation that emphasizes improving conditions and organizational posture (**“we are encouraged by progress”**).

### B. Soft vs Hard Information Shift — Required
- Label: **Soft→Soft.**
- Justification: **Numeric cue hint: Before_has_numeric_cue=False; After_has_numeric_cue=False.** The shift is qualitative and sentiment-laden (from “uncertainty” to “encouraged by progress”), without metric disclosure in either excerpt.

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before=1.0; delta_after=0.99997; slope_pattern=Similar slope (stable accumulation intensity).**
- Interpret: **Stable** accumulated communication intensity; the inflection is primarily tonal/reframing rather than an observable acceleration in information injection.

### D. Local Responses vs Session Baseline — Required
- Local Market Evidence Status: **Available.**
  - One local observation: **Quote_Revision_Frequency local peak check shows local_max=152** in the event window.
  - One deviation-table highlight: **Quote_Revision_Frequency local_mean_minus_baseline_mean = -222.563** (local quote-update activity lower than the after-hours baseline mean).
- After-hours context: This window exhibits **sub-baseline quote revision frequency and trade activity** (e.g., **Trade_Count deviation = -18.3447; Trade_Volume deviation = -4441.07**), which is observed alongside **higher quote volatility relative to baseline** (**Quote_Volatility deviation = +15.5529**). In after-hours trading, lower volume is common relative to regular hours, and dispersion in quotes/spreads is typically more pronounced; interpretation should therefore emphasize deviations relative to the session baseline rather than absolute size.


## Change Point at Transcript 304.396s

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **No.**
- If No: classify the shift as one of {topic boundary, procedural transition, risk management pivot, metric disclosure}. **Topic boundary.**
- This packet is tracked because it marks a clear product-focus transition from Apple Watch feature/review commentary (**“Apple Watch Series 7… larger display, faster charging”**) to a new hardware announcement segment centered on MacBook Pro and Apple silicon (**“introduced the… MacBook Pro… M1 Pro and M1 Max”**).

### B. Soft vs Hard Information Shift — Required
- Label: **Hard→Soft.**
- Justification: **Numeric cue hint: Before_has_numeric_cue=True; After_has_numeric_cue=False.** The pre-change statement contains specification-style attribute cues associated with harder product descriptors, whereas the post-change excerpt is framed as an announcement without explicit quantified attributes in the excerpt (with subsequent sentence relying on superlatives such as “most powerful notebooks ever”).

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before=0.00114; delta_after=1.0; slope_pattern=Steepening (higher information injection intensity).**
- Interpret: **Steepening** suggests a higher-rate accumulation of tone momentum around the transition, consistent with a more intensive informational segment introduction (new flagship product line announcement) rather than continuation-level commentary.

### D. Local Responses vs Session Baseline — Required
- Local Market Evidence Status: **Available.**
  - One local observation: **Quote_Revision_Frequency local peak check shows local_max=260**.
  - One deviation-table highlight: **Quote_Volatility local_mean_minus_baseline_mean = +23.1559** (elevated quote volatility relative to after-hours baseline).
- After-hours context: Despite an observed **local peak in quote revisions**, the deviation table indicates **Quote_Revision_Frequency = -147.896** versus baseline (lower mean activity than baseline), alongside **lower trade intensity** (**Trade_Count = -11.8653; Trade_Volume = -5354.1**). In after-hours trading, such mixed patterns—episodic quote activity with comparatively thin trades—are commonly observed, and wide dispersion (including the reported spread range) is consistent with the session’s limited liquidity conditions.


## Change Point at Transcript 988.104s

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **No.**
- If No: classify the shift as one of {topic boundary, procedural transition, risk management pivot, metric disclosure}. **Metric disclosure.**
- This packet is tracked because it transitions from an organizational signpost into segment detail (**“Let me get into more detail for each of our revenue categories.”**) to a numerically anchored iPhone revenue release with performance qualifiers (**“iPhone revenue grew 47%… record of $38.9 billion despite supply constraints”**).

### B. Soft vs Hard Information Shift — Required
- Label: **Soft→Hard.**
- Justification: **Numeric cue hint: Before_has_numeric_cue=False; After_has_numeric_cue=True.** The post-change excerpt introduces explicit accounting metrics and growth rates (**“47%… $38.9 billion”**), replacing a procedural transition sentence.

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before=1.0; delta_after=1.0; slope_pattern=Similar slope (stable accumulation intensity).**
- Interpret: **Stable** accumulation intensity; the tracked change is driven by a shift in content type (procedural → quantified performance) more than a change in cumulative tone slope.

### D. Local Responses vs Session Baseline — Required
- Local Market Evidence Status: **Available.**
  - One local observation: **Quote_Revision_Frequency local peak check shows local_max=36**.
  - One deviation-table highlight: **Order_Book_Imbalance local_mean_minus_baseline_mean = +0.460434** (more positive imbalance than baseline on average within the window).
- After-hours context: The local window shows **sub-baseline quoting and trading intensity** (**Quote_Revision_Frequency = -279.563; Trade_Count = -19.0335; Trade_Volume = -6556.63**) alongside **wider spreads relative to baseline mean** (**Bid_Ask_Spread deviation = +0.0170362**). In after-hours settings, lower trade/quote counts can still be meaningful relative to the session baseline, and wider spreads are expected; emphasis is therefore on the co-occurrence of metric disclosure with comparatively thin liquidity and a more positive average imbalance.


## Change Point at Transcript 1357.173s

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **No.**
- If No: classify the shift as one of {topic boundary, procedural transition, risk management pivot, metric disclosure}. **Metric disclosure.**
- This packet is tracked because it moves from balance sheet positioning and capital structure context (**“net cash was $66 billion… goal of net cash neutral over time”**) to a more granular capital return breakdown (**“return $24 billion… included $3.6 billion… and 20 billion… repurchases… 137 million… shares”**), indicating a step-up in specificity within the same capital allocation theme.

### B. Soft vs Hard Information Shift — Required
- Label: **Hard→Hard.**
- Justification: **Numeric cue hint: Before_has_numeric_cue=True; After_has_numeric_cue=True.** Both sides are numerically dense (e.g., **“$66 billion”** before; **“$24 billion… $3.6 billion… 20 billion… 137 million”** after), reflecting continued hard-information delivery.

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before=1.0; delta_after=1e-05; slope_pattern=Flattening (stabilization/procedural transition).**
- Interpret: **Flattening** indicates reduced incremental tone accumulation immediately after the change point, consistent with a stabilization in communication momentum even as numeric detail continues (i.e., less tonal acceleration during the granular breakdown).

### D. Local Responses vs Session Baseline — Required
- Local Market Evidence Status: **Available.**
  - One local observation: **Quote_Revision_Frequency local peak check shows local_max=95**.
  - One deviation-table highlight: **Bid_Ask_Spread local_mean_minus_baseline_mean = +0.265536** (spread level higher than baseline mean; interpret as wider dispersion, without sign-based inference).
- After-hours context: The window shows **lower trade intensity than baseline** (**Trade_Count = -18.7573; Trade_Volume = -6236.73**) alongside **higher quote volatility** (**Quote_Volatility = +17.8609**) and **wider spread dispersion** versus baseline. In after-hours markets, such combinations are often observed alongside limited liquidity conditions; here they are temporally aligned with detailed shareholder return figures rather than broad narrative commentary.