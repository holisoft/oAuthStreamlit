import streamlit as st
import login

st.set_page_config(
    page_title="Dashboard Listini HoliSoft",
    layout="wide"
)

# Debug
st.write("✅ App avviata.")
st.write("Session state:", dict(st.session_state))
st.write("Query params:", st.query_params)

# Authentication flow
if "authenticated" not in st.session_state:
    if "code" in st.query_params:
        login.handle_callback()
    else:
        login.show()
    st.stop()

# Authenticated
st.success("✅ Login effettuato con successo!")

# Display token
token = st.session_state.get("token")
if token:
    st.subheader("🔑 Token di accesso")
    st.json(token)
else:
    st.warning("⚠️ Nessun token presente.")

# Main app content
st.markdown("---")
st.write("🚀 Benvenuto nella tua app protetta!")
