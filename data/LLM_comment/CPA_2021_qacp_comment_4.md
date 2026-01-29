## Change Point at Transcript 1509.410s (and Dimension cautious)

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **No.**
- If No: classify the shift as one of {topic boundary, procedural transition, risk management pivot, metric disclosure}. **Topic boundary.**
- Explanation (tracked departure): The dialogue shifts from a COVID-adjusted unit revenue/guidance decomposition (“**two-thirds of the reduction in margin… related to the Omicron… and about a third related to fuel**”) to a distinct customer-product investment question (“**How much would it cost to add Wi‑Fi… and what sort of cost-benefit analysis…**”), representing a clear departure from macro demand and margin attribution into ancillary product economics.

### B. Soft vs Hard Information Shift — Required
- Label: **Soft→Soft.**
- Justification: Both sides are predominantly qualitative in the provided change-point bracketing excerpts, consistent with the numeric cue hint (**Before_has_numeric_cue=False; After_has_numeric_cue=False**). Before: “**too early to make an assessment for the rest of the year**”; After: “**I don’t have a figure for Wi‑Fi… we have not yet seen a compelling case**.”

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before = -0.066; delta_after = -0.069; slope_pattern = Similar slope (stable accumulation intensity).**
- Interpret: For the **cautious** dimension, the negative cumulative-tone increment remains slightly more negative after the change point, but the pattern is **stable**, suggesting no meaningful intensification in caution-related accumulated communication at this boundary (i.e., similar information injection intensity in cautious framing).

### D. Local Responses vs Session Baseline — Required
- Local Market Evidence Status: **Available.**
  - One local observation: The local peak check indicates **Quote_Revision_Frequency local_max = 52** within the window surrounding this packet.
  - One deviation-table highlight: **Quote_Revision_Frequency local_mean_minus_baseline_mean = -13.8013**, indicating quote-revision activity below the session baseline on average in this local window.
- Regular-session context: Because this is a **Regular** market session with generally higher baseline activity, the observed **below-baseline quote revision frequency** is interpreted as comparatively muted microstructure updating relative to the broader session distribution, even as spreads/volumes may vary substantially intraday (no causal interpretation implied).


## Change Point at Transcript 3096.520s (and Dimension cautious)

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **No.**
- If No: classify the shift as one of {topic boundary, procedural transition, risk management pivot, metric disclosure}. **Procedural transition.**
- Explanation (tracked departure): The interaction moves from an acknowledged information gap and generalized qualitative demand commentary (“**we are not prepared to answer… we’ll get back to you… very, very general answer**”) to the formal wrap-up (“**That ends our Q&A session… closing remarks**”), marking a procedural closure that terminates the interactive uncertainty rather than extending the substantive narrative.

### B. Soft vs Hard Information Shift — Required
- Label: **Soft→Hard.**
- Justification: The numeric cue hint indicates a transition to numerically anchored or structured content (**After_has_numeric_cue=True**), consistent with moving into scripted closing remarks (“**This concludes our Q4 and 2021 earnings call**”), whereas the preceding exchange is explicitly non-quantified and generalized (“**very, very general answer**”).

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before = -0.057; delta_after = -0.061; slope_pattern = Similar slope (stable accumulation intensity).**
- Interpret: In the **cautious** dimension, the cumulative-tone increment remains negative with a **stable** pattern, indicating that the closing transition does not coincide with a material steepening or flattening in caution-related accumulated communication intensity.

### D. Local Responses vs Session Baseline — Required
- Local Market Evidence Status: **Available.**
  - One local observation: The local peak check shows **Quote_Revision_Frequency local_max = 154**, the maximum observed in the provided local window.
  - One deviation-table highlight: **Quote_Revision_Frequency local_mean_minus_baseline_mean = 21.434**, indicating higher quote-revision activity than the session baseline on average.
- Regular-session context: In a **Regular** session, elevated quote-revision frequency alongside slightly higher trade-count deviation (**Trade_Count local_mean_minus_baseline_mean = 1.12409**) is interpreted as comparatively stronger contemporaneous updating activity relative to the session baseline, while recognizing that regular-hours liquidity conditions naturally permit substantial dispersion across windows (no causal interpretation implied).


## Change Point at Transcript 2641.480s (and Dimension optimistic)

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **No.**
- If No: classify the shift as one of {topic boundary, procedural transition, risk management pivot, metric disclosure}. **Topic boundary.**
- Explanation (tracked departure): The discussion transitions from forward-horizon capacity normalization framing (“**by the second half of this year, we will be at a pre-pandemic capacity…**”) to a new line of questioning on intra-group cost structure and unit performance (“**to what extent Wingo… [aids] the overall system cost story going forward**”), constituting a tracked departure from market-wide capacity timing to segment-level cost mechanics.

