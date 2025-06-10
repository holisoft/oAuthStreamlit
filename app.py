import streamlit as st
import login

st.set_page_config(page_title="Dashboard Listini HoliSoft", layout="wide")

# Debug
st.write("✅ App avviata.")
st.write("📦 Session state:", dict(st.session_state))

# Flusso di autenticazione
if not st.session_state.get("authenticated"):
    login.show()
    st.stop()

# Autenticato
st.success("✅ Login completato!")
st.subheader("🔑 Token di accesso")
st.json(st.session_state["token"])

# Qui parte la tua app protetta...
st.markdown("---")
st.write("🚀 Benvenuto nella tua app!")
