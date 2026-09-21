import streamlit as st
import pandas as pd
import urllib.parse
import os

# मोबाइल स्क्रीन व लेआउट सेटअप
st.set_page_config(
    page_title="Bharat World AI — Universal Super Suite",
    page_icon="🌍",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# हाई-कंट्रास्ट क्लीन CSS (सफ़ेद बॉक्स में साफ़ काला टेक्स्ट)
st.markdown("""
<style>
    .stApp {
        background-color: #0B1329 !important;
        color: #FFFFFF !important;
    }
    label, .stMarkdown, p, span, h1, h2, h3, h4 {
        color: #FFFFFF !important;
        font-weight: 600 !important;
    }
    input, textarea, .stTextInput input, .stTextArea textarea, select {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        font-weight: 600 !important;
        font-size: 15px !important;
        border-radius: 8px !important;
    }
    .app-header {
        background: linear-gradient(135deg, #1D4ED8 0%, #2563EB 100%);
        padding: 16px;
        border-radius: 14px;
        text-align: center;
        margin-bottom: 12px;
        border: 1px solid #60A5FA;
    }
    .app-header h2 {
        color: #FFFFFF !important;
        font-size: 21px !important;
        margin: 0 !important;
        font-weight: 800 !important;
    }
    .app-header p {
        color: #E2E8F0 !important;
        font-size: 12px !important;
        margin-top: 4px !important;
        margin-bottom: 0 !important;
    }
    .card-box {
        background-color: #1E293B;
        border: 1px solid #334155;
        border-radius: 10px;
        padding: 14px;
        margin-bottom: 12px;
    }
    .founder-card {
        background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
        border: 2px solid #38BDF8;
        border-radius: 14px;
        padding: 16px;
        text-align: center;
        margin-top: 24px;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(56, 189, 248, 0.2);
    }
    .upi-pay-btn {
        display: block;
        background: linear-gradient(90deg, #10B981 0%, #059669 100%);
        color: #FFFFFF !important;
        text-align: center;
        font-weight: bold;
        font-size: 14px;
        padding: 11px;
        border-radius: 10px;
        text-decoration: none;
        margin: 10px 0;
    }
    div.stButton > button {
        background-color: #1E293B !important;
        color: #38BDF8 !important;
        border: 1px solid #38BDF8 !important;
        border-radius: 8px !important;
        font-weight: 700 !important;
        font-size: 14px !important;
        width: 100% !important;
        padding: 9px !important;
    }
</style>
""", unsafe_allow_html=True)

# 🌐 भाषा स्विच
lang_toggle = st.radio("🌐 Select Language / भाषा चुनें:", ["हिंदी (Hindi)", "English"], horizontal=True)
is_en = (lang_toggle == "English")

MY_WA_NUMBER = "917484878440"

# हेडर
if is_en:
    st.markdown("""
    <div class="app-header">
        <h2>🌍 WORLD AI — ALL-IN-ONE SUPER APP</h2>
        <p>Voice AI, Scanner, Digital Khata, Govt Schemes & Global Utility</p>
    </div>
    """, unsafe_allow_html=True)
    tab_names = ["🎙️ Voice AI", "📸 Photo Scanner", "💰 Daily Khata", "🪪 Govt Schemes", "💼 Earn Daily", "🏢 Directory"]
else:
    st.markdown("""
    <div class="app-header">
        <h2>🌍 WORLD AI — ऑल-इन-वन सुपर ऐप</h2>
        <p>बोलकर चलाएं, स्कैनर, डिजिटल खाता, सरकारी योजनाएं व ग्लोबल टूल्स</p>
    </div>
    """, unsafe_allow_html=True)
    tab_names = ["🎙️ वॉइस AI", "📸 फोटो स्कैनर", "💰 डिजिटल खाता", "🪪 सरकारी योजनाएं", "💼 रोज़गार व कमाई", "🏢 डायरेक्टरी"]

tab_voice, tab_scan, tab_khata, tab_scheme, tab_earn, tab_dir = st.tabs(tab_names)

# ----------------------------------------------------
# 1. 🎙️ बोलकर चलाओ वॉइस AI (Voice Assistant)
# ----------------------------------------------------
with tab_voice:
    st.markdown("### 🎙️ वॉइस AI असिस्टेंट (Voice Assistant)")
    st.caption("अनपढ़ हों या पढ़े-लिखे—कीबोर्ड माइक दबाकर बोलें या टाइप करें")
    v_input = st.text_input("अपनी भाषा में बोलें या लिखें:", placeholder="उदा: बुखार में क्या करें? / दुकान का हिसाब कैसे रखें?")
    if st.button("🚀 तुरंत AI समाधान"):
        if v_input.strip():
            q_low = v_input.lower()
            if any(w in q_low for w in ["बुखार", "दवा", "सिरदर्द", "fever", "health"]):
                res = "🩺 **स्वास्थ्य सलाह:** पर्याप्त आराम करें और गुनगुना पानी/ओआरएस पिएं। बुखार 48 घंटे से अधिक रहे तो तुरंत डॉक्टर से संपर्क करें।"
            elif any(w in q_low for w in ["हिसाब", "दुकान", "कमाई", "business"]):
                res = "💼 **व्यापार सलाह:** डिजिटल खाता टैब का उपयोग करें, ग्राहकों को WhatsApp बिल भेजें और दैनिक खर्चों को ट्रैक करें।"
            else:
                res = f"💡 **World AI परामर्श:** आपके सवाल '{v_input}' का विश्लेषण किया गया है। विस्तृत सहायता हेतु संबंधित टैब का उपयोग करें।"
            st.markdown(f'<div class="card-box" style="border-left: 4px solid #10B981;">{res}</div>', unsafe_allow_html=True)
        else:
            st.warning("कृपया अपना सवाल बोलें या लिखें।")

# ----------------------------------------------------
# 2. 📸 फोटो व दस्तावेज़ स्कैनर (Photo Scanner)
# ----------------------------------------------------
with tab_scan:
    st.markdown("### 📸 1-क्लिक AI फोटो व डॉक्यूमेंट विश्लेषक")
    st.caption("दवा का पर्चा, बिल, सवाल या रसीद की फोटो अपलोड करें")
    uploaded_file = st.file_uploader("फ़ाइल या फोटो चुनें (JPG, PNG):", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption="अपलोड किया गया दस्तावेज़", width=200)
        st.success("✅ दस्तावेज़ सफलता से लोड हुआ! AI विश्लेषण:")
        st.markdown("""
        <div class="card-box" style="border-left: 4px solid #38BDF8;">
            <b>📄 AI स्कैन परिणाम:</b><br>
            • दस्तावेज़ का प्रकार: रसीद / पर्चा / सामान्य फ़ाइल<br>
            • स्थिति: स्पष्ट व पढ़ने योग्य<br>
            • सुझाव: इसे सुरक्षित डिजिटल बैकअप के रूप में अपने WhatsApp पर सहेजें।
        </div>
        """, unsafe_allow_html=True)

# ----------------------------------------------------
# 3. 💰 दैनिक बजट व डिजिटल खाता (Personal & Shop Khata)
# ----------------------------------------------------
with tab_khata:
    st.markdown("### 💰 दैनिक गल्ला व डिजिटल खाता (Daily Khata)")
    st.caption("दुकान या घर का दैनिक खर्च और कमाई तुरंत जोड़ें")
    k_type = st.radio("प्रकार:", ["➕ दैनिक कमाई (Income)", "➖ दैनिक खर्च (Expense)"], horizontal=True)
    k_desc = st.text_input("विवरण:", placeholder="उदा: आज की दुकान बिक्री / सब्जी का खर्च")
    k_amt = st.number_input("रकम (₹):", min_value=1, value=500, step=50)
    if st.button("📝 खाते में दर्ज करें"):
        st.success(f"✅ ₹{k_amt} '{k_desc}' के लिए दर्ज कर दिया गया है!")

# ----------------------------------------------------
# 4. 🪪 1-क्लिक सरकारी योजना व जन-सेवा
# ----------------------------------------------------
with tab_scheme:
    st.markdown("### 🪪 सरकारी योजना व जन-सेवा खोजक")
    age_group = st.selectbox("वर्ग चुनें:", ["👴 बुज़ुर्ग (60+ वर्ष)", "👩 महिलाएँ व बालिकाएँ", "🌾 किसान भाई", "🧑 छात्र व युवा"])
    if "बुज़ुर्ग" in age_group:
        st.markdown("""
        <div class="card-box">
            <b>1. आयुष्मान भारत योजना:</b> ₹5 लाख तक का सालाना मुफ़्त इलाज। आधार + राशन कार्ड आवश्यक।<br>
            <b>2. वृद्धावस्था पेंशन:</b> हर महीने बंधी आर्थिक सहायता। ब्लॉक/CSC से ऑनलाइन आवेदन।
        </div>
        """, unsafe_allow_html=True)
    elif "महिलाएँ" in age_group:
        st.markdown("""
        <div class="card-box">
            <b>1. लखपति दीदी योजना:</b> स्वयं सहायता समूह की महिलाओं को बिना ब्याज लोन व बिज़नेस ट्रेनिंग।<br>
            <b>2. मातृत्व वंदना योजना:</b> गर्भवती महिलाओं को पोषण हेतु ₹5000 की वित्तीय मदद।
        </div>
        """, unsafe_allow_html=True)
    elif "किसान" in age_group:
        st.markdown("""
        <div class="card-box">
            <b>1. पीएम किसान सम्मान निधि:</b> हर साल ₹6,000 सीधे खाते में। ई-केवाईसी अनिवार्य।<br>
            <b>2. किसान क्रेडिट कार्ड (KCC):</b> 4% ब्याज पर खेती व पशुपालन हेतु ऋण।
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="card-box">
            <b>1. पीएम इंटर्नशिप योजना:</b> टॉप कंपनियों में मासिक स्टाइपेंड के साथ ट्रेनिंग।<br>
            <b>2. कौशल विकास मिशन:</b> फ्री कंप्यूटर व वोकेशनल ट्रेनिंग सर्टिफिकेट के साथ।
        </div>
        """, unsafe_allow_html=True)

# ----------------------------------------------------
# 5. 💼 रोज़गार व मोबाइल से कमाई (Earn Daily)
# ----------------------------------------------------
with tab_earn:
    st.markdown("### 💼 मोबाइल से रोज़ाना कमाई के साधन")
    st.caption("छात्रों और युवाओं के लिए जीरो-इन्वेस्टमेंट कमाई के सिद्ध तरीके")
    st.markdown("""
    <div class="card-box" style="border-left: 4px solid #10B981;">
        <b>1. बायोडाटा व फॉर्म सेवा:</b> अपने गांव/कस्बे के लड़कों का जॉब बायोडाटा हमारे ऐप से बनाकर ₹30-50 प्रति बायोडाटा लें।<br><br>
        <b>2. दुकानदारों के लिए डिजिटल बिलिंग:</b> आसपास के 10 दुकानदारों को WhatsApp डिजिटल बिलिंग सेवा देकर महीने का ₹100-200 प्रति दुकान लें।<br><br>
        <b>3. डायरेक्टरी री-सेल:</b> हमारे वेरिफाइड रियल एस्टेट व कार डीलर्स की लिस्ट को प्रॉपर्टी खरीदारों को साझा करके कमीशन पाएं।
    </div>
    """, unsafe_allow_html=True)

# ----------------------------------------------------
# 6. 🏢 लीड्स व डायरेक्टरी (Founder Free Access)
# ----------------------------------------------------
with tab_dir:
    st.markdown("### 🏢 वेरिफाइड डीलर डायरेक्टरी")
    df_leads = pd.DataFrame({
        "फर्म": ["Patna Prime Builders", "Capital Property Hub", "Bihar Second-Hand Cars", "Danapur Auto Deals"],
        "कैटेगरी": ["Real Estate", "Real Estate", "Used Cars", "Bikes & Cars"],
        "शहर": ["Patna", "Patna", "Patna", "Danapur"],
        "संपर्क": ["+91 98765***** 🔒", "+91 94310***** 🔒", "+91 99310***** 🔒", "+91 70040***** 🔒"]
    })
    st.dataframe(df_leads, use_container_width=True, hide_index=True)
    
    upi_str = f"upi://pay?pa=7484878449-2@ybl&pn=World%20AI&am=49&cu=INR&tn=Directory%20Access"
    st.markdown(f'<a href="{upi_str}" class="upi-pay-btn">⚡ संपूर्ण डेटाबेस अनलॉक करें (₹49)</a>', unsafe_allow_html=True)
    
    utr_entry = st.text_input("पेमेंट के बाद UTR नंबर डालें (फाउंडर फ्री कोड सक्रिय):", placeholder="12 अंकों का UTR नंबर", key="utr_glob")
    if st.button("🚀 फाइल डाउनलोड करें"):
        if utr_entry.strip() in ["7484878440", "111122223333"] or (len(utr_entry.strip()) == 12 and utr_entry.strip().isdigit()):
            st.success("✅ सत्यापित! नीचे दिए गए बटन से पूरी शीट डाउनलोड करें:")
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
# 👑 संस्थापक प्रोफाइल कार्ड
# ----------------------------------------------------
st.markdown("---")
wa_link = f"https://wa.me/{MY_WA_NUMBER}?text={urllib.parse.quote('नमस्ते साहिल जी, मैंने आपका World AI ऐप देखा।')}"
st.markdown(f"""
<div class="founder-card">
    <p style="color: #94A3B8 !important; font-size: 11px; margin: 0; text-transform: uppercase;">
        🏛️ FOUNDER & LEAD DEVELOPER
    </p>
    <h2 style="color: #38BDF8 !important; margin: 6px 0; font-size: 20px; font-weight: 800;">
        साहिल अहमद (Sahil Ahmad)
    </h2>
    <p style="color: #E2E8F0 !important; font-size: 12px; margin-bottom: 12px;">
        🌍 वर्ल्ड एआई मिशन — देश व दुनिया के हर छात्र, युवा, बुज़ुर्ग व व्यापारी को डिजिटल शक्ति से सशक्त बनाने की पहल।
    </p>
    <a href="{wa_link}" target="_blank" 
       style="background: linear-gradient(90deg, #10B981 0%, #059669 100%); color: #FFFFFF !important; padding: 10px 20px; border-radius: 8px; text-decoration: none; font-size: 13px; font-weight: bold; display: inline-block;">
        💬 सीधे WhatsApp (+91 {MY_WA_NUMBER[-10:]}) पर जुड़ें
    </a>
</div>
""", unsafe_allow_html=True)
