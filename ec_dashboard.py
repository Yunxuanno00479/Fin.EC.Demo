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

# Quote / Trade 指標白名單
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

# Quarter buttons style（藍綠＝選取，灰白＝未選）
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


# Key Indicators 線條顏色（Quote 用一組、Trade 用一組）
INDICATOR_COLORS = {
    "Bid Ask Spread": "#2563eb",            # 藍
    "Order Book Imbalance": "#ea580c",      # 橘
    "Quote Revision Frequency": "#16a34a",  # 綠
    "Quote Volatility": "#9333ea",          # 紫
    "trade count": "#dc2626",               # 紅
    "trade volume": "#0f766e",              # 深青
    "trade vwap": "#0891b2",                # 藍綠
}

# Q&A cumulative 線條顏色
QA_DIM_COLORS = {
    "assertive": "#ff7f0e",
    "cautious": "#2ca02c",
    "optimistic": "#9467bd",
    "specific": "#8c564b",
    "clear": "#e377c2",
    "relevant": "#7f7f7f",
}

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
    """Load pre (presentation) data for given ticker / year / quarter."""
    path = DATA_DIR / "Pre_finbert_tone" / f"{tic}_{year}_pre.csv"
    if not path.exists():
        return pd.DataFrame()

    df = pd.read_csv(path).copy()
    df = df[df["quarter"] == quarter].copy()
    if df.empty:
        return df

    df["section_id"] = df["sent_section_id"].astype(int)
    df["timestamp_p"] = df["timestamp_p"].astype(float)
    df["timestamp_sec"] = df["timestamp_p"]

    df["display_text"] = df["presentation_text"].fillna("")
    df["cumulative_tone"] = df["tone_cumulative"].astype(float)

    if "sentence_level_CP" not in df.columns:
        df["sentence_level_CP"] = 0
    if "trend_level_CP" not in df.columns:
        df["trend_level_CP"] = 0

    cp_any = (df["sentence_level_CP"] == 1) | (df["trend_level_CP"] == 1)
    df["is_changepoint"] = cp_any.astype(int)

    return df


def load_qa_df(tic: str, year: int, quarter: int) -> pd.DataFrame:
    """Load QA (subjective) data for given ticker / year / quarter."""
    path = DATA_DIR / "QA_subjectiveqa" / f"{tic}_{year}_qa.csv"
    if not path.exists():
        return pd.DataFrame()

    df = pd.read_csv(path).copy()
    df = df[df["quarter"] == quarter].copy()
    if df.empty:
        return df

    df["section_id"] = df["sent_section_id"].astype(int)
    df["timestamp_Q"] = df["timestamp_Q"].astype(float)
    df["timestamp_A"] = df["timestamp_A"].astype(float)
    df["timestamp_sec"] = df["timestamp_Q"]

    q = df["question_text"].fillna("")
    a = df["answer_text"].fillna("")
    df["display_text"] = "Q: " + q.astype(str) + "\nA: " + a.astype(str)

    cp_cols = [c for c in df.columns if c.endswith("_sentence_level_CP")]
    if cp_cols:
        df["is_changepoint"] = df[cp_cols].eq(1).any(axis=1).astype(int)
    else:
        df["is_changepoint"] = 0

    return df


def load_panel_df(tic: str, year: int, quarter: int) -> pd.DataFrame:
    """
    Load quote/trade panel data for given ticker / year / quarter.

    ✅ 現在的邏輯：
    - 優先使用 CSV 裡你新加的 timestamp_et_full（已經是 ET datetime）
    - 轉成秒數 timestamp_sec，給 Key Indicators 當 x 軸用
    - 若沒有 timestamp_et_full，就退回舊的 Timestamp_UTC 解析方式（保險）
    """
    path = DATA_DIR / "Panel_quote_trade" / f"{tic}_{year}_panel.csv"
    if not path.exists():
        return pd.DataFrame()

    df = pd.read_csv(path).copy()

    # year / quarter 篩選
    if "year" in df.columns:
        df = df[df["year"] == year]
    if "quarter" in df.columns:
        df = df[df["quarter"] == quarter]
    if df.empty:
        return df

    # ====== 1. 優先使用 timestamp_et_full（你剛剛已經寫回 CSV 的欄位） ======
    if "timestamp_et_full" in df.columns:
        # 轉成 datetime（包含時區，例如 -05:00）
        df["timestamp_et_full"] = pd.to_datetime(df["timestamp_et_full"], errors="coerce")

        # 有可能會有 NaT，先丟掉這些 row
        df = df.dropna(subset=["timestamp_et_full"])
        if df.empty:
            return df

        # 以第一個時間點當作 t = 0，換成「經過秒數」
        base = df["timestamp_et_full"].min()
        df["timestamp_sec"] = (df["timestamp_et_full"] - base).dt.total_seconds()

        return df

    # ====== 2. 如果還沒有 timestamp_et_full，就維持你之前的 fallback 行為 ======
    if "Timestamp_UTC" in df.columns:
        def parse_offset_to_sec(s: str) -> float:
            """
            原本的邏輯：把類似 "24:05.3" 或 "00:29.5" 轉成秒數
            - "MM:SS.s" → MM*60 + SS.s
            - "SS.s"    → 直接當秒數
            - "HH:MM:SS.s" → 保險處理
            """
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

    # ====== 3. 最後真的完全沒有時間欄位，就用 index 當時間軸（應該用不到，但保底） ======
    df["timestamp_sec"] = range(len(df))
    return df

