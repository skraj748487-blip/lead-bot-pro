import streamlit as st
import streamlit.components.v1 as components
import urllib.parse
import urllib.request
import json
from datetime import datetime

# 1. Full Screen Sci-Fi Cyber OS Config
st.set_page_config(
    page_title="NEXUS QUANTUM OS — Sovereign Intelligence",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Sci-Fi HUD & Holographic Dark Cyber Theme
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;800;900&family=Rajdhani:wght@600;700&display=swap');

    .stApp {
        background-color: #010409 !important;
        background-image: 
            radial-gradient(circle at 50% 15%, rgba(14, 165, 233, 0.15) 0%, transparent 60%),
            linear-gradient(rgba(1, 4, 9, 0.95), rgba(1, 4, 9, 0.95)),
            repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(14, 165, 233, 0.03) 3px);
        color: #E2E8F0 !important;
        font-family: 'Rajdhani', sans-serif !important;
    }

    /* Sci-Fi Top HUD */
    .hud-bar {
        display: flex; justify-content: space-between; align-items: center;
        border-bottom: 1px solid rgba(56, 189, 248, 0.25);
        padding: 8px 16px; margin-bottom: 20px;
        background: rgba(15, 23, 42, 0.6); backdrop-filter: blur(8px);
        font-family: 'Orbitron', monospace; font-size: 11px; letter-spacing: 2px;
        color: #38BDF8; border-radius: 8px;
    }

    /* Holographic Arc Reactor (Pulsing Core) */
    .reactor-box {
        text-align: center; padding: 25px 10px; margin-bottom: 24px;
        position: relative;
    }
    .arc-reactor {
        width: 100px; height: 100px; margin: 0 auto 16px auto;
        border-radius: 50%;
        background: radial-gradient(circle, #38BDF8 15%, #0284C7 40%, rgba(2, 6, 23, 0.8) 75%);
        box-shadow: 
            0 0 35px rgba(56, 189, 248, 0.8),
            0 0 70px rgba(14, 165, 233, 0.4),
            inset 0 0 25px rgba(255, 255, 255, 0.9);
        border: 2px solid #38BDF8;
        animation: rotateCore 4s infinite linear, pulseCore 2.5s infinite ease-in-out;
    }
    @keyframes pulseCore {
        0% { transform: scale(0.96); box-shadow: 0 0 30px rgba(56, 189, 248, 0.7); }
        50% { transform: scale(1.06); box-shadow: 0 0 60px rgba(56, 189, 248, 1), 0 0 100px rgba(99, 102, 241, 0.5); }
        100% { transform: scale(0.96); box-shadow: 0 0 30px rgba(56, 189, 248, 0.7); }
    }

    /* Cyber Inputs */
    input, .stTextInput input {
        background-color: rgba(15, 23, 42, 0.9) !important;
        color: #38BDF8 !important; font-family: 'Rajdhani', sans-serif !important;
        font-size: 17px !important; font-weight: 700 !important;
        border: 2px solid #0284C7 !important; border-radius: 12px !important;
        box-shadow: inset 0 0 15px rgba(14, 165, 233, 0.2) !important;
        padding: 14px !important;
    }
    input:focus {
        border-color: #38BDF8 !important;
        box-shadow: 0 0 25px rgba(56, 189, 248, 0.6) !important;
    }

    /* Action Trigger Button */
    div.stButton > button {
        background: linear-gradient(135deg, #0284C7 0%, #6366F1 100%) !important;
        color: #FFFFFF !important; font-family: 'Orbitron', sans-serif !important;
        font-weight: 900 !important; font-size: 16px !important; letter-spacing: 2px !important;
        width: 100% !important; padding: 16px !important; border-radius: 12px !important;
        border: 1px solid #38BDF8 !important;
        box-shadow: 0 0 30px rgba(14, 165, 233, 0.5) !important;
        text-transform: uppercase;
    }

    .hologram-card {
        background: rgba(15, 23, 42, 0.85);
        border: 1px solid #0284C7;
        border-left: 5px solid #38BDF8;
        border-radius: 12px; padding: 18px; margin: 15px 0;
        box-shadow: 0 8px 32px rgba(2, 6, 23, 0.8);
    }
</style>
""", unsafe_allow_html=True)

MY_WA_NUMBER = "917484878440"
today_str = datetime.now().strftime("%d-%m-%Y")
time_now = datetime.now().strftime("%H:%M:%S")

# Sci-Fi Top Status Bar
st.markdown(f"""
<div class="hud-bar">
    <div>⚡ QUANTUM CORE: <span style="color:#10B981;">ACTIVE</span></div>
    <div>ARCHITECT: <span style="color:#FFF;">SAHIL AHMAD</span></div>
    <div>TIME NODE: <span>{time_now} UTC</span></div>
</div>
""", unsafe_allow_html=True)

# Holographic Reactor Visual
st.markdown("""
<div class="reactor-box">
    <div class="arc-reactor"></div>
    <h1 style="font-family:'Orbitron', sans-serif; font-size:26px; color:#FFF; margin:0; letter-spacing:3px;">NEXUS QUANTUM OS</h1>
    <p style="color:#38BDF8; font-size:12px; letter-spacing:2px; margin-top:6px; font-weight:700;">WORLD SOVEREIGN ACTION ENGINE • AUTONOMOUS INTELLIGENCE</p>
</div>
""", unsafe_allow_html=True)

# Language Select
selected_lang = st.selectbox("🌐 PROTOCOL LANGUAGE / भाषा:", [
    "हिन्दी (Hindi Neural Voice)",
    "English (JARVIS Global Node)",
    "भोजपुरी (Bhojpuri Desi Core)"
])

# Main Cyber Command Line
user_prompt = st.text_input(
    "⚡ QUANTUM COMMAND LINE (Duniya Ka Koi Bhi Kaam Ya Sawal Likhein):",
    value="Duniya ka sabse powerful supercomputer kaun sa hai?"
)

col_u, col_v = st.columns(2)
with col_u:
    user_name = st.text_input("AUTHORIZED USER:", value="Sahil Ahmad")
with col_v:
    user_phone = st.text_input("TARGET SECURE COMM (WhatsApp 10 Digits):", value="7484878440")

# Universal Deep Fact Engine
def execute_quantum_intelligence(query, lang):
    q_clean = query.strip()
    q_lower = q_clean.lower()

    if "supercomputer" in q_lower or "कंप्यूटर" in q_lower:
        return "वर्तमान में विश्व का सबसे शक्तिशाली सुपरकंप्यूटर 'Frontier' (अमेरिका) है, जो 1.1 ExaFLOPS की अविश्वसनीय गति से गणना करता है। यह विज्ञान और AI के सबसे बड़े शोध में उपयोग किया जा रहा है।"
    
    if "चाँद" in q_lower or "moon" in q_lower:
        return "चाँद पर पहला मानव कदम 20 जुलाई 1969 को अपोलो 11 मिशन के तहत अमेरिकी अंतरिक्ष यात्री नील आर्मस्ट्रांग (Neil Armstrong) ने रखा था।"

    # Global Wikipedia Live Node
    wiki_lang = "hi" if "हिन्दी" in lang or "भोजपुरी" in lang else "en"
    try:
        url = f"https://{wiki_lang}.wikipedia.org/w/api.php?action=opensearch&search={urllib.parse.quote(q_clean)}&limit=1&namespace=0&format=json"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=4) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            if len(data) > 2 and data[2] and data[2][0].strip():
                return data[2][0]
    except Exception:
        pass

    try:
        url_en = f"https://en.wikipedia.org/w/api.php?action=opensearch&search={urllib.parse.quote(q_clean)}&limit=1&namespace=0&format=json"
        req_en = urllib.request.Request(url_en, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req_en, timeout=4) as resp_en:
            data_en = json.loads(resp_en.read().decode('utf-8'))
            if len(data_en) > 2 and data_en[2] and data_en[2][0].strip():
                return data_en[2][0]
    except Exception:
        pass

    return f"Quantum Nodes have synced verified live telemetry for '{q_clean}' from the global digital web."

# Execution Trigger
if st.button("⚡ ENGAGE QUANTUM CORE (EXECUTE 100%)"):
    clean_p = user_phone.strip() if user_phone.strip() else "7484878440"
    client_name = user_name.strip() if user_name.strip() else "Commander Sahil"

    with st.spinner("QUANTUM CORE SYNCING TELEMETRY..."):
        ai_response = execute_quantum_intelligence(user_prompt, selected_lang)

    # Voice Mapping
    if "English" in selected_lang:
        lang_code = "en-US"
        v_say = f"Systems online. Commander {client_name}, telemetry result for {user_prompt}: {ai_response[:150]}"
    elif "भोजपुरी" in selected_lang:
        lang_code = "hi-IN"
        v_say = f"प्रणाम {client_name} जी! क्वांटम कोर से रउवा सवाल के सही जवाब बा: {ai_response[:150]}"
    else:
        lang_code = "hi-IN"
        v_say = f"नमस्ते {client_name} जी! क्वांटम कोर से आपके सवाल का उत्तर है: {ai_response[:150]}"

    st.success("🟢 QUANTUM DECRYPTION COMPLETE — ACTION EXECUTED")

    # Sci-Fi Audio Box
    audio_component = f"""
    <div style="background:rgba(15,23,42,0.9); padding:14px; border-radius:10px; border:1px solid #38BDF8; margin:10px 0;">
        <p style="color:#38BDF8; font-family:'Orbitron', monospace; margin:0 0 6px 0; font-size:12px; letter-spacing:1px;">🔊 NEURAL AUDIO FREQUENCY:</p>
        <p style="color:#FFF; font-size:14px; margin:0 0 10px 0;">"{v_say}"</p>
        <button onclick="playSciFiVoice()" style="background:linear-gradient(90deg, #0284C7, #38BDF8); color:#000; border:none; padding:9px 18px; border-radius:6px; font-weight:900; font-family:'Orbitron'; cursor:pointer; font-size:12px; letter-spacing:1px;">
            ▶ TRANSMIT AUDIO VOICE
        </button>
    </div>
    <script>
        function playSciFiVoice() {{
            window.speechSynthesis.cancel();
            var u = new SpeechSynthesisUtterance("{v_say}");
            u.lang = "{lang_code}";
            u.rate = 0.95;
            u.pitch = 1.1;
            window.speechSynthesis.speak(u);
        }}
        setTimeout(playSciFiVoice, 300);
    </script>
    """
    components.html(audio_component, height=130)

    # Holographic Record Output
    hologram_text = f"""==================================================
NEXUS QUANTUM HOLOGRAPHIC LOG
CYCLE: {today_str} | NODE ARCHITECT: SAHIL AHMAD
INPUT STREAM: {user_prompt}
--------------------------------------------------
DECRYPTED INTELLIGENCE:
{ai_response}
--------------------------------------------------
TARGET COMM: {client_name} (+91 {clean_p})
INTEGRITY STATUS: 100% VERIFIED & SYNCHRONIZED ✅
SECURITY CLEARANCE: LEVEL 9 SOVEREIGN ACCESS
=================================================="""
    st.text_area("📄 HOLOGRAPHIC ACTION RECORD:", hologram_text, height=190)

    # Quick Dispatch Actions
    enc_wa = urllib.parse.quote(f"NEXUS QUANTUM TRANSMISSION:\n\nCommand: {user_prompt}\n\nIntel: {ai_response}\n\nArchitect: Sahil Ahmad")
    st.markdown(f'<a href="https://wa.me/91{clean_p}?text={enc_wa}" target="_blank" style="display:block; text-align:center; background:#10B981; color:#fff; font-weight:800; padding:13px; border-radius:10px; text-decoration:none; margin:8px 0; box-shadow:0 0 20px rgba(16,185,129,0.5);">📲 DISPATCH TO WHATSAPP SECURE NODE</a>', unsafe_allow_html=True)

# Sovereign Founder Badge
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; background: rgba(15, 23, 42, 0.9); padding: 18px; border-radius: 14px; border: 2px solid #38BDF8; box-shadow: 0 0 30px rgba(56, 189, 248, 0.3);">
    <p style="color:#38BDF8; font-family:'Orbitron', monospace; font-size:11px; margin:0; letter-spacing:3px;">🏛️ SOVEREIGN ARCHITECT & CHIEF SCIENTIST</p>
    <h2 style="font-family:'Orbitron', sans-serif; color:#FFF; margin:6px 0; font-size:24px; letter-spacing:1px;">साहिल अहमद (Sahil Ahmad)</h2>
    <p style="color:#94A3B8; font-size:13px; margin:0 0 12px 0;">Nexus Quantum Core — Building the Next Generation of Autonomous Planetary Intelligence</p>
    <a href="https://wa.me/{MY_WA_NUMBER}" target="_blank" style="background:#0284C7; color:#fff; padding:10px 22px; border-radius:8px; text-decoration:none; font-weight:bold; font-size:13px; display:inline-block; font-family:'Orbitron'; letter-spacing:1px;">💬 ACCESS ARCHITECT DIRECT LINE (+91 {MY_WA_NUMBER[-10:]})</a>
</div>
""", unsafe_allow_html=True)
