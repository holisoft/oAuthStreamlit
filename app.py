# app.py
import streamlit as st
import login
import importlib

# ✅ Deve essere la primissima cosa nel file
st.set_page_config(
    page_title="Dashboard HoliSoft",
    layout="wide"
)

# DEBUG — mostra lo stato corrente
st.write("✅ App avviata.")
st.write("Session state:", dict(st.session_state))
st.write("Query params:", st.query_params)

# 🔐 LOGIN FLOW
if "authenticated" not in st.session_state:
    # Azure restituisce ?code=...&state=... dopo il login
    if "code" in st.query_params:
        login.handle_callback()
    else:
        login.show()
    st.stop()

# ✅ SE ARRIVIAMO QUI, L’UTENTE È AUTENTICATO
st.success("✅ Login effettuato con successo!")

# Mostra info del token
token = st.session_state.get("token")
if token:
    st.subheader("🔑 Token di accesso")
    st.json(token)
else:
    st.warning("⚠ Nessun token presente.")

# Qui puoi continuare con la tua app
st.markdown("---")
st.write("🚀 Benvenuto nella tua app protetta!")