### B. Soft vs Hard Information Shift — Required
- Label: **Soft→Soft.**
- Justification: The numeric cue hint is negative on both sides (**Before_has_numeric_cue=False; After_has_numeric_cue=False**). The “before” segment is qualitative and time-referential (“**second half of this year**”), and the “after” segment is also qualitative/strategic (“**to what extent… cost story going forward**”) without provided numerically anchored disclosures at the boundary.

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before = 0.535; delta_after = 0.48; slope_pattern = Similar slope (stable accumulation intensity).**
- Interpret: For the **optimistic** dimension, cumulative tone remains positive with a modestly lower increment after the change point, but the pattern is assessed as **stable**, suggesting broadly steady optimism-related accumulated communication intensity across this topic transition rather than a sharp re-acceleration.

### D. Local Responses vs Session Baseline — Required
- Local Market Evidence Status: **Available.**
  - One local observation: The local peak check indicates **Quote_Revision_Frequency local_max = 154** in this broader window that includes the change point.
  - One deviation-table highlight: **Trade_Volume local_mean_minus_baseline_mean = 401.622** (and **Trade_Count = 0.320252**), indicating higher local trading volume (and slightly higher trade counts) relative to the session baseline on average.
- Regular-session context: During **Regular** hours, above-baseline trading volume may be notable given the generally higher baseline, yet interpretation should remain relative: the window also shows lower-than-baseline quote volatility (**Quote_Volatility local_mean_minus_baseline_mean = -4.47543**), consistent with a mixed response profile (co-occurrence only).


## Change Point at Transcript 3096.520s (and Dimension clear)

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **No.**
- If No: classify the shift as one of {topic boundary, procedural transition, risk management pivot, metric disclosure}. **Procedural transition.**
- Explanation (tracked departure): The exchange moves from a conversational, partially improvised response acknowledging missing prepared information (“**we are not prepared to answer… very, very general… we’ll get back to you**”) into operator-directed closure (“**That ends our Q&A session… closing remarks**”), representing a tracked transition from interactive problem-solving under uncertainty to structured termination of Q&A.

### B. Soft vs Hard Information Shift — Required
- Label: **Soft→Hard.**
- Justification: The numeric cue hint flags a shift toward structured/numeric content after the boundary (**After_has_numeric_cue=True**). Before: qualitative, non-specific assurances (“**very, very general answer**”); After: scripted closing statement (“**This concludes our Q4 and 2021 earnings call**”) consistent with a more formalized information format.

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before = 0.434; delta_after = 0.621; slope_pattern = Steepening (higher information injection intensity).**
- Interpret: In the **clear** dimension, the cumulative-tone increment **steepens** after the change point, consistent with a higher clarity-related accumulated communication intensity as the call moves into formal closing remarks (i.e., a more structured, unambiguous segment).

### D. Local Responses vs Session Baseline — Required
- Local Market Evidence Status: **Available.**
  - One local observation: The local peak check shows **Quote_Revision_Frequency local_max = 154**.
  - One deviation-table highlight: **Bid_Ask_Spread local_mean_minus_baseline_mean = 0.154256** (dispersion context only), indicating that average spread levels in the local window are above the session baseline.
- Regular-session context: In **Regular** hours, above-baseline spreads can still occur alongside active updating; here, higher quote-revision frequency versus baseline (**+21.434**) co-occurs with wider spread conditions on average, reflecting a locally more “active-but-wider” microstructure state relative to the session baseline (no causal interpretation implied).


## Change Point at Transcript 3096.520s (and Dimension relevant)

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **No.**
- If No: classify the shift as one of {topic boundary, procedural transition, risk management pivot, metric disclosure}. **Procedural transition.**
- Explanation (tracked departure): The conversation exits from an analyst–management interaction featuring acknowledged informational incompleteness (“**we are not prepared to answer… we’ll get back to you**”) into the operator’s formal termination of Q&A (“**That ends our Q&A session**”), which is a tracked departure because it ends relevance-bearing exchange opportunities rather than extending the substantive thread.

### B. Soft vs Hard Information Shift — Required
- Label: **Soft→Hard.**
- Justification: The numeric cue hint indicates an increase in numeric/formal structuring after the boundary (**After_has_numeric_cue=True**). The “before” is explicitly non-quantitative (“**very, very general answer**”), while the “after” is a formal closing statement tied to reporting period completion (“**This concludes our Q4 and 2021 earnings call**”).

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before = 0.493; delta_after = 0.785; slope_pattern = Steepening (higher information injection intensity).**
- Interpret: For the **relevant** dimension, the post-change-point increment **steepens**, consistent with an increase in relevance-oriented accumulated communication intensity as the interaction transitions into a structured closing segment (i.e., higher consolidation/packaging of salient takeaways).

### D. Local Responses vs Session Baseline — Required
- Local Market Evidence Status: **Available.**
  - One local observation: The local peak check indicates **Quote_Revision_Frequency local_max = 154**.
  - One deviation-table highlight: **Trade_Count local_mean_minus_baseline_mean = 1.12409**, indicating a higher average number of trades per bin relative to the session baseline.
- Regular-session context: Under **Regular** trading conditions, a positive trade-count deviation alongside higher quote-revision frequency (**Quote_Revision_Frequency deviation = 21.434**) is consistent with comparatively elevated contemporaneous activity versus the session baseline, while the local average trade volume is below baseline (**Trade_Volume deviation = -144.346**), suggesting that the activity increase is not uniformly mirrored in share volume (co-occurrence only).