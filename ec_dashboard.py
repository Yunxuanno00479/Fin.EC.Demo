import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, State, ctx, ALL
import pandas as pd
from pathlib import Path
import plotly.graph_objs as go

# ============================================================
# 0. Config & Paths
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
YEAR_DEFAULT = 2021

# Quote / Trade
QUOTE_COLS = [
    "Bid_Ask_Spread",
    "Order_Book_Imbalance",
    "Quote_Revision_Frequency",
    "Quote_Volatility",
]
TRADE_COLS = [
    "trade_count",
    "trade_volume",
    "trade_vwap",
]

# Quarter buttons style
STYLE_ACTIVE = {
    "backgroundColor": "#009688",
    "color": "white",
    "fontWeight": "600",
}
STYLE_INACTIVE = {
    "backgroundColor": "#ffffff",
    "color": "#4b5563",
    "fontWeight": "500",
}

# Key Indicators line colors
INDICATOR_COLORS = {
    "Bid Ask Spread":          "#3B5FA5",
    "Order Book Imbalance":    "#C06A2C",
    "Quote Revision Frequency":"#4C9A62",
    "Quote Volatility":        "#7A68B3",
    "trade count":             "#B45309",
    "trade volume":            "#2F7F7A",
    "trade vwap":              "#4B8FA8",
}


# Q&A cumulative line colors
QA_DIM_COLORS = {
    "assertive": "#3B5FA5",
    "cautious":  "#4C9A62",
    "optimistic":"#7A68B3",
    "specific":  "#5C6F7B",
    "clear":     "#4FA3BF",
    "relevant":  "#9A9A9A",
}

# ============================================================
# Shared plot styling
# ============================================================

SHARED_PLOT_MARGIN = dict(l=44, r=44, t=40, b=36)

AXIS_TICK_FONT = dict(size=10, color="#374151")
AXIS_TITLE_FONT = dict(size=11, color="#6b7280")

SHARED_XAXIS_STYLE = dict(
    title=dict(text="Timestamp", font=AXIS_TITLE_FONT, standoff=6),
    tickfont=AXIS_TICK_FONT,
    ticks="outside",
    ticklen=4,
    tickwidth=1,
    showline=True,
    linewidth=1,
    linecolor="#9ca3af",
    zeroline=False,
    mirror=False,
)

# ============================================================
# 1. Load basic data
# ============================================================

df_companies = pd.read_csv(DATA_DIR / "companies_list.csv")
COMPANY_DATA = df_companies.to_dict("records")
DROPDOWN_OPTIONS = [
    {"label": item["name_tic"], "value": item["tic"]} for item in COMPANY_DATA
]

# ============================================================
# 2. Data loader helpers
# ============================================================


def load_pre_df(tic: str, year: int, quarter: int) -> pd.DataFrame:
    """Load presentation data. Normalizes columns for backward compatibility."""
    path = DATA_DIR / "Pre_finbert_tone" / f"{tic}_{year}_pre.csv"
    if not path.exists():
        return pd.DataFrame()

    df = pd.read_csv(path).copy()

    # Quarter filter
    if "quarter" in df.columns:
        df = df[df["quarter"] == quarter].copy()
    if df.empty:
        return df

    # Section ID
    if "section_id" in df.columns:
        df["section_id"] = df["section_id"].astype(int)
    elif "sent_section_id" in df.columns:
        df["section_id"] = df["sent_section_id"].astype(int)
    else:
        df["section_id"] = range(1, len(df) + 1)

    # Timestamp (seconds)
    if "timestamp_p" in df.columns:
        df["timestamp_sec"] = df["timestamp_p"].astype(float)
    elif "timestamp_sec" in df.columns:
        df["timestamp_sec"] = df["timestamp_sec"].astype(float)
    else:
        df["timestamp_sec"] = range(len(df))

    # Text
    if "presentation_text" in df.columns:
        df["display_text"] = df["presentation_text"].fillna("")
    elif "text" in df.columns:
        df["display_text"] = df["text"].fillna("")
    else:
        df["display_text"] = ""

    # Cumulative tone
    if "finberttone_cumulative_tone" in df.columns:
        df["cumulative_tone"] = pd.to_numeric(df["finberttone_cumulative_tone"], errors="coerce")
    elif "cumulative_tone" in df.columns:
        df["cumulative_tone"] = pd.to_numeric(df["cumulative_tone"], errors="coerce")
    else:
        df["cumulative_tone"] = float("nan")

    # Expected value tone
    if "finberttone_expected_value" in df.columns:
        df["tone_expected_value"] = pd.to_numeric(df["finberttone_expected_value"], errors="coerce")
    elif "tone_expected_value" in df.columns:
        df["tone_expected_value"] = pd.to_numeric(df["tone_expected_value"], errors="coerce")
    else:
        df["tone_expected_value"] = float("nan")

    # Change point
    change_point_cols = [c for c in df.columns if c.endswith("_change_point")]
    if change_point_cols:
        cp_col = "finberttone_change_point" if "finberttone_change_point" in change_point_cols else change_point_cols[0]
        df[cp_col] = df[cp_col].fillna(0).astype(int)
        df["is_changepoint"] = (df[cp_col] == 1).astype(int)
    return df


