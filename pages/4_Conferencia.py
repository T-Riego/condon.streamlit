import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import streamlit as st
from data.mock_data import init_session_state, CHECKLIST_ITENS, VALORES_ABRIL_2026
from core.arredondamentos import calc_rateio
from utils.formatters import brl, status_badge

st.set_page_config(page_title="Conferência — Neápolis", page_icon="✅", layout="wide")

init_session_state(st.session_state)

st.markdown("# ✅ Conferência Mensal")
st.markdown("**Competência:** Abril/2026")
st.divider()

col_check, col_validacao = st.columns([1, 1])

with col_check:
    st.markdown("### Checklist de Fechamento")

    checklist = st.session_state["checklist"]
    marcados = sum(1 for v in checklist.values() if v)
    total    = len(CHECKLIST_ITENS)

    cor_barra = "#27AE60" if marcados == total else ("#F39C12" if marcados >= total // 2 else "#E74C3C")
    st.markdown(
        f'<div style="height:8px;background:#E5E7EB;border-radius:4px;margin-bottom:16px">'
        f'<div style="height:100%;width:{int(marcados/total*100)}%;background:{cor_barra};border-radius:4px"></div></div>',
        unsafe_allow_html=True,
    )
    st.markdown(f"**{marcados} de {total} itens concluídos**")

    st.markdown("")
    for item in CHECKLIST_ITENS:
        novo_valor = st.checkbox(item, value=checklist.get(item, False), key=f"check_{item}")
        st.session_state["checklist"][item] = novo_valor

    st.markdown("")
    todos_ok = all(st.session_state["checklist"].values())

    if todos_ok:
        st.success("🎉 Todos os itens conferidos! Competência pronta para ser fechada.")
        if st.button("🔒 Fechar Competência", type="primary", use_container_width=True):
            st.session_state["competencia_status"] = "fechada"
            st.balloons()
            st.success("✅ Competência Abril/2026 fechada com sucesso!")
    else:
        st.button("🔒 Fechar Competência", disabled=True, use_container_width=True,
                  help=f"Complete todos os {total} itens para fechar a competência.")

with col_validacao:
    st.markdown("### Validações Automáticas")

    despesas = st.session_state["despesas"]
    total_desp = sum(d["valor"] for d in despesas)
    parcial, sindico, fundo, rateio_final = calc_rateio(total_desp)

    total_arrecadar = sum(v["total"] for v in VALORES_ABRIL_2026)
    rateio_esperado = 462.74
    rateio_calc     = float(rateio_final)

    validacoes = [
        {
            "label": "Rateio calculado = R$ 462,74",
            "ok":    abs(rateio_calc - rateio_esperado) < 0.01,
            "detalhe": f"Calculado: {brl(rateio_calc)}",
        },
        {
            "label": "14 leituras de água registradas",
            "ok":    all("agua" in st.session_state["leituras"].get(ap, {}) for ap in
                         ["201","202","301","302","401","402","501","502","601","602","701","702","801","802"]),
            "detalhe": "Verifica se todas as leituras estão no session state",
        },
        {
            "label": "COPASA lançada",
            "ok":    st.session_state["copasa"]["valor_total"] > 0,
            "detalhe": f"Total COPASA: {brl(st.session_state['copasa']['valor_total'])}",
        },
        {
            "label": "Despesas lançadas",
            "ok":    len(despesas) > 0,
            "detalhe": f"{len(despesas)} despesas, total {brl(total_desp)}",
        },
        {
            "label": "Total arrecadar calculado",
            "ok":    total_arrecadar > 0,
            "detalhe": f"Total: {brl(total_arrecadar)}",
        },
    ]

    for v in validacoes:
        icone = "✅" if v["ok"] else "❌"
        cor   = "#27AE60" if v["ok"] else "#E74C3C"
        st.markdown(
            f'<div style="background:white;border-left:4px solid {cor};padding:10px 14px;border-radius:0 8px 8px 0;margin-bottom:8px">'
            f'<strong>{icone} {v["label"]}</strong><br>'
            f'<small style="color:#6B7280">{v["detalhe"]}</small></div>',
            unsafe_allow_html=True,
        )

    st.markdown("---")
    st.markdown("### Resumo Financeiro")

    pagamentos = st.session_state["pagamentos"]
    pagos_val  = sum(v["total"] for v in VALORES_ABRIL_2026 if pagamentos[v["ap"]]["pago"])
    pend_val   = total_arrecadar - pagos_val

    st.metric("Total a arrecadar", brl(total_arrecadar))
    c1, c2 = st.columns(2)
    c1.metric("Recebido",  brl(pagos_val), delta=f"{sum(1 for p in pagamentos.values() if p['pago'])} APs")
    c2.metric("Pendente",  brl(pend_val),  delta=f"{sum(1 for p in pagamentos.values() if not p['pago'])} APs", delta_color="inverse")

    st.markdown("---")
    status = st.session_state["competencia_status"]
    st.markdown(f"**Status atual:** {status_badge(status)}", unsafe_allow_html=True)
