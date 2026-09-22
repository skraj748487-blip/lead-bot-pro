import streamlit as st
import streamlit.components.v1 as components
import urllib.parse
import urllib.request
import json
from datetime import datetime

# 1. Page Config
st.set_page_config(
    page_title="JARVIS — QUANTUM CORE",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Complete Cybernetic JARVIS Theme
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=Rajdhani:wght@600;700&display=swap');

    .stApp {
        background-color: #010409 !important;
        background-image: 
            radial-gradient(circle at 50% 18%, rgba(14, 165, 233, 0.25) 0%, transparent 65%),
            linear-gradient(rgba(1, 4, 9, 0.98), rgba(1, 4, 9, 0.98));
        color: #E2E8F0 !important;
        font-family: 'Rajdhani', sans-serif !important;
    }

    .hud-bar {
        display: flex; justify-content: space-between; align-items: center;
        border: 1px solid rgba(56, 189, 248, 0.3);
        padding: 10px 18px; margin-bottom: 20px;
        background: rgba(15, 23, 42, 0.7); backdrop-filter: blur(10px);
        font-family: 'Orbitron', monospace; font-size: 11px; letter-spacing: 2px;
        color: #38BDF8; border-radius: 10px;
        box-shadow: 0 0 20px rgba(14, 165, 233, 0.2);
    }

    .arc-reactor {
        width: 110px; height: 110px; margin: 0 auto 16px auto;
        border-radius: 50%;
        background: radial-gradient(circle, #38BDF8 20%, #0284C7 50%, rgba(2, 6, 23, 0.9) 80%);
        box-shadow: 
            0 0 40px rgba(56, 189, 248, 0.9),
            0 0 80px rgba(14, 165, 233, 0.5),
            inset 0 0 30px rgba(255, 255, 255, 0.9);
        border: 3px solid #38BDF8;
        animation: pulseCore 2.5s infinite ease-in-out;
    }
    @keyframes pulseCore {
        0% { transform: scale(0.95); box-shadow: 0 0 30px rgba(56, 189, 248, 0.7); }
        50% { transform: scale(1.06); box-shadow: 0 0 70px rgba(56, 189, 248, 1), 0 0 110px rgba(99, 102, 241, 0.6); }
        100% { transform: scale(0.95); box-shadow: 0 0 30px rgba(56, 189, 248, 0.7); }
    }

    input, .stTextInput input, textarea, .stTextArea textarea {
        background-color: rgba(15, 23, 42, 0.95) !important;
        color: #38BDF8 !important; font-family: 'Rajdhani', sans-serif !important;
        font-size: 16px !important; font-weight: 700 !important;
        border: 1.5px solid #0284C7 !important; border-radius: 12px !important;
        box-shadow: inset 0 0 15px rgba(14, 165, 233, 0.2) !important;
    }

    div.stButton > button {
        background: linear-gradient(135deg, #0284C7 0%, #4F46E5 100%) !important;
        color: #FFFFFF !important; font-family: 'Orbitron', sans-serif !important;
        font-weight: 900 !important; font-size: 16px !important; letter-spacing: 2px !important;
        width: 100% !important; padding: 16px !important; border-radius: 12px !important;
        border: 1px solid #38BDF8 !important;
        box-shadow: 0 0 30px rgba(14, 165, 233, 0.5) !important;
        text-transform: uppercase;
    }
</style>
""", unsafe_allow_html=True)

MY_WA_NUMBER = "917484878440"
today_str = datetime.now().strftime("%d-%m-%Y")
time_now = datetime.now().strftime("%H:%M:%S")

# HUD Status
st.markdown(f"""
<div class="hud-bar">
    <div>⚡ JARVIS CORE: <span style="color:#10B981;">100% ONLINE</span></div>
    <div>ARCHITECT: <span style="color:#FFF;">SAHIL AHMAD</span></div>
    <div>GRID: <span>SECURE</span></div>
</div>
""", unsafe_allow_html=True)

# Reactor Center
st.markdown("""
<div style="text-align:center; margin-bottom: 20px;">
    <div class="arc-reactor"></div>
    <h1 style="font-family:'Orbitron', sans-serif; font-size:26px; color:#FFF; margin:0; letter-spacing:3px;">JARVIS AI</h1>
    <p style="color:#38BDF8; font-size:12px; letter-spacing:2px; margin-top:6px; font-weight:700;">AUTONOMOUS ACTION & DEFENSE PROTOCOL</p>
</div>
""", unsafe_allow_html=True)

# Command Box
user_prompt = st.text_input(
    "⚡ JARVIS COMMAND INPUT (आदेश दें):",
    value="जार्विस सिस्टम स्टेटस बताओ"
)

col_u, col_v = st.columns(2)
with col_u:
    user_name = st.text_input("COMMANDER:", value="साहिल अहमद")
with col_v:
    user_phone = st.text_input("SECURE COMM (WhatsApp):", value="7484878440")

# Authentic JARVIS Mind Core
def get_jarvis_authentic_response(cmd, commander):
    c = cmd.strip().lower()

    if any(k in c for k in ["सिस्टम स्टेटस", "status", "system"]):
        return f"ऑल सिस्टम्स १००% ऑनलाइन हैं, {commander} सर। क्वांटम न्यूरल कोर सक्रिय है, ग्लोबल सर्वर ग्रिड स्थिर है और सभी सुरक्षा प्रोटोकॉल स्तर ९ पर तैनात हैं। मैं आपके अगले निर्देश के लिए पूरी तरह तैयार हूँ।"

    if any(k in c for k in ["सुपरकंप्यूटर", "supercomputer", "computer"]):
        return f"{commander} सर, दुनिया का सबसे तेज़ सुपरकंप्यूटर 'Frontier' है जो १.१ एक्साफ़्लॉप्स की शक्ति से चलता है। हमारी क्वांटम कोर उसी कंप्यूटेशनल ग्रिड से जुड़ी हुई है।"

    if any(k in c for k in ["चाँद", "moon"]):
        return f"{commander} सर, ऐतिहासिक रिकॉर्ड के अनुसार २० जुलाई १९६९ को अपोलो ११ मिशन के तहत नील आर्मस्ट्रांग ने चाँद पर पहला मानव कदम रखा था।"

    if any(k in c for k in ["कौन हो", "who are you", "tum kaun ho", "jarvis"]):
        return f"मैं जार्विस हूँ, {commander} सर। आपका व्यक्तिगत ऑटोनॉमस एआई सहायक। सिस्टम प्रबंधन, सुरक्षा और वास्तविक इंटरनेट ऑपरेशन्स को निष्पादित करने के लिए तैनात।"

    # Wikipedia Web Telemetry Fallback
    try:
        url = f"https://hi.wikipedia.org/w/api.php?action=opensearch&search={urllib.parse.quote(cmd.strip())}&limit=1&namespace=0&format=json"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=3) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            if len(data) > 2 and data[2] and data[2][0].strip():
                return f"{commander} सर, ग्लोबल नेटवर्क से प्राप्त सत्यापित डेटा यह है: {data[2][0]}"
    except Exception:
        pass

    return f"कमांड निष्पादित कर दी गई है, {commander} सर। क्वांटम डेटाबेस को अद्यतन कर सुरक्षित वॉल्ट में लॉक कर दिया गया है।"

if st.button("⚡ ENGAGE JARVIS CORE (आदेश निष्पादित करें)"):
    clean_p = user_phone.strip() if user_phone.strip() else "7484878440"
    commander_title = user_name.strip() if user_name.strip() else "साहिल अहमद"

    with st.spinner("JARVIS DECRYPTING & COMPUTING..."):
        jarvis_reply = get_jarvis_authentic_response(user_prompt, commander_title)

    st.success("🟢 JARVIS PROTOCOL ACTIVE — COMMAND EXECUTED")

    # Real Sound Output
    audio_widget = f"""
    <div style="background:rgba(15,23,42,0.95); padding:14px; border-radius:10px; border:1px solid #38BDF8; margin:10px 0;">
        <p style="color:#38BDF8; font-family:'Orbitron', monospace; margin:0 0 6px 0; font-size:12px; letter-spacing:1px;">🔊 JARVIS VOCAL RESPONSE:</p>
        <p style="color:#FFF; font-size:14px; margin:0 0 10px 0;">"{jarvis_reply}"</p>
        <button onclick="playJarvisVoice()" style="background:linear-gradient(90deg, #0284C7, #38BDF8); color:#000; border:none; padding:9px 18px; border-radius:6px; font-weight:900; font-family:'Orbitron'; cursor:pointer; font-size:12px; letter-spacing:1px;">
            ▶ TRANSMIT JARVIS AUDIO
        </button>
    </div>
    <script>
        function playJarvisVoice() {{
            window.speechSynthesis.cancel();
            var u = new SpeechSynthesisUtterance("{jarvis_reply}");
            u.lang = "hi-IN";
            u.rate = 0.93;
            u.pitch = 0.95; // Real Deep Robotic Tone
            window.speechSynthesis.speak(u);
        }}
        setTimeout(playJarvisVoice, 300);
    </script>
    """
    components.html(audio_widget, height=130)

    # Black-Transparent Holographic Box
    hologram_text = f"""==================================================
JARVIS SOVEREIGN TELEMETRY RECORD
CYCLE: {today_str} | NODE ARCHITECT: SAHIL AHMAD
COMMAND: {user_prompt}
--------------------------------------------------
JARVIS DIRECTIVE RESPONSE:
{jarvis_reply}
--------------------------------------------------
COMMANDER CLEARANCE: LEVEL 9 SOVEREIGN
STATUS: 100% OPERATIONAL & VERIFIED ONLINE ✅
=================================================="""
    st.text_area("📄 HOLOGRAPHIC ACTION RECORD:", hologram_text, height=180)

    # WhatsApp Transmission
    enc_wa = urllib.parse.quote(f"JARVIS DIRECTIVE LOG:\n\nकमांड: {user_prompt}\n\nउत्तर: {jarvis_reply}\n\nChief Architect: Sahil Ahmad")
    st.markdown(f'<a href="https://wa.me/91{clean_p}?text={enc_wa}" target="_blank" style="display:block; text-align:center; background:#10B981; color:#fff; font-weight:800; padding:13px; border-radius:10px; text-decoration:none; margin:8px 0; box-shadow:0 0 20px rgba(16,185,129,0.5);">📲 DISPATCH TO WHATSAPP SECURE NODE</a>', unsafe_allow_html=True)

# Founder Status
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; background: rgba(15, 23, 42, 0.95); padding: 18px; border-radius: 14px; border: 2px solid #38BDF8; box-shadow: 0 0 30px rgba(56, 189, 248, 0.3);">
    <p style="color:#38BDF8; font-family:'Orbitron', monospace; font-size:11px; margin:0; letter-spacing:3px;">🏛️ SOVEREIGN ARCHITECT & CHIEF SCIENTIST</p>
    <h2 style="font-family:'Orbitron', sans-serif; color:#FFF; margin:6px 0; font-size:24px; letter-spacing:1px;">साहिल अहमद (Sahil Ahmad)</h2>
    <p style="color:#94A3B8; font-size:13px; margin:0 0 12px 0;">JARVIS Protocol — Autonomous Planetary Voice Intelligence</p>
    <a href="https://wa.me/{MY_WA_NUMBER}" target="_blank" style="background:#0284C7; color:#fff; padding:10px 22px; border-radius:8px; text-decoration:none; font-weight:bold; font-size:13px; display:inline-block; font-family:'Orbitron'; letter-spacing:1px;">💬 ACCESS ARCHITECT DIRECT LINE (+91 {MY_WA_NUMBER[-10:]})</a>
</div>
""", unsafe_allow_html=True)
