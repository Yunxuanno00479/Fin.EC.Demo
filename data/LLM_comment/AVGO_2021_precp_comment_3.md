## Change Point at Transcript 114.108s

### A. Structural Inflection (Tracking) — Required
- Past→Future shift? **No.**
- If No: classify the shift as one of {topic boundary, procedural transition, risk management pivot, metric disclosure}.  
  **Procedural transition.**
- One sentence explaining why this is a tracked departure from the prior narrative trajectory, based on excerpts.  
  The packet marks a handoff from IR framing about reporting basis (“**Comments made during today's call will primarily refer to our non-GAAP financial results**”) to CEO turn-taking (“**I'll now turn the call over to Hauk**” / “**Thank you, G.**”), indicating a structural transition into the prepared performance narrative.

### B. Soft vs Hard Information Shift — Required
- Label: **Soft→Soft.**
- Justification: cite numeric cue hint + excerpt evidence.  
  **Numeric cue hint:** Before_has_numeric_cue=False; After_has_numeric_cue=False. **Excerpt evidence:** the content shifts from procedural non-GAAP framing to a brief acknowledgement (“Thank you, G.”), with no numeric disclosure within the packet excerpts.

### C. Accumulated Communication Intensity — Required
- Report slope proxy: **delta_before = -0.00225; delta_after = 0.03818; slope_pattern = Steepening (higher information injection intensity).**
- Interpret: **Steepening** is observed as an increase in accumulated tone momentum immediately after the handoff, consistent with a transition into denser prepared remarks (Accumulated Communication intensity increasing), even though the immediate “after” sentence is itself brief.

### D. Local Responses vs Session Baseline — Required
- Focus ONLY on the provided Local Evidence and Local-vs-Baseline Deviation.
- Local Market Evidence Status is **Available**:
  - **One local observation (local evidence):** Quote_Revision_Frequency local peak check reports **local_max = 1**, and the local stats show **Quote_Revision_Frequency mean = 1** within the event window.
  - **One deviation-table highlight:** **Trade_Volume local_mean_minus_baseline_mean = 38.9453** shares (local above baseline in mean terms).
- **After-Hours context:** Given the after-hours session (where liquidity is thinner and wide spreads are common), the above-baseline local trade volume is notable relative to the session’s lower-activity baseline, while the quote revision rate is below the after-hours baseline (deviation **-4.88**), consistent with limited quote updating in this window.