def load_qa_df(tic: str, year: int, quarter: int) -> pd.DataFrame:
    """Load Q&A data. Normalizes columns for backward compatibility."""
    path = DATA_DIR / "QA_subjectiveqa" / f"{tic}_{year}_qa.csv"
    if not path.exists():
        return pd.DataFrame()

    df = pd.read_csv(path).copy()

    # Quarter filter
    if "quarter" in df.columns:
        df = df[df["quarter"] == quarter].copy()
    if df.empty:
        return df

    # Section ID
    if "QA_Index" in df.columns:
        df["section_id"] = df["QA_Index"].astype(int)
    elif "section_id" in df.columns:
        df["section_id"] = df["section_id"].astype(int)
    elif "sent_section_id" in df.columns:
        df["section_id"] = df["sent_section_id"].astype(int)
    else:
        df["section_id"] = range(1, len(df) + 1)

    # Timestamps
    if "Q_Timestamp" in df.columns:
        df["timestamp_Q"] = pd.to_numeric(df["Q_Timestamp"], errors="coerce")
        df["timestamp_sec"] = df["timestamp_Q"]
    else:
        if "timestamp_Q" in df.columns:
            df["timestamp_Q"] = pd.to_numeric(df["timestamp_Q"], errors="coerce")
        if "timestamp_A" in df.columns:
            df["timestamp_A"] = pd.to_numeric(df["timestamp_A"], errors="coerce")
        df["timestamp_sec"] = df["timestamp_Q"] if "timestamp_Q" in df.columns else range(len(df))

    # Text
    if "Question" in df.columns:
        df["question_text"] = df["Question"].fillna("")
    else:
        df["question_text"] = df.get("question_text", "").fillna("") if isinstance(df.get("question_text", ""), pd.Series) else df.get("question_text", "")

    if "Answer" in df.columns:
        df["answer_text"] = df["Answer"].fillna("")
    else:
        df["answer_text"] = df.get("answer_text", "").fillna("") if isinstance(df.get("answer_text", ""), pd.Series) else df.get("answer_text", "")

    df["display_text"] = "Q: " + df["question_text"].astype(str) + "\nA: " + df["answer_text"].astype(str)

    # Normalize QA dimension columns
    dims = ["assertive", "cautious", "optimistic", "specific", "clear", "relevant"]
    for d in dims:
        # Cumulative
        if f"{d}_cumulative_tone" in df.columns:
            df[f"qa_{d}_cumulative"] = pd.to_numeric(df[f"{d}_cumulative_tone"], errors="coerce")
        elif f"qa_{d}_cumulative" in df.columns:
            df[f"qa_{d}_cumulative"] = pd.to_numeric(df[f"qa_{d}_cumulative"], errors="coerce")
        else:
            df[f"qa_{d}_cumulative"] = float("nan")

        # Expected value
        if f"{d}_expected_value" in df.columns:
            df[f"qa_{d}_expected_value"] = pd.to_numeric(df[f"{d}_expected_value"], errors="coerce")
        elif f"qa_{d}_expected_value" in df.columns:
            df[f"qa_{d}_expected_value"] = pd.to_numeric(df[f"qa_{d}_expected_value"], errors="coerce")
        else:
            df[f"qa_{d}_expected_value"] = float("nan")

        # Change point
        if f"{d}_change_point" in df.columns:
            df[f"qa_{d}_change_point"] = df[f"{d}_change_point"].fillna(0).astype(int)
        elif f"qa_{d}_change_point" in df.columns:
            df[f"qa_{d}_change_point"] = df[f"qa_{d}_change_point"].fillna(0).astype(int)
        else:
            df[f"qa_{d}_change_point"] = 0

    # Aggregate change point flag
    cp_cols_new = [c for c in df.columns if c.endswith("_change_point")]

    if cp_cols_new:
        df["is_changepoint"] = df[cp_cols_new].fillna(0).astype(int).eq(1).any(axis=1).astype(int)
    else:
        df["is_changepoint"] = 0

    return df


def load_panel_df(tic: str, year: int, quarter: int) -> pd.DataFrame:
    """Load quote/trade panel data."""
    path = DATA_DIR / "Panel_quote_trade" / f"{tic}_{year}_panel.csv"
    if not path.exists():
        return pd.DataFrame()

    df = pd.read_csv(path).copy()

    # Year / quarter filter
    if "year" in df.columns:
        df = df[df["year"] == year]
    if "quarter" in df.columns:
        df = df[df["quarter"] == quarter]
    if df.empty:
        return df

    # Timestamp processing: prefer timestamp_et_full
    if "timestamp_et_full" in df.columns:
        df["timestamp_et_full"] = pd.to_datetime(df["timestamp_et_full"], errors="coerce")
        df = df.dropna(subset=["timestamp_et_full"])
        if df.empty:
            return df
        base = df["timestamp_et_full"].min()
        df["timestamp_sec"] = (df["timestamp_et_full"] - base).dt.total_seconds()
        return df

    # Fallback: parse Timestamp_UTC
    if "Timestamp_UTC" in df.columns:
        def parse_offset_to_sec(s: str) -> float:
            s = str(s).strip()
            if not s:
                return 0.0
            try:
                parts = s.split(":")
                if len(parts) == 2:
                    m, sec = parts
                    return int(m) * 60 + float(sec)
                elif len(parts) == 1:
                    return float(parts[0])
                else:
                    h, m, sec = parts[-3:]
                    return int(h) * 3600 + int(m) * 60 + float(sec)
            except Exception:
                return 0.0

        df["timestamp_sec"] = df["Timestamp_UTC"].astype(str).apply(parse_offset_to_sec)
        return df

    # Final fallback
    df["timestamp_sec"] = range(len(df))
    return df


def load_calendar_row(tic: str, year: int, quarter: int):
    """Load calendar row for a given company/year/quarter."""
    path = DATA_DIR / "ec_calendar.csv"
    if not path.exists():
        return None

    df = pd.read_csv(path)
    row = df[(df["tic"] == tic) & (df["year"] == year) & (df["quarter"] == quarter)].head(1)

    if row.empty:
        return None
    return row.iloc[0]
def load_comment_md(tic: str, year: int, quarter: int):
    """Load Markdown comment for a given company/year/quarter."""
    md_path = DATA_DIR / "LLM_comment" / f"{tic}_{year}_comment_{quarter}.md"
    if not md_path.exists():
        return ""

    try:
        return md_path.read_text(encoding="utf-8")
    except Exception:
        return "(Unable to read LLM comment file)"


def _df_from_store(data):
    """Convert store data to DataFrame."""
    return pd.DataFrame(data) if data else pd.DataFrame()


def build_global_df(pre_df: pd.DataFrame, qa_df: pd.DataFrame) -> pd.DataFrame:
    """Build global DataFrame combining pre and qa timestamps."""
    p = pre_df[["section_id", "timestamp_sec"]].copy()
    q = qa_df[["section_id", "timestamp_sec"]].copy()
    p["mode"] = "pre"
    q["mode"] = "qa"
    return pd.concat([p, q], ignore_index=True)


def choose_default_changepoint(df: pd.DataFrame) -> int:
    """Choose default changepoint section ID."""
    if df is None or df.empty:
        return 0
    if "is_changepoint" in df.columns:
        idx = df.index[df["is_changepoint"] == 1]
        if len(idx) > 0:
            return int(df.loc[idx[0], "section_id"])
    return int(df.iloc[0]["section_id"])


