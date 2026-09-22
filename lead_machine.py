import streamlit as st
import streamlit.components.v1 as components
import urllib.parse
from datetime import datetime

# 1. पेज कॉन्फ़िगरेशन
st.set_page_config(
    page_title="OmniCare AGI — Autonomous Enterprise Engine",
    page_icon="🎧",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# भाषा चयन
lang = st.radio("🌐 भाषा चुनें / Select Language:", ["🇮🇳 हिंदी (Hindi)", "🌍 English"], horizontal=True)

# 2. डार्क एंटरप्राइज थीम
st.markdown("""
<style>
    .stApp { background-color: #030712 !important; color: #F9FAFB !important; }
    label, p, span, h1, h2, h3, h4 { color: #F9FAFB !important; font-weight: 600 !important; }
    input, textarea, .stTextInput input, .stTextArea textarea, select {
        background-color: #111827 !important; color: #38BDF8 !important;
        font-weight: 600 !important; border: 1px solid #374151 !important; border-radius: 12px !important;
    }
    .omni-banner {
        background: linear-gradient(135deg, #0284C7 0%, #2563EB 50%, #4F46E5 100%);
        padding: 22px; border-radius: 18px; text-align: center; margin-bottom: 18px;
        box-shadow: 0 10px 40px rgba(37, 99, 235, 0.4); border: 1px solid #38BDF8;
    }
    .card-block {
        background-color: #111827; border: 1px solid #1F2937; border-radius: 14px;
        padding: 16px; margin-bottom: 14px;
    }
    .pay-btn-glow {
        display: block; background: linear-gradient(90deg, #10B981 0%, #059669 100%);
        color: #FFFFFF !important; text-align: center; font-weight: 900; font-size: 15px;
        padding: 13px; border-radius: 10px; text-decoration: none; margin: 10px 0;
        box-shadow: 0 4px 20px rgba(16, 185, 129, 0.4);
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
<div class="omni-banner">
    <h2 style="color:#FFF; margin:0; font-size:22px;">🎧 OMNICARE AGI — यूनिवर्सल AI कस्टमर केयर इंजन</h2>
    <p style="color:#E0F2FE; font-size:13px; margin-top:6px;">Jio, टेलीकॉम, रिटेल और सर्विस कंपनियों के लिए 24/7 ऑटोमैटिक वॉयस सपोर्ट</p>
</div>
""", unsafe_allow_html=True)

tabs = st.tabs([
    "📞 1. AI कस्टमर केयर सिम्युलेटर",
    "🎫 2. ऑटोमैटिक टिकट व WhatsApp रसीद",
    "👑 3. एंटरप्राइज केयर लाइसेंस"
])

# ----------------------------------------------------
# टैब 1: AI कस्टमर केयर सिम्युलेटर
# ----------------------------------------------------
with tabs[0]:
    st.markdown("### 📞 यूनिवर्सल AI केयर असिस्टेंट (लाइव ऑडियो टेस्ट)")
    st.caption("चुनें कि ग्राहक किस सेवा के लिए कॉल कर रहा है — AI सीधे महिला आवाज़ में समाधान सुनाएगा:")

    care_dept = st.selectbox("कस्टमर केयर विभाग चुनें:", [
        "📶 Jio / टेलीकॉम केयर (नेटवर्क, रिचार्ज व प्लान समस्या)",
        "🛍️ रिटेल व ई-कॉमर्स केयर (ऑर्डर ट्रैकिंग व रिफंड सपोर्ट)",
        "🚗 ऑटोमोबाइल व बाइक केयर (सर्विसिंग व रोड-साइड असिस्टेंस)",
        "🏥 हेल्थकेयर व क्लीनिक केयर (अपॉइंटमेंट व रिपोर्ट इंक्वायरी)"
    ])

    c_name = st.text_input("ग्राहक का नाम:", value="साहिल अहमद")
    c_phone = st.text_input("ग्राहक का मोबाइल नंबर:", value="7484878440")
    c_problem = st.selectbox("ग्राहक की समस्या (Customer Issue):", [
        "इंटरनेट स्पीड बहुत धीमी है और कॉल ड्रॉप हो रही है",
        "मेरा पिछला रिचार्ज खत्म हो गया, नया बेस्ट प्लान बताइए",
        "मैंने सामान ऑर्डर किया था, अभी तक डिलीवरी नहीं मिली",
        "मुझे अपनी गाड़ी की सर्विस के लिए मैकेनिक स्लॉट बुक करना है"
    ])

    if st.button("🚀 कस्टमर केयर लाइव कॉल शुरू करें (Speaker Live)"):
        st.success("🟢 OmniCare वॉयस इंजन कनेक्ट हो गया! फोन का वॉल्यूम तेज रखें।")

        if "Jio" in care_dept or "टेलीकॉम" in care_dept:
            dialogue_text = f"नमस्ते {c_name} जी! Jio कस्टमर सपोर्ट में आपका स्वागत है। मैं आपकी सीनियर एग्जीक्यूटिव नेहा बोल रही हूँ। आपकी शिकायत संख्या दर्ज कर ली गई है। आपके क्षेत्र के टावर का रिसेट सिग्नल भेज दिया गया है, अगले 15 मिनट में आपकी स्पीड 5G स्तर पर सामान्य हो जाएगी।"
        elif "रिटेल" in care_dept:
            dialogue_text = f"नमस्ते {c_name} जी! रिटेल कस्टमर केयर में आपका स्वागत है। मैं नेहा बोल रही हूँ। आपकी शिकायत दर्ज कर ली गई है। आपका पार्सल आज शाम तक आपके पते पर डिलीवर हो जाएगा।"
        else:
            dialogue_text = f"नमस्ते {c_name} जी! कस्टमर केयर में आपका स्वागत है। आपकी अनुरोध संख्या दर्ज कर ली गई है और डॉक्टर का कन्फर्मेशन स्लॉट आपके WhatsApp पर भेज दिया गया है।"

        # सटीक महिला आवाज़ (Female Neural Voice Synthesizer)
        js_speech = f"""
        <script>
            window.speechSynthesis.cancel();
            var msg = new SpeechSynthesisUtterance();
            msg.text = "{dialogue_text}";
            msg.lang = 'hi-IN';
            msg.rate = 0.90;
            msg.pitch = 1.35;

            var voices = window.speechSynthesis.getVoices();
            for(var i = 0; i < voices.length; i++) {{
                if(voices[i].lang.includes('hi') || voices[i].lang.includes('IN')) {{
                    msg.voice = voices[i];
                    break;
                }}
            }}
            window.speechSynthesis.speak(msg);
        </script>
        """
        components.html(js_speech, height=0)

        st.markdown(f"""
        <div class="card-block" style="border-left: 4px solid #10B981; margin-top:12px;">
            <p style="color:#10B981; font-weight:bold; margin-bottom:6px;">🎧 AI कस्टमर केयर एजेंट का जवाब (नेहा - लाइव ट्रांसक्रिप्ट):</p>
            <p style="font-size:14px; color:#F9FAFB;">"{dialogue_text}"</p>
        </div>
        """, unsafe_allow_html=True)

# ----------------------------------------------------
# टैब 2: ऑटोमैटिक टिकट व WhatsApp रसीद
# ----------------------------------------------------
with tabs[1]:
    st.markdown("### 🎫 कंप्लेंट टिकट व WhatsApp रसीद")
    ticket_num = f"OMNI-GRIEVANCE-{datetime.now().strftime('%d%m%H%M')}"

    st.markdown(f"""
    <div class="card-block" style="border-left: 4px solid #38BDF8;">
        <h4 style="color:#38BDF8; margin:0;">ऑटोमैटिक कंप्लेंट टिकट संख्या: <b>{ticket_num}</b></h4>
        <p style="font-size:13px; color:#94A3B8; margin-top:4px;">स्थिति: सक्रिय (In-Progress) | समाधान अवधि: 2 घंटे</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("📲 ग्राहक के WhatsApp पर टिकट रसीद भेजें"):
        wa_payload = f"""नमस्ते {c_name} जी! 🙏
OmniCare सपोर्ट में संपर्क करने के लिए धन्यवाद।

🎫 **कंप्लेंट टिकट संख्या:** {ticket_num}
📌 **दर्ज समस्या:** {c_problem}
⚡ **स्थिति:** हमारी AI टीम ने समाधान शुरू कर दिया है। 2 घंटे में समाधान हो जाएगा।

धन्यवाद!"""
        enc_payload = urllib.parse.quote(wa_payload)
        st.markdown(f'<a href="https://wa.me/91{c_phone}?text={enc_payload}" target="_blank" class="pay-btn-glow">📲 WhatsApp खोलें और रसीद भेजें</a>', unsafe_allow_html=True)

# ----------------------------------------------------
# टैब 3: एंटरप्राइज लाइसेंस
# ----------------------------------------------------
with tabs[2]:
    st.markdown("### 👑 Enterprise OmniCare Architecture License")
    st.markdown("""
    <div class="card-block" style="border-left: 4px solid #F59E0B;">
        <h3 style="color:#F59E0B; margin:0;">फुल कस्टमर केयर ऑटोमेशन सूट</h3>
        <p style="font-size:14px; color:#F8FAFC; margin:8px 0;">
            • 50 टेलीकॉलर्स की जगह अकेला AI एजेंट<br>
            • 24/7 ऑटोमैटिक कॉल हैंडलिंग (Hindi / English Neural Female Voice)<br>
            • ऑटोमैटिक CRM टिकट व WhatsApp डिलीवरी
        </p>
        <p style="font-size:18px; color:#38BDF8; font-weight:bold; margin:0;">One-Time Deployment: ₹1,00,000 | मासिक: ₹25,000</p>
    </div>
    """, unsafe_allow_html=True)

    token_cost = "10000"
    upi_str = f"upi://pay?pa={MY_UPI_ID}&pn=OmniCare%20Enterprise&am={token_cost}&cu=INR&tn=Care%20Token"
    qr_code_url = f"https://api.qrserver.com/v1/create-qr-code/?size=180x180&data={urllib.parse.quote(upi_str)}"

    st.markdown(f"""
    <div class="card-block" style="text-align: center;">
        <p style="color: #38BDF8 !important; font-weight: bold;">📲 Pay ₹10,000 Advance Token (GPay / PhonePe):</p>
        <img src="{qr_code_url}" width="165" style="background:#fff; padding:6px; border-radius:12px; border:2px solid #2563EB;" />
        <p style="font-size:12px; color:#94A3B8; margin-top:6px;">UPI ID: <b>{MY_UPI_ID}</b></p>
    </div>
    """, unsafe_allow_html=True)

# संस्थापक कार्ड
st.markdown("---")
st.markdown(f"""
<div class="card-block" style="text-align: center; border: 2px solid #38BDF8;">
    <p style="color:#38BDF8; font-size:11px; margin:0; letter-spacing:2px;">🏛️ FOUNDER & CHIEF ARCHITECT</p>
    <h2 style="color:#FFF; margin:6px 0; font-size:22px;">साहिल अहमद (Sahil Ahmad)</h2>
    <p style="color:#CBD5E1; font-size:13px; margin-bottom:12px;">OmniCare AGI — Engineering Enterprise AI Support Engines</p>
    <a href="https://wa.me/{MY_WA_NUMBER}" target="_blank" style="background:#10B981; color:#fff; padding:10px 22px; border-radius:8px; text-decoration:none; font-weight:bold; font-size:13px; display:inline-block;">💬 Connect on WhatsApp (+91 {MY_WA_NUMBER[-10:]})</a>
</div>
""", unsafe_allow_html=True)
        
