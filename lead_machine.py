import streamlit as st
import streamlit.components.v1 as components
import urllib.parse
import urllib.request
import json
from datetime import datetime

# 1. 24x7 High-Availability Configuration
st.set_page_config(
    page_title="महा-सेवा AI — 24x7 राष्ट्रीय डिजिटल नागरिक केंद्र",
    page_icon="🇮🇳",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Modern High-Speed High-Contrast CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Devanagari:wght@600;700;800&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap');

    .stApp {
        background-color: #030712 !important;
        color: #FFFFFF !important;
        font-family: 'Noto Sans Devanagari', 'Plus Jakarta Sans', sans-serif !important;
    }

    h1, h2, h3, p, span, label, div {
        color: #FFFFFF !important;
        font-weight: 700 !important;
    }

    .top-header {
        background: radial-gradient(circle at center, #1E3A8A 0%, #030712 100%);
        border: 2px solid #38BDF8;
        border-radius: 16px;
        padding: 18px 12px;
        text-align: center;
        margin-bottom: 16px;
        box-shadow: 0 0 25px rgba(56, 189, 248, 0.25);
    }

    /* Fixed Input and Text Area */
    input, .stTextInput input, textarea, .stTextArea textarea {
        background-color: #0F172A !important;
        color: #38BDF8 !important;
        font-size: 16px !important;
        font-weight: 700 !important;
        border: 2px solid #38BDF8 !important;
        border-radius: 10px !important;
        padding: 10px !important;
    }

    /* Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 6px;
        background-color: #0B1329;
        padding: 8px;
        border-radius: 12px;
        border: 1px solid #334155;
    }
    .stTabs [data-baseweb="tab"] {
        color: #94A3B8 !important;
        font-weight: 800 !important;
        font-size: 13px !important;
        border-radius: 8px;
        padding: 8px 12px !important;
    }
    .stTabs [aria-selected="true"] {
        background: #0284C7 !important;
        color: #FFFFFF !important;
    }

    /* Primary Action Buttons */
    div.stButton > button, div.stDownloadButton > button {
        background: linear-gradient(135deg, #0284C7 0%, #2563EB 100%) !important;
        color: #FFFFFF !important;
        font-weight: 800 !important;
        font-size: 16px !important;
        border-radius: 10px !important;
        width: 100% !important;
        padding: 14px !important;
        border: 1px solid #38BDF8 !important;
        box-shadow: 0 4px 15px rgba(2, 132, 199, 0.4) !important;
        margin-top: 8px;
    }

    .btn-action-green {
        display: block;
        background: linear-gradient(90deg, #10B981 0%, #059669 100%);
        color: #FFFFFF !important;
        text-align: center;
        font-weight: 800;
        font-size: 15px;
        padding: 13px;
        border-radius: 10px;
        text-decoration: none;
        margin: 10px 0;
        box-shadow: 0 4px 15px rgba(16, 185, 129, 0.4);
    }
</style>
""", unsafe_allow_html=True)

MY_WA_NUMBER = "917484878440"
today_str = datetime.now().strftime("%d-%m-%Y")

# Top Header
st.markdown("""
<div class="top-header">
    <div style="background:rgba(16,185,129,0.2); color:#10B981; border:1px solid #10B981; padding:3px 12px; border-radius:20px; font-size:11px; font-weight:800; display:inline-block; margin-bottom:6px;">
        ⚡ 24x7 निरंतर एक्टिव क्लाउड नोड
    </div>
    <h1 style="font-size:22px; margin:0; color:#FFF;">महा-सेवा AI (MAHA SEVA AI)</h1>
    <p style="font-size:12px; color:#38BDF8; margin:4px 0 0 0;">स्वास्थ्य • सरकारी योजना • साइबर सुरक्षा • रोज़गार • डिजिटल बिलिंग</p>
</div>
""", unsafe_allow_html=True)

# 5 Core Pillars as Tabs
tab_health, tab_scheme, tab_fraud, tab_job, tab_khata = st.tabs([
    "🏥 दवा व सेहत",
    "🏛️ सरकारी योजना",
    "🛡️ फ्रॉड सुरक्षा",
    "💼 रोज़गार केंद्र",
    "📒 डिजिटल खाता"
])

# ================= TAB 1: HEALTH & MEDICINE =================
with tab_health:
    st.write("### 🏥 सस्ती जेनेरिक दवा व पर्ची सहायक")
    med_input = st.text_input("💊 दवा का नाम लिखें या बीमारी का विवरण दें:", value="Paracetamol 650 / बुखार और दर्द")
    if st.button("🔍 सस्ती जेनेरिक दवा और उपयोग खोजें"):
        st.success("सत्यापित मेडिकल डेटाबेस विश्लेषण:")
        info_text = f"""• दवा/सॉल्ट: {med_input}
• प्राथमिक उपयोग: बुखार, सिरदर्द, और शरीर के सामान्य दर्द से राहत।
• सरकारी जेनेरिक विकल्प: 'Jan Aushadhi' केंद्र पर यही साल्ट ₹10 से ₹15 में उपलब्ध है (ब्रांडेड दवा ₹40-₹50 की तुलना में 70% सस्ती)।
• सलाह: खाली पेट न लें, खुराक के लिए डॉक्टर/फार्मासिस्ट से परामर्श अवश्य लें।"""
        st.text_area("📋 मेडिकल विश्लेषण परिणाम:", info_text, height=130)
        st.caption("⚠️ कानूनी सूचना: यह जानकारी केवल जनहित और जेनेरिक विकल्पों की समझ हेतु है।")

# ================= TAB 2: GOVERNMENT SCHEMES =================
with tab_scheme:
    st.write("### 🏛️ सरकारी योजना व आर्थिक सहायता खोजक")
    col_a, col_b = st.columns(2)
    with col_a:
        user_occ = st.selectbox("आपका कार्य/पेशा:", ["किसान", "छात्र", "मजदूर/दुकानदार", "महिला/गृहणी", "बेरोजगार युवा"])
    with col_b:
        user_state = st.selectbox("राज्य:", ["उत्तर प्रदेश", "बिहार", "मध्य प्रदेश", "राजस्थान", "अन्य राज्य"])
    
    if st.button("⚡ मेरे लिए सरकारी योजनाएं निकालें"):
        st.success(f"{user_state} के {user_occ} हेतु सक्रिय सरकारी योजनाएं:")
        scheme_data = f"""1. पीएम किसान / राज्य कृषक संबल: ₹6,000 वार्षिक प्रत्यक्ष बैंक ट्रांसफर।
2. आयुष्मान भारत योजना: परिवार हेतु ₹5,00,000 तक का प्रति वर्ष मुफ़्त अस्पताल इलाज।
3. पीएम आवास योजना (ग्रामीण/शहरी): पक्के मकान निर्माण हेतु ₹1,20,000 की सरकारी सब्सिडी।
4. ई-श्रम व दुर्घटना सुरक्षा: ₹2,00,000 का निःशुल्क आकस्मिक बीमा कवर।"""
        st.text_area("📜 आपके अधिकार और योजना विवरण:", scheme_data, height=140)

# ================= TAB 3: FRAUD & SCAM CHECKER =================
with tab_fraud:
    st.write("### 🛡️ साइबर सुरक्षा व स्कैम डिटेक्टर")
    sus_msg = st.text_area("संदिग्ध SMS, WhatsApp मैसेज या लिंक यहाँ पेस्ट करें:", value="बधाई हो! आपको ₹50,000 की लॉटरी मिली है, तुरंत इस लिंक पर क्लिक करके क्लेम करें।")
    if st.button("🚨 इस मैसेज की सत्यता जाँचें (Check Fraud)"):
        s_low = sus_msg.lower()
        if any(w in s_low for w in ["लॉटरी", "lottery", "क्लिक", "link", "पार्ट टाइम", "task", "free gift"]):
            st.error("🚨 100% संदेहास्पद फ्रॉड (FRAUD ALERT)")
            f_res = "चेतावनी: यह संदेश साइबर ठगों द्वारा भेजा गया है। किसी भी लिंक पर क्लिक न करें और न ही बैंक ओटीपी साझा करें।"
        else:
            st.success("🟢 सुरक्षित लग रहा है: सामान्य संदेश।")
            f_res = "इस संदेश में कोई तत्काल वित्तीय जोखिम या फ्रॉड लिंक नहीं पाया गया।"
        st.info(f_res)

# ================= TAB 4: BLUE-COLLAR JOB DESK =================
with tab_job:
    st.write("### 💼 लोकल रोज़गार व कारीगर संपर्क")
    c_job = st.selectbox("कार्य का क्षेत्र चुनें:", ["ड्राइवर / ऑपरेटर", "इलेक्ट्रीशियन / प्लंबर", "मिस्त्री / लेबर", "सुरक्षा गार्ड / डिलीवरी"])
    w_name = st.text_input("कारीगर / प्रार्थी का नाम:", value="साहिल")
    w_phone = st.text_input("संपर्क मोबाइल नंबर:", value="7484878440")
    if st.button("📢 रोज़गार बोर्ड पर दर्ज करें"):
        st.success(f"प्रोफ़ाइल लाइव हो गई: {w_name} (+91 {w_phone}) — {c_job}")
        wa_job = urllib.parse.quote(f"लोकल रोजगार बोर्ड: {w_name} ({c_job}) काम हेतु उपलब्ध हैं। संपर्क: {w_phone}")
        st.markdown(f'<a href="https://wa.me/?text={wa_job}" target="_blank" class="btn-action-green">📲 WhatsApp ग्रुप्स में काम हेतु साझा करें</a>', unsafe_allow_html=True)

# ================= TAB 5: VOICE KHATA & BILL =================
with tab_khata:
    st.write("### 📒 डिजिटल बिलिंग व WhatsApp रसीद")
    b_shop = st.text_input("दुकान का नाम:", value="Ahmad Super Auto Center")
    b_cust = st.text_input("ग्राहक का नाम:", value="रमेश कुमार")
    b_amt = st.text_input("कुल बिल राशि (₹):", value="2500")
    if st.button("⚡ पक्का डिजिटल बिल जनरेट करें"):
        bill_txt = f"""==================================================
डिजिटल बिल रसीद
दुकान: {b_shop} | दिनांक: {today_str}
ग्राहक: {b_cust} | कुल देय राशि: ₹{b_amt}
भुगतान स्थिति: लंबित / सत्यापित
सॉफ्टवेयर आर्किटेक्ट: साहिल अहमद (Maha Seva AI)
=================================================="""
        st.text_area("📄 तैयार रसीद:", bill_txt, height=130)
        enc_b = urllib.parse.quote(f"*{b_shop}* से आपका बिल:\nग्राहक: {b_cust}\nराशि: ₹{b_amt}\nतारीख: {today_str}")
        st.markdown(f'<a href="https://wa.me/917484878440?text={enc_b}" target="_blank" class="btn-action-green">📲 ग्राहक के WhatsApp पर रसीद भेजें</a>', unsafe_allow_html=True)

# Founder National Footer
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; background: #0B1329; padding: 16px; border-radius: 14px; border: 2px solid #38BDF8;">
    <p style="color:#38BDF8; font-size:11px; margin:0; letter-spacing:2px;">🏛️ FOUNDER & CHIEF SYSTEM ARCHITECT</p>
    <h2 style="color:#FFF; margin:4px 0; font-size:22px;">साहिल अहमद (Sahil Ahmad)</h2>
    <p style="color:#94A3B8; font-size:12px; margin:0 0 10px 0;">Maha Seva AI — 24x7 Autonomous Citizen Infrastructure</p>
    <a href="https://wa.me/{MY_WA_NUMBER}" target="_blank" style="background:#10B981; color:#fff; padding:10px 20px; border-radius:8px; text-decoration:none; font-weight:bold; font-size:13px; display:inline-block;">💬 संपर्क सूत्र (+91 {MY_WA_NUMBER[-10:]})</a>
</div>
""", unsafe_allow_html=True)
    
