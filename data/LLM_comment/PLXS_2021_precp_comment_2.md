## Change Point at Transcript 174.673s

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **No.**
- If No: **procedural transition**.
- This packet is tracked because the excerpted language marks a handoff from investor-relations logistics (“**Let me now turn the call over to Todd Kelsey.**”) to the CEO’s opening address (“**Thank you, Sean, and good morning, everyone.**”), indicating a formal boundary between administrative framing and substantive management commentary.

### B. Soft vs Hard Information Shift — Required
- Label: **Soft→Soft**.
- Justification: **Numeric cue hint** indicates no numeric cues on either side (Before_has_numeric_cue=False; After_has_numeric_cue=False), and the excerpts are greeting/turn-taking text rather than quantified performance disclosures.

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before = -0.00013; delta_after = 0.21451; slope_pattern = Steepening (higher information injection intensity)**.
- Interpret: **Steepening** is consistent with a rising rate of tone accumulation immediately after the speaker transition, aligning with an onset of higher-intensity narrative delivery (Accumulated Communication), even though the boundary itself is procedural.

### D. Local Responses vs Session Baseline — Required
- Local Market Evidence Status: **Unavailable** — No market rows found within the local window (08:31:56–08:34:34 ET).
- Discussion (Session Baseline only; Pre-Market context): In the **Pre-Market** session, liquidity is typically limited; therefore, interpretation relies on the baseline panel only. Session-baseline **Bid_Ask_Spread** shows wide dispersion (**range -2 to 0.784**), which is not unusual pre-market. Baseline **Quote_Revision_Frequency** is modest on average (**mean 3.86; max 17**), and **Trade_Count/Trade_Volume** are **Unavailable in provided data.**


## Change Point at Transcript 895.222s

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **No.**
- If No: **risk management pivot**.
- This packet is tracked because the narrative shifts from a quantified shortfall statement (“**Revenue in our aerospace and defense sector was down 7% in the fiscal second quarter.**” / “meaningfully short of our expectations…”) to contextualization of the miss via operational frictions (“**Broad softness across the sector, combined with labor shortages due to COVID quarantines… were the reason for the miss.**”), representing a departure from pure metric reporting toward explanatory/risk-oriented framing.

### B. Soft vs Hard Information Shift — Required
- Label: **Hard→Soft**.
- Justification: The **numeric cue hint** switches from numeric to non-numeric (Before_has_numeric_cue=True; After_has_numeric_cue=False). The “before” excerpt contains a **7%** decline (hard), while the “after” excerpt emphasizes qualitative factors (sector softness, COVID quarantines; soft).

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before = -1.0; delta_after = -1.0; slope_pattern = Similar slope (stable accumulation intensity)**.
- Interpret: **Stable** accumulation intensity suggests the packet reflects a continuation in tonal momentum rather than an acceleration in information injection, even as the content pivots from quantified outcome to qualitative discussion (Accumulated Communication remains steady).

### D. Local Responses vs Session Baseline — Required
- Local Market Evidence Status: **Unavailable** — No market rows found within the local window (08:43:54–08:46:32 ET).
- Discussion (Session Baseline only; Pre-Market context): With **Pre-Market** baseline conditions, quoted liquidity measures often display higher variability. The session baseline indicates **Order_Book_Imbalance** spans **-0.333 to 1** (wide range), and **Quote_Volatility** is variable where available (**min 0; max 75.929; mean 25.625**). **Trade_Count/Trade_Volume** are **Unavailable in provided data**, so response scaling is limited to quote-based baselines.


## Change Point at Transcript 932.518s

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **No.**
- If No: **metric disclosure**.
- This packet is tracked because it moves from a slide-navigation prompt (“**Please advance to slide eight…**”) into a dense quantified wins disclosure (“**We won 42 new manufacturing programs… $284 million in annualized revenue…**”), representing a clear shift from procedural sequencing to metric-heavy reporting.

### B. Soft vs Hard Information Shift — Required
- Label: **Soft→Hard**.
- Justification: The **numeric cue hint** flips to numeric (Before_has_numeric_cue=False; After_has_numeric_cue=True). The “after” excerpt introduces discrete counts and dollar magnitudes (**42** programs; **$284 million** annualized), consistent with hard information.

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before = 0.18565; delta_after = 0.99998; slope_pattern = Steepening (higher information injection intensity)**.
- Interpret: **Steepening** aligns with an intensified injection of quantified content into Accumulated Communication immediately after the change point, consistent with the transition into program wins and magnitude metrics.

### D. Local Responses vs Session Baseline — Required
- Local Market Evidence Status: **Unavailable** — No market rows found within the local window (08:44:25–08:47:13 ET).
- Discussion (Session Baseline only; Pre-Market context): Under **Pre-Market** conditions, even modest quote-update activity may be meaningful relative to limited liquidity, but no local confirmation is available. The baseline shows **Quote_Revision_Frequency** (available for 7 bins) with **median 2** and **max 17**, while **Bid_Ask_Spread** dispersion is broad (**range -2 to 0.784**). **Trade_Count/Trade_Volume** are **Unavailable in provided data.**


## Change Point at Transcript 1459.175s

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **Yes.**
- If Yes: quote the phrase(s) indicating forward-looking guidance.
  - “**We expect to repurchase the balance of the authorized amount on a consistent basis throughout the remainder of fiscal 2021 while taking market conditions into consideration.**”
