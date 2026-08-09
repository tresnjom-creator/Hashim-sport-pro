import streamlit as st

# Podešavanje stranice
st.set_page_config(
    page_title="Hashim Sport Pro — AI Asistent",
    page_icon="⚽",
    layout="centered"
)

# Stil za chat i izgled sličan AI asistentu
st.markdown("""
    <style>
    .main-title {
        font-size: 28px;
        font-weight: bold;
        color: #1f2937;
        margin-bottom: 5px;
    }
    .sub-title {
        font-size: 14px;
        color: #6b7280;
        margin-bottom: 25px;
    }
    .chat-bubble-user {
        background-color: #e5e7eb;
        color: #1f2937;
        padding: 12px 16px;
        border-radius: 12px;
        margin-bottom: 10px;
        text-align: right;
    }
    .chat-bubble-ai {
        background-color: #f3f4f6;
        color: #1f2937;
        padding: 12px 16px;
        border-radius: 12px;
        margin-bottom: 10px;
        border-left: 4px solid #3b82f6;
    }
    </style>
""", unsafe_allow_html=True)

# Naslov aplikacije
st.markdown('<div class="main-title">⚽ Hashim Sport Pro AI</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Tvoj lični sportski analitičar i generator tiketa. Pitaj me za analizu, H2H, golove ili poene!</div>', unsafe_allow_html=True)

# Inicijalizacija istorije razgovora
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Zdravo Merzuhe! Spreman sam za analizu utakmica i sastavljanje dobitnih tiketa. Koji mečevi su danas na programu?"}
    ]

# Prikaz istorije poruka
for message in st.session_state.messages:
    if message["role"] == "user":
         st.markdown(f'<div class="chat-bubble-user"><b>Ti:</b><br>{message["content"]}</div>', unsafe_allow_html=True)
    else:
         st.markdown(f'<div class="chat-bubble-ai"><b>Hashim AI:</b><br>{message["content"]}</div>', unsafe_allow_html=True)

# Polje za unos poruke od korisnika (na dnu, kao u pravom chatu)
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Unesi parove, pitanje za analizu ili granicu (npr. Real - Barcelona preko 2.5):", placeholder="Npr. Kakav im je h2h i koliko golova?")
    submit_button = st.form_submit_button(label="Pošalji poruku")

    if submit_button and user_input:
        # Dodavanje korisnikove poruke
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Generisanje odgovora u mom stilu
        if "gol" in user_input.lower() or "over" in user_input.lower() or "2.5" in user_input:
            ai_response = f"Analiziram zahtjev za: *'{user_input}'*. Na osnovu trenutne forme, međusobnih duela (H2H) i statistike, predlog za ovaj meč je tip sa sigurnijom granicom golova ili poena. Da li želiš da dodamo ovaj par na tiket?"
        elif "tiket" in user_input.lower():
            ai_response = "Sastavljam tiket za tebe! Reci mi još parova koje želiš da ubacimo da optimizujemo ukupnu kvotu."
        else:
            ai_response = f"Razumio sam! Pratim podatke za: *'{user_input}'*. Spreman sam da izvučem statistiku i pomognem ti oko najbolje odluke."

        # Dodavanje odgovora asistenta
        st.session_state.messages.append({"role": "assistant", "content": ai_response})
        st.rerun()

# Sidebar opcije za brzu pomoć
with st.sidebar:
    st.header("⚙️ Opcije")
    if st.button("🗑️ Obriši razgovor"):
        st.session_state.messages = [
            {"role": "assistant", "content": "Razgovor je resetovan. Spreman za nove analize!"}
        ]
        st.rerun()
        
    st.markdown("---")
    st.markdown("**Status:** Online 🟢")
    st.markdown("**Režim:** Interaktivni AI Asistent")
