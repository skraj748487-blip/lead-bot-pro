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

# मॉडर्न मोबाइल CSS
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
        box-shadow: 0 4px 15px rgba(56, 189, 248, 0.2);
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

# 🌐 भाषा चयन (Language Selection)
lang_choice = st.selectbox(
    "🌐 Choose Language / भाषा चुनें / மொழியைத் தேர்ந்தெடுக்கவும்:",
    ["हिंदी (Hindi)", "English", "தமிழ் (Tamil)"]
)

# 🎯 भाषा के अनुसार पूरा डाटा डिक्शनरी (100% Complete Translation)
TEXTS = {
    "Hindi": {
        "title": "🌍 UNIVERSAL BHARAT AI",
        "subtitle": "बच्चा, छात्र, महिला, बुज़ुर्ग या व्यापारी — हर भारतीय का सच्चा डिजिटल साथी",
        "tab_ai": "🤖 AI समाधान",
        "tab_kids": "🧒 बच्चे व छात्र",
        "tab_women": "👩 महिला कॉर्नर",
        "tab_seniors": "👴 बुज़ुर्ग सेवा",
        "tab_business": "🏪 व्यापारी टूल्स",
        "ai_header": "🎙️ कोई भी सवाल पूछें (बोलकर या लिखकर)",
        "ai_placeholder": "उदा: बुखार में क्या करें? / दुकान की बिक्री कैसे बढ़ाएँ?",
        "ai_btn": "🚀 तुरंत समाधान पाएँ",
        "kids_header": "🧒 छात्र सहायता व बाल कहानियाँ",
        "kids_story": "📖 ज्ञानवर्धक कहानी",
        "kids_leave": "📝 स्कूल छुट्टी की अर्ज़ी",
        "women_header": "👩 महिला सशक्तिकरण व स्वास्थ्य",
        "seniors_header": "👴 बुज़ुर्ग जन-सेवा व स्वास्थ्य योजनाएँ",
        "biz_header": "🏪 व्यापारी डिजिटल टूल्स",
        "bill_btn": "📲 WhatsApp पर बिल भेजें",
        "notice_btn": "📩 कानूनी उधारी तगादा भेजें"
    },
    "English": {
        "title": "🌍 UNIVERSAL BHARAT AI",
        "subtitle": "Universal Digital Assistant for Students, Women, Seniors & Businesses",
        "tab_ai": "🤖 AI Assistant",
        "tab_kids": "🧒 Kids & Students",
        "tab_women": "👩 Women Corner",
        "tab_seniors": "👴 Seniors Care",
        "tab_business": "🏪 Business Tools",
        "ai_header": "🎙️ Ask Any Question (Type or Voice)",
        "ai_placeholder": "e.g. How to cure cold? / How to grow local business?",
        "ai_btn": "🚀 Get Instant Solution",
        "kids_header": "🧒 Student Homework & Moral Stories",
        "kids_story": "📖 Inspiring Story",
        "kids_leave": "📝 Leave Application",
        "women_header": "👩 Women Empowerment & Health",
        "seniors_header": "👴 Senior Citizen Support & Health Schemes",
        "biz_header": "🏪 Smart Business Tools",
        "bill_btn": "📲 Send Invoice on WhatsApp",
        "notice_btn": "📩 Send Legal Payment Reminder"
    },
    "Tamil": {
        "title": "🌍 யுனிவர்சல் பாரத் AI",
        "subtitle": "மாணவர்கள், பெண்கள், முதியவர்கள் மற்றும் வணிகர்களுக்கான முழுமையான தளம்",
        "tab_ai": "🤖 AI தீர்வு",
        "tab_kids": "🧒 குழந்தைகள்",
        "tab_women": "👩 பெண்கள் பகுதி",
        "tab_seniors": "👴 முதியோர் சேவை",
        "tab_business": "🏪 வணிக கருவிகள்",
        "ai_header": "🎙️ எந்த கேள்வியையும் கேளுங்கள்",
        "ai_placeholder": "எ.கா: காய்ச்சலுக்கு என்ன செய்ய வேண்டும்? / வியாபாரத்தை வளர்ப்பது எப்படி?",
        "ai_btn": "🚀 உடனடி தீர்வு பெறுக",
        "kids_header": "🧒 மாணவர் உதவி & கதைகள்",
        "kids_story": "📖 நல்லொழுக்க கதை",
        "kids_leave": "📝 விடுப்பு விண்ணப்பம்",
        "women_header": "👩 மகளிர் நலம் மற்றும் வழிகாட்டுதல்",
        "seniors_header": "👴 முதியோர் நலத் திட்டங்கள் & மருத்துவம்",
        "biz_header": "🏪 வணிக கருவிகள்",
        "bill_btn": "📲 வாட்ஸ்அப்பில் பில் அனுப்பவும்",
        "notice_btn": "📩 கடன் வசூல் அறிவிப்பு அனுப்பவும்"
    }
}

