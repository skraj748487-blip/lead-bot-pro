import streamlit as st
import urllib.parse
from datetime import datetime

# 1. एजेंसी कॉन्फ़िगरेशन
st.set_page_config(
    page_title="GrowthCore AI — 3-in-1 Business Growth OS",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. भाषा चयन (Language Switcher)
lang = st.radio("🌐 भाषा चुनें / Select Language:", ["🇮🇳 हिंदी", "🌍 English"], horizontal=True)

# 3. डार्क साइबर UI
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
    .main-banner {
        background: linear-gradient(135deg, #0EA5E9 0%, #2563EB 50%, #4F46E5 100%);
        padding: 22px;
        border-radius: 18px;
        text-align: center;
        margin-bottom: 16px;
        box-shadow: 0 10px 40px rgba(37, 99, 235, 0.35);
        border: 1px solid #38BDF8;
    }
    .main-banner h2 {
        color: #FFFFFF !important;
        font-size: 22px !important;
        margin: 0 !important;
        font-weight: 900 !important;
    }
    .main-banner p {
        color: #E0F2FE !important;
        font-size: 13px !important;
        margin-top: 6px !important;
        margin-bottom: 0 !important;
    }
    .real-card {
        background-color: #0F172A;
        border: 1px solid #1E293B;
        border-radius: 14px;
        padding: 16px;
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
    .founder-card {
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
        background: linear-gradient(135deg, #0EA5E9 0%, #2563EB 100%) !important;
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

MY_WA_NUMBER = "917484878440"
MY_UPI_ID = "7484878449-2@ybl"
today_date = datetime.now().strftime("%d-%m-%Y")

# हेडर बैनर
if "हिंदी" in lang:
    st.markdown("""
    <div class="main-banner">
        <h2>⚡ GROWTHCORE — 3-IN-1 बिज़नेस ग्रोथ इंजन</h2>
        <p>Google Maps 5-स्टार रैंकिंग • वायरल रील्स स्क्रिप्ट • 1-क्लिक रिव्यू बूस्टर</p>
    </div>
    """, unsafe_allow_html=True)
    tabs = st.tabs([
        "⭐ Google Maps रिव्यू इंजन",
        "📲 WhatsApp रिव्यू बूस्टर",
        "🎬 AI वायरल रील्स स्क्रिप्ट",
        "👑 ₹30,000 एजेंसी बुकिंग"
    ])
else:
    st.markdown("""
    <div class="main-banner">
        <h2>⚡ GROWTHCORE — 3-IN-1 BUSINESS GROWTH ENGINE</h2>
        <p>Google Maps 5-Star Booster • Viral Reels Generator • Instant Review Automator</p>
    </div>
    """, unsafe_allow_html=True)
    tabs = st.tabs([
        "⭐ Google Maps Review Engine",
        "📲 WhatsApp Review Automator",
        "🎬 AI Viral Reels Generator",
        "👑 ₹30,000 Agency Retainer"
    ])

# ----------------------------------------------------
# 1. ⭐ Google Maps Review Engine
# ----------------------------------------------------
with tabs[0]:
    if "हिंदी" in lang:
        st.markdown("### ⭐ Google Maps 5-स्टार रिव्यू और रैंकिंग बूस्टर")
        st.caption("क्लाइंट का Google Maps लिंक या दुकान का नाम डालें — सिस्टम तुरंत असली स्कैनिंग QR बना देगा:")
        b_name_map = st.text_input("दुकान / कंपनी का नाम:", placeholder="उदा: पटना ऑटोमोटिव केयर")
        map_link = st.text_input("Google Maps Review लिंक (या दुकान का नाम व शहर):", placeholder="उदा: https://maps.app.goo.gl/xyz123")
        btn_qr = "🚀 असली Review QR कोड जनरेट करें"
    else:
        st.markdown("### ⭐ Google Maps 5-Star Review Booster")
        st.caption("Enter client's shop name or Maps link to generate an instant review QR code:")
        b_name_map = st.text_input("Business / Shop Name:", placeholder="e.g. Coimbatore Car Care")
        map_link = st.text_input("Google Maps Link (or Shop Name with City):", placeholder="e.g. https://maps.app.goo.gl/xyz123")
        btn_qr = "🚀 Generate Instant Review QR Code"

    if st.button(btn_qr):
        target_link = map_link.strip() if map_link.strip() else f"https://www.google.com/search?q={urllib.parse.quote(b_name_map + ' reviews')}"
        qr_gen_url = f"https://api.qrserver.com/v1/create-qr-code/?size=220x220&data={urllib.parse.quote(target_link)}"

        st.markdown(f"""
        <div class="real-card" style="text-align: center; border-left: 4px solid #F59E0B;">
            <p style="color: #F59E0B; font-size: 15px; font-weight: bold; margin-bottom: 8px;">
                📲 {b_name_map if b_name_map else 'Your Business'} 5-Star Review QR
            </p>
            <img src="{qr_gen_url}" width="180" style="background:#fff; padding:8px; border-radius:12px; border:2px solid #F59E0B;" />
            <p style="color:#94A3B8; font-size:12px; margin-top:8px;">
                {'ग्राहक इसे स्कैन करते ही सीधे 5-स्टार रिव्यू पेज पर पहुँचेगा।' if 'हिंदी' in lang else 'Customers can scan this to leave an instant 5-star Google review.'}
            </p>
        </div>
        """, unsafe_allow_html=True)

# ----------------------------------------------------
# 2. 📲 WhatsApp Review Automator
# ----------------------------------------------------
with tabs[1]:
    if "हिंदी" in lang:
        st.markdown("### 📲 ग्राहक के WhatsApp पर डायरेक्ट 5-स्टार रिव्यू रिक्वेस्ट भेजें")
        st.caption("बिलिंग के बाद ग्राहक को 1-क्लिक में रिव्यू लिंक भेजें ताकि वह घर जाकर भी 5-स्टार दे:")
        wa_cname = st.text_input("ग्राहक का नाम:", placeholder="उदा: अमित कुमार")
        wa_cphone = st.text_input("ग्राहक का WhatsApp नंबर (10 अंक):", placeholder="उदा: 9876543210")
        wa_bname = st.text_input("आपकी दुकान का नाम:", placeholder="उदा: रॉयल गैरेज")
        wa_link = st.text_input("Google Review लिंक:", placeholder="https://maps.app.goo.gl/...")
        btn_wa_rev = "⚡ WhatsApp पर रिव्यू मैसेज भेजें"
    else:
        st.markdown("### 📲 Send 1-Click WhatsApp Review Requests")
        st.caption("Send instant automated review requests to customers right after their visit:")
        wa_cname = st.text_input("Customer Name:", placeholder="e.g. John Doe")
        wa_cphone = st.text_input("Customer WhatsApp Number (10 digits):", placeholder="e.g. 9876543210")
        wa_bname = st.text_input("Your Business Name:", placeholder="e.g. Coimbatore Motors")
        wa_link = st.text_input("Google Maps Review Link:", placeholder="https://maps.app.goo.gl/...")
        btn_wa_rev = "⚡ Send Review Request on WhatsApp"

    if st.button(btn_wa_rev):
        cn = wa_cname.strip() if wa_cname.strip() else "Valued Customer"
        bn = wa_bname.strip() if wa_bname.strip() else "Our Store"
        rl = wa_link.strip() if wa_link.strip() else "https://google.com"
        cp = wa_cphone.strip() if len(wa_cphone.strip()) == 10 else MY_WA_NUMBER

        if "हिंदी" in lang:
            req_msg = f"नमस्ते {cn} जी! {bn} में आने के लिए हार्दिक धन्यवाद। 🙏\n\nयदि आपको हमारी सेवा पसंद आई, तो कृपया नीचे दिए गए लिंक पर 5 सेकंड निकालकर हमें Google पर 5-Star रेटिंग दें। आपका एक रिव्यू हमारे लिए बहुत महत्वपूर्ण है:\n👉 {rl}\n\nधन्यवाद!"
        else:
            req_msg = f"Hello {cn}! Thank you for visiting {bn}. 🙏\n\nIf you enjoyed our service, please take 5 seconds to support us with a 5-Star rating on Google:\n👉 {rl}\n\nWe appreciate your support!"

        enc_req = urllib.parse.quote(req_msg)
        wa_fire_url = f"https://wa.me/91{cp}?text={enc_req}"
        st.markdown(f'<a href="{wa_fire_url}" target="_blank" class="pay-btn-main" style="background:#25D366;">📲 Open WhatsApp & Send Request</a>', unsafe_allow_html=True)

# ----------------------------------------------------
# 3. 🎬 AI Viral Reels Generator
# ----------------------------------------------------
with tabs[2]:
    if "हिंदी" in lang:
        st.markdown("### 🎬 AI वायरल रील्स व शॉर्ट्स स्क्रिप्ट इंजन")
        biz_cat = st.selectbox("बिज़नेस कैटेगरी:", ["🚗 कार रिपेयर / ऑटो गैरेज", "🏋️ जिम व फिटनेस सेंटर", "🏥 डेंटल व स्किन क्लीनिक", "🏢 रियल एस्टेट", "🛍️ रिटेल स्टोर"])
        reel_topic = st.text_input("वीडियो टॉपिक:", placeholder="उदा: 20% माइलेज बढ़ाने का तरीका")
        btn_reel = "🔥 30-सेकंड वायरल रील तैयार करें"
    else:
        st.markdown("### 🎬 AI Viral Reels & Shorts Engine")
        biz_cat = st.selectbox("Business Category:", ["🚗 Automobile & Garage", "🏋️ Gym & Fitness Center", "🏥 Dental & Skin Clinic", "🏢 Real Estate & Property", "🛍️ Retail & Fashion"])
        reel_topic = st.text_input("Video Topic:", placeholder="e.g. 3 Tips to save 20% fuel")
        btn_reel = "🔥 Generate 30-Second Viral Script"

    if st.button(btn_reel):
        t_clean = reel_topic.strip() if reel_topic.strip() else "Best Special Offer"
        r_script = f"""==================================================
🎬 30-SECOND VIRAL REEL BLUEPRINT
CATEGORY: {biz_cat}
TOPIC: {t_clean}
==================================================

[00:00 - 00:03] 🔥 HOOK (Fast cut visual):
"Stop making this huge mistake with your {biz_cat.split(' ')[1]}! Watch this till the end."

[00:03 - 00:15] 💡 THE SOLUTION (B-roll footage):
"Most people ignore this simple step. Here is how you solve {t_clean} in 5 minutes..."

[00:15 - 00:25] ⚡ PROOF & OFFER:
"Visit our store this week and get an exclusive 15% discount on your first appointment."

[00:25 - 00:30] 🚀 CALL TO ACTION:
"Click the link in our bio or WhatsApp us directly right now!"
=================================================="""
        st.text_area("Reel Script:", r_script, height=220)
        st.download_button("📥 Download Script (TXT)", data=r_script, file_name="Reel_Script.txt", mime="text/plain", use_container_width=True)

# ----------------------------------------------------
# 4. 👑 ₹30,000 Agency Booking
# ----------------------------------------------------
with tabs[3]:
    st.markdown("### 👑 GrowthCore Commercial Agency Retainer")
    st.markdown("""
    <div class="real-card" style="border-left: 4px solid #10B981;">
        <h3 style="color:#10B981; margin:0;">Complete 3-in-1 Business Growth Retainer</h3>
        <p style="font-size:14px; color:#F8FAFC; margin:8px 0;">
            • Google Maps Top-3 Ranking System<br>
            • 25 AI Viral Reels Scripts & Content Plan / month<br>
            • 1-Click WhatsApp Review Automator
        </p>
        <p style="font-size:16px; color:#38BDF8; font-weight:bold; margin:0;">Monthly Retainer: ₹30,000 / $360 USD</p>
    </div>
    """, unsafe_allow_html=True)

    token_amt = "1500"
    upi_engine = f"upi://pay?pa={MY_UPI_ID}&pn=GrowthCore%20Agency&am={token_amt}&cu=INR&tn=Retainer%20Booking"
    qr_engine_img = f"https://api.qrserver.com/v1/create-qr-code/?size=180x180&data={urllib.parse.quote(upi_engine)}"

    st.markdown(f"""
    <div class="real-card" style="text-align: center;">
        <p style="color: #38BDF8 !important; font-weight: bold; margin-bottom: 8px;">📲 Pay ₹1,500 Advance Token (PhonePe / GPay):</p>
        <img src="{qr_engine_img}" width="165" style="background: #fff; padding: 6px; border-radius: 12px; border: 2px solid #2563EB;" />
        <p style="font-size: 12px; color: #94A3B8 !important; margin-top: 6px;">UPI ID: <b>{MY_UPI_ID}</b></p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f'<a href="{upi_engine}" class="pay-btn-main">⚡ Pay ₹{token_amt} Token Now</a>', unsafe_allow_html=True)

# संस्थापक प्रोफाइल
st.markdown("---")
wa_founder_link = f"https://wa.me/{MY_WA_NUMBER}?text={urllib.parse.quote('Hello Sahil, I want to deploy GrowthCore 3-in-1 Engine for my business.')}"
st.markdown(f"""
<div class="founder-card">
    <p style="color: #38BDF8 !important; font-size: 11px; margin: 0; text-transform: uppercase; letter-spacing: 2px;">
        🏛️ FOUNDER & MANAGING DIRECTOR
    </p>
    <h2 style="color: #FFFFFF !important; margin: 8px 0; font-size: 22px; font-weight: 900;">
        साहिल अहमद (Sahil Ahmad)
    </h2>
    <p style="color: #CBD5E1 !important; font-size: 13px; margin-bottom: 14px;">
        ⚡ GrowthCore AI — Engineered to scale local businesses with Google Maps, AI Reels, and Automation.
    </p>
    <a href="{wa_founder_link}" target="_blank" 
       style="background: linear-gradient(90deg, #10B981 0%, #059669 100%); color: #FFFFFF !important; padding: 12px 24px; border-radius: 10px; text-decoration: none; font-size: 13px; font-weight: bold; display: inline-block;">
        💬 Connect on WhatsApp (+91 {MY_WA_NUMBER[-10:]})
    </a>
</div>
""", unsafe_allow_html=True)
        
