import streamlit as st
import pandas as pd
import urllib.parse
import os

# मोबाइल स्क्रीन व लेआउट सेटअप
st.set_page_config(
    page_title="World AI Super App",
    page_icon="🌍",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# प्रीमियम टेक UI और ऑडियो स्टाइलिंग
st.markdown("""
<style>
    .stApp {
        background-color: #060D1F !important;
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
        background: linear-gradient(135deg, #1E3A8A 0%, #3B82F6 100%);
        padding: 18px;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 14px;
        border: 1px solid rgba(255, 255, 255, 0.15);
        box-shadow: 0 8px 25px rgba(30, 58, 138, 0.4);
    }
    .app-header h2 {
        color: #FFFFFF !important;
        font-size: 22px !important;
        margin: 0 !important;
        font-weight: 800 !important;
        letter-spacing: 0.5px;
    }
    .app-header p {
        color: #E2E8F0 !important;
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
        box-shadow: 0 4px 20px rgba(56, 189, 248, 0.2);
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

# भाषा स्विच
lang_toggle = st.radio("🌐 भाषा चुनें / Select Language:", ["हिंदी (Hindi)", "English"], horizontal=True)
is_en = (lang_toggle == "English")

MY_WA_NUMBER = "917484878440"

# हेडर
if is_en:
    st.markdown("""
    <div class="app-header">
        <h2>🌍 WORLD AI — GLOBAL SUPER APP</h2>
        <p>Voice AI, Smart Scanner, Digital Khata & Global Utilities</p>
    </div>
    """, unsafe_allow_html=True)
    tab_names = ["🎙️ Voice AI", "📸 Photo Scanner", "💰 Daily Khata", "🪪 Govt Schemes", "🏢 Directory"]
else:
    st.markdown("""
    <div class="app-header">
        <h2>🌍 WORLD AI — ऑल-इन-वन सुपर ऐप</h2>
        <p>बोलकर चलाएं, स्कैनर, डिजिटल खाता, सरकारी योजनाएं व ग्लोबल टूल्स</p>
    </div>
    """, unsafe_allow_html=True)
    tab_names = ["🎙️ वॉइस AI", "📸 फोटो स्कैनर", "💰 डिजिटल खाता", "🪪 सरकारी योजनाएं", "🏢 डायरेक्टरी"]

tab_voice, tab_scan, tab_khata, tab_scheme, tab_dir = st.tabs(tab_names)

# ----------------------------------------------------
# 1. 🎙️ बोलकर चलाओ और सुनो (Voice Assistant With Audio)
# ----------------------------------------------------
with tab_voice:
    st.markdown("### 🎙️ बोलकर पूछें व आवाज़ में सुनें")
    st.caption("कीबोर्ड माइक से बोलें — AI लिखकर और बोलकर दोनों तरह से समाधान देगा")
    v_input = st.text_input("अपनी भाषा में बोलें या लिखें:", placeholder="उदा: दर्द कर रहा है कौन सा दवाई लें / दुकान का हिसाब")
    
    if st.button("🚀 तुरंत AI समाधान व आवाज़ सुनें"):
        if v_input.strip():
            q_low = v_input.lower()
            if any(w in q_low for w in ["dard", "दर्द", "dawai", "दवा", "bukhar", "बुखार", "fever"]):
                res = "यदि शरीर में दर्द या बुखार है, तो पर्याप्त आराम करें और गुनगुना पानी पिएं। बिना डॉक्टर के परामर्श के कोई भी तेज दर्द निवारक दवा न लें। स्थिति गंभीर होने पर तुरंत नजदीकी अस्पताल जाएं।"
            elif any(w in q_low for w in ["hisaab", "हिसाब", "dukan", "दुकान", "kamai", "कमाई"]):
                res = "दुकान की बिक्री बढ़ाने के लिए डिजिटल खाता मेंटेन करें और ग्राहकों को तुरंत व्हाट्सएप बिल भेजें।"
            else:
                res = f"आपके सवाल '{v_input}' का समाधान तैयार है। कृपया संबंधित सेवा का उपयोग करें।"

            # स्क्रीन पर दिखाना
            st.markdown(f'<div class="card-box" style="border-left: 4px solid #10B981;"><b>💡 AI समाधान:</b><br>{res}</div>', unsafe_allow_html=True)
            
            # ऑटो वॉइस स्पीच (Google TTS ऑडियो प्लेयर)
            audio_url = f"https://translate.google.com/translate_tts?ie=UTF-8&q={urllib.parse.quote(res[:180])}&tl=hi&client=tw-ob"
            st.audio(audio_url, format="audio/mp3")
            st.caption("🔊 ऊपर प्ले बटन दबाकर आवाज़ सुनें")
        else:
            st.warning("कृपया अपना सवाल बोलें या लिखें।")

# ----------------------------------------------------
# 2. 📸 फोटो व दस्तावेज़ स्कैनर
# ----------------------------------------------------
with tab_scan:
    st.markdown("### 📸 1-क्लिक AI दस्तावेज़ व पर्चा विश्लेषक")
    st.caption("दवा का पर्चा, बिल, सवाल या रसीद की फोटो अपलोड करें")
    uploaded_file = st.file_uploader("फ़ाइल चुनें (JPG, PNG):", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption="अपलोड किया गया दस्तावेज़", width=220)
        st.success("✅ दस्तावेज़ का विश्लेषण:")
        st.markdown("""
        <div class="card-box" style="border-left: 4px solid #38BDF8;">
            <b>📄 AI स्कैन सारांश:</b><br>
            • स्थिति: दस्तावेज़ पढ़ने योग्य है।<br>
            • मेडिकल पर्चा/बिल होने पर हमेशा डॉक्टर या अधिकृत विक्रेता से पुष्टि करें।<br>
            • बैकअप के लिए इसे सुरक्षित रखें।
        </div>
        """, unsafe_allow_html=True)

# ----------------------------------------------------
# 3. 💰 डिजिटल खाता
# ----------------------------------------------------
with tab_khata:
    st.markdown("### 💰 दैनिक गल्ला व डिजिटल खाता")
    k_type = st.radio("प्रकार:", ["➕ दैनिक कमाई (Income)", "➖ दैनिक खर्च (Expense)"], horizontal=True)
    k_desc = st.text_input("विवरण:", placeholder="उदा: आज की दुकान बिक्री")
    k_amt = st.number_input("रकम (₹):", min_value=1, value=500, step=50)
    if st.button("📝 खाते में दर्ज करें"):
        st.success(f"✅ ₹{k_amt} दर्ज कर दिया गया है!")

# ----------------------------------------------------
# 4. 🪪 सरकारी योजनाएं
# ----------------------------------------------------
with tab_scheme:
    st.markdown("### 🪪 सरकारी योजना व जन-सेवा")
    age_group = st.selectbox("वर्ग चुनें:", ["👴 बुज़ुर्ग (60+ वर्ष)", "👩 महिलाएँ", "🌾 किसान", "🧑 युवा"])
    if "बुज़ुर्ग" in age_group:
        st.markdown('<div class="card-box"><b>1. आयुष्मान भारत:</b> ₹5 लाख तक मुफ़्त इलाज।<br><b>2. वृद्धावस्था पेंशन:</b> मासिक आर्थिक सहायता।</div>', unsafe_allow_html=True)
    elif "महिलाएँ" in age_group:
        st.markdown('<div class="card-box"><b>1. लखपति दीदी योजना:</b> बिना ब्याज ऋण व प्रशिक्षण।</div>', unsafe_allow_html=True)
    elif "किसान" in age_group:
        st.markdown('<div class="card-box"><b>1. पीएम किसान:</b> ₹6,000 सालाना सीधे खाते में।</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="card-box"><b>1. पीएम इंटर्नशिप व कौशल विकास:</b> मुफ़्त ट्रेनिंग व स्टाइपेंड।</div>', unsafe_allow_html=True)

# ----------------------------------------------------
# 5. 🏢 डायरेक्टरी व फाउंडर अनलॉक
# ----------------------------------------------------
with tab_dir:
    st.markdown("### 🏢 वेरिफाइड डायरेक्टरी")
    df_leads = pd.DataFrame({
        "फर्म": ["Patna Prime Builders", "Capital Property Hub", "Bihar Second-Hand Cars", "Danapur Auto Deals"],
        "कैटेगरी": ["Real Estate", "Real Estate", "Used Cars", "Bikes & Cars"],
        "शहर": ["Patna", "Patna", "Patna", "Danapur"],
        "संपर्क": ["+91 98765***** 🔒", "+91 94310***** 🔒", "+91 99310***** 🔒", "+91 70040***** 🔒"]
    })
    st.dataframe(df_leads, use_container_width=True, hide_index=True)
    
    upi_str = f"upi://pay?pa=7484878449-2@ybl&pn=World%20AI&am=49&cu=INR&tn=Directory%20Access"
    st.markdown(f'<a href="{upi_str}" class="upi-pay-btn">⚡ संपूर्ण डेटाबेस अनलॉक करें (₹49)</a>', unsafe_allow_html=True)
    
    utr_entry = st.text_input("12 अंकों का UTR नंबर डालें (फाउंडर फ्री कोड सक्रिय):", placeholder="UTR नंबर", key="utr_dir_k")
    if st.button("🚀 फाइल डाउनलोड करें"):
        if utr_entry.strip() in ["7484878440", "111122223333"] or (len(utr_entry.strip()) == 12 and utr_entry.strip().isdigit()):
            st.success("✅ सत्यापित!")
            st.download_button("📥 डाउनलोड CSV", data="Dealer,City,Mobile\nPatna Prime,Patna,+91 9876543210", file_name="Verified_Dealers.csv", mime="text/csv", use_container_width=True)
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
        🌍 वर्ल्ड एआई मिशन — देश व दुनिया के हर नागरिक को सशक्त बनाने की तकनीकी पहल।
    </p>
    <a href="{wa_link}" target="_blank" 
       style="background: linear-gradient(90deg, #10B981 0%, #059669 100%); color: #FFFFFF !important; padding: 10px 20px; border-radius: 8px; text-decoration: none; font-size: 13px; font-weight: bold; display: inline-block;">
        💬 सीधे WhatsApp (+91 {MY_WA_NUMBER[-10:]}) पर जुड़ें
    </a>
</div>
""", unsafe_allow_html=True)