# एक्टिव भाषा चुनना
if "English" in lang_choice:
    T = TEXTS["English"]
    CURR_LANG = "en"
elif "தமிழ்" in lang_choice:
    T = TEXTS["Tamil"]
    CURR_LANG = "ta"
else:
    T = TEXTS["Hindi"]
    CURR_LANG = "hi"

# ऐप हेडर
st.markdown(f"""
<div class="app-header">
    <h2>{T['title']}</h2>
    <p>{T['subtitle']}</p>
</div>
""", unsafe_allow_html=True)

# 5 मुख्य टैब्स
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    T["tab_ai"],
    T["tab_kids"],
    T["tab_women"],
    T["tab_seniors"],
    T["tab_business"]
])

# ----------------------------------------------------
# 1. AI असिस्टेंट
# ----------------------------------------------------
with tab1:
    st.markdown(f"### {T['ai_header']}")
    u_query = st.text_input("", placeholder=T["ai_placeholder"])
    if st.button(T["ai_btn"]):
        q = u_query.lower()
        if not q:
            st.warning("Please type your question / कृपया सवाल लिखें")
        else:
            if CURR_LANG == "en":
                ans = f"""💡 **World AI Guidance for:** *"{u_query}"*
1. **Practical Advice:** For health symptoms, consult a nearby healthcare clinic immediately. Stay hydrated and well-rested.
2. **Productivity:** Break large tasks into smaller 20-minute actions. Keep track of daily expenses.
3. **Assistance:** Explore the specialized tabs for Students, Seniors, and Business Invoicing."""
            elif CURR_LANG == "ta":
                ans = f"""💡 **World AI தமிழ் வழிகாட்டுதல்:** *"{u_query}"*
1. **முக்கிய அறிவுரை:** உடல்நலம் பாதிக்கப்பட்டால் உடனடியாக அருகில் உள்ள மருத்துவரை அணுகவும்.
2. **முன்னேற்றம்:** உங்கள் பணிகளைத் திட்டமிட்டு தினமும் சிறிது சிறிதாகச் செய்து முடிக்கவும்.
3. **உதவி:** கல்வி, மூத்த குடிமக்கள் திட்டம் மற்றும் வியாபார பில் பயன்பாட்டிற்கு குறிப்பிட்ட பிரிவுகளைப் பார்க்கவும்."""
            else:
                ans = f"""💡 **Universal AI समाधान:** *"{u_query}"*
1. **स्वास्थ्य व प्राथमिक सलाह:** यदि शारीरिक अस्वस्थता है तो तुरंत नज़दीकी डॉक्टर या प्राथमिक स्वास्थ्य केंद्र से संपर्क करें।
2. **दैनिक प्रगति:** अपने महत्वपूर्ण कार्यों की सूची बनाएँ और प्रतिदिन छोटे-छोटे लक्ष्यों को पूरा करें।
3. **विशेष सुविधा:** छात्र, बुज़ुर्ग सहायता या दुकान के बिल बनाने हेतु ऊपर दिए गए संबंधित टैब का इस्तेमाल करें।"""
            
            st.markdown(f'<div class="guide-box">{ans}</div>', unsafe_allow_html=True)

