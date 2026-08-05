import streamlit as st
from data_fetcher import fetch_football_data

st.set_page_config(page_title="Hashim Sport Pro - Autonomni", page_icon="⚽", layout="centered")

st.title("⚽ Hashim Sport Pro (Autonomni Režim)")
st.write("Dobrodošao! Aplikacija je prešla u pametni, autonomni rad. Pritisni dugme ispod da pokreneš pretragu i analizu mečeva sa interneta bez ručnog unosa.")

if st.button("Pokreni automatsku analizu mečeva", type="primary"):
    with st.spinner("Sistem skuplja podatke i analizira lige..."):
        leagues, matches = fetch_football_data()
        
        st.success("Analiza uspješno završena!")
        
        st.subheader("📊 Aktivne lige u praćenju:")
        for l in leagues:
            st.markdown(f"- **{l['league_name']}** (Prioritet: {l['priority']})")
        
        st.subheader("🎯 Automatski izdvojeni mečevi i preporuke:")
        for m in matches:
            st.info(f"**{m['match']}**\n\n* **Liga:** {m['league']}\n* **Prosjek golova:** {m['avg_goals']}\n* **Preporuka:** {m['recommendation']}")

st.markdown("---")
st.caption("Hashim Sport Pro v2 — Autonomni sistem za analizu sportskih mečeva.")