def find_nearest_point(global_df: pd.DataFrame, timestamp: float):
    """Find nearest point in global_df to given timestamp."""
    if global_df.empty:
        return "pre", 0
    idx = (global_df["timestamp_sec"] - timestamp).abs().idxmin()
    row = global_df.loc[idx]
    return row["mode"], int(row["section_id"])


def find_nearest_section_in_mode(global_df: pd.DataFrame, x: float, mode: str) -> int:
    """Find nearest section_id by timestamp within a fixed mode (pre/qa)."""
    if global_df is None or global_df.empty:
        return 0
    dfm = global_df[global_df.get("mode", "").astype(str) == str(mode)].copy()
    if dfm.empty:
        # fallback: use all
        dfm = global_df
    try:
        x = float(x)
    except Exception:
        return int(dfm.iloc[0]["section_id"]) if "section_id" in dfm.columns else 0
    idx = (dfm["timestamp_sec"] - x).abs().idxmin()
    try:
        return int(dfm.loc[idx, "section_id"])
    except Exception:
        return int(dfm.iloc[0]["section_id"]) if "section_id" in dfm.columns else 0


# ============================================================
# 3. Figures
# ============================================================


def build_tone_figure(pre_df, qa_df, active_mode, active_section_id, segment_range=None, legend_state=None):
    """Build cumulative tone figure with dual y-axis for presentation."""
    fig = go.Figure()
    legend_state = legend_state or {}
    def _vis(name: str):
        v = legend_state.get(name)
        if v is None:
            return None
        return "legendonly" if v is False else True

    show_pre = (active_mode == "pre")
    show_qa = (active_mode == "qa")

    # Presentation: dual y-axis
    if show_pre and not pre_df.empty:
        # Left y-axis: tone expected value
        if "tone_expected_value" in pre_df.columns and pre_df["tone_expected_value"].notna().any():
            fig.add_trace(
                go.Scatter(
                    x=pre_df["timestamp_sec"],
                    y=pre_df["tone_expected_value"],
                    mode="lines",
                    name="tone expected value",
                    visible=_vis("tone expected value"),
                    line=dict(shape="linear", width=1, color="#c7c7c7"),
                    yaxis="y",
                    showlegend=False,
                    hovertemplate="t=%{x:.0f}s<br>tone expected value=%{y:.3f}<extra></extra>",
                )
            )

        # Right y-axis: cumulative tone
        fig.add_trace(
            go.Scatter(
                x=pre_df["timestamp_sec"],
                y=pre_df["cumulative_tone"],
                mode="lines",
                name="Presentation",
                visible=_vis("Presentation"),
                line=dict(shape="linear", width=2.5, color="#2563eb"),
                yaxis="y2",
                hovertemplate=(
                    "t=%{x:.0f}s<br>cumulative tone=%{y:.3f}"
                    + ("<br>label=%{customdata[0]}<br>score=%{customdata[1]:.3f}"
                       if set(["tone_label", "tone_score"]).issubset(pre_df.columns) else "")
                    + "<extra></extra>"
                ),
                customdata=pre_df[["tone_label", "tone_score"]].values
                if set(["tone_label", "tone_score"]).issubset(pre_df.columns) else None,
            )
        )

        # Change points
        if "is_changepoint" in pre_df.columns:
            m = pre_df["is_changepoint"].fillna(0).astype(int) == 1
            if m.any():
                fig.add_trace(
                    go.Scatter(
                        x=pre_df.loc[m, "timestamp_sec"],
                        y=pre_df.loc[m, "cumulative_tone"],
                        mode="markers",
                        name="Change Point",
                        visible=_vis("Change Point"),
                        hovertemplate=(
                            "t=%{x:.0f}s<br>cumulative tone=%{y:.3f}"
                            + ("<br>label=%{customdata[0]}<br>score=%{customdata[1]:.3f}"
                                if set(["tone_label", "tone_score"]).issubset(pre_df.columns) else "")
                            + "<extra></extra>"
                        ),
                        marker=dict(color="#d62728", size=6, symbol="circle"),
                        yaxis="y2",
                        showlegend=True,
                    )
                )
                for ts in pre_df.loc[m, "timestamp_sec"]:
                    fig.add_shape(
                        type="line", x0=float(ts), x1=float(ts), y0=0, y1=1,
                        xref="x", yref="paper",
                        line=dict(color="#d62728", width=1.5, dash="dot"),
                    )

    # Q&A: 6 dimensions
    if show_qa and not qa_df.empty:
        dims = [
            ("assertive", "qa_assertive_cumulative", "qa_assertive_expected_value", "qa_assertive_change_point"),
            ("cautious", "qa_cautious_cumulative", "qa_cautious_expected_value", "qa_cautious_change_point"),
            ("optimistic", "qa_optimistic_cumulative", "qa_optimistic_expected_value", "qa_optimistic_change_point"),
            ("specific", "qa_specific_cumulative", "qa_specific_expected_value", "qa_specific_change_point"),
            ("clear", "qa_clear_cumulative", "qa_clear_expected_value", "qa_clear_change_point"),
            ("relevant", "qa_relevant_cumulative", "qa_relevant_expected_value", "qa_relevant_change_point"),
        ]

        for name, cum_col, ev_col, cp_col in dims:
            if cum_col not in qa_df.columns:
                continue

            color = QA_DIM_COLORS.get(name, None)
            customdata = (qa_df[[ev_col]].values
                          if ev_col in qa_df.columns and qa_df[ev_col].notna().any()
                          else None)

            fig.add_trace(
                go.Scatter(
                    x=qa_df["timestamp_sec"],
                    y=qa_df[cum_col],
                    mode="lines+markers",
                    name=name.capitalize(),
                    visible=_vis(name.capitalize()),
                    legendgroup=name,
                    legendgrouptitle_text=None,
                    line=dict(width=2, color=color),
                    marker=dict(size=5, color=color),
                    customdata=customdata,
                    hovertemplate=(
                        f"t=%{{x:.0f}}s<br>{name} cumulative tone=%{{y:.3f}}"
                        + (f"<br>{name} expected value=%{{customdata[0]:.3f}}" if customdata is not None else "")
                        + "<extra></extra>"
                    ),
                )
            )

            # Per-dimension change points
            if cp_col in qa_df.columns:
                m_cp = qa_df[cp_col].fillna(0).astype(int) == 1
                if m_cp.any():
                    fig.add_trace(
                        go.Scatter(
                            x=qa_df.loc[m_cp, "timestamp_sec"],
                            y=qa_df.loc[m_cp, cum_col],
                            mode="markers",
                            name=f"{name.capitalize()} CP",
                            visible=_vis(name.capitalize()),
                            legendgroup=name,
                            marker=dict(color=color, size=10, symbol="triangle-down", line=dict(color="white", width=1)),
                            showlegend=False,
                        )
                    )
                    # Per-dimension change point vertical lines (full-height; toggled with legend)
                    dim_vis = _vis(name.capitalize())
                    if dim_vis != "legendonly":
                        for ts in qa_df.loc[m_cp, "timestamp_sec"].astype(float).tolist():
                            fig.add_shape(
                                type="line", x0=float(ts), x1=float(ts), y0=0, y1=1,
                                xref="x", yref="paper",
                                line=dict(color=color, width=1.5, dash="dot"),
                            )


    # Active vertical line
    df = pre_df if active_mode == "pre" else qa_df
    if not df.empty:
        r = df[df["section_id"] == active_section_id]
        if not r.empty:
            ts = float(r.iloc[0]["timestamp_sec"])
            fig.add_shape(
                type="line", x0=ts, x1=ts, y0=0, y1=1,
                xref="x", yref="paper",
                line=dict(color="black", width=2),
            )

    # X-axis range
    if segment_range is not None:
        x_min, x_max = segment_range
        if x_min is not None and x_max is not None and x_min < x_max:
            span = x_max - x_min
            dtick = max(span / 5.0, 1.0)
            fig.update_xaxes(range=[x_min, x_max], tickmode="linear", tick0=x_min, dtick=dtick)

    # Layout
    legend_config = dict(
        groupclick="togglegroup",
        orientation="h", yanchor="bottom", y=1.08, xanchor="left", x=0,
        bgcolor="rgba(255,255,255,0.9)", bordercolor="#e5e7eb", borderwidth=1, font=dict(size=10),
    )

    if show_pre and not pre_df.empty:
        fig.update_layout(
            margin=SHARED_PLOT_MARGIN,
            xaxis=dict(**SHARED_XAXIS_STYLE),
            yaxis=dict(title=dict(text="Tone Expected Value", font=AXIS_TITLE_FONT, standoff=6), tickfont=AXIS_TICK_FONT, automargin=True, zeroline=False),
            yaxis2=dict(title=dict(text="Cumulative Tone", font=AXIS_TITLE_FONT, standoff=6), tickfont=AXIS_TICK_FONT, automargin=True, overlaying="y", side="right", zeroline=False),
            template=None,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            legend=legend_config,
            uirevision="tone",
        )
    else:
        fig.update_layout(
            margin=SHARED_PLOT_MARGIN,
            xaxis=dict(**SHARED_XAXIS_STYLE),
            yaxis=dict(title=dict(text="Cumulative Tone", font=AXIS_TITLE_FONT, standoff=6), tickfont=AXIS_TICK_FONT, automargin=True, zeroline=False),
            template=None,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            legend=legend_config,
            uirevision="tone",
        )

    return fig


