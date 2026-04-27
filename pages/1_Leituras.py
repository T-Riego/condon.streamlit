import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from core.auth import require_auth
require_auth()

import streamlit as st
from data.mock_data import APARTAMENTOS, LEITURAS_ANTERIORES, CONSUMOS_ABRIL_2026, init_session_state

st.set_page_config(page_title="Leituras — Neápolis", page_icon="💧", layout="wide")

st.markdown("""
<style>
.ap-header {
    background: #1E3A5F; color: white;
    padding: 8px 16px; border-radius: 8px 8px 0 0;
    font-weight: 700; font-size: 15px;
}
.ap-card {
    background: white; border: 1px solid #E5E7EB;
    border-radius: 0 0 8px 8px; padding: 12px 16px;
    margin-bottom: 12px;
}
.consumo-ok  { color: #27AE60; font-weight: 600; }
.consumo-err { color: #E74C3C; font-weight: 600; }
</style>
""", unsafe_allow_html=True)

init_session_state(st.session_state)

st.markdown("# 💧 Leituras de Medidores")
st.markdown("**Competência:** Abril/2026 &nbsp;|&nbsp; Dias 27–29 do mês")

# --- progresso ---
leituras = st.session_state["leituras"]
total_medidores = 15 + 15  # 15 água + 15 gás (AP 201 tem 2 de gás = 16, mas contamos 15 pontos de gás)
# Na prática: 14 agua + 1 piscina(201) = 15 agua; 13 gas + 2 gas(201) = 15 gas
preenchidos = sum(
    1 for ap in APARTAMENTOS
    if ap in leituras and any(v is not None and v >= 0 for v in leituras[ap].values())
)
st.progress(preenchidos / 14, text=f"{preenchidos} de 14 apartamentos com leituras registradas")

st.divider()

# --- filtro ---
col_f1, col_f2 = st.columns([2, 1])
andar_filtro = col_f1.selectbox(
    "Filtrar por andar",
    ["Todos", "2º andar (201/202)", "3º andar (301/302)", "4º andar (401/402)",
     "5º andar (501/502)", "6º andar (601/602)", "7º andar (701/702)", "8º andar (801/802)"],
    label_visibility="collapsed",
)

andar_map = {
    "2º andar (201/202)": ["201", "202"],
    "3º andar (301/302)": ["301", "302"],
    "4º andar (401/402)": ["401", "402"],
    "5º andar (501/502)": ["501", "502"],
    "6º andar (601/602)": ["601", "602"],
    "7º andar (701/702)": ["701", "702"],
    "8º andar (801/802)": ["801", "802"],
}
aps_exibir = andar_map.get(andar_filtro, APARTAMENTOS)

