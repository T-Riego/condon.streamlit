import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import streamlit as st
from data.mock_data import init_session_state, VALORES_ABRIL_2026, MORADORES
from utils.formatters import brl

st.set_page_config(page_title="Pagamentos — Neápolis", page_icon="💳", layout="wide")

init_session_state(st.session_state)

FORMAS = {"pix": "PIX", "boleto": "Boleto", "dinheiro": "Dinheiro", "transferencia": "Transferência"}

valor_por_ap = {v["ap"]: v["total"] for v in VALORES_ABRIL_2026}

st.markdown("# 💳 Controle de Pagamentos")
st.markdown("**Competência:** Abril/2026")
st.divider()

pagamentos = st.session_state["pagamentos"]
pagos_count    = sum(1 for p in pagamentos.values() if p["pago"])
pendentes_count = 14 - pagos_count
total_pago     = sum(valor_por_ap[ap] for ap, p in pagamentos.items() if p["pago"])
total_pendente = sum(valor_por_ap[ap] for ap, p in pagamentos.items() if not p["pago"])

# --- métricas ---
c1, c2, c3, c4 = st.columns(4)
c1.metric("Pagos",    f"{pagos_count}/14",     brl(total_pago))
c2.metric("Pendentes", f"{pendentes_count}/14", brl(total_pendente), delta_color="inverse")
c3.metric("Total recebido",  brl(total_pago))
c4.metric("Total pendente",  brl(total_pendente))

# barra de progresso
pct = int(pagos_count / 14 * 100)
st.markdown(
    f'<div style="margin:12px 0 4px;font-size:13px;color:#6B7280">{pagos_count} de 14 unidades pagas ({pct}%)</div>'
    f'<div style="height:10px;background:#E5E7EB;border-radius:5px">'
    f'<div style="height:100%;width:{pct}%;background:#27AE60;border-radius:5px"></div></div>',
    unsafe_allow_html=True,
)

st.divider()

aba_pend, aba_pagos = st.tabs([f"⏳ Pendentes ({pendentes_count})", f"✅ Pagos ({pagos_count})"])

# ---- ABA PENDENTES ----
with aba_pend:
    aps_pendentes = [ap for ap, p in pagamentos.items() if not p["pago"]]
    if not aps_pendentes:
        st.success("🎉 Todas as unidades estão pagas!")
    else:
        for ap in aps_pendentes:
            valor = valor_por_ap[ap]
            morador = MORADORES.get(ap, "—")

            with st.container():
                c1, c2, c3 = st.columns([1, 2, 2])
                c1.markdown(
                    f'<div style="background:#1E3A5F;color:white;border-radius:8px;padding:12px;text-align:center;font-size:20px;font-weight:700">AP {ap}</div>',
                    unsafe_allow_html=True,
                )
                c2.markdown(f"**{morador}**")
                c2.markdown(f"Valor: **{brl(valor)}**")
                c2.markdown('<span style="color:#E74C3C;font-weight:600">⏳ Pendente</span>', unsafe_allow_html=True)

                with c3:
                    with st.expander("Registrar pagamento"):
                        with st.form(f"pag_{ap}"):
                            valor_pago = st.number_input("Valor pago R$", value=float(valor), step=0.01, format="%.2f", key=f"vp_{ap}")
                            data_pag   = st.date_input("Data do pagamento", key=f"dt_{ap}")
                            forma      = st.selectbox("Forma", list(FORMAS.keys()), format_func=lambda k: FORMAS[k], key=f"fm_{ap}")
                            recibo_num = st.text_input("Nº do recibo", placeholder="Ex: 003/2026", key=f"rec_{ap}")
                            nome_pag   = st.text_input("Nome do pagador", value=morador if morador != "—" else "", key=f"np_{ap}")
                            enviado    = st.checkbox("Recibo enviado", key=f"env_{ap}")
                            confirmar  = st.form_submit_button("✅ Confirmar Pagamento", type="primary")

                        if confirmar:
                            st.session_state["pagamentos"][ap] = {
                                "pago":       True,
                                "valor_pago": valor_pago,
                                "data":       str(data_pag),
                                "forma":      forma,
                                "recibo":     recibo_num,
                                "enviado":    enviado,
                            }
                            pg_count = sum(1 for p in st.session_state["pagamentos"].values() if p["pago"])
                            if pg_count == 14:
                                st.session_state["checklist"]["Pagamentos registrados"] = True
                            st.success(f"✅ Pagamento do AP {ap} registrado!")
                            st.rerun()

                st.divider()

# ---- ABA PAGOS ----
with aba_pagos:
    aps_pagos = [ap for ap, p in pagamentos.items() if p["pago"]]
    if not aps_pagos:
        st.info("Nenhum pagamento registrado ainda.")
    else:
        for ap in aps_pagos:
            pg    = pagamentos[ap]
            valor = valor_por_ap[ap]
            morador = MORADORES.get(ap, "—")

            with st.container():
                c1, c2, c3, c4 = st.columns([1, 2, 2, 1])
                c1.markdown(
                    f'<div style="background:#27AE60;color:white;border-radius:8px;padding:12px;text-align:center;font-size:20px;font-weight:700">AP {ap}</div>',
                    unsafe_allow_html=True,
                )
                c2.markdown(f"**{morador}**")
                c2.markdown(f"Valor: **{brl(pg['valor_pago'])}**")
                c2.markdown('<span style="color:#27AE60;font-weight:600">✅ Pago</span>', unsafe_allow_html=True)
                c3.markdown(f"📅 {pg['data']}")
                c3.markdown(f"💳 {FORMAS.get(pg['forma'], pg['forma'])}")
                if pg.get("recibo"):
                    c3.markdown(f"🧾 Recibo {pg['recibo']}")
                enviado_badge = "✅" if pg.get("enviado") else "📤"
                c4.markdown(f"{enviado_badge} Enviado" if pg.get("enviado") else "📤 Não enviado")

                if not pg.get("enviado"):
                    if c4.button("Marcar enviado", key=f"env_ok_{ap}", use_container_width=True):
                        st.session_state["pagamentos"][ap]["enviado"] = True
                        st.rerun()

                if c4.button("↩ Estornar", key=f"estornar_{ap}", use_container_width=True):
                    st.session_state["pagamentos"][ap] = {
                        "pago": False, "valor_pago": None, "data": None,
                        "forma": None, "recibo": None, "enviado": False,
                    }
                    st.rerun()

                st.divider()
