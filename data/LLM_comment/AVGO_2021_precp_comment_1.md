## Change Point at Transcript 113.045s

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **No.**
- If No: **procedural transition**.
- One-sentence rationale (departure): The packet marks a handoff from IR’s compliance/framing language (e.g., non-GAAP orientation) to the CEO’s opening address, indicating a tracked shift from call mechanics to the start of substantive prepared remarks (“**I’ll now turn the call over to Hawk.**” → “**Thank you…for joining us today.**”).

### B. Soft vs Hard Information Shift — Required
- Label: **Soft→Soft**.
- Justification: **Numeric cue hint** indicates no numeric cues on either side (Before_has_numeric_cue=False; After_has_numeric_cue=False), and the excerpts are ceremonial/procedural rather than metric-bearing (“Comments made…”; “Thank you…”).

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before = -0.00387; delta_after = 0.10428; slope_pattern = Steepening**.
- Interpret: The steepening is consistent with **higher accumulated communication intensity** immediately after the handoff, aligning with the transition into the CEO’s prepared narrative where information content typically becomes denser.

### D. Local Responses vs Session Baseline — Required
- Local Evidence Status: **Available**.
  - One local observation: **Quote_Revision_Frequency local_max = 6** within 17:00:50–17:03:50 ET.
  - One deviation-table highlight: **Quote_Revision_Frequency local_mean_minus_baseline_mean = -3.81707** (below the session mean).
- After-Hours context: In **after-hours**, lower trade activity and intermittent quote updates are common; here, the local window shows **sub-baseline quote revision frequency and lower volatility vs baseline** (Quote_Volatility deviation = **-60.8799**), which is observed alongside the procedural handoff rather than a clearly metric-dense disclosure in this packet.


## Change Point at Transcript 979.155s

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **No.**
- If No: **metric disclosure**.
- One-sentence rationale (departure): The narrative transitions from a general cash-flow/working-capital framing (“**This is up 35% year-over-year as we carefully manage working capital.**”) into a sequence of balance-sheet operating metrics (DSO, then inventory levels), representing a tracked shift into more granular working-capital components (“**Day sales outstanding were 35 days…**” → “**inventory of $952 million…**”).

### B. Soft vs Hard Information Shift — Required
- Label: **Hard→Hard**.
- Justification: **Numeric cue hint** is present on both sides (Before_has_numeric_cue=True; After_has_numeric_cue=True), and the excerpts are explicitly quantitative (e.g., “**35% year-over-year**,” “**35 days…compared to 57 days**,” “**$952 million…decrease of $51 million or 5%**”).

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before = -0.00013; delta_after = -0.52155; slope_pattern = Steepening**.
- Interpret: The steepening indicates **higher accumulated communication intensity**, but with a more negative tone increment after the change point, temporally aligned with the pivot into detailed operational balance-sheet disclosures (DSO/inventory), which can be interpreted as denser “hard” accounting granularity rather than sentiment improvement.

### D. Local Responses vs Session Baseline — Required
- Local Evidence Status: **Available**.
  - One local observation: **Quote_Revision_Frequency local_max = 16** within 17:15:19–17:17:56 ET.
  - One deviation-table highlight: **Quote_Revision_Frequency local_mean_minus_baseline_mean = +5.18293** (above the session mean).
- After-Hours context: Given **after-hours** liquidity conditions, the observed **above-baseline quote revision frequency** and **higher quote volatility vs baseline** (Quote_Volatility deviation = **+52.3051**) are notable relative to the session baseline, and they co-occur with the packet’s tightly packed quantitative working-capital disclosures (DSO and inventory figures). Bid-ask spread and order-book imbalance are **Unavailable in provided data** for the local window (NaN), so interpretation is anchored on quoting/trading deviations only.