def load_calendar_row(tic: str, year: int, quarter: int):
    path = DATA_DIR / "ec_calendar.csv"
    if not path.exists():
        return None

    df = pd.read_csv(path)
    row = df[
        (df["tic"] == tic) & (df["year"] == year) & (df["quarter"] == quarter)
    ].head(1)

    if row.empty:
        return None
    return row.iloc[0]

# ========= Load Markdown comment (from LLM_comment) =========

def load_comment_md(tic: str, year: int, quarter: int):
    """
    Load Markdown comment for a given company / year / quarter.
    Expected filename: {tic}_{year}_comment_{quarter}.md
    """
    from pathlib import Path
    md_path = DATA_DIR / "LLM_comment" / f"{tic}_{year}_comment_{quarter}.md"
    if not md_path.exists():
        return ""

    try:
        text = md_path.read_text(encoding="utf-8")
        return text
    except Exception:
        return "(Unable to read LLM comment file)"
    

def _df_from_store(data):
    return pd.DataFrame(data) if data else pd.DataFrame()


def build_global_df(pre_df: pd.DataFrame, qa_df: pd.DataFrame) -> pd.DataFrame:
    p = pre_df[["section_id", "timestamp_sec"]].copy()
    q = qa_df[["section_id", "timestamp_sec"]].copy()
    p["mode"] = "pre"
    q["mode"] = "qa"
    return pd.concat([p, q], ignore_index=True)


def choose_default_changepoint(df: pd.DataFrame) -> int:
    if df is None or df.empty:
        return 0
    if "is_changepoint" in df.columns:
        idx = df.index[df["is_changepoint"] == 1]
        if len(idx) > 0:
            return int(df.loc[idx[0], "section_id"])
    return int(df.iloc[0]["section_id"])


def find_nearest_point(global_df: pd.DataFrame, timestamp: float):
    if global_df.empty:
        return "pre", 0
    idx = (global_df["timestamp_sec"] - timestamp).abs().idxmin()
    row = global_df.loc[idx]
    return row["mode"], int(row["section_id"])


# ============================================================
# 3. Figures
# ============================================================


