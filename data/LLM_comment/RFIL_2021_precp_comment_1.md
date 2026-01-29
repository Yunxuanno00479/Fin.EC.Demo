## Change Point at Transcript 371.144s

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **Yes.**
- Forward-looking guidance phrases (verbatim):
  - “**let's turn the page and talk about where we're heading.**”
  - “**it's a good indicator of future growth**” (in the immediate post-change window).
- One-sentence tracking rationale: The speaker explicitly pivots away from “obvious challenges” toward an outlook-framed narrative that is immediately substantiated with booking/backlog evidence, marking a departure from retrospective framing.

### B. Soft vs Hard Information Shift — Required
- Label: **Soft→Hard.**
- Justification: The pre-change excerpt is qualitative (“turn the page… where we're heading”), while the post-change excerpt introduces numeric disclosure (“**backlog was $7.1 million, up from $6.3 million**”), consistent with the numeric cue hint (Before: False; After: True).

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before=1.0; delta_after=0.61467; slope_pattern=Flattening (stabilization/procedural transition).**
- Interpret: **Flattening** indicates reduced incremental tone momentum after the inflection, consistent with a shift from rhetorical setup into measured metric reporting rather than escalating affective intensity.

### D. Local Responses vs Session Baseline — Required
- Local Market Evidence Status: **Available.**
  - One local observation: At **16:36:36 ET**, **Trade_Count=1** and **Trade_Volume=10** shares are observed within the evidence window.
  - One deviation-table highlight: **Trade_Volume local_mean_minus_baseline_mean = -229.667** (and **Trade_Count = -0.466667**), indicating locally lower trading activity than the after-hours baseline panel average.
- After-Hours context: Given **after-hours** microstructure conditions, sparse trades can still be informational relative to a limited-liquidity baseline; however, here the provided deviations indicate activity that is **below** the session baseline rather than unusually elevated (spread/quote-related fields are largely **Unavailable (nan)** locally, limiting depth of microstructure comparison).

---

## Change Point at Transcript 1086.175s

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **No.**
- If No: classify the shift as one of {topic boundary, procedural transition, risk management pivot, metric disclosure}. **Procedural transition.**
- One-sentence tracking rationale: The inflection coincides with the handoff to the CFO (“turn the call over to Peter…”) and the immediate move into an adverse-condition framing (“challenging sales environment… impact on our revenue”), representing a structural speaker/section transition rather than a forward-looking pivot.

### B. Soft vs Hard Information Shift — Required
- Label: **Soft→Soft.**
- Justification: Both sides are non-numeric—pre-change is procedural greeting/turn-taking (“Thank you, Rob…”), and the post-change continues qualitative commentary (“challenging sales environment… impact on our revenue”), consistent with the numeric cue hint (Before: False; After: False).

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before=-1.0; delta_after=-0.25709; slope_pattern=Flattening (stabilization/procedural transition).**
- Interpret: The **flattening** (less negative incremental change) is consistent with a stabilization around a new speaker’s opening and early contextual setup, rather than a sustained acceleration in cumulative tone momentum.

### D. Local Responses vs Session Baseline — Required
- Local Market Evidence Status: **Available.**
  - One local observation: At **16:48:52 ET**, **Trade_Count=1** and **Trade_Volume=100** shares are recorded.
  - One deviation-table highlight: **Trade_Volume local_mean_minus_baseline_mean = -139.667** (and **Trade_Count = -0.466667**), indicating locally lower trading activity versus the after-hours baseline.
- After-Hours context: In **after-hours** trading, single prints are common and spreads/quote variables are often sparse; in this window, the evidence shows **limited** local trading and **Unavailable (nan)** quote/spread fields, so the comparison relies primarily on the negative trade-activity deviations.

---

## Change Point at Transcript 1236.512s

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **Yes.**
- Forward-looking guidance phrases (verbatim):
  - “**we are starting to see momentum build around new business**”
  - “**pipeline is slowly building**” (implied in the surrounding booking/backlog discussion).
- One-sentence tracking rationale: The narrative shifts from strategic reassurance (“stay the course… opportunity in front of us”) into an outlook-oriented momentum claim that is immediately operationalised via bookings/backlog discussion, constituting a tracked transition into evidence-backed forward trajectory.

### B. Soft vs Hard Information Shift — Required
- Label: **Soft→Hard.**
- Justification: The pre-change excerpt is qualitative positioning (“better positioned… critical… stay the course”), while the post-change introduces numeric backlog disclosure (“**backlog was $7.1 million, up from $6.3 million**”), aligning with the numeric cue hint (Before: False; After: True).

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before=1.0; delta_after=0.70235; slope_pattern=Flattening (stabilization/procedural transition).**
- Interpret: The **flattening** suggests that, despite positive framing, incremental tone accumulation moderates after the inflection as the speaker transitions into concrete metric enumeration (backlog figures; subsequent purchase order and backlog update).

### D. Local Responses vs Session Baseline — Required
- Local Market Evidence Status: **Available.**
  - One local observation: The local peak check reports **Quote_Revision_Frequency local_max=5** (within the 16:49:03–16:52:27 ET window), indicating a moment of heightened quote updating in the local window.
  - One deviation-table highlight: **Quote_Revision_Frequency local_mean_minus_baseline_mean = 0.410256**, i.e., local quoting activity is above the after-hours baseline mean (while **Trade_Volume = -134.167** indicates below-baseline share volume on average).
- After-Hours context: Under **after-hours** conditions, wider spreads and intermittent trades are expected; the local window shows relatively **more active quote updating** than baseline alongside **sub-baseline volume**, a configuration consistent with heightened quotation activity without commensurate trading depth in a thin-liquidity session (spread dispersion is present locally with observed values such as **0.021–0.164**, and the deviation indicates a lower local mean spread than baseline, without invoking causal interpretation).