# --- formulário de leituras ---
with st.form("form_leituras"):
    for ap in aps_exibir:
        ant = LEITURAS_ANTERIORES[ap]
        lei = leituras.get(ap, {})

        st.markdown(f'<div class="ap-header">AP {ap}</div>', unsafe_allow_html=True)

        if ap == "201":
            c1, c2, c3 = st.columns(3)
            with c1:
                st.markdown("**💧 Água**")
                ant_agua = ant["agua"]
                st.caption(f"Leitura anterior: {ant_agua:.3f}")
                agua_atual = st.number_input(
                    "Leitura atual água 201",
                    value=float(ant_agua + lei.get("agua", CONSUMOS_ABRIL_2026["201"]["agua"])),
                    step=0.001, format="%.3f",
                    label_visibility="collapsed",
                    key=f"agua_{ap}",
                )
                consumo_agua = round(agua_atual - ant_agua, 3)
                css = "consumo-ok" if consumo_agua >= 0 else "consumo-err"
                st.markdown(f'<span class="{css}">Consumo: {consumo_agua:.3f} m³</span>', unsafe_allow_html=True)

            with c2:
                st.markdown("**🔥 Gás — Apt**")
                ant_gas_apt = ant["gas_apt"]
                st.caption(f"Leitura anterior: {ant_gas_apt:.3f}")
                gas_apt_atual = st.number_input(
                    "Leitura gás apt 201",
                    value=float(ant_gas_apt + lei.get("gas_apt", 0.0)),
                    step=0.001, format="%.3f",
                    label_visibility="collapsed",
                    key=f"gas_apt_{ap}",
                )
                consumo_gas_apt = round(gas_apt_atual - ant_gas_apt, 3)
                css = "consumo-ok" if consumo_gas_apt >= 0 else "consumo-err"
                st.markdown(f'<span class="{css}">Consumo: {consumo_gas_apt:.3f} m³</span>', unsafe_allow_html=True)

            with c3:
                st.markdown("**🔥 Gás — Piscina**")
                ant_gas_pisc = ant["gas_piscina"]
                st.caption(f"Leitura anterior: {ant_gas_pisc:.3f}")
                gas_pisc_atual = st.number_input(
                    "Leitura gás piscina 201",
                    value=float(ant_gas_pisc + lei.get("gas_piscina", 0.0)),
                    step=0.001, format="%.3f",
                    label_visibility="collapsed",
                    key=f"gas_pisc_{ap}",
                )
                consumo_gas_pisc = round(gas_pisc_atual - ant_gas_pisc, 3)
                css = "consumo-ok" if consumo_gas_pisc >= 0 else "consumo-err"
                st.markdown(f'<span class="{css}">Consumo: {consumo_gas_pisc:.3f} m³</span>', unsafe_allow_html=True)

        else:
            c1, c2 = st.columns(2)
            with c1:
                st.markdown("**💧 Água**")
                ant_agua = ant["agua"]
                st.caption(f"Leitura anterior: {ant_agua:.3f}")
                agua_atual = st.number_input(
                    f"Água {ap}",
                    value=float(ant_agua + lei.get("agua", CONSUMOS_ABRIL_2026[ap]["agua"])),
                    step=0.001, format="%.3f",
                    label_visibility="collapsed",
                    key=f"agua_{ap}",
                )
                consumo_agua = round(agua_atual - ant_agua, 3)
                css = "consumo-ok" if consumo_agua >= 0 else "consumo-err"
                st.markdown(f'<span class="{css}">Consumo: {consumo_agua:.3f} m³</span>', unsafe_allow_html=True)

            with c2:
                st.markdown("**🔥 Gás**")
                ant_gas = ant["gas"]
                st.caption(f"Leitura anterior: {ant_gas:.3f}")
                gas_atual = st.number_input(
                    f"Gás {ap}",
                    value=float(ant_gas + lei.get("gas", CONSUMOS_ABRIL_2026[ap]["gas"])),
                    step=0.001, format="%.3f",
                    label_visibility="collapsed",
                    key=f"gas_{ap}",
                )
                consumo_gas = round(gas_atual - ant_gas, 3)
                css = "consumo-ok" if consumo_gas >= 0 else "consumo-err"
                st.markdown(f'<span class="{css}">Consumo: {consumo_gas:.3f} m³</span>', unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

    salvar = st.form_submit_button("💾 Salvar Todas as Leituras", type="primary", use_container_width=True)

if salvar:
    for ap in aps_exibir:
        ant = LEITURAS_ANTERIORES[ap]
        if ap == "201":
            agua_val   = st.session_state.get(f"agua_{ap}", 0)
            gas_apt    = st.session_state.get(f"gas_apt_{ap}", 0)
            gas_pisc   = st.session_state.get(f"gas_pisc_{ap}", 0)
            st.session_state["leituras"][ap] = {
                "agua":        round(agua_val  - ant["agua"],        3),
                "gas_apt":     round(gas_apt   - ant["gas_apt"],     3),
                "gas_piscina": round(gas_pisc  - ant["gas_piscina"], 3),
            }
        else:
            agua_val = st.session_state.get(f"agua_{ap}", 0)
            gas_val  = st.session_state.get(f"gas_{ap}", 0)
            st.session_state["leituras"][ap] = {
                "agua": round(agua_val - ant["agua"], 3),
                "gas":  round(gas_val  - ant["gas"],  3),
            }
    st.success("✅ Leituras salvas com sucesso!")
    st.session_state["checklist"]["Todas as leituras de água registradas (15 medidores)"] = True
    st.session_state["checklist"]["Todas as leituras de gás registradas (15 medidores)"]  = True
