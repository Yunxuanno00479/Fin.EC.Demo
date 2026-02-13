import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, State, ctx, ALL
import pandas as pd
from pathlib import Path
import plotly.graph_objs as go
import numpy as np
from datetime import datetime

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
    "Trade_Count",
    "Trade_Volume",
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
    "Bid Ask Spread":          "#1f77b4",
    "Order Book Imbalance":    "#ff7f0e",
    "Quote Revision Frequency":"#2ca02c",
    "Quote Volatility":        "#9467bd",
    "Trade Count":             "#d62728",
    "Trade Volume":            "#17becf",
}

# Q&A cumulative line colors
QA_DIM_COLORS = {
    "assertive": "#1f77b4",
    "cautious":  "#2ca02c",
    "optimistic":"#9467bd",
    "specific":  "#8c564b",
    "clear":     "#17becf",
    "relevant":  "#7f7f7f",
}

# Change Point color
CHANGE_POINT_COLOR = "#d62728"

# Q&A Change Point badge colors
QA_CP_BADGE_COLORS = {
    "assertive": {"bg": "#E3F2FD", "border": "#1976D2", "text": "#0D47A1"},
    "cautious":  {"bg": "#E8F5E9", "border": "#388E3C", "text": "#1B5E20"},
    "optimistic":{"bg": "#F3E5F5", "border": "#7B1FA2", "text": "#4A148C"},
    "specific":  {"bg": "#FFEBEE", "border": "#C62828", "text": "#B71C1C"},
    "clear":     {"bg": "#E0F7FA", "border": "#0097A7", "text": "#006064"},
    "relevant":  {"bg": "#F5F5F5", "border": "#616161", "text": "#212121"},
}

# ============================================================
# Shared plot styling
# ============================================================

SHARED_PLOT_MARGIN = dict(l=50, r=50, t=56, b=36)

AXIS_TICK_FONT = dict(size=11, color="#374151")
AXIS_TITLE_FONT = dict(size=12, color="#1f2937", family="Arial")

