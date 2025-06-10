# login.py
import streamlit as st
from authlib.integrations.requests_client import OAuth2Session
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("AZURE_CLIENT_ID")
CLIENT_SECRET = os.getenv("AZURE_CLIENT_SECRET")
TENANT_ID = os.getenv("AZURE_TENANT_ID")
REDIRECT_URI = os.getenv("AZURE_REDIRECT_URI")

AUTH_URL = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/authorize"
TOKEN_URL = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"
SCOPE = ["openid", "profile", "email"]

def show():
    st.title("Login con Azure AD")

    oauth = OAuth2Session(CLIENT_ID, CLIENT_SECRET, scope=SCOPE, redirect_uri=REDIRECT_URI)
    authorization_url, state = oauth.create_authorization_url(AUTH_URL)
    st.session_state["oauth_state"] = state

    st.markdown(f"[🔐 Clicca qui per accedere con Microsoft]({authorization_url})")

def handle_callback():
    code = st.query_params.get("code")
    state = st.query_params.get("state")
st.write("📦 code ricevuto:", code)
st.write("📦 state ricevuto:", state)
st.write("📦 state salvato in session_state:", st.session_state.get("oauth_state"))
