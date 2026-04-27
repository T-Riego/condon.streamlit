import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import streamlit as st
import pandas as pd
from data.mock_data import init_session_state
from core.arredondamentos import calc_rateio
from utils.formatters import brl

st.set_page_config(page_title="Despesas — Neápolis", page_icon="💰", layout="wide")

init_session_state(st.session_state)

TIPOS = {
    "NF":            "Nota Fiscal",
    "retencao":      "Retenção",
    "seguro":        "Seguro",
    "sindico":       "Pró-labore Síndico",
    "fundo_reserva": "Fundo de Reserva",
    "outros":        "Outros",
}

st.markdown("# 💰 Despesas do Mês")
st.markdown("**Competência:** Abril/2026")

st.divider()

col_lista, col_rateio = st.columns([3, 1])

with col_lista:
    despesas = st.session_state["despesas"]
    total_desp = sum(d["valor"] for d in despesas)

    st.markdown(f"### Lançamentos ({len(despesas)} itens) — Total: **{brl(total_desp)}**")

    # exibe cada despesa com botão de remover
    for i, d in enumerate(despesas):
        c1, c2, c3, c4 = st.columns([4, 2, 1, 1])
        c1.markdown(f"**{d['descricao']}**  \n<small style='color:#6B7280'>{TIPOS.get(d['tipo'], d['tipo'])} — base {d['base']} unidades</small>", unsafe_allow_html=True)
        c2.markdown(f"**{brl(d['valor'])}**")
        c3.markdown("✅ Rateável" if d["rateavel"] else "—")
        if c4.button("🗑", key=f"del_{d['id']}", help="Remover despesa"):
            st.session_state["despesas"] = [x for x in despesas if x["id"] != d["id"]]
            st.rerun()
        st.divider()

    # formulário para nova despesa
    with st.expander("➕ Adicionar nova despesa", expanded=False):
        with st.form("form_nova_despesa", clear_on_submit=True):
            descricao = st.text_input("Descrição", placeholder="Ex: Manutenção portão")
            c1, c2 = st.columns(2)
            valor     = c1.number_input("Valor R$", min_value=0.01, step=0.01, format="%.2f")
            tipo      = c2.selectbox("Tipo", list(TIPOS.keys()), format_func=lambda k: TIPOS[k])
            c3, c4 = st.columns(2)
            rateavel  = c3.checkbox("Rateável entre unidades", value=True)
            base      = c4.selectbox("Base de rateio", [14, 13])
            adicionar = st.form_submit_button("Adicionar", type="primary")

        if adicionar and descricao:
            novo_id = st.session_state["despesa_next_id"]
            st.session_state["despesas"].append({
                "id":        novo_id,
                "descricao": descricao,
                "valor":     valor,
                "tipo":      tipo,
                "rateavel":  rateavel,
                "base":      base,
            })
            st.session_state["despesa_next_id"] = novo_id + 1
            st.session_state["checklist"]["Despesas do mês lançadas"] = True
            st.success(f"✅ Despesa '{descricao}' adicionada!")
            st.rerun()

with col_rateio:
    st.markdown("### 📊 Cálculo do Rateio")

    despesas = st.session_state["despesas"]
    total_rateavel = sum(d["valor"] for d in despesas if d["rateavel"])
    total_desp     = sum(d["valor"] for d in despesas)

    parcial, sindico, fundo, final = calc_rateio(total_desp)

    st.markdown(f"""
    <div style="background:white;border-radius:10px;padding:16px;border:1px solid #E5E7EB;">
        <div style="margin-bottom:8px;">
            <div style="font-size:11px;color:#6B7280;text-transform:uppercase;font-weight:600">Total Despesas</div>
            <div style="font-size:22px;font-weight:700;color:#1E3A5F">{brl(total_desp)}</div>
        </div>
        <hr style="margin:8px 0;border-color:#F3F4F6">
        <div style="font-size:13px;margin-bottom:6px">
            <span style="color:#6B7280">Parcial ÷14 =</span>
            <strong>{brl(float(parcial))}</strong>
        </div>
        <div style="font-size:13px;margin-bottom:6px">
            <span style="color:#6B7280">Síndico ÷13 =</span>
            <strong>{brl(float(sindico))}</strong>
        </div>
        <div style="font-size:13px;margin-bottom:6px">
            <span style="color:#6B7280">Fundo Reserva =</span>
            <strong>R$ 150,00</strong>
        </div>
        <hr style="margin:8px 0;border-color:#F3F4F6">
        <div style="background:#1E3A5F;color:white;border-radius:8px;padding:12px;text-align:center;">
            <div style="font-size:11px;opacity:0.8;text-transform:uppercase">RATEIO FINAL / UNIDADE</div>
            <div style="font-size:28px;font-weight:700">{brl(float(final))}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("")
    st.caption("Rateio = Parcial + Síndico + Fundo de Reserva")
    st.caption("Síndico não paga para si — o valor é dividido entre 13 unidades.")

    if abs(float(final) - 462.74) < 0.01:
        st.success("✅ Bate com Abril/2026 (R$ 462,74)")

    st.markdown("---")
    st.markdown("**Detalhamento**")
    df_det = pd.DataFrame([
        {"Tipo": TIPOS.get(d["tipo"], d["tipo"]), "Valor": brl(d["valor"])}
        for d in despesas
    ])
    st.dataframe(df_det, use_container_width=True, hide_index=True)