SHARED_XAXIS_STYLE = dict(
    title=dict(text="Time (seconds since call start)", font=AXIS_TITLE_FONT, standoff=8),
    tickfont=AXIS_TICK_FONT,
    ticks="outside",
    ticklen=5,
    tickwidth=1.5,
    showline=True,
    linewidth=1.5,
    linecolor="#9ca3af",
    zeroline=True,
    zerolinewidth=1,
    zerolinecolor="#e5e7eb",
    mirror=False,
    showgrid=True,
    gridwidth=1,
    gridcolor="rgba(156, 163, 175, 0.2)",
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

def safe_numeric_convert(series, default=np.nan):
    """Safely convert series to numeric with error handling."""
    try:
        return pd.to_numeric(series, errors="coerce").fillna(default)
    except Exception:
        return pd.Series([default] * len(series))


def load_pre_df(tic: str, year: int, quarter: int) -> pd.DataFrame:
    """Load presentation data with improved error handling."""
    path = DATA_DIR / "Pre_finbert_tone" / f"{tic}_{year}_pre.csv"
    if not path.exists():
        return pd.DataFrame()

    try:
        df = pd.read_csv(path).copy()
    except Exception as e:
        print(f"Error loading {path}: {e}")
        return pd.DataFrame()

    if "quarter" in df.columns:
        df = df[df["quarter"] == quarter].copy()
    if df.empty:
        return df

    if "section_id" in df.columns:
        df["section_id"] = df["section_id"].astype(int)
    elif "sent_section_id" in df.columns:
        df["section_id"] = df["sent_section_id"].astype(int)
    else:
        df["section_id"] = range(1, len(df) + 1)

    if "timestamp_p" in df.columns:
        df["timestamp_sec"] = safe_numeric_convert(df["timestamp_p"], 0.0)
    elif "timestamp_sec" in df.columns:
        df["timestamp_sec"] = safe_numeric_convert(df["timestamp_sec"], 0.0)
    else:
        df["timestamp_sec"] = np.arange(len(df), dtype=float)

    if "presentation_text" in df.columns:
        df["display_text"] = df["presentation_text"].fillna("")
    elif "text" in df.columns:
        df["display_text"] = df["text"].fillna("")
    else:
        df["display_text"] = ""

    if "finberttone_cumulative_tone" in df.columns:
        df["cumulative_tone"] = safe_numeric_convert(df["finberttone_cumulative_tone"])
    elif "cumulative_tone" in df.columns:
        df["cumulative_tone"] = safe_numeric_convert(df["cumulative_tone"])
    else:
        df["cumulative_tone"] = np.nan

    if "finberttone_expected_value" in df.columns:
        df["tone_expected_value"] = safe_numeric_convert(df["finberttone_expected_value"])
    elif "tone_expected_value" in df.columns:
        df["tone_expected_value"] = safe_numeric_convert(df["tone_expected_value"])
    else:
        df["tone_expected_value"] = np.nan

    # Tone label and score for hover
    if "tone_label" not in df.columns:
        df["tone_label"] = ""
    if "tone_score" not in df.columns:
        df["tone_score"] = np.nan

    change_point_cols = [c for c in df.columns if c.endswith("_change_point")]
    if change_point_cols:
        cp_col = "finberttone_change_point" if "finberttone_change_point" in change_point_cols else change_point_cols[0]
        df[cp_col] = df[cp_col].fillna(0).astype(int)
        df["is_changepoint"] = (df[cp_col] == 1).astype(int)
    else:
        df["is_changepoint"] = 0
        
    return df


def load_qa_df(tic: str, year: int, quarter: int) -> pd.DataFrame:
    """Load Q&A data with improved error handling."""
    path = DATA_DIR / "QA_subjectiveqa" / f"{tic}_{year}_qa.csv"
    if not path.exists():
        return pd.DataFrame()

    try:
        df = pd.read_csv(path).copy()
    except Exception as e:
        print(f"Error loading {path}: {e}")
        return pd.DataFrame()

    if "quarter" in df.columns:
        df = df[df["quarter"] == quarter].copy()
    if df.empty:
        return df

    if "QA_Index" in df.columns:
        df["section_id"] = df["QA_Index"].astype(int)
    elif "section_id" in df.columns:
        df["section_id"] = df["section_id"].astype(int)
    elif "sent_section_id" in df.columns:
        df["section_id"] = df["sent_section_id"].astype(int)
    else:
        df["section_id"] = range(1, len(df) + 1)

    if "Q_Timestamp" in df.columns:
        df["timestamp_Q"] = safe_numeric_convert(df["Q_Timestamp"], 0.0)
        df["timestamp_sec"] = df["timestamp_Q"]
    else:
        if "timestamp_Q" in df.columns:
            df["timestamp_Q"] = safe_numeric_convert(df["timestamp_Q"], 0.0)
        if "timestamp_A" in df.columns:
            df["timestamp_A"] = safe_numeric_convert(df["timestamp_A"], 0.0)
        df["timestamp_sec"] = df.get("timestamp_Q", pd.Series(range(len(df)), dtype=float))

    if "Question" in df.columns:
        df["question_text"] = df["Question"].fillna("")
    else:
        df["question_text"] = ""

    if "Answer" in df.columns:
        df["answer_text"] = df["Answer"].fillna("")
    else:
        df["answer_text"] = ""

    df["display_text"] = "Q: " + df["question_text"].astype(str) + "\nA: " + df["answer_text"].astype(str)

    dims = ["assertive", "cautious", "optimistic", "specific", "clear", "relevant"]
    for d in dims:
        if f"{d}_cumulative_tone" in df.columns:
            df[f"qa_{d}_cumulative"] = safe_numeric_convert(df[f"{d}_cumulative_tone"])
        elif f"qa_{d}_cumulative" in df.columns:
            df[f"qa_{d}_cumulative"] = safe_numeric_convert(df[f"qa_{d}_cumulative"])
        else:
            df[f"qa_{d}_cumulative"] = np.nan

        if f"{d}_expected_value" in df.columns:
            df[f"qa_{d}_expected_value"] = safe_numeric_convert(df[f"{d}_expected_value"])
        elif f"qa_{d}_expected_value" in df.columns:
            df[f"qa_{d}_expected_value"] = safe_numeric_convert(df[f"qa_{d}_expected_value"])
        else:
            df[f"qa_{d}_expected_value"] = np.nan

        cp_col = f"{d}_change_point"
        if cp_col in df.columns:
            df[f"qa_{d}_change_point"] = df[cp_col].fillna(0).astype(int)
        elif f"qa_{cp_col}" in df.columns:
            df[f"qa_{d}_change_point"] = df[f"qa_{cp_col}"].fillna(0).astype(int)
        else:
            df[f"qa_{d}_change_point"] = 0

    cp_cols_new = [f"qa_{d}_change_point" for d in dims if f"qa_{d}_change_point" in df.columns]
    
    if cp_cols_new:
        df["is_changepoint"] = df[cp_cols_new].fillna(0).astype(int).eq(1).any(axis=1).astype(int)
    else:
        df["is_changepoint"] = 0

    return df


def load_panel_df(tic: str, year: int, quarter: int, mode: str = "all") -> pd.DataFrame:
    """Load quote/trade panel data."""
    path = DATA_DIR / "Panel_quote_trade" / f"{tic}_{year}_panel.csv"
    if not path.exists():
        return pd.DataFrame()

    try:
        df = pd.read_csv(path).copy()
    except Exception as e:
        print(f"Error loading {path}: {e}")
        return pd.DataFrame()

    if "year" in df.columns:
        df = df[df["year"] == year]
    if "quarter" in df.columns:
        df = df[df["quarter"] == quarter]
    if df.empty:
        return df

    if "Timestamp_ET" in df.columns:
        try:
            df["timestamp_dt"] = pd.to_datetime(df["Timestamp_ET"], errors="coerce")
            df = df.dropna(subset=["timestamp_dt"])
            if df.empty:
                return df
            
            cal_row = load_calendar_row(tic, year, quarter)
            if cal_row is not None and pd.notna(cal_row.get("timestamp_et_start")):
                call_start = pd.to_datetime(cal_row["timestamp_et_start"])
                
                if df["timestamp_dt"].dt.tz is not None and call_start.tz is None:
                    df["timestamp_dt"] = df["timestamp_dt"].dt.tz_localize(None)
                elif df["timestamp_dt"].dt.tz is None and call_start.tz is not None:
                    call_start = call_start.tz_localize(None)
                elif df["timestamp_dt"].dt.tz is not None and call_start.tz is not None:
                    df["timestamp_dt"] = df["timestamp_dt"].dt.tz_localize(None)
                    call_start = call_start.tz_localize(None)
                
                df["timestamp_sec"] = (df["timestamp_dt"] - call_start).dt.total_seconds()
                
                if mode != "all":
                    pre_df = load_pre_df(tic, year, quarter)
                    qa_df = load_qa_df(tic, year, quarter)
                    
                    if mode == "pre" and not pre_df.empty:
                        pre_start = pre_df["timestamp_sec"].min()
                        pre_end = pre_df["timestamp_sec"].max()
                        df = df[(df["timestamp_sec"] >= pre_start) & (df["timestamp_sec"] <= pre_end)]
                    elif mode == "qa" and not qa_df.empty:
                        qa_start = qa_df["timestamp_sec"].min()
                        qa_end = qa_df["timestamp_sec"].max()
                        df = df[(df["timestamp_sec"] >= qa_start) & (df["timestamp_sec"] <= qa_end)]
            else:
                base = df["timestamp_dt"].min()
                if df["timestamp_dt"].dt.tz is not None:
                    df["timestamp_dt"] = df["timestamp_dt"].dt.tz_localize(None)
                    base = base.tz_localize(None)
                df["timestamp_sec"] = (df["timestamp_dt"] - base).dt.total_seconds()
        except Exception as e:
            print(f"Error parsing timestamps in panel data: {e}")
            df["timestamp_sec"] = np.arange(len(df), dtype=float)
    else:
        df["timestamp_sec"] = np.arange(len(df), dtype=float)
        
    return df


def load_calendar_row(tic: str, year: int, quarter: int):
    """Load calendar row for a given company/year/quarter."""
    path = DATA_DIR / "ec_calendar.csv"
    if not path.exists():
        return None

    try:
        df = pd.read_csv(path)
        row = df[(df["tic"] == tic) & (df["year"] == year) & (df["quarter"] == quarter)].head(1)
        if row.empty:
            return None
        return row.iloc[0]
    except Exception as e:
        print(f"Error loading calendar: {e}")
        return None


def calculate_market_times(cal_row):
    """Calculate market open/close times in seconds relative to call start."""
    if cal_row is None:
        return None, None
    
    try:
        call_start = pd.to_datetime(cal_row.get("timestamp_et_start"))
        if pd.isna(call_start):
            return None, None
        
        call_date = call_start.date()

        market_open = pd.to_datetime(f"{call_date} 09:30:00")  # 09:30 AM ET
        market_close = pd.to_datetime(f"{call_date} 16:00:00")  # 04:00 PM ET
        
        # Handle timezone
        if call_start.tz is not None:
            market_open = market_open.tz_localize(call_start.tz)
            market_close = market_close.tz_localize(call_start.tz)
        
        # Calculate seconds relative to call start
        market_open_sec = (market_open - call_start).total_seconds()
        market_close_sec = (market_close - call_start).total_seconds()
        
        return market_open_sec, market_close_sec
        
    except Exception as e:
        print(f"Error calculating market times: {e}")
        return None, None


def load_comment_md(tic: str, year: int, quarter: int, mode: str = "summary", transcript_mode: str = "pre"):
    """
    Load Markdown comment for a given company/year/quarter.
    mode: "summary" or "cp" (change point)
    transcript_mode: "pre" or "qa"
    
    Summary mode: {tic}_{year}_{pre/qa}_comment_{quarter}.md
    CP mode: {tic}_{year}_{pre/qa}cp_comment_{quarter}.md
    """
    if mode == "summary":
        if transcript_mode == "pre":
            md_path = DATA_DIR / "LLM_comment" / f"{tic}_{year}_pre_comment_{quarter}.md"
        else:
            md_path = DATA_DIR / "LLM_comment" / f"{tic}_{year}_qa_comment_{quarter}.md"
    else:
        if transcript_mode == "pre":
            md_path = DATA_DIR / "LLM_comment" / f"{tic}_{year}_precp_comment_{quarter}.md"
        else:
            md_path = DATA_DIR / "LLM_comment" / f"{tic}_{year}_qacp_comment_{quarter}.md"
    
    if not md_path.exists():
        if mode == "cp":
            return "**Current Transcript has no Change Point.**"
        return ""

    try:
        return md_path.read_text(encoding="utf-8")
    except Exception:
        return "(Unable to read LLM comment file)"


def _df_from_store(data):
    """Convert store data to DataFrame with error handling."""
    if not data:
        return pd.DataFrame()
    try:
        return pd.DataFrame(data)
    except Exception:
        return pd.DataFrame()


def build_global_df(pre_df: pd.DataFrame, qa_df: pd.DataFrame) -> pd.DataFrame:
    """Build global DataFrame combining pre and qa timestamps."""
    dfs = []
    
    if not pre_df.empty and "section_id" in pre_df.columns and "timestamp_sec" in pre_df.columns:
        p = pre_df[["section_id", "timestamp_sec"]].copy()
        p["mode"] = "pre"
        dfs.append(p)
    
    if not qa_df.empty and "section_id" in qa_df.columns and "timestamp_sec" in qa_df.columns:
        q = qa_df[["section_id", "timestamp_sec"]].copy()
        q["mode"] = "qa"
        dfs.append(q)
    
    if not dfs:
        return pd.DataFrame()
        
    return pd.concat(dfs, ignore_index=True)


def choose_default_changepoint(df: pd.DataFrame) -> int:
    """Choose default changepoint section ID."""
    if df is None or df.empty:
        return 0
    if "is_changepoint" in df.columns:
        idx = df.index[df["is_changepoint"] == 1]
        if len(idx) > 0:
            return int(df.loc[idx[0], "section_id"])
    if "section_id" in df.columns:
        return int(df.iloc[0]["section_id"])
    return 0


def find_nearest_section_in_mode(global_df: pd.DataFrame, x: float, mode: str) -> int:
    """Find nearest section_id by timestamp within a fixed mode (pre/qa)."""
    if global_df is None or global_df.empty:
        return 0
    
    dfm = global_df[global_df.get("mode", "").astype(str) == str(mode)].copy()
    if dfm.empty:
        dfm = global_df
    
    if dfm.empty:
        return 0
        
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

def build_tone_figure(pre_df, qa_df, active_mode, active_section_id, segment_range=None, legend_state=None, market_times=None):
    """Build cumulative tone figure."""
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
                    name="Tone Expected Value",
                    visible=_vis("Tone Expected Value"),
                    line=dict(shape="linear", width=1, color="#bdbdbd"),
                    yaxis="y",
                    showlegend=True,
                    hovertemplate="<b>Time:</b> %{x:.0f}s<br><b>Tone Expected Value:</b> %{y:.3f}<extra></extra>",
                )
            )

        # Right y-axis: cumulative tone
        customdata = None
        if set(["tone_label", "tone_score"]).issubset(pre_df.columns):
            customdata = pre_df[["tone_label", "tone_score"]].values
            
        fig.add_trace(
            go.Scatter(
                x=pre_df["timestamp_sec"],
                y=pre_df["cumulative_tone"],
                mode="lines",
                name="Presentation",
                visible=_vis("Presentation"),
                line=dict(shape="linear", width=3, color="#2563eb"),
                yaxis="y2",
                hovertemplate=(
                    "<b>Time:</b> %{x:.3f}s<br><b>Cumulative Tone:</b> %{y:.3f}"
                    + "<extra></extra>"
                ),
                customdata=customdata,
            )
        )

        # Change points
        if "is_changepoint" in pre_df.columns:
            m = pre_df["is_changepoint"].fillna(0).astype(int) == 1
            if m.any():
                #customdata：cumulative_tone, tone_expected_value
                cp_df = pre_df.loc[m].copy()
                cp_customdata = cp_df[["cumulative_tone", "tone_expected_value"]].values
                    
                fig.add_trace(
                    go.Scatter(
                        x=cp_df["timestamp_sec"],
                        y=cp_df["cumulative_tone"],
                        mode="markers",
                        name="Change Point",
                        visible=_vis("Change Point"),
                        hovertemplate=(
                            "<b>Change Point</b><br>"
                            "<b>Time:</b> %{x:.3f}s<br>"
                            "<b>Cumulative Tone:</b> %{customdata[0]:.3f}<br>"
                            "<b>Tone Expected Value:</b> %{customdata[1]:.3f}"
                            "<extra></extra>"
                        ),
                        marker=dict(color=CHANGE_POINT_COLOR, size=10, symbol="triangle-down", 
                                   line=dict(color="white", width=1.5)),
                        yaxis="y2",
                        showlegend=True,
                        customdata=cp_customdata,
                    )
                )
                for ts in cp_df["timestamp_sec"]:
                    fig.add_shape(
                        type="line", x0=float(ts), x1=float(ts), y0=0, y1=1,
                        xref="x", yref="paper",
                        line=dict(color=CHANGE_POINT_COLOR, width=1.5, dash="dot"),
                        layer="below",
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

            color = QA_DIM_COLORS.get(name, "#636363")
            customdata = None
            if ev_col in qa_df.columns and qa_df[ev_col].notna().any():
                customdata = qa_df[[ev_col]].values

            fig.add_trace(
                go.Scatter(
                    x=qa_df["timestamp_sec"],
                    y=qa_df[cum_col],
                    mode="lines+markers",
                    name=name.capitalize(),
                    visible=_vis(name.capitalize()),
                    legendgroup=name,
                    line=dict(width=1.5, color=color),
                    marker=dict(size=4, color=color),
                    customdata=customdata,
                    hovertemplate=(
                        f"<b>{name.capitalize()}</b><br>"
                        f"<b>Time:</b> %{{x:.3f}}s<br><b>Cumulative Tone:</b> %{{y:.3f}}"
                        + (f"<br><b>Tone Expected Value:</b> %{{customdata[0]:.3f}}" if customdata is not None else "")
                        + "<extra></extra>"
                    ),
                )
            )

            # Per-dimension change points
            if cp_col in qa_df.columns:
                m_cp = qa_df[cp_col].fillna(0).astype(int) == 1
                if m_cp.any():
                    cp_qa_df = qa_df.loc[m_cp].copy()
                    # customdata: cumulative, expected_value
                    cp_qa_customdata = cp_qa_df[[cum_col, ev_col]].values if ev_col in cp_qa_df.columns else cp_qa_df[[cum_col]].values
                    
                    fig.add_trace(
                        go.Scatter(
                            x=cp_qa_df["timestamp_sec"],
                            y=cp_qa_df[cum_col],
                            mode="markers",
                            name=f"{name.capitalize()} CP",
                            visible=_vis(name.capitalize()),
                            legendgroup=name,
                            marker=dict(color=CHANGE_POINT_COLOR, size=10, symbol="triangle-down", 
                                       line=dict(color="white", width=1.5)),
                            showlegend=False,
                            hovertemplate=(
                                f"<b>{name.capitalize()} Change Point</b><br>"
                                f"<b>Time:</b> %{{x:.3f}}s<br>"
                                f"<b>Cumulative Tone:</b> %{{customdata[0]:.3f}}<br>"
                                + (f"<b>Tone Expected Value:</b> %{{customdata[1]:.3f}}" if ev_col in cp_qa_df.columns else "")
                                + "<extra></extra>"
                            ),
                            customdata=cp_qa_customdata,
                        )
                    )
                    dim_vis = _vis(name.capitalize())
                    if dim_vis != "legendonly":
                        for ts in cp_qa_df["timestamp_sec"].astype(float).tolist():
                            fig.add_shape(
                                type="line", x0=float(ts), x1=float(ts), y0=0, y1=1,
                                xref="x", yref="paper",
                                line=dict(color=CHANGE_POINT_COLOR, width=1.5, dash="dot"),
                                layer="below",
                            )

    # Active vertical line
    df = pre_df if active_mode == "pre" else qa_df
    if not df.empty and "section_id" in df.columns:
        r = df[df["section_id"] == active_section_id]
        if not r.empty and "timestamp_sec" in r.columns:
            ts = float(r.iloc[0]["timestamp_sec"])

            fig.add_trace(
                go.Scatter(
                    x=[ts],
                    y=[0.5],
                    mode="markers",
                    name="Active Line Control",
                    marker=dict(
                        size=15,
                        color="rgba(0,0,0,0.3)",
                        symbol="line-ns-open",
                        line=dict(width=3, color="#000000"),
                    ),
                    showlegend=False,
                    hoverinfo="skip",
                    yaxis="y2" if (show_pre and not pre_df.empty) else "y",
                    customdata=[[active_section_id]],
                )
            )
            fig.add_shape(
                type="line", x0=ts, x1=ts, y0=0, y1=1,
                xref="x", yref="paper",
                line=dict(color="#000000", width=3),
                layer="above",
            )
    
    # Market open/close time markers
    if market_times is not None and segment_range is not None:
        market_open_sec, market_close_sec = market_times
        x_min, x_max = segment_range
        
        # Pre-Market
        if market_open_sec is not None and market_open_sec > x_min:
            pre_market_end = min(market_open_sec, x_max)
            # background
            fig.add_shape(
                type="rect",
                x0=x_min, x1=pre_market_end,
                y0=0, y1=1,
                xref="x", yref="paper",
                fillcolor="rgba(14, 165, 233, 0.02)",
                line=dict(width=0),
                layer="below",
            )
            # fine dotted line
            fig.add_shape(
                type="line",
                x0=market_open_sec, x1=market_open_sec,
                y0=0, y1=1,
                xref="x", yref="paper",
                line=dict(color="rgba(14, 165, 233, 0.7)", width=0.5, dash="dot"),
                layer="below",
            )
            # small label
            if pre_market_end - x_min > (x_max - x_min) * 0.1:
                fig.add_annotation(
                    x=x_min + (pre_market_end - x_min) * 0.02,
                    y=1.05,
                    xref="x", yref="paper",
                    text="Pre-Market",
                    showarrow=False,
                    font=dict(size=7, color="rgba(14, 165, 233, 0.6)"),
                    xanchor="left",
                    yanchor="top",
                )
        
        # After-Hours
        if market_close_sec is not None and market_close_sec < x_max:
            after_market_start = max(market_close_sec, x_min)
            # background
            fig.add_shape(
                type="rect",
                x0=after_market_start, x1=x_max,
                y0=0, y1=1,
                xref="x", yref="paper",
                fillcolor="rgba(251, 191, 36, 0.03)",
                line=dict(width=0),
                layer="below",
            )
            # fine dotted line
            fig.add_shape(
                type="line",
                x0=market_close_sec, x1=market_close_sec,
                y0=0, y1=1,
                xref="x", yref="paper",
                line=dict(color="rgba(251, 191, 36, 0.7)", width=0.5, dash="dot"),
                layer="below",
            )
            # small label
            if x_max - after_market_start > (x_max - x_min) * 0.1:
                fig.add_annotation(
                    x=x_max - (x_max - after_market_start) * 0.02,
                    y=1.05,
                    xref="x", yref="paper",
                    text="After-Hours",
                    showarrow=False,
                    font=dict(size=7, color="rgba(251, 191, 36, 0.9)"),
                    xanchor="right",
                    yanchor="top",
                )

    # X-axis range
    if segment_range is not None:
        x_min, x_max = segment_range
        if x_min is not None and x_max is not None and x_min < x_max:
            span = x_max - x_min
            dtick = max(span / 8.0, 1.0)
            fig.update_xaxes(range=[x_min, x_max], tickmode="linear", tick0=x_min, dtick=dtick)

    # Layout with legend at top
    legend_config = dict(
        groupclick="togglegroup",
        orientation="h", 
        yanchor="bottom", 
        y=1.06,
        xanchor="left", 
        x=0,
        bgcolor="rgba(255,255,255,0.95)", 
        bordercolor="#cbd5e1", 
        borderwidth=1.5, 
        font=dict(size=10),
    )

    if show_pre and not pre_df.empty:
        fig.update_layout(
            margin=SHARED_PLOT_MARGIN,
            xaxis=dict(**SHARED_XAXIS_STYLE),
            yaxis=dict(
                title=dict(text="Tone Expected Value", font=AXIS_TITLE_FONT, standoff=8), 
                tickfont=AXIS_TICK_FONT, 
                automargin=True, 
                zeroline=True,
                zerolinewidth=1,
                zerolinecolor="#e5e7eb",
                showgrid=True,
                gridwidth=1,
                gridcolor="rgba(156, 163, 175, 0.2)",
            ),
            yaxis2=dict(
                title=dict(text="Cumulative Tone", font=AXIS_TITLE_FONT, standoff=8), 
                tickfont=AXIS_TICK_FONT, 
                automargin=True, 
                overlaying="y", 
                side="right", 
                zeroline=True,
                zerolinewidth=1,
                zerolinecolor="#e5e7eb",
                showgrid=False,
            ),
            template=None,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(249, 250, 251, 0.5)",
            legend=legend_config,
            uirevision="tone",
            hovermode="closest",
            dragmode=False,
        )
    else:
        fig.update_layout(
            margin=SHARED_PLOT_MARGIN,
            xaxis=dict(**SHARED_XAXIS_STYLE),
            yaxis=dict(
                title=dict(text="Cumulative Tone", font=AXIS_TITLE_FONT, standoff=8), 
                tickfont=AXIS_TICK_FONT, 
                automargin=True, 
                zeroline=True,
                zerolinewidth=1,
                zerolinecolor="#e5e7eb",
                showgrid=True,
                gridwidth=1,
                gridcolor="rgba(156, 163, 175, 0.2)",
            ),
            template=None,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(249, 250, 251, 0.5)",
            legend=legend_config,
            uirevision="tone",
            hovermode="closest",
            dragmode=False,
        )
    fig.update_xaxes(fixedrange=True)
    fig.update_yaxes(fixedrange=True)
    if show_pre and not pre_df.empty:
        fig.update_layout(yaxis2=dict(fixedrange=True))

    return fig


def build_indicator_figure(panel_df, active_timestamp, indicator_mode, segment_range=None, legend_state=None, market_times=None):
    """Build key indicators figure"""
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
            yaxis=dict(
                title=dict(text="Value", font=AXIS_TITLE_FONT, standoff=8), 
                tickfont=AXIS_TICK_FONT, 
                automargin=True, 
                zeroline=True,
                zerolinewidth=1,
                zerolinecolor="#e5e7eb",
            ),
            template=None,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(249, 250, 251, 0.5)",
            uirevision="indicators",
            legend=dict(
                groupclick="togglegroup",
                orientation="h", yanchor="bottom", y=1.05, xanchor="left", x=0,
                bgcolor="rgba(255,255,255,0.95)", bordercolor="#cbd5e1", borderwidth=1.5, font=dict(size=10),
            ),
            dragmode="pan",
        )
        return fig

    LABEL_MAP = {
        "Bid_Ask_Spread": "Bid Ask Spread",
        "Order_Book_Imbalance": "Order Book Imbalance",
        "Quote_Revision_Frequency": "Quote Revision Frequency",
        "Quote_Volatility": "Quote Volatility",
        "Trade_Count": "Trade Count",
        "Trade_Volume": "Trade Volume",
    }
    
    COLOR_KEY_MAP = {
        "Bid Ask Spread": "Bid Ask Spread",
        "Order Book Imbalance": "Order Book Imbalance",
        "Quote Revision Frequency": "Quote Revision Frequency",
        "Quote Volatility": "Quote Volatility",
        "Trade Count": "Trade Count",
        "Trade Volume": "Trade Volume",
    }

    allowed = TRADE_COLS if indicator_mode == "trade" else QUOTE_COLS
    cols = [c for c in allowed if c in panel_df.columns]
    
    if not cols:
        return fig
    
    x = panel_df["timestamp_sec"]
    
    for col in cols:
        mask = panel_df[col].notna()
        if not mask.any():
            continue
            
        display_name = LABEL_MAP.get(col, col)
        color_lookup_key = COLOR_KEY_MAP.get(display_name, display_name)
        
        fig.add_trace(
            go.Scatter(
                x=x[mask],
                y=panel_df.loc[mask, col],
                mode="lines",
                name=display_name,
                visible=_vis(display_name),
                line=dict(width=1.5, color=INDICATOR_COLORS.get(color_lookup_key, "#636363")),
                hovertemplate=f"<b>{display_name}</b><br><b>Time:</b> %{{x:.3f}}s<br><b>Value:</b> %{{y:.4f}}<extra></extra>",
            )
        )

    # Active timestamp line
    if active_timestamp is not None:
        fig.add_shape(
            type="line", x0=active_timestamp, x1=active_timestamp, y0=0, y1=1,
            xref="x", yref="paper",
            line=dict(color="#000000", width=3),
            layer="above",
        )
    
    # Market open/close time markers
    if market_times is not None and segment_range is not None:
        market_open_sec, market_close_sec = market_times
        x_min, x_max = segment_range
        
        # Pre-market
        if market_open_sec is not None and market_open_sec > x_min:
            pre_market_end = min(market_open_sec, x_max)
            # background
            fig.add_shape(
                type="rect",
                x0=x_min, x1=pre_market_end,
                y0=0, y1=1,
                xref="x", yref="paper",
                fillcolor="rgba(14, 165, 233, 0.03)",
                line=dict(width=0),
                layer="below",
            )
            # fine dotted line
            fig.add_shape(
                type="line",
                x0=market_open_sec, x1=market_open_sec,
                y0=0, y1=1,
                xref="x", yref="paper",
                line=dict(color="rgba(14, 165, 233, 0.7)", width=0.5, dash="dot"),  # 細線 + dot虛線
                layer="below",
            )
            # small label
            if pre_market_end - x_min > (x_max - x_min) * 0.1:
                fig.add_annotation(
                    x=x_min + (pre_market_end - x_min) * 0.02,
                    y=1.05,
                    xref="x", yref="paper",
                    text="Pre-Market",
                    showarrow=False,
                    font=dict(size=7, color="rgba(14, 165, 233, 0.6)"),
                    xanchor="left",
                    yanchor="top",
                )
        
        # After-hours
        if market_close_sec is not None and market_close_sec < x_max:
            after_market_start = max(market_close_sec, x_min)
            # background
            fig.add_shape(
                type="rect",
                x0=after_market_start, x1=x_max,
                y0=0, y1=1,
                xref="x", yref="paper",
                fillcolor="rgba(251, 191, 36, 0.03)",
                line=dict(width=0),
                layer="below",
            )
            # fine dotted line
            fig.add_shape(
                type="line",
                x0=market_close_sec, x1=market_close_sec,
                y0=0, y1=1,
                xref="x", yref="paper",
                line=dict(color="rgba(251, 191, 36, 0.7)", width=0.5, dash="dot"),
                layer="below",
            )
            # small label
            if x_max - after_market_start > (x_max - x_min) * 0.1:
                fig.add_annotation(
                    x=x_max - (x_max - after_market_start) * 0.02,
                    y=1.05,
                    xref="x", yref="paper",
                    text="After-Hours",
                    showarrow=False,
                    font=dict(size=7, color="rgba(251, 191, 36, 0.9)"),
                    xanchor="right",
                    yanchor="top",
                )

    # X-axis range
    if segment_range is not None:
        x_min, x_max = segment_range
        if x_min is not None and x_max is not None and x_min < x_max:
            span = x_max - x_min
            dtick = max(span / 8.0, 1.0)
            fig.update_xaxes(range=[x_min, x_max], tickmode="linear", tick0=x_min, dtick=dtick)

    fig.update_layout(
        margin=SHARED_PLOT_MARGIN,
        xaxis=dict(**SHARED_XAXIS_STYLE),
        yaxis=dict(
            title=dict(text="Value", font=AXIS_TITLE_FONT, standoff=8), 
            tickfont=AXIS_TICK_FONT, 
            automargin=True, 
            zeroline=True,
            zerolinewidth=1,
            zerolinecolor="#e5e7eb",
            showgrid=True,
            gridwidth=1,
            gridcolor="rgba(156, 163, 175, 0.2)",
        ),
        template=None,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(249, 250, 251, 0.5)",
        uirevision="indicators",
        hovermode="closest",
        legend=dict(
            groupclick="togglegroup",
            orientation="h", yanchor="bottom", y=1.06, xanchor="left", x=0,
            bgcolor="rgba(255,255,255,0.95)", bordercolor="#cbd5e1", borderwidth=1.5, font=dict(size=10),
        ),
        dragmode=False,
    )
    
    fig.update_xaxes(fixedrange=True)
    fig.update_yaxes(fixedrange=True)

    return fig


