import streamlit as st
import login

# Deve essere la PRIMA chiamata
st.set_page_config(page_title="Dashboard Listini HoliSoft", layout="wide")

# Debug iniziale
st.write("✅ App avviata.")
st.write("📦 Session state:", dict(st.session_state))
st.write("📦 Query params:", st.query_params)

# Flusso di autenticazione
if not st.session_state.get("authenticated"):
    if "code" in st.query_params:
        login.handle_callback()
    else:
        login.show()
    st.stop()

# Sei autenticato
st.success("✅ Login effettuato con successo!")

# Mostra il token per conferma
st.subheader("🔑 Token e informazioni utente")
st.json(st.session_state["token"])

# Qui inizia la tua app vera
st.markdown("---")
st.write("🚀 Benvenuto nella tua app protetta!")
