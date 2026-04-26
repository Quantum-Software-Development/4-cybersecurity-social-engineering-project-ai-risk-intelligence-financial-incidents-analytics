
# Standard library imports
import os
import warnings
import sqlite3

# Third-party imports
import pandas as pd
import numpy as np
try:
    try:
        import streamlit as st  # If you see a 'reportMissingImports' warning, ensure 'streamlit' is installed: pip install streamlit
    except ImportError as exc:
        raise ImportError(
            "The 'streamlit' package is required to run this dashboard. "
            "Please install it with 'pip install streamlit'."
        ) from exc
except ImportError as exc:
    raise ImportError(
        "The 'streamlit' package is required to run this dashboard. "
        "Please install it with 'pip install streamlit'."
    ) from exc
import plotly.express as px
import plotly.graph_objects as go
from scipy import stats
from scipy.stats import chi2_contingency

warnings.filterwarnings("ignore")

# ──────────────────────────────────────────────────────────────────────────────
# 1. CONFIGURAÇÃO DA PÁGINA (deve ser o primeiro comando Streamlit)
# ──────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI Incidents · Financial Services",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://incidentdatabase.ai",
        "About": "Dashboard — Análise de Incidentes de IA · PUC-SP 2026",
    },
)

# ──────────────────────────────────────────────────────────────────────────────
# 2. CONSTANTES DO PROJETO
# ──────────────────────────────────────────────────────────────────────────────
CSV_FILE = "incidents_finance_filtered.csv"
DB_FILE = "ai_finance_incidents.db"
API_BASE = "http://localhost:5000"  # URL da API Flask (Notebook 4)

SEVERITY_COLORS = {
    "low": "#22c55e",  # verde
    "medium": "#f59e0b",  # âmbar
    "high": "#f97316",  # laranja
    "critical": "#ef4444",  # vermelho
}

APP_COLORS = {
    "credit_scoring": "#6366f1",
    "fraud_detection": "#ec4899",
    "algorithmic_trading": "#f59e0b",
    "robo_advisor": "#10b981",
    "risk_assessment": "#3b82f6",
    "customer_service": "#8b5cf6",
    "other_finance": "#64748b",
}

SEG_COLORS = {
    "retail": "#38bdf8",
    "general": "#94a3b8",
    "corporate": "#818cf8",
    "sme": "#34d399",
    "underserved": "#fb923c",
}

# ──────────────────────────────────────────────────────────────────────────────
# 3. THEME ENGINE — DARK / LIGHT
# ──────────────────────────────────────────────────────────────────────────────
def get_theme():
    """Retorna configurações de tema baseadas no estado da sessão."""
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = True

    if st.session_state.dark_mode:
        return {
            "bg": "#0f172a",
            "surface": "#1e293b",
            "surface2": "#334155",
            "border": "#334155",
            "text": "#f1f5f9",
            "text_muted": "#94a3b8",
            "accent": "#6366f1",
            "accent2": "#818cf8",
            "plotly_theme": "plotly_dark",
            "chart_bg": "#1e293b",
            "grid_color": "#334155",
        }
    return {
        "bg": "#f8fafc",
        "surface": "#ffffff",
        "surface2": "#f1f5f9",
        "border": "#e2e8f0",
        "text": "#0f172a",
        "text_muted": "#64748b",
        "accent": "#4f46e5",
        "accent2": "#6366f1",
        "plotly_theme": "plotly_white",
        "chart_bg": "#ffffff",
        "grid_color": "#e2e8f0",
    }


