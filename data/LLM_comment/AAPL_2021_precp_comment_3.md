## Change Point at Transcript 99.394s

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **No.**
- If No: **procedural transition**.
- One-sentence rationale (excerpt-based): The narrative transitions from opening remarks (“**Good afternoon, everyone.**”) into the quarter’s prepared performance summary (“**reporting a very strong quarter**” and “**revenue record of $81.4 billion, up 36%**”), marking the start of metric-heavy disclosure after preliminaries.

### B. Soft vs Hard Information Shift — Required
- Label: **Soft→Hard**.
- Justification: Numeric cue shifts from absent to present (Before_has_numeric_cue=False; After_has_numeric_cue=True), with the after excerpt introducing quantified outcomes: “**$81.4 billion, up 36% from last year**.”

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before=1.0; delta_after=1.0; slope_pattern=Similar slope (stable accumulation intensity)**.
- Interpret: **Stable** accumulated communication intensity; the change point reflects a *recomposition* toward hard metrics rather than a steepening in cumulative tone momentum.

### D. Local Responses vs Session Baseline — Required
- Local Market Evidence Status: **Available**.
  - One local observation: **Quote_Revision_Frequency local_max=109** within the 16:00:43–16:03:41 ET window.
  - One deviation-table highlight: **Trade_Volume local_mean_minus_baseline_mean = +2722.18 shares** (Trade_Volume_M: **+0.00272218**).
- After-Hours context: In an **After-Hours** setting, lower and more irregular trading intensity is typical relative to Regular hours; against that baseline, a positive local trade-volume deviation is notable, while spreads are also expected to be wider (here, **Bid_Ask_Spread** deviation is **+0.350755**, reported as dispersion/level only).

---

## Change Point at Transcript 1281.248s

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **No.**
- If No: **metric disclosure**.
- One-sentence rationale (excerpt-based): The discourse refines balance-sheet structure by moving from a gross liquidity statement (“**194 billion in cash plus marketable securities**”) to capital-structure actions and an implied net position (“**retired 3 billion of term debt… total debt of 122 billion**” → “**Net cash was $72 billion**”), representing a tracked clarification within the financial metrics narrative.

### B. Soft vs Hard Information Shift — Required
- Label: **Hard→Hard**.
- Justification: Numeric cues are present both before and after (Before_has_numeric_cue=True; After_has_numeric_cue=True), and both excerpts are explicitly quantitative (e.g., “**194 billion**” and “**Net cash was $72 billion**”).

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before=2e-05; delta_after=2e-05; slope_pattern=Similar slope (stable accumulation intensity)**.
- Interpret: **Stable/flat** accumulation intensity; the packet signals continuation of detailed financial reporting rather than an acceleration in cumulative tone momentum.

### D. Local Responses vs Session Baseline — Required
- Local Market Evidence Status: **Available**.
  - One local observation: **Quote_Revision_Frequency local_max=70** within the 16:19:58–16:23:07 ET window.
  - One deviation-table highlight: **Order_Book_Imbalance local_mean_minus_baseline_mean = +1.0547** (alongside **Quote_Volatility = +13.4352**).
- After-Hours context: In **After-Hours** trading, order-book and volatility measures can be comparatively noisy under thinner liquidity; the observed positive imbalance deviation and higher quote-volatility deviation are therefore best interpreted relative to the session’s limited-liquidity baseline rather than Regular-hours norms, while **Trade_Count** and **Trade_Volume** are below baseline (deviations **-9.052** and **-5676.05** respectively), consistent with after-hours dispersion.