# ----------------------------------------------------
# 2. बच्चे व छात्र (Kids & Students)
# ----------------------------------------------------
with tab2:
    st.markdown(f"### {T['kids_header']}")
    k_mode = st.radio("Options:", [T["kids_story"], T["kids_leave"]], horizontal=True)
    
    if k_mode == T["kids_story"]:
        if CURR_LANG == "en":
            st.markdown("""
            <div class="guide-box">
                <b>🪓 The Honest Woodcutter:</b><br>
                A poor woodcutter dropped his axe into the river. An angel offered gold and silver axes, but he only accepted his own iron axe. Impressed by his honesty, the angel gifted him all three axes.<br>
                <b>Moral:</b> Honesty is always rewarded.
            </div>
            """, unsafe_allow_html=True)
        elif CURR_LANG == "ta":
            st.markdown("""
            <div class="guide-box">
                <b>🪓 நேர்மையான மரம்வெட்டி:</b><br>
                மரம்வெட்டியின் கோடாரி ஆற்றில் விழுந்தது. தேவதை தங்கம் மற்றும் வெள்ளி கோடாரிகளைக் கொடுத்தபோதும், அவன் தன் இரும்பு கோடாரியையே கேட்டான். அவனது நேர்மையைப் பாராட்டி தேவதை அனைத்தையும் பரிசளித்தது.<br>
                <b>நீதி:</b> நேர்மையே சிறந்த கொள்கை.
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="guide-box">
                <b>🪓 ईमानदार लकड़हारा:</b><br>
                गरीब लकड़हारे ने सोने-चाँदी की कुल्हाड़ी का लालच न करके अपनी लोहे की कुल्हाड़ी माँगी। जलपरी ने प्रसन्न होकर तीनों कुल्हाड़ियाँ उपहार में दे दीं।<br>
                <b>सीख:</b> ईमानदारी ही सबसे बड़ा धन है।
            </div>
            """, unsafe_allow_html=True)
            
    else:
        st_name = st.text_input("Student Name / नाम:", value="Sahil")
        st_days = st.text_input("Days / दिन:", value="2")
        if st.button("Generate Leave Application / अर्ज़ी बनाएँ"):
            if CURR_LANG == "en":
                app_txt = f"To,\nThe Principal,\n\nSubject: Leave Application for {st_days} days.\n\nRespected Sir/Madam,\nI kindly request you to grant me leave for {st_days} days due to personal urgent work.\n\nThanking you,\nYours obediently,\n{st_name}"
            else:
                app_txt = f"सेवा में,\nप्रधानाचार्य महोदय,\n\nविषय: {st_days} दिन के अवकाश हेतु प्रार्थना पत्र।\n\nमहोदय,\nसविनय निवेदन है कि आवश्यक कार्य होने के कारण मैं {st_days} दिन तक विद्यालय आने में असमर्थ हूँ। कृपया अवकाश प्रदान करें।\n\nआपका आज्ञाकारी छात्र,\n{st_name}"
            st.text_area("Result:", app_txt, height=140)

