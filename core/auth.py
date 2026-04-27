import os
import requests
import streamlit as st

SUPABASE_URL = os.getenv("SUPABASE_URL", "https://mgkyqailpawykhzsidxd.supabase.co")
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY", "")


def sign_in(email: str, password: str) -> dict | None:
    """Autentica via Supabase Auth. Retorna user dict ou None se falhar."""
    resp = requests.post(
        f"{SUPABASE_URL}/auth/v1/token?grant_type=password",
        headers={"apikey": SUPABASE_ANON_KEY, "Content-Type": "application/json"},
        json={"email": email, "password": password},
        timeout=10,
    )
    if resp.status_code == 200:
        data = resp.json()
        return {
            "access_token": data["access_token"],
            "email": data["user"]["email"],
            "user_id": data["user"]["id"],
        }
    return None


def require_auth():
    """Exibe tela de login se não autenticado. Bloqueia execução da página."""
    if "auth_user" not in st.session_state:
        st.session_state.auth_user = None

    if st.session_state.auth_user:
        return  # já autenticado, continua normalmente

    # --- Tela de login ---
    st.set_page_config(page_title="Neápolis — Login", page_icon="🏢", layout="centered")

    col = st.columns([1, 2, 1])[1]
    with col:
        st.markdown("### Sistema ADM")
        st.markdown("# Neápolis")
        st.caption("Residencial · Belo Horizonte / MG")
        st.divider()

        with st.form("login_form"):
            email = st.text_input("E-mail", placeholder="seu@email.com")
            password = st.text_input("Senha", type="password", placeholder="••••••••")
            submitted = st.form_submit_button("Entrar", use_container_width=True)

        if submitted:
            if not email or not password:
                st.error("Preencha e-mail e senha.")
            else:
                with st.spinner("Autenticando…"):
                    user = sign_in(email, password)
                if user:
                    st.session_state.auth_user = user
                    st.rerun()
                else:
                    st.error("E-mail ou senha incorretos.")

        st.caption("Acesso restrito a administradores.")

    st.stop()  # bloqueia renderização do restante da página