def build_indicator_figure(panel_df, active_timestamp, indicator_mode, segment_range=None, legend_state=None):
    """Build key indicators figure with clean legend labels."""
    fig = go.Figure()
    legend_state = legend_state or {}
    
    def _vis(name: str):
        v = legend_state.get(name)
        if v is None:
            return None
        return "legendonly" if v is False else True

    if panel_df.empty:
        fig.update_layout(
            margin=SHARED_PLOT_MARGIN,
            xaxis=dict(**SHARED_XAXIS_STYLE),
            yaxis=dict(title=dict(text="Key Indicators", font=AXIS_TITLE_FONT, standoff=6), tickfont=AXIS_TICK_FONT, automargin=True, zeroline=False),
            template=None,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            uirevision="indicators",
            legend=dict(
                groupclick="togglegroup",
                orientation="h", yanchor="bottom", y=1.08, xanchor="left", x=0,
                bgcolor="rgba(255,255,255,0.9)", bordercolor="#e5e7eb", borderwidth=1, font=dict(size=10),
            ),
        )
        return fig

    # Mapping: Original Column Name -> Desired Legend Label
    LABEL_MAP = {
        "Bid_Ask_Spread": "Bid Ask Spread",
        "Order_Book_Imbalance": "Order Book Imbalance",
        "Quote_Revision_Frequency": "Quote Revision Frequency",
        "Quote_Volatility": "Quote Volatility",
        "trade_count": "Trade Count",
        "trade_volume": "Trade Volume",
        "trade_vwap": "Trade vwap"
    }
    
    # Mapping: Display Label -> Color Key (to match INDICATOR_COLORS dictionary keys)
    COLOR_KEY_MAP = {
        "Bid Ask Spread": "Bid Ask Spread",
        "Order Book Imbalance": "Order Book Imbalance",
        "Quote Revision Frequency": "Quote Revision Frequency",
        "Quote Volatility": "Quote Volatility",
        "Trade Count": "trade count",
        "Trade Volume": "trade volume",
        "Trade vwap": "trade vwap"
    }

    allowed = TRADE_COLS if indicator_mode == "trade" else QUOTE_COLS
    cols = [c for c in allowed if c in panel_df.columns]
    x = panel_df["timestamp_sec"]

    for col in cols:
        display_name = LABEL_MAP.get(col, col)
        color_lookup_key = COLOR_KEY_MAP.get(display_name, display_name)
        
        fig.add_trace(
            go.Scatter(
                x=x,
                y=panel_df[col],
                mode="lines",
                name=display_name,
                visible=_vis(display_name),
                line=dict(width=2, color=INDICATOR_COLORS.get(color_lookup_key, None)),
                hovertemplate="t=%{x:.0f}s<br>%{y:.3f}<extra></extra>",
            )
        )

    # Active timestamp line
    if active_timestamp is not None:
        fig.add_shape(
            type="line", x0=active_timestamp, x1=active_timestamp, y0=0, y1=1,
            xref="x", yref="paper",
            line=dict(color="black", width=2),
        )

    # X-axis range
    if segment_range is not None:
        x_min, x_max = segment_range
        if x_min is not None and x_max is not None and x_min < x_max:
            span = x_max - x_min
            dtick = max(span / 5.0, 1.0)
            fig.update_xaxes(range=[x_min, x_max], tickmode="linear", tick0=x_min, dtick=dtick)

    fig.update_layout(
        margin=SHARED_PLOT_MARGIN,
        xaxis=dict(**SHARED_XAXIS_STYLE),
        yaxis=dict(title=dict(text="Key Indicators", font=AXIS_TITLE_FONT, standoff=6), tickfont=AXIS_TICK_FONT, automargin=True, zeroline=False),
        template=None,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        uirevision="indicators",
        legend=dict(
            groupclick="togglegroup",
            orientation="h", yanchor="bottom", y=1.08, xanchor="left", x=0,
            bgcolor="rgba(255,255,255,0.9)", bordercolor="#e5e7eb", borderwidth=1, font=dict(size=10),
        ),
    )

    return fig
