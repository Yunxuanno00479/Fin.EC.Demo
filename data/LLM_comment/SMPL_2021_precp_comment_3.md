## Change Point at Transcript 198.078s (and Dimension Unavailable)

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **No.**
- If Yes: **Unavailable.**
- If No: **metric disclosure.**
- The packet marks a tracked departure from narrative conditions (“shopper traffic… improved”) toward a discrete financial performance disclosure (“Adjusted EBITDA… increased 55.6%”), indicating a shift from operating environment commentary to quantified results attribution.

### B. Soft vs Hard Information Shift — Required
- Label: **Soft→Hard.**
- Justification: The “After” excerpt introduces a numeric performance metric (“**increased 55.6%**”) whereas the “Before” excerpt is descriptive and non-quantified (“shopper traffic… improved”); consistent with the numeric cue hint (**Before_has_numeric_cue=False; After_has_numeric_cue=True**).

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before=0.42104; delta_after=1.0; slope_pattern=Steepening (higher information injection intensity).**
- Interpret: **Steepening** is observed, consistent with higher accumulated communication intensity as the speaker transitions into quantified profitability discussion.

### D. Local Responses vs Session Baseline — Required
- Local Market Evidence Status: **Available.**
  - ONE local observation: Within the local window, there is **1 trade** reported at **08:33:42 ET** with **Trade_Volume=30 shares** (other microstructure fields are **Unavailable in provided data** for that timestamp).
  - ONE deviation-table highlight: **Trade_Volume local_mean_minus_baseline_mean = 8.8 shares** (Trade_Volume_M deviation **= 8.8e-06**).
- Session context (Pre-Market): With **limited liquidity baseline** in pre-market conditions, even sparse trading (here, a single-bin observation) can be meaningful relative to typical activity; however, interpretation is bounded by the absence of contemporaneous quote/spread fields in the local evidence (reported as **nan/Unavailable** for those measures).

---

## Change Point at Transcript 598.410s (and Dimension Unavailable)

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **Yes.**
- If Yes: quote the phrase(s) indicating forward-looking guidance.
  - “**We expect that the demand for Quest chips and convention items will remain strong and that supply will be pressured.**”
  - (Contextually adjacent forward-looking phrasing in the packet window: “**In Q4, we anticipate…**”)
- One sentence explaining why this is a tracked departure from the prior narrative trajectory, based on excerpts: The packet transitions from outlook continuity framing (“anticipate… similar to the third quarter”) to an explicit forward-looking demand/supply condition statement (“will remain strong… supply will be pressured”), followed by operational actions (“we have taken actions…”), indicating a new guidance-and-mitigation thread.

### B. Soft vs Hard Information Shift — Required
- Label: **Soft→Soft.**
- Justification: Both excerpts are primarily qualitative expectations and planned actions without numeric anchors (“**We expect… will remain strong… supply will be pressured**” → “**we have taken actions… dialing back trade promotions**”); consistent with numeric cue hint (**Before_has_numeric_cue=False; After_has_numeric_cue=False**).

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before=0.99792; delta_after=-0.00257; slope_pattern=Flattening (stabilization/procedural transition).**
- Interpret: **Flattening** is observed, consistent with reduced accumulated communication intensity as the packet moves from expectation-setting to a more procedural mitigation description.

### D. Local Responses vs Session Baseline — Required
- Local Market Evidence Status: **Unavailable.**
  - Reason: **No market rows found within the local window [2021-07-01 08:38:44.237000 , 2021-07-01 08:41:43.064000].**
  - Therefore, **Local vs Baseline Deviation is Unavailable** in provided data, and no local peak/deviation statements are made.
- Session context (Pre-Market baseline only): The session baseline indicates typically **low trade counts (mean=1 trade/bin; observed count=5 bins)** and **modest volumes (mean=21.2 shares/bin; max=50)** with **limited quote coverage** (e.g., Quote_Volatility count=3). In pre-market conditions, such low-activity baselines are expected, and any contemporaneous responses would be evaluated relative to this constrained-liquidity environment, but **local confirmation is unavailable** for this change point.