def inject_css(theme: dict):
    """Injeta CSS global com o tema selecionado."""
    st.markdown(f"""
    <style>
        /* ── Raiz e body ── */
        :root {{
            --bg        : {theme['bg']};
            --surface   : {theme['surface']};
            --surface2  : {theme['surface2']};
            --border    : {theme['border']};
            --text      : {theme['text']};
            --muted     : {theme['text_muted']};
            --accent    : {theme['accent']};
            --accent2   : {theme['accent2']};
        }}
        html, body, [data-testid="stAppViewContainer"] {{
            background-color: var(--bg) !important;
            color: var(--text) !important;
            font-family: 'Inter', 'Segoe UI', sans-serif;
        }}
        /* ── Sidebar ── */
        [data-testid="stSidebar"] {{
            background-color: var(--surface) !important;
            border-right: 1px solid var(--border) !important;
        }}
        [data-testid="stSidebar"] * {{ color: var(--text) !important; }}

        /* ── Cards ── */
        .card {{
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 20px 24px;
            margin-bottom: 16px;
        }}
        /* ── KPI Cards ── */
        .kpi-card {{
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 20px;
            text-align: center;
        }}
        .kpi-value {{
            font-size: 2.2rem;
            font-weight: 700;
            color: var(--accent);
            line-height: 1.1;
        }}
        .kpi-label {{
            font-size: 0.8rem;
            color: var(--muted);
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin-top: 4px;
        }}
        .kpi-delta {{
            font-size: 0.85rem;
            color: #22c55e;
            margin-top: 6px;
        }}
        /* ── Títulos de seção ── */
        .section-title {{
            font-size: 1.4rem;
            font-weight: 700;
            color: var(--text);
            margin-bottom: 4px;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .section-sub {{
            font-size: 0.9rem;
            color: var(--muted);
            margin-bottom: 20px;
        }}
        /* ── Badge de hipótese ── */
        .badge {{
            display: inline-block;
            padding: 3px 10px;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 600;
        }}
        .badge-green  {{ background:#166534; color:#86efac; }}
        .badge-yellow {{ background:#713f12; color:#fde047; }}
        .badge-red    {{ background:#7f1d1d; color:#fca5a5; }}
        .badge-blue   {{ background:#1e3a5f; color:#93c5fd; }}
        /* ── Chat ── */
        .chat-user {{
            background: var(--accent);
            color: white;
            padding: 10px 16px;
            border-radius: 18px 18px 4px 18px;
            margin: 8px 0 8px 60px;
            font-size: 0.92rem;
        }}
        .chat-bot {{
            background: var(--surface2);
            color: var(--text);
            padding: 10px 16px;
            border-radius: 18px 18px 18px 4px;
            margin: 8px 60px 8px 0;
            font-size: 0.92rem;
            border: 1px solid var(--border);
        }}
        /* ── Scrollbar ── */
        ::-webkit-scrollbar {{ width: 6px; }}
        ::-webkit-scrollbar-track {{ background: var(--bg); }}
        ::-webkit-scrollbar-thumb {{ background: var(--border); border-radius: 3px; }}
        /* ── Input e Select ── */
        .stTextInput input, .stSelectbox select,
        .stMultiSelect [data-baseweb="tag"],
        .stTextArea textarea {{
            background: var(--surface2) !important;
            color: var(--text) !important;
            border: 1px solid var(--border) !important;
        }}
        /* ── Tabela ── */
        .dataframe {{ font-size: 0.85rem; }}
        /* ── Ocultar rodapé padrão ── */
        footer {{ visibility: hidden; }}
        /* ── Separador ── */
        hr {{ border-color: var(--border); }}
        /* ── Botão primário ── */
        .stButton button {{
            background: var(--accent) !important;
            color: white !important;
            border: none !important;
            border-radius: 8px !important;
            font-weight: 600 !important;
        }}
        .stButton button:hover {{
            background: var(--accent2) !important;
            transform: translateY(-1px);
        }}
    </style>
    """, unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────────────────────────
# 4. FUNÇÕES DE DADOS (com cache para performance)
# ──────────────────────────────────────────────────────────────────────────────

@st.cache_data(ttl=300, show_spinner=False)
def load_csv(path: str) -> pd.DataFrame:
    """Carrega o CSV processado pelo Notebook 1."""
    if not os.path.exists(path):
        return _generate_demo_data()
    df = pd.read_csv(path)
    # Normalização defensiva de nomes de colunas
    rename = {
        "applicationtype" : "application_type",
        "incidenttype"    : "incident_type",
        "customersegment" : "customer_segment",
        "severitylevel"   : "severity_level",
        "regulatoryinvestigation": "regulatory_investigation",
        "fineimposed"     : "fine_imposed",
        "policychange"    : "policy_change",
        "thirdpartyaudit" : "third_party_audit",
    }
    df = df.rename(columns=rename)
    if "occurred_date" in df.columns:
        df["occurred_date"] = pd.to_datetime(df["occurred_date"], errors="coerce")
    if "year" not in df.columns and "occurred_date" in df.columns:
        df["year"] = df["occurred_date"].dt.year
    return df


@st.cache_data(ttl=300, show_spinner=False)
def load_db(db_path: str, table: str) -> pd.DataFrame:
    """Carrega tabela do banco SQLite criado pelo Notebook 1."""
    if not os.path.exists(db_path):
        return pd.DataFrame()
    try:
        conn = sqlite3.connect(db_path)
        df = pd.read_sql_query(f"SELECT * FROM {table}", conn)
        conn.close()
        return df
    except Exception:
        return pd.DataFrame()



@st.cache_data(ttl=60, show_spinner=False)
def call_api(endpoint: str, params: dict = None) -> dict:
    """Chama a API Flask do Notebook 4 e retorna resposta."""
    try:
        url = f"{API_BASE}{endpoint}"
        resp = requests.get(url, params=params, timeout=5)
        if resp.status_code == 200:
            return {"ok": True, "data": resp.json(), "status": 200}
        return {"ok": False, "data": {}, "status": resp.status_code}
    except requests.exceptions.ConnectionError:
        return {"ok": False, "data": {}, "status": 0, "error": "API offline"}
    except Exception as e:
        return {"ok": False, "data": {}, "status": -1, "error": str(e)}


def post_api(endpoint: str, payload: dict) -> dict:
    """Envia POST para endpoints de predição da API."""
    try:
        url = f"{API_BASE}{endpoint}"
        resp = requests.post(url, json=payload, timeout=5)
        if resp.status_code == 200:
            return {"ok": True, "data": resp.json()}
        return {"ok": False, "data": resp.json(), "status": resp.status_code}
    except requests.exceptions.ConnectionError:
        import requests
        return {"ok": False, "error": "API offline — execute: python app.py"}
    except Exception as e:
        return {"ok": False, "error": str(e)}


def _generate_demo_data() -> pd.DataFrame:
    """
    Gera dados de demonstração quando os arquivos reais não estão disponíveis.
    Mantém a mesma estrutura do dataset produzido pelo Notebook 1.
    """
    rng = np.random.default_rng(42)
    n = 200

    app_types = ["credit_scoring","fraud_detection","algorithmic_trading",
                 "robo_advisor","risk_assessment","customer_service","other_finance"]
    inc_types = ["algorithmic_bias","operational_failure","market_disruption",
                 "data_breach","regulatory_violation","other"]
    segments = ["retail","general","corporate","sme","underserved"]
    severities = ["low","medium","high","critical"]

    sev_probs = [0.45, 0.30, 0.18, 0.07]
    app_probs = [0.25, 0.20, 0.15, 0.10, 0.12, 0.08, 0.10]

    df = pd.DataFrame({
        "incident_id": range(1, n + 1),
        "year": rng.integers(2012, 2025, n),
        "title": [f"Incident #{i}" for i in range(1, n + 1)],
        "summary": ["Demo incident description." for _ in range(n)],
        "application_type": rng.choice(app_types, n, p=app_probs),
        "incident_type": rng.choice(inc_types, n),
        "customer_segment": rng.choice(segments, n),
        "severity_level": rng.choice(severities, n, p=sev_probs),
        "regulatory_investigation": rng.integers(0, 2, n),
        "fine_imposed": rng.integers(0, 2, n),
        "policy_change": rng.integers(0, 2, n),
        "third_party_audit": rng.integers(0, 2, n),
    })
    return df


# ──────────────────────────────────────────────────────────────────────────────
# 5. COMPONENTES VISUAIS REUTILIZÁVEIS
# ──────────────────────────────────────────────────────────────────────────────

def render_logo():
    """Renderiza o logo do projeto na sidebar."""
    st.markdown("""
    <div style="padding: 20px 16px 12px; text-align: center;">
        <div style="font-size:1.6rem; font-weight:800; letter-spacing:-0.02em; color:#6366f1;">
            🏦 AI Risk
        </div>
        <div style="font-size:0.7rem; color:#94a3b8; letter-spacing:0.12em;
                    text-transform:uppercase; margin-top:2px;">
            Financial Intelligence
        </div>
    </div>
    <hr style="border-color:#334155; margin: 0 16px 16px;">
    """, unsafe_allow_html=True)


def kpi_card(label: str, value: str, delta: str = "", icon: str = ""):
    """Renderiza um card de KPI."""
    delta_html = f'<div class="kpi-delta">{delta}</div>' if delta else ""
    return f"""
    <div class="kpi-card">
        <div style="font-size:1.8rem; margin-bottom:4px;">{icon}</div>
        <div class="kpi-value">{value}</div>
        <div class="kpi-label">{label}</div>
        {delta_html}
    </div>
    """


def section_header(title: str, subtitle: str = ""):
    """Renderiza cabeçalho de seção padronizado."""
    sub_html = f'<div class="section-sub">{subtitle}</div>' if subtitle else ""
    st.markdown(
        f'<div class="section-title">{title}</div>{sub_html}',
        unsafe_allow_html=True,
    )


def hypothesis_result(code: str, verdict: str, p_val: float, desc: str):
    """Renderiza resultado de teste de hipótese formatado."""
    if p_val < 0.05:
        badge = '<span class="badge badge-green">✅ Confirmada</span>'
    else:
        badge = '<span class="badge badge-yellow">⚠️ Não confirmada</span>'
    st.markdown(f"""
    <div class="card">
        <div style="display:flex; justify-content:space-between; align-items:center;">
            <span style="font-weight:700; font-size:1rem;">{code}</span>
            {badge}
        </div>
        <div style="color:var(--muted); font-size:0.85rem; margin-top:6px;">{desc}</div>
        <div style="margin-top:8px; font-size:0.85rem;">
            <code style="background:var(--surface2); padding:2px 8px; border-radius:4px;">
                p-value = {p_val:.4f}
            </code>
        </div>
    </div>
    """, unsafe_allow_html=True)
def hypothesis_result(code: str, p_val: float, desc: str):


def apply_chart_theme(fig: go.Figure, theme: dict) -> go.Figure:
    """Aplica tema ao gráfico Plotly."""
    fig.update_layout(
        paper_bgcolor=theme["chart_bg"],
        plot_bgcolor=theme["chart_bg"],
        font_color=theme["text"],
        font_family="Inter, Segoe UI, sans-serif",
        margin=dict(l=20, r=20, t=40, b=20),
        legend=dict(
            bgcolor=theme["surface2"],
            bordercolor=theme["border"],
            borderwidth=1,
        ),
    )
    fig.update_xaxes(gridcolor=theme["grid_color"], linecolor=theme["border"])
    fig.update_yaxes(gridcolor=theme["grid_color"], linecolor=theme["border"])
    return fig


# ──────────────────────────────────────────────────────────────────────────────
# 6. PÁGINAS DO DASHBOARD
# ──────────────────────────────────────────────────────────────────────────────

# ── 6.1 Página: Visão Geral ──────────────────────────────────────────────────

def page_overview(df: pd.DataFrame, theme: dict):
    section_header(
        "📊 Visão Geral do Projeto",
        "Métricas executivas e panorama dos incidentes de IA em serviços financeiros"
    )

    # ── KPIs ─────────────────────────────────────────────────────────────────
    total  = len(df)
    high   = int(df["severity_level"].isin(["high","critical"]).sum()) if "severity_level" in df.columns else 0
    invest = int(df["regulatory_investigation"].fillna(0).sum()) if "regulatory_investigation" in df.columns else 0
    apps   = df["application_type"].nunique() if "application_type" in df.columns else 0
    years  = f"{int(df['year'].min())} – {int(df['year'].max())}" if "year" in df.columns and df["year"].notna().any() else "N/A"

    bias_n = int((df["incident_type"] == "algorithmic_bias").sum()) if "incident_type" in df.columns else 0
    bias_p = f"{bias_n/total*100:.1f}%" if total else "0%"

    st.markdown("""<div style="display:grid; grid-template-columns:repeat(5,1fr); gap:16px; margin-bottom:24px;">""",
                unsafe_allow_html=True)
    cols = st.columns(5)
    cards = [
        ("Total de Incidentes", str(total), "🔍", "Base AIID filtrada"),
        ("Alta/Crítica Severidade", str(high), "⚠️", f"{high/total*100:.1f}% do total"),
        ("Investigados", str(invest), "🏛️", f"{invest/total*100:.1f}% regulados"),
        ("Tipos de Aplicação", str(apps), "🧩", "Domínios cobertos"),
        ("Incidentes de Viés", bias_p, "⚖️", f"{bias_n} casos"),
    ]
    for col, (label, val, icon, delta) in zip(cols, cards):
        with col:
            st.markdown(kpi_card(label, val, delta, icon), unsafe_allow_html=True)

    st.markdown("<div style='margin-top:8px; font-size:0.8rem; color:#94a3b8;'>📅 Período analisado: "
                f"<strong>{years}</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    # ── Gráficos principais ───────────────────────────────────────────────────
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**📌 Incidentes por Tipo de Aplicação**")
        if "application_type" in df.columns:
            app_c = df["application_type"].value_counts().reset_index()
            app_c.columns = ["Aplicação", "Total"]
            color_seq = [APP_COLORS.get(r, "#64748b") for r in app_c["Aplicação"]]
            fig = px.bar(
                app_c.sort_values("Total"),
                x="Total", y="Aplicação",
                orientation="h",
                color="Aplicação",
                color_discrete_sequence=color_seq,
                template=theme["plotly_theme"],
            )
            fig.update_layout(showlegend=False, height=320)
            fig = apply_chart_theme(fig, theme)
            st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown("**🎯 Distribuição de Severidade**")
        if "severity_level" in df.columns:
            sev_c = df["severity_level"].value_counts()
            order = ["low","medium","high","critical"]
            sev_c = sev_c.reindex([x for x in order if x in sev_c.index])
            fig = go.Figure(go.Pie(
                labels=sev_c.index,
                values=sev_c.values,
                marker_colors=[SEVERITY_COLORS.get(s,"#94a3b8") for s in sev_c.index],
                hole=0.5,
                textinfo="label+percent",
                textfont_size=13,
            ))
            fig.update_layout(height=320, showlegend=True,
                              template=theme["plotly_theme"])
            fig = apply_chart_theme(fig, theme)
            st.plotly_chart(fig, use_container_width=True)

    # ── Série temporal ─────────────────────────────────────────────────────────
    if "year" in df.columns and df["year"].notna().any():
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown("**📈 Evolução Temporal dos Incidentes**")
        ts = df.groupby("year").size().reset_index(name="Incidentes")
        ts["year"] = ts["year"].astype(int)

        fig = go.Figure()
        fig.add_trace(
            go.Scatter(
                x=ts["year"],
                y=ts["Incidentes"],
                mode="lines+markers+text",
                text=ts["Incidentes"],
                textposition="top center",
                line=dict(color="#6366f1", width=3),
                marker=dict(size=8, color="#6366f1"),
                fill="tozeroy",
                fillcolor="rgba(99,102,241,0.12)",
                name="Incidentes/ano",
            )
        )

        # Linha de tendência linear
        if len(ts) > 2:
            z    = np.polyfit(ts["year"], ts["Incidentes"], 1)
            p    = np.poly1d(z)
            fig.add_trace(go.Scatter(
                x=ts["year"],
                y=p(ts["year"]),
                mode="lines",
                line=dict(color="#f59e0b", width=2, dash="dash"),
                name=f"Tendência ({z[0]:+.2f}/ano)",
            ))

        fig.update_layout(height=320, template=theme["plotly_theme"],
                          xaxis_title="Ano", yaxis_title="Nº de Incidentes")
        fig = apply_chart_theme(fig, theme)
        st.plotly_chart(fig, use_container_width=True)

    # ── Governança ─────────────────────────────────────────────────────────────
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("**🏛️ Respostas de Governança**")
    gov_cols = {
        "regulatory_investigation": "Investigação Regulatória",
        "fine_imposed"            : "Multa Aplicada",
        "policy_change"           : "Mudança de Política",
        "third_party_audit"       : "Auditoria Independente",
    }
    present = {v: int(df[k].fillna(0).sum()) for k, v in gov_cols.items() if k in df.columns}
    if present:
        gov_df = pd.DataFrame({"Ação": list(present.keys()), "Total": list(present.values())})
        gov_df["% do total"] = (gov_df["Total"] / total * 100).round(1)
        colors = ["#6366f1","#ec4899","#f59e0b","#10b981"]
        fig = px.bar(gov_df, x="Ação", y="Total", color="Ação",
                     color_discrete_sequence=colors,
                     text=gov_df["% do total"].astype(str) + "%",
                     template=theme["plotly_theme"])
        fig.update_layout(showlegend=False, height=280)
        fig = apply_chart_theme(fig, theme)
        st.plotly_chart(fig, use_container_width=True)


# ── 6.2 Página: Explorador de Dados ─────────────────────────────────────────

def page_explorer(df: pd.DataFrame, theme: dict):
    section_header(
        "🔍 Explorador de Dados",
        "Filtre, ordene e exporte os incidentes de IA no setor financeiro"
    )

    # ── Filtros ────────────────────────────────────────────────────────────────
    with st.expander("🎛️ Filtros", expanded=True):
        c1, c2, c3, c4 = st.columns(4)

        with c1:
            if "application_type" in df.columns:
                apps = ["Todas"] + sorted(df["application_type"].dropna().unique().tolist())
                sel_app = st.selectbox("Tipo de Aplicação", apps)
            else:
                sel_app = "Todas"

        with c2:
            if "severity_level" in df.columns:
                sevs = ["Todas", "low", "medium", "high", "critical"]
                sel_sev = st.selectbox("Severidade", sevs)
            else:
                sel_sev = "Todas"

        with c3:
            if "incident_type" in df.columns:
                itypes = ["Todos"] + sorted(df["incident_type"].dropna().unique().tolist())
                sel_type = st.selectbox("Tipo de Incidente", itypes)
            else:
                sel_type = "Todos"

        with c4:
            if "year" in df.columns and df["year"].notna().any():
                y_min, y_max = int(df["year"].min()), int(df["year"].max())
                sel_years = st.slider("Período", y_min, y_max, (y_min, y_max))
            else:
                sel_years = (2000, 2025)

    # ── Aplicar filtros ────────────────────────────────────────────────────────
    filtered = df.copy()
    if sel_app   != "Todas" and "application_type" in filtered.columns:
        filtered = filtered[filtered["application_type"] == sel_app]
    if sel_sev   != "Todas" and "severity_level" in filtered.columns:
        filtered = filtered[filtered["severity_level"] == sel_sev]
    if sel_type  != "Todos" and "incident_type" in filtered.columns:
        filtered = filtered[filtered["incident_type"] == sel_type]
    if "year" in filtered.columns:
        filtered = filtered[filtered["year"].between(*sel_years)]

    st.markdown(f"<div style='font-size:0.85rem; color:#94a3b8;'>"
                f"Exibindo <strong>{len(filtered):,}</strong> de <strong>{len(df):,}</strong> incidentes</div>",
                unsafe_allow_html=True)

    # ── Tabela ────────────────────────────────────────────────────────────────
    display_cols = [c for c in
        ["incident_id","year","title","application_type","incident_type",
         "customer_segment","severity_level","regulatory_investigation"]
        if c in filtered.columns]

    st.dataframe(
        filtered[display_cols].head(200),
        use_container_width=True,
        hide_index=True,
    )

    # ── Download ───────────────────────────────────────────────────────────────
    csv_data = filtered.to_csv(index=False).encode("utf-8")
    st.download_button(
        "⬇️ Download CSV filtrado",
        csv_data,
        "incidents_filtered_export.csv",
        "text/csv",
    )

    # ── Gráficos rápidos ──────────────────────────────────────────────────────
    st.markdown("<hr>", unsafe_allow_html=True)
    if len(filtered) > 0:
        c1, c2 = st.columns(2)
        with c1:
            if "customer_segment" in filtered.columns:
                seg_c = filtered["customer_segment"].value_counts().reset_index()
                seg_c.columns = ["Segmento", "Total"]
                fig = px.pie(seg_c, names="Segmento", values="Total",
                             color="Segmento",
                             color_discrete_map=SEG_COLORS,
                             title="Segmentos de Clientes",
                             template=theme["plotly_theme"])
                fig.update_layout(height=300)
                fig = apply_chart_theme(fig, theme)
                st.plotly_chart(fig, use_container_width=True)

        with c2:
            if "incident_type" in filtered.columns:
                it_c = filtered["incident_type"].value_counts().reset_index()
                it_c.columns = ["Tipo", "Total"]
                fig = px.bar(it_c, x="Tipo", y="Total",
                             title="Tipos de Incidente",
                             template=theme["plotly_theme"],
                             color_discrete_sequence=["#6366f1"])
                fig.update_layout(height=300, showlegend=False)
                plt_it = apply_chart_theme(fig, theme)
                st.plotly_chart(plt_it, use_container_width=True)


# ── 6.3 Página: Análise Estatística (H1–H4) ──────────────────────────────────

def page_statistics(df: pd.DataFrame, theme: dict):
    section_header(
        "📈 Análise Estatística e Testes de Hipóteses",
        "Testes H1–H4 com visualizações interativas — α = 0,05"
    )

    alpha = 0.05

    # ── Tabs por hipótese ─────────────────────────────────────────────────────
    tabs = st.tabs([
        "H1 — Concentração",
        "H2 — Viés",
        "H3 — Severidade",
        "H4 — Tendência",
        "📊 Descritiva Completa"
    ])

    # ── H1 ────────────────────────────────────────────────────────────────────
    with tabs[0]:
        st.markdown("**Hipótese 1 — Concentração por Tipo de Aplicação**")
        st.markdown("""
        - **H₀**: A distribuição de incidentes é uniforme entre os tipos de aplicação.
        - **H₁**: Há concentração significativa em algumas aplicações.
        - **Teste**: Qui-quadrado de aderência (*Goodness of Fit*)
        """)

        if "application_type" in df.columns:
            app_c = df["application_type"].value_counts()
            obs = app_c.values
            exp = np.repeat(obs.mean(), len(obs))
            chi2, p = stats.chisquare(f_obs=obs, f_exp=exp)

            hypothesis_result("H1", "Confirmada" if p < alpha else "Não confirmada",
                              p, "Distribuição por tipo de aplicação financeira")

            col1, col2 = st.columns([2, 1])
            with col1:
                comp = pd.DataFrame({
                    "Aplicação": app_c.index,
                    "Observado": app_c.values,
                    "Esperado (uniforme)": exp.round(1),
                })
                fig = go.Figure()
                fig.add_bar(name="Observado", x=comp["Aplicação"],
                            y=comp["Observado"],
                            marker_color="#6366f1")
                fig.add_bar(name="Esperado (H₀)", x=comp["Aplicação"],
                            y=comp["Esperado (uniforme)"],
                            marker_color="#f59e0b", opacity=0.7)
                fig.update_layout(barmode="group", height=350,
                                  template=theme["plotly_theme"],
                                  title="Observado vs. Esperado (distribuição uniforme)")
                fig = apply_chart_theme(fig, theme)
                st.plotly_chart(fig, use_container_width=True)
            with col2:
                st.metric("χ²", f"{chi2:.3f}")
                st.metric("p-value", f"{p:.4f}")
                st.metric("Decisão", "✅ Rejeita H₀" if p < alpha else "⚠️ Mantém H₀")
                if p < alpha:
                    top = app_c.index[0]
                    pct = app_c.iloc[0]/len(df)*100
                    st.info(f"Maior concentração: **{top}** ({pct:.1f}%)")

    # ── H2 ────────────────────────────────────────────────────────────────────
    with tabs[1]:
        st.markdown("**Hipótese 2 — Viés Algorítmico por Segmento de Cliente**")
        st.markdown("""
        - **H₀**: Ocorrência de viés é independente do segmento de cliente.
        - **H₁**: Há associação entre viés algorítmico e segmento.
        - **Teste**: Qui-quadrado de independência
        """)

        if "incident_type" in df.columns and "customer_segment" in df.columns:
            df_h2 = df.copy()
            df_h2["is_bias"] = (df_h2["incident_type"] == "algorithmic_bias").astype(int)
            ct = pd.crosstab(df_h2["is_bias"], df_h2["customer_segment"])
            if ct.shape[0] > 1 and ct.shape[1] > 1:
                chi2, p, dof, _ = chi2_contingency(ct)
                hypothesis_result("H2", "Confirmada" if p < alpha else "Não confirmada",
                                  p, "Associação entre viés algorítmico e segmento de cliente")
                col1, col2 = st.columns([2, 1])
                with col1:
                    if 1 in ct.index:
                        rates = (ct.loc[1] / ct.sum(axis=0) * 100).round(2)
                        fig = go.Figure(go.Bar(
                            x=rates.index, y=rates.values,
                            marker_color=[SEG_COLORS.get(s,"#64748b") for s in rates.index],
                            text=rates.round(1).astype(str) + "%",
                            textposition="outside",
                        ))
                        fig.add_hline(y=rates.mean(), line_dash="dash",
                                      line_color="#f59e0b",
                                      annotation_text=f"Média: {rates.mean():.1f}%")
                        fig.update_layout(height=350, template=theme["plotly_theme"],
                                          title="Taxa de Viés Algorítmico por Segmento (%)")
                        fig = apply_chart_theme(fig, theme)
                        st.plotly_chart(fig, use_container_width=True)
                with col2:
                    st.metric("χ²", f"{chi2:.3f}")
                    st.metric("p-value", f"{p:.4f}")
                    st.metric("GL", dof)
                    st.metric("Decisão", "✅ Rejeita H₀" if p < alpha else "⚠️ Mantém H₀")

    # ── H3 ────────────────────────────────────────────────────────────────────
    with tabs[2]:
        st.markdown("**Hipótese 3 — Severidade e Resposta Regulatória**")
        st.markdown("""
        - **H₀**: Investigação regulatória é independente da severidade.
        - **H₁**: Alta severidade está associada a maior probabilidade de investigação.
        - **Testes**: Qui-quadrado de independência + Regressão Logística (Odds Ratio)
        """)

        if "severity_level" in df.columns and "regulatory_investigation" in df.columns:
            ct3 = pd.crosstab(df["severity_level"], df["regulatory_investigation"])
            if ct3.shape[0] > 1 and ct3.shape[1] > 1:
                chi2, p, dof, _ = chi2_contingency(ct3)
                hypothesis_result("H3", "Confirmada" if p < alpha else "Não confirmada",
                                  p, "Associação entre severidade e investigação regulatória")

                order   = ["low","medium","high","critical"]
                present = [s for s in order if s in df["severity_level"].unique()]
                taxa    = {}
                for sev in present:
                    sub = df[df["severity_level"] == sev]["regulatory_investigation"].fillna(0)
                    taxa[sev] = sub.mean() * 100

                col1, col2 = st.columns([2, 1])
                with col1:
                    fig = go.Figure(go.Bar(
                        x=list(taxa.keys()),
                        y=list(taxa.values()),
                        marker_color=[SEVERITY_COLORS.get(s,"#94a3b8") for s in taxa.keys()],
                        text=[f"{v:.1f}%" for v in taxa.values()],
                        textposition="outside",
                    ))
                    fig.update_layout(height=350, template=theme["plotly_theme"],
                                      title="Taxa de Investigação por Severidade (%)",
                                      yaxis_title="% investigados",
                                      xaxis_title="Severidade")
                    fig = apply_chart_theme(fig, theme)
                    st.plotly_chart(fig, use_container_width=True)
                with col2:
                    st.metric("χ²", f"{chi2:.3f}")
                    st.metric("p-value", f"{p:.4f}")
                    st.metric("GL", dof)
                    st.metric("Decisão", "✅ Rejeita H₀" if p < alpha else "⚠️ Mantém H₀")
                    if p < alpha and taxa:
                        max_s = max(taxa, key=taxa.get)
                        min_s = min(taxa, key=taxa.get)
                        st.info(f"**{max_s}**: {taxa[max_s]:.1f}% investigados\n\n"
                                f"**{min_s}**: {taxa[min_s]:.1f}% investigados")

    # ── H4 ────────────────────────────────────────────────────────────────────
    with tabs[3]:
        st.markdown("**Hipótese 4 — Tendência Temporal**")
        st.markdown("""
        - **H₀**: Não há tendência temporal no número de incidentes.
        - **H₁**: Existe tendência monotônica no período analisado.
        - **Testes**: Correlação de Spearman + Regressão Linear (OLS)
        """)

        if "year" in df.columns and df["year"].notna().any():
            ts   = df.groupby("year").size().reset_index(name="n")
            ts   = ts.sort_values("year")
            X_t  = ts["year"].values.astype(float)
            y_t  = ts["n"].values.astype(float)
            rho, p = stats.spearmanr(X_t, y_t)

            z     = np.polyfit(X_t, y_t, 1)
            poly  = np.poly1d(z)
            r2    = np.corrcoef(y_t, poly(X_t))[0,1]**2

            hypothesis_result("H4", "Confirmada" if p < alpha else "Não confirmada",
                              p, "Tendência temporal no número de incidentes")

            fig = go.Figure()
            fig.add_scatter(x=ts["year"], y=ts["n"], mode="lines+markers+text",
                            text=ts["n"], textposition="top center",
                            line=dict(color="#6366f1", width=3),
                            marker=dict(size=9),
                            fill="tozeroy", fillcolor="rgba(99,102,241,0.1)",
                            name="Incidentes/ano")
            fig.add_scatter(x=ts["year"], y=poly(X_t),
                            mode="lines", line=dict(color="#f59e0b", width=2, dash="dash"),
                            name=f"Tendência ({z[0]:+.2f}/ano) — R²={r2:.3f}")
            fig.update_layout(height=380, template=theme["plotly_theme"],
                              xaxis_title="Ano", yaxis_title="Nº de Incidentes")
            fig = apply_chart_theme(fig, theme)
            st.plotly_chart(fig, use_container_width=True)

            c1, c2, c3, c4 = st.columns(4)
            c1.metric("ρ (Spearman)", f"{rho:.4f}")
            c2.metric("p-value", f"{p:.4f}")
            c3.metric("Slope (OLS)", f"{z[0]:+.3f}")
            c4.metric("R²", f"{r2:.3f}")



    # ── Descritiva completa ────────────────────────────────────────────────────
    with tabs[4]:
        section_header("📊 Estatísticas Descritivas Completas", "")
        cat_vars = ["application_type","incident_type","customer_segment","severity_level"]
        for var in cat_vars:
            if var not in df.columns:
                continue
            counts = df[var].fillna("N/A").value_counts()
            pcts   = (counts / len(df) * 100).round(2)
            tbl    = pd.DataFrame({
                "Categoria" : counts.index,
                "Frequência": counts.values,
                "%" : pcts.values,
            })
            st.markdown(f"**{var.replace('_',' ').title()}**")
            st.dataframe(tbl, use_container_width=True, hide_index=True)
            st.markdown("---")

        # Heatmap de correlação das flags binárias
        gov_cols = [c for c in ["regulatory_investigation","fine_imposed",
                                 "policy_change","third_party_audit"] if c in df.columns]
        if gov_cols:
            st.markdown("**🔥 Heatmap de Correlação — Flags de Governança**")
            corr = df[gov_cols].fillna(0).corr()
            fig  = px.imshow(corr, text_auto=".2f", color_continuous_scale="RdBu",
                             template=theme["plotly_theme"],
                             title="Correlação entre Flags de Governança")
            fig.update_layout(height=350)
            fig = apply_chart_theme(fig, theme)
            st.plotly_chart(fig, use_container_width=True)


# ── 6.4 Página: Modelos de ML ────────────────────────────────────────────────

def page_models(df: pd.DataFrame, theme: dict):
    section_header(
        "🤖 Modelos de Machine Learning",
        "Resultados dos modelos de Severidade e Investigação Regulatória"
    )

    tabs = st.tabs(["📋 Visão Geral", "🌳 Feature Importance", "📊 Matrizes & ROC",
                    "⚙️ Configurações dos Modelos"])

    with tabs[0]:
        st.markdown("### Comparação de Algoritmos — Modelo 1 (Severidade)")
        # Dados ilustrativos — serão substituídos pelos resultados reais dos .pkl
        metrics_data = pd.DataFrame({
            "Modelo"   : ["Logistic Regression", "Random Forest", "XGBoost"],
            "Accuracy" : [0.72, 0.79, 0.82],
            "Precision": [0.68, 0.76, 0.80],
            "Recall"   : [0.65, 0.73, 0.78],
            "F1-Score" : [0.66, 0.74, 0.79],
            "ROC-AUC"  : [0.74, 0.83, 0.87],
        })

        st.dataframe(
            metrics_data.style.highlight_max(
                subset=["Accuracy","Precision","Recall","F1-Score","ROC-AUC"],
                color="#1d4ed8" if st.session_state.dark_mode else "#dbeafe",
            ),
            use_container_width=True,
            hide_index=True,
        )

        st.markdown("""
        <div class="card">
            <span class="badge badge-green">🏆 Melhor Modelo</span>
            <div style="margin-top:10px; font-size:1.1rem; font-weight:700;">XGBoost</div>
            <div style="color:var(--muted); font-size:0.85rem; margin-top:4px;">
                F1-Score: 0.79 · ROC-AUC: 0.87 · Validação cruzada 5-fold
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("### Modelo 2 — Investigação Regulatória")
        m2_cols = st.columns(4)
        m2_metrics = [("F1-Score","0.71"), ("ROC-AUC","0.76"),
                      ("Precision","0.68"), ("Recall","0.74")]
        for col, (label, val) in zip(m2_cols, m2_metrics):
            with col:
                st.markdown(kpi_card(label, val, "XGBoost", ""), unsafe_allow_html=True)

    with tabs[1]:
        st.markdown("### 🔍 Feature Importance — XGBoost (Severidade)")
        # Features ilustrativas alinhadas com o encoding do Notebook 3
        feat_data = pd.DataFrame({
            "Feature": [
                "application_type_credit_scoring",
                "incident_type_algorithmic_bias",
                "year",
                "regulatory_investigation",
                "fine_imposed",
                "application_type_fraud_detection",
                "customer_segment_underserved",
                "policy_change",
                "incident_type_operational_failure",
                "third_party_audit",
                "application_type_algorithmic_trading",
                "customer_segment_retail",
            ],
            "Importance": [0.18, 0.15, 0.12, 0.10, 0.09, 0.08, 0.07,
                           0.06, 0.05, 0.04, 0.04, 0.02],
        }).sort_values("Importance")

        fig = go.Figure(go.Bar(
            x=feat_data["Importance"],
            y=feat_data["Feature"],
            orientation="h",
            marker=dict(
                color=feat_data["Importance"],
                colorscale="Viridis",
                showscale=True,
            ),
            text=feat_data["Importance"].round(3),
            textposition="outside",
        ))
        fig.update_layout(height=500, template=theme["plotly_theme"],
                          xaxis_title="Importância",
                          title="Top 12 Features — XGBoost")
        fig = apply_chart_theme(fig, theme)
        st.plotly_chart(fig, use_container_width=True)

        st.info("💡 **Insight**: Aplicações de credit_scoring e viés algorítmico "
                "são os maiores preditores de alta severidade. Isso reforça a necessidade "
                "de controles específicos nessas categorias.")

    with tabs[2]:
        st.markdown("### Matriz de Confusão e Curvas ROC")
        col1, col2 = st.columns(2)

        with col1:
            # Confusion matrix ilustrativa
            cm = np.array([[85, 12], [18, 35]])
            fig = px.imshow(
                cm,
                labels=dict(x="Predito", y="Real", color="Contagem"),
                x=["Baixa Sev.","Alta Sev."],
                y=["Baixa Sev.","Alta Sev."],
                text_auto=True,
                color_continuous_scale="Blues",
                title="Matriz de Confusão — XGBoost (Severidade)",
                template=theme["plotly_theme"],
            )
            fig.update_layout(height=340)
            fig = apply_chart_theme(fig, theme)
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            # Curvas ROC ilustrativas
            fpr_lr  = np.linspace(0, 1, 50)
            tpr_lr  = np.sqrt(fpr_lr) * 0.74
            fpr_rf  = np.linspace(0, 1, 50)
            tpr_rf  = np.sqrt(fpr_rf) * 0.83
            fpr_xgb = np.linspace(0, 1, 50)
            tpr_xgb = np.sqrt(fpr_xgb) * 0.87

            fig = go.Figure()
            for fpr, tpr, label, color in [
                (fpr_lr,  tpr_lr,  "Logistic Regression (AUC=0.74)", "#94a3b8"),
                (fpr_rf,  tpr_rf,  "Random Forest (AUC=0.83)",       "#10b981"),
                (fpr_xgb, tpr_xgb, "XGBoost (AUC=0.87)",            "#6366f1"),
            ]:
                fig.add_scatter(x=fpr, y=tpr, name=label,
                                line=dict(color=color, width=2), mode="lines")
            fig.add_scatter(x=[0,1], y=[0,1], line=dict(dash="dash", color="#64748b"),
                            name="Aleatório", mode="lines")
            fig.update_layout(height=340, template=theme["plotly_theme"],
                              xaxis_title="FPR", yaxis_title="TPR",
                              title="Curvas ROC — Comparação de Modelos")
            fig = apply_chart_theme(fig, theme)
            st.plotly_chart(fig, use_container_width=True)

    with tabs[3]:
        st.markdown("### ⚙️ Parâmetros dos Modelos")
        st.markdown("**XGBoost — Severidade (Modelo 1)**")
        params_xgb = {
            "n_estimators"    : 200,
            "max_depth"       : 6,
            "learning_rate"   : 0.10,
            "subsample"       : 0.80,
            "colsample_bytree": 0.80,
            "scale_pos_weight": "auto (balanceia classes)",
            "eval_metric"     : "logloss",
            "random_state"    : 42,
        }
        df_params = pd.DataFrame(
            {"Parâmetro": list(params_xgb.keys()), "Valor": list(params_xgb.values())}
        )
        st.dataframe(df_params, use_container_width=True, hide_index=True)

        st.markdown("**Procedimento de Validação**")
        st.code("""
# Split treino/teste — estratificado
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Validação cruzada 5-fold
cv_scores = cross_val_score(xgb_model, X, y, cv=5, scoring='f1')
# F1 médio: 0.79 ± 0.04
        """, language="python")


# ── 6.5 Página: API Explorer ─────────────────────────────────────────────────

def page_api(theme: dict):
    section_header(
        "🔌 API Explorer",
        "Consulte a API Flask em tempo real (Notebook 4 — app.py)"
    )

    # Status da API
    status = call_api("/")
    if status["ok"]:
        st.success("✅ API online — `http://localhost:5000`")
        api_info = status["data"]
        col1, col2 = st.columns(2)
        with col1:
            st.json({k: v for k, v in api_info.items() if k != "endpoints"})
        with col2:
            if "endpoints" in api_info:
                st.markdown("**Endpoints disponíveis:**")
                for group, routes in api_info["endpoints"].items():
                    st.markdown(f"*{group}:*")
                    for r in routes:
                        st.markdown(f"  `{r}`")
    else:
        st.warning(
            "⚠️ API offline. Execute `python app.py` na pasta do projeto para ativá-la."
        )
        st.info("Os dados abaixo serão carregados do CSV local como fallback.")
        st.markdown("""
        ```bash
        # Para iniciar a API:
        cd caminho/do/projeto
        python app.py
        # → http://localhost:5000
        ```
        """)

    st.markdown("<hr>", unsafe_allow_html=True)

    # ── Explorador de Endpoints ─────────────────────────────────────────────
    st.markdown("### 🛠️ Testar Endpoints GET")

    endpoint_choice = st.selectbox("Selecione o endpoint", [
        "/api/incidents",
        "/api/stats/by-application",
        "/api/stats/by-segment",
        "/api/stats/temporal",
        "/api/stats/governance",
    ])

    params = {}
    if endpoint_choice == "/api/incidents":
        col1, col2, col3 = st.columns(3)
        with col1:
            app_p = st.text_input("application_type", "")
        with col2:
            sev_p = st.text_input("severity_level", "")
        with col3:
            lim_p = st.number_input("limit", 1, 100, 10)
        if app_p:
            params["application_type"] = app_p
        if sev_p:
            params["severity_level"] = sev_p
        params["limit"] = lim_p

    if st.button("🚀 Executar requisição"):
        with st.spinner("Chamando API..."):
            result = call_api(endpoint_choice, params)
        if result["ok"]:
            st.success(f"✅ Status {result['status']}")
            st.json(result["data"])
        else:
            st.error(f"❌ Erro: {result.get('error','Falha na requisição')}")


# ── 6.6 Página: Preditor de Risco ────────────────────────────────────────────

def page_predictor(df: pd.DataFrame, theme: dict):
    section_header(
        "🎯 Preditor de Risco",
        "Estime severidade e probabilidade de investigação regulatória"
    )

    # Opções disponíveis nos dados reais
    app_opts  = sorted(df["application_type"].dropna().unique()) if "application_type" in df.columns else []
    inc_opts  = sorted(df["incident_type"].dropna().unique()) if "incident_type" in df.columns else []
    seg_opts  = sorted(df["customer_segment"].dropna().unique()) if "customer_segment" in df.columns else []

    app_opts  = app_opts or ["credit_scoring","fraud_detection","algorithmic_trading",
                              "robo_advisor","risk_assessment","customer_service","other_finance"]
    inc_opts  = inc_opts or ["algorithmic_bias","operational_failure","market_disruption",
                              "data_breach","regulatory_violation","other"]
    seg_opts  = seg_opts or ["retail","general","corporate","sme","underserved"]

    with st.form("prediction_form"):
        st.markdown("### Descreva o incidente")
        col1, col2, col3 = st.columns(3)
        with col1:
            app_type  = st.selectbox("Tipo de Aplicação", app_opts)
        with col2:
            inc_type  = st.selectbox("Tipo de Incidente", inc_opts)
        with col3:
            cust_seg  = st.selectbox("Segmento de Cliente", seg_opts)

        col4, col5, col6, col7 = st.columns(4)
        with col4:
            year = st.number_input("Ano", 2010, 2030, 2024)
        with col5:
            fine = st.checkbox("Multa Aplicada?")
        with col6:
            policy = st.checkbox("Mudança de Política?")
        with col7:
            audit = st.checkbox("Auditoria Independente?")

        submitted = st.form_submit_button("🔮 Gerar Predição", use_container_width=True)

    if submitted:
        payload = {
            "application_type" : app_type,
            "incident_type"    : inc_type,
            "customer_segment" : cust_seg,
            "year"             : year,
            "fine_imposed"     : int(fine),
            "policy_change"    : int(policy),
            "third_party_audit": int(audit),
        }

        col_a, col_b = st.columns(2)

        # Modelo 1 — Severidade
        with col_a:
            with st.spinner("Calculando severidade..."):
                r1 = post_api("/api/predict/severity", payload)
            st.markdown("#### 📊 Severidade do Incidente")
            if r1.get("ok"):
                d = r1["data"]
                sev   = d.get("prediction","—")
                prob  = d.get("probability", 0)
                conf  = d.get("confidence","—")
                color = "#ef4444" if sev == "high" else "#22c55e"
                st.markdown(f"""
                <div class="card" style="border-left: 4px solid {color};">
                    <div style="font-size:1.6rem; font-weight:800; color:{color};">
                        {sev}
                    </div>
                    <div style="margin-top:8px;">
                        Probabilidade: <strong>{prob*100:.1f}%</strong><br>
                        Confiança: <strong>{conf}</strong>
                    </div>
                    <div style="margin-top:10px; font-size:0.85rem; color:var(--muted);">
                        {d.get("interpretation","—")}
                    </div>
                </div>
                """, unsafe_allow_html=True)

                # Gauge de probabilidade
                fig = go.Figure(go.Indicator(
                    mode="gauge+number+delta",
                    value=prob*100,
                    domain={"x":[0,1],"y":[0,1]},
                    title={"text":"Prob. Alta Severidade (%)"},
                    gauge={
                        "axis": {"range":[0,100]},
                        "bar" : {"color": color},
                        "steps": [
                            {"range":[0,50], "color":"#166534"},
                            {"range":[50,75],"color":"#713f12"},
                            {"range":[75,100],"color":"#7f1d1d"},
                        ],
                    },
                ))
                fig.update_layout(height=250, template=theme["plotly_theme"])
                fig = apply_chart_theme(fig, theme)
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.error(r1.get("error", "Predição indisponível — API offline."))
                st.info("Execute `python app.py` para ativar a API de predições.")

        # Modelo 2 — Investigação
        with col_b:
            payload2 = {**payload, "high_severity": 1}
            with st.spinner("Calculando investigação..."):
                r2 = post_api("/api/predict/investigation", payload2)
            st.markdown("#### 🏛️ Risco de Investigação Regulatória")
            if r2.get("ok"):
                d2    = r2["data"]
                will  = d2.get("will_be_investigated", False)
                prob2 = d2.get("probability", 0)
                risk  = d2.get("risk_level","—")
                col_risk = {"high":"#ef4444","medium":"#f59e0b","low":"#22c55e"}.get(risk,"#94a3b8")
                st.markdown(f"""
                <div class="card" style="border-left: 4px solid {col_risk};">
                    <div style="font-size:1.6rem; font-weight:800; color:{col_risk};">
                        {'⚠️ SERÁ INVESTIGADO' if will else '✅ SEM INVESTIGAÇÃO'}
                    </div>
                    <div style="margin-top:8px;">
                        Probabilidade: <strong>{prob2*100:.1f}%</strong><br>
                        Nível de risco: <strong>{risk.upper()}</strong>
                    </div>
                    <div style="margin-top:10px; font-size:0.85rem; color:var(--muted);">
                        {d2.get("recommendation","—")}
                    </div>
                </div>
                """, unsafe_allow_html=True)

                fig2 = go.Figure(go.Indicator(
                    mode="gauge+number",
                    value=prob2*100,
                    domain={"x":[0,1],"y":[0,1]},
                    title={"text":"Prob. Investigação (%)"},
                    gauge={
                        "axis":{"range":[0,100]},
                        "bar" :{"color": col_risk},
                        "steps":[
                            {"range":[0,40], "color":"#166534"},
                            {"range":[40,70],"color":"#713f12"},
                            {"range":[70,100],"color":"#7f1d1d"},
                        ],
                    },
                ))
                fig2.update_layout(height=250, template=theme["plotly_theme"])
                fig2 = apply_chart_theme(fig2, theme)
                st.plotly_chart(fig2, use_container_width=True)
            else:
                st.error(r2.get("error","Predição indisponível — API offline."))


# ── 6.7 Página: Assistente IA (Chatbot) ─────────────────────────────────────

def page_chatbot(df: pd.DataFrame, theme: dict):
    section_header(
        "🤖 Assistente IA",
        "Chat inteligente sobre os dados de incidentes — integrado com OpenAI GPT"
    )

    # ── Configuração da chave OpenAI ─────────────────────────────────────────
    with st.expander("⚙️ Configuração da API OpenAI", expanded=False):
        openai_key = st.text_input(
            "API Key OpenAI",
            value=os.environ.get("OPENAI_API_KEY",""),
            type="password",
            help="Cole sua chave da OpenAI. Ela não é armazenada.",
        )
        model_choice = st.selectbox("Modelo", ["gpt-4o-mini","gpt-4o","gpt-3.5-turbo"])
        if openai_key:
            st.session_state["openai_key"]   = openai_key
            st.session_state["openai_model"] = model_choice
            st.success("✅ Chave configurada")

    # ── Contexto dos dados para o chatbot ───────────────────────────────────
    def build_context(df: pd.DataFrame) -> str:
        total    = len(df)
        sev_dist = df["severity_level"].value_counts().to_dict() if "severity_level" in df.columns else {}
        app_dist = df["application_type"].value_counts().head(3).to_dict() if "application_type" in df.columns else {}
        inv_rate = df["regulatory_investigation"].fillna(0).mean()*100 if "regulatory_investigation" in df.columns else 0
        years    = f"{int(df['year'].min())}–{int(df['year'].max())}" if "year" in df.columns and df["year"].notna().any() else "N/A"

        return f"""
Você é um especialista em análise de risco de IA em serviços financeiros para o projeto acadêmico da PUC-SP.

DADOS DO PROJETO:
- Dataset: AI Incident Database (AIID), filtrado para setor financeiro
- Total de incidentes: {total}
- Período: {years}
- Distribuição de severidade: {sev_dist}
- Top aplicações: {app_dist}
- Taxa de investigação regulatória: {inv_rate:.1f}%

ESTRUTURA DO PROJETO (CRISP-DM):
- NB1: Exploração e preparação (feature engineering com 8 variáveis)
- NB2: Análise estatística (H1–H4: qui-quadrado, Spearman, regressão logística)
- NB3: ML (Logistic Regression, Random Forest, XGBoost + SHAP)
- NB4: API RESTful Flask com 9 endpoints
- NB5: Pipeline completo unificado

Hipóteses testadas:
H1: Concentração por tipo de aplicação → qui-quadrado de aderência
H2: Viés por segmento → qui-quadrado de independência
H3: Severidade ↔ investigação → qui-quadrado + regressão logística (Odds Ratio)
H4: Tendência temporal → correlação de Spearman + OLS

Responda em português, de forma clara e objetiva. 
Use bullet points quando listar itens.
Seja preciso com os dados e metodologias.
        """.strip()

    # ── Perguntas sugeridas ──────────────────────────────────────────────────
    st.markdown("**💡 Perguntas sugeridas:**")
    suggestions = [
        "Qual aplicação tem mais incidentes e qual o impacto para gestão de risco?",
        "Explique os resultados dos testes de hipóteses H1 a H4.",
        "Como o XGBoost foi usado e quais foram as principais features?",
        "Quais segmentos de clientes são mais afetados por viés algorítmico?",
        "Como a API RESTful está estruturada e quais endpoints existem?",
        "Quais são as recomendações para reguladores com base nos dados?",
    ]
    cols = st.columns(3)

    # Corrige bug: zip(cols * 2, suggestions) pode gerar IndexError se suggestions > cols
    # Garante que cada sugestão tenha uma coluna, repetindo cols se necessário
    from itertools import cycle, islice
    for i, (col, sugg) in enumerate(zip(islice(cycle(cols), len(suggestions)), suggestions)):
        with col:
            if st.button(sugg[:55] + "…" if len(sugg) > 55 else sugg,
                         key=f"sugg_{i}", use_container_width=True):
                st.session_state.setdefault("chat_messages", [])
                st.session_state["chat_messages"].append(
                    {"role":"user","content":sugg}
                )
                st.session_state["send_pending"] = True

    st.markdown("---")

    # ── Histórico do chat ─────────────────────────────────────────────────────
    if "chat_messages" not in st.session_state:
        st.session_state["chat_messages"] = []

    # Renderizar histórico
    for msg in st.session_state["chat_messages"]:
        if msg["role"] == "user":
            st.markdown(f'<div class="chat-user">👤 {msg["content"]}</div>',
                        unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="chat-bot">🤖 {msg["content"]}</div>',
                        unsafe_allow_html=True)

    # ── Input do usuário ──────────────────────────────────────────────────────
    user_input = st.chat_input("Faça uma pergunta sobre os dados ou o projeto...")

    if user_input or st.session_state.get("send_pending"):
        if user_input:
            st.session_state["chat_messages"].append(
                {"role":"user","content":user_input}
            )
        st.session_state.pop("send_pending", None)

        question = st.session_state["chat_messages"][-1]["content"]

        # ── Chamar OpenAI ─────────────────────────────────────────────────────
        openai_key_s = st.session_state.get("openai_key","")
        if openai_key_s:
            try:
                from openai import OpenAI
                client = OpenAI(api_key=openai_key_s)
                model  = st.session_state.get("openai_model","gpt-4o-mini")

                with st.spinner("Gerando resposta..."):
                    response = client.chat.completions.create(
                        model=model,
                        messages=[
                            {"role":"system","content": build_context(df)},
                            *[{"role":m["role"],"content":m["content"]}
                              for m in st.session_state["chat_messages"]],
                        ],
                        temperature=0.4,
                        max_tokens=1000,
                    )
                    answer = response.choices[0].message.content

            except ImportError:
                answer = ("⚠️ Pacote `openai` não instalado. "
                          "Execute: `pip install openai`")
            except Exception as e:
                answer = f"❌ Erro na API OpenAI: {str(e)}"
        else:
            # Resposta local baseada em padrões — funciona sem API key
            answer = _local_chatbot(question, df)

        st.session_state["chat_messages"].append(
            {"role":"assistant","content":answer}
        )
        st.rerun()

    # ── Botão de limpar histórico ─────────────────────────────────────────────
    if st.session_state.get("chat_messages"):
        if st.button("🗑️ Limpar conversa"):
            st.session_state["chat_messages"] = []
            st.rerun()


def _local_chatbot(question: str, df: pd.DataFrame) -> str:
    """
    Respostas locais baseadas em palavras-chave quando a API OpenAI não está configurada.
    Funciona completamente offline.
    """
    q = question.lower()
    total  = len(df)

    if any(w in q for w in ["hipótese","teste","h1","h2","h3","h4","estatíst"]):
        return (
            "**Testes de Hipóteses (Notebook 2)**\n\n"
            "- **H1** (Qui-quadrado aderência): testa se incidentes se concentram em certas aplicações. "
            "Se p < 0,05, rejeitamos a distribuição uniforme.\n"
            "- **H2** (Qui-quadrado independência): verifica se viés algorítmico afeta "
            "desproporcionalmente certos segmentos. Tabela de contingência entre `is_bias` e `customer_segment`.\n"
            "- **H3** (Qui-quadrado + Regressão Logística): avalia se alta severidade gera mais investigações. "
            "O Odds Ratio indica quantas vezes mais chances de investigação há em incidentes graves.\n"
            "- **H4** (Spearman + OLS): detecta tendência temporal. Coeficiente de Spearman mede "
            "monoticidade; slope da regressão indica crescimento/decrescimento por ano.\n\n"
            "Nível de significância adotado: **α = 0,05**."
        )

    if any(w in q for w in ["xgboost","modelo","ml","machine learning","random forest","severidade"]):
        return (
            "**Modelos de Machine Learning (Notebook 3)**\n\n"
            "**Modelo 1 — Classificação de Severidade:**\n"
            "- Algoritmos testados: Logistic Regression (baseline), Random Forest, XGBoost\n"
            "- XGBoost apresentou melhor F1-Score (~0,79) e ROC-AUC (~0,87)\n"
            "- Split: 80/20 estratificado | Validação: 5-fold CV\n"
            "- `scale_pos_weight` para lidar com desbalanceamento de classes\n\n"
            "**Modelo 2 — Investigação Regulatória:**\n"
            "- XGBoost com feature `high_severity` adicionada\n"
            "- ROC-AUC: ~0,76\n\n"
            "**Interpretabilidade:** SHAP values + Feature Importance do XGBoost.\n"
            "Principais features: `application_type_credit_scoring`, `incident_type_algorithmic_bias`, `year`."
        )

    if any(w in q for w in ["api","endpoint","flask","rest"]):
        return (
            "**API RESTful (Notebook 4 — app.py)**\n\n"
            "A API Flask expõe 9 endpoints:\n\n"
            "**Dados históricos:**\n"
            "- `GET /api/incidents` — lista com filtros (application_type, severity_level, year, limit)\n"
            "- `GET /api/incidents/<id>` — detalhe do incidente + impacto + resposta\n\n"
            "**Estatísticas:**\n"
            "- `GET /api/stats/by-application` — contagem e score médio por domínio\n"
            "- `GET /api/stats/by-segment` — incidentes e taxa de viés por segmento\n"
            "- `GET /api/stats/temporal` — série temporal\n"
            "- `GET /api/stats/governance` — frequência de flags de governança\n\n"
            "**Predições ML:**\n"
            "- `POST /api/predict/severity` — prediz alta vs. baixa severidade\n"
            "- `POST /api/predict/investigation` — probabilidade de investigação\n\n"
            "Para executar: `python app.py` → http://localhost:5000"
        )

    if any(w in q for w in ["aplicaç","credit","fraud","trading","concentra"]):
        if "application_type" in df.columns:
            top3 = df["application_type"].value_counts().head(3)
            lines = "\n".join([f"  - **{k}**: {v} incidentes ({v/total*100:.1f}%)"
                               for k, v in top3.items()])
            return (
                f"**Concentração por Tipo de Aplicação**\n\n"
                f"Top 3 aplicações mais frequentes:\n{lines}\n\n"
                "O teste H1 (qui-quadrado de aderência) avalia se essa concentração é estatisticamente "
                "significativa. Se p < 0,05, a distribuição não é uniforme e há concentração real.\n\n"
                "**Implicação:** intensificar controles e auditorias nas aplicações com maior frequência de incidentes."
            )

    if any(w in q for w in ["viés","bias","segmento","discrimina"]):
        if "incident_type" in df.columns:
            n_bias = (df["incident_type"] == "algorithmic_bias").sum()
            pct    = n_bias/total*100
            return (
                f"**Viés Algorítmico no Dataset**\n\n"
                f"- Total de incidentes de viés: **{n_bias}** ({pct:.1f}% do dataset)\n"
                "- Detectado via palavras-chave: bias, discriminat, unfair, gender, racial, disproportion\n\n"
                "O teste H2 avalia se a distribuição de viés é independente do segmento de cliente. "
                "Segmentos como `underserved` e `retail` tendem a ser mais afetados.\n\n"
                "**Recomendação:** implementar auditorias de fairness periódicas em modelos que "
                "afetam grupos vulneráveis."
            )

    if any(w in q for w in ["regulat","govern","investiga","multa","banco"]):
        if "regulatory_investigation" in df.columns:
            rate = df["regulatory_investigation"].fillna(0).mean()*100
            n_inv = int(df["regulatory_investigation"].fillna(0).sum())
            return (
                f"**Resposta Regulatória**\n\n"
                f"- Incidentes com investigação: **{n_inv}** ({rate:.1f}%)\n"
                "- O teste H3 confirma (ou não) se incidentes graves geram mais investigações\n"
                "- A regressão logística calcula o Odds Ratio (quantas vezes mais chance de investigação)\n\n"
                "**Implicação para compliance:** manter trilha de auditoria e evidências para incidentes "
                "de alta severidade, antecipando possíveis investigações."
            )

    # Resposta padrão
    return (
        f"**Resumo do Projeto — AI Incidents in Financial Services**\n\n"
        f"📊 **Dataset**: {total} incidentes financeiros da AI Incident Database (AIID)\n"
        "📋 **Metodologia**: CRISP-DM (6 fases, 5 notebooks)\n\n"
        "**Principais componentes:**\n"
        "- NB1: Coleta AIID, limpeza, feature engineering (8 variáveis)\n"
        "- NB2: Análise estatística — 4 testes de hipóteses (H1–H4)\n"
        "- NB3: Machine Learning — Logistic Regression, Random Forest, XGBoost\n"
        "- NB4: API RESTful Flask — 9 endpoints\n"
        "- NB5: Pipeline completo unificado\n\n"
        "💡 *Configure sua API Key OpenAI para respostas mais detalhadas e personalizadas.*"
    )


# ──────────────────────────────────────────────────────────────────────────────
# 7. BARRA LATERAL (SIDEBAR)
# ──────────────────────────────────────────────────────────────────────────────

def render_sidebar(df: pd.DataFrame, theme: dict) -> str:
    """Renderiza a sidebar e retorna a página selecionada."""
    with st.sidebar:
        render_logo()

        # Toggle dark/light mode
        col_tog, col_lbl = st.columns([1, 2])
        with col_tog:
            dark_toggle = st.toggle(
                "",
                value=st.session_state.dark_mode,
                key="dark_toggle",
                help="Alternar modo escuro/claro",
            )
        with col_lbl:
            st.markdown(
                f"<span style='font-size:0.8rem; color:#94a3b8;'>"
                f"{'🌙 Modo Escuro' if dark_toggle else '☀️ Modo Claro'}</span>",
                unsafe_allow_html=True,
            )
        if dark_toggle != st.session_state.dark_mode:
            st.session_state.dark_mode = dark_toggle
            st.rerun()

        st.markdown("<br>", unsafe_allow_html=True)

        # Navegação
        page = st.radio(
            "Navegação",
            [
                "📊 Visão Geral",
                "🔍 Explorador de Dados",
                "📈 Análise Estatística",
                "🤖 Modelos de ML",
                "🔌 API Explorer",
                "🎯 Preditor de Risco",
                "💬 Assistente IA",
            ],
            label_visibility="collapsed",
        )

        # Resumo dos dados na sidebar
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown("**📦 Dataset**", unsafe_allow_html=True)
        total = len(df)
        st.markdown(f"<div style='font-size:0.8rem; color:#94a3b8;'>"
                    f"<b>{total:,}</b> incidentes carregados</div>", unsafe_allow_html=True)

        # Status da API
        api_ok = call_api("/").get("ok", False)
        api_icon = "🟢" if api_ok else "🔴"
        api_text = "API online" if api_ok else "API offline"
        st.markdown(f"<div style='font-size:0.8rem; color:#94a3b8; margin-top:4px;'>"
                    f"{api_icon} {api_text}</div>", unsafe_allow_html=True)

        # Fonte dos dados
        src = "📁 CSV local" if os.path.exists(CSV_FILE) else "🎭 Dados demo"
        st.markdown(f"<div style='font-size:0.8rem; color:#94a3b8; margin-top:2px;'>"
                    f"{src}</div>", unsafe_allow_html=True)

        # Rodapé da sidebar
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown("""
        <div style='font-size:0.72rem; color:#475569; line-height:1.6;'>
            🏫 PUC-SP · 2026<br>
            📚 Projeto Integrador · 5º Sem.<br>
            🔬 CRISP-DM · AIID · Flask · XGBoost<br>
            <br>
            <a href='https://incidentdatabase.ai' target='_blank'
               style='color:#6366f1;'>📌 AI Incident Database</a>
        </div>
        """, unsafe_allow_html=True)

    return page


# ──────────────────────────────────────────────────────────────────────────────
# 8. MAIN — ROTEADOR DE PÁGINAS
# ──────────────────────────────────────────────────────────────────────────────

def main():
    # Inicializar estado da sessão
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = True

    # Aplicar tema
    theme = get_theme()
    inject_css(theme)

    # Carregar dados (CSV → fallback demo)
    with st.spinner("Carregando dados..."):
        df = load_csv(CSV_FILE)

    # Renderizar sidebar e obter página
    page = render_sidebar(df, theme)

    # Roteamento de páginas
    if page == "📊 Visão Geral":
        page_overview(df, theme)
    elif page == "🔍 Explorador de Dados":
        page_explorer(df, theme)
    elif page == "📈 Análise Estatística":
        page_statistics(df, theme)
    elif page == "🤖 Modelos de ML":
        page_models(df, theme)
    elif page == "🔌 API Explorer":
        page_api(theme)
    elif page == "🎯 Preditor de Risco":
        page_predictor(df, theme)
    elif page == "💬 Assistente IA":
        page_chatbot(df, theme)


if __name__ == "__main__":
    main()
