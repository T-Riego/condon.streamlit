import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

import streamlit as st
import pandas as pd
from data.mock_data import (
    VALORES_ABRIL_2026, MORADORES, FUNDO_RESERVA_SALDO,
    HISTORICO, init_session_state,
)
from utils.formatters import brl, m3, status_badge, pagamento_badge

st.set_page_config(
    page_title="Neápolis — ADM",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
[data-testid="stSidebar"] { background-color: #1E3A5F; }
[data-testid="stSidebar"] * { color: #FFFFFF !important; }
[data-testid="stSidebar"] a { color: #7EC8E3 !important; }
.metric-card {
    background: white;
    border-radius: 10px;
    padding: 20px 24px;
    box-shadow: 0 1px 4px rgba(0,0,0,0.08);
    border-left: 4px solid #1E3A5F;
}
.metric-card.success { border-left-color: #27AE60; }
.metric-card.warning { border-left-color: #F39C12; }
.metric-card.info    { border-left-color: #2E86AB; }
.metric-label { font-size: 12px; color: #6B7280; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; }
.metric-value { font-size: 28px; font-weight: 700; color: #1A1A2E; margin-top: 4px; }
.metric-sub   { font-size: 12px; color: #9CA3AF; margin-top: 2px; }
.section-title { font-size: 18px; font-weight: 700; color: #1E3A5F; margin: 24px 0 12px 0; }
</style>
""", unsafe_allow_html=True)

# --- inicializa session state ---
init_session_state(st.session_state)

# --- sidebar ---
with st.sidebar:
    st.markdown("### 🏢 Neápolis")
    st.markdown("**Condomínio Residencial**  \nBelo Horizonte / MG")
    st.markdown("---")
    st.markdown("**CNPJ:** 09.408.714/0001-08")
    st.markdown("**Banco:** Inter — AG 0001")
    st.markdown("**CC:** 26620410-4")
    st.markdown("**PIX:** CNPJ")
    st.markdown("---")
    st.markdown("👤 **Robson** — Síndico")
    st.markdown("**Competência:** Abril/2026")

# --- cabeçalho ---
st.markdown("# 🏢 Condomínio Residencial Neápolis")
st.markdown("### Dashboard — Abril/2026")

status = st.session_state["competencia_status"]
st.markdown(
    f"**Status da competência:** {status_badge(status)}",
    unsafe_allow_html=True,
)

col_status = st.columns([1, 1, 1])
opcoes = ["aberta", "conferida", "fechada"]
idx = opcoes.index(status)
labels = {"aberta": "▶ Marcar como Conferida", "conferida": "▶ Marcar como Fechada", "fechada": "✅ Fechada"}
if status != "fechada":
    if col_status[0].button(labels[status], type="primary"):
        st.session_state["competencia_status"] = opcoes[idx + 1]
        st.rerun()

st.divider()

# --- métricas ---
pagamentos = st.session_state["pagamentos"]
pagos_count = sum(1 for p in pagamentos.values() if p["pago"])
pendentes_count = 14 - pagos_count
total_pago = sum(
    v["total"] for v in VALORES_ABRIL_2026
    if pagamentos[v["ap"]]["pago"]
)
total_pendente = sum(
    v["total"] for v in VALORES_ABRIL_2026
    if not pagamentos[v["ap"]]["pago"]
)
total_geral = sum(v["total"] for v in VALORES_ABRIL_2026)

c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Total a Arrecadar</div>
        <div class="metric-value">{brl(total_geral)}</div>
        <div class="metric-sub">14 unidades — Abril/2026</div>
    </div>""", unsafe_allow_html=True)
with c2:
    st.markdown(f"""
    <div class="metric-card success">
        <div class="metric-label">Recebido</div>
        <div class="metric-value">{brl(total_pago)}</div>
        <div class="metric-sub">{pagos_count} de 14 pagos</div>
    </div>""", unsafe_allow_html=True)
with c3:
    st.markdown(f"""
    <div class="metric-card warning">
        <div class="metric-label">Pendente</div>
        <div class="metric-value">{brl(total_pendente)}</div>
        <div class="metric-sub">{pendentes_count} unidades em aberto</div>
    </div>""", unsafe_allow_html=True)
with c4:
    st.markdown(f"""
    <div class="metric-card info">
        <div class="metric-label">Fundo de Reserva</div>
        <div class="metric-value">{brl(FUNDO_RESERVA_SALDO)}</div>
        <div class="metric-sub">Saldo acumulado</div>
    </div>""", unsafe_allow_html=True)

st.markdown("")

# --- tabela de apartamentos ---
st.markdown('<div class="section-title">📋 Resumo por Unidade — Abril/2026</div>', unsafe_allow_html=True)

rows = []
for v in VALORES_ABRIL_2026:
    ap = v["ap"]
    pg = pagamentos[ap]
    rows.append({
        "AP":           ap,
        "Morador":      MORADORES.get(ap, "—"),
        "Água m³":      f"{v['agua_m3']:.3f}".replace(".", ","),
        "Água/Esgoto":  brl(v["agua_r"]),
        "Gás m³":       f"{v['gas_m3']:.3f}".replace(".", ","),
        "Gás R$":       brl(v["gas_r"]),
        "Rateio":       brl(v["rateio"]),
        "Total":        brl(v["total"]),
        "Pagamento":    "✅ Pago" if pg["pago"] else "⏳ Pendente",
    })

df = pd.DataFrame(rows)


def highlight_pagamento(row):
    if row["Pagamento"] == "✅ Pago":
        return ["background-color: #F0FFF4"] * len(row)
    return ["background-color: #FFFBF0"] * len(row)


styled = df.style.apply(highlight_pagamento, axis=1)
st.dataframe(styled, use_container_width=True, hide_index=True)

# totais
total_agua = sum(v["agua_r"] for v in VALORES_ABRIL_2026)
total_gas = sum(v["gas_r"] for v in VALORES_ABRIL_2026)
c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Água/Esgoto", brl(total_agua))
c2.metric("Total Gás", brl(total_gas))
c3.metric("Rateio por Unidade", brl(462.74))
c4.metric("Total Geral", brl(total_geral))

# --- condominial ---
st.divider()
st.markdown('<div class="section-title">🏠 Consumo Condominial (Residual)</div>', unsafe_allow_html=True)
cc1, cc2 = st.columns([1, 3])
cc1.metric("Água COND", "18,457 m³")
cc2.info("O consumo condominial é o residual: total COPASA menos soma dos consumos individuais. Não é cobrado diretamente — já está incluído no rateio.")

# --- atalhos ---
st.divider()
st.markdown('<div class="section-title">⚡ Ações Rápidas</div>', unsafe_allow_html=True)
col_a, col_b, col_c, col_d = st.columns(4)
col_a.page_link("pages/1_Leituras.py",     label="💧 Registrar Leituras",    icon=None)
col_b.page_link("pages/2_COPASA.py",       label="💧 Conta COPASA",          icon=None)
col_c.page_link("pages/3_Despesas.py",     label="💰 Lançar Despesas",       icon=None)
col_d.page_link("pages/5_Pagamentos.py",   label="✅ Registrar Pagamentos",  icon=None)
