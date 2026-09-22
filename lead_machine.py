import streamlit as st
import streamlit.components.v1 as components
import requests
import urllib.parse
from datetime import datetime

# 1. पेज सेटअप
st.set_page_config(
    page_title="OmniCare AGI — Universal AI Customer Care Engine",
    page_icon="🎧",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# भाषा चयन
lang = st.radio("🌐 भाषा चुनें / Select Language:", ["🇮🇳 हिंदी (Hindi)", "🌍 English"], horizontal=True)

# डार्क थीम UI
st.markdown("""
<style>
    .stApp { background-color: #030712 !important; color: #F9FAFB !important; }
    label, p, span, h1, h2, h3, h4 { color: #F9FAFB !important; font-weight: 600 !important; }
    input, textarea, .stTextInput input, .stTextArea textarea, select {
        background-color: #111827 !important; color: #38BDF8 !important;
        font-weight: 600 !important; border: 1px solid #374151 !important; border-radius: 12px !important;
    }
    .care-hero {
        background: linear-gradient(135deg, #0284C7 0%, #2563EB 50%, #4F46E5 100%);
        padding: 22px; border-radius: 18px; text-align: center; margin-bottom: 18px;
        box-shadow: 0 10px 40px rgba(37, 99, 235, 0.4); border: 1px solid #38BDF8;
    }
    .care-card {
        background-color: #111827; border: 1px solid #1F2937; border-radius: 14px;
        padding: 16px; margin-bottom: 14px;
    }
    .pay-btn-glow {
        display: block; background: linear-gradient(90deg, #10B981 0%, #059669 100%);
        color: #FFFFFF !important; text-align: center; font-weight: 900; font-size: 16px;
        padding: 14px; border-radius: 12px; text-decoration: none; margin: 12px 0;
        box-shadow: 0 4px 25px rgba(16, 185, 129, 0.4);
    }
    div.stButton > button {
        background: linear-gradient(135deg, #0284C7 0%, #2563EB 100%) !important;
        color: #FFFFFF !important; border: none !important; border-radius: 12px !important;
        font-weight: 900 !important; font-size: 15px !important; width: 100% !important; padding: 14px !important;
    }
</style>
""", unsafe_allow_html=True)

MY_WA_NUMBER = "917484878440"
MY_UPI_ID = "7484878449-2@ybl"
today_date = datetime.now().strftime("%d-%m-%Y")

# हेडर बैनर
st.markdown("""
<div class="care-hero">
    <h2 style="color:#FFF; margin:0; font-size:22px;">🎧 OMNICARE AGI — यूनिवर्सल AI कस्टमर केयर इंजन</h2>
    <p style="color:#E0F2FE; font-size:13px; margin-top:6px;">Jio, टेलीकॉम, रिटेल और सर्विस कंपनियों के लिए 24/7 ऑटोमैटिक वॉयस सपोर्ट</p>
</div>
""", unsafe_allow_html=True)

tabs = st.tabs([
    "📞 1. AI कस्टमर केयर सिम्युलेटर",
    "⚡ 2. रियल फोन कॉल ट्रिगर (Vapi API)",
    "🎫 3. ऑटोमैटिक टिकट व WhatsApp रसीद",
    "👑 4. एंटरप्राइज केयर लाइसेंस"
])

# ----------------------------------------------------
# टैब 1: AI कस्टमर केयर सिम्युलेटर (ब्राउज़र स्पीकर से आवाज़)
# ----------------------------------------------------
with tabs[0]:
    st.markdown("### 📞 यूनिवर्सल AI केयर असिस्टेंट (लाइव ऑडियो टेस्ट)")
    st.caption("चुनें कि ग्राहक किस सेवा के लिए कॉल कर रहा है — AI सीधे इंसान की आवाज़ में समस्या सुनेगा और हल देगा:")
    
    care_department = st.selectbox("कस्टमर केयर विभाग चुनें:", [
        "📶 Jio / टेलीकॉम केयर (नेटवर्क, रिचार्ज व प्लान समस्या)",
        "🛍️ रिटेल व ई-कॉमर्स केयर (ऑर्डर ट्रैकिंग व रिफंड सपोर्ट)",
        "🚗 ऑटोमोबाइल व बाइक केयर (सर्विसिंग व रोड-साइड असिस्टेंस)",
        "🏥 हेल्थकेयर व क्लीनिक केयर (अपॉइंटमेंट व रिपोर्ट इंक्वायरी)"
    ])
    
    cust_name = st.text_input("ग्राहक का नाम:", value="साहिल अहमद")
    cust_phone = st.text_input("ग्राहक का मोबाइल नंबर:", value="7484878440")
    cust_issue = st.selectbox("ग्राहक की समस्या (Customer Issue):", [
        "इंटरनेट स्पीड बहुत धीमी है और कॉल ड्रॉप हो रही है",
        "मेरा पिछला रिचार्ज खत्म हो गया, नया बेस्ट प्लान बताइए",
        "मैंने सामान ऑर्डर किया था, अभी तक डिलीवरी नहीं मिली",
        "मुझे अपनी गाड़ी की सर्विस के लिए मैकेनिक स्लॉट बुक करना है"
    ])

    if st.button("🚀 कस्टमर केयर लाइव कॉल शुरू करें (Speaker Live)"):
        st.success("🟢 OmniCare वॉइस इंजन कनेक्ट हो गया! फोन का वॉल्यूम तेज रखें।")
        
        # विभाग के अनुसार AI का जवाब
        if "Jio" in care_department or "टेलीकॉम" in care_department:
            ai_dialogue = f"नमस्ते {cust_name} जी! Jio कस्टमर सपोर्ट में आपका स्वागत है। मैं आपकी AI असिस्टेंट बोल रही हूँ। मुझे दिख रहा है कि आप '{cust_issue}' के संबंध में परेशान हैं। चिंता मत कीजिए, मैंने आपके क्षेत्र के टावर का रिसेट सिग्नल भेज दिया है। अगले 15 मिनट में आपकी स्पीड 5G स्तर पर सामान्य हो जाएगी।"
        elif "रिटेल" in care_department:
            ai_dialogue = f"नमस्ते {cust_name} जी! रिटेल कस्टमर केयर में आपका स्वागत है। आपकी शिकायत दर्ज कर ली गई है। आपका पार्सल नज़दीकी हब पर पहुँच चुका है और आज शाम 5 बजे तक आपके पते पर डिलीवर हो जाएगा।"
        else:
            ai_dialogue = f"नमस्ते {cust_name} जी! कस्टमर केयर में आपका स्वागत है। आपकी अनुरोध संख्या दर्ज कर ली गई है और हमारे सीनियर एग्जीक्यूटिव का कन्फर्मेशन स्लॉट आपके WhatsApp पर भेज दिया गया है।"

        # सीधे फोन के स्पीकर से बुलवाने वाला जावास्क्रिप्ट कोड
        js_care_speech = f"""
        <script>
            var careMsg = new SpeechSynthesisUtterance();
            careMsg.text = "{ai_dialogue}";
            careMsg.lang = 'hi-IN';
            careMsg.rate = 0.95;
            careMsg.pitch = 1.0;
            window.speechSynthesis.cancel();
            window.speechSynthesis.speak(careMsg);
        </script>
        """
        components.html(js_care_speech, height=0)

        st.markdown(f"""
        <div class="care-card" style="border-left: 4px solid #10B981; margin-top:12px;">
            <p style="color:#10B981; font-weight:bold; margin-bottom:6px;">🎧 AI कस्टमर केयर एजेंट का जवाब (ऑडियो लाइव):</p>
            <p style="font-size:14px; color:#F9FAFB;">"{ai_dialogue}"</p>
        </div>
        """, unsafe_allow_html=True)

# ----------------------------------------------------
# टैब 2: रियल फोन कॉल ट्रिगर (Vapi API से मोबाइल पर रिंग)
# ----------------------------------------------------
with tabs[1]:
    st.markdown("### ⚡ असली मोबाइल पर कॉल भेजें (Production API)")
    st.caption("यदि आपके पास Vapi.ai की चाबी है, तो यहाँ सीधे नंबर डालकर असली रिंगटोन बजवा सकते हैं:")
    
    vapi_key_input = st.text_input("Vapi Private API Key:", type="password", placeholder="उदा: 4a2b-xxxx-xxxx")
    vapi_asst_input = st.text_input("Vapi Assistant ID:", placeholder="उदा: ast_991823xxxx")
    
    if st.button("📞 असली मोबाइल पर लाइव कॉल ट्रिगर करें"):
        clean_p = cust_phone.strip()
        if vapi_key_input.strip() and vapi_asst_input.strip() and len(clean_p) == 10:
            headers = {
                "Authorization": f"Bearer {vapi_key_input.strip()}",
                "Content-Type": "application/json"
            }
            body = {
                "assistantId": vapi_asst_input.strip(),
                "customer": {"number": f"+91{clean_p}"}
            }
            st.info("📡 टेलीकॉम नेटवर्क को सिग्नल भेजा जा रहा है...")
            try:
                res = requests.post("https://api.vapi.ai/call/phone", json=body, headers=headers)
                if res.status_code in [200, 201]:
                    st.success(f"🟢 कॉल कनेक्ट हो गई! +91 {clean_p} पर फोन चेक करें।")
                else:
                    st.error(f"कॉल एरर: {res.text}")
            except Exception as ex:
                st.error(f"नेटवर्क एरर: {ex}")
        else:
            st.warning("कृपया अपनी Vapi API Key, Assistant ID और 10 अंकों का फोन नंबर भरें।")

# ----------------------------------------------------
# टैब 3: ऑटोमैटिक टिकट व WhatsApp रसीद
# ----------------------------------------------------
with tabs[2]:
    st.markdown("### 🎫 कंप्लेंट टिकट व WhatsApp रसीद")
    ticket_id = f"TKT-{datetime.now().strftime('%Y%m%d%H%M')}"
    
    st.markdown(f"""
    <div class="care-card" style="border-left: 4px solid #38BDF8;">
        <h4 style="color:#38BDF8; margin:0;">ऑटोमैटिक कंप्लेंट टिकट संख्या: <b>{ticket_id}</b></h4>
        <p style="font-size:13px; color:#9CA3AF; margin-top:4px;">स्थिति: सक्रिय (In-Progress) | SLA: 2 घंटे के भीतर समाधान</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("📲 ग्राहक के WhatsApp पर टिकट रसीद भेजें"):
        wa_text = f"""नमस्ते {cust_name} जी! 🙏
OmniCare सपोर्ट में संपर्क करने के लिए धन्यवाद।

🎫 **कंप्लेंट टिकट संख्या:** {ticket_id}
📌 **दर्ज समस्या:** {cust_issue}
⚡ **स्थिति:** हमारी AI टीम ने समाधान शुरू कर दिया है। 2 घंटे में आपका काम पूरा हो जाएगा।

धन्यवाद!"""
        enc_wa = urllib.parse.quote(wa_text)
        st.markdown(f'<a href="https://wa.me/91{cust_phone}?text={enc_wa}" target="_blank" class="pay-btn-glow">📲 Open WhatsApp & Send Complaint Receipt</a>', unsafe_allow_html=True)

# ----------------------------------------------------
# टैब 4: एंटरप्राइज केयर लाइसेंस (₹1,00,000)
# ----------------------------------------------------
with tabs[3]:
    st.markdown("### 👑 Enterprise OmniCare Architecture License")
    st.markdown("""
    <div class="care-card" style="border-left: 4px solid #F59E0B;">
        <h3 style="color:#F59E0B; margin:0;">फुल कस्टमर केयर ऑटोमेशन सूट</h3>
        <p style="font-size:14px; color:#F8FAFC; margin:8px 0;">
            • 50 टेलीकॉलर्स की जगह अकेला AI एजेंट<br>
            • 24/7 ऑटोमैटिक कॉल हैंडलिंग (Hindi / English / Tamil / Regional)<br>
            • ऑटोमैटिक CRM टिकट व WhatsApp डिलीवरी
        </p>
        <p style="font-size:18px; color:#38BDF8; font-weight:bold; margin:0;">One-Time Deployment: ₹1,00,000</p>
    </div>
    """, unsafe_allow_html=True)

    token_val = "10000"
    upi_care = f"upi://pay?pa={MY_UPI_ID}&pn=OmniCare%20Enterprise&am={token_val}&cu=INR&tn=Care%20Token"
    qr_care = f"https://api.qrserver.com/v1/create-qr-code/?size=180x180&data={urllib.parse.quote(upi_care)}"

    st.markdown(f"""
    <div class="care-card" style="text-align: center;">
        <p style="color: #38BDF8 !important; font-weight: bold;">📲 Pay ₹10,000 Advance Token (GPay / PhonePe):</p>
        <img src="{qr_care}" width="165" style="background:#fff; padding:6px; border-radius:12px; border:2px solid #2563EB;" />
        <p style="font-size:12px; color:#9CA3AF; margin-top:6px;">UPI ID: <b>{MY_UPI_ID}</b></p>
    </div>
    """, unsafe_allow_html=True)

# संस्थापक प्रोफ़ाइल
st.markdown("---")
st.markdown(f"""
<div class="care-card" style="text-align: center; border: 2px solid #38BDF8;">
    <p style="color:#38BDF8; font-size:11px; margin:0; letter-spacing:2px;">🏛️ FOUNDER & CHIEF ARCHITECT</p>
    <h2 style="color:#FFF; margin:6px 0; font-size:22px;">साहिल अहमद (Sahil Ahmad)</h2>
    <p style="color:#CBD5E1; font-size:13px; margin-bottom:12px;">OmniCare AGI — Engineering Enterprise AI Support Engines</p>
    <a href="https://wa.me/{MY_WA_NUMBER}" target="_blank" style="background:#10B981; color:#fff; padding:10px 22px; border-radius:8px; text-decoration:none; font-weight:bold; font-size:13px; display:inline-block;">💬 Connect on WhatsApp (+91 {MY_WA_NUMBER[-10:]})</a>
</div>
""", unsafe_allow_html=True)
        
