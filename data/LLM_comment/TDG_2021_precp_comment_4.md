No Change Point PACKETS were provided for this Presentation (Pre) segment (TDG 2021 Q4). The data context explicitly states that **no change points were detected**, so there are **zero packets** to instantiate under the required per-packet template. As a result, packet-level structural-turn tracking fields (A–D) are **Unavailable in provided data** for this segment.

Given the absence of packet-level Local Evidence / Local-vs-Baseline Deviation blocks, the only admissible market context is the **Regular-session baseline panel**:

- **Market Session context (Regular):** Higher baseline activity is typical, with substantial dispersion in microstructure indicators; interpretation should emphasize variability rather than isolated extremes.
- **Baseline levels (Panel):**
  - **Bid–Ask Spread (USD):** mean **-0.0229**, median **0.005**, range **[-2, 2]** (negatives present; report dispersion/range only).
  - **Order Book Imbalance:** mean **0.0148**, median **0**, range **[-1, 1]**.
  - **Quote Revision Frequency:** mean **20.71**, median **14**, range **[1, 184]**.
  - **Quote Volatility:** mean **111.41**, median **63.37**, range **[0.003, 307.087]**.
  - **Trade Count:** mean **2.34**, median **1**, range **[1, 54]**.
  - **Trade Volume (shares):** mean **73.35**, median **4**, range **[1, 2075]**.

If you intended to include Change Point PACKETS (with transcript seconds, dimension, excerpts, delta_before/delta_after, and any Local Evidence/Deviation tables), please provide those rows; the report can then be generated **packet-by-packet** in the mandated template.