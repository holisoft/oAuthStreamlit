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
    st.title("🔐 Login con Azure AD (Device Code Flow)")

    # Usa ConfidentialClientApplication, così include client_secret
    msal_app = msal.ConfidentialClientApplication(
        CLIENT_ID,
        authority=AUTHORITY,
        client_credential=CLIENT_SECRET
    )

    device_flow = msal_app.initiate_device_flow(scopes=SCOPES)
    if "user_code" not in device_flow:
        st.error("Impossibile iniziare il device flow.")
        st.stop()

    st.session_state["device_flow"] = device_flow

    st.write("1. Vai a:", device_flow["verification_uri"])
    st.write("2. Inserisci il codice:", device_flow["user_code"])
    st.write("---")
    if st.button("Ho effettuato l’accesso"):
        handle_device_flow()

def handle_device_flow():
    device_flow = st.session_state.get("device_flow")
    if not device_flow:
        st.error("Sessione di device flow non trovata. Riprova.")
        st.stop()

    msal_app = msal.ConfidentialClientApplication(
        CLIENT_ID,
        authority=AUTHORITY,
        client_credential=CLIENT_SECRET
    )
    # Ora include automaticamente client_secret nella richiesta
    result = msal_app.acquire_token_by_device_flow(device_flow)

    if "access_token" in result:
        st.session_state["authenticated"] = True
        st.session_state["token"] = result
        st.experimental_rerun()
    else:
        st.error(f"❌ Errore token: {result.get('error')} — {result.get('error_description')}")
        st.stop()