def build_transcript_children(df, active_section_id, scroll_state):
    """Build transcript cards with more/less window."""
    if df.empty:
        return [html.Div("No transcript data", className="transcript-empty")]

    scroll_state = scroll_state or {}
    above_more = bool(scroll_state.get("above_more", False))
    below_more = bool(scroll_state.get("below_more", False))

    df_sorted = df.sort_values("timestamp_sec").reset_index(drop=True)
    
    # 找到 active_section_id 在排序後 DataFrame 中的位置
    idx = df_sorted.index[df_sorted["section_id"] == active_section_id]
    if len(idx) == 0:
        # 如果找不到，使用第一個
        center_i = 0
        active_section_id = int(df_sorted.iloc[0]["section_id"])
    else:
        center_i = int(idx[0])
    
    # 獲取 active 卡片的 timestamp，用於後續比較
    active_timestamp = float(df_sorted.iloc[center_i]["timestamp_sec"])

    # Window size - 確保 center_i 始終作為中心點
    base_above = 1
    base_below = 1
    more_above = 5
    more_below = 5

    # 根據 more/less 狀態計算範圍，但始終以 center_i 為中心
    above_range = (base_above + more_above) if above_more else base_above
    below_range = (base_below + more_below) if below_more else base_below

    start_i = max(center_i - above_range, 0)
    end_i = min(center_i + below_range, len(df_sorted) - 1)

    children = []
    is_pre = "presentation_text" in df.columns

    for i in range(start_i, end_i + 1):
        row = df_sorted.iloc[i]
        sec_id = int(row["section_id"])

        classes = ["transcript-line"]
        
        # 關鍵修改：使用 section_id 和 timestamp 雙重判斷
        if sec_id == active_section_id:
            classes.append("transcript-active")
        else:
            # 使用 timestamp 來判斷上下關係，而不是索引位置
            row_timestamp = float(row["timestamp_sec"])
            if row_timestamp < active_timestamp:
                classes.append("transcript-above")
            else:
                classes.append("transcript-below")

        # Meta rows
        meta_rows = []

        if is_pre:
            speaker_name = str(row.get("speaker_name_P", "") or "").strip()
            speaker_title = str(row.get("speaker_title_P", "") or "").strip()
            speaker_spans = []
            if speaker_name:
                speaker_spans.append(html.Span(speaker_name, className="speaker-name"))
            if speaker_title:
                speaker_spans.append(html.Span(speaker_title, className="speaker-title"))
            if speaker_spans:
                meta_rows.append(html.Div(speaker_spans, className="transcript-meta-row"))

        # Change point badges
        cp_badges = []

        if is_pre:
            # Presentation: keep the original single "Change Point" badge
            if int(row.get("is_changepoint", 0)) == 1:
                cp_badges.append(html.Span("Change Point", className="cp-tag cp-tag-sentence"))
        else:
            # Q&A: show per-dimension Change Point badges (can be multiple per row)
            dims = ["assertive", "cautious", "optimistic", "specific", "clear", "relevant"]
            for d in dims:
                cp_col = f"qa_{d}_change_point"
                if (cp_col in df_sorted.columns) and int(row.get(cp_col, 0) or 0) == 1:
                    color = QA_DIM_COLORS.get(d, "#111827")
                    cp_badges.append(
                        html.Span(
                            f"{d.capitalize()} Change Point",
                            className="cp-tag cp-tag-sentence",
                            style={
                                "backgroundColor": f"rgba{tuple(int(color[i:i+2], 16) for i in (1, 3, 5)) + (0.15,)}",
                                "borderColor": f"rgba{tuple(int(color[i:i+2], 16) for i in (1, 3, 5)) + (0.55,)}",
                                "color": color,
                            },
                        )
                    )

            if (not cp_badges) and int(row.get("is_changepoint", 0)) == 1:
                cp_badges.append(html.Span("Change Point", className="cp-tag cp-tag-sentence"))

        if cp_badges:
            meta_rows.append(html.Div(cp_badges, className="cp-row"))

        # Text block
        if is_pre:
            text = str(row.get("presentation_text", "") or "")
            text_block = html.Div(text, className="transcript-text")
        else:
            q_text = str(row.get("question_text", "") or "").strip()
            a_text = str(row.get("answer_text", "") or "").strip()
            q_name = str(row.get("speaker_name_Q", "") or "").strip()
            q_title = str(row.get("speaker_title_Q", "") or "").strip()
            a_name = str(row.get("speaker_name_A", "") or "").strip()
            a_title = str(row.get("speaker_title_A", "") or "").strip()

            text_block = html.Div(
                [
                    html.Div(
                        [
                            html.Span("Q", className="qa-label qa-label-q",
                                      title=(q_name + " " + q_title).strip()),
                            html.Div(q_text, className="qa-bubble qa-bubble-q"),
                        ],
                        className="qa-line qa-line-q",
                    ),
                    html.Div(
                        [
                            html.Span("A", className="qa-label qa-label-a",
                                      title=(a_name + " " + a_title).strip()),
                            html.Div(a_text, className="qa-bubble qa-bubble-a"),
                        ],
                        className="qa-line qa-line-a",
                    ),
                ],
                className="qa-text-block",
            )

        children.append(
            html.Div(
                id={"type": "transcript-item", "index": sec_id},
                n_clicks=0,
                className=" ".join(classes),
                children=[
                    html.Div(meta_rows, className="transcript-meta"),
                    text_block,
                ],
            )
        )

    return children


