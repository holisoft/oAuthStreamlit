import streamlit as st
import login

# Deve essere la PRIMA chiamata di Streamlit
st.set_page_config(page_title="Dashboard Listini HoliSoft", layout="wide")

# Debug iniziale
st.write("✅ App avviata.")
st.write("Session state:", dict(st.session_state))
st.write("Query params:", st.query_params)

# Flow di autenticazione
if not st.session_state.get("authenticated"):
    if "code" in st.query_params:
        login.handle_callback()
    else:
        login.show()
    st.stop()

# Se arrivi qui, sei autenticato
st.success("✅ Login effettuato con successo!")

# Visualizzo il token per conferma
st.subheader("🔑 Token e dati utente")
st.json(st.session_state["token"])

# Qui il resto della tua app
st.markdown("---")
st.write("🚀 Benvenuto nella tua app protetta da Azure AD!")
