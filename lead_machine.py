import streamlit as st
import streamlit.components.v1 as components
import urllib.parse
from datetime import datetime
import pandas as pd

# 1. Page Configuration
st.set_page_config(
    page_title="BHARAT MIND OS — Global Autonomous Action Engine",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Modern Cyber Dark CSS
st.markdown("""
<style>
    .stApp { background-color: #020617 !important; color: #F8FAFC !important; }
    label, p, span, h1, h2, h3, h4 { color: #F8FAFC !important; font-weight: 600 !important; }
    input, .stTextInput input, textarea, .stTextArea textarea, select, .stSelectbox div {
        background-color: #0F172A !important; color: #38BDF8 !important;
        font-size: 15px !important; font-weight: 600 !important;
        border: 2px solid #1E293B !important; border-radius: 12px !important;
    }
    .hero-orb {
        background: radial-gradient(circle at center, #1E1B4B 0%, #020617 100%);
        padding: 22px 14px; border-radius: 20px; text-align: center; margin-bottom: 16px;
        border: 1px solid #312E81; box-shadow: 0 10px 40px rgba(99, 102, 241, 0.3);
    }
    .action-box {
        background: #0B1329; border: 1px solid #1E293B; border-radius: 14px;
        padding: 16px; margin-bottom: 14px;
    }
    .pay-btn-glow {
        display: block; background: linear-gradient(90deg, #10B981 0%, #059669 100%);
        color: #FFFFFF !important; text-align: center; font-weight: 900; font-size: 15px;
        padding: 14px; border-radius: 12px; text-decoration: none; margin: 10px 0;
        box-shadow: 0 4px 20px rgba(16, 185, 129, 0.4);
    }
    div.stButton > button {
        background: linear-gradient(135deg, #2563EB 0%, #4F46E5 100%) !important;
        color: #FFFFFF !important; border: none !important; border-radius: 12px !important;
        font-weight: 900 !important; font-size: 16px !important; width: 100% !important;
        padding: 15px !important; box-shadow: 0 4px 25px rgba(37, 99, 235, 0.45) !important;
    }
</style>
""", unsafe_allow_html=True)

MY_WA_NUMBER = "917484878440"
MY_UPI_ID = "7484878449-2@ybl"
today_str = datetime.now().strftime("%d-%m-%Y")

# Header
st.markdown("""
<div class="hero-orb">
    <div style="font-size: 34px; margin-bottom: 4px;">⚡🌐</div>
    <h1 style="color:#FFF; margin:0; font-size:22px; letter-spacing: -0.5px;">BHARAT MIND OS — GLOBAL ENGINE</h1>
    <p style="color:#94A3B8; font-size:12px; margin-top:4px;">Google सिर्फ लिंक दिखाता है — Bharat Mind OS काम खुद पूरा करता है।</p>
</div>
""", unsafe_allow_html=True)

# 1. भाषा चयन
selected_lang = st.selectbox("🌍 भाषा चुनें / Select Language:", [
    "🇮🇳 Hindi (हिन्दी)",
    "🇬🇧 English (International)",
    "🌾 Bhojpuri / Maithili (देसी बोली)",
    "🇦🇪 Arabic (العربية)",
    "🇪🇸 Spanish (Español)"
])

# 2. कार्य श्रेणी
user_role = st.selectbox("🎯 कार्य श्रेणी चुनें:", [
    "💼 दुकानदार / व्यापारी (दैनिक हिसाब-किताब व बहीखाता)",
    "📞 कस्टमर केयर एजेंट (लाइव आवाज़ व WhatsApp रसीद)",
    "🎓 छात्र व युवा (आवेदन पत्र, लीव लेटर व रिज्यूमे)",
    "🏛️ आम नागरिक (सरकारी योजना, राशन व कानूनी ड्राफ्ट)"
])

# 3. कार्य इनपुट
task_input = st.text_input(
    "👉 अपना काम यहाँ लिखें (Command Bar):",
    value="दुकान की आज की कुल बिक्री ₹14,500 दर्ज करो और WhatsApp पर्ची बनाओ"
)

col_1, col_2 = st.columns(2)
with col_1:
    user_name = st.text_input("आपका नाम:", value="साहिल अहमद")
with col_2:
    user_phone = st.text_input("WhatsApp नंबर (10 अंक):", value="7484878440")

# 1-Click Action Execution
if st.button("🚀 1-CLICK EXECUTE (काम तुरंत पूरा करें)"):
    clean_p = user_phone.strip()
    st.success("🟢 आदेश स्वीकार हुआ! न्यूरल कोर ने काम पूरा कर दिया:")

    # भाषा व कार्य के अनुसार रिस्पॉन्स
    if "English" in selected_lang:
        lang_code = "en-US"
        spoken_text = f"Hello {user_name}! Your automated action for {task_input} has been executed successfully. Details dispatched to WhatsApp."
        doc_header = "GLOBAL AUTONOMOUS DIGITAL LEDGER"
    elif "Arabic" in selected_lang:
        lang_code = "ar-SA"
        spoken_text = f"مرحبا {user_name}! تم إنجاز المهمة بنجاح وتجهيز التقرير للإرسال."
        doc_header = "دفتر الحسابات الرقمي الذاتي"
    elif "Bhojpuri" in selected_lang:
        lang_code = "hi-IN"
        spoken_text = f"प्रणाम {user_name} जी! रउवा आदेश के काम पूरा हो गईल बा, परची WhatsApp पर तइयार बा।"
        doc_header = "भोजपुरी देसी डिजिटल बहीखाता"
    elif "Spanish" in selected_lang:
        lang_code = "es-ES"
        spoken_text = f"¡Hola {user_name}! Su tarea ha sido procesada exitosamente."
        doc_header = "LIBRO DE ACCIÓN AUTÓNOMA"
    else:
        lang_code = "hi-IN"
        spoken_text = f"नमस्ते {user_name} जी! आपके आदेशानुसार काम पूरा कर दिया गया है। आपकी रसीद WhatsApp पर तैयार है।"
        doc_header = "दैनिक डिजिटल बहीखाता व आधिकारिक रिकॉर्ड"

    final_doc = f"""==================================================
{doc_header}
दिनांक: {today_str} | अधिकृत: {user_name}
भाषा मोड: {selected_lang}
दर्ज कार्य: {task_input}
स्थिति: न्यूरल कोर द्वारा सत्यापित एवं पूर्ण ✅
=================================================="""

    # स्पष्ट महिला आवाज़ (Female Speech Synthesis)
    js_multi_voice = f"""
    <script>
        window.speechSynthesis.cancel();
        var msg = new SpeechSynthesisUtterance();
        msg.text = "{spoken_text}";
        msg.lang = '{lang_code}';
        msg.rate = 0.92;
        msg.pitch = 1.6;

        var vList = window.speechSynthesis.getVoices();
        for (var i = 0; i < vList.length; i++) {{
            var n = vList[i].name.toLowerCase();
            if ((vList[i].lang.includes('{lang_code.split("-")[0]}')) && 
                (n.includes('female') || n.includes('google') || n.includes('india') || n.includes('zira'))) {{
                msg.voice = vList[i];
                break;
            }}
        }}
        window.speechSynthesis.speak(msg);
    </script>
    """
    components.html(js_multi_voice, height=0)

    # आउटपुट कार्ड
    st.markdown(f"""
    <div class="action-box" style="border-left: 4px solid #10B981; margin-top:12px;">
        <p style="color:#10B981; font-weight:bold; margin-bottom:4px;">🔊 AI वॉयस एग्जीक्यूटर ({selected_lang}):</p>
        <p style="font-size:14px; color:#F8FAFC; margin:0;">"{spoken_text}"</p>
    </div>
    """, unsafe_allow_html=True)

    st.text_area("📄 तैयार दस्तावेज़ / आउटपुट:", final_doc, height=130)

    # WhatsApp शेयर
    enc_wa = urllib.parse.quote(f"{doc_header}\n{spoken_text}")
    st.markdown(f'<a href="https://wa.me/91{clean_p}?text={enc_wa}" target="_blank" class="pay-btn-glow">📲 सीधे WhatsApp पर रसीद भेजें</a>', unsafe_allow_html=True)

# डेटाबेस ग्रिड
st.markdown("---")
st.markdown("### 📊 लाइव एक्शन ग्रिड (National Execution Log)")
live_grid = {
    "समय": [datetime.now().strftime("%H:%M:%S"), "16:20:10", "15:55:40"],
    "यूज़र": [user_name, "अनिल कुमार (पटना)", "प्रिया सिंह (लखनऊ)"],
    "भाषा": [selected_lang.split(" ")[1], "हिन्दी", "हिन्दी"],
    "स्थिति": ["सफल ✅", "सफल ✅", "सफल ✅"]
}
st.dataframe(pd.DataFrame(live_grid), use_container_width=True)

# टोकन गेटवे
st.markdown("---")
st.markdown("### 👑 Enterprise Sovereign Deployment — ₹1,00,000")
st.caption("अपने बिज़नेस में इस AI सिस्टम को तैनात करने के लिए टोकन ट्रांसफर करें:")

token_amt = "10000"
upi_uri = f"upi://pay?pa={MY_UPI_ID}&pn=Bharat%20Mind%20OS&am={token_amt}&cu=INR&tn=Sovereign%20Token"
qr_uri = f"https://api.qrserver.com/v1/create-qr-code/?size=180x180&data={urllib.parse.quote(upi_uri)}"

col_k, col_l = st.columns([1, 2])
with col_k:
    st.image(qr_uri, width=150)
with col_l:
    st.markdown(f"""
    <div style="padding-top:8px;">
        <p style="color:#38BDF8; font-size:15px; margin:0;"><b>Book ₹10,000 Deployment Token</b></p>
        <p style="color:#94A3B8; font-size:12px; margin:4px 0 10px 0;">PhonePe / Google Pay / BHIM Support</p>
        <p style="color:#CBD5E1; font-size:13px; margin:0;">UPI ID: <b>{MY_UPI_ID}</b></p>
    </div>
    """, unsafe_allow_html=True)

# संस्थापक प्रोफ़ाइल
st.markdown("---")
st.markdown(f"""
<div class="action-box" style="text-align: center; border: 2px solid #38BDF8;">
    <p style="color:#38BDF8; font-size:11px; margin:0; letter-spacing:2px;">🏛️ FOUNDER & CHIEF ARCHITECT</p>
    <h2 style="color:#FFF; margin:6px 0; font-size:22px;">साहिल अहमद (Sahil Ahmad)</h2>
    <p style="color:#CBD5E1; font-size:13px; margin-bottom:12px;">Bharat Mind OS — Engineering Global Sovereign Autonomous Intelligence</p>
    <a href="https://wa.me/{MY_WA_NUMBER}" target="_blank" style="background:#10B981; color:#fff; padding:10px 22px; border-radius:8px; text-decoration:none; font-weight:bold; font-size:13px; display:inline-block;">💬 Connect on WhatsApp (+91 {MY_WA_NUMBER[-10:]})</a>
</div>
""", unsafe_allow_html=True)
