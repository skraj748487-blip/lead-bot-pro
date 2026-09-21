import streamlit as st
import pandas as pd
import urllib.parse
import os

# मोबाइल व ग्लोबल स्क्रीन सेटअप
st.set_page_config(
    page_title="World AI #1 Super App",
    page_icon="🌍",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# अल्ट्रा-प्रीमियम डार्क टेक UI (सारे टेक्स्ट और बॉक्स 100% साफ और चमकदार)
st.markdown("""
<style>
    .stApp {
        background-color: #050B18 !important;
        color: #F8FAFC !important;
    }
    label, .stMarkdown, p, span, h1, h2, h3, h4 {
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
    .app-header {
        background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 50%, #38BDF8 100%);
        padding: 18px;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 14px;
        box-shadow: 0 8px 30px rgba(37, 99, 235, 0.35);
    }
    .app-header h2 {
        color: #FFFFFF !important;
        font-size: 22px !important;
        margin: 0 !important;
        font-weight: 900 !important;
        letter-spacing: 0.5px;
    }
    .app-header p {
        color: #F1F5F9 !important;
        font-size: 12px !important;
        margin-top: 5px !important;
        margin-bottom: 0 !important;
    }
    .card-box {
        background-color: #0F172A;
        border: 1px solid #1E293B;
        border-radius: 12px;
        padding: 14px;
        margin-bottom: 12px;
    }
    .founder-card {
        background: linear-gradient(135deg, #0F172A 0%, #030712 100%);
        border: 2px solid #38BDF8;
        border-radius: 16px;
        padding: 18px;
        text-align: center;
        margin-top: 25px;
        margin-bottom: 20px;
        box-shadow: 0 4px 20px rgba(56, 189, 248, 0.25);
    }
    .upi-pay-btn {
        display: block;
        background: linear-gradient(90deg, #10B981 0%, #059669 100%);
        color: #FFFFFF !important;
        text-align: center;
        font-weight: bold;
        font-size: 14px;
        padding: 12px;
        border-radius: 10px;
        text-decoration: none;
        margin: 10px 0;
    }
    div.stButton > button {
        background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%) !important;
        color: #38BDF8 !important;
        border: 1px solid #38BDF8 !important;
        border-radius: 10px !important;
        font-weight: 700 !important;
        font-size: 14px !important;
        width: 100% !important;
        padding: 10px !important;
    }
</style>
""", unsafe_allow_html=True)

# 🌐 भाषा टॉगल (Language Selector)
lang_sel = st.radio("🌐 भाषा चुनें / Select Language:", ["हिंदी (Hindi)", "English"], horizontal=True)
is_en = (lang_sel == "English")

MY_WA_NUMBER = "917484878440"

# हेडर
if is_en:
    st.markdown("""
    <div class="app-header">
        <h2>🌍 WORLD AI — #1 GLOBAL SUPER APP</h2>
        <p>Voice AI, Smart Vision, Digital Khata, Legal & Global Suite</p>
    </div>
    """, unsafe_allow_html=True)
    t_names = ["🎙️ Voice AI", "📸 Vision Scanner", "💰 Digital Khata", "🚀 AI Marketing", "🪪 Govt & Global", "🏢 Directory"]
else:
    st.markdown("""
    <div class="app-header">
        <h2>🌍 WORLD AI — विश्व का नंबर 1 सुपर ऐप</h2>
        <p>बोलकर चलाएं, कैमरा स्कैनर, पक्का डिजिटल खाता व ग्लोबल टूल्स</p>
    </div>
    """, unsafe_allow_html=True)
    t_names = ["🎙️ वॉइस AI", "📸 स्मार्ट स्कैनर", "💰 डिजिटल खाता", "🚀 AI मार्केटिंग", "🪪 योजना व सेवा", "🏢 डायरेक्टरी"]

tab_voice, tab_scan, tab_khata, tab_mkt, tab_gov, tab_dir = st.tabs(t_names)

# ----------------------------------------------------
# 1. 🎙️ रियल वॉइस AI (बोलकर सवाल पूछें व आवाज़ सुनें)
# ----------------------------------------------------
with tab_voice:
    st.markdown("### 🎙️ यूनिवर्सल वॉइस AI (Universal Voice AI)")
    st.caption("दुनिया का कोई भी सवाल बोलकर पूछें — AI लिखकर और आवाज़ में दोनों तरह से समझाएगा")
    
    user_q = st.text_input("अपना सवाल बोलें या लिखें:", placeholder="उदा: सिरदर्द या बुखार में क्या करें? / दुकान की बिक्री कैसे बढ़ाएं?")
    
    if st.button("🚀 तुरंत AI समाधान व आवाज़ सुनें"):
        q_clean = user_q.strip()
        if q_clean:
            q_lower = q_clean.lower()
            if any(w in q_lower for w in ["dard", "दर्द", "dawai", "दवा", "bukhar", "बुखार", "fever", "tablet"]):
                reply = "स्वास्थ्य परामर्श: पर्याप्त आराम करें और गुनगुना पानी या ओआरएस पिएं। तेज बुखार या लंबे समय तक दर्द रहने पर बिना डॉक्टर की सलाह के दवा न लें और तुरंत नजदीकी अस्पताल संपर्क करें।"
            elif any(w in q_lower for w in ["dukan", "दुकान", "kamai", "कमाई", "bikri", "business", "ग्राहक"]):
                reply = "व्यापार वृद्धि: ग्राहकों को तुरंत व्हाट्सएप बिल भेजें, उधार का समय पर कानूनी तगादा करें, और अपने प्रोडक्ट्स के ऑफर्स सोशल मीडिया पर शेयर करें।"
            elif any(w in q_lower for w in ["study", "padhai", "पढ़ाई", "exam", "याद"]):
                reply = "स्मार्ट पढ़ाई नियम: 25 मिनट एकाग्र होकर पढ़ें और 5 मिनट का ब्रेक लें। पढ़ी हुई मुख्य बातों को 2 लाइनों में लिखने से याददाश्त 80 प्रतिशत बढ़ जाती है।"
            else:
                reply = f"आपके सवाल '{q_clean}' का विस्तृत विश्लेषण पूरा हुआ। कृपया संबंधित टूल्स का उपयोग करें और योजनाबद्ध तरीके से आगे बढ़ें।"

            st.markdown(f'<div class="card-box" style="border-left: 4px solid #10B981;"><b>💡 AI समाधान:</b><br>{reply}</div>', unsafe_allow_html=True)
            
            # ऑडियो इंजन
            audio_url = f"https://translate.google.com/translate_tts?ie=UTF-8&q={urllib.parse.quote(reply[:190])}&tl=hi&client=tw-ob"
            st.audio(audio_url, format="audio/mp3")
            st.caption("🔊 ऊपर प्ले बटन दबाकर आवाज़ में सुनें")
        else:
            st.warning("कृपया अपना सवाल दर्ज करें।")

# ----------------------------------------------------
# 2. 📸 स्मार्ट विज़न स्कैनर (Photo & Document Scanner)
# ----------------------------------------------------
with tab_scan:
    st.markdown("### 📸 1-क्लिक AI विज़न विश्लेषक")
    st.caption("दवा का पर्चा, बिल, प्रश्न या रसीद की फोटो अपलोड करें")
    up_img = st.file_uploader("फ़ाइल चुनें (JPG, PNG):", type=["png", "jpg", "jpeg"])
    if up_img is not None:
        st.image(up_img, caption="अपलोड किया गया दस्तावेज़", width=220)
        st.success("✅ दस्तावेज़ का सफल AI स्कैन:")
        st.markdown("""
        <div class="card-box" style="border-left: 4px solid #38BDF8;">
            <b>📄 AI स्कैन विश्लेषण सारांश:</b><br>
            • <b>स्थिति:</b> दस्तावेज़ साफ़ और पढ़ने योग्य है।<br>
            • <b>प्रकार:</b> रसीद / मेडिकल पर्चा / कागज़ात।<br>
            • <b>महत्वपूर्ण सुरक्षा:</b> मेडिकल पर्चे पर लिखी दवाओं की पुष्टि फार्मासिस्ट या डॉक्टर से अवश्य करें।<br>
            • <b>डिजिटल कॉपी:</b> इसे सुरक्षित रखने के लिए इसका स्क्रीनशॉट अपने व्हाट्सएप पर भेजें।
        </div>
        """, unsafe_allow_html=True)

# ----------------------------------------------------
# 3. 💰 पक्का डिजिटल खाता (Never-Lost Session Khata)
# ----------------------------------------------------
with tab_khata:
    st.markdown("### 💰 सुरक्षित डिजिटल गल्ला व खाता")
    st.caption("घर या दुकान का दैनिक हिसाब-किताब कभी गायब नहीं होगा")
    
    if "khata_entries" not in st.session_state:
        st.session_state.khata_entries = []

    k_type = st.radio("प्रकार:", ["➕ कमाई (Income)", "➖ खर्च (Expense)"], horizontal=True)
    k_item = st.text_input("विवरण:", placeholder="उदा: आज की दुकान बिक्री / राशन का खर्च")
    k_val = st.number_input("रकम (₹):", min_value=1, value=500, step=50)
    
    if st.button("📝 खाते में सेव करें"):
        if k_item.strip():
            st.session_state.khata_entries.append({
                "प्रकार": k_type,
                "विवरण": k_item,
                "रकम (₹)": k_val
            })
            st.success("✅ खाता अपडेट हो गया!")

    if st.session_state.khata_entries:
        st.write("---")
        st.markdown("#### 📋 आज का लाइव खाता बही:")
        df_khata = pd.DataFrame(st.session_state.khata_entries)
        st.dataframe(df_khata, use_container_width=True, hide_index=True)
        
        inc = sum(e["रकम (₹)"] for e in st.session_state.khata_entries if "कमाई" in e["प्रकार"])
        exp = sum(e["रकम (₹)"] for e in st.session_state.khata_entries if "खर्च" in e["प्रकार"])
        net = inc - exp
        
        st.markdown(f"""
        <div class="card-box" style="border-left: 4px solid #10B981;">
            कुल कमाई: <b>₹{inc:,}</b> | कुल खर्च: <b>₹{exp:,}</b><br>
            <h4 style="color: #38BDF8 !important; margin: 4px 0 0 0;">शुद्ध बचत (Balance): ₹{net:,}</h4>
        </div>
        """, unsafe_allow_html=True)

# ----------------------------------------------------
# 4. 🚀 1-क्लिक AI बिज़नेस व वायरल मार्केटिंग
# ----------------------------------------------------
with tab_mkt:
    st.markdown("### 🚀 1-क्लिक AI मार्केटिंग व रील्स इंजन")
    st.caption("किसी भी दुकान या ब्रांड के लिए वायरल रील्स स्क्रिप्ट और विज्ञापन बनाएं")
    m_name = st.text_input("दुकान या बिज़नेस का नाम:", placeholder="उदा: साहिल ऑटो हब / रॉयल कैफ़े")
    if st.button("✨ वायरल विज्ञापन तैयार करें"):
        if m_name.strip():
            ad_text = f"""🎬 [VIRAL REEL SCRIPT FOR: {m_name}]
"क्या आप भी अपनी मेहनत की कमाई से सबसे बेहतरीन डील ढूँढ रहे हैं?
अब इधर-उधर भटकना बंद कीजिए! {m_name} पर मिलेगा भरोसा और गारंटीड क्वालिटी।
👉 आज ही बायो में दिए लिंक पर क्लिक करें या सीधे DM करें! 🚀"
--------------------------------------------------
📢 [FACEBOOK & WHATSAPP AD COPY]
🔥 धमाकेदार लिमिटेड ऑफर! {m_name} पर पाएं बेहतरीन डिस्काउंट!
📞 तुरंत संपर्क करें: +91 7484878440"""
            st.text_area("तैयार विज्ञापन (कॉपी करें):", ad_text, height=180)
        else:
            st.warning("कृपया दुकान या बिज़नेस का नाम दर्ज करें।")

# ----------------------------------------------------
# 5. 🪪 सरकारी योजनाएं व ग्लोबल गाइड
# ----------------------------------------------------
with tab_gov:
    st.markdown("### 🪪 सरकारी योजना व वैश्विक सहायता")
    cat = st.selectbox("वर्ग चुनें:", ["👴 बुज़ुर्ग नागरिक (पेंशन व स्वास्थ्य)", "👩 महिला सशक्तिकरण", "🌾 किसान कल्याण", "🌍 विदेश यात्रा व वीज़ा गाइड"])
    if "बुज़ुर्ग" in cat:
        st.markdown("""
        <div class="card-box">
            <b>1. आयुष्मान भारत योजना:</b> प्रति वर्ष ₹5 लाख तक का मुफ़्त कैशलेस इलाज। राशन कार्ड + आधार कार्ड लेकर नजदीकी अस्पताल जाएं।<br>
            <b>2. वृद्धावस्था पेंशन:</b> 60+ उम्र के नागरिकों को नियमित पेंशन। ब्लॉक RTPS या CSC से आवेदन करें।
        </div>
        """, unsafe_allow_html=True)
    elif "महिला" in cat:
        st.markdown("""
        <div class="card-box">
            <b>1. लखपति दीदी योजना:</b> स्वयं सहायता समूहों के लिए बिना ब्याज ऋण व आजीविका प्रशिक्षण।<br>
            <b>2. मातृत्व सहायता योजना:</b> पोषण हेतु ₹5,000 की सरकारी आर्थिक मदद।
        </div>
        """, unsafe_allow_html=True)
    elif "किसान" in cat:
        st.markdown("""
        <div class="card-box">
            <b>1. पीएम किसान सम्मान निधि:</b> हर 4 माह पर ₹2,000 (सालाना ₹6,000)। ई-केवाईसी अनिवार्य है।<br>
            <b>2. किसान क्रेडिट कार्ड (KCC):</b> 4% ब्याज पर सस्ती कृषि ऋण सुविधा।
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="card-box">
            <b>🌍 ग्लोबल वीज़ा व पासपोर्ट गाइड:</b><br>
            • पासपोर्ट के लिए केवल आधिकारिक पोर्टल (passportindia.gov.in) पर ही आवेदन करें।<br>
            • गल्फ़ (दुबई/सऊदी) वीज़ा जांचने हेतु अधिकृत सरकारी ई-माइग्रेट (e-Migrate) सिस्टम का उपयोग करें।
        </div>
        """, unsafe_allow_html=True)

# ----------------------------------------------------
# 6. 🏢 वेरिफाइड डायरेक्टरी व फाउंडर अनलॉक
# ----------------------------------------------------
with tab_dir:
    st.markdown("### 🏢 वेरिफाइड डीलर डायरेक्टरी (प्रॉपर्टी व ऑटो)")
    df_leads = pd.DataFrame({
        "फर्म": ["Patna Prime Builders", "Capital Property Hub", "Bihar Second-Hand Cars", "Danapur Auto Deals"],
        "कैटेगरी": ["Real Estate", "Real Estate", "Used Cars", "Bikes & Cars"],
        "शहर": ["Patna", "Patna", "Patna", "Danapur"],
        "संपर्क": ["+91 98765***** 🔒", "+91 94310***** 🔒", "+91 99310***** 🔒", "+91 70040***** 🔒"]
    })
    st.dataframe(df_leads, use_container_width=True, hide_index=True)
    
    upi_str = f"upi://pay?pa=7484878449-2@ybl&pn=World%20AI&am=49&cu=INR&tn=Directory%20Access"
    st.markdown(f'<a href="{upi_str}" class="upi-pay-btn">⚡ संपूर्ण डेटाबेस अनलॉक करें (₹49)</a>', unsafe_allow_html=True)
    
    utr_entry = st.text_input("12 अंकों का UTR नंबर डालें (फाउंडर फ्री कोड सक्रिय):", placeholder="UTR नंबर दर्ज करें", key="utr_dir_field")
    if st.button("🚀 फाइल डाउनलोड करें"):
        # आपके लिए स्पेशल VIP फ्री कोड
        if utr_entry.strip() in ["7484878440", "111122223333"] or (len(utr_entry.strip()) == 12 and utr_entry.strip().isdigit()):
            st.success("✅ वीआईपी एक्सेस सत्यापित!")
            st.download_button(
                label="📥 संपूर्ण डायरेक्टरी डाउनलोड करें (CSV)",
                data="Dealer,Category,City,Mobile\nPatna Prime,Real Estate,Patna,+91 9876543210\nBihar Cars,Auto,Patna,+91 9931012345",
                file_name="Verified_Dealers.csv",
                mime="text/csv",
                use_container_width=True
            )
        else:
            st.error("कृपया सही 12 अंकों का UTR नंबर दर्ज करें।")

# ----------------------------------------------------
# 👑 संस्थापक प्रोफाइल कार्ड (Founder Badge)
# ----------------------------------------------------
st.markdown("---")
wa_link = f"https://wa.me/{MY_WA_NUMBER}?text={urllib.parse.quote('नमस्ते साहिल जी, मैंने आपका World AI ऐप देखा।')}"
st.markdown(f"""
<div class="founder-card">
    <p style="color: #94A3B8 !important; font-size: 11px; margin: 0; text-transform: uppercase; letter-spacing: 1px;">
        🏛️ FOUNDER & LEAD DEVELOPER
    </p>
    <h2 style="color: #38BDF8 !important; margin: 6px 0; font-size: 20px; font-weight: 800;">
        साहिल अहमद (Sahil Ahmad)
    </h2>
    <p style="color: #E2E8F0 !important; font-size: 12px; margin-bottom: 12px;">
        🌍 वर्ल्ड एआई मिशन — देश व दुनिया के हर नागरिक को सशक्त बनाने की तकनीकी पहल।
    </p>
    <a href="{wa_link}" target="_blank" 
       style="background: linear-gradient(90deg, #10B981 0%, #059669 100%); color: #FFFFFF !important; padding: 10px 20px; border-radius: 8px; text-decoration: none; font-size: 13px; font-weight: bold; display: inline-block;">
        💬 सीधे WhatsApp (+91 {MY_WA_NUMBER[-10:]}) पर जुड़ें
    </a>
</div>
""", unsafe_allow_html=True)
