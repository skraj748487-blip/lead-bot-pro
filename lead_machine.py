import streamlit as st
import pandas as pd
import urllib.parse
import os

# मोबाइल स्क्रीन सेटअप
st.set_page_config(
    page_title="Universal Bharat AI",
    page_icon="🌍",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# बिल्कुल साफ़ और विज़िबल मोबाइल CSS (सारे टेक्स्ट और आइकॉन साफ़ दिखेंगे)
st.markdown("""
<style>
    .stApp {
        background-color: #0B1329 !important;
        color: #FFFFFF !important;
    }
    
    /* सभी लेबल्स और टेक्स्ट को चमकदार सफ़ेद बनाना */
    label, .stMarkdown, p, span, h1, h2, h3, h4 {
        color: #FFFFFF !important;
        font-weight: 600 !important;
    }

    .app-header {
        background: linear-gradient(135deg, #1D4ED8 0%, #3B82F6 100%);
        padding: 16px;
        border-radius: 14px;
        text-align: center;
        margin-bottom: 14px;
        border: 1px solid #60A5FA;
    }
    .app-header h2 {
        color: #FFFFFF !important;
        font-size: 20px !important;
        margin: 0 !important;
        font-weight: 800 !important;
    }
    .app-header p {
        color: #E2E8F0 !important;
        font-size: 12px !important;
        margin-top: 4px !important;
        margin-bottom: 0 !important;
    }

    /* रेडियो और चेकबॉक्स के टेक्स्ट को पूरी तरह विज़िबल करना */
    div[data-testid="stMarkdownContainer"] > p {
        font-size: 14px !important;
        color: #F8FAFC !important;
    }

    .guide-box {
        background-color: #1E293B;
        border-left: 4px solid #38BDF8;
        border-radius: 8px;
        padding: 14px;
        margin-bottom: 14px;
        font-size: 13px;
        color: #F8FAFC !important;
        line-height: 1.6;
    }

    .founder-card {
        background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
        border: 2px solid #38BDF8;
        border-radius: 14px;
        padding: 16px;
        text-align: center;
        margin-top: 24px;
        margin-bottom: 20px;
    }

    .upi-pay-btn {
        display: block;
        background: linear-gradient(90deg, #10B981 0%, #059669 100%);
        color: #FFFFFF !important;
        text-align: center;
        font-weight: bold;
        font-size: 15px;
        padding: 12px;
        border-radius: 10px;
        text-decoration: none;
        margin: 12px 0;
    }

    div.stButton > button {
        background-color: #1E293B !important;
        color: #38BDF8 !important;
        border: 1px solid #38BDF8 !important;
        border-radius: 8px !important;
        font-weight: 700 !important;
        font-size: 14px !important;
        width: 100% !important;
        padding: 10px !important;
    }
</style>
""", unsafe_allow_html=True)

# भाषा चयन (Language Selector)
lang = st.selectbox(
    "🌐 भाषा चुनें / Select Language / மொழியைத் தேர்ந்தெடுக்கவும்:",
    ["हिंदी (Hindi)", "English", "தமிழ் (Tamil)"]
)

# भाषा के अनुसार हेडर और शब्द बदलना
if "English" in lang:
    title = "🌍 UNIVERSAL BHARAT AI"
    subtitle = "For Students, Women, Seniors, Youth & Business Owners"
    t_kids, t_women, t_seniors, t_youth, t_vyapar = "🧒 Kids & Students", "👩 Women", "👴 Seniors", "🧑 Youth & Jobs", "🏪 Business Tools"
elif "தமிழ்" in lang:
    title = "🌍 யுனிவர்சல் பாரத் AI"
    subtitle = "மாணவர்கள், பெண்கள், முதியவர்கள் மற்றும் வணிகர்களுக்கான தளம்"
    t_kids, t_women, t_seniors, t_youth, t_vyapar = "🧒 குழந்தைகள்/மாணவர்கள்", "👩 பெண்கள் பகுதி", "👴 முதியோர் சேவை", "🧑 வேலைவாய்ப்பு", "🏪 வணிக கருவிகள்"
else:
    title = "🌍 UNIVERSAL BHARAT AI"
    subtitle = "बच्चा, महिला, युवा, बुज़ुर्ग या व्यापारी — हर भारतीय का सच्चा डिजिटल साथी"
    t_kids, t_women, t_seniors, t_youth, t_vyapar = "🧒 बच्चे व छात्र", "👩 महिला कॉर्नर", "👴 बुज़ुर्ग जन-सेवा", "🧑 युवा व रोज़गार", "🏪 व्यापारी टूल्स"

# हेडर डिस्प्ले
st.markdown(f"""
<div class="app-header">
    <h2>{title}</h2>
    <p>{subtitle}</p>
</div>
""", unsafe_allow_html=True)

# आपका असली WhatsApp नंबर
MY_WA_NUMBER = "917484878440"

# मुख्य टैब्स
tab1, tab2, tab3, tab4, tab5 = st.tabs([t_kids, t_women, t_seniors, t_youth, t_vyapar])

# ----------------------------------------------------
# 1. बच्चे व छात्र कॉर्नर
# ----------------------------------------------------
with tab1:
    st.markdown("### 🧒 छात्र सहायता व बाल कहानियाँ")
    kid_action = st.radio("विकल्प चुनें:", ["📖 ज्ञानवर्धक कहानी", "📝 स्कूल छुट्टी की अर्ज़ी"], horizontal=True)
    
    if kid_action == "📖 ज्ञानवर्धक कहानी":
        story = st.selectbox("कहानी चुनें:", ["ईमानदार लकड़हारा", "बुद्धिमान खरगोश", "प्यासा कौआ"])
        if st.button("✨ कहानी पढ़ें / सुनें"):
            if "लकड़हारा" in story:
                st.markdown("""
                <div class="guide-box">
                    <b>🪓 ईमानदार लकड़हारा:</b><br>
                    ईमानदारी सबसे बड़ा धन है। नदी से जब सोने की कुल्हाड़ी निकली तो लकड़हारे ने लालच नहीं किया, और अपनी लोहे की कुल्हाड़ी ही ली। जलपरी ने खुश होकर उसे तीनों कुल्हाड़ियाँ दे दीं।
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class="guide-box">
                    <b>🐰 बुद्धिमान खरगोश:</b><br>
                    शरीर के बल से दिमाग की बुद्धि हमेशा बड़ी होती है। खरगोश ने अपनी अक्ल से शेर को कुएं में गिरा दिया।
                </div>
                """, unsafe_allow_html=True)

    elif kid_action == "📝 स्कूल छुट्टी की अर्ज़ी":
        s_name = st.text_input("विद्यार्थी का नाम:", placeholder="उदा: साहिल कुमार")
        s_days = st.text_input("छुट्टी के दिन:", placeholder="उदा: 2 दिन")
        if st.button("📝 अर्ज़ी तैयार करें"):
            letter = f"""सेवा में,\nप्रधानाचार्य महोदय,\nविषय: अवकाश हेतु प्रार्थना पत्र\n\nमहोदय,\nसविनय निवेदन है कि आवश्यक कार्यवश मैं {s_days} तक विद्यालय आने में असमर्थ रहूँगा। कृपया अवकाश प्रदान करें।\n\nआज्ञाकारी छात्र,\n{s_name}"""
            st.text_area("कॉपी करें:", letter, height=150)

# ----------------------------------------------------
# 2. महिला कॉर्नर
# ----------------------------------------------------
with tab2:
    st.markdown("### 👩 महिला सुविधा व रसोई टिप्स")
    w_option = st.selectbox("विषय चुनें:", ["🍲 10 मिनट सूजी हलवा रेसिपी", "🌿 चेहरे की चमक के घरेलू नुस्खे", "📜 लखपति दीदी योजना"])
    
    if "हलवा" in w_option:
        st.markdown("""
        <div class="guide-box">
            <b>🥣 स्वादिष्ट सूजी हलवा:</b><br>
            घी में सूजी को सुनहरा भूनें। गरम चीनी-पानी धीरे-धीरे मिलाएँ और इलायची डालकर गरमा-गरम परोसें।
        </div>
        """, unsafe_allow_html=True)
    elif "घरेलू" in w_option:
        st.markdown("""
        <div class="guide-box">
            <b>✨ चमकती त्वचा:</b><br>
            बेसन, चुटकी भर हल्दी और कच्चे दूध का लेप 10 मिनट चेहरे पर लगाएँ। चेहरा एकदम साफ़ और चमकदार होगा।
        </div>
        """, unsafe_allow_html=True)
    elif "योजना" in w_option:
        st.markdown("""
        <div class="guide-box">
            <b>🇮🇳 लखपति दीदी योजना:</b><br>
            स्वयं सहायता समूह की महिलाओं को छोटा व्यवसाय शुरू करने के लिए आर्थिक मदद और प्रशिक्षण मिलता है।
        </div>
        """, unsafe_allow_html=True)

# ----------------------------------------------------
# 3. बुज़ुर्ग जन-सेवा
# ----------------------------------------------------
with tab3:
    st.markdown("### 👴 बुज़ुर्ग जन-सेवा व स्वास्थ्य")
    s_choice = st.selectbox("योजना या सेवा:", ["👴 वृद्धावस्था पेंशन नियम", "🏥 आयुष्मान भारत ₹5 लाख मुफ़्त इलाज", "🦴 घुटनों व जोड़ों के दर्द की मालिश"])
    
    if "पेंशन" in s_choice:
        st.markdown("""
        <div class="guide-box">
            <b>👴 वृद्धावस्था पेंशन:</b> 60 वर्ष या अधिक उम्र। आधार कार्ड, बैंक पासबुक और आय प्रमाण पत्र लेकर नजदीकी CSC/ब्लॉक में जमा करें।
        </div>
        """, unsafe_allow_html=True)
    elif "आयुष्मान" in s_choice:
        st.markdown("""
        <div class="guide-box">
            <b>🏥 आयुष्मान कार्ड:</b> हर परिवार को साल में ₹5 लाख तक का सरकारी व प्राइवेट अस्पतालों में मुफ़्त इलाज।
        </div>
        """, unsafe_allow_html=True)
    elif "घुटनों" in s_choice:
        st.markdown("""
        <div class="guide-box">
            <b>🌿 जोड़ों की देखभाल:</b> सरसों तेल में लहसुन व अजवाइन पकाकर गुनगुना मालिश करें। सुबह खाली पेट गुनगुना पानी पिएं।
        </div>
        """, unsafe_allow_html=True)

# ----------------------------------------------------
# 4. युवा व रोज़गार
# ----------------------------------------------------
with tab4:
    st.markdown("### 🧑 1-क्लिक जॉब बायोडाटा (Resume)")
    y_name = st.text_input("पूरा नाम:", placeholder="उदा: सुमित कुमार")
    y_phone = st.text_input("मोबाइल नंबर:", placeholder="उदा: 9876543210")
    y_edu = st.text_input("शिक्षा:", placeholder="उदा: 10वीं / 12वीं / ग्रेजुएट")
    y_exp = st.text_input("काम का हुनर:", placeholder="उदा: ड्राइविंग, कंप्यूटर टाइपिंग, सेल्स")
    
    if st.button("📄 तुरंत बायोडाटा तैयार करें"):
        res = f"""बायोडाटा / RESUME\nनाम: {y_name}\nमोबाइल: {y_phone}\nशिक्षा: {y_edu}\nहुनर: {y_exp}\nउपलब्धता: तत्काल कार्य हेतु उपलब्ध"""
        st.text_area("कॉपी करें:", res, height=150)

# ----------------------------------------------------
# 5. व्यापारी टूल्स
# ----------------------------------------------------
with tab5:
    st.markdown("### 🏪 स्मार्ट व्यापारी टूल्स")
    b_tool = st.radio("टूल चुनें:", ["🧾 WhatsApp डिजिटल बिल", "💰 उधारी वसूली नोटिस"], horizontal=True)
    
    if b_tool == "🧾 WhatsApp डिजिटल बिल":
        b_shop = st.text_input("दुकान का नाम:", placeholder="उदा: जनता ट्रेडर्स")
        b_cust = st.text_input("ग्राहक का नाम:", placeholder="उदा: रमेश जी")
        b_phone = st.text_input("ग्राहक का WhatsApp नंबर:", placeholder="उदा: 9876543210")
        b_total = st.text_input("कुल रकम (₹):", placeholder="उदा: 750")
        
        if st.button("📲 डिजिटल बिल भेजें"):
            if b_shop and b_cust and b_phone and b_total:
                msg = f"🧾 *डिजिटल पर्चा / BILL*\n🏪 दुकान: {b_shop}\n👤 ग्राहक: {b_cust}\n💰 कुल देय: ₹{b_total}\nस्थिति: भुगतान प्राप्त ✅\nधन्यवाद!"
                wa_url = f"https://wa.me/91{b_phone.strip()[-10:]}?text={urllib.parse.quote(msg)}"
                st.markdown(f'<a href="{wa_url}" target="_blank" class="upi-pay-btn">👉 WhatsApp पर बिल भेजें</a>', unsafe_allow_html=True)

    elif b_tool == "💰 उधारी वसूली नोटिस":
        c_name = st.text_input("बकायेदार का नाम:", placeholder="उदा: विकास जी")
        c_amount = st.text_input("बकाया रकम (₹):", placeholder="उदा: 3000")
        c_phone = st.text_input("बकायेदार का नंबर:", placeholder="उदा: 9876543210")
        
        if st.button("📩 कानूनी तगादा भेजें"):
            if c_name and c_amount and c_phone:
                msg = f"नमस्ते {c_name} जी, आपके ऊपर ₹{c_amount} का व्यापारिक बकाया लंबित है। कृपया आज ही सेटल करें अन्यथा कानूनी प्रक्रिया शुरू की जा सकती है।"
                wa_url = f"https://wa.me/91{c_phone.strip()[-10:]}?text={urllib.parse.quote(msg)}"
                st.markdown(f'<a href="{wa_url}" target="_blank" class="upi-pay-btn">👉 WhatsApp पर नोटिस भेजें</a>', unsafe_allow_html=True)

# ----------------------------------------------------
# 👑 संस्थापक प्रोफाइल (असली WhatsApp नंबर के साथ)
# ----------------------------------------------------
st.markdown("---")
wa_direct = f"https://wa.me/{MY_WA_NUMBER}?text={urllib.parse.quote('नमस्ते साहिल जी, मैंने आपका Universal Bharat AI ऐप देखा।')}"
st.markdown(f"""
<div class="founder-card">
    <p style="color: #94A3B8 !important; font-size: 11px; margin: 0; text-transform: uppercase;">
        🏛️ प्लेटफ़ॉर्म निर्माता एवं संस्थापक (Founder & Developer)
    </p>
    <h2 style="color: #38BDF8 !important; margin: 6px 0; font-size: 20px; font-weight: 800;">
        साहिल अहमद (Sahil Ahmad)
    </h2>
    <p style="color: #E2E8F0 !important; font-size: 12px; margin-bottom: 12px;">
        🇮🇳 डिजिटल भारत मिशन — देश के हर छात्र, बुज़ुर्ग, युवा व व्यापारी को डिजिटल सुविधा से जोड़ने की पहल।
    </p>
    <a href="{wa_direct}" target="_blank" 
       style="background: linear-gradient(90deg, #10B981 0%, #059669 100%); color: #FFFFFF !important; padding: 10px 20px; border-radius: 8px; text-decoration: none; font-size: 13px; font-weight: bold; display: inline-block;">
        💬 सीधे साहिल जी से WhatsApp (+91 {MY_WA_NUMBER[-10:]}) पर जुड़ें
    </a>
</div>
""", unsafe_allow_html=True)
