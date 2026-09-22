import streamlit as st
import streamlit.components.v1 as components
import urllib.parse
from datetime import datetime

# 1. Page Configuration
st.set_page_config(
    page_title="APEX AI — Sovereign Business Engine",
    page_icon="💼",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Luxury Dark Executive CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;700;800&family=Space+Grotesk:wght@600;700&display=swap');

    .stApp {
        background-color: #030712 !important;
        color: #F9FAFB !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }
    .hud-top {
        display: flex; justify-content: space-between; align-items: center;
        border: 1px solid rgba(56, 189, 248, 0.2);
        padding: 10px 16px; margin-bottom: 20px;
        background: rgba(17, 24, 39, 0.8); backdrop-filter: blur(10px);
        font-family: 'Space Grotesk', monospace; font-size: 11px; letter-spacing: 1.5px;
        color: #38BDF8; border-radius: 12px;
    }
    .revenue-card {
        text-align: center; padding: 22px 14px; margin-bottom: 20px;
        background: radial-gradient(circle at center, #1E1B4B 0%, #030712 100%);
        border-radius: 20px; border: 1px solid #3730A3;
        box-shadow: 0 10px 35px rgba(99, 102, 241, 0.25);
    }
    .revenue-badge {
        display: inline-block; background: rgba(16, 185, 129, 0.15);
        color: #10B981; border: 1px solid #10B981; padding: 4px 12px;
        border-radius: 20px; font-size: 11px; font-weight: 800; margin-bottom: 10px;
    }
    input, .stTextInput input, textarea, .stTextArea textarea {
        background-color: #111827 !important; color: #38BDF8 !important;
        font-size: 15px !important; font-weight: 600 !important;
        border: 1.5px solid #1F2937 !important; border-radius: 12px !important;
    }
    input:focus, textarea:focus {
        border-color: #38BDF8 !important; box-shadow: 0 0 15px rgba(56, 189, 248, 0.3) !important;
    }
    .btn-deal {
        display: block; background: linear-gradient(90deg, #10B981 0%, #059669 100%);
        color: #FFFFFF !important; text-align: center; font-weight: 800; font-size: 15px;
        padding: 14px; border-radius: 12px; text-decoration: none; margin: 10px 0;
        box-shadow: 0 4px 20px rgba(16, 185, 129, 0.4);
    }
    div.stButton > button {
        background: linear-gradient(135deg, #2563EB 0%, #4F46E5 100%) !important;
        color: #FFFFFF !important; font-weight: 800 !important; font-size: 16px !important;
        border-radius: 12px !important; width: 100% !important; padding: 15px !important;
        border: none !important; box-shadow: 0 4px 25px rgba(37, 99, 235, 0.4) !important;
    }
</style>
""", unsafe_allow_html=True)

MY_WA_NUMBER = "917484878440"
today_str = datetime.now().strftime("%d-%m-%Y")
time_now = datetime.now().strftime("%I:%M %p")

# Top Metrics HUD
st.markdown(f"""
<div class="hud-top">
    <div>🚀 ENGINE: <span style="color:#10B981;">ENTERPRISE ACTIVE</span></div>
    <div>ARCHITECT: <span style="color:#FFF;">SAHIL AHMAD</span></div>
    <div>SYSTEM NODE: <span>2026 CLOUD</span></div>
</div>
""", unsafe_allow_html=True)

# Main Title Card
st.markdown("""
<div class="revenue-card">
    <div class="revenue-badge">HIGH-TICKET REVENUE ARCHITECTURE</div>
    <h1 style="font-size:24px; color:#FFF; margin:0;">APEX SOVEREIGN OS</h1>
    <p style="color:#94A3B8; font-size:13px; margin-top:6px;">High-Conversion Client Acquisition & Digital Deal Closing Engine</p>
</div>
""", unsafe_allow_html=True)

# Business Form Inputs
c_name = st.text_input("🏢 बिज़नेस / क्लाइंट का नाम:", value="Ahmad Super Auto Center")
c_service = st.selectbox("💼 सर्विस / डील का प्रकार चुनें:", [
    "AI ऑटोमेशन और सॉफ्टवेयर सेटअप (₹25,000 पैकेज)",
    "मासिक डिजिटल ग्रोथ और मेंटेनेंस (₹10,000/माह)",
    "कस्टमर केयर और ऑटो-व्हाट्सएप सिस्टम (₹15,000 पैकेज)",
    "कंप्लीट एंटरप्राइज इंफ्रास्ट्रक्चर (₹50,000 पैकेज)"
])
c_client = st.text_input("👤 ग्राहक का नाम (Lead Name):", value="Ramesh Kumar")
c_phone = st.text_input("📱 ग्राहक का WhatsApp नंबर (10 अंक):", value="7484878440")

if st.button("⚡ GENERATE HIGH-TICKET DEAL & CLOSE (प्रपोजल तैयार करें)"):
    clean_p = c_phone.strip() if c_phone.strip() else "7484878440"
    deal_code = f"DL-{datetime.now().strftime('%d%H%M')}"
    
    # Extract Amount
    amt = "₹25,000"
    if "10,000" in c_service: amt = "₹10,000"
    elif "15,000" in c_service: amt = "₹15,000"
    elif "50,000" in c_service: amt = "₹50,000"

    spoken_line = f"नमस्ते {c_client} जी! {c_name} की तरफ से आपका बिजनेस ऑटोमेशन प्रपोजल और पेमेंट लिंक तैयार कर दिया गया है।"

    proposal_doc = f"""==================================================
OFFICIAL EXECUTIVE DEAL PROPOSAL
डील आईडी: {deal_code} | दिनांक: {today_str}
--------------------------------------------------
जारीकर्ता: {c_name}
अधिकृत आर्किटेक्ट: साहिल अहमद (Apex Sovereign OS)
क्लाइंट का नाम: {c_client} (+91 {clean_p})

अनुबंध विवरण:
• सर्विस: {c_service}
• कुल निवेश राशि: {amt}
• डिलीवरी समय: 24 से 48 घंटे में लाइव
• सपोर्ट: 24x7 ऑटोमेशन एवं मेंटेनेंस

भुगतान स्थिति: लंबित (Pending Verification)
=================================================="""

    st.success("🟢 प्रीमियम बिजनेस प्रपोजल सफलतापूर्वक लॉक हो गया:")

    # Voice Engine Output
    voice_html = f"""
    <div style="background:#111827; padding:12px; border-radius:10px; border-left:4px solid #10B981; margin:8px 0;">
        <p style="color:#10B981; margin:0 0 4px 0; font-size:12px; font-weight:bold;">🔊 एआई वॉइस कन्फर्मेशन:</p>
        <p style="color:#FFF; margin:0 0 8px 0; font-size:13px;">"{spoken_line}"</p>
        <button onclick="playVoice()" style="background:#10B981; color:#fff; border:none; padding:8px 14px; border-radius:6px; font-weight:bold; cursor:pointer; font-size:12px;">
            ▶️ वॉयस सुनें
        </button>
    </div>
    <script>
        function playVoice() {{
            window.speechSynthesis.cancel();
            var u = new SpeechSynthesisUtterance("{spoken_line}");
            u.lang = "hi-IN";
            u.rate = 0.95;
            window.speechSynthesis.speak(u);
        }}
        setTimeout(playVoice, 300);
    </script>
    """
    components.html(voice_html, height=115)

    st.text_area("📄 एग्जीक्यूटिव बिज़नेस रिकॉर्ड:", proposal_doc, height=180)

    # High-Converting WhatsApp Dispatch
    wa_msg = f"नमस्ते {c_client} जी!\n\n{c_name} द्वारा आपका बिजनेस डील प्रपोजल तैयार कर दिया गया है।\n\n📌 सर्विस: {c_service}\n💰 राशि: {amt}\n\nकृपया नीचे दिए गए सुरक्षित लिंक से कन्फर्म करें।\n\nचीफ आर्किटेक्ट: साहिल अहमद"
    enc_wa = urllib.parse.quote(wa_msg)
    st.markdown(f'<a href="https://wa.me/91{clean_p}?text={enc_wa}" target="_blank" class="btn-deal">📲 1-Click WhatsApp Deal Dispatch & Payment Link</a>', unsafe_allow_html=True)

# Executive Founder Card
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; background: #111827; padding: 18px; border-radius: 14px; border: 2px solid #38BDF8;">
    <p style="color:#38BDF8; font-family:'Space Grotesk', monospace; font-size:11px; margin:0; letter-spacing:2px;">🏛️ CHIEF TECHNOLOGY ARCHITECT</p>
    <h2 style="color:#FFF; margin:4px 0; font-size:22px;">साहिल अहमद (Sahil Ahmad)</h2>
    <p style="color:#94A3B8; font-size:12px; margin:0 0 10px 0;">Sovereign AI Infrastructure • Enterprise Automation</p>
    <a href="https://wa.me/{MY_WA_NUMBER}" target="_blank" style="background:#10B981; color:#fff; padding:10px 20px; border-radius:8px; text-decoration:none; font-weight:bold; font-size:13px; display:inline-block;">💬 Book Enterprise Deployment (+91 {MY_WA_NUMBER[-10:]})</a>
</div>
""", unsafe_allow_html=True)