# ============================================================
# 4. App Layout
# ============================================================

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = dbc.Container(
    [
        dcc.Store(id="store-pre-data"),
        dcc.Store(id="store-qa-data"),
        dcc.Store(id="store-panel-data"),
        dcc.Store(id="store-global-data"),
        dcc.Store(id="store-active-point"),
        dcc.Store(id="store-active-transcript"),
        dcc.Store(id="store-scroll-state", data={"above_more": False, "below_more": False}),
        dcc.Store(id="store-quarter", data=1),
        dcc.Store(id="store-indicator-mode", data="quote"),
        dcc.Store(id="store-scroll-dummy"),
        dcc.Store(id="store-legend-tone", data={}),
        dcc.Store(id="store-legend-indicators", data={}),
        dcc.Store(id="store-scroll-trigger", data=0),

        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [
                            html.H5("Transcript", className="block-title"),
                            html.Div(
                                className="transcript-tab-row",
                                children=[
                                    dbc.Button("Presentation", id="btn-tab-pre", n_clicks=0,
                                               className="transcript-tab active"),
                                    dbc.Button("Q&A", id="btn-tab-qa", n_clicks=0,
                                               className="transcript-tab"),
                                ],
                            ),
                            html.Div(
                                className="more-less-row top",
                                children=[
                                    html.Button("+ More", id="btn-more-top", n_clicks=0,
                                                className="more-less-btn"),
                                    html.Button("- Less", id="btn-less-top", n_clicks=0,
                                                className="more-less-btn"),
                                ],
                            ),
                            html.Div(
                                id="transcript-container",
                                className="transcript-container",
                                children=[html.Div(id="transcript-inner")],
                            ),
                            html.Div(
                                className="more-less-row bottom",
                                children=[
                                    html.Button("+ More", id="btn-more-bottom", n_clicks=0,
                                                className="more-less-btn"),
                                    html.Button("- Less", id="btn-less-bottom", n_clicks=0,
                                                className="more-less-btn"),
                                ],
                            ),
                        ],
                        className="dash-card transcript-card",
                    ),
                    width=3,
                    style={"padding": "10px", "height": "100%"},
                ),
                dbc.Col(
                    [
                        html.Div(
                            [
                                html.H5("Cumulative Tone", className="block-title"),
                                html.Div(id="tone-time-label", className="tone-time-label"),
                                dcc.Graph(id="graph-tone", config={"displayModeBar": False},
                                          className="tone-graph"),
                            ],
                            className="dash-card chart-card",
                            style={"height": "calc(50% - 6px)", "marginBottom": "8px"},
                        ),
                        html.Div(
                            [
                                html.H5("Key Indicators", className="block-title"),
                                html.Div(
                                    className="indicator-tab-row",
                                    children=[
                                        html.Button("Quote", id="btn-ind-quote", n_clicks=0,
                                                    className="indicator-tab active"),
                                        html.Button("Trade", id="btn-ind-trade", n_clicks=0,
                                                    className="indicator-tab"),
                                    ],
                                ),
                                dcc.Graph(id="graph-indicators", config={"displayModeBar": False},
                                          className="indicator-graph"),
                            ],
                            className="dash-card chart-card",
                            style={"height": "calc(50% - 6px)"},
                        ),
                    ],
                    width=6,
                    style={"padding": "10px", "height": "100%"},
                ),
                dbc.Col(
                    [
                        html.Div("EARNINGS CALL DASHBOARD", className="top-header"),
                        dbc.Row(
                            [
                                dbc.Col(
                                    html.Div(
                                        [
                                            html.Label("Year", style={
                                                "position": "absolute", "top": "5px", "left": "10px",
                                                "fontSize": "13px", "color": "#888", "fontWeight": "400",
                                            }),
                                            html.Div(str(YEAR_DEFAULT), style={
                                                "fontSize": "22px", "fontWeight": "550",
                                                "marginLeft": "10px", "marginTop": "8px"
                                            }),
                                        ],
                                        className="dash-card",
                                        style={"padding": "5px", "height": "50px", "display": "flex",
                                               "alignItems": "center", "justifyContent": "center",
                                               "position": "relative"},
                                    ),
                                    width=4,
                                    style={"paddingRight": "8px", "height": "50px"},
                                ),
                                dbc.Col(
                                    dbc.ButtonGroup(
                                        [
                                            dbc.Button("Q1", id="btn-q1", n_clicks=0, style=STYLE_ACTIVE),
                                            dbc.Button("Q2", id="btn-q2", n_clicks=0, style=STYLE_INACTIVE),
                                            dbc.Button("Q3", id="btn-q3", n_clicks=0, style=STYLE_INACTIVE),
                                            dbc.Button("Q4", id="btn-q4", n_clicks=0, style=STYLE_INACTIVE),
                                        ],
                                        className="custom-btn-group",
                                    ),
                                    width=8,
                                    style={"paddingLeft": "0px", "height": "50px"},
                                ),
                            ],
                            className="g-0",
                            style={"marginBottom": "8px"},
                        ),
                        html.Div(
                            [
                                html.Label("Company", style={
                                    "fontSize": "13px", "color": "#888", "fontWeight": "400",
                                    "position": "absolute", "top": "5px", "left": "10px",
                                }),
                                dcc.Dropdown(
                                    options=DROPDOWN_OPTIONS,
                                    value=DROPDOWN_OPTIONS[0]["value"] if DROPDOWN_OPTIONS else None,
                                    clearable=True,
                                    searchable=False,
                                    className="clean-dropdown",
                                    style={"border": "none", "marginTop": "10px"},
                                    id="dropdown-company",
                                ),
                            ],
                            className="dash-card dropdown-card",
                            style={"marginBottom": "8px", "padding": "10px 15px", "position": "relative"},
                        ),
                        html.Div(
                            [
                                html.H5("Comment", className="block-title"),
                                dcc.Markdown(
                                    id="comment-content",
                                    className="comment-content",
                                    children="",
                                    style={"flex": "1", "minHeight": "0"},
                                ),
                            ],
                            className="dash-card comment-card",
                            style={"flex": "1", "padding": "8px 12px", "display": "flex",
                                   "flexDirection": "column"},
                        ),
                    ],
                    width=3,
                    style={"padding": "8px", "height": "100%", "display": "flex",
                           "flexDirection": "column"},
                ),
            ],
            style={"height": "100%"},
        ),
    ],
    fluid=True,
    style={"height": "100vh", "backgroundColor": "#f4f4f4", "padding": "10px"},
)

# ============================================================
# 5. Callbacks
# ============================================================

