import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import streamlit as st
import pandas as pd
from data.mock_data import init_session_state, HISTORICO
from utils.formatters import brl, status_badge

st.set_page_config(page_title="Histórico — Neápolis", page_icon="📊", layout="wide")

init_session_state(st.session_state)

STATUS_CORES = {
    "aberta":    "#F39C12",
    "conferida": "#2E86AB",
    "fechada":   "#27AE60",
}

st.markdown("# 📊 Histórico de Competências")
st.divider()

# --- gráfico de barras ---
st.markdown("### Evolução Mensal (Total Arrecadado)")
df_chart = pd.DataFrame({
    "Mês":   [h["display"] for h in reversed(HISTORICO)],
    "Total": [h["total"]   for h in reversed(HISTORICO)],
})
df_chart = df_chart.set_index("Mês")
st.bar_chart(df_chart, height=280)

st.divider()

# --- filtro de ano ---
anos_disponiveis = sorted({h["ano_mes"][:4] for h in HISTORICO}, reverse=True)
ano_sel = st.selectbox("Filtrar por ano", ["Todos"] + anos_disponiveis, label_visibility="collapsed")

historico_filtrado = [
    h for h in HISTORICO
    if ano_sel == "Todos" or h["ano_mes"].startswith(ano_sel)
]

# --- listagem ---
st.markdown(f"### Competências ({len(historico_filtrado)} registros)")

for h in historico_filtrado:
    cor = STATUS_CORES.get(h["status"], "#999")
    with st.container():
        c1, c2, c3, c4, c5 = st.columns([2, 2, 2, 2, 1])

        c1.markdown(
            f'<div style="background:{cor};color:white;border-radius:8px;padding:10px 14px;font-size:18px;font-weight:700">'
            f'{h["display"]}</div>',
            unsafe_allow_html=True,
        )
        c2.metric("Total Arrecadado", brl(h["total"]))
        c3.metric("Pagos",    f'{h["pagos"]}/14')
        c4.metric("Pendentes", str(h["pendentes"]))
        c5.markdown(
            f'<div style="margin-top:12px">{status_badge(h["status"])}</div>',
            unsafe_allow_html=True,
        )
        st.divider()

# --- tabela resumo ---
st.markdown("### Tabela Resumo")
df_tabela = pd.DataFrame([
    {
        "Competência": h["display"],
        "Status":      h["status"].capitalize(),
        "Total R$":    brl(h["total"]),
        "Pagos":       f'{h["pagos"]}/14',
        "Pendentes":   h["pendentes"],
    }
    for h in historico_filtrado
])
st.dataframe(df_tabela, use_container_width=True, hide_index=True)

# --- estatísticas ---
st.divider()
st.markdown("### Estatísticas do Período")

totais = [h["total"] for h in historico_filtrado]
if totais:
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Média mensal",  brl(sum(totais) / len(totais)))
    c2.metric("Maior mês",     brl(max(totais)))
    c3.metric("Menor mês",     brl(min(totais)))
    c4.metric("Total período", brl(sum(totais)))
