import streamlit as st
import matplotlib.pyplot as plt
from gtts import gTTS
import time

# --- PAGE CONFIG ---
st.set_page_config(page_title="Agro Twin - Live", page_icon="🛰️", layout="wide")
st.title("🛰️ Agro Twin: Rover Live Stream (Version 2)")

translations = {
    "Long Term": "நீண்ட கால பயிர்",
    "Short Term": "குறுகிய கால பயிர்",
    "High Profit": "அதிவேக லாப பயிர்",
    "Teak": "தேக்கு மரம்", "Mahogany": "மஹோகனி",
    "Turmeric": "மஞ்சள்", "Groundnut": "நிலக்கடலை",
    "Banana": "வாழை", "Papaya": "பப்பாளி"
}

# --- LIVE STATUS BAR ---
status_placeholder = st.empty()
status_placeholder.warning("📡 Status: Waiting for Rover Signal...")

if st.button("⚡ START ROVER DATA FETCH"):
    with st.status("Rover Navigating...", expanded=True) as status:
        st.write("Checking GPS Coordinates...")
        time.sleep(1)
        st.write("Deploying Soil Probes...")
        time.sleep(1)
        st.write("Collecting NPK & pH Data...")
        time.sleep(1)
        status.update(label="Data Received!", state="complete", expanded=False)
    
    # --- SIMULATED LIVE DATA ---
    live_ph, live_n = 7.1, 32
    lt = "Teak" if live_ph > 6.5 else "Mahogany"
    st_c = "Turmeric" if live_n > 20 else "Groundnut"
    hp = "Banana"
    p_lt, p_st, p_hp = 40, 35, 25

    # --- DASHBOARD LAYOUT ---
    st.divider()
    m1, m2, m3 = st.columns(3)
    m1.metric("Live pH", live_ph, "Normal")
    m2.metric("Nitrogen", f"{live_n} ppm", "+4")
    m3.metric("Signal Strength", "98%", "Strong")

    res_c1, res_c2 = st.columns(2)
    with res_c1:
        st.subheader("📋 Autonomous Recommendations")
        st.write(f"**{translations['Long Term']}:** {lt} — **{p_lt}%**")
        st.write(f"**{translations['Short Term']}:** {st_c} — **{p_st}%**")
        st.write(f"**{translations['High Profit']}:** {hp} — **{p_hp}%**")
        
        # Audio
        voice_text = f"ரோவர் தரவு: {p_lt} சதவீதம் {translations[lt]}, {p_st} சதவீதம் {translations[st_c]}, {p_hp} சதவீதம் {translations[hp]}."
        tts = gTTS(text=voice_text, lang='ta')
        tts.save("live_voice.mp3")
        st.audio("live_voice.mp3")
        st.balloons()

    with res_c2:
        st.subheader("📊 Live Field Composition")
        fig, ax = plt.subplots()
        ax.pie([p_lt, p_st, p_hp], labels=[lt, st_c, hp], autopct='%1.1f%%', colors=['#2e7d32', '#fbc02d', '#d32f2f'])
        st.pyplot(fig)