def build_tone_figure(pre_df, qa_df, active_mode, active_section_id, segment_range=None):
    fig = go.Figure()
    show_pre = (active_mode == "pre")
    show_qa = (active_mode == "qa")
        # -------- Presentation: 1 條 cumulative 線 --------
    if show_pre and not pre_df.empty:
        fig.add_trace(
            go.Scatter(
                x=pre_df["timestamp_sec"],
                y=pre_df["cumulative_tone"],
                mode="lines",                 # ✅ 只有線，不要滿天點
                name="Presentation",
                line=dict(shape="linear", width=2.5, color="#2563eb"),
                hovertemplate=(
                    "t=%{x:.0f}s<br>"
                    "cum tone=%{y:.3f}"
                    + (
                        "<br>label=%{customdata[0]}<br>score=%{customdata[1]:.3f}"
                        if set(["tone_label", "tone_score"]).issubset(pre_df.columns)
                        else ""
                    )
                    + "<extra></extra>"
                ),
                customdata=pre_df[["tone_label", "tone_score"]].values
                if set(["tone_label", "tone_score"]).issubset(pre_df.columns)
                else None,
            )
        )

        # sentence-level CP → 紅點 + 紅 dot 虛線
        if "sentence_level_CP" in pre_df.columns:
            m = pre_df["sentence_level_CP"] == 1
            if m.any():
                fig.add_trace(
                    go.Scatter(
                        x=pre_df.loc[m, "timestamp_sec"],
                        y=pre_df.loc[m, "cumulative_tone"],
                        mode="markers",
                        name="Sentence-level CP",
                        marker=dict(color="#d62728", size=8, symbol="circle"),
                        showlegend=True,
                    )
                )
                for ts in pre_df.loc[m, "timestamp_sec"]:
                    fig.add_shape(
                        type="line",
                        x0=ts,
                        x1=ts,
                        y0=0,
                        y1=1,
                        xref="x",
                        yref="paper",
                        line=dict(color="#d62728", width=1.5, dash="dot"),
                    )

        # trend-level CP → 紫 diamond + 紫 dash 虛線
        if "trend_level_CP" in pre_df.columns:
            m = pre_df["trend_level_CP"] == 1
            if m.any():
                fig.add_trace(
                    go.Scatter(
                        x=pre_df.loc[m, "timestamp_sec"],
                        y=pre_df.loc[m, "cumulative_tone"],
                        mode="markers",
                        name="Trend-level CP",
                        marker=dict(color="#9467bd", size=8, symbol="diamond"),
                        showlegend=True,
                    )
                )
                for ts in pre_df.loc[m, "timestamp_sec"]:
                    fig.add_shape(
                        type="line",
                        x0=ts,
                        x1=ts,
                        y0=0,
                        y1=1,
                        xref="x",
                        yref="paper",
                        line=dict(color="#9467bd", width=1.5, dash="dash"),
                    )

    # -------- Q&A: 6 cumulative tone dimensions --------
    if show_qa and not qa_df.empty:
        dims = [
            ("assertive", "qa_assertive_cumulative", "assertive_label", "assertive_score",
             "qa_assertive_sentence_level_CP"),
            ("cautious", "qa_cautious_cumulative", "cautious_label", "cautious_score",
             "qa_cautious_sentence_level_CP"),
            ("optimistic", "qa_optimistic_cumulative", "optimistic_label", "optimistic_score",
             "qa_optimistic_sentence_level_CP"),
            ("specific", "qa_specific_cumulative", "specific_label", "specific_score",
             "qa_specific_sentence_level_CP"),
            ("clear", "qa_clear_cumulative", "clear_label", "clear_score",
             "qa_clear_sentence_level_CP"),
            ("relevant", "qa_relevant_cumulative", "relevant_label", "relevant_score",
             "qa_relevant_sentence_level_CP"),
        ]

        for name, cum_col, lab_col, score_col, cp_col in dims:
            if cum_col not in qa_df.columns:
                continue

            color = QA_DIM_COLORS.get(name, None)

            customdata = (
                qa_df[[lab_col, score_col]].values
                if set([lab_col, score_col]).issubset(qa_df.columns)
                else None
            )

            fig.add_trace(
                go.Scatter(
                    x=qa_df["timestamp_sec"],
                    y=qa_df[cum_col],
                    mode="lines+markers",
                    name=name.capitalize(),
                    line=dict(width=2, color=color),
                    marker=dict(size=5, color=color),
                    customdata=customdata,
                    hovertemplate=(
                        "t=%{x:.0f}s<br>"
                        f"{name} cum=%{{y:.3f}}"
                        + (
                            "<br>label=%{customdata[0]}<br>score=%{customdata[1]:.3f}"
                            if customdata is not None
                            else ""
                        )
                        + "<extra></extra>"
                    ),
                )
            )

            # sentence-level CP：以該維度色系畫開圓點 + dot 虛線
            if cp_col in qa_df.columns:
                m = qa_df[cp_col] == 1
                if m.any():
                    fig.add_trace(
                        go.Scatter(
                            x=qa_df.loc[m, "timestamp_sec"],
                            y=qa_df.loc[m, cum_col],
                            mode="markers",
                            name=f"{name} CP",
                            marker=dict(color=color, size=7, symbol="circle-open"),
                            showlegend=False,
                        )
                    )
                    for ts in qa_df.loc[m, "timestamp_sec"]:
                        fig.add_shape(
                            type="line",
                            x0=ts,
                            x1=ts,
                            y0=0,
                            y1=1,
                            xref="x",
                            yref="paper",
                            line=dict(color=color, width=1, dash="dot"),
                        )

    # -------- active 垂直線 --------
    df = pre_df if active_mode == "pre" else qa_df
    if not df.empty:
        r = df[df["section_id"] == active_section_id]
        if not r.empty:
            ts = float(r.iloc[0]["timestamp_sec"])
            fig.add_shape(
                type="line",
                x0=ts,
                x1=ts,
                y0=0,
                y1=1,
                xref="x",
                yref="paper",
                line=dict(color="black", width=2),
            )

    # x 軸範圍：與 Key Indicators 共用 segment_range
    if segment_range is not None:
        x_min, x_max = segment_range
        if x_min is not None and x_max is not None and x_min < x_max:
            span = x_max - x_min
            dtick = max(span / 5.0, 1.0)
            fig.update_xaxes(
                range=[x_min, x_max],
                tickmode="linear",
                tick0=x_min,
                dtick=dtick,
            )

    fig.update_layout(
        margin=dict(l=40, r=20, t=28, b=40),
        xaxis_title="timestamp",
        yaxis_title="cumulative tone",
        template=None,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="left",
            x=0,
            bgcolor="rgba(255,255,255,0.9)",
            bordercolor="#e5e7eb",
            borderwidth=1,
            font=dict(size=10),
        ),
    )
    return fig

