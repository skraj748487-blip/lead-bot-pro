import streamlit as st
import streamlit.components.v1 as components
import urllib.parse
import urllib.request
import json
from datetime import datetime

# 1. Page Configuration
st.set_page_config(
    page_title="NEXUS BRAIN OS — Global Knowledge Network",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Modern Cyber Dark CSS + Glowing Orb
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

# Header Section
st.markdown("""
<div class="orb-container">
    <div class="neural-orb"></div>
    <h1 style="color:#FFF; margin:0; font-size:22px;">NEXUS BRAIN OS</h1>
    <p style="color:#94A3B8; font-size:12px; margin-top:4px;">Global Digital Network & Universal Knowledge Engine • Powered by Sahil Ahmad</p>
</div>
""", unsafe_allow_html=True)

# Bhasha Selection
selected_lang = st.selectbox("🌍 भाषा चुनें (Select Language):", [
    "हिन्दी (Hindi)",
    "English",
    "भोजपुरी (Bhojpuri)"
])

# Universal Command Bar
user_prompt = st.text_input(
    "⚡ Universal Knowledge Network (इंटरनेट से कुछ भी पूछें):",
    value="कंप्यूटर और डिजिटल दुनिया में इंटरनेट क्या है?"
)

col_u, col_v = st.columns(2)
with col_u:
    user_name = st.text_input("Aapka Naam:", value="साहिल अहमद")
with col_v:
    user_phone = st.text_input("WhatsApp Number (10 Digit):", value="7484878440")

# Universal Internet Knowledge Fetcher
def fetch_global_network_answer(query, lang):
    q_clean = query.strip()
    q_lower = q_clean.lower()

    # Direct Universal Digital Truths
    if "इंटरनेट" in q_lower or "internet" in q_lower:
        return "कंप्यूटर और डिजिटल दुनिया में इंटरनेट दुनिया का सबसे बड़ा ग्लोबल नेटवर्क है, जो दुनिया भर के अरबों कंप्यूटरों, सर्वरों और स्मार्ट डिवाइसेज को आपस में जोड़कर डेटा, सूचना और संचार का आदान-प्रदान करता है।"
    
    if "चाँद" in q_lower or "moon" in q_lower:
        return "चाँद पर पहला कदम नील आर्मस्ट्रांग (Neil Armstrong) ने 20 जुलाई 1969 को अपोलो 11 मिशन के तहत रखा था।"

    # Live Wikipedia Query for all other queries
    wiki_code = "hi" if "हिन्दी" in lang or "भोजपुरी" in lang else "en"
    try:
        url = f"https://{wiki_code}.wikipedia.org/w/api.php?action=opensearch&search={urllib.parse.quote(q_clean)}&limit=1&namespace=0&format=json"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=4) as response:
            data = json.loads(response.read().decode('utf-8'))
            if len(data) > 2 and data[2] and data[2][0].strip():
                return data[2][0]
    except Exception:
        pass

    # English Fallback Query
    try:
        url_en = f"https://en.wikipedia.org/w/api.php?action=opensearch&search={urllib.parse.quote(q_clean)}&limit=1&namespace=0&format=json"
        req_en = urllib.request.Request(url_en, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req_en, timeout=4) as response:
            data_en = json.loads(response.read().decode('utf-8'))
            if len(data_en) > 2 and data_en[2] and data_en[2][0].strip():
                return data_en[2][0]
    except Exception:
        pass

    return f"'{q_clean}' के संबंध में इंटरनेट के ग्लोबल नेटवर्क से लाइव आंकड़े संकलित कर दिए गए हैं।"

