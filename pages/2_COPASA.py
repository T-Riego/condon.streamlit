import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import streamlit as st
from data.mock_data import init_session_state
from utils.formatters import brl

st.set_page_config(page_title="COPASA — Neápolis", page_icon="🚰", layout="wide")

init_session_state(st.session_state)

HISTORICO_COPASA = [
    {"mes": "Mar/2026", "consumo": 221.500, "agua": 1880.00, "esgoto": 598.00, "recurso": 181.20, "total": 2659.20, "custo_m3": 12.01},
    {"mes": "Fev/2026", "consumo": 208.200, "agua": 1760.00, "esgoto": 562.00, "recurso": 170.80, "total": 2492.80, "custo_m3": 11.97},
    {"mes": "Jan/2026", "consumo": 234.100, "agua": 1982.00, "esgoto": 632.00, "recurso": 191.50, "total": 2805.50, "custo_m3": 11.98},
]

st.markdown("# 🚰 Conta COPASA")
st.markdown("**Competência:** Abril/2026")

st.divider()

col_form, col_info = st.columns([2, 1])

with col_form:
    st.markdown("### Lançamento da Conta")

    copasa = st.session_state["copasa"]

    with st.form("form_copasa"):
        consumo = st.number_input(
            "Consumo total m³",
            value=float(copasa["consumo_total_m3"]),
            step=0.001, format="%.3f",
            help="Consumo total medido pela COPASA (soma individual + condominial)",
        )
        c1, c2 = st.columns(2)
        valor_agua    = c1.number_input("Valor água R$",            value=float(copasa["valor_agua"]),    step=0.01, format="%.2f")
        valor_esgoto  = c2.number_input("Valor esgoto R$",          value=float(copasa["valor_esgoto"]),  step=0.01, format="%.2f")
        valor_recurso = c1.number_input("Valor recurso hídrico R$", value=float(copasa["valor_recurso"]), step=0.01, format="%.2f")
        valor_total   = c2.number_input(
            "Valor total R$ (conferência)",
            value=float(copasa["valor_total"]),
            step=0.01, format="%.2f",
            help="Deve corresponder a água + esgoto + recurso",
        )
        data_venc = st.date_input("Data de vencimento", value=None)

        st.markdown("")
        salvar = st.form_submit_button("💾 Salvar Conta COPASA", type="primary", use_container_width=True)

    if salvar:
        custo_m3 = round(valor_total / consumo, 4) if consumo > 0 else 0
        calculado = round(valor_agua + valor_esgoto + valor_recurso, 2)
        if abs(calculado - valor_total) > 0.02:
            st.warning(f"⚠️ Água + Esgoto + Recurso = {brl(calculado)}, mas total informado é {brl(valor_total)}. Verifique.")
        else:
            st.session_state["copasa"] = {
                "consumo_total_m3": consumo,
                "valor_agua":       valor_agua,
                "valor_esgoto":     valor_esgoto,
                "valor_recurso":    valor_recurso,
                "valor_total":      valor_total,
                "custo_por_m3":     custo_m3,
                "data_vencimento":  str(data_venc) if data_venc else copasa["data_vencimento"],
            }
            st.success("✅ Conta COPASA salva!")
            st.session_state["checklist"]["Conta COPASA lançada"] = True

with col_info:
    st.markdown("### Custo por m³ (calculado)")
    cop = st.session_state["copasa"]
    consumo_atual = cop["consumo_total_m3"]
    total_atual   = cop["valor_total"]
    custo_m3_calc = total_atual / consumo_atual if consumo_atual > 0 else 0

    st.metric("Custo/m³", f"R$ {custo_m3_calc:.4f}".replace(".", ","))
    st.metric("Consumo total", f"{consumo_atual:.3f} m³".replace(".", ","))
    st.metric("Valor total", brl(total_atual))

    st.markdown("---")
    st.markdown("**Conferência**")
    soma = cop["valor_agua"] + cop["valor_esgoto"] + cop["valor_recurso"]
    diff = abs(soma - cop["valor_total"])
    if diff < 0.02:
        st.success(f"✅ Totais conferem ({brl(soma)})")
    else:
        st.error(f"❌ Diferença de {brl(diff)}")

    st.markdown("---")
    st.markdown("**Vencimento**")
    st.info(f"📅 {cop['data_vencimento']}")

st.divider()
st.markdown("### 📊 Histórico COPASA (últimos 3 meses)")

import pandas as pd
df_hist = pd.DataFrame(HISTORICO_COPASA)
df_hist.columns = ["Mês", "Consumo m³", "Água R$", "Esgoto R$", "Recurso R$", "Total R$", "Custo/m³"]
st.dataframe(df_hist, use_container_width=True, hide_index=True)

st.markdown("---")
st.markdown("#### Evolução do Consumo")
consumos = {h["mes"]: h["consumo"] for h in HISTORICO_COPASA}
consumos["Abr/2026"] = st.session_state["copasa"]["consumo_total_m3"]
df_chart = pd.DataFrame({"Mês": list(consumos.keys()), "Consumo (m³)": list(consumos.values())})
df_chart = df_chart.set_index("Mês")
st.bar_chart(df_chart)
