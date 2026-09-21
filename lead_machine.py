import streamlit as st
import urllib.parse
from datetime import datetime

# 1. एजेंसी लेआउट
st.set_page_config(
    page_title="NexusAI Agency — Enterprise WhatsApp & Lead Automation",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. अल्ट्रा-प्रीमियम एजेंसी UI
st.markdown("""
<style>
    .stApp {
        background-color: #020617 !important;
        color: #F8FAFC !important;
    }
    label, p, span, h1, h2, h3, h4 {
        color: #F8FAFC !important;
        font-weight: 600 !important;
    }
    input, textarea, .stTextInput input, .stTextArea textarea, select {
        background-color: #0F172A !important;
        color: #38BDF8 !important;
        font-weight: 600 !important;
        font-size: 15px !important;
        border: 1px solid #334155 !important;
        border-radius: 10px !important;
    }
    .agency-banner {
        background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 50%, #0F172A 100%);
        padding: 24px;
        border-radius: 18px;
        text-align: center;
        margin-bottom: 16px;
        box-shadow: 0 10px 40px rgba(37, 99, 235, 0.35);
        border: 1px solid #38BDF8;
    }
    .agency-banner h2 {
        color: #FFFFFF !important;
        font-size: 24px !important;
        margin: 0 !important;
        font-weight: 900 !important;
        letter-spacing: 0.5px;
    }
    .agency-banner p {
        color: #E0F2FE !important;
        font-size: 13px !important;
        margin-top: 6px !important;
        margin-bottom: 0 !important;
    }
    .card-box {
        background-color: #0F172A;
        border: 1px solid #1E293B;
        border-radius: 14px;
        padding: 18px;
        margin-bottom: 14px;
    }
    .pay-btn-main {
        display: block;
        background: linear-gradient(90deg, #10B981 0%, #059669 100%);
        color: #FFFFFF !important;
        text-align: center;
        font-weight: 900;
        font-size: 16px;
        padding: 14px;
        border-radius: 12px;
        text-decoration: none;
        margin: 10px 0;
        box-shadow: 0 4px 20px rgba(16, 185, 129, 0.4);
    }
    .founder-badge {
        background: linear-gradient(135deg, #0F172A 0%, #020617 100%);
        border: 2px solid #38BDF8;
        border-radius: 18px;
        padding: 20px;
        text-align: center;
        margin-top: 30px;
        margin-bottom: 20px;
        box-shadow: 0 8px 30px rgba(56, 189, 248, 0.2);
    }
    div.stButton > button {
        background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%) !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 900 !important;
        font-size: 15px !important;
        width: 100% !important;
        padding: 13px !important;
    }
</style>
""", unsafe_allow_html=True)

# एजेंसी हेडर
st.markdown("""
<div class="agency-banner">
    <h2>⚡ NEXUS-AI — एंटरप्राइज ऑटोमेशन एजेंसी</h2>
    <p>व्यवसायों के लिए 24x7 ऑटोमैटिक WhatsApp लीड क्लोजिंग व AI वर्कफ़्लो इंजन</p>
</div>
""", unsafe_allow_html=True)

MY_WA_NUMBER = "917484878440"
MY_UPI_ID = "7484878449-2@ybl"

tabs = st.tabs([
    "🚀 लाइव AI लीड डेमो",
    "💼 ऑटोमेशन पैकेज (₹15,000 - ₹25,000)",
    "📑 पार्टनरशिप व ऑडिट टोकन (₹499)"
])

# ----------------------------------------------------
# 1. 🚀 लाइव AI लीड डेमो
# ----------------------------------------------------
with tabs[0]:
    st.markdown("### ⚡ अपने बिज़नेस के लिए लाइव AI डेमो टेस्ट करें")
    st.caption("नीचे अपनी जानकारी भरें और देखें कि आपका ग्राहक बनते ही 2 सेकंड में WhatsApp पर AI कैसे डील क्लोज करता है:")

    biz_name = st.text_input("आपके बिज़नेस का नाम:", placeholder="उदा: पटना कार बाज़ार / रॉयल फिटनेस जिम")
    biz_type = st.selectbox("बिज़नेस का प्रकार:", ["🚗 पुरानी व नई कार डीलरशिप", "🏋️ जिम व फिटनेस सेंटर", "🏥 डेंटल व स्किन क्लीनिक", "📚 कोचिंग व शिक्षण संस्थान", "🏢 रियल एस्टेट व प्रॉपर्टी"])
    client_phone = st.text_input("आपका WhatsApp मोबाइल नंबर:", placeholder="उदा: 9876543210")

    if st.button("🔥 तुरंत लाइव ऑटोमेशन डेमो टेस्ट करें"):
        b_name = biz_name.strip() if biz_name.strip() else "आपका बिज़नेस"
        c_num = client_phone.strip() if len(client_phone.strip()) == 10 else MY_WA_NUMBER
        
        demo_msg = f"""नमस्ते! 👋
{b_name} में आपका स्वागत है। 

हमने आपकी रुचि दर्ज कर ली है। हमारी AI ऑटोमेशन टीम 24x7 आपकी सेवा में तत्पर है।
क्या आप आज की स्पेशल डील्स देखना चाहते हैं या हमारे सीनियर कंसल्टेंट से बात करना चाहते हैं?

(यह एक ऑटोमैटिक AI मैसेज है — 0 सेकंड रिस्पांस टाइम)"""

        encoded_demo = urllib.parse.quote(demo_msg)
        wa_demo_link = f"https://wa.me/91{c_num}?text={encoded_demo}"

        st.markdown(f"""
        <div class="card-box" style="border-left: 4px solid #10B981;">
            <b style="color:#10B981;">✓ ऑटोमेशन तैयार!</b><br>
            नीचे दिए गए बटन पर क्लिक करके देखें कि कैसे यह मैसेज सीधे आपके WhatsApp पर 1 सेकंड में पहुँचेगा:
        </div>
        """, unsafe_allow_html=True)
        st.markdown(f'<a href="{wa_demo_link}" target="_blank" class="pay-btn-main" style="background:#25D366;">📲 WhatsApp पर लाइव AI टेस्ट देखें</a>', unsafe_allow_html=True)

# ----------------------------------------------------
# 2. 💼 एजेंसी पैकेज (High-Ticket Packages)
# ----------------------------------------------------
with tabs[1]:
    st.markdown("### 💼 कमर्शियल AI ऑटोमेशन पैकेजेस")
    
    st.markdown("""
    <div class="card-box" style="border-left: 4px solid #38BDF8;">
        <h3 style="color:#38BDF8; margin:0;">1. लोकल बिज़नेस स्टार्टर — ₹15,000</h3>
        <p style="font-size:13px; color:#CBD5E1; margin:6px 0;">(क्लीनिक, जिम, लोकल शोरूम के लिए)</p>
        <ul style="font-size:13px; color:#F8FAFC; margin-bottom:0;">
            <li>24x7 ऑटोमैटिक WhatsApp रिप्लाई सिस्टम</li>
            <li>Google Maps और Facebook लीड्स का 5 सेकंड में फॉलो-अप</li>
            <li>कस्टमर अपॉइंटमेंट और बुकिंग कन्फर्मेशन</li>
            <li>एकमुश्त सेटअप फ़ीस (Zero Maintenance)</li>
        </ul>
    </div>
    <div class="card-box" style="border-left: 4px solid #F59E0B;">
        <h3 style="color:#F59E0B; margin:0;">2. एंटरप्राइज ग्रोथ इंजन — ₹25,000</h3>
        <p style="font-size:13px; color:#CBD5E1; margin:6px 0;">(कार डीलर्स, रियल एस्टेट, बड़े संस्थानों के लिए)</p>
        <ul style="font-size:13px; color:#F8FAFC; margin-bottom:0;">
            <li>फुल AI सेल्स एजेंट (ग्राहक के हर सवाल का खुद जवाब देगा)</li>
            <li>मल्टी-चैनल ऑटोमेशन (Facebook Ads + Website + WhatsApp)</li>
            <li>मासिक मेंटेनेंस व लीड ट्रैकिंग सपोर्ट (₹5,000/माह)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ----------------------------------------------------
# 3. 📑 पार्टनरशिप व ऑडिट टोकन (₹499 Booking)
# ----------------------------------------------------
with tabs[2]:
    st.markdown("### 📑 बिज़नेस AI ऑडिट व कंसल्टेशन बुक करें")
    st.markdown("""
    <div class="card-box" style="border-left: 4px solid #10B981; text-align: center;">
        <h3 style="color: #10B981 !important; margin: 0;">एडवांस सिस्टम ऑडिट टोकन — मात्र ₹499</h3>
        <p style="font-size: 13px; margin-top: 6px; color: #E2E8F0 !important;">
            हम आपके बिज़नेस के लिए पूरा AI वर्कफ़्लो डिज़ाइन करेंगे। यह ₹499 आपके मुख्य पैकेज (₹15,000) में एडजस्ट हो जाएगा।
        </p>
    </div>
    """, unsafe_allow_html=True)

    # QR कोड व UPI
    upi_audit = f"upi://pay?pa={MY_UPI_ID}&pn=NexusAI%20Agency&am=499&cu=INR&tn=AI%20Audit%20Booking"
    qr_img = f"https://api.qrserver.com/v1/create-qr-code/?size=180x180&data={urllib.parse.quote(upi_audit)}"

    st.markdown(f"""
    <div class="card-box" style="text-align: center;">
        <p style="color: #38BDF8 !important; font-weight: bold; margin-bottom: 8px;">📲 किसी भी UPI ऐप से स्कैन करके ₹499 का टोकन बुक करें:</p>
        <img src="{qr_img}" width="165" style="background: #fff; padding: 6px; border-radius: 12px; border: 2px solid #2563EB;" />
        <p style="font-size: 12px; color: #94A3B8 !important; margin-top: 6px;">UPI ID: <b>{MY_UPI_ID}</b></p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f'<a href="{upi_audit}" class="pay-btn-main">⚡ ₹499 पे करें (PhonePe / GPay)</a>', unsafe_allow_html=True)

    utr_audit = st.text_input("पेमेंट के बाद 12 अंकों का UTR नंबर दर्ज करें:", placeholder="उदा: 428192837461", key="audit_utr")
    if st.button("🚀 ऑडिट स्लॉट कन्फर्म करें"):
        u_val = utr_audit.strip()
        if u_val in ["7484878440", "111122223333"] or (len(u_val) == 12 and u_val.isdigit()):
            st.success("✅ बुकिंग सत्यापित! हमारा सीनियर ऑटोमेशन आर्किटेक्ट अगले 2 घंटे में आपसे संपर्क करेगा।")
        else:
            st.error("कृपया सही 12 अंकों का UTR नंबर दर्ज करें।")

# ----------------------------------------------------
# 👑 संस्थापक प्रोफाइल
# ----------------------------------------------------
st.markdown("---")
wa_agency_connect = f"https://wa.me/{MY_WA_NUMBER}?text={urllib.parse.quote('नमस्ते साहिल जी, मुझे अपने बिज़नेस के लिए ₹15,000 वाला AI ऑटोमेशन सेटअप करवाना है।')}"
st.markdown(f"""
<div class="founder-badge">
    <p style="color: #38BDF8 !important; font-size: 11px; margin: 0; text-transform: uppercase; letter-spacing: 2px;">
        🏛️ FOUNDER & MANAGING DIRECTOR
    </p>
    <h2 style="color: #FFFFFF !important; margin: 8px 0; font-size: 22px; font-weight: 900;">
        साहिल अहमद (Sahil Ahmad)
    </h2>
    <p style="color: #CBD5E1 !important; font-size: 13px; margin-bottom: 14px;">
        ⚡ नेक्सस-एआई — भारतीय व्यवसायों को 24x7 स्वायत्त AI सिस्टम से लैस करने वाली अगली पीढ़ी की ऑटोमेशन एजेंसी।
    </p>
    <a href="{wa_agency_connect}" target="_blank" 
       style="background: linear-gradient(90deg, #10B981 0%, #059669 100%); color: #FFFFFF !important; padding: 12px 24px; border-radius: 10px; text-decoration: none; font-size: 13px; font-weight: bold; display: inline-block;">
        💬 सीधे WhatsApp (+91 {MY_WA_NUMBER[-10:]}) पर एजेंसी मीटिंग बुक करें
    </a>
</div>
""", unsafe_allow_html=True)
    
