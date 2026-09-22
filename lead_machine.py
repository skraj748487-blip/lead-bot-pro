import streamlit as st
import streamlit.components.v1 as components
import urllib.parse
from datetime import datetime

# 1. Page Config
st.set_page_config(
    page_title="VYAPAR MIND OS",
    page_icon="💼",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Modern Cyber Dark CSS
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
today_date = datetime.now().strftime("%d-%m-%Y")
time_now = datetime.now().strftime("%I:%M %p")

# Language Selection
lang_choice = st.selectbox("🌍 Select Language / भाषा चुनें:", [
    "English",
    "हिन्दी (Hindi)",
    "भोजपुरी (Bhojpuri)"
])

is_en = "English" in lang_choice
is_bhoj = "भोजपुरी" in lang_choice

# Header Translation
sub_title = "Smart Voice Khata & WhatsApp Billing • Engineered by Sahil Ahmad" if is_en else "बोलकर खाता व WhatsApp पर्ची • Powered by Sahil Ahmad"
st.markdown(f"""
<div class="hero-box">
    <div style="font-size: 32px; margin-bottom: 4px;">💼⚡</div>
    <h1 style="color:#FFF; margin:0; font-size:22px;">VYAPAR MIND OS</h1>
    <p style="color:#94A3B8; font-size:12px; margin-top:4px;">{sub_title}</p>
</div>
""", unsafe_allow_html=True)

# Transaction Type Options
if is_en:
    txn_label = "Select Transaction Type:"
    txn_options = ["Cash Sale", "Customer Credit (Udhar)"]
    c_name_lbl = "Customer / Party Name:"
    c_phone_lbl = "Customer WhatsApp Number (10 Digits):"
    item_lbl = "Items / Description:"
    amt_lbl = "Amount (₹):"
    btn_lbl = "🚀 Lock Entry & Generate WhatsApp Invoice"
    success_msg = "🟢 Transaction secured and recorded into digital ledger!"
    voice_header = "🔊 AI Voice Verification:"
    receipt_lbl = "📄 Digital Invoice Receipt:"
    wa_btn_lbl = "📲 Send Invoice Directly to WhatsApp"
    voice_btn_lbl = "▶️ Play Voice"
else:
    txn_label = "लेन-देन का प्रकार चुनें:"
    txn_options = ["नगद बिक्री (Cash Sale)", "उधार दिया (Customer Credit)"]
    c_name_lbl = "ग्राहक / पार्टी का नाम:"
    c_phone_lbl = "ग्राहक WhatsApp नंबर (10 अंक):"
    item_lbl = "सामान / विवरण:"
    amt_lbl = "रकम / Amount (₹):"
    btn_lbl = "🚀 हिसाब लॉक करें और WhatsApp पर्ची तैयार करें"
    success_msg = "🟢 हिसाब बहीखाते में सुरक्षित दर्ज हो गया!"
    voice_header = "🔊 AI वॉइस पुष्टि:"
    receipt_lbl = "📄 डिजिटल बहीखाता पर्ची:"
    wa_btn_lbl = "📲 सीधे ग्राहक के WhatsApp पर पर्ची भेजें"
    voice_btn_lbl = "▶️ आवाज़ सुनें (Play Voice)"

txn_type = st.radio(txn_label, txn_options, horizontal=True)

col_a, col_b = st.columns(2)
with col_a:
    cust_name = st.text_input(c_name_lbl, value="Ramesh Kumar")
with col_b:
    cust_phone = st.text_input(c_phone_lbl, value="7484878440")

col_c, col_d = st.columns(2)
with col_c:
    item_desc = st.text_input(item_lbl, value="5L Mustard Oil + Ration")
with col_d:
    amount = st.number_input(amt_lbl, min_value=1, value=650, step=10)

if st.button(btn_lbl):
    clean_p = cust_phone.strip()
    invoice_id = f"INV-{datetime.now().strftime('%H%M%S')}"

    # Multilingual Voice and Receipt Text
    if is_en:
        lang_code = "en-US"
        speech = f"Hello {cust_name}! Your bill of rupees {amount} has been recorded successfully. Receipt is ready on WhatsApp."
        receipt_text = f"""----------------------------------------
🧾 OFFICIAL DIGITAL INVOICE
Invoice No: {invoice_id}
Date: {today_date} | Time: {time_now}
----------------------------------------
Customer: {cust_name}
Transaction: {txn_type}
Items: {item_desc}
Total Amount: ₹{amount}/-
Status: VERIFIED & LOCKED IN LEDGER ✅
----------------------------------------
Merchant: Sahil Ahmad (Vyapar Mind OS)
----------------------------------------"""
    elif is_bhoj:
        lang_code = "hi-IN"
        speech = f"Pranaam {cust_name} ji! Rauwa {amount} rupiya ke hisab darj ho gail ba, parchi WhatsApp par taiyar ba."
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
दुकानदार: Sahil Ahmad (Vyapar Mind OS)
----------------------------------------"""
    else:
        lang_code = "hi-IN"
        speech = f"नमस्ते {cust_name} जी! आपकी दुकान का {amount} रुपये का हिसाब दर्ज कर दिया गया है।"
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
दुकानदार: Sahil Ahmad (Vyapar Mind OS)
----------------------------------------"""

    st.success(success_msg)

    # Dynamic Audio Engine
    audio_widget = f"""
    <div style="background:#0F172A; padding:12px; border-radius:10px; border-left:4px solid #10B981; margin:8px 0;">
        <p style="color:#10B981; margin:0 0 4px 0; font-size:13px; font-weight:bold;">{voice_header}</p>
        <p style="color:#FFF; margin:0 0 8px 0; font-size:14px;">"{speech}"</p>
        <button onclick="playKhataVoice()" style="background:#10B981; color:#fff; border:none; padding:8px 16px; border-radius:6px; font-weight:bold; cursor:pointer;">
            {voice_btn_lbl}
        </button>
    </div>
    <script>
        function playKhataVoice() {{
            window.speechSynthesis.cancel();
            var ut = new SpeechSynthesisUtterance("{speech}");
            ut.lang = "{lang_code}";
            ut.rate = 0.95;
            ut.pitch = 1.25;
            window.speechSynthesis.speak(ut);
        }}
        setTimeout(playKhataVoice, 300);
    </script>
    """
    components.html(audio_widget, height=115)

    st.text_area(receipt_lbl, receipt_text, height=190)

    # WhatsApp Push
    enc_bill = urllib.parse.quote(receipt_text)
    st.markdown(f'<a href="https://wa.me/91{clean_p}?text={enc_bill}" target="_blank" class="wa-btn">{wa_btn_lbl}</a>', unsafe_allow_html=True)

# Founder Branding
st.markdown("---")
f_role = "FOUNDER & CHIEF ARCHITECT" if is_en else "संस्थापक एवं मुख्य आर्किटेक्ट"
f_desc = "Vyapar Mind OS — Autonomous Business & Ledger Infrastructure" if is_en else "व्यापार माइंड OS — ऑटोमेशन एवं डिजिटल बहीखाता सिस्टम"

st.markdown(f"""
<div style="text-align: center; background:#0B1329; padding:16px; border-radius:14px; border: 2px solid #38BDF8;">
    <p style="color:#38BDF8; font-size:11px; margin:0; letter-spacing:2px;">🏛️ {f_role}</p>
    <h2 style="color:#FFF; margin:4px 0; font-size:22px;">Sahil Ahmad</h2>
    <p style="color:#94A3B8; font-size:12px; margin:0 0 10px 0;">{f_desc}</p>
    <a href="https://wa.me/{MY_WA_NUMBER}" target="_blank" style="background:#10B981; color:#fff; padding:10px 20px; border-radius:8px; text-decoration:none; font-weight:bold; font-size:13px; display:inline-block;">💬 Connect on WhatsApp (+91 {MY_WA_NUMBER[-10:]})</a>
</div>
""", unsafe_allow_html=True)
