import streamlit as st
import urllib.parse
from datetime import datetime

# Enterprise App Config
st.set_page_config(
    page_title="Nexus Core AGI — Autonomous AI Calling & Sales Engine",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Language Selector
lang = st.radio("🌐 Bhasha Chunein / Select Language:", ["🇮🇳 Hindi", "🌍 English"], horizontal=True)

# High-Tech Cyber Enterprise UI
st.markdown("""
<style>
    .stApp {
        background-color: #030712 !important;
        color: #F9FAFB !important;
    }
    label, p, span, h1, h2, h3, h4 {
        color: #F9FAFB !important;
        font-weight: 600 !important;
    }
    input, textarea, .stTextInput input, .stTextArea textarea, select {
        background-color: #111827 !important;
        color: #38BDF8 !important;
        font-weight: 600 !important;
        font-size: 15px !important;
        border: 1px solid #374151 !important;
        border-radius: 12px !important;
    }
    .god-banner {
        background: linear-gradient(135deg, #4F46E5 0%, #7C3AED 50%, #06B6D4 100%);
        padding: 24px;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 10px 40px rgba(124, 58, 237, 0.45);
        border: 1px solid #818CF8;
    }
    .god-banner h2 {
        color: #FFFFFF !important;
        font-size: 22px !important;
        margin: 0 !important;
        font-weight: 900 !important;
    }
    .god-banner p {
        color: #EDE9FE !important;
        font-size: 13px !important;
        margin-top: 6px !important;
    }
    .feature-card {
        background-color: #111827;
        border: 1px solid #1F2937;
        border-radius: 14px;
        padding: 18px;
        margin-bottom: 14px;
    }
    .pay-btn-glow {
        display: block;
        background: linear-gradient(90deg, #10B981 0%, #059669 100%);
        color: #FFFFFF !important;
        text-align: center;
        font-weight: 900;
        font-size: 16px;
        padding: 14px;
        border-radius: 12px;
        text-decoration: none;
        margin: 12px 0;
        box-shadow: 0 4px 25px rgba(16, 185, 129, 0.4);
    }
    .founder-box {
        background: linear-gradient(135deg, #111827 0%, #030712 100%);
        border: 2px solid #8B5CF6;
        border-radius: 18px;
        padding: 20px;
        text-align: center;
        margin-top: 30px;
        margin-bottom: 20px;
        box-shadow: 0 8px 30px rgba(139, 92, 246, 0.25);
    }
    div.stButton > button {
        background: linear-gradient(135deg, #4F46E5 0%, #7C3AED 100%) !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 12px !important;
        font-weight: 900 !important;
        font-size: 15px !important;
        width: 100% !important;
        padding: 14px !important;
    }
</style>
""", unsafe_allow_html=True)

MY_WA_NUMBER = "917484878440"
MY_UPI_ID = "7484878449-2@ybl"

if "Hindi" in lang:
    st.markdown("""
    <div class="god-banner">
        <h2>⚡ NEXUS CORE AGI — ऑटोनॉमस AI कॉलिंग व सेल्स इंजन</h2>
        <p>असली इंसानी आवाज़ में कॉलिंग • 24/7 ऑटो-क्लोजर • 5 कर्मचारियों का काम 1 सेकंड में</p>
    </div>
    """, unsafe_allow_html=True)
    tabs = st.tabs([
        "📞 1. AI वॉयस कॉल सिम्युलेटर",
        "🧠 2. लाइव ऑब्जेक्शन किलर AI",
        "👑 3. ₹50,000 एंटरप्राइज लाइसेंस"
    ])
else:
    st.markdown("""
    <div class="god-banner">
        <h2>⚡ NEXUS CORE AGI — Autonomous AI Voice & Sales Engine</h2>
        <p>Human-Like Autonomous Calling • 24/7 Closer • Replaces 5 Staff Instantly</p>
    </div>
    """, unsafe_allow_html=True)
    tabs = st.tabs([
        "📞 1. AI Voice Call Simulator",
        "🧠 2. Live Objection Killer AI",
        "👑 3. ₹50,000 Enterprise License"
    ])

# ----------------------------------------------------
# 1. 📞 AI VOICE CALL SIMULATOR
# ----------------------------------------------------
with tabs[0]:
    if "Hindi" in lang:
        st.markdown("### 📞 लाइव AI वॉयस कॉल ट्रिगर टेस्ट")
        st.caption("क्लाइंट को हैरान करने वाला डेमो: नंबर डालते ही 1 सेकंड में AI कॉलिंग स्क्रिप्ट और रिस्पॉन्स तैयार:")
        c_biz = st.selectbox("इंडस्ट्री चुनें:", [
            "🏢 रियल एस्टेट बिल्डर (Property Sales)",
            "🏥 सुपर स्पेशियलिटी हॉस्पिटल / क्लीनिक",
            "🚗 लक्ज़री कार शोरूम व डीलरशिप",
            "🎓 प्रीमियम कोचिंग संस्थान / यूनिवर्सिटी"
        ])
        c_name = st.text_input("क्लाइंट / कस्टमर का नाम:", placeholder="उदा: विक्रम सिंघानिया")
        c_num = st.text_input("मोबाइल नंबर (10 अंक):", placeholder="उदा: 9876543210")
        btn_call = "🚀 AI कॉल ट्रिगर करें (Live Simulation)"
    else:
        st.markdown("### 📞 Live AI Autonomous Calling Simulator")
        st.caption("High-impact demo: Enter lead details to simulate real human-sounding AI calling:")
        c_biz = st.selectbox("Select Industry:", [
            "🏢 Real Estate Developer (Luxury Villas & Flats)",
            "🏥 Super-Speciality Hospital & Clinic",
            "🚗 Luxury Automobile Dealership",
            "🎓 EdTech & Premium Coaching Institute"
        ])
        c_name = st.text_input("Lead / Client Name:", placeholder="e.g. Vikram Singhania")
        c_num = st.text_input("Mobile Number (10 digits):", placeholder="e.g. 9876543210")
        btn_call = "🚀 Trigger Autonomous AI Call Simulation"

    if st.button(btn_call):
        cn = c_name.strip() if c_name.strip() else "Sir/Ma'am"
        st.success("✅ AI Autonomous Telecaller Initialized! Voice Packet Routing Successful.")
        
        sim_audio_script = f"""==================================================
🤖 [AUTONOMOUS AI VOICE CALL TRANSCRIPT - 0.4s LATENCY]
Caller: Nexus Autonomous Voice Agent (Hindi/English Neural Voice)
Recipient: {cn} ({c_biz.split('(')[0]})
Status: CONNECTED 🟢
==================================================

[00:01 - AI Voice]: "नमस्ते {cn} जी! मैं {c_biz.split('(')[0]} से बात कर रही हूँ। आपने हमारे नए प्रोजेक्ट/ऑफर के बारे में इन्क्वायरी की थी। क्या यह आपसे 2 मिनट बात करने का सही समय है?"

[Customer]: "हाँ, बताइए क्या डिटेल्स हैं?"

[00:08 - AI Voice]: "सर, हमारे पास प्राइम लोकेशन पर लिमिटेड इन्वेंटरी बची है जिसमें शुरुआती 5 ग्राहकों के लिए एक्सक्लूसिव 10% इंसेंटिव डिस्काउंट है। क्या मैं आज शाम 4 बजे आपके लिए सीनियर डायरेक्टर के साथ एक प्राइवेट स्लॉट रिजर्व कर दूँ?"

[Customer]: "मुझे लोकेशन और ब्रोशर WhatsApp पर चाहिए।"

[00:18 - AI Voice]: "बिल्कुल सर! कॉल कट होते ही 2 सेकंड में आपके WhatsApp नंबर पर ऑफिशियल ब्रोशर और लोकेशन पहुंच रही है। आपका दिन शुभ हो!"
=================================================="""
        st.text_area("Live Audio Call Engine Output:", sim_audio_script, height=250)
        st.info("💡 क्लाइंट को समझाएं: यह सिस्टम एक दिन में 10,000 ग्राहकों को कॉल करके ऑटोमैटिकली अपॉइंटमेंट लॉक करता है।")

# ----------------------------------------------------
# 2. 🧠 LIVE OBJECTION KILLER AI
# ----------------------------------------------------
with tabs[1]:
    if "Hindi" in lang:
        st.markdown("### 🧠 रियल-टाइम AI ऑब्जेक्शन हैंडलर")
        st.caption("कस्टमर कॉल पर जो भी बहाना बनाएगा, AI 1 सेकंड में उसे क्लोजिंग तर्क देगा:")
        obj_type = st.selectbox("कस्टमर का बहाना / ऑब्जेक्शन चुनें:", [
            "💸 'आपका प्राइस बहुत ज़्यादा है, डिस्काउंट दीजिए'",
            "⏳ 'मैं 15 दिन बाद सोचकर बताऊंगा'",
            "🏢 'दूसरी कंपनी इससे सस्ता दे रही है'",
            "📞 'मुझे अभी बात नहीं करनी, बाद में कॉल करो'"
        ])
        btn_obj = "⚡ AI क्लोजिंग तर्क जनरेट करें"
    else:
        st.markdown("### 🧠 Real-Time Autonomous Objection Closer")
        st.caption("Instant neural response for difficult customer objections:")
        obj_type = st.selectbox("Select Customer Objection:", [
            "💸 'Your pricing is too expensive, give more discount'",
            "⏳ 'I will think about it and tell you after 2 weeks'",
            "🏢 'Your competitor is offering a cheaper alternative'",
            "📞 'I am busy right now, don't call me'"
        ])
        btn_obj = "⚡ Generate Autonomous Closing Response"

    if st.button(btn_obj):
        if "प्राइस" in obj_type or "expensive" in obj_type:
            resp_txt = "AI Response: 'सर, मैं आपकी बात समझती हूँ। लेकिन सस्ता विकल्प लेने के बाद 80% लोगों को बार-बार मेंटेनेंस में दोगुना पैसा लगाना पड़ता है। हमारा सिस्टम पहली बार में ही 100% गारंटी देता है। क्या आप लंबे समय की शांति चाहते हैं या सस्ता समझौता?'"
        elif "सोचकर" in obj_type or "think" in obj_type:
            resp_txt = "AI Response: 'बिल्कुल सर, सोचना आपका हक है। लेकिन जो स्पेशल डिस्काउंट और स्लॉट आज उपलब्ध है, वह कल शाम 5 बजे एक्सपायर हो जाएगा। क्या मैं सिर्फ ₹1,000 से आपका स्लॉट होल्ड कर दूँ ताकि आपका नुकसान न हो?'"
        else:
            resp_txt = "AI Response: 'सर, मैं सिर्फ 30 सेकंड में सबसे महत्वपूर्ण पॉइंट शेयर कर देती हूँ ताकि आपका कीमती समय बचे और आपको सही निर्णय लेने में मदद मिले।' "
        
        st.markdown(f"""
        <div class="feature-card" style="border-left: 4px solid #10B981;">
            <h4 style="color:#10B981; margin:0;">🎯 AI न्यूरल क्लोजिंग रिस्पॉन्स:</h4>
            <p style="margin:10px 0; font-size:15px; color:#F8FAFC;">{resp_txt}</p>
        </div>
        """, unsafe_allow_html=True)

# ----------------------------------------------------
# 3. 👑 ₹50,000 ENTERPRISE LICENSE
# ----------------------------------------------------
with tabs[2]:
    st.markdown("### 👑 Enterprise Autonomous AI Retainer")
    st.markdown("""
    <div class="feature-card" style="border-left: 4px solid #F59E0B;">
        <h3 style="color:#F59E0B; margin:0;">Full Autonomous Enterprise Suite</h3>
        <p style="font-size:14px; color:#F8FAFC; margin:8px 0;">
            • Dedicated Autonomous AI Calling Bot (10,000 calls/month)<br>
            • Custom Neural Voice (Hindi / English / Tamil / Regional)<br>
            • Instant CRM & WhatsApp Auto-Booking Integration
        </p>
        <p style="font-size:18px; color:#38BDF8; font-weight:bold; margin:0;">
            One-Time Deployment: ₹50,000 | Monthly Retainer: ₹15,000
        </p>
    </div>
    """, unsafe_allow_html=True)

    token_amount = "5000"
    upi_ent = f"upi://pay?pa={MY_UPI_ID}&pn=Nexus%20Enterprise&am={token_amount}&cu=INR&tn=Enterprise%20Token"
    qr_ent = f"https://api.qrserver.com/v1/create-qr-code/?size=180x180&data={urllib.parse.quote(upi_ent)}"

    st.markdown(f"""
    <div class="feature-card" style="text-align: center;">
        <p style="color: #38BDF8 !important; font-weight: bold; margin-bottom: 8px;">📲 Pay ₹5,000 Advance Token for Architecture Setup:</p>
        <img src="{qr_ent}" width="165" style="background: #fff; padding: 6px; border-radius: 12px; border: 2px solid #8B5CF6;" />
        <p style="font-size: 12px; color: #9CA3AF !important; margin-top: 6px;">UPI ID: <b>{MY_UPI_ID}</b></p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f'<a href="{upi_ent}" class="pay-btn-glow">⚡ Pay ₹{token_amount} Advance Token</a>', unsafe_allow_html=True)

# FOUNDER PROFILE
st.markdown("---")
wa_founder = f"https://wa.me/{MY_WA_NUMBER}?text={urllib.parse.quote('Hello Sahil, I want to deploy the Autonomous AI Voice Engine for our business.')}"
st.markdown(f"""
<div class="founder-box">
    <p style="color: #A78BFA !important; font-size: 11px; margin: 0; text-transform: uppercase; letter-spacing: 2px;">
        🏛️ FOUNDER & AI ARCHITECT
    </p>
    <h2 style="color: #FFFFFF !important; margin: 8px 0; font-size: 22px; font-weight: 900;">
        साहिल अहमद (Sahil Ahmad)
    </h2>
    <p style="color: #D1D5DB !important; font-size: 13px; margin-bottom: 14px;">
        Nexus Core AGI — Engineering enterprise autonomous voice bots and high-ticket AI growth architectures.
    </p>
    <a href="{wa_founder}" target="_blank" 
       style="background: linear-gradient(90deg, #10B981 0%, #059669 100%); color: #FFFFFF !important; padding: 12px 24px; border-radius: 10px; text-decoration: none; font-size: 13px; font-weight: bold; display: inline-block;">
        💬 Schedule Enterprise Strategy Call (+91 {MY_WA_NUMBER[-10:]})
    </a>
</div>
""", unsafe_allow_html=True)
        
