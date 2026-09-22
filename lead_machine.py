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

# 2. High-Contrast Crystal Clear Styling (Dark & Bright Text)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@600;700;800&family=Space+Grotesk:wght@600;700&display=swap');

    .stApp {
        background-color: #030712 !important;
        color: #FFFFFF !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }

    /* Clear High-Contrast Labels */
    label, p, span, h1, h2, h3, h4, div {
        color: #FFFFFF !important;
        font-weight: 700 !important;
    }

    /* Top HUD */
    .hud-top {
        display: flex; justify-content: space-between; align-items: center;
        border: 1px solid #38BDF8;
        padding: 12px 18px; margin-bottom: 20px;
        background: #0B1329;
        font-family: 'Space Grotesk', monospace; font-size: 12px; letter-spacing: 1.5px;
        border-radius: 12px; box-shadow: 0 0 20px rgba(56, 189, 248, 0.25);
    }

    /* Crystal Clear Inputs */
    input, .stTextInput input, textarea, .stTextArea textarea {
        background-color: #0F172A !important;
        color: #38BDF8 !important;
        font-size: 16px !important;
        font-weight: 800 !important;
        border: 2px solid #38BDF8 !important;
        border-radius: 12px !important;
        padding: 12px !important;
    }
    input:focus, textarea:focus {
        border-color: #10B981 !important;
        box-shadow: 0 0 20px rgba(16, 185, 129, 0.5) !important;
    }

    /* Select Dropdown */
    div[data-baseweb="select"] > div {
        background-color: #0F172A !important;
        border: 2px solid #38BDF8 !important;
        color: #FFFFFF !important;
        border-radius: 12px !important;
        font-weight: 800 !important;
    }

    /* Buttons */
    div.stButton > button {
        background: linear-gradient(135deg, #2563EB 0%, #4F46E5 100%) !important;
        color: #FFFFFF !important;
        font-weight: 900 !important;
        font-size: 17px !important;
        border-radius: 12px !important;
        width: 100% !important;
        padding: 16px !important;
        border: 1px solid #38BDF8 !important;
        box-shadow: 0 4px 25px rgba(37, 99, 235, 0.5) !important;
    }

    .btn-deal {
        display: block;
        background: linear-gradient(90deg, #10B981 0%, #059669 100%);
        color: #FFFFFF !important;
        text-align: center;
        font-weight: 900;
        font-size: 16px;
        padding: 15px;
        border-radius: 12px;
        text-decoration: none;
        margin: 10px 0;
        box-shadow: 0 4px 20px rgba(16, 185, 129, 0.4);
    }

    .qr-card {
        background: #0B1329;
        border: 2px solid #10B981;
        border-radius: 14px;
        padding: 18px;
        text-align: center;
        margin-top: 15px;
        box-shadow: 0 0 25px rgba(16, 185, 129, 0.25);
    }
</style>
""", unsafe_allow_html=True)

MY_WA_NUMBER = "917484878440"
UPI_ID = "7484878440@ybl"
today_str = datetime.now().strftime("%d-%m-%Y")
time_now = datetime.now().strftime("%I:%M %p")

# Top Metrics HUD
st.markdown(f"""
<div class="hud-top">
    <div>🚀 SYSTEM: <span style="color:#10B981;">100% ACTIVE</span></div>
    <div>ARCHITECT: <span style="color:#FFF;">SAHIL AHMAD</span></div>
    <div>NODE: <span style="color:#38BDF8;">SECURE CLOUD</span></div>
</div>
""", unsafe_allow_html=True)

# 1. Bhasha Chunein (Language Toggle)
lang_mode = st.radio(
    "🌐 अपनी पसंदीदा भाषा चुनें / Choose Language:",
    ["🇮🇳 हिन्दी (Hindi)", "🇬🇧 English (Global)"],
    horizontal=True
)
is_hindi = "हिन्दी" in lang_mode

# Header Title Card
if is_hindi:
    st.markdown("""
    <div style="text-align:center; padding: 18px 10px; margin-bottom: 20px; background: #0B1329; border: 2px solid #38BDF8; border-radius: 16px;">
        <span style="background:rgba(16,185,129,0.2); color:#10B981; border:1px solid #10B981; padding:4px 14px; border-radius:20px; font-size:12px; font-weight:800;">लाखों की कमाई वाला बिज़नेस सिस्टम</span>
        <h1 style="font-size:24px; color:#FFF; margin:8px 0 0 0;">APEX SOVEREIGN AI</h1>
        <p style="color:#38BDF8; font-size:13px; margin:4px 0 0 0;">क्लाइंट ऑटोमेशन • डायरेक्ट बिलिंग • तुरंत पेमेंट वसूली</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div style="text-align:center; padding: 18px 10px; margin-bottom: 20px; background: #0B1329; border: 2px solid #38BDF8; border-radius: 16px;">
        <span style="background:rgba(16,185,129,0.2); color:#10B981; border:1px solid #10B981; padding:4px 14px; border-radius:20px; font-size:12px; font-weight:800;">HIGH-TICKET REVENUE ARCHITECTURE</span>
        <h1 style="font-size:24px; color:#FFF; margin:8px 0 0 0;">APEX SOVEREIGN AI</h1>
        <p style="color:#38BDF8; font-size:13px; margin:4px 0 0 0;">Client Acquisition • Instant Deals • Automated WhatsApp Pay</p>
    </div>
    """, unsafe_allow_html=True)

# Form Fields based on Language
if is_hindi:
    c_name = st.text_input("🏢 बिज़नेस या दुकान का नाम:", value="Ahmad Super Auto Center")
    service_options = [
        "AI ऑटोमेशन और सॉफ़्टवेयर सेटअप (₹25,000 पैकेज)",
        "मासिक डिजिटल मेंटेनेंस व ग्रोथ (₹10,000 प्रति माह)",
        "कस्टमर केयर व ऑटो-WhatsApp सिस्टम (₹15,000 पैकेज)",
        "कंप्लीट एंटरप्राइज इंफ्रास्ट्रक्चर (₹50,000 पैकेज)"
    ]
    c_service = st.selectbox("💼 डील या सर्विस पैकेज चुनें:", service_options)
    c_client = st.text_input("👤 ग्राहक का नाम (Client Name):", value="रमेश कुमार")
    c_phone = st.text_input("📱 ग्राहक का WhatsApp नंबर (10 अंक):", value="7484878440")
    btn_text = "⚡ 1-क्लिक में प्रपोजल तैयार करें और डील लॉक करें"
else:
    c_name = st.text_input("🏢 Business or Store Name:", value="Ahmad Super Auto Center")
    service_options = [
        "Full AI Automation & Software Setup (₹25,000 Package)",
        "Monthly Digital Growth & Maintenance (₹10,000 / Month)",
        "Customer Care & Auto-WhatsApp Protocol (₹15,000 Package)",
        "Complete Enterprise Infrastructure (₹50,000 Package)"
    ]
    c_service = st.selectbox("💼 Select Deal / Service Package:", service_options)
    c_client = st.text_input("👤 Client / Party Name:", value="Ramesh Kumar")
    c_phone = st.text_input("📱 Client WhatsApp Number (10 Digits):", value="7484878440")
    btn_text = "⚡ GENERATE DEAL PROPOSAL & LOCK IN 1-CLICK"

# Action Execution
if st.button(btn_text):
    clean_p = c_phone.strip() if c_phone.strip() else "7484878440"
    deal_code = f"NX-{datetime.now().strftime('%d%H%M')}"
    
    # Amount parsing
    amt = "₹25,000"
    amt_num = "25000"
    if "10,000" in c_service: 
        amt = "₹10,000"
        amt_num = "10000"
    elif "15,000" in c_service: 
        amt = "₹15,000"
        amt_num = "15000"
    elif "50,000" in c_service: 
        amt = "₹50,000"
        amt_num = "50000"

    if is_hindi:
        spoken_line = f"नमस्ते {c_client} जी! {c_name} की तरफ से आपका {amt} का आधिकारिक बिजनेस प्रपोजल और पेमेंट लिंक तैयार है।"
        doc_header = "आधिकारिक बिजनेस प्रपोजल व इनवॉइस"
        doc_content = f"""==================================================
{doc_header}
डील आईडी: {deal_code} | दिनांक: {today_str} | समय: {time_now}
--------------------------------------------------
जारीकर्ता: {c_name}
चीफ टेक्नोलॉजी आर्किटेक्ट: साहिल अहमद (Apex AI)
क्लाइंट का नाम: {c_client} (+91 {clean_p})

अनुबंध विवरण:
• सर्विस पैकेज: {c_service}
• कुल निवेश राशि: {amt}
• सिस्टम स्टेटस: 100% सत्यापित एवं क्लाउड लॉक ✅
• भुगतान माध्यम: PhonePe / Google Pay / UPI ({UPI_ID})
=================================================="""
        wa_msg = f"नमस्ते {c_client} जी!\n\n{c_name} द्वारा आपका बिजनेस डील प्रपोजल तैयार है।\n\n📌 सर्विस: {c_service}\n💰 कुल रकम: {amt}\n\n💳 UPI Payment ID: {UPI_ID}\n\nचीफ आर्किटेक्ट: साहिल अहमद"
    else:
        spoken_line = f"Hello {c_client}! Your official executive deal proposal of {amt} from {c_name} is locked and ready."
        doc_header = "OFFICIAL EXECUTIVE DEAL PROPOSAL & INVOICE"
        doc_content = f"""==================================================
{doc_header}
DEAL ID: {deal_code} | DATE: {today_str} | TIME: {time_now}
--------------------------------------------------
ISSUER: {c_name}
CHIEF TECHNOLOGY ARCHITECT: SAHIL AHMAD (Apex AI)
CLIENT: {c_client} (+91 {clean_p})

CONTRACT DETAILS:
• Service Scope: {c_service}
• Investment Amount: {amt}
• System Status: 100% VERIFIED & CLOUD SECURED ✅
• Settlement Protocol: PhonePe / Google Pay / UPI ({UPI_ID})
=================================================="""
        wa_msg = f"Hello {c_client}!\n\nYour official deal proposal from {c_name} is ready.\n\n📌 Service: {c_service}\n💰 Investment: {amt}\n\n💳 UPI Payment ID: {UPI_ID}\n\nChief Architect: Sahil Ahmad"

    st.success("🟢 " + ("सत्यापित प्रपोजल तैयार हो गया है:" if is_hindi else "Verified Deal Proposal Locked:"))

    # High Quality Voice Engine
    voice_html = f"""
    <div style="background:#0F172A; padding:14px; border-radius:12px; border-left:5px solid #10B981; margin:10px 0;">
        <p style="color:#10B981; margin:0 0 6px 0; font-size:13px; font-weight:bold;">🔊 {"AI वॉइस पुष्टि:" if is_hindi else "AI Vocal Confirmation:"}</p>
        <p style="color:#FFF; margin:0 0 10px 0; font-size:14px; font-weight:bold;">"{spoken_line}"</p>
        <button onclick="playVoiceNow()" style="background:#10B981; color:#fff; border:none; padding:10px 20px; border-radius:8px; font-weight:bold; cursor:pointer; font-size:13px;">
            ▶️ {"आवाज़ सुनें (Play Voice)" if is_hindi else "Play Vocal Output"}
        </button>
    </div>
    <script>
        function playVoiceNow() {{
            window.speechSynthesis.cancel();
            var u = new SpeechSynthesisUtterance("{spoken_line}");
            u.lang = "{"hi-IN" if is_hindi else "en-US"}";
            u.rate = 0.95;
            window.speechSynthesis.speak(u);
        }}
        setTimeout(playVoiceNow, 300);
    </script>
    """
    components.html(voice_html, height=125)

    # Document Box with Bright Neon Styling
    st.text_area("📄 " + ("आधिकारिक दस्तावेज रिकॉर्ड:" if is_hindi else "Official Executed Document:"), doc_content, height=200)

    # WhatsApp Push
    enc_wa = urllib.parse.quote(wa_msg)
    wa_label = "📲 1. WhatsApp पर प्रपोजल व पेमेंट लिंक भेजें" if is_hindi else "📲 1. Dispatch Proposal & Payment on WhatsApp"
    st.markdown(f'<a href="https://wa.me/91{clean_p}?text={enc_wa}" target="_blank" class="btn-deal">{wa_label}</a>', unsafe_allow_html=True)

    # Direct UPI Payment QR Code
    upi_pay_link = f"upi://pay?pa={UPI_ID}&pn=Sahil%20Ahmad&am={amt_num}&cu=INR"
    qr_img_url = f"https://api.qrserver.com/v1/create-qr-code/?size=180x180&data={urllib.parse.quote(upi_pay_link)}"
    
    st.markdown(f"""
    <div class="qr-card">
        <h3 style="color:#10B981; margin:0 0 8px 0; font-size:18px;">💳 {"तुरंत पेमेंट स्कैन करें (PhonePe / Google Pay / Paytm)" if is_hindi else "Instant Payment QR Code (PhonePe / GPay)"}</h3>
        <p style="color:#94A3B8; font-size:13px; margin:0 0 12px 0;">{"क्लाइंट यह QR कोड स्कैन करके सीधे आपके बैंक खाते में पैसे भेज सकता है:" if is_hindi else "Client scans to pay directly into your bank account:"}</p>
        <img src="{qr_img_url}" style="border: 4px solid #38BDF8; border-radius: 12px; margin: 0 auto; display: block;" />
        <p style="color:#38BDF8; font-size:15px; margin-top:10px; font-weight:800;">UPI ID: {UPI_ID}</p>
        <p style="color:#10B981; font-size:16px; margin:4px 0 0 0; font-weight:900;">{"रकम:" if is_hindi else "Amount:"} {amt}</p>
    </div>
    """, unsafe_allow_html=True)

# Founder Status Footer
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; background: #0B1329; padding: 18px; border-radius: 14px; border: 2px solid #38BDF8; box-shadow: 0 0 30px rgba(56, 189, 248, 0.25);">
    <p style="color:#38BDF8; font-family:'Space Grotesk', monospace; font-size:11px; margin:0; letter-spacing:2px;">🏛️ CHIEF TECHNOLOGY ARCHITECT</p>
    <h2 style="color:#FFF; margin:4px 0; font-size:22px;">साहिल अहमद (Sahil Ahmad)</h2>
    <p style="color:#94A3B8; font-size:13px; margin:0 0 12px 0;">Apex AI Sovereign Infrastructure • Direct Business Closures</p>
    <a href="https://wa.me/{MY_WA_NUMBER}" target="_blank" style="background:#10B981; color:#fff; padding:10px 22px; border-radius:8px; text-decoration:none; font-weight:bold; font-size:13px; display:inline-block;">💬 Connect on WhatsApp (+91 {MY_WA_NUMBER[-10:]})</a>
</div>
""", unsafe_allow_html=True)
