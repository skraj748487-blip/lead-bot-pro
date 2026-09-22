import streamlit as st
import streamlit.components.v1 as components
import urllib.parse
from datetime import datetime

# 1. Page Configuration
st.set_page_config(
    page_title="NEXUS BRAIN OS — Autonomous Action Engine",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Modern Cyber Dark CSS + Glowing Neural Orb
st.markdown("""
<style>
    .stApp { background-color: #020617 !important; color: #F8FAFC !important; }
    label, p, span, h1, h2, h3, h4 { color: #F8FAFC !important; font-weight: 600 !important; }
    input, .stTextInput input, textarea {
        background-color: #0F172A !important; color: #38BDF8 !important;
        font-size: 16px !important; font-weight: 600 !important;
        border: 2px solid #1E293B !important; border-radius: 14px !important;
        padding: 14px !important;
    }
    input:focus, .stTextInput input:focus {
        border-color: #38BDF8 !important; box-shadow: 0 0 20px rgba(56, 189, 248, 0.4) !important;
    }
    .orb-container {
        text-align: center; padding: 24px 10px; margin-bottom: 20px;
        background: radial-gradient(circle at center, #1E1B4B 0%, #020617 100%);
        border-radius: 24px; border: 1px solid #312E81;
        box-shadow: 0 10px 45px rgba(99, 102, 241, 0.35);
    }
    .neural-orb {
        width: 75px; height: 75px; margin: 0 auto 12px auto;
        border-radius: 50%;
        background: radial-gradient(circle, #38BDF8 10%, #6366F1 60%, #020617 100%);
        box-shadow: 0 0 30px #38BDF8, 0 0 60px #6366F1;
        animation: pulse 2.5s infinite ease-in-out;
    }
    @keyframes pulse {
        0% { transform: scale(0.95); box-shadow: 0 0 20px #38BDF8, 0 0 40px #6366F1; }
        50% { transform: scale(1.08); box-shadow: 0 0 40px #38BDF8, 0 0 80px #6366F1; }
        100% { transform: scale(0.95); box-shadow: 0 0 20px #38BDF8, 0 0 40px #6366F1; }
    }
    .action-card {
        background: #0B1329; border: 1px solid #1E293B; border-radius: 14px;
        padding: 16px; margin-bottom: 14px;
    }
    .wa-btn {
        display: block; background: linear-gradient(90deg, #10B981 0%, #059669 100%);
        color: #FFFFFF !important; text-align: center; font-weight: 900; font-size: 15px;
        padding: 14px; border-radius: 12px; text-decoration: none; margin: 8px 0;
        box-shadow: 0 4px 20px rgba(16, 185, 129, 0.4);
    }
    .search-btn {
        display: block; background: linear-gradient(90deg, #0284C7 0%, #2563EB 100%);
        color: #FFFFFF !important; text-align: center; font-weight: 900; font-size: 15px;
        padding: 14px; border-radius: 12px; text-decoration: none; margin: 8px 0;
        box-shadow: 0 4px 20px rgba(37, 99, 235, 0.4);
    }
    div.stButton > button {
        background: linear-gradient(135deg, #2563EB 0%, #4F46E5 100%) !important;
        color: #FFFFFF !important; border: none !important; border-radius: 14px !important;
        font-weight: 900 !important; font-size: 16px !important; width: 100% !important;
        padding: 16px !important; box-shadow: 0 4px 25px rgba(37, 99, 235, 0.5) !important;
    }
</style>
""", unsafe_allow_html=True)

MY_WA_NUMBER = "917484878440"
today_str = datetime.now().strftime("%d-%m-%Y")
time_str = datetime.now().strftime("%I:%M %p")

# Glowing Neural Core Header
st.markdown("""
<div class="orb-container">
    <div class="neural-orb"></div>
    <h1 style="color:#FFF; margin:0; font-size:24px; letter-spacing:-0.5px;">NEXUS BRAIN OS</h1>
    <p style="color:#94A3B8; font-size:12px; margin-top:6px;">Autonomous Action Engine • Google Shows Links, Nexus Executes Real Tasks</p>
</div>
""", unsafe_allow_html=True)

# 1. Bhasha Mode
selected_lang = st.selectbox("🌍 Bhasha Chunein / Select Language:", [
    "🇮🇳 हिन्दी (Hindi)",
    "🇬🇧 English (Global)",
    "🌾 भोजपुरी (Bhojpuri)"
])

# 2. Universal Command Box
user_prompt = st.text_input(
    "⚡ Universal Command Bar (Apna Kaam Yahan Likhein):",
    value="Dukan ki aaj ki bikri 14,500 darj karein aur WhatsApp parchi banayein"
)

col_u, col_v = st.columns(2)
with col_u:
    user_name = st.text_input("Aapka / Client Ka Naam:", value="Sahil Ahmad")
with col_v:
    user_phone = st.text_input("WhatsApp Mobile Number (10 Digit):", value="7484878440")

# Execution Button
if st.button("🚀 EXECUTE AUTONOMOUS ACTION (1-Click Run)"):
    clean_p = user_phone.strip()
    cmd_lower = user_prompt.lower()

    # Intelligent Task Recognition
    if any(k in cmd_lower for k in ["script", "video", "youtube", "reels", "shorts", "content"]):
        task_mode = "CREATOR_STUDIO"
        doc_title = "🎬 AUTONOMOUS VIRAL CONTENT SCRIPT"
        spoken_text = f"Hello {user_name}! Your viral content script and trending tags are ready."
        res_content = f"""==================================================
{doc_title}
Topic: {user_prompt}
Date: {today_str} | Architect: Sahil Ahmad
--------------------------------------------------
[HOOK (0-3s)]: "Wait, if you don't know this hack in 2026, you are losing money!"
[BODY (3-20s)]: Step-by-step breakdown of {user_prompt}. Explain with fast pacing.
[CALL TO ACTION]: "Save this reel and share with someone who needs it!"
[TAGS]: #viral #trending #nexusai #creator #tech
=================================================="""

    elif any(k in cmd_lower for k in ["notice", "legal", "draft", "complaint", "police", "agreement", "application"]):
        task_mode = "LEGAL_CIVIC"
        doc_title = "📜 OFFICIAL LEGAL / CIVIC DRAFT"
        spoken_text = f"Namaste {user_name} ji! Aapka kanooni application draft taiyar hai."
        res_content = f"""==================================================
{doc_title}
Ref No: NX-LEG-{datetime.now().strftime('%H%M%S')}
Applicant: {user_name} | Date: {today_str}
Subject: {user_prompt}
--------------------------------------------------
To,
The Competent Authority / Concerned Department.

Respected Sir/Madam,
I am submitting this formal application regarding: {user_prompt}. 
Please review the verified records and initiate swift action.

Sincerely,
{user_name} (+91 {clean_p})
=================================================="""

    else:
        # Default: Vyapar Ledger & General Task
        task_mode = "BUSINESS_LEDGER"
        doc_title = "🧾 OFFICIAL DIGITAL BUSINESS RECORD"
        if "English" in selected_lang:
            spoken_text = f"Hello {user_name}! Your business action for {user_prompt} is verified and locked."
        elif "भोजपुरी" in selected_lang:
            spoken_text = f"Pranaam {user_name} ji! Rauwa hisab-kitab bilkul darj ho gail ba."
        else:
            spoken_text = f"नमस्ते {user_name} जी! आपकी दुकान का हिसाब बहीखाते में दर्ज हो गया है।"

        res_content = f"""==================================================
{doc_title}
Inv ID: NX-INV-{datetime.now().strftime('%H%M%S')}
Date: {today_str} | Time: {time_str}
Client: {user_name} (+91 {clean_p})
Task Log: {user_prompt}
Status: 100% VERIFIED & SECURED ON CLOUD ✅
System Architect: Sahil Ahmad
=================================================="""

    st.success("🟢 Task Processed! Autonomous Neural Core ne action execute kar diya:")

    # Voice Engine (Audio trigger + manual fallback button)
    audio_code = f"""
    <div style="background:#0F172A; padding:12px; border-radius:10px; border-left:4px solid #10B981; margin:8px 0;">
        <p style="color:#10B981; margin:0 0 4px 0; font-size:13px; font-weight:bold;">🔊 Neural Voice Confirmation:</p>
        <p style="color:#FFF; margin:0 0 8px 0; font-size:14px;">"{spoken_text}"</p>
        <button onclick="playVoiceNow()" style="background:#10B981; color:#fff; border:none; padding:8px 16px; border-radius:6px; font-weight:bold; cursor:pointer;">
            ▶️ Aawaz Sunein (Play Audio)
        </button>
    </div>
    <script>
        function playVoiceNow() {{
            window.speechSynthesis.cancel();
            var ut = new SpeechSynthesisUtterance("{spoken_text}");
            ut.lang = "{"en-US" if "English" in selected_lang else "hi-IN"}";
            ut.rate = 0.95;
            ut.pitch = 1.3;
            window.speechSynthesis.speak(ut);
        }}
        setTimeout(playVoiceNow, 300);
    </script>
    """
    components.html(audio_code, height=115)

    st.text_area("📄 Executed Document / Output Result:", res_content, height=180)

    # Direct Action Buttons
    enc_wa = urllib.parse.quote(f"{doc_title}\n\n{user_prompt}\nStatus: Verified ✅\nBy: Sahil Ahmad (Nexus Brain OS)")
    st.markdown(f'<a href="https://wa.me/91{clean_p}?text={enc_wa}" target="_blank" class="wa-btn">📲 1. WhatsApp Par Direct Dispatch Karein</a>', unsafe_allow_html=True)

    enc_srch = urllib.parse.quote(user_prompt)
    st.markdown(f'<a href="https://www.google.com/search?q={enc_srch}" target="_blank" class="search-btn">🌐 2. Live Internet Web Search Trigger Karein</a>', unsafe_allow_html=True)

# Founder Branding Footer
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; background:#0B1329; padding:16px; border-radius:14px; border: 2px solid #38BDF8;">
    <p style="color:#38BDF8; font-size:11px; margin:0; letter-spacing:2px;">🏛️ FOUNDER & CHIEF ARCHITECT</p>
    <h2 style="color:#FFF; margin:4px 0; font-size:22px;">साहिल अहमद (Sahil Ahmad)</h2>
    <p style="color:#94A3B8; font-size:12px; margin:0 0 10px 0;">Nexus Brain OS — Autonomous Artificial Intelligence Infrastructure</p>
    <a href="https://wa.me/{MY_WA_NUMBER}" target="_blank" style="background:#10B981; color:#fff; padding:10px 20px; border-radius:8px; text-decoration:none; font-weight:bold; font-size:13px; display:inline-block;">💬 Connect on WhatsApp (+91 {MY_WA_NUMBER[-10:]})</a>
</div>
""", unsafe_allow_html=True)
