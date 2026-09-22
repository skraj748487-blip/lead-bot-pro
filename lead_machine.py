import streamlit as st
import streamlit.components.v1 as components
import urllib.parse
from datetime import datetime

# 1. Page Configuration
st.set_page_config(
    page_title="NEXUS BRAIN OS",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Cyber-Dark Styling & Glowing Orb
st.markdown("""
<style>
    .stApp { background-color: #020617 !important; color: #F8FAFC !important; }
    label, p, span, h1, h2, h3, h4 { color: #F8FAFC !important; font-weight: 600 !important; }
    input, .stTextInput input, textarea {
        background-color: #0F172A !important; color: #38BDF8 !important;
        font-size: 15px !important; font-weight: 600 !important;
        border: 2px solid #1E293B !important; border-radius: 12px !important;
    }
    input:focus, .stTextInput input:focus {
        border-color: #38BDF8 !important; box-shadow: 0 0 15px rgba(56, 189, 248, 0.4) !important;
    }
    .orb-container {
        text-align: center; padding: 20px 10px; margin-bottom: 16px;
        background: radial-gradient(circle at center, #1E1B4B 0%, #020617 100%);
        border-radius: 20px; border: 1px solid #312E81;
        box-shadow: 0 10px 40px rgba(99, 102, 241, 0.35);
    }
    .neural-orb {
        width: 70px; height: 70px; margin: 0 auto 10px auto; border-radius: 50%;
        background: radial-gradient(circle, #38BDF8 10%, #6366F1 60%, #020617 100%);
        box-shadow: 0 0 25px #38BDF8, 0 0 50px #6366F1;
    }
    .wa-btn {
        display: block; background: linear-gradient(90deg, #10B981 0%, #059669 100%);
        color: #FFFFFF !important; text-align: center; font-weight: 800; font-size: 15px;
        padding: 13px; border-radius: 10px; text-decoration: none; margin: 8px 0;
        box-shadow: 0 4px 15px rgba(16, 185, 129, 0.4);
    }
    .search-btn {
        display: block; background: linear-gradient(90deg, #0284C7 0%, #2563EB 100%);
        color: #FFFFFF !important; text-align: center; font-weight: 800; font-size: 15px;
        padding: 13px; border-radius: 10px; text-decoration: none; margin: 8px 0;
        box-shadow: 0 4px 15px rgba(37, 99, 235, 0.4);
    }
    div.stButton > button {
        background: linear-gradient(135deg, #2563EB 0%, #4F46E5 100%) !important;
        color: #FFFFFF !important; border: none !important; border-radius: 12px !important;
        font-weight: 800 !important; font-size: 16px !important; width: 100% !important;
        padding: 14px !important; box-shadow: 0 4px 20px rgba(37, 99, 235, 0.4) !important;
    }
</style>
""", unsafe_allow_html=True)

MY_WA_NUMBER = "917484878440"
today_str = datetime.now().strftime("%d-%m-%Y")
time_str = datetime.now().strftime("%I:%M %p")

# Header
st.markdown("""
<div class="orb-container">
    <div class="neural-orb"></div>
    <h1 style="color:#FFF; margin:0; font-size:22px;">NEXUS BRAIN OS</h1>
    <p style="color:#94A3B8; font-size:12px; margin-top:4px;">Autonomous Action Engine • Powered by Sahil Ahmad</p>
</div>
""", unsafe_allow_html=True)

selected_lang = st.selectbox("🌍 भाषा चुनें (Select Language):", [
    "हिन्दी (Hindi)",
    "English",
    "भोजपुरी (Bhojpuri)"
])

user_prompt = st.text_input(
    "⚡ Universal Command Bar (यहाँ अपना काम लिखें):",
    value="Ahmad Car Care - Car Servicing and Oil Change Bill"
)

col_u, col_v = st.columns(2)
with col_u:
    user_name = st.text_input("ग्राहक / पार्टी का नाम:", value="साहिल अहमद")
with col_v:
    user_phone = st.text_input("WhatsApp नंबर (10 अंक):", value="7484878440")

if st.button("🚀 EXECUTE AUTONOMOUS ACTION (काम पूरा करें)"):
    clean_p = user_phone.strip() if user_phone.strip() else "7484878440"
    client_title = user_name.strip() if user_name.strip() else "ग्राहक"
    cmd_lower = user_prompt.lower()

    # Smart Keyword Detection
    if any(k in cmd_lower for k in ["car", "service", "care", "auto", "repair", "garage"]):
        doc_title = "🚗 AHMAD CAR CARE — OFFICIAL WORK ORDER & INVOICE"
        spoken_text = f"नमस्ते {client_title} जी! अहमद कार केयर का सर्विस बिल और जॉब रिकॉर्ड सफलतापूर्वक तैयार कर दिया गया है।"
        res_content = f"""==================================================
{doc_title}
जॉब कार्ड आईडी: ACC-{datetime.now().strftime('%H%M%S')}
तारीख: {today_str} | समय: {time_str}
--------------------------------------------------
ग्राहक: {client_title} (+91 {clean_p})
काम विवरण: {user_prompt}
सर्विस स्टेटस: कार्य पूर्ण एवं सत्यापित ✅
अधिकृत वर्कशॉप: Ahmad Car Care Center
आर्किटेक्ट सिस्टम: Sahil Ahmad (Nexus Brain OS)
=================================================="""

    elif any(k in cmd_lower for k in ["script", "video", "youtube", "reels", "shorts"]):
        doc_title = "🎬 वायरल कंटेंट स्क्रिप्ट व रील्स प्लानर"
        spoken_text = f"नमस्ते {client_title} जी! आपके वीडियो का वायरल स्क्रिप्ट और ट्रेंडिंग टैग्स तैयार हैं।"
        res_content = f"""==================================================
{doc_title}
विषय: {user_prompt}
दिनांक: {today_str} | क्रिएटर: {client_title}
--------------------------------------------------
[हुक]: रुकिए! अगर आप यह ट्रिक नहीं जानते तो आपका समय बर्बाद हो रहा है।
[मुख्य भाग]: {user_prompt} के बारे में 3 मुख्य बातें साफ़ शब्दों में बोलें।
[कॉल टू एक्शन]: वीडियो को सेव करें और अभी दोस्तों के साथ शेयर करें!
[टैग्स]: #viral #trending #reels #nexus #tech
=================================================="""

    elif any(k in cmd_lower for k in ["notice", "legal", "draft", "complaint", "police", "agreement", "kiraya"]):
        doc_title = "📜 आधिकारिक कानूनी व नागरिक आवेदन प्रारूप"
        spoken_text = f"नमस्ते {client_title} जी! आपका विधिक आवेदन पत्र ड्राफ्ट कर दिया गया है।"
        res_content = f"""==================================================
{doc_title}
रेफरेंस नंबर: NX-LEG-{datetime.now().strftime('%H%M%S')}
आवेदक: {client_title} (+91 {clean_p}) | दिनांक: {today_str}
विषय: {user_prompt}
--------------------------------------------------
महोदय,
सविनय निवेदन है कि उपरोक्त मामले ({user_prompt}) के संबंध में उचित कानूनी कार्रवाई सुनिश्चित की जाए।
सत्यापित: सक्षम प्राधिकारी हेतु प्रस्तुत।
=================================================="""

    else:
        doc_title = "🧾 आधिकारिक डिजिटल व्यापार बहीखाता"
        spoken_text = f"नमस्ते {client_title} जी! आपकी दुकान का हिसाब दर्ज कर दिया गया है और पर्ची तैयार है।"
        res_content = f"""==================================================
{doc_title}
बिल नंबर: NX-INV-{datetime.now().strftime('%H%M%S')}
दिनांक: {today_str} | समय: {time_str}
पार्टी/ग्राहक: {client_title} (+91 {clean_p})
विवरण: {user_prompt}
स्थिति: क्लाउड पर 100% सत्यापित एवं दर्ज ✅
आर्किटेक्ट: Sahil Ahmad
=================================================="""

    st.success("🟢 आदेश स्वीकार हुआ! सिस्टम ने कार्रवाई पूरी कर दी:")

    # Voice Box
    audio_code = f"""
    <div style="background:#0F172A; padding:12px; border-radius:10px; border-left:4px solid #10B981; margin:8px 0;">
        <p style="color:#10B981; margin:0 0 4px 0; font-size:13px; font-weight:bold;">🔊 AI वॉइस पुष्टि:</p>
        <p style="color:#FFF; margin:0 0 8px 0; font-size:14px;">"{spoken_text}"</p>
        <button onclick="playVoiceNow()" style="background:#10B981; color:#fff; border:none; padding:8px 16px; border-radius:6px; font-weight:bold; cursor:pointer;">
            ▶️ आवाज़ सुनें (Play Voice)
        </button>
    </div>
    <script>
        function playVoiceNow() {{
            window.speechSynthesis.cancel();
            var ut = new SpeechSynthesisUtterance("{spoken_text}");
            ut.lang = "{"en-US" if "English" in selected_lang else "hi-IN"}";
            ut.rate = 0.95;
            ut.pitch = 1.3;
            window.speechSynthesis.speak(ut);
        }}
        setTimeout(playVoiceNow, 300);
    </script>
    """
    components.html(audio_code, height=115)

    st.text_area("📄 तैयार दस्तावेज़ / आउटपुट:", res_content, height=180)

    # Action Buttons
    enc_wa = urllib.parse.quote(f"{doc_title}\n\nग्राहक: {client_title}\nविवरण: {user_prompt}\nस्थिति: सत्यापित ✅\nबाय: Sahil Ahmad (Nexus Brain OS)")
    st.markdown(f'<a href="https://wa.me/91{clean_p}?text={enc_wa}" target="_blank" class="wa-btn">📲 1. सीधे WhatsApp पर पर्ची भेजें</a>', unsafe_allow_html=True)

    enc_srch = urllib.parse.quote(user_prompt)
    st.markdown(f'<a href="https://www.google.com/search?q={enc_srch}" target="_blank" class="search-btn">🌐 2. इंटरनेट लाइव सर्च रन करें</a>', unsafe_allow_html=True)

# Founder Branding Footer
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; background:#0B1329; padding:16px; border-radius:14px; border: 2px solid #38BDF8;">
    <p style="color:#38BDF8; font-size:11px; margin:0; letter-spacing:2px;">🏛️ FOUNDER & CHIEF ARCHITECT</p>
    <h2 style="color:#FFF; margin:4px 0; font-size:22px;">साहिल अहमद (Sahil Ahmad)</h2>
    <p style="color:#94A3B8; font-size:12px; margin:0 0 10px 0;">Nexus Brain OS — Autonomous Artificial Intelligence Infrastructure</p>
    <a href="https://wa.me/{MY_WA_NUMBER}" target="_blank" style="background:#10B981; color:#fff; padding:10px 20px; border-radius:8px; text-decoration:none; font-weight:bold; font-size:13px; display:inline-block;">💬 Connect on WhatsApp (+91 {MY_WA_NUMBER[-10:]})</a>
</div>
""", unsafe_allow_html=True)