def build_transcript_children(df, active_section_id, show_all):
    """
    Build transcript cards.
    show_all=True: show all
    show_all=False: only show active and one above and below
    """
    if df.empty:
        return [html.Div("No transcript data available", className="transcript-empty")]

    df_sorted = df.sort_values("timestamp_sec").reset_index(drop=True)

    idx = df_sorted.index[df_sorted["section_id"] == active_section_id]
    if len(idx) == 0:
        center_i = 0
        display_section_id = int(df_sorted.iloc[0]["section_id"])
    else:
        center_i = int(idx[0])
        display_section_id = active_section_id
    
    active_timestamp = float(df_sorted.iloc[center_i]["timestamp_sec"])

    if show_all:
        start_i = 0
        end_i = len(df_sorted) - 1
    else:
        start_i = max(center_i - 1, 0)
        end_i = min(center_i + 1, len(df_sorted) - 1)

    children = []
    is_pre = "presentation_text" in df.columns

    for i in range(start_i, end_i + 1):
        row = df_sorted.iloc[i]
        sec_id = int(row["section_id"])

        classes = ["transcript-line"]
        
        if sec_id == display_section_id:
            classes.append("transcript-active")
        else:
            row_timestamp = float(row["timestamp_sec"])
            if row_timestamp < active_timestamp:
                classes.append("transcript-above")
            else:
                classes.append("transcript-below")

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

        cp_badges = []

        if is_pre:
            if int(row.get("is_changepoint", 0)) == 1:
                cp_badges.append(html.Span("Change Point", className="cp-tag cp-tag-sentence"))
        else:
            dims = ["assertive", "cautious", "optimistic", "specific", "clear", "relevant"]
            for d in dims:
                cp_col = f"qa_{d}_change_point"
                if (cp_col in df_sorted.columns) and int(row.get(cp_col, 0) or 0) == 1:
                    colors = QA_CP_BADGE_COLORS.get(d, {"bg": "#F5F5F5", "border": "#9E9E9E", "text": "#424242"})
                    cp_badges.append(
                        html.Span(
                            f"{d.capitalize()} Change Point",
                            className="cp-tag cp-tag-qa",
                            style={
                                "backgroundColor": colors["bg"],
                                "borderColor": colors["border"],
                                "color": colors["text"],
                                "borderWidth": "2px",
                                "borderStyle": "solid",
                            },
                        )
                    )

            if (not cp_badges) and int(row.get("is_changepoint", 0)) == 1:
                cp_badges.append(html.Span("Change Point", className="cp-tag cp-tag-sentence"))

        if cp_badges:
            meta_rows.append(html.Div(cp_badges, className="cp-row"))

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
                                      title=(q_name + " " + q_title).strip() or "Question"),
                            html.Div(q_text, className="qa-bubble qa-bubble-q"),
                        ],
                        className="qa-line qa-line-q",
                    ),
                    html.Div(
                        [
                            html.Span("A", className="qa-label qa-label-a",
                                      title=(a_name + " " + a_title).strip() or "Answer"),
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

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],  title="TRACE")
server = app.server

