
import streamlit as st
import time

# Podešavanje stranice
st.set_page_config(page_title="Hashim Sport Pro AI", page_icon="⚽", layout="wide")

# --- CSS za Gemini stil (Tamni mod) ---
st.markdown("""
    <style>
    /* Glavna pozadina i font */
    .stApp {
        background-color: #131314;
        color: #e3e3e3;
        font-family: 'Google Sans', Roboto, Helvetica, Arial, sans-serif;
    }
    
    /* Header (Naslovna traka) - Fiksirana na vrhu */
    .header-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background-color: #1e1f20;
        padding: 15px 30px;
        display: flex;
        align-items: center;
        border-bottom: 1px solid #333;
        z-index: 1000;
    }
    .header-title {
        font-size: 22px;
        font-weight: 500;
        color: #e3e3e3;
        margin-left: 15px;
    }
    .header-icon {
        font-size: 24px;
        color: #a8c7fa;
    }

    /* Glavni kontejner za čet, sa paddingom da ne prekriva header */
    .main-chat-container {
        margin-top: 80px;
        padding-bottom: 100px;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
    }

    /* Balončići za poruke */
    .bubble-container {
        display: flex;
        margin-bottom: 30px;
    }
    .bubble-icon {
        font-size: 20px;
        margin-right: 15px;
        margin-top: 5px;
    }
    .bubble-ai {
        background-color: #1e1f20;
        padding: 15px 20px;
        border-radius: 18px;
        line-height: 1.5;
        border-top-left-radius: 5px;
    }
    .bubble-user {
        background-color: #333333;
        padding: 15px 20px;
        border-radius: 18px;
        line-height: 1.5;
        border-top-right-radius: 5px;
        margin-left: auto; /* Poravnanje desno */
        max-width: 70%;
    }

    /* Polje za unos - Fiksirano na dnu */
    .input-container {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #131314;
        padding: 20px;
        display: flex;
        justify-content: center;
        border-top: 1px solid #333;
    }
    .stTextInput > div > div > input {
        background-color: #1e1f20 !important;
        color: white !important;
        border: 1px solid #444 !important;
        border-radius: 30px !important;
        padding: 15px 20px !important;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Prikaz Header-a (Trake) ---
st.markdown(f"""
    <div class="header-container">
        <div class="header-icon">⚽</div>
        <div class="header-title">Hashim Sport Pro AI</div>
    </div>
""", unsafe_allow_html=True)

# Inicijalizacija istorije poruka
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Zdravo Merzuhe! Spreman sam za analizu utakmica i sastavljanje dobitnih tiketa. Koji mečevi su danas na programu?"}
    ]

# --- Prikaz Četa u Gemini stilu ---
st.markdown('<div class="main-chat-container">', unsafe_allow_html=True)

for message in st.session_state.messages:
    if message["role"] == "assistant":
        st.markdown(f"""
            <div class="bubble-container">
                <div class="bubble-icon">⚽</div>
                <div class="bubble-ai"><b>Hashim AI:</b><br>{message["content"]}</div>
            </div>
        """, unsafe_allow_html=True)
    else:
         st.markdown(f"""
            <div class="bubble-container">
                <div class="bubble-user"><b>Ti:</b><br>{message["content"]}</div>
            </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True) # Zatvaranje main-chat-container

# --- Polje za unos (Gemini stil) ---
st.markdown('<div class="input-container">', unsafe_allow_html=True)
with st.form(key="chat_form", clear_on_submit=True):
    # Sakrivamo labelu inputa da bi stao u jednu liniju
    user_input = st.text_input("", placeholder="Npr. Analiziraj Real - Barcelona...")
    submit_button = st.form_submit_button(label="Pošalji")

    if submit_button and user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Simulacija AI odgovora
        with st.spinner("Hashim analizira..."):
            time.sleep(1) # Simulacija razmišljanja
            bot_response = f"Analiziram vaš zahtjev za: *{user_input}*. Provjeravam statistiku..."
            st.session_state.messages.append({"role": "assistant", "content": bot_response})
            st.rerun()

st.markdown('</div>', unsafe_allow_html=True) # Zatvaranje input-container
