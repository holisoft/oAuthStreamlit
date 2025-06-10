# app.py
import streamlit as st
import login

st.set_page_config(page_title="Dashboard Listini HoliSoft", layout="wide")

# Debug iniziale
st.write("✅ App avviata.")
st.write("📦 Session state:", dict(st.session_state))

if not st.session_state.get("authenticated"):
    login.show()
    st.stop()

# Autenticato
st.success("✅ Login completato!")
st.subheader("🔑 Token di accesso")
st.json(st.session_state["token"])

st.markdown("---")
st.write("🚀 Benvenuto nella tua app!")