# ----------------------------------------------------
# 3. महिला कॉर्नर (Women Corner)
# ----------------------------------------------------
with tab3:
    st.markdown(f"### {T['women_header']}")
    if CURR_LANG == "en":
        st.markdown("""
        <div class="guide-box">
            <b>🍲 Quick Healthy Suji Halwa Recipe (10 Mins):</b><br>
            • Roast 1 cup suji in 2 tbsp ghee until golden brown.<br>
            • Boil 2 cups water with sugar and cardamom.<br>
            • Slowly pour hot sugar syrup into the roasted suji, stir well, and serve hot!
        </div>
        <div class="guide-box">
            <b>📜 Lakhpati Didi Scheme:</b><br>
            Financial support and skill training for women in Self Help Groups (SHGs) to start micro-enterprises. Visit your local block development office to apply.
        </div>
        """, unsafe_allow_html=True)
    elif CURR_LANG == "ta":
        st.markdown("""
        <div class="guide-box">
            <b>🍲 10 நிமிட சுவையான ரவா கேசரி:</b><br>
            நெய்யில் ரவையை பொன்னிறமாக வறுத்து, கொதிக்கும் சர்க்கரை தண்ணீரைச் சேர்த்து கட்டி இல்லாமல் கிளறி ஏலக்காய் தூவினால் சுவையான கேசரி தயார்!
        </div>
        <div class="guide-box">
            <b>📜 லக்பதி தீதி திட்டம்:</b><br>
            சுயஉதவிக்குழுப் பெண்களுக்கு சுயதொழில் தொடங்க குறைந்த வட்டியில் நிதியுதவி மற்றும் பயிற்சி அளிக்கப்படுகிறது.
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="guide-box">
            <b>🍲 10 मिनट सूजी हलवा रेसिपी:</b><br>
            धीमी आँच पर सूजी को घी में सुनहरा भूनें। गरम चीनी-पानी धीरे-धीरे मिलाएँ और इलायची डालकर गरमा-गरम परोसें।
        </div>
        <div class="guide-box">
            <b>📜 लखपति दीदी योजना:</b><br>
            महिला स्वयं सहायता समूहों को आजीविका बढ़ाने हेतु बिना ब्याज या कम ब्याज पर वित्तीय सहायता और प्रशिक्षण दिया जाता है। ब्लॉक कार्यालय में संपर्क करें।
        </div>
        """, unsafe_allow_html=True)

# ----------------------------------------------------
# 4. बुज़ुर्ग सेवा (Seniors Care)
# ----------------------------------------------------
with tab4:
    st.markdown(f"### {T['seniors_header']}")
    if CURR_LANG == "en":
        st.markdown("""
        <div class="guide-box">
            <b>🏥 Ayushman Bharat Card (₹5 Lakh Free Treatment):</b><br>
            • Cashless treatment up to ₹5,00,000 per family per year across empaneled hospitals.<br>
            • <b>Documents Required:</b> Ration Card & Aadhaar Card.<br>
            • <b>Helpline:</b> Call 14555 toll-free.
        </div>
        <div class="guide-box">
            <b>👴 Old Age Pension Scheme:</b><br>
            • Monthly pension for citizens aged 60 and above.<br>
            • Apply online at your nearest CSC Center with Aadhaar, Bank Passbook, and Age Proof.
        </div>
        """, unsafe_allow_html=True)
    elif CURR_LANG == "ta":
        st.markdown("""
        <div class="guide-box">
            <b>🏥 ஆயுஷ்மான் பாரத் அட்டை (₹5 லட்சம் இலவச சிகிச்சை):</b><br>
            • குடும்பத்திற்கு ஆண்டுக்கு ₹5 லட்சம் வரை இலவச மருத்துவ சிகிச்சை.<br>
            • <b>தேவையான ஆவணங்கள்:</b> குடும்ப அட்டை மற்றும் ஆதார் அட்டை.<br>
            • <b>உதவி எண்:</b> 14555.
        </div>
        <div class="guide-box">
            <b>👴 முதியோர் ஓய்வூதியத் திட்டம்:</b><br>
            • 60 வயதுக்கு மேற்பட்ட மூத்த குடிமக்களுக்கு மாதாந்திர உதவித்தொகை. அருகில் உள்ள இ-சேவை மையத்தில் விண்ணப்பிக்கவும்.
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="guide-box">
            <b>🏥 आयुष्मान भारत योजना (₹5 लाख तक मुफ़्त इलाज):</b><br>
            • सभी सूचीबद्ध सरकारी और प्राइवेट अस्पतालों में प्रति वर्ष ₹5,00,000 तक का कैशलेस इलाज।<br>
            • <b>आवश्यक कागजात:</b> राशन कार्ड और आधार कार्ड।<br>
            • <b>टोल-फ्री हेल्पलाइन:</b> 14555 पर तुरंत कॉल करें।
        </div>
        <div class="guide-box">
            <b>👴 वृद्धावस्था पेंशन योजना:</b><br>
            • 60 वर्ष या अधिक उम्र के नागरिकों को मासिक आर्थिक सहायता।<br>
            • आधार कार्ड, बैंक पासबुक और आय प्रमाण पत्र के साथ नजदीकी जन सेवा केंद्र (CSC) से ऑनलाइन आवेदन करें।
        </div>
        """, unsafe_allow_html=True)

