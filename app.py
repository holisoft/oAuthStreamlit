import streamlit as st
import login

st.set_page_config(page_title="Dashboard Listini HoliSoft", layout="wide")

st.write("✅ App avviata.")
st.write("📦 Session state:", dict(st.session_state))
st.write("📦 Query params:", st.query_params)

if not st.session_state.get("authenticated"):
    if "code" in st.query_params:
        login.handle_callback()
    else:
        login.show()
    st.stop()

st.success("✅ Login effettuato con successo!")
st.json(st.session_state["token"])

# Visualizza il token per conferma
st.subheader("🔑 Dati del token")
st.json(st.session_state["token"])

st.markdown("---")
st.write("🚀 Benvenuto nella tua app protetta!")
