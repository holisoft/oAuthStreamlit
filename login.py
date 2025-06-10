# login.py
import streamlit as st
import os
import msal
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID     = os.getenv("AZURE_CLIENT_ID")
CLIENT_SECRET = os.getenv("AZURE_CLIENT_SECRET")
TENANT_ID     = os.getenv("AZURE_TENANT_ID")
AUTHORITY     = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPES        = ["User.Read"]

def show():
    """Mostra la schermata di avvio del Device Code Flow."""
    st.title("🔐 Login con Azure AD (Device Code Flow)")

    msal_app = msal.ConfidentialClientApplication(
        CLIENT_ID,
        authority=AUTHORITY,
        client_credential=CLIENT_SECRET
    )

    device_flow = msal_app.initiate_device_flow(scopes=SCOPES)
    if "user_code" not in device_flow:
        st.error("Impossibile iniziare il device flow.")
        st.stop()

    # Salvo il dispositivo
    st.session_state["device_flow"] = device_flow

    st.write("1. Vai a:", device_flow["verification_uri"])
    st.write("2. Inserisci il codice:", device_flow["user_code"])
    st.write("---")
    if st.button("Ho effettuato l’accesso"):
        handle_device_flow()

def handle_device_flow():
    """Esegue il polling per ottenere il token dopo che l’utente ha loggato."""
    device_flow = st.session_state.get("device_flow")
    if not device_flow:
        st.error("Sessione di device flow non trovata. Riprova.")
        st.stop()

    msal_app = msal.ConfidentialClientApplication(
        CLIENT_ID,
        authority=AUTHORITY,
        client_credential=CLIENT_SECRET
    )
    result = msal_app.acquire_token_by_device_flow(device_flow)

    # Debug: vedi cosa torna
    st.write("🔄 Result from acquire_token_by_device_flow():", result)
    st.write("📦 Session state subito dopo polling:", dict(st.session_state))

    if result and "access_token" in result:
        st.session_state["authenticated"] = True
        st.session_state["token"] = result
        st.experimental_rerun()
    else:
        err  = result.get("error", "unknown_error")
        desc = result.get("error_description", "")
        st.error(f"❌ Errore token: {err} — {desc}")
        st.stop()