# ----------------------------------------------------
# 5. व्यापारी टूल्स (Business Tools)
# ----------------------------------------------------
with tab5:
    st.markdown(f"### {T['biz_header']}")
    b_shop = st.text_input("Shop Name / दुकान का नाम:", value="Sahil General Store")
    b_cust = st.text_input("Customer Name / ग्राहक का नाम:", value="Rahul Kumar")
    b_phone = st.text_input("Customer WhatsApp (10 digits):", value="9876543210")
    b_total = st.text_input("Total Amount (₹):", value="550")
    
    if st.button(T["bill_btn"]):
        clean_p = b_phone.strip()[-10:]
        if CURR_LANG == "en":
            bill_msg = f"🧾 *DIGITAL INVOICE*\nShop: {b_shop}\nCustomer: {b_cust}\nTotal Amount: ₹{b_total}\nStatus: Paid ✅\nThank you for visiting!"
        else:
            bill_msg = f"🧾 *डिजिटल बिल / CASH MEMO*\nदुकान: {b_shop}\nग्राहक: {b_cust}\nकुल रकम: ₹{b_total}\nस्थिति: भुगतान सफल ✅\nधन्यवाद! फिर पधारें।"
        
        wa_url = f"https://wa.me/91{clean_p}?text={urllib.parse.quote(bill_msg)}"
        st.markdown(f'<a href="{wa_url}" target="_blank" class="upi-pay-btn">👉 Open WhatsApp & Send Bill</a>', unsafe_allow_html=True)

# ----------------------------------------------------
# 👑 संस्थापक प्रोफाइल (100% सही WhatsApp नंबर के साथ)
# ----------------------------------------------------
st.markdown("---")
MY_WA = "917484878440[span_5](start_span)"[span_5](end_span)
founder_msg = urllib.parse.quote("नमस्ते साहिल जी, मैंने आपका Universal Bharat AI ऐप देखा।")
founder_link = f"https://wa.me/{MY_WA}?text={founder_msg}"

st.markdown(f"""
<div class="founder-card">
    <p style="color: #94A3B8 !important; font-size: 11px; margin: 0; text-transform: uppercase;">
        🏛️ FOUNDER & LEAD DEVELOPER
    </p>
    <h2 style="color: #38BDF8 !important; margin: 6px 0; font-size: 20px; font-weight: 800;">
        साहिल अहमद (Sahil Ahmad)
    </h2>
    <p style="color: #E2E8F0 !important; font-size: 12px; margin-bottom: 12px;">
        🇮🇳 डिजिटल भारत मिशन — देश के हर छात्र, बुज़ुर्ग, युवा व व्यापारी को डिजिटल शक्ति से जोड़ने की पहल।
    </p>
    <a href="{founder_link}" target="_blank" 
       style="background: linear-gradient(90deg, #10B981 0%, #059669 100%); color: #FFFFFF !important; padding: 10px 20px; border-radius: 8px; text-decoration: none; font-size: 13px; font-weight: bold; display: inline-block;">
        💬 सीधे WhatsApp (+91 {MY_WA[-10:]}) पर जुड़ें
    </a>
</div>
""", unsafe_allow_html=True)