@app.callback(
    Output("btn-q1", "style"),
    Output("btn-q2", "style"),
    Output("btn-q3", "style"),
    Output("btn-q4", "style"),
    Output("store-quarter", "data"),
    Input("btn-q1", "n_clicks"),
    Input("btn-q2", "n_clicks"),
    Input("btn-q3", "n_clicks"),
    Input("btn-q4", "n_clicks"),
)
def update_quarter_styles(n1, n2, n3, n4):
    triggered_id = ctx.triggered_id
    if not triggered_id:
        return STYLE_ACTIVE, STYLE_INACTIVE, STYLE_INACTIVE, STYLE_INACTIVE, 1
    quarter = {"btn-q1": 1, "btn-q2": 2, "btn-q3": 3, "btn-q4": 4}.get(triggered_id, 1)
    styles = [STYLE_INACTIVE] * 4
    styles[quarter - 1] = STYLE_ACTIVE
    return styles[0], styles[1], styles[2], styles[3], quarter

@app.callback(
    Output("store-indicator-mode", "data"),
    Output("btn-ind-quote", "className"),
    Output("btn-ind-trade", "className"),
    Input("btn-ind-quote", "n_clicks"),
    Input("btn-ind-trade", "n_clicks"),
    State("store-indicator-mode", "data"),
)
def switch_indicator_mode(nq, nt, current_mode):
    mode = "trade" if ctx.triggered_id == "btn-ind-trade" else "quote"
    quote_class = "indicator-tab active" if mode == "quote" else "indicator-tab"
    trade_class = "indicator-tab active" if mode == "trade" else "indicator-tab"
    return mode, quote_class, trade_class

@app.callback(
    Output("store-pre-data", "data"),
    Output("store-qa-data", "data"),
    Output("store-panel-data", "data"),
    Output("store-global-data", "data"),
    Output("store-active-point", "data"),
    Output("store-active-transcript", "data"),
    Output("tone-time-label", "children"),
    Output("comment-content", "children"),
    Input("dropdown-company", "value"),
    Input("store-quarter", "data"),
    Input("graph-tone", "clickData"),
    Input("graph-indicators", "clickData"),
    Input({"type": "transcript-item", "index": ALL}, "n_clicks_timestamp"),
    Input("btn-tab-pre", "n_clicks"),
    Input("btn-tab-qa", "n_clicks"),
    State("store-pre-data", "data"),
    State("store-qa-data", "data"),
    State("store-panel-data", "data"),
    State("store-global-data", "data"),
    State("store-active-point", "data"),
    State("store-active-transcript", "data"),
)
def unified_data_and_active(
    tic, quarter, tone_click, ind_click, transcript_clicks,
    tab_pre, tab_qa,
    pre_data, qa_data, panel_data, global_data, active_point, active_transcript,
):
    triggered = ctx.triggered_id
    if triggered == "graph-tone" and tone_click is None:
        raise dash.exceptions.PreventUpdate
    if triggered == "graph-indicators" and ind_click is None:
        raise dash.exceptions.PreventUpdate

    if triggered in ["dropdown-company", "store-quarter"]:
        if tic is None: raise dash.exceptions.PreventUpdate
        year = YEAR_DEFAULT
        pre_df = load_pre_df(tic, year, quarter)
        qa_df = load_qa_df(tic, year, quarter)
        panel_df = load_panel_df(tic, year, quarter)
        global_df = build_global_df(pre_df, qa_df)
        if not pre_df.empty:
            sec_id, mode = choose_default_changepoint(pre_df), "pre"
        else:
            sec_id, mode = choose_default_changepoint(qa_df), "qa"
        active_point = {"mode": mode, "section_id": int(sec_id)}
        active_transcript = int(sec_id)
        row, label = load_calendar_row(tic, year, quarter), ""
        if row is not None:
            start, end = row.get("timestamp_et_start", ""), row.get("timestamp_et_end", "")
            if pd.notna(start) and pd.notna(end):
                try:
                    label = f"[{pd.to_datetime(start).strftime('%Y-%m-%d %H:%M')}, {pd.to_datetime(end).strftime('%Y-%m-%d %H:%M')}] ET"
                except: label = f"[{start}, {end}] ET"
        return (pre_df.to_dict("records"), qa_df.to_dict("records"), panel_df.to_dict("records"), 
                global_df.to_dict("records"), active_point, int(active_point["section_id"]), label, load_comment_md(tic, year, quarter))

    pre_df, qa_df, global_df = _df_from_store(pre_data), _df_from_store(qa_data), _df_from_store(global_data)
    active_point = active_point or {"mode": "pre", "section_id": 0}
    active_transcript = active_transcript or int(active_point["section_id"])
    mode, section_id = active_point.get("mode", "pre"), int(active_point.get("section_id", 0))

    if triggered == "graph-tone" and tone_click:
        section_id = find_nearest_section_in_mode(global_df, tone_click["points"][0]["x"], mode)
        active_transcript = section_id
    elif triggered == "graph-indicators" and ind_click:
        section_id = find_nearest_section_in_mode(global_df, ind_click["points"][0]["x"], mode)
        active_transcript = section_id
    elif isinstance(triggered, dict) and triggered.get("type") == "transcript-item":
        section_id = active_transcript = int(triggered["index"])
    elif triggered == "btn-tab-pre":
        mode, section_id = "pre", (choose_default_changepoint(pre_df) if not pre_df.empty else 0)
        active_transcript = section_id
    elif triggered == "btn-tab-qa":
        mode, section_id = "qa", (choose_default_changepoint(qa_df) if not qa_df.empty else 0)
        active_transcript = section_id

    return (pre_data, qa_data, panel_data, global_data, {"mode": mode, "section_id": int(section_id)}, active_transcript, dash.no_update, dash.no_update)

@app.callback(
    Output("store-scroll-state", "data"),
    Output("store-scroll-trigger", "data"),
    Input("btn-more-top", "n_clicks"), 
    Input("btn-less-top", "n_clicks"),
    Input("btn-more-bottom", "n_clicks"), 
    Input("btn-less-bottom", "n_clicks"),
    State("store-scroll-state", "data"),
    State("store-scroll-trigger", "data"),
    prevent_initial_call=True,
)
def toggle_scroll_state(nmt, nlt, nmb, nlb, scroll_state, trigger_count):
    scroll_state = scroll_state or {"above_more": False, "below_more": False}
    trigger_count = trigger_count or 0
    trig = ctx.triggered_id
    
    if trig == "btn-more-top": 
        scroll_state["above_more"] = True
    elif trig == "btn-less-top": 
        scroll_state["above_more"] = False
    elif trig == "btn-more-bottom": 
        scroll_state["below_more"] = True
    elif trig == "btn-less-bottom": 
        scroll_state["below_more"] = False
    
    return scroll_state, trigger_count + 1