app.layout = dbc.Container(
    [
        dcc.Store(id="store-pre-data"),
        dcc.Store(id="store-qa-data"),
        dcc.Store(id="store-panel-data"),
        dcc.Store(id="store-global-data"),
        dcc.Store(id="store-active-point", data={"mode": "pre", "section_id": 0}),
        dcc.Store(id="store-active-transcript", data=0),
        dcc.Store(id="store-show-all", data=False),
        dcc.Store(id="store-quarter", data=1),
        dcc.Store(id="store-indicator-mode", data="quote"),
        dcc.Store(id="store-scroll-dummy"),
        dcc.Store(id="store-comment-scroll-dummy"),
        dcc.Store(id="store-legend-tone", data={}),
        dcc.Store(id="store-legend-indicators", data={}),
        dcc.Store(id="store-tic"),

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
                                className="show-all-control",
                                children=[
                                    html.Div(
                                        [
                                            dcc.Checklist(
                                                id="checkbox-show-all",
                                                options=[{"label": "", "value": "show_all"}],
                                                value=[],
                                                className="show-all-checkbox",
                                            ),
                                            html.Span("Show All Transcripts", className="show-all-label"),
                                        ],
                                        className="show-all-inner",
                                    ),
                                ],
                            ),
                            html.Div(
                                id="transcript-container",
                                className="transcript-container",
                                children=[html.Div(id="transcript-inner")],
                            ),
                            
                            html.Div(
                                id="scroll-buttons",
                                className="scroll-buttons",
                                children=[
                                    html.Button("↑", id="btn-scroll-top", className="scroll-btn", title="Scroll to Top"),
                                    html.Button("↓", id="btn-scroll-bottom", className="scroll-btn", title="Scroll to Bottom"),
                                ],
                            ),
                        ],
                        className="dash-card transcript-card",
                    ),
                    width=3,
                    style={"padding": "10px", "height": "100%", "display": "flex", "flexDirection": "column"},
                ),
                dbc.Col(
                    [
                        html.Div(
                            [
                                html.H5("Cumulative Tone", className="block-title"),
                                html.Div(id="tone-time-label", className="tone-time-label"),
                                dcc.Graph(id="graph-tone", config={"displayModeBar": False, "doubleClick": False, "showAxisDragHandles": False, "showAxisRangeEntryBoxes": False},
                                          className="tone-graph"),
                            ],
                            className="dash-card chart-card",
                            style={"flex": "1", "marginBottom": "8px"},
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
                                dcc.Graph(id="graph-indicators", config={"displayModeBar": False, "doubleClick": False, "showAxisDragHandles": False, "showAxisRangeEntryBoxes": False},
                                          className="indicator-graph"),
                            ],
                            className="dash-card chart-card",
                            style={"flex": "1"},
                        ),
                    ],
                    width=6,
                    style={"padding": "10px", "height": "100%", "display": "flex", "flexDirection": "column"},
                ),
                dbc.Col(
                    [
                        html.Div("TRACE", className="top-header"),
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
                                                "fontSize": "20px", "fontWeight": "500",
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
                                    clearable=False,
                                    searchable=False,
                                    id="dropdown-company",
                                    className="company-dropdown-fixed",
                                    optionHeight=35,
                                    maxHeight=250,
                                    style={"marginTop": "10px"},
                                ),
                            ],
                            className="dash-card dropdown-card-fixed",
                            style={"marginBottom": "8px", "padding": "10px 15px", "position": "relative"},
                        ),
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H5("Comment", className="block-title", style={"marginBottom": "0"}),
                                        html.Div(
                                            [
                                                dbc.Button("Summary", id="btn-comment-summary", n_clicks=0,
                                                          className="comment-tab active-comment-tab"),
                                                dbc.Button("Change Point", id="btn-comment-cp", n_clicks=0,
                                                          className="comment-tab"),
                                            ],
                                            className="comment-tab-row",
                                        ),
                                    ],
                                    style={"display": "flex", "justifyContent": "space-between", "alignItems": "center", "marginBottom": "8px"},
                                ),
                                dcc.Markdown(
                                    id="comment-content",
                                    className="comment-content",
                                    children="",
                                ),
                                
                                html.Div(
                                    id="comment-scroll-buttons",
                                    className="comment-scroll-buttons",
                                    children=[
                                        html.Button("↑", id="btn-comment-scroll-top", className="comment-scroll-btn", title="Scroll to Top"),
                                        html.Button("↓", id="btn-comment-scroll-bottom", className="comment-scroll-btn", title="Scroll to Bottom"),
                                    ],
                                ),
                            ],
                            className="dash-card comment-card",
                            style={"flex": "1", "padding": "8px 12px", "display": "flex",
                                   "flexDirection": "column", "minHeight": "0"},
                        ),
                        dcc.Store(id="store-comment-mode", data="summary"),
                    ],
                    width=3,
                    style={"padding": "10px", "height": "100%", "display": "flex",
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
    prevent_initial_call=False,
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
    prevent_initial_call=True,
)
def switch_indicator_mode(nq, nt, current_mode):
    mode = "trade" if ctx.triggered_id == "btn-ind-trade" else "quote"
    quote_class = "indicator-tab active" if mode == "quote" else "indicator-tab"
    trade_class = "indicator-tab active" if mode == "trade" else "indicator-tab"
    return mode, quote_class, trade_class


