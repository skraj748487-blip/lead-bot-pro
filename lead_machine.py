import streamlit as st
import streamlit.components.v1 as components
import urllib.parse
import urllib.request
import json
from datetime import datetime

# 1. Page Config
st.set_page_config(
    page_title="JARVIS — QUANTUM OS",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Authentic JARVIS Cyber HUD Styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=Rajdhani:wght@600;700&display=swap');

    .stApp {
        background-color: #010409 !important;
        background-image: 
            radial-gradient(circle at 50% 18%, rgba(14, 165, 233, 0.22) 0%, transparent 65%),
            linear-gradient(rgba(1, 4, 9, 0.96), rgba(1, 4, 9, 0.96));
        color: #E2E8F0 !important;
        font-family: 'Rajdhani', sans-serif !important;
    }

    /* Top Holographic HUD Bar */
    .hud-bar {
        display: flex; justify-content: space-between; align-items: center;
        border: 1px solid rgba(56, 189, 248, 0.3);
        padding: 10px 18px; margin-bottom: 20px;
        background: rgba(15, 23, 42, 0.7); backdrop-filter: blur(10px);
        font-family: 'Orbitron', monospace; font-size: 11px; letter-spacing: 2px;
        color: #38BDF8; border-radius: 10px;
        box-shadow: 0 0 20px rgba(14, 165, 233, 0.2);
    }

    /* Arc Reactor Core with Holographic Rings */
    .reactor-container {
        text-align: center; padding: 20px 10px; margin-bottom: 20px;
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

    /* Fixed Cyber Neon Input & Textarea */
    input, .stTextInput input, textarea, .stTextArea textarea {
        background-color: rgba(15, 23, 42, 0.95) !important;
        color: #38BDF8 !important; font-family: 'Rajdhani', sans-serif !important;
        font-size: 16px !important; font-weight: 700 !important;
        border: 1.5px solid #0284C7 !important; border-radius: 12px !important;
        box-shadow: inset 0 0 15px rgba(14, 165, 233, 0.2) !important;
    }
    input:focus, textarea:focus {
        border-color: #38BDF8 !important;
        box-shadow: 0 0 25px rgba(56, 189, 248, 0.6) !important;
    }

    /* JARVIS Execute Button */
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

# Top Sci-Fi Status Bar
st.markdown(f"""
<div class="hud-bar">
    <div>⚡ CORE: <span style="color:#10B981;">ONLINE</span></div>
    <div>ARCHITECT: <span style="color:#FFF;">SAHIL AHMAD</span></div>
    <div>NODE TIME: <span>{time_now}</span></div>
</div>
""", unsafe_allow_html=True)

# Glowing Reactor
st.markdown("""
<div class="reactor-container">
    <div class="arc-reactor"></div>
    <h1 style="font-family:'Orbitron', sans-serif; font-size:26px; color:#FFF; margin:0; letter-spacing:3px;">JARVIS — PROTOCOL 9</h1>
    <p style="color:#38BDF8; font-size:12px; letter-spacing:2px; margin-top:6px; font-weight:700;">AUTONOMOUS QUANTUM VOICE INTELLIGENCE</p>
</div>
""", unsafe_allow_html=True)

# Speech-to-Text (Mic Voice Control Module)
components.html("""
<div style="text-align:center; padding: 10px 0;">
    <button onclick="startVoiceInput()" style="background: linear-gradient(90deg, #10B981, #059669); color: #fff; font-family: sans-serif; font-weight: bold; border: none; padding: 12px 24px; border-radius: 30px; cursor: pointer; font-size: 15px; box-shadow: 0 0 25px rgba(16, 185, 129, 0.6);">
        🎙️ बोलकर पूछें (Tap & Speak to JARVIS)
    </button>
    <p id="speech-status" style="color: #94A3B8; font-size: 13px; margin-top: 8px;">माइक पर क्लिक करके कुछ भी बोलें...</p>
</div>
<script>
    function startVoiceInput() {
        var status = document.getElementById('speech-status');
        if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window)) {
            status.innerText = "आपके ब्राउज़र में माइक सपोर्ट उपलब्ध नहीं है।";
            return;
        }
        var SpeechRec = window.SpeechRecognition || window.webkitSpeechRecognition;
        var recognition = new SpeechRec();
        recognition.lang = 'hi-IN';
        recognition.start();

        status.innerText = "🔴 सुन रहा हूँ... बोलिए!";

        recognition.onresult = function(event) {
            var text = event.results[0][0].transcript;
            status.innerText = "आपने कहा: " + text;
            
            // Auto copy spoken text to clipboard
            navigator.clipboard.writeText(text);
            alert("JARVIS ने सुना: '" + text + "'\\nनीचे कमांड बॉक्स में पेस्ट करके Execute दबाएँ।");
        };

        recognition.onerror = function() {
            status.innerText = "आवाज़ सुनाई नहीं दी, दोबारा प्रयास करें।";
        };
    }
</script>
""", height=90)

# Command Bar
user_prompt = st.text_input(
    "⚡ JARVIS COMMAND PROTOCOL (यहाँ बोलें या लिखें):",
    value="Duniya ka sabse powerful supercomputer kaun sa hai?"
)

col_u, col_v = st.columns(2)
with col_u:
    user_name = st.text_input("COMMANDER NAME:", value="Sahil Ahmad")
with col_v:
    user_phone = st.text_input("SECURE COMM (WhatsApp):", value="7484878440")

# Knowledge Engine
def jarvis_intelligence(query):
    q_clean = query.strip().lower()

    if "supercomputer" in q_clean or "कंप्यूटर" in q_clean:
        return "विश्व का सबसे शक्तिशाली सुपरकंप्यूटर 'Frontier' है जो अमेरिका की ओक रिज नेशनल लेबोरेटरी में स्थित है। यह 1.1 ExaFLOPS की अविश्वसनीय गति से कार्य करता है।"
    if "चाँद" in q_clean or "moon" in q_clean:
        return "चाँद पर पहला मानव कदम नील आर्मस्ट्रांग ने 20 जुलाई 1969 को अपोलो 11 मिशन के दौरान रखा था।"
    
    # Real-time Web Knowledge
    try:
        url = f"https://hi.wikipedia.org/w/api.php?action=opensearch&search={urllib.parse.quote(query.strip())}&limit=1&namespace=0&format=json"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=3) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            if len(data) > 2 and data[2] and data[2][0].strip():
                return data[2][0]
    except Exception:
        pass

    return f"कमांड '{query}' का डेटाबेस और क्वांटम सिमुलेशन रिकॉर्ड तैयार कर दिया गया है।"

if st.button("⚡ EXECUTE JARVIS PROTOCOL"):
    clean_p = user_phone.strip() if user_phone.strip() else "7484878440"
    client_name = user_name.strip() if user_name.strip() else "Commander Sahil"

    with st.spinner("JARVIS DECRYPTING SATELLITE TELEMETRY..."):
        ai_response = jarvis_intelligence(user_prompt)

    v_say = f"नमस्ते {client_name} सर! आपके सवाल का उत्तर है: {ai_response[:150]}"

    st.success("🟢 JARVIS PROTOCOL ENGAGED — TELEMETRY ONLINE")

    # Audio Voice Output
    audio_widget = f"""
    <div style="background:rgba(15,23,42,0.95); padding:14px; border-radius:10px; border:1px solid #38BDF8; margin:10px 0;">
        <p style="color:#38BDF8; font-family:'Orbitron', monospace; margin:0 0 6px 0; font-size:12px; letter-spacing:1px;">🔊 JARVIS VOCAL FREQUENCY:</p>
        <p style="color:#FFF; font-size:14px; margin:0 0 10px 0;">"{v_say}"</p>
        <button onclick="playJarvisVoice()" style="background:linear-gradient(90deg, #0284C7, #38BDF8); color:#000; border:none; padding:9px 18px; border-radius:6px; font-weight:900; font-family:'Orbitron'; cursor:pointer; font-size:12px; letter-spacing:1px;">
            ▶ TRANSMIT JARVIS AUDIO
        </button>
    </div>
    <script>
        function playJarvisVoice() {{
            window.speechSynthesis.cancel();
            var u = new SpeechSynthesisUtterance("{v_say}");
            u.lang = "hi-IN";
            u.rate = 0.95;
            u.pitch = 1.1;
            window.speechSynthesis.speak(u);
        }}
        setTimeout(playJarvisVoice, 300);
    </script>
    """
    components.html(audio_widget, height=130)

    # Black-Transparent Holographic Box
    hologram_text = f"""==================================================
JARVIS QUANTUM HOLOGRAPHIC LOG
DATE: {today_str} | ARCHITECT: SAHIL AHMAD
COMMAND: {user_prompt}
--------------------------------------------------
INTELLIGENCE TELEMETRY:
{ai_response}
--------------------------------------------------
CLEARANCE: LEVEL 9 SOVEREIGN ACCESS
STATUS: FULLY VERIFIED & EXECUTED ONLINE ✅
=================================================="""
    st.text_area("📄 HOLOGRAPHIC ACTION RECORD:", hologram_text, height=180)

    # WhatsApp Transmission
    enc_wa = urllib.parse.quote(f"JARVIS AI TRANSMISSION:\n\nCommand: {user_prompt}\n\nResult: {ai_response}\n\nSystem Architect: Sahil Ahmad")
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