- This packet is tracked because the narrative transitions from completed buyback execution metrics (“**purchased approximately 349,000 shares… for $29.2 million… $83.39 per share**” and remaining authorization) to an explicit forward-looking capital return plan (expectation for repurchases through the remainder of fiscal 2021).

### B. Soft vs Hard Information Shift — Required
- Label: **Hard→Hard**.
- Justification: The **numeric cue hint** is numeric on both sides (Before_has_numeric_cue=True; After_has_numeric_cue=True). The before excerpt is fully quantified (shares, dollars, average price), and the after excerpt, while plan-oriented, remains anchored in a quantified authorization framework (“balance of the authorized amount,” remainder of fiscal 2021).

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before = -0.00001; delta_after = 0.00003; slope_pattern = Steepening (higher information injection intensity)**.
- Interpret: **Steepening** indicates a modest upward shift in tone-accumulation rate around the pivot into forward-looking repurchase language, consistent with a slight intensification in Accumulated Communication.

### D. Local Responses vs Session Baseline — Required
- Local Market Evidence Status: **Unavailable** — No market rows found within the local window (08:53:16–08:56:17 ET).
- Discussion (Session Baseline only; Pre-Market context): In **Pre-Market**, spreads commonly exhibit dispersion and quote updates may occur intermittently. The baseline **Bid_Ask_Spread** range (**-2 to 0.784**) and **Order_Book_Imbalance** range (**-0.333 to 1**) provide the only available scale context. **Trade_Count/Trade_Volume** are **Unavailable in provided data**, limiting assessment to quoting conditions only.


## Change Point at Transcript 1517.502s

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **No.**
- If No: **metric disclosure**.
- This packet is tracked because the content shifts from balance-sheet leverage detail (“**$38 million borrowed under our $350 million revolving credit facility**”) to a performance/return metric block (“**return on invested capital of 17.3 percent… highest return in four years**”), representing a distinct change from funding/structure metrics to profitability/efficiency outcome metrics.

### B. Soft vs Hard Information Shift — Required
- Label: **Hard→Hard**.
- Justification: The **numeric cue hint** remains numeric on both sides (Before_has_numeric_cue=True; After_has_numeric_cue=True). The before excerpt contains quantified borrowing/capacity figures, while the after excerpt contains quantified ROIC (**17.3%**) and basis-point comparisons (**100 basis points**), both hard metrics.

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before = -0.00001; delta_after = 1.0; slope_pattern = Steepening (higher information injection intensity)**.
- Interpret: The pronounced **steepening** is consistent with a sharper increase in Accumulated Communication intensity at the onset of the ROIC/economic return discussion, where multiple high-salience metrics are introduced in close sequence.

### D. Local Responses vs Session Baseline — Required
- Local Market Evidence Status: **Unavailable** — No market rows found within the local window (08:53:49–08:56:57 ET).
- Discussion (Session Baseline only; Pre-Market context): Given **Pre-Market** limited-liquidity baseline, response interpretation is restricted to baseline ranges. **Quote_Volatility** (where available) spans **0 to 75.929**, indicating potentially large dispersion in quote movements in this session. **Quote_Revision_Frequency** shows **mean 3.86** with **max 17** (limited coverage). **Trade_Count/Trade_Volume** are **Unavailable in provided data.**


## Change Point at Transcript 1598.078s

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **Yes.**
- If Yes: quote the phrase(s) indicating forward-looking guidance.
  - “**Fiscal third quarter gross margin is expected to be in the range of 9.5 to 10 percent.**”
  - (Contextual setup) “**I'll review some additional details… summarized on slide 17.**”
- This packet is tracked because it marks a transition from working-capital/cash-cycle mechanics (“**customer deposits increased…**”) into explicit forward-looking guidance details (gross margin expected range for fiscal third quarter), changing the narrative trajectory from balance-sheet dynamics to near-term outlook parameters.

### B. Soft vs Hard Information Shift — Required
- Label: **Hard→Hard**.
- Justification: The **numeric cue hint** indicates numeric cues on both sides (Before_has_numeric_cue=True; After_has_numeric_cue=True). The before excerpt is quantified (**$20 million** increase in deposits), and the after excerpt provides a quantified guidance range (**9.5 to 10 percent** gross margin), both hard information.

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before = -0.0; delta_after = -0.00002; slope_pattern = Steepening (higher information injection intensity)**.
- Interpret: Despite small deltas, the flagged **steepening** indicates a slight increase in Accumulated Communication intensity coincident with the guidance-detail section, consistent with the introduction of a bounded outlook metric.

### D. Local Responses vs Session Baseline — Required
- Local Market Evidence Status: **Unavailable** — No market rows found within the local window (08:55:27–08:58:19 ET).
- Discussion (Session Baseline only; Pre-Market context): With **Pre-Market** baseline limitations and no local microstructure rows, only session dispersion can be referenced. The baseline **Bid_Ask_Spread** exhibits broad dispersion (**-2 to 0.784**), and **Order_Book_Imbalance** ranges widely (**-0.333 to 1**), consistent with thinner pre-market depth. **Trade_Count/Trade_Volume** are **Unavailable in provided data**, constraining the response characterization to quote-side baselines.