@app.callback(
    Output("store-comment-mode", "data"),
    Output("btn-comment-summary", "className"),
    Output("btn-comment-cp", "className"),
    Input("btn-comment-summary", "n_clicks"),
    Input("btn-comment-cp", "n_clicks"),
    prevent_initial_call=True,
)
def switch_comment_mode(n_summary, n_cp):
    mode = "cp" if ctx.triggered_id == "btn-comment-cp" else "summary"
    summary_class = "comment-tab active-comment-tab" if mode == "summary" else "comment-tab"
    cp_class = "comment-tab active-comment-tab" if mode == "cp" else "comment-tab"
    return mode, summary_class, cp_class


@app.callback(
    Output("comment-content", "children"),
    Input("store-comment-mode", "data"),
    Input("store-tic", "data"),
    Input("store-quarter", "data"),
    Input("store-active-point", "data"),
    prevent_initial_call=False,
)
def update_comment_content(comment_mode, tic, quarter, active_point):
    if not tic or not quarter:
        return ""
    
    mode = active_point.get("mode", "pre") if active_point else "pre"
    comment_mode = comment_mode or "summary"
    
    return load_comment_md(tic, YEAR_DEFAULT, quarter, comment_mode, mode)


@app.callback(
    Output("store-pre-data", "data"),
    Output("store-qa-data", "data"),
    Output("store-panel-data", "data"),
    Output("store-global-data", "data"),
    Output("store-active-point", "data"),
    Output("store-active-transcript", "data"),
    Output("tone-time-label", "children"),
    Output("store-tic", "data"),
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
    State("store-tic", "data"),
    prevent_initial_call=False,
)
def unified_data_and_active(
    tic, quarter, tone_click, ind_click, transcript_clicks,
    tab_pre, tab_qa,
    pre_data, qa_data, panel_data, global_data, active_point, active_transcript, stored_tic,
):
    triggered = ctx.triggered_id
    
    if triggered == "graph-tone" and tone_click is None:
        raise dash.exceptions.PreventUpdate
    if triggered == "graph-indicators" and ind_click is None:
        raise dash.exceptions.PreventUpdate

    if triggered in ["dropdown-company", "store-quarter", None]:
        if tic is None: 
            raise dash.exceptions.PreventUpdate
            
        year = YEAR_DEFAULT
        pre_df = load_pre_df(tic, year, quarter)
        qa_df = load_qa_df(tic, year, quarter)
        
        default_mode = "pre" if not pre_df.empty else "qa"
        panel_df = load_panel_df(tic, year, quarter, mode=default_mode)
        
        global_df = build_global_df(pre_df, qa_df)
        
        if not pre_df.empty:
            sec_id, mode = choose_default_changepoint(pre_df), "pre"
        else:
            sec_id, mode = choose_default_changepoint(qa_df), "qa"
            
        active_point = {"mode": mode, "section_id": int(sec_id)}
        active_transcript = int(sec_id)
        
        row = load_calendar_row(tic, year, quarter)
        label = ""
        if row is not None:
            start, end = row.get("timestamp_et_start", ""), row.get("timestamp_et_end", "")
            if pd.notna(start) and pd.notna(end):
                try:
                    start_dt = pd.to_datetime(start)
                    end_dt = pd.to_datetime(end)

                    label = html.Div(
                        [
                            html.Span("📅 ", style={"marginRight": "4px"}),
                            html.Span(f"{start_dt.strftime('%Y-%m-%d %H:%M')}", style={"fontWeight": "600"}),
                            html.Span(" to ", style={"margin": "0 4px", "color": "#6b7280"}),
                            html.Span(f"{end_dt.strftime('%H:%M')}", style={"fontWeight": "600"}),
                            html.Span(" ET", style={"marginLeft": "4px", "color": "#6b7280", "fontSize": "10px"}),
                        ],
                        style={
                            "display": "flex",
                            "alignItems": "center",
                            "fontSize": "11px",
                        }
                    )
                except: 
                    label = f"[{start}, {end}] ET"
        
        return (
            pre_df.to_dict("records"), 
            qa_df.to_dict("records"), 
            panel_df.to_dict("records"), 
            global_df.to_dict("records"), 
            active_point, 
            active_transcript, 
            label,
            tic,
        )

    pre_df = _df_from_store(pre_data)
    qa_df = _df_from_store(qa_data)
    global_df = _df_from_store(global_data)
    
    active_point = active_point or {"mode": "pre", "section_id": 0}
    active_transcript = active_transcript or int(active_point["section_id"])
    mode = active_point.get("mode", "pre")
    section_id = int(active_point.get("section_id", 0))
    
    reload_panel = False

    if triggered == "graph-tone" and tone_click:
        section_id = find_nearest_section_in_mode(global_df, tone_click["points"][0]["x"], mode)
        active_transcript = section_id
    elif triggered == "graph-indicators" and ind_click:
        clicked_time = ind_click["points"][0]["x"]
        section_id = find_nearest_section_in_mode(global_df, clicked_time, mode)
        active_transcript = section_id
    elif isinstance(triggered, dict) and triggered.get("type") == "transcript-item":
        trig = (ctx.triggered[0] if ctx.triggered else {})
        trig_val = trig.get("value")
        if trig_val is None or trig_val == 0:
            raise dash.exceptions.PreventUpdate
        section_id = active_transcript = int(triggered["index"])
    elif triggered == "btn-tab-pre":
        mode = "pre"
        section_id = choose_default_changepoint(pre_df) if not pre_df.empty else 0
        active_transcript = section_id
        reload_panel = True
    elif triggered == "btn-tab-qa":
        mode = "qa"
        section_id = choose_default_changepoint(qa_df) if not qa_df.empty else 0
        active_transcript = section_id
        reload_panel = True
    
    if reload_panel and stored_tic:
        panel_df = load_panel_df(stored_tic, YEAR_DEFAULT, quarter, mode=mode)
        panel_data = panel_df.to_dict("records")

    return (
        pre_data, qa_data, panel_data, global_data, 
        {"mode": mode, "section_id": int(section_id)}, 
        active_transcript, 
        dash.no_update,
        dash.no_update,
    )


