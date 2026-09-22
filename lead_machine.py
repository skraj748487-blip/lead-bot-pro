import streamlit as st
import streamlit.components.v1 as components
import urllib.parse
from datetime import datetime

# 1. Page Configuration
st.set_page_config(
    page_title="SEVA AI — डिजिटल सहायता केंद्र",
    page_icon="🇮🇳",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. High-Contrast Clear Dark CSS (No White Box Glitch)
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

    /* Fixed Input & Textarea Styling - No White Blanks */
    input, .stTextInput input, textarea, .stTextArea textarea {
        background-color: #0F172A !important;
        color: #38BDF8 !important;
        font-size: 16px !important;
        font-weight: 700 !important;
        border: 2px solid #38BDF8 !important;
        border-radius: 12px !important;
        padding: 12px !important;
    }
    input:focus, textarea:focus {
        border-color: #10B981 !important;
        box-shadow: 0 0 18px rgba(16, 185, 129, 0.4) !important;
    }

    div[data-baseweb="select"] > div {
        background-color: #0F172A !important;
        border: 2px solid #38BDF8 !important;
        color: #FFFFFF !important;
        border-radius: 12px !important;
        font-weight: 700 !important;
    }

    div.stButton > button, div.stDownloadButton > button {
        background: linear-gradient(135deg, #0284C7 0%, #2563EB 100%) !important;
        color: #FFFFFF !important;
        font-weight: 800 !important;
        font-size: 17px !important;
        border-radius: 12px !important;
        width: 100% !important;
        padding: 15px !important;
        border: 1px solid #38BDF8 !important;
        box-shadow: 0 4px 20px rgba(2, 132, 199, 0.4) !important;
        margin-top: 8px;
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
        margin: 10px 0;
        box-shadow: 0 4px 18px rgba(16, 185, 129, 0.4);
    }
</style>
""", unsafe_allow_html=True)

MY_WA_NUMBER = "917484878440"
today_str = datetime.now().strftime("%d-%m-%Y")

# Top Header
st.markdown("""
<div class="header-box">
    <div style="background:rgba(16,185,129,0.2); color:#10B981; border:1px solid #10B981; padding:4px 14px; border-radius:20px; font-size:12px; font-weight:800; display:inline-block; margin-bottom:8px;">
        🇮🇳 राष्ट्रीय नागरिक सहायता केंद्र
    </div>
    <h1 style="font-size:24px; margin:0; color:#FFF;">SEVA AI (सेवा एआई)</h1>
    <p style="font-size:13px; color:#94A3B8; margin:6px 0 0 0;">बैंक, ब्लॉक व थाने की कानूनी अर्ज़ी 5 सेकंड में तैयार करें</p>
</div>
""", unsafe_allow_html=True)

# Select Category
doc_type = st.selectbox(
    "📋 आपको किस प्रकार का प्रार्थना पत्र चाहिए?",
    [
        "बैंक खाता / एटीएम / पासबुक से संबंधित प्रार्थना पत्र",
        "ग्राम प्रधान / नगर निगम (सड़क, नाली, सफ़ाई) शिकायत पत्र",
        "राशन कार्ड नया / नाम जुड़वाने हेतु आवेदन",
        "थाना प्रभारी (पुलिस) को शिकायती प्रार्थना पत्र",
        "स्कूल / कॉलेज / ऑफिस में छुट्टी हेतु आवेदन पत्र"
    ]
)

u_name = st.text_input("👤 आपका पूरा नाम:", value="साहिल अहमद")
u_phone = st.text_input("📱 आपका WhatsApp नंबर:", value="7484878440")
u_details = st.text_area(
    "✍️ अपनी समस्या या विवरण यहाँ लिखें:",
    value="मेरी बैंक पासबुक खो गई है, मुझे नई पासबुक जारी करवाने के लिए शाखा प्रबंधक को प्रार्थना पत्र लिखना है।"
)

if st.button("⚡ आधिकारिक प्रार्थना पत्र तैयार करें"):
    clean_num = u_phone.strip() if u_phone.strip() else "7484878440"
    doc_ref = f"SEVA-{datetime.now().strftime('%d%H%M')}"

    # Official Letter Content
    full_letter = f"""सेवा में,
श्रीमान शाखा प्रबंधक महोदय / संबंधित सक्षम अधिकारी,
विषय: {doc_type} के संबंध में।

महोदय,
सविनय निवेदन है कि प्रार्थी {u_name}, निवासी का स्थायी नागरिक है।

मामले का पूर्ण विवरण:
{u_details}

अतः आपसे विनम्र प्रार्थना है कि उक्त विषय पर संज्ञान लेते हुए आवश्यक प्रशासनिक कार्रवाई करने की कृपा करें। इसके लिए प्रार्थी सदैव आपका आभारी रहेगा।

संलग्नक: पहचान पत्र (आधार कार्ड) एवं आवश्यक दस्तावेज प्रति
दिनांक: {today_str}
हस्ताक्षर प्रार्थी: ........................
नाम: {u_name}
मोबाइल: +91 {clean_num}
--------------------------------------------------
सत्यापित संदर्भ संख्या: {doc_ref}
डिजिटल इंफ्रास्ट्रक्चर: Seva AI Bharat
चीफ सिस्टम आर्किटेक्ट: साहिल अहमद (Sahil Ahmad)"""

    st.success("🟢 आधिकारिक प्रार्थना पत्र तैयार हो चुका है:")
    st.text_area("📄 तैयार आवेदन पत्र:", full_letter, height=240)

    # Direct Chrome Download Button
    st.download_button(
        label="📥 सीधे मोबाइल में डाउनलोड करें (Chrome Download)",
        data=full_letter.encode('utf-8'),
        file_name=f"Prarthana_Patra_{today_str}.txt",
        mime="text/plain"
    )

    # WhatsApp Push
    enc_share = urllib.parse.quote(f"SEVA AI OFFICIAL APPLICATION:\n\n{full_letter}")
    st.markdown(f'<a href="https://wa.me/91{clean_num}?text={enc_share}" target="_blank" class="btn-wa">📲 सीधे WhatsApp पर फ़ाइल भेजें</a>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; background: #0B1329; padding: 16px; border-radius: 14px; border: 2px solid #38BDF8;">
    <p style="color:#38BDF8; font-size:11px; margin:0; letter-spacing:2px;">🏛️ FOUNDER & CHIEF SYSTEM ARCHITECT</p>
    <h2 style="color:#FFF; margin:4px 0; font-size:22px;">साहिल अहमद (Sahil Ahmad)</h2>
    <p style="color:#94A3B8; font-size:12px; margin:0 0 10px 0;">Seva AI — Autonomous Citizen Legal Technology</p>
    <a href="https://wa.me/{MY_WA_NUMBER}" target="_blank" style="background:#10B981; color:#fff; padding:10px 20px; border-radius:8px; text-decoration:none; font-weight:bold; font-size:13px; display:inline-block;">💬 संपर्क सूत्र (+91 {MY_WA_NUMBER[-10:]})</a>
</div>
""", unsafe_allow_html=True)
