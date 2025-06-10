import streamlit as st
import login

st.set_page_config(...)

# Controllo autenticazione
if "authenticated" not in st.session_state:
    if "code" in st.query_params:
        login.handle_callback()
    else:
        login.show()
    st.stop()

# Se sei qui, sei autenticato
st.success("🔒 Login effettuato con successo!")

# Mostra i dati del token
token = st.session_state.get("token")
if token:
    st.subheader("🧾 Dati del token ricevuto:")
    st.json(token)  # visualizza il token in JSON
else:
    st.error("Problema: token non presente in session_state")

# Continua con il resto dell'app...