@app.callback(
    Output("btn-more-top", "className"), Output("btn-less-top", "className"),
    Output("btn-more-bottom", "className"), Output("btn-less-bottom", "className"),
    Input("store-scroll-state", "data"),
)
def update_more_less_button_classes(scroll_state):
    base = "more-less-btn"
    scroll_state = scroll_state or {"above_more": False, "below_more": False}
    a, b = scroll_state.get("above_more"), scroll_state.get("below_more")
    return base+(" more-less-btn-active" if a else ""), base+("" if a else " more-less-btn-active"), \
           base+(" more-less-btn-active" if b else ""), base+("" if b else " more-less-btn-active")

@app.callback(
    Output("store-legend-tone", "data"), Input("graph-tone", "restyleData"),
    State("graph-tone", "figure"), State("store-legend-tone", "data"), prevent_initial_call=True
)
def persist_legend_state_tone(restyle_data, fig, state):
    if not restyle_data or not fig: raise dash.exceptions.PreventUpdate
    state, (changes, trace_idxs) = state or {}, restyle_data
    if isinstance(trace_idxs, int): trace_idxs = [trace_idxs]
    vis_list = changes.get("visible") if isinstance(changes.get("visible"), list) else [changes.get("visible")]*len(trace_idxs)
    for i, t_idx in enumerate(trace_idxs):
        name = fig["data"][t_idx].get("name")
        if name: state[name] = False if vis_list[i] == "legendonly" else True
    return state

@app.callback(
    Output("store-legend-indicators", "data"), Input("graph-indicators", "restyleData"),
    State("graph-indicators", "figure"), State("store-legend-indicators", "data"), prevent_initial_call=True
)
def persist_legend_state_indicators(restyle_data, fig, state):
    if not restyle_data or not fig: raise dash.exceptions.PreventUpdate
    state, (changes, trace_idxs) = state or {}, restyle_data
    if isinstance(trace_idxs, int): trace_idxs = [trace_idxs]
    vis_list = changes.get("visible") if isinstance(changes.get("visible"), list) else [changes.get("visible")]*len(trace_idxs)
    for i, t_idx in enumerate(trace_idxs):
        name = fig["data"][t_idx].get("name")
        if name: state[name] = False if vis_list[i] == "legendonly" else True
    return state

@app.callback(
    Output("graph-tone", "figure"), 
    Output("graph-indicators", "figure"),
    Input("store-active-point", "data"), 
    Input("store-pre-data", "data"), 
    Input("store-qa-data", "data"), 
    Input("store-panel-data", "data"),
    Input("store-indicator-mode", "data"),
    Input("store-legend-tone", "data"), 
    Input("store-legend-indicators", "data"),
)
def update_graphs(active_point, pre_data, qa_data, panel_data, indicator_mode, legend_tone, legend_indicators):
    pre_df, qa_df, panel_df = _df_from_store(pre_data), _df_from_store(qa_data), _df_from_store(panel_data)
    mode, section_id = (active_point.get("mode", "pre"), int(active_point.get("section_id", 0))) if active_point else ("pre", 0)
    current_df = pre_df if mode == "pre" else qa_df
    seg_range, active_ts = None, None
    if not current_df.empty:
        s, e = float(current_df["timestamp_sec"].min()), float(current_df["timestamp_sec"].max())
        if e > s: seg_range = (s, e)
        r = current_df[current_df["section_id"] == section_id]
        if not r.empty: active_ts = float(r.iloc[0]["timestamp_sec"])
    return build_tone_figure(pre_df, qa_df, mode, section_id, seg_range, legend_tone), \
           build_indicator_figure(panel_df, active_ts, indicator_mode, seg_range, legend_indicators)

@app.callback(
    Output("transcript-inner", "children"), 
    Output("btn-tab-pre", "className"), 
    Output("btn-tab-qa", "className"),
    Input("store-active-transcript", "data"),
    Input("store-scroll-trigger", "data"),
    State("store-active-point", "data"),
    State("store-pre-data", "data"), 
    State("store-qa-data", "data"),
    State("store-scroll-state", "data"),
    prevent_initial_call=False,
)
def update_transcript(active_transcript, scroll_trigger, active_point, pre_data, qa_data, scroll_state):
    pre_df, qa_df = _df_from_store(pre_data), _df_from_store(qa_data)
    mode = active_point.get("mode", "pre") if active_point else "pre"
    section_id = int(active_point.get("section_id", 0)) if active_point else 0
    current_df = pre_df if mode == "pre" else qa_df
    
    if active_transcript is not None:
        display_section_id = int(active_transcript)
    else:
        display_section_id = section_id
    
    if not current_df.empty:
        if display_section_id not in current_df["section_id"].values:
            if section_id in current_df["section_id"].values:
                display_section_id = section_id
            else:
                display_section_id = int(current_df.iloc[0]["section_id"])
    
    return build_transcript_children(current_df, display_section_id, scroll_state or {}), \
           "transcript-tab active" if mode == "pre" else "transcript-tab", \
           "transcript-tab active" if mode == "qa" else "transcript-tab"

app.clientside_callback(
    """function(at, trigger, ss, ch) {
        if (!ch) return null;

        var targetId = at !== null && at !== undefined ? at : 0;
        
        requestAnimationFrame(function() {
            requestAnimationFrame(function() {
                var container = document.getElementById('transcript-container');
                if (!container) return;
                
                var activeEls = container.getElementsByClassName('transcript-active');
                if (!activeEls.length) return;
                
                var activeEl = activeEls[0];
                var contRect = container.getBoundingClientRect();
                var actRect = activeEl.getBoundingClientRect();

                var scrollOffset = (actRect.top + actRect.bottom)/2 - (contRect.top + contRect.bottom)/2;

                if (Math.abs(scrollOffset) > 5) {
                    container.scrollBy({
                        top: scrollOffset,
                        behavior: 'smooth'
                    });
                }
            });
        });
        
        return null;
    }""",
    Output("store-scroll-dummy", "data"), 
    Input("store-active-transcript", "data"),
    Input("store-scroll-trigger", "data"),
    Input("store-scroll-state", "data"), 
    Input("transcript-inner", "children"),
)

if __name__ == "__main__":
    app.run_server(debug=True)