@app.callback(
    Output("store-show-all", "data"),
    Input("checkbox-show-all", "value"),
    prevent_initial_call=True,
)
def update_show_all(checkbox_value):
    return "show_all" in (checkbox_value or [])


@app.callback(
    Output("store-legend-tone", "data"), 
    Input("graph-tone", "restyleData"),
    State("graph-tone", "figure"), 
    State("store-legend-tone", "data"), 
    prevent_initial_call=True
)
def persist_legend_state_tone(restyle_data, fig, state):
    if not restyle_data or not fig: 
        raise dash.exceptions.PreventUpdate
        
    state = state or {}
    changes, trace_idxs = restyle_data
    
    if isinstance(trace_idxs, int): 
        trace_idxs = [trace_idxs]
    
    vis_list = changes.get("visible")
    if not isinstance(vis_list, list):
        vis_list = [vis_list] * len(trace_idxs)
    
    for i, t_idx in enumerate(trace_idxs):
        if t_idx < len(fig["data"]):
            name = fig["data"][t_idx].get("name")
            if name: 
                state[name] = False if vis_list[i] == "legendonly" else True
                
    return state


@app.callback(
    Output("store-legend-indicators", "data"), 
    Input("graph-indicators", "restyleData"),
    State("graph-indicators", "figure"), 
    State("store-legend-indicators", "data"), 
    prevent_initial_call=True
)
def persist_legend_state_indicators(restyle_data, fig, state):
    if not restyle_data or not fig: 
        raise dash.exceptions.PreventUpdate
        
    state = state or {}
    changes, trace_idxs = restyle_data
    
    if isinstance(trace_idxs, int): 
        trace_idxs = [trace_idxs]
    
    vis_list = changes.get("visible")
    if not isinstance(vis_list, list):
        vis_list = [vis_list] * len(trace_idxs)
    
    for i, t_idx in enumerate(trace_idxs):
        if t_idx < len(fig["data"]):
            name = fig["data"][t_idx].get("name")
            if name: 
                state[name] = False if vis_list[i] == "legendonly" else True
                
    return state


