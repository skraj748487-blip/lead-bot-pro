import streamlit as st
import streamlit.components.v1 as components
import urllib.parse
from datetime import datetime

# 1. Page Configuration
st.set_page_config(
    page_title="स्मार्ट बिज़नेस व बिलिंग ऐप — Sahil Ahmad",
    page_icon="📱",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Clean, Modern & High-Contrast Design
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Devanagari:wght@500;700;800&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap');

    .stApp {
        background-color: #0B1120 !important;
        color: #FFFFFF !important;
        font-family: 'Noto Sans Devanagari', 'Plus Jakarta Sans', sans-serif !important;
    }

    /* Headings & Text */
    h1, h2, h3, p, span, label, div {
        color: #FFFFFF !important;
        font-weight: 700 !important;
    }

    /* Top Clean Header */
    .top-badge {
        background: #1E293B;
        border: 1px solid #38BDF8;
        border-radius: 12px;
        padding: 10px 16px;
        text-align: center;
        margin-bottom: 16px;
    }

    /* Input Fields - Clear, Big & Bold */
    input, .stTextInput input, textarea, .stTextArea textarea {
        background-color: #0F172A !important;
        color: #38BDF8 !important;
        font-size: 16px !important;
        font-weight: 700 !important;
        border: 2px solid #334155 !important;
        border-radius: 10px !important;
        padding: 12px !important;
    }
    input:focus, textarea:focus {
        border-color: #38BDF8 !important;
        box-shadow: 0 0 15px rgba(56, 189, 248, 0.4) !important;
    }

    /* Big Main Action Button */
    div.stButton > button {
        background: linear-gradient(135deg, #0284C7 0%, #2563EB 100%) !important;
        color: #FFFFFF !important;
        font-weight: 800 !important;
        font-size: 18px !important;
        border-radius: 12px !important;
        width: 100% !important;
        padding: 16px !important;
        border: none !important;
        box-shadow: 0 4px 20px rgba(2, 132, 199, 0.5) !important;
        margin-top: 10px;
    }

    /* WhatsApp Button */
    .btn-wa {
        display: block;
        background: linear-gradient(90deg, #10B981 0%, #059669 100%);
        color: #FFFFFF !important;
        text-align: center;
        font-weight: 800;
        font-size: 16px;
        padding: 14px;
        border-radius: 10px;
        text-decoration: none;
        margin: 12px 0;
        box-shadow: 0 4px 15px rgba(16, 185, 129, 0.4);
    }

    /* Clean Card */
    .bill-card {
        background: #0F172A;
        border: 2px solid #38BDF8;
        border-radius: 14px;
        padding: 18px;
        margin-top: 14px;
    }
</style>
""", unsafe_allow_html=True)

MY_WA_NUMBER = "917484878440"
MY_UPI_ID = "7484878440@ybl"
today_str = datetime.now().strftime("%d-%m-%Y")
time_now = datetime.now().strftime("%I:%M %p")

# Language Selection
lang_mode = st.radio(
    "🌐 भाषा चुनें / Select Language:",
    ["🇮🇳 हिन्दी (Hindi)", "🇬🇧 English"],
    horizontal=True
)
is_hindi = "हिन्दी" in lang_mode

# App Header
if is_hindi:
    st.markdown("""
    <div class="top-badge">
        <h2 style="font-size:22px; margin:0; color:#38BDF8;">⚡ स्मार्ट डिजिटल बिलिंग व पेमेंट सिस्टम</h2>
        <p style="font-size:13px; color:#94A3B8; margin:4px 0 0 0;">दुकान, गैरेज, क्लिनिक और किसी भी बिज़नेस के लिए</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div class="top-badge">
        <h2 style="font-size:22px; margin:0; color:#38BDF8;">⚡ Smart Digital Billing & Pay System</h2>
        <p style="font-size:13px; color:#94A3B8; margin:4px 0 0 0;">For Shops, Garages, Clinics & All Businesses</p>
    </div>
    """, unsafe_allow_html=True)

# Form Section
st.write("---")

if is_hindi:
    shop_name = st.text_input("🏪 दुकान / बिज़नेस का नाम:", value="Ahmad Super Auto Center")
    col1, col2 = st.columns(2)
    with col1:
        cust_name = st.text_input("👤 ग्राहक का नाम:", value="रमेश कुमार")
    with col2:
        cust_phone = st.text_input("📱 ग्राहक का WhatsApp नंबर:", value="7484878440")
    
    item_desc = st.text_input("🔧 काम या सामान का विवरण:", value="कार सर्विसिंग + नया मोबिल आयल")
    bill_amt = st.text_input("💰 कुल बिल राशि (रुपये में):", value="2500")
    btn_label = "✅ 1-क्लिक में डिजिटल बिल व पर्ची तैयार करें"
else:
    shop_name = st.text_input("🏪 Store / Business Name:", value="Ahmad Super Auto Center")
    col1, col2 = st.columns(2)
    with col1:
        cust_name = st.text_input("👤 Customer Name:", value="Ramesh Kumar")
    with col2:
        cust_phone = st.text_input("📱 Customer WhatsApp Number:", value="7484878440")
    
    item_desc = st.text_input("🔧 Work or Product Details:", value="Full Car Servicing + Engine Oil")
    bill_amt = st.text_input("💰 Total Bill Amount (in ₹):", value="2500")
    btn_label = "✅ Generate Digital Bill & Receipt in 1-Click"

# Button Click
if st.button(btn_label):
    clean_phone = cust_phone.strip() if cust_phone.strip() else "7484878440"
    clean_amt = bill_amt.strip() if bill_amt.strip() else "0"
    bill_no = f"INV-{datetime.now().strftime('%d%H%M')}"

    if is_hindi:
        spoken_text = f"नमस्ते {cust_name} जी! {shop_name} की तरफ से आपका {clean_amt} रुपये का डिजिटल बिल तैयार है।"
        receipt_text = f"""==================================================
              डिजिटल रसीद एवं बिल
दुकान: {shop_name}
बिल नंबर: {bill_no} | दिनांक: {today_str} ({time_now})
--------------------------------------------------
ग्राहक का नाम: {cust_name}
WhatsApp नंबर: +91 {clean_phone}
काम/सामान का विवरण: {item_desc}
--------------------------------------------------
कुल भुगतान राशि: ₹{clean_amt}
भुगतान माध्यम: PhonePe / Google Pay / UPI ({MY_UPI_ID})
सॉफ्टवेयर आर्किटेक्ट: साहिल अहमद
=================================================="""
        wa_text = f"नमस्ते {cust_name} जी!\n\n*{shop_name}* की तरफ से आपका डिजिटल बिल तैयार है:\n\n📄 *बिल नंबर:* {bill_no}\n🔧 *विवरण:* {item_desc}\n💰 *कुल राशि:* ₹{clean_amt}\n\n💳 *ऑनलाइन पेमेंट करें (PhonePe/GPay UPI):* {MY_UPI_ID}\n\nधन्यवाद!"
    else:
        spoken_text = f"Hello {cust_name}! Your bill of rupees {clean_amt} from {shop_name} is ready."
        receipt_text = f"""==================================================
              DIGITAL BILL RECEIPT
Store: {shop_name}
Bill No: {bill_no} | Date: {today_str} ({time_now})
--------------------------------------------------
Customer: {cust_name}
WhatsApp: +91 {clean_phone}
Work/Item: {item_desc}
--------------------------------------------------
TOTAL AMOUNT: ₹{clean_amt}
Payment Mode: PhonePe / Google Pay / UPI ({MY_UPI_ID})
Software Architect: Sahil Ahmad
=================================================="""
        wa_text = f"Hello {cust_name}!\n\nYour digital bill from *{shop_name}* is ready:\n\n📄 *Bill No:* {bill_no}\n🔧 *Details:* {item_desc}\n💰 *Total Amount:* ₹{clean_amt}\n\n💳 *Pay via UPI:* {MY_UPI_ID}\n\nThank you!"

    st.success("🟢 " + ("बिल सफलतापूर्वक तैयार हो गया!" if is_hindi else "Digital Bill Generated Successfully!"))

    # Audio Confirmation
    audio_box = f"""
    <div style="background:#0F172A; padding:12px; border-radius:10px; border-left:4px solid #10B981; margin:10px 0;">
        <p style="color:#10B981; margin:0 0 4px 0; font-size:13px; font-weight:bold;">🔊 {"बोलकर पुष्टि (वॉयस):" if is_hindi else "Voice Confirmation:"}</p>
        <p style="color:#FFF; margin:0 0 8px 0; font-size:14px;">"{spoken_text}"</p>
        <button onclick="playVoice()" style="background:#10B981; color:#fff; border:none; padding:8px 16px; border-radius:6px; font-weight:bold; cursor:pointer;">
            ▶️ {"आवाज़ सुनें" if is_hindi else "Play Audio"}
        </button>
    </div>
    <script>
        function playVoice() {{
            window.speechSynthesis.cancel();
            var u = new SpeechSynthesisUtterance("{spoken_text}");
            u.lang = "{"hi-IN" if is_hindi else "en-US"}";
            u.rate = 0.95;
            window.speechSynthesis.speak(u);
        }}
        setTimeout(playVoice, 300);
    </script>
    """
    components.html(audio_box, height=115)

    # Receipt Box
    st.text_area("📋 " + ("तैयार डिजिटल रसीद:" if is_hindi else "Digital Receipt Card:"), receipt_text, height=200)

    # WhatsApp Button
    enc_wa = urllib.parse.quote(wa_text)
    wa_btn_label = "📲 सीधे ग्राहक के WhatsApp पर बिल भेजें" if is_hindi else "📲 Dispatch Bill to Customer's WhatsApp"
    st.markdown(f'<a href="https://wa.me/91{clean_phone}?text={enc_wa}" target="_blank" class="btn-wa">{wa_btn_label}</a>', unsafe_allow_html=True)

    # UPI QR Code
    upi_url = f"upi://pay?pa={MY_UPI_ID}&pn=Sahil%20Ahmad&am={clean_amt}&cu=INR"
    qr_img = f"https://api.qrserver.com/v1/create-qr-code/?size=180x180&data={urllib.parse.quote(upi_url)}"

    st.markdown(f"""
    <div style="background:#0F172A; border:2px solid #10B981; border-radius:12px; padding:16px; text-align:center; margin-top:14px;">
        <h3 style="color:#10B981; margin:0 0 6px 0; font-size:18px;">💳 {"PhonePe / Google Pay से पेमेंट करें" if is_hindi else "Pay via PhonePe / Google Pay / Paytm"}</h3>
        <p style="color:#94A3B8; font-size:13px; margin:0 0 10px 0;">{"ग्राहक इस QR कोड को स्कैन करके सीधे भुगतान कर सकता है:" if is_hindi else "Customer scans this to pay directly into your account:"}</p>
        <img src="{qr_img}" style="border: 3px solid #38BDF8; border-radius: 10px; margin:0 auto; display:block;" />
        <p style="color:#38BDF8; font-size:14px; margin-top:8px; font-weight:bold;">UPI ID: {MY_UPI_ID}</p>
        <p style="color:#10B981; font-size:16px; margin:2px 0 0 0; font-weight:bold;">{"कुल रकम:" if is_hindi else "Total Amount:"} ₹{clean_amt}</p>
    </div>
    """, unsafe_allow_html=True)

# Founder Branding Footer
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; background: #0F172A; padding: 16px; border-radius: 12px; border: 1px solid #38BDF8;">
    <p style="color:#38BDF8; font-size:11px; margin:0; letter-spacing:1px;">🏛️ सॉफ्टवेयर डेवलपर एवं सिस्टम आर्किटेक्ट</p>
    <h2 style="color:#FFF; margin:4px 0; font-size:20px;">साहिल अहमद (Sahil Ahmad)</h2>
    <p style="color:#94A3B8; font-size:12px; margin:0 0 10px 0;">अपनी दुकान या बिज़नेस के लिए ऐसा स्मार्ट बिलिंग सॉफ्टवेयर बनवाने हेतु संपर्क करें</p>
    <a href="https://wa.me/{MY_WA_NUMBER}" target="_blank" style="background:#0284C7; color:#fff; padding:8px 18px; border-radius:8px; text-decoration:none; font-weight:bold; font-size:13px; display:inline-block;">💬 WhatsApp पर बात करें (+91 {MY_WA_NUMBER[-10:]})</a>
</div>
""", unsafe_allow_html=True)