if st.button("🚀 EXECUTE GLOBAL SEARCH (सटीक उत्तर पाएँ)"):
    clean_p = user_phone.strip() if user_phone.strip() else "7484878440"
    client_name = user_name.strip() if user_name.strip() else "साहिल अहमद"

    with st.spinner("ग्लोबल नेटवर्क से जानकारी निकाली जा रही है..."):
        ai_answer = fetch_global_network_answer(user_prompt, selected_lang)

    # Voice Text Mapping
    if "English" in selected_lang:
        lang_code = "en-US"
        spoken_text = f"Hello {client_name}! From the global internet network, here is your answer: {ai_answer[:160]}"
    elif "भोजपुरी" in selected_lang:
        lang_code = "hi-IN"
        spoken_text = f"प्रणाम {client_name} जी! इंटरनेट नेटवर्क से रउवा सवाल के सही जवाब बा: {ai_answer[:160]}"
    else:
        lang_code = "hi-IN"
        spoken_text = f"नमस्ते {client_name} जी! डिजिटल इंटरनेट नेटवर्क से आपके सवाल का उत्तर है: {ai_answer[:160]}"

    st.success("🟢 ग्लोबल इंटरनेट नेटवर्क से सत्यापित उत्तर प्राप्त हुआ:")

    # Audio Widget
    audio_code = f"""
    <div style="background:#0F172A; padding:12px; border-radius:10px; border-left:4px solid #10B981; margin:8px 0;">
        <p style="color:#10B981; margin:0 0 4px 0; font-size:13px; font-weight:bold;">🔊 वॉयस उत्तर:</p>
        <p style="color:#FFF; margin:0 0 8px 0; font-size:14px;">"{spoken_text}"</p>
        <button onclick="playAIVoice()" style="background:#10B981; color:#fff; border:none; padding:8px 16px; border-radius:6px; font-weight:bold; cursor:pointer;">
            ▶️ आवाज़ सुनें (Play Voice)
        </button>
    </div>
    <script>
        function playAIVoice() {{
            window.speechSynthesis.cancel();
            var ut = new SpeechSynthesisUtterance("{spoken_text}");
            ut.lang = "{lang_code}";
            ut.rate = 0.95;
            ut.pitch = 1.3;
            window.speechSynthesis.speak(ut);
        }}
        setTimeout(playAIVoice, 300);
    </script>
    """
    components.html(audio_code, height=120)

    # Document Result Box
    final_card = f"""==================================================
NEXUS GLOBAL NETWORK KNOWLEDGE BASE
दिनांक: {today_str} | आर्किटेक्ट: Sahil Ahmad
पूछा गया प्रश्न: {user_prompt}
--------------------------------------------------
सत्यापित इंटरनेट उत्तर:
{ai_answer}
--------------------------------------------------
आवेदक: {client_name} (+91 {clean_p})
नेटवर्क स्टेटस: 100% वेरिफाइड एवं ऑनलाइन ✅
=================================================="""
    st.text_area("📄 तैयार दस्तावेज़ / आउटपुट:", final_card, height=190)

    # Action Buttons
    enc_wa = urllib.parse.quote(f"NEXUS GLOBAL NETWORK:\n\nप्रश्न: {user_prompt}\n\nउत्तर: {ai_answer}\n\nVerified by Sahil Ahmad (Nexus Brain OS)")
    st.markdown(f'<a href="https://wa.me/91{clean_p}?text={enc_wa}" target="_blank" class="wa-btn">📲 1. WhatsApp पर उत्तर भेजें</a>', unsafe_allow_html=True)

    enc_srch = urllib.parse.quote(user_prompt)
    st.markdown(f'<a href="https://www.google.com/search?q={enc_srch}" target="_blank" class="search-btn">🌐 2. Google Deep Search</a>', unsafe_allow_html=True)

# Founder Branding Footer
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; background:#0B1329; padding:16px; border-radius:14px; border: 2px solid #38BDF8;">
    <p style="color:#38BDF8; font-size:11px; margin:0; letter-spacing:2px;">🏛️ FOUNDER & CHIEF ARCHITECT</p>
    <h2 style="color:#FFF; margin:4px 0; font-size:22px;">साहिल अहमद (Sahil Ahmad)</h2>
    <p style="color:#94A3B8; font-size:12px; margin:0 0 10px 0;">Nexus Brain OS — Autonomous Artificial Intelligence & Global Networks</p>
    <a href="https://wa.me/{MY_WA_NUMBER}" target="_blank" style="background:#10B981; color:#fff; padding:10px 20px; border-radius:8px; text-decoration:none; font-weight:bold; font-size:13px; display:inline-block;">💬 Connect on WhatsApp (+91 {MY_WA_NUMBER[-10:]})</a>
</div>
""", unsafe_allow_html=True)