@app.callback(
    Output("graph-tone", "figure"), 
    Output("graph-indicators", "figure"),
    Input("store-active-point", "data"),
    Input("store-indicator-mode", "data"),
    Input("store-legend-tone", "data"), 
    Input("store-legend-indicators", "data"),
    State("store-pre-data", "data"), 
    State("store-qa-data", "data"), 
    State("store-panel-data", "data"),
    State("store-tic", "data"),
    State("store-quarter", "data"),
    prevent_initial_call=False,
)
def update_graphs(active_point, indicator_mode, legend_tone, legend_indicators, pre_data, qa_data, panel_data, tic, quarter):
    pre_df = _df_from_store(pre_data)
    qa_df = _df_from_store(qa_data)
    panel_df = _df_from_store(panel_data)
    
    if not active_point:
        active_point = {"mode": "pre", "section_id": 0}
        
    mode = active_point.get("mode", "pre")
    section_id = int(active_point.get("section_id", 0))
    
    current_df = pre_df if mode == "pre" else qa_df
    
    seg_range = None
    active_ts = None
    
    if not current_df.empty and "timestamp_sec" in current_df.columns:
        s = float(current_df["timestamp_sec"].min())
        e = float(current_df["timestamp_sec"].max())
        if e > s: 
            seg_range = (s, e)
            
        r = current_df[current_df["section_id"] == section_id]
        if not r.empty and "timestamp_sec" in r.columns: 
            active_ts = float(r.iloc[0]["timestamp_sec"])
    
    # Calculate market times
    market_times = None
    if tic and quarter:
        cal_row = load_calendar_row(tic, YEAR_DEFAULT, quarter)
        if cal_row is not None:
            market_times = calculate_market_times(cal_row)
    
    tone_fig = build_tone_figure(pre_df, qa_df, mode, section_id, seg_range, legend_tone, market_times)
    ind_fig = build_indicator_figure(panel_df, active_ts, indicator_mode, seg_range, legend_indicators, market_times)
    
    return tone_fig, ind_fig


