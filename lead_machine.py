import streamlit as st
import streamlit.components.v1 as components
import urllib.parse
from datetime import datetime

# 1. Page Configuration
st.set_page_config(
    page_title="SEVA AI — भारत का डिजिटल सहायता केंद्र",
    page_icon="🇮🇳",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Devanagari:wght@600;700;800&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap');

    .stApp {
        background-color: #060D1A !important;
        color: #FFFFFF !important;
        font-family: 'Noto Sans Devanagari', 'Plus Jakarta Sans', sans-serif !important;
    }
    h1, h2, h3, p, span, label, div {
        color: #FFFFFF !important;
        font-weight: 700 !important;
    }
    .header-box {
        background: radial-gradient(circle at center, #1E3A8A 0%, #060D1A 100%);
        border: 2px solid #38BDF8;
        border-radius: 16px;
        padding: 20px 14px;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 8px 30px rgba(56, 189, 248, 0.25);
    }
    .badge-national {
        background: rgba(16, 185, 129, 0.2);
        color: #10B981;
        border: 1px solid #10B981;
        padding: 4px 14px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 800;
        display: inline-block;
        margin-bottom: 8px;
    }
    input, .stTextInput input, textarea, .stTextArea textarea {
        background-color: #0F172A !important;
        color: #38BDF8 !important;
        font-size: 16px !important;
        font-weight: 700 !important;
        border: 2px solid #334155 !important;
        border-radius: 12px !important;
        padding: 12px !important;
    }
    input:focus, textarea:focus {
        border-color: #38BDF8 !important;
        box-shadow: 0 0 18px rgba(56, 189, 248, 0.4) !important;
    }
    div.stButton > button {
        background: linear-gradient(135deg, #0284C7 0%, #2563EB 100%) !important;
        color: #FFFFFF !important;
        font-weight: 800 !important;
        font-size: 18px !important;
        border-radius: 12px !important;
        width: 100% !important;
        padding: 16px !important;
        border: 1px solid #38BDF8 !important;
        box-shadow: 0 4px 25px rgba(2, 132, 199, 0.4) !important;
        margin-top: 10px;
    }
    .btn-wa {
        display: block;
        background: linear-gradient(90deg, #10B981 0%, #059669 100%);
        color: #FFFFFF !important;
        text-align: center;
        font-weight: 800;
        font-size: 16px;
        padding: 14px;
        border-radius: 12px;
        text-decoration: none;
        margin: 12px 0;
        box-shadow: 0 4px 18px rgba(16, 185, 129, 0.4);
    }
    .lock-card {
        background: #3B0764;
        border: 2px solid #C084FC;
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        margin-top: 20px;
        box-shadow: 0 0 30px rgba(192, 132, 252, 0.3);
    }
</style>
""", unsafe_allow_html=True)

MY_WA_NUMBER = "917484878440"
MY_UPI_ID = "7484878440@ybl"
today_str = datetime.now().strftime("%d-%m-%Y")

if "doc_count" not in st.session_state:
    st.session_state.doc_count = 0
if "is_subscribed" not in st.session_state:
    st.session_state.is_subscribed = False

st.markdown("""
<div class="header-box">
    <div class="badge-national">🇮🇳 राष्ट्रीय डिजिटल नागरिक सहायता केंद्र</div>
    <h1 style="font-size:24px; margin:0; color:#FFF;">SEVA AI (सेवा एआई)</h1>
    <p style="font-size:13px; color:#94A3B8; margin:6px 0 0 0;">बैंक, ब्लॉक व सरकारी अर्ज़ी 5 सेकंड में तैयार करें और प्रिंट लें</p>
</div>
""", unsafe_allow_html=True)

lang_choice = st.radio(
    "🌐 भाषा चुनें / Select Language:",
    ["🇮🇳 हिन्दी (Hindi)", "🇬🇧 English"],
    horizontal=True
)
is_hindi = "हिन्दी" in lang_choice

# Paywall Logic after 1 Free Document
if st.session_state.doc_count >= 1 and not st.session_state.is_subscribed:
    st.markdown(f"""
    <div class="lock-card">
        <h2 style="color:#F3E8FF; margin:0 0 8px 0;">🎉 आपका मुफ़्त दस्तावेज़ तैयार हो चुका है!</h2>
        <p style="color:#E9D5FF; font-size:14px; margin:0 0 14px 0;">
            साइबर कैफ़े में ₹150 खर्च करने के बजाय, मात्र ₹9 में अगला दस्तावेज़ बनाएँ या महीने का अनलिमिटेड पास लें।
        </p>
        <div style="background:rgba(255,255,255,0.1); padding:12px; border-radius:10px; margin-bottom:14px;">
            <p style="color:#FFF; font-size:16px; margin:0;">💰 सिंगल डाउनलोड पास: <b>₹9</b> | मासिक अनलिमिटेड पास: <b>₹49</b></p>
        </div>
        <p style="color:#C084FC; font-size:13px;">PhonePe / Google Pay UPI ID:</p>
        <p style="color:#FFF; font-size:18px; font-weight:800; margin:2px 0 14px 0;">{MY_UPI_ID}</p>
        <a href="https://wa.me/{MY_WA_NUMBER}?text=Maine%20Seva%20AI%20par%20payment%20kar%20diya%20hai,%20kripya%20unlock%20karein" target="_blank" class="btn-wa">
            📲 पेमेंट स्क्रीनशॉट भेजें और तुरंत अनलॉक करें
        </a>
    </div>
    """, unsafe_allow_html=True)

    st.write("---")
    admin_pin = st.text_input("🔑 आर्किटेक्ट अनलॉक पिन (केवल साहिल अहमद हेतु):", type="password")
    if st.button("🔓 वीआईपी पास सक्रिय करें (Unlock Access)"):
        if admin_pin == "7484":
            st.session_state.is_subscribed = True
            st.success("असीमित वीआईपी पास सक्रिय कर दिया गया है!")
            st.rerun()
        else:
            st.error("गलत पिन!")

else:
    st.write("---")
    if is_hindi:
        doc_type = st.selectbox(
            "📋 आपको किस प्रकार का प्रार्थना पत्र / दस्तावेज़ चाहिए?",
            [
                "बैंक खाता / एटीएम / पासबुक से संबंधित प्रार्थना पत्र",
                "ग्राम प्रधान / नगर निगम (सड़क, नाली, सफाई) शिकायत पत्र",
                "राशन कार्ड नया / नाम जुड़वाने हेतु आवेदन",
                "थाना प्रभारी (पुलिस) को शिकायती प्रार्थना पत्र",
                "स्कूल / कॉलेज / ऑफिस में छुट्टी हेतु आवेदन पत्र"
            ]
        )
        u_name = st.text_input("👤 आपका पूरा नाम:", value="साहिल अहमद")
        u_phone = st.text_input("📱 आपका WhatsApp नंबर:", value="7484878440")
        u_details = st.text_area(
            "✍️ अपनी समस्या यहाँ लिखें (या बोलकर टाइप करें):",
            value="मेरी बैंक पासबुक खो गई है, मुझे नई पासबुक जारी करवाने के लिए शाखा प्रबंधक को प्रार्थना पत्र लिखना है।"
        )
        btn_action = "⚡ आधिकारिक प्रार्थना पत्र व PDF तैयार करें"
    else:
        doc_type = st.selectbox(
            "📋 Select Application / Document Category:",
            [
                "Bank Application (Passbook/ATM/Account issue)",
                "Municipal / Village Head Public Complaint",
                "Ration Card Application / Correction",
                "Police Station Formal Complaint Letter",
                "Leave Application for School/College/Office"
            ]
        )
        u_name = st.text_input("👤 Your Full Name:", value="Sahil Ahmad")
        u_phone = st.text_input("📱 Your WhatsApp Number:", value="7484878440")
        u_details = st.text_area(
            "✍️ Describe Your Need / Issue:",
            value="My passbook is lost, I need a formal letter to Branch Manager to reissue a new passbook."
        )
        btn_action = "⚡ Generate Formal Letter & PDF"

    if st.button(btn_action):
        st.session_state.doc_count += 1
        clean_num = u_phone.strip() if u_phone.strip() else "7484878440"
        doc_ref = f"SEVA-{datetime.now().strftime('%d%H%M')}"

        full_letter = f"""सेवा में,
श्रीमान शाखा प्रबंधक महोदय / संबंधित सक्षम अधिकारी,
विषय: {doc_type} के संबंध में।

महोदय,
सविनय निवेदन है कि प्रार्थी {u_name}, निवासी का स्थायी नागरिक है। 

विवरण:
{u_details}

अतः आपसे विनम्र प्रार्थना है कि उक्त विषय पर संज्ञान लेते हुए आवश्यक कार्रवाई करने की कृपा करें। इसके लिए प्रार्थी सदैव आपका आभारी रहेगा।

संलग्नक: आधार कार्ड एवं आवश्यक दस्तावेज
दिनांक: {today_str}
हस्ताक्षर प्रार्थी: ........................
नाम: {u_name}
मोबाइल: +91 {clean_num}
--------------------------------------------------
सत्यापित संदर्भ संख्या: {doc_ref}
डिजिटल इंफ्रास्ट्रक्चर: Seva AI Bharat
चीफ आर्किटेक्ट: साहिल अहमद (Sahil Ahmad)"""

        st.success("🟢 आधिकारिक प्रार्थना पत्र तैयार हो चुका है:")

        st.text_area("📄 तैयार आवेदन पत्र (प्रिंट हेतु):", full_letter, height=220)

        # 1-Click Print & PDF HTML Component
        print_component = f"""
        <div style="text-align:center; margin: 12px 0;">
            <button onclick="window.print()" style="background: linear-gradient(90deg, #0284C7, #2563EB); color: #fff; font-size: 16px; font-weight: bold; border: none; padding: 12px 24px; border-radius: 10px; cursor: pointer; box-shadow: 0 4px 15px rgba(2, 132, 199, 0.4);">
                🖨️ प्रिंट करें / PDF डाउनलोड करें (Save as PDF)
            </button>
        </div>
        """
        components.html(print_component, height=70)

        # WhatsApp Direct Send
        enc_share = urllib.parse.quote(f"SEVA AI OFFICIAL APPLICATION:\n\n{full_letter}")
        st.markdown(f'<a href="https://wa.me/91{clean_num}?text={enc_share}" target="_blank" class="btn-wa">📲 WhatsApp पर आवेदन प्राप्त करें</a>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; background: #0B1329; padding: 18px; border-radius: 14px; border: 2px solid #38BDF8;">
    <p style="color:#38BDF8; font-size:11px; margin:0; letter-spacing:2px;">🏛️ FOUNDER & CHIEF SYSTEM ARCHITECT</p>
    <h2 style="color:#FFF; margin:4px 0; font-size:22px;">साहिल अहमद (Sahil Ahmad)</h2>
    <p style="color:#94A3B8; font-size:12px; margin:0 0 10px 0;">Seva AI — Building Autonomous Citizen Technology for Bharat</p>
    <a href="https://wa.me/{MY_WA_NUMBER}" target="_blank" style="background:#10B981; color:#fff; padding:10px 20px; border-radius:8px; text-decoration:none; font-weight:bold; font-size:13px; display:inline-block;">💬 संपर्क सूत्र (+91 {MY_WA_NUMBER[-10:]})</a>
</div>
""", unsafe_allow_html=True)
