# app.py
import streamlit as st
import streamlit_authenticator as stauth

# ------------------------------------------------------------
# 1) Definisci gli utenti e le loro password in chiaro
# ------------------------------------------------------------
usernames = ["admin"]
names     = ["Amministratore"]
passwords = ["password"]  # <-- qui la pw che vuoi usare per il test

# ------------------------------------------------------------
# 2) Genera gli hash in modo sicuro (passlib sotto al cofano)
# ------------------------------------------------------------
hashed_passwords = stauth.Hasher(passwords).generate()

# ------------------------------------------------------------
# 3) Costruisci il dict delle credenziali
# ------------------------------------------------------------
credentials = {
    "usernames": {
        user: {"name": name, "password": hashed}
        for user, name, hashed in zip(usernames, names, hashed_passwords)
    }
}

# ------------------------------------------------------------
# 4) Parametri cookie (usa in prod una chiave lunga e forte)
# ------------------------------------------------------------
cookie_name        = "holisoft_auth"
cookie_key         = "ciccio"        # per prova va bene, ma in produzione >32 char
cookie_expiry_days = 30
preauthorized      = []              # liste di email pre-autorizzate (se ne hai)

authenticator = stauth.Authenticate(
    credentials,
    cookie_name,
    cookie_key,
    cookie_expiry_days,
    preauthorized
)

# ------------------------------------------------------------
# 5) Mostra il form di login e popola st.session_state
# ------------------------------------------------------------
authenticator.login(location="main")

# ------------------------------------------------------------
# 6) (DEBUG) Vedi cosa c’è in session_state dopo il submit
# ------------------------------------------------------------
st.write("🔍 session_state:", dict(st.session_state))

# ------------------------------------------------------------
# 7) Gestisci lo stato di autenticazione
# ------------------------------------------------------------
auth_status = st.session_state.get("authentication_status")

if auth_status:
    # login OK
    name = st.session_state.get("name")
    st.sidebar.success(f"✅ Benvenuto, {name}!")
    st.title("🚀 Dashboard riservata")
    st.write("Contenuto segreto qui.")
    authenticator.logout(location="sidebar")

elif auth_status is False:
    st.error("❌ Username o password errati")

else:
    st.info("🔒 Inserisci username e password")