@app.callback(
    Output("transcript-inner", "children"), 
    Output("btn-tab-pre", "className"), 
    Output("btn-tab-qa", "className"),
    Input("store-active-transcript", "data"),
    Input("store-show-all", "data"),
    State("store-active-point", "data"),
    State("store-pre-data", "data"), 
    State("store-qa-data", "data"),
    prevent_initial_call=False,
)
def update_transcript(active_transcript, show_all, active_point, pre_data, qa_data):
    pre_df = _df_from_store(pre_data)
    qa_df = _df_from_store(qa_data)
    
    mode = active_point.get("mode", "pre") if active_point else "pre"
    section_id = int(active_point.get("section_id", 0)) if active_point else 0
    current_df = pre_df if mode == "pre" else qa_df

    display_section_id = section_id
    
    children = build_transcript_children(current_df, display_section_id, show_all)
    
    pre_class = "transcript-tab active" if mode == "pre" else "transcript-tab"
    qa_class = "transcript-tab active" if mode == "qa" else "transcript-tab"
    
    return children, pre_class, qa_class


# Auto-scroll and show/hide buttons
app.clientside_callback(
    """function(at, show_all, ch) {
        if (!ch) return [null, {'display': 'none'}];

        var container = document.getElementById('transcript-container');
        if (!container) return [null, {'display': 'none'}];
        
        var showButtons = false;
        if (show_all && container.scrollHeight > container.clientHeight) {
            var scrollTop = container.scrollTop;
            var scrollBottom = container.scrollHeight - container.clientHeight - scrollTop;
            if (scrollTop > 100 || scrollBottom > 100) {
                showButtons = true;
            }
        }

        requestAnimationFrame(function() {
            requestAnimationFrame(function() {
                var activeEls = container.getElementsByClassName('transcript-active');
                if (!activeEls.length) return;
                
                var activeEl = activeEls[0];
                var contRect = container.getBoundingClientRect();
                var actRect = activeEl.getBoundingClientRect();

                var scrollOffset;
                if (actRect.height > contRect.height * 0.5) {
                    scrollOffset = actRect.top - contRect.top - 20;
                } else {
                    scrollOffset = (actRect.top + actRect.bottom)/2 - (contRect.top + contRect.bottom)/2;
                }

                if (Math.abs(scrollOffset) > 5) {
                    container.scrollBy({
                        top: scrollOffset,
                        behavior: 'smooth'
                    });
                }
            });
        });
        
        return [null, {'display': showButtons ? 'flex' : 'none'}];
    }""",
    Output("store-scroll-dummy", "data"),
    Output("scroll-buttons", "style"),
    Input("store-active-transcript", "data"),
    Input("store-show-all", "data"),
    Input("transcript-inner", "children"),
)




# Scroll buttons
app.clientside_callback(
    """function(n_top, n_bottom) {
        var container = document.getElementById('transcript-container');
        if (!container) return null;
        
        var triggeredId = dash_clientside.callback_context.triggered[0].prop_id;
        
        if (triggeredId.includes('btn-scroll-top')) {
            container.scrollTo({top: 0, behavior: 'smooth'});
        } else if (triggeredId.includes('btn-scroll-bottom')) {
            container.scrollTo({top: container.scrollHeight, behavior: 'smooth'});
        }
        
        return null;
    }""",
    Output("store-scroll-dummy", "data", allow_duplicate=True),
    Input("btn-scroll-top", "n_clicks"),
    Input("btn-scroll-bottom", "n_clicks"),
    prevent_initial_call=True,
)

# Scroll to top when switching comment mode
app.clientside_callback(
    """function(comment_mode) {
        var commentContent = document.querySelector('.comment-content');
        if (commentContent) {
            commentContent.scrollTop = 0;
        }
        return null;
    }""",
    Output("store-comment-scroll-dummy", "data"),
    Input("store-comment-mode", "data"),
    prevent_initial_call=True,
)

# Comment scroll buttons visibility
app.clientside_callback(
    """function(comment_content) {
        var container = document.querySelector('.comment-content');
        if (!container) return {'display': 'none'};
        
        var showButtons = false;
        if (container.scrollHeight > container.clientHeight) {
            var scrollTop = container.scrollTop;
            var scrollBottom = container.scrollHeight - container.clientHeight - scrollTop;
            if (scrollTop > 100 || scrollBottom > 100) {
                showButtons = true;
            }
        }
        
        return {'display': showButtons ? 'flex' : 'none'};
    }""",
    Output("comment-scroll-buttons", "style"),
    Input("comment-content", "children"),
)

# Comment scroll buttons click handler
app.clientside_callback(
    """function(n_top, n_bottom) {
        var container = document.querySelector('.comment-content');
        if (!container) return null;
        
        var triggeredId = dash_clientside.callback_context.triggered[0].prop_id;
        
        if (triggeredId.includes('btn-comment-scroll-top')) {
            container.scrollTo({top: 0, behavior: 'smooth'});
        } else if (triggeredId.includes('btn-comment-scroll-bottom')) {
            container.scrollTo({top: container.scrollHeight, behavior: 'smooth'});
        }
        
        return null;
    }""",
    Output("store-comment-scroll-dummy", "data", allow_duplicate=True),
    Input("btn-comment-scroll-top", "n_clicks"),
    Input("btn-comment-scroll-bottom", "n_clicks"),
    prevent_initial_call=True,
)

if __name__ == "__main__":
    app.run_server(debug=True)