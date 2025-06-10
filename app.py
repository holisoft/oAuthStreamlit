# app.py
import streamlit as st
import login

# Deve essere la PRIMA chiamata di Streamlit
st.set_page_config(page_title="Dashboard HoliSoft", layout="wide")

# Debug iniziale
st.write("✅ App avviata.")
st.write("📦 Session state:", dict(st.session_state))
st.write("📦 Query params:", st.query_params)

# **Flusso di autenticazione**
if not st.session_state.get("authenticated"):
    if "code" in st.query_params:
        # Sei rientrato dal redirect Azure
        login.handle_callback()
    else:
        # Mostra il link di login
        login.show()
    st.stop()

# **Qui sei autenticato**
st.success("✅ Login effettuato con successo!")

# Visualizza il token per conferma
st.subheader("🔑 Dati del token")
st.json(st.session_state["token"])

st.markdown("---")
st.write("🚀 Benvenuto nella tua app protetta!")