def build_indicator_figure(panel_df, active_timestamp, indicator_mode, segment_range=None):
    fig = go.Figure()

    if panel_df.empty:
        fig.update_layout(
            margin=dict(l=40, r=20, t=28, b=40),
            xaxis_title="timestamp",
            yaxis_title="key indicators",
            template=None,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            legend=dict(
                orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0,
                bgcolor="rgba(255,255,255,0.9)", bordercolor="#e5e7eb", borderwidth=1, font=dict(size=10),
            ),
        )
        return fig

    # 選擇 Quote / Trade 欄位
    if indicator_mode == "trade":
        allowed = TRADE_COLS
    else:
        indicator_mode = "quote"
        allowed = QUOTE_COLS

    cols = [c for c in allowed if c in panel_df.columns]
    x = panel_df["timestamp_sec"]

    for col in cols:
        fig.add_trace(
            go.Scatter(
                x=x,
                y=panel_df[col],
                mode="lines",
                name=col,
                line=dict(width=2, color=INDICATOR_COLORS.get(col, None)),
                hovertemplate="t=%{x:.0f}s<br>%{y:.3f}<extra></extra>",
            )
        )

    if active_timestamp is not None:
        fig.add_shape(
            type="line",
            x0=active_timestamp,
            x1=active_timestamp,
            y0=0,
            y1=1,
            xref="x",
            yref="paper",
            line=dict(color="black", width=2),
        )

    # x 軸跟 Tone 同一個 range
    if segment_range is not None:
        x_min, x_max = segment_range
        if x_min is not None and x_max is not None and x_min < x_max:
            span = x_max - x_min
            dtick = max(span / 5.0, 1.0)
            fig.update_xaxes(
                range=[x_min, x_max],
                tickmode="linear",
                tick0=x_min,
                dtick=dtick,
            )

    fig.update_layout(
        margin=dict(l=40, r=20, t=28, b=40),
        xaxis_title="timestamp",
        yaxis_title="key indicators",
        template=None,  # ✅ 改成透明背景，和上圖一致
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="left",
            x=0,
            bgcolor="rgba(255,255,255,0.9)",
            bordercolor="#e5e7eb",
            borderwidth=1,
            font=dict(size=10),
        ),
    )
    return fig
