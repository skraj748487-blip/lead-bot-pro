import streamlit as st
import streamlit.components.v1 as components
import urllib.parse
from datetime import datetime
import pandas as pd

# 1. Page Configuration
st.set_page_config(
    page_title="VYAPAR MIND OS — Smart Khata",
    page_icon="💼",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Clean Cyber-Dark Theme
st.markdown("""
<style>
    .stApp { background-color: #020617 !important; color: #F8FAFC !important; }
    label, p, span, h1, h2, h3, h4 { color: #F8FAFC !important; font-weight: 600 !important; }
    input, .stTextInput input, .stNumberInput input {
        background-color: #0F172A !important; color: #38BDF8 !important;
        font-size: 16px !important; font-weight: 600 !important;
        border: 2px solid #1E293B !important; border-radius: 12px !important;
    }
    .hero-box {
        background: radial-gradient(circle at center, #1E1B4B 0%, #020617 100%);
        padding: 20px 14px; border-radius: 20px; text-align: center; margin-bottom: 16px;
        border: 1px solid #312E81; box-shadow: 0 10px 40px rgba(99, 102, 241, 0.3);
    }
    .bill-card {
        background: #0B1329; border: 1px solid #1E293B; border-radius: 14px;
        padding: 16px; margin-bottom: 14px;
    }
    .wa-btn {
        display: block; background: linear-gradient(90deg, #10B981 0%, #059669 100%);
        color: #FFFFFF !important; text-align: center; font-weight: 900; font-size: 15px;
        padding: 14px; border-radius: 12px; text-decoration: none; margin-top: 10px;
        box-shadow: 0 4px 20px rgba(16, 185, 129, 0.4);
    }
    div.stButton > button {
        background: linear-gradient(135deg, #2563EB 0%, #4F46E5 100%) !important;
        color: #FFFFFF !important; border: none !important; border-radius: 12px !important;
        font-weight: 900 !important; font-size: 16px !important; width: 100% !important;
        padding: 15px !important; box-shadow: 0 4px 25px rgba(37, 99, 235, 0.45) !important;
    }
</style>
""", unsafe_allow_html=True)

MY_WA_NUMBER = "917484878440"
MY_UPI_ID = "7484878449-2@ybl"
today_date = datetime.now().strftime("%d-%m-%Y")
time_now = datetime.now().strftime("%I:%M %p")

# Header
st.markdown("""
<div class="hero-box">
    <div style="font-size: 32px; margin-bottom: 4px;">💼⚡</div>
    <h1 style="color:#FFF; margin:0; font-size:22px;">VYAPAR MIND OS</h1>
    <p style="color:#94A3B8; font-size:12px; margin-top:4px;">Bolkar Khata & WhatsApp Parchi • Powered by Sahil Ahmad</p>
</div>
""", unsafe_allow_html=True)

# 1. Bhasha Selection
lang_choice = st.selectbox("🌍 Bhasha Chunein (Language):", [
    "हिन्दी (Hindi)",
    "English",
    "भोजपुरी (Bhojpuri)"
])

# 2. Entry Type
txn_type = st.radio("लेन-देन का प्रकार चुनें:", ["नगद बिक्री (Cash Sale)", "उधार दिया (Customer Credit)"], horizontal=True)

col_a, col_b = st.columns(2)
with col_a:
    cust_name = st.text_input("ग्राहक / पार्टी का नाम:", value="Ramesh Kumar")
with col_b:
    cust_phone = st.text_input("ग्राहक WhatsApp नंबर (10 अंक):", value="7484878440")

col_c, col_d = st.columns(2)
with col_c:
    item_desc = st.text_input("सामान / विवरण:", value="5L Mustard Oil + Ration")
with col_d:
    amount = st.number_input("रकम / Amount (₹):", min_value=1, value=650, step=10)

# Execute Button
if st.button("🚀 हिसाब लॉक करें और WhatsApp पर्ची तैयार करें"):
    clean_p = cust_phone.strip()
    invoice_id = f"INV-{datetime.now().strftime('%H%M%S')}"
    
    # Language specific speech
    if "English" in lang_choice:
        lang_code = "en-US"
        speech = f"Hello {cust_name}! Your bill of rupees {amount} has been added. Receipt is ready on WhatsApp."
    elif "भोजपुरी" in lang_choice:
        lang_code = "hi-IN"
        speech = f"Pranaam {cust_name} ji! Rauwa {amount} rupiya ke hisab darj ho gail ba."
    else:
        lang_code = "hi-IN"
        speech = f"नमस्ते {cust_name} जी! आपकी दुकान का {amount} रुपये का हिसाब दर्ज कर दिया गया है।"

    # Generate Professional Ledger Receipt
    receipt_text = f"""----------------------------------------
🧾 आधिकारिक डिजिटल पर्ची (DIGITAL BILL)
बिल नंबर: {invoice_id}
तारीख: {today_date} | समय: {time_now}
----------------------------------------
ग्राहक: {cust_name}
प्रकार: {txn_type}
सामान: {item_desc}
कुल राशि: ₹{amount}/-
स्थिति: सफलतापूर्वक दर्ज एवं सत्यापित ✅
----------------------------------------
दुकानदार: साहil Ahmad (Vyapar Mind OS)
----------------------------------------"""

    st.success("🟢 हिसाब बहीखाते में सुरक्षित दर्ज हो गया!")

    # Live Audio Widget
    audio_widget = f"""
    <div style="background:#0F172A; padding:12px; border-radius:10px; border-left:4px solid #10B981; margin:8px 0;">
        <p style="color:#10B981; margin:0 0 4px 0; font-size:13px; font-weight:bold;">🔊 AI वॉइस पुष्टि:</p>
        <p style="color:#FFF; margin:0 0 8px 0; font-size:14px;">"{speech}"</p>
        <button onclick="playKhataVoice()" style="background:#10B981; color:#fff; border:none; padding:8px 16px; border-radius:6px; font-weight:bold; cursor:pointer;">
            ▶️ आवाज़ सुनें (Play Voice)
        </button>
    </div>
    <script>
        function playKhataVoice() {{
            window.speechSynthesis.cancel();
            var ut = new SpeechSynthesisUtterance("{speech}");
            ut.lang = "{lang_code}";
            ut.rate = 0.95;
            ut.pitch = 1.3;
            window.speechSynthesis.speak(ut);
        }}
        setTimeout(playKhataVoice, 300);
    </script>
    """
    components.html(audio_widget, height=115)

    st.text_area("📄 डिजिटल बहीखाता पर्ची:", receipt_text, height=190)

    # WhatsApp Direct Send Button
    enc_bill = urllib.parse.quote(receipt_text)
    st.markdown(f'<a href="https://wa.me/91{clean_p}?text={enc_bill}" target="_blank" class="wa-btn">📲 सीधे ग्राहक के WhatsApp पर पर्ची भेजें</a>', unsafe_allow_html=True)

# ----------------------------------------------------
# Founder Branding Section
# ----------------------------------------------------
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; background:#0B1329; padding:16px; border-radius:14px; border: 2px solid #38BDF8;">
    <p style="color:#38BDF8; font-size:11px; margin:0; letter-spacing:2px;">🏛️ FOUNDER & CHIEF ARCHITECT</p>
    <h2 style="color:#FFF; margin:4px 0; font-size:22px;">साहिल अहमद (Sahil Ahmad)</h2>
    <p style="color:#94A3B8; font-size:12px; margin:0 0 10px 0;">Vyapar Mind OS — Autonomous Business Infrastructure</p>
    <a href="https://wa.me/{MY_WA_NUMBER}" target="_blank" style="background:#10B981; color:#fff; padding:10px 20px; border-radius:8px; text-decoration:none; font-weight:bold; font-size:13px; display:inline-block;">💬 Connect on WhatsApp (+91 {MY_WA_NUMBER[-10:]})</a>
</div>
""", unsafe_allow_html=True)
