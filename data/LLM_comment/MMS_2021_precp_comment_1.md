## Change Point at Transcript 392.029s

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **No.**
- If No: classify the shift as one of {topic boundary, procedural transition, risk management pivot, metric disclosure}. **Metric disclosure.**
- One-sentence explanation (excerpt-based): The narrative shifts from qualitative pandemic backfill commentary (“secured COVID response work to backfill…”) to quantified segment performance reporting (“segment increased 11.5% to $155.4 million.”), constituting a tracked departure into numeric disclosure.

### B. Soft vs Hard Information Shift — Required
- Label: **Soft→Hard.**
- Justification: **Numeric cue appears after the change point** (Before_has_numeric_cue=False; After_has_numeric_cue=True), with the after-excerpt explicitly reporting results (“**increased 11.5% to $155.4 million**”).

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before = -2e-05; delta_after = 0.99992; slope_pattern = Steepening (higher information injection intensity).**
- Interpret: **Steepening** is consistent with a sharper upward increment in cumulative tone, aligning with increased information injection through concrete quarterly metrics.

### D. Local Responses vs Session Baseline — Required
- **Local Market Evidence Status: Unavailable.** Reason: **No market rows found within local window [2021-02-04 09:05:24.960000 , 2021-02-04 09:08:12.916000].**
- Local vs Baseline Deviation: **Unavailable (local window missing).**
- Session-baseline context only (Pre-Market): With **limited-liquidity baseline** in Pre-Market, interpretation should emphasize that baseline activity can be sparse; the panel indicates central tendencies such as **Trade_Count median = 1** and **Trade_Volume median = 100 shares**, while spreads can be wide/variable (Bid_Ask_Spread range **[-2, 2]**, dispersion only).


## Change Point at Transcript 547.521s

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **No.**
- If No: classify the shift as one of {topic boundary, procedural transition, risk management pivot, metric disclosure}. **Procedural transition.**
- One-sentence explanation (excerpt-based): The speaker explicitly transitions the presentation sequence from strategic/value framing (“good avenue to create substantial long-term shareholder value”) to financial statement line-items (“Let me turn to cash flow items and the balance sheet.”), marking a tracked structural departure in the flow of disclosure.

### B. Soft vs Hard Information Shift — Required
- Label: **Soft→Hard.**
- Justification: The change point precedes balance-sheet numerics (Before_has_numeric_cue=False; After_has_numeric_cue=True), with the after-excerpt providing hard figures (“**no draws**… and **$132.6 million of cash and cash equivalents**”).

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before = -5e-05; delta_after = -1e-05; slope_pattern = Flattening (stabilization/procedural transition).**
- Interpret: **Flattening** indicates reduced incremental momentum in cumulative tone around the transition, consistent with a stabilizing cadence as the speaker moves into structured cash-flow/balance-sheet items.

### D. Local Responses vs Session Baseline — Required
- **Local Market Evidence Status: Unavailable.** Reason: **No market rows found within local window [2021-02-04 09:08:00.815000 , 2021-02-04 09:10:46.402000].**
- Local vs Baseline Deviation: **Unavailable (local window missing).**
- Session-baseline context only (Pre-Market): Given the **Pre-Market limited-liquidity baseline**, even moderate dispersion can be typical; the session panel shows **Quote_Revision_Frequency** is **Unavailable in provided data** at the local level (baseline has count=14 only) and **Quote_Volatility** baseline ranges up to **45.681**, while trades are often low (Trade_Count mean **2.73**, median **1**), underscoring that baseline microstructure measures can be episodic.


## Change Point at Transcript 901.283s

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **Yes.**
- If Yes: quote the phrase(s) indicating forward-looking guidance.
  - “**Over the course of the administration, we will likely see** a meaningful increase in funding…”
- One-sentence explanation (excerpt-based): The discourse moves from describing already-taken policy actions (“has already taken actions…”) toward probabilistic, forward-looking policy funding expectations (“we will likely see… over the course of the administration”), representing a tracked departure into prospective framing.

### B. Soft vs Hard Information Shift — Required
- Label: **Soft→Soft.**
- Justification: **No numeric cue** on either side (Before_has_numeric_cue=False; After_has_numeric_cue=False), and both excerpts are qualitative policy commentary, with the after-excerpt explicitly using uncertainty language (“**will likely see** a meaningful increase…”).

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before = 0.96823; delta_after = 0.99968; slope_pattern = Similar slope (stable accumulation intensity).**
- Interpret: **Stable** accumulation suggests continuity in tone momentum, with information injection intensity remaining broadly similar despite the shift toward forward-looking language.

### D. Local Responses vs Session Baseline — Required
- **Local Market Evidence Status: Unavailable.** Reason: **No market rows found within local window [2021-02-04 09:13:47.385000 , 2021-02-04 09:17:09.026000].**
- Local vs Baseline Deviation: **Unavailable (local window missing).**
- Session-baseline context only (Pre-Market): In **Pre-Market**, baseline trading can be thin and quote conditions can be noisy; the panel indicates a wide distribution for **Trade_Volume** (max **8294** shares vs median **100**) and **Bid_Ask_Spread** dispersion across **[-2, 2]** (do not interpret sign), consistent with variable liquidity conditions.


## Change Point at Transcript 1009.049s

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **Yes.**
- If Yes: quote the phrase(s) indicating forward-looking guidance.
  - “**Our work has expanded** as government demand has increased into new areas.”
- One-sentence explanation (excerpt-based): The speaker pivots from an “initially” historical description of COVID-related work (“Initially, our COVID work centered around…”) to an expansion-oriented trajectory (“work has expanded… into new areas”), which is tracked as a forward-leaning reframing of operational scope.

### B. Soft vs Hard Information Shift — Required
- Label: **Soft→Soft.**
- Justification: **No numeric cue** on either side (Before_has_numeric_cue=False; After_has_numeric_cue=False); both excerpts remain qualitative, with the after side describing programmatic expansion rather than quantified results.

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before = 0.9992; delta_after = 0.10096; slope_pattern = Flattening (stabilization/procedural transition).**
- Interpret: **Flattening** reflects a marked reduction in incremental cumulative tone momentum after the change point, consistent with a more matter-of-fact elaboration of service areas rather than escalating evaluative language.

### D. Local Responses vs Session Baseline — Required
- **Local Market Evidence Status: Unavailable.** Reason: **No market rows found within local window [2021-02-04 09:15:39.026000 , 2021-02-04 09:18:30.992000].**
- Local vs Baseline Deviation: **Unavailable (local window missing).**
- Session-baseline context only (Pre-Market): With **limited liquidity** typical of Pre-Market, session baselines indicate low central trade intensity (Trade_Count median **1**) alongside occasional bursts (Trade_Count max **26**), and quote-based measures (where available) can vary substantially (Quote_Revision_Frequency max **35**; Quote_Volatility max **45.681**), so any interpretation should remain anchored to baseline dispersion rather than local-window movements (which are unavailable here).