def build_transcript_children(df, active_section_id, scroll_state):
    """Build transcript cards around active_section_id with more/less window."""
    if df.empty:
        return [html.Div("No transcript data", className="transcript-empty")]

    scroll_state = scroll_state or {}
    above_more = bool(scroll_state.get("above_more", False))
    below_more = bool(scroll_state.get("below_more", False))

    df_sorted = df.sort_values("timestamp_sec").reset_index(drop=True)
    idx = df_sorted.index[df_sorted["section_id"] == active_section_id]
    center_i = int(idx[0]) if len(idx) > 0 else 0

    # 視窗大小設定
    base_above = 1
    base_below = 1
    more_above = 5
    more_below = 5

    start_i = max(center_i - base_above, 0)
    end_i = min(center_i + base_below, len(df_sorted) - 1)

    if above_more:
        start_i = max(center_i - (base_above + more_above), 0)
    if below_more:
        end_i = min(center_i + (base_below + more_below), len(df_sorted) - 1)

    children = []
    is_pre = "presentation_text" in df.columns  # Presentation vs QA

    for i in range(start_i, end_i + 1):
        row = df_sorted.iloc[i]
        sec_id = int(row["section_id"])

        classes = ["transcript-line"]

        ts_row = float(row["timestamp_sec"])
        ts_active = float(df[df["section_id"] == active_section_id]["timestamp_sec"].iloc[0])

        if ts_row < ts_active:
            classes.append("transcript-above")
        elif ts_row == ts_active:
            classes.append("transcript-active")
        else:
            classes.append("transcript-below")

        # ---------- Meta rows ----------
        meta_rows = []

        if is_pre:
            speaker_name = str(row.get("speaker_name_P", "") or "").strip()
            speaker_title = str(row.get("speaker_title_P", "") or "").strip()
            speaker_spans = []
            if speaker_name:
                speaker_spans.append(
                    html.Span(speaker_name, className="speaker-name")
                )
            if speaker_title:
                speaker_spans.append(
                    html.Span(speaker_title, className="speaker-title")
                )
            if speaker_spans:
                meta_rows.append(
                    html.Div(speaker_spans, className="transcript-meta-row")
                )
        else:
            # Q&A：保留 speaker 資訊做 tooltip 用
            q_name = str(row.get("speaker_name_Q", "") or "").strip()
            q_title = str(row.get("speaker_title_Q", "") or "").strip()
            a_name = str(row.get("speaker_name_A", "") or "").strip()
            a_title = str(row.get("speaker_title_A", "") or "").strip()
            # 不再在 meta_row 畫 Q/A 圓圈，改成放在文字左側氣泡

        # ---------- CP badge row ----------
        cp_badges = []
        if is_pre:
            if int(row.get("sentence_level_CP", 0)) == 1:
                cp_badges.append(
                    html.Span("Sentence Change Point", className="cp-tag cp-tag-sentence")
                )
            if int(row.get("trend_level_CP", 0)) == 1:
                cp_badges.append(
                    html.Span("Trend Change Point", className="cp-tag cp-tag-trend")
                )
        else:
            if int(row.get("is_changepoint", 0)) == 1:
                cp_badges.append(
                    html.Span("Sentence Change Point", className="cp-tag cp-tag-sentence")
                )

        if cp_badges:
            meta_rows.append(html.Div(cp_badges, className="cp-row"))

        # ---------- 文字本體 ----------
        if is_pre:
            text = str(row.get("presentation_text", "") or "")
            text_block = html.Div(text, className="transcript-text")
        else:
            q_text = str(row.get("question_text", "") or "").strip()
            a_text = str(row.get("answer_text", "") or "").strip()

            # 💬 Q/A 氣泡對話 layout
            text_block = html.Div(
                [
                    # Q line
                    html.Div(
                        [
                            html.Span(
                                "Q",
                                className="qa-label qa-label-q",
                                title=(q_name + " " + q_title).strip(),
                            ),
                            html.Div(
                                q_text,
                                className="qa-bubble qa-bubble-q",
                            ),
                        ],
                        className="qa-line qa-line-q",
                    ),
                    # A line
                    html.Div(
                        [
                            html.Span(
                                "A",
                                className="qa-label qa-label-a",
                                title=(a_name + " " + a_title).strip(),
                            ),
                            html.Div(
                                a_text,
                                className="qa-bubble qa-bubble-a",
                            ),
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
# 4. App Layout（三欄骨架）
# ============================================================

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        # hidden stores
        dcc.Store(id="store-pre-data"),
        dcc.Store(id="store-qa-data"),
        dcc.Store(id="store-panel-data"),
        dcc.Store(id="store-global-data"),
        dcc.Store(id="store-active-point"),
        dcc.Store(id="store-scroll-state", data={"above_more": False, "below_more": False}),
        dcc.Store(id="store-quarter", data=1),
        dcc.Store(id="store-indicator-mode", data="quote"),
        dcc.Store(id="store-scroll-dummy"),  # for clientside scroll centering

        dbc.Row(
            [
                # --- 左側 Transcript 區 ---
                dbc.Col(
                    html.Div(
                        [
                            html.H5("Transcript", className="block-title"),

                            html.Div(
                                className="transcript-tab-row",
                                children=[
                                    dbc.Button(
                                        "Presentation",
                                        id="btn-tab-pre",
                                        n_clicks=0,
                                        className="transcript-tab active",
                                        title="Switch to Presentation transcript",
                                    ),
                                    dbc.Button(
                                        "Q&A",
                                        id="btn-tab-qa",
                                        n_clicks=0,
                                        className="transcript-tab",
                                        title="Switch to Q&A transcript",
                                    ),
                                ],
                            ),

                            html.Div(
                                className="more-less-row top",
                                children=[
                                    html.Button(
                                        "+ More",
                                        id="btn-more-top",
                                        n_clicks=0,
                                        className="more-less-btn",
                                        title="Show more sentences above",
                                    ),
                                    html.Button(
                                        "- Less",
                                        id="btn-less-top",
                                        n_clicks=0,
                                        className="more-less-btn",
                                        title="Collapse above; keep only previous line and current line",
                                    ),
                                ],
                            ),

                            # 這裡用外層容器 + 內層 transcript-inner，
                            # 之後只更新 inner 的 children，scrollTop 不會被 reset
                            html.Div(
                                id="transcript-container",
                                className="transcript-container",
                                children=[
                                    html.Div(id="transcript-inner")
                                ],
                            ),

                            html.Div(
                                className="more-less-row bottom",
                                children=[
                                    html.Button(
                                        "+ More",
                                        id="btn-more-bottom",
                                        n_clicks=0,
                                        className="more-less-btn",
                                        title="Show more sentences below",
                                    ),
                                    html.Button(
                                        "- Less",
                                        id="btn-less-bottom",
                                        n_clicks=0,
                                        className="more-less-btn",
                                        title="Collapse below; keep only next line and current line",
                                    ),
                                ],
                            ),
                        ],
                        className="dash-card transcript-card",
                    ),
                    width=3,
                    style={"padding": "10px", "height": "100%"},
                ),

                # --- 中間：兩張圖 ---
                dbc.Col(
                    [
                        html.Div(
                            [
                                html.H5("Cumulative Tone", className="block-title"),
                                html.Div(id="tone-time-label", className="tone-time-label"),
                                dcc.Graph(
                                    id="graph-tone",
                                    config={"displayModeBar": False},
                                    className="tone-graph",
                                ),
                            ],
                            className="dash-card chart-card",
                            style={"height": "calc(50% - 6px)", "marginBottom": "8px"},
                        ),
                        html.Div(
                            [
                                html.H5("Key Indicators", className="block-title"),

                                # Quote / Trade tabs
                                html.Div(
                                    className="indicator-tab-row",
                                    children=[
                                        html.Button(
                                            "Quote",
                                            id="btn-ind-quote",
                                            n_clicks=0,
                                            className="indicator-tab active",
                                            title="Show quote-based microstructure indicators",
                                        ),
                                        html.Button(
                                            "Trade",
                                            id="btn-ind-trade",
                                            n_clicks=0,
                                            className="indicator-tab",
                                            title="Show trade-based microstructure indicators",
                                        ),
                                    ],
                                ),

                                dcc.Graph(
                                    id="graph-indicators",
                                    config={"displayModeBar": False},
                                    className="indicator-graph",
                                ),
                            ],
                            className="dash-card chart-card",
                            style={"height": "calc(50% - 6px)"},
                        ),
                    ],
                    width=6,
                    style={"padding": "10px", "height": "100%"},
                ),

                # --- 右側 Year / Quarter / Company / Comment ---
                dbc.Col(
                    [
                        html.Div("EARNINGS CALL DASHBOARD", className="top-header"),

                        dbc.Row(
                            [
                                dbc.Col(
                                    html.Div(
                                        [
                                            html.Label(
                                                "Year",
                                                style={
                                                    "position": "absolute",
                                                    "top": "5px",
                                                    "left": "10px",
                                                    "font-family": "Calibri",
                                                    "fontSize": "13px",
                                                    "color": "#888",
                                                    "fontWeight": "400",
                                                },
                                            ),
                                            html.Div(
                                                str(YEAR_DEFAULT),
                                                style={
                                                    "font-family": "Calibri",
                                                    "fontSize": "22px",
                                                    "fontWeight": "550",
                                                    "marginLeft": "10px",
                                                    "marginTop": "8px"
                                                },
                                            ),
                                        ],
                                        className="dash-card",
                                        style={
                                            "padding": "5px",
                                            "height": "50px",
                                            "display": "flex",
                                            "alignItems": "center",
                                            "justifyContent": "center",
                                            "position": "relative",
                                        },
                                    ),
                                    width=4,
                                    style={"paddingRight": "8px", "height": "50px"},
                                ),
                                dbc.Col(
                                    dbc.ButtonGroup(
                                        [
                                            dbc.Button(
                                                "Q1",
                                                id="btn-q1",
                                                n_clicks=0,
                                                style=STYLE_ACTIVE,
                                            ),
                                            dbc.Button(
                                                "Q2",
                                                id="btn-q2",
                                                n_clicks=0,
                                                style=STYLE_INACTIVE,
                                            ),
                                            dbc.Button(
                                                "Q3",
                                                id="btn-q3",
                                                n_clicks=0,
                                                style=STYLE_INACTIVE,
                                            ),
                                            dbc.Button(
                                                "Q4",
                                                id="btn-q4",
                                                n_clicks=0,
                                                style=STYLE_INACTIVE,
                                            ),
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
                                html.Label(
                                    "Company",
                                    style={
                                        "font-family": "Calibri",
                                        "fontSize": "13px",
                                        "color": "#888",
                                        "fontWeight": "400",
                                        "position": "absolute",
                                        "top": "5px",
                                        "left": "10px",
                                    },
                                ),
                                dcc.Dropdown(
                                    options=DROPDOWN_OPTIONS,
                                    value=DROPDOWN_OPTIONS[0]["value"]
                                    if DROPDOWN_OPTIONS
                                    else None,
                                    clearable=True,
                                    searchable=False,
                                    className="clean-dropdown",
                                    style={"border": "none", "marginTop": "10px"},
                                    id="dropdown-company",
                                ),
                            ],
                            className="dash-card dropdown-card",
                            style={
                                "marginBottom": "8px",
                                "padding": "10px 15px",
                                "position": "relative",
                            },
                        ),

                        # Comment 卡片：吃掉右側剩餘高度
                        html.Div(
                            [
                                html.H5("Comment", className="block-title"),
                                dcc.Markdown(id="comment-content", className="comment-content", children="",
                                             style={
                                                "flex": "1",
                                                "minHeight": "0",     # 讓 flexbox 允許內容縮小，scroll 才能生效
                                                },
                                            ),
                            ],
                            className="dash-card comment-card",
                            style={
                                "flex": "1",
                                "padding": "8px 12px",
                                "display": "flex",
                                "flexDirection": "column",
                            },
                        ),
                    ],
                    width=3,
                    style={
                        "padding": "8px",
                        "height": "100%",
                        "display": "flex",
                        "flexDirection": "column",
                    },
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

    styles = [STYLE_INACTIVE, STYLE_INACTIVE, STYLE_INACTIVE, STYLE_INACTIVE]
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
    trig = ctx.triggered_id
    if trig == "btn-ind-trade":
        mode = "trade"
    else:
        mode = "quote"

    quote_class = "indicator-tab active" if mode == "quote" else "indicator-tab"
    trade_class = "indicator-tab active" if mode == "trade" else "indicator-tab"
    return mode, quote_class, trade_class


@app.callback(
    Output("store-pre-data", "data"),
    Output("store-qa-data", "data"),
    Output("store-panel-data", "data"),
    Output("store-global-data", "data"),
    Output("store-active-point", "data"),
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
)
def unified_data_and_active(
    tic,
    quarter,
    tone_click,
    ind_click,
    transcript_clicks,
    tab_pre,
    tab_qa,
    pre_data,
    qa_data,
    panel_data,
    global_data,
    active_point,
):
    triggered = ctx.triggered_id

    # ---------- (1) 公司或季度改變：重載資料 ----------
    if triggered in ["dropdown-company", "store-quarter"]:
        if tic is None:
            raise dash.exceptions.PreventUpdate

        year = YEAR_DEFAULT
        pre_df = load_pre_df(tic, year, quarter)
        qa_df = load_qa_df(tic, year, quarter)
        panel_df = load_panel_df(tic, year, quarter)
        global_df = build_global_df(pre_df, qa_df)

        if not pre_df.empty:
            sec_id = choose_default_changepoint(pre_df)
            mode = "pre"
        else:
            sec_id = choose_default_changepoint(qa_df)
            mode = "qa"

        active_point = {"mode": mode, "section_id": int(sec_id)}

        row = load_calendar_row(tic, year, quarter)
        label = ""
        if row is not None:
            start = row.get("timestamp_et_start", "")
            end = row.get("timestamp_et_end", "")
            if pd.notna(start) and pd.notna(end):
                try:
                    s = pd.to_datetime(start).strftime("%Y-%m-%d %H:%M")
                    e = pd.to_datetime(end).strftime("%Y-%m-%d %H:%M")
                    label = f"[{s}, {e}] ET"
                except Exception:
                    # 萬一 parse 失敗就退回原字串
                    label = f"[{start}, {end}] ET"

        # ----- (comment) 讀取 LLM_comment 的 markdown -----
        comment = ""
        cpath = DATA_DIR / "LLM_comment" / f"{tic}_{year}_comment_{quarter}.md"
        if cpath.exists():
            try:
                comment = cpath.read_text(encoding="utf-8")
            except Exception:
                comment = f"(Unable to read comment file: {cpath})"

        # --- Load LLM comment markdown ---
        md_comment = load_comment_md(tic, year, quarter)

        return (
            pre_df.to_dict("records"),
            qa_df.to_dict("records"),
            panel_df.to_dict("records"),
            global_df.to_dict("records"),
            active_point,
            label,
            md_comment,
        )


    # ---------- (2) 互動行為：更新 active_point ----------
    pre_df = _df_from_store(pre_data)
    qa_df = _df_from_store(qa_data)
    global_df = _df_from_store(global_data)

    if active_point is None:
        active_point = {"mode": "pre", "section_id": 0}

    mode = active_point.get("mode", "pre")
    section_id = int(active_point.get("section_id", 0))

    if triggered == "graph-tone" and tone_click:
        x = tone_click["points"][0]["x"]
        mode_, sec_id = find_nearest_point(global_df, x)
        active_point = {"mode": mode_, "section_id": sec_id}

    elif triggered == "graph-indicators" and ind_click:
        x = ind_click["points"][0]["x"]
        mode_, sec_id = find_nearest_point(global_df, x)
        active_point = {"mode": mode_, "section_id": sec_id}

    elif isinstance(triggered, dict) and triggered.get("type") == "transcript-item":
        # 真正的 transcript 點擊（使用 n_clicks_timestamp 作為 Input）
        sec_id = int(triggered["index"])
        active_point = {"mode": mode, "section_id": sec_id}

    elif triggered == "btn-tab-pre":
        mode = "pre"
        if not pre_df.empty:
            sec_id = choose_default_changepoint(pre_df)
        else:
            sec_id = 0
        active_point = {"mode": mode, "section_id": int(sec_id)}

    elif triggered == "btn-tab-qa":
        mode = "qa"
        if not qa_df.empty:
            sec_id = choose_default_changepoint(qa_df)
        else:
            sec_id = 0
        active_point = {"mode": mode, "section_id": int(sec_id)}

    return (
        pre_data,
        qa_data,
        panel_data,
        global_data,
        active_point,
        dash.no_update,
        dash.no_update,
    )


@app.callback(
    Output("store-scroll-state", "data"),
    Input("btn-more-top", "n_clicks"),
    Input("btn-less-top", "n_clicks"),
    Input("btn-more-bottom", "n_clicks"),
    Input("btn-less-bottom", "n_clicks"),
    State("store-scroll-state", "data"),
)
def toggle_scroll_state(nmt, nlt, nmb, nlb, scroll_state):
    if scroll_state is None:
        scroll_state = {"above_more": False, "below_more": False}

    trig = ctx.triggered_id
    if trig == "btn-more-top":
        scroll_state["above_more"] = True
    elif trig == "btn-less-top":
        scroll_state["above_more"] = False
    elif trig == "btn-more-bottom":
        scroll_state["below_more"] = True
    elif trig == "btn-less-bottom":
        scroll_state["below_more"] = False

    return scroll_state


@app.callback(
    Output("btn-more-top", "className"),
    Output("btn-less-top", "className"),
    Output("btn-more-bottom", "className"),
    Output("btn-less-bottom", "className"),
    Input("store-scroll-state", "data"),
)
def update_more_less_button_classes(scroll_state):
    base = "more-less-btn"
    if not scroll_state:
        scroll_state = {"above_more": False, "below_more": False}

    above_more = bool(scroll_state.get("above_more", False))
    below_more = bool(scroll_state.get("below_more", False))

    class_more_top = base + (" more-less-btn-active" if above_more else "")
    class_less_top = base + ("" if above_more else " more-less-btn-active")
    class_more_bottom = base + (" more-less-btn-active" if below_more else "")
    class_less_bottom = base + ("" if below_more else " more-less-btn-active")

    return class_more_top, class_less_top, class_more_bottom, class_less_bottom


@app.callback(
    Output("graph-tone", "figure"),
    Output("graph-indicators", "figure"),
    Output("transcript-inner", "children"),
    Output("btn-tab-pre", "className"),
    Output("btn-tab-qa", "className"),
    Input("store-active-point", "data"),
    Input("store-pre-data", "data"),
    Input("store-qa-data", "data"),
    Input("store-panel-data", "data"),
    Input("store-scroll-state", "data"),
    Input("store-indicator-mode", "data"),
)
def update_visuals(active_point, pre_data, qa_data, panel_data, scroll_state, indicator_mode):
    pre_df = _df_from_store(pre_data)
    qa_df = _df_from_store(qa_data)
    panel_df = _df_from_store(panel_data)

    if active_point is None:
        mode = "pre"
        section_id = 0
    else:
        mode = active_point.get("mode", "pre")
        section_id = int(active_point.get("section_id", 0))

    # 依目前 tab（Presentation / Q&A）選擇對應的 transcript
    current_df = pre_df if mode == "pre" else qa_df

    # ✅ x 軸範圍：統一用「目前 transcript 的 timestamp_sec」
    #    這樣 Cumulative Tone 和 Key Indicators 的 x 軸就一定對齊
    segment_range = None
    if not current_df.empty:
        seg_start = float(current_df["timestamp_sec"].min())
        seg_end = float(current_df["timestamp_sec"].max())
        if seg_end > seg_start:
            segment_range = (seg_start, seg_end)

    # ✅ 灰色線 / 黑線的位置，同樣用 timestamp_sec
    active_ts = None
    if not current_df.empty:
        r = current_df[current_df["section_id"] == section_id]
        if not r.empty:
            active_ts = float(r.iloc[0]["timestamp_sec"])

    tone_fig = build_tone_figure(pre_df, qa_df, mode, section_id, segment_range)
    indicator_fig = build_indicator_figure(panel_df, active_ts, indicator_mode, segment_range)
    transcript_children = build_transcript_children(current_df, section_id, scroll_state or {})

    pre_class = "transcript-tab active" if mode == "pre" else "transcript-tab"
    qa_class = "transcript-tab active" if mode == "qa" else "transcript-tab"

    return tone_fig, indicator_fig, transcript_children, pre_class, qa_class


# ============================================================
# 6. Client-side scroll centering
# ============================================================

app.clientside_callback(
    """
    function(active_point, scroll_state, children) {
        if (!children || !active_point) {
            return null;
        }

        setTimeout(function() {
            try {
                var container = document.getElementById('transcript-container');
                if (!container) return;

                var activeEls = container.getElementsByClassName('transcript-active');
                if (!activeEls.length) return;

                var activeEl = activeEls[0];

                var contRect = container.getBoundingClientRect();
                var actRect  = activeEl.getBoundingClientRect();

                var contCenter = (contRect.top + contRect.bottom) / 2;
                var actCenter  = (actRect.top + actRect.bottom) / 2;

                var delta = actCenter - contCenter;

                if (!isNaN(delta)) {
                    container.scrollTop += delta;
                }

            } catch (e) {
                console.log("scroll center error:", e);
            }
        }, 0);

        return null;
    }
    """,
    Output("store-scroll-dummy", "data"),
    Input("store-active-point", "data"),
    Input("store-scroll-state", "data"),
    Input("transcript-inner", "children"),
)

# ============================================================
# 7. Run
# ============================================================

if __name__ == "__main__":
    app.run(debug=True)
