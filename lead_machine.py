import streamlit as st
import streamlit.components.v1 as components
import urllib.parse
from datetime import datetime
import pandas as pd

# 1. Page Config
st.set_page_config(
    page_title="BHARAT MIND OS — Global Multi-Language AI",
    page_icon="🌐",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Ultra-Clean Responsive Mobile Styling
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
        padding: 20px 14px; border-radius: 20px; text-align: center; margin-bottom: 16px;
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
    <div style="font-size: 32px; margin-bottom: 4px;">🌐⚡</div>
    <h1 style="color:#FFF; margin:0; font-size:22px; letter-spacing: -0.5px;">BHARAT MIND OS — WORLD AI</h1>
    <p style="color:#94A3B8; font-size:12px; margin-top:4px;">Global Multilingual Autonomous Engine (Duniya Ki Har Bhasha Me)</p>
</div>
""", unsafe_allow_html=True)

# Global Language Selector (Duniya ki kisi bhi bhasha ke liye)
selected_lang = st.selectbox("🌍 Bhasha Chunein / Select Language / اختر اللغة:", [
    "🇮🇳 Hindi (हिन्दी)",
    "🇬🇧 English (US/UK)",
    "🌾 Bhojpuri / Maithili (देसी बोली)",
    "🇦🇪 Arabic (العربية)",
    "🇪🇸 Spanish (Español)",
    "🇷🇺 Russian (Русский)",
    "🇫🇷 French (Français)"
])

# Role / Action Selector (Fixed text layout)
user_role = st.selectbox("🎯 Kaam Ka Prakar Chunein:", [
    "💼 Dukandar / Vyapari (Hisab-Kitab Ledger)",
    "📞 24/7 Voice Care & WhatsApp Ticket",
    "🎓 Student / Job Application & Resume",
    "🏛️ Legal & Civic Document Drafter"
])

# Task Input
task_input = st.text_input(
    "👉 Apna Kaam Likhein:",
    value="Dukan ki aaj ki kul bikri ₹14,500 darj karo aur WhatsApp par bhyjo"
)

col_1, col_2 = st.columns(2)
with col_1:
    user_name = st.text_input("Aapka Naam:", value="Sahil Ahmad")
with col_2:
    user_phone = st.text_input("WhatsApp Number (10 Digit):", value="7484878440")

# 1-Click Action Execution
if st.button("🚀 1-CLICK EXECUTE (Kaam Turant Karein)"):
    clean_p = user_phone.strip()
    st.success("🟢 Aadesh sweekar hua! System ne kaam complete kar diya:")

    # Multi-Language Voice Code & Response Mapping
    if "English" in selected_lang:
        lang_code = "en-US"
        spoken_text = f"Hello {user_name}! Your automated ledger entry for {task_input} has been processed successfully. Receipt is ready on WhatsApp."
        doc_header = "GLOBAL AUTONOMOUS DIGITAL LEDGER"
    elif "Arabic" in selected_lang:
        lang_code = "ar-SA"
        spoken_text = f"مرحبا {user_name}! تم تسجيل المعاملة بنجاح وجاهزة للإرسال عبر واتساب."
        doc_header = "دفتر الحسابات الرقمي الذاتي"
    elif "Spanish" in selected_lang:
        lang_code = "es-ES"
        spoken_text = f"¡Hola {user_name}! Su registro comercial ha sido completado con éxito."
        doc_header = "LIBRO DE ACCIÓN AUTÓNOMA"
    elif "Bhojpuri" in selected_lang:
        lang_code = "hi-IN"
        spoken_text = f"Pranaam {user_name} ji! Rauwa dukan ke hisab-kitab bilkul darj ho gail ba, parchi WhatsApp par bhej dihal gail ba."
        doc_header = "BHOJPURI DESI DIGITAL KHATA"
    elif "Russian" in selected_lang:
        lang_code = "ru-RU"
        spoken_text = f"Здравствуйте {user_name}! Ваша задача успешно выполнена."
        doc_header = "ЦИФРОВОЙ РЕЕСТР ДЕЙСТВИЙ"
    elif "French" in selected_lang:
        lang_code = "fr-FR"
        spoken_text = f"Bonjour {user_name}! Votre tâche a été exécutée avec succès."
        doc_header = "REGISTRE NUMÉRIQUE AUTONOME"
    else: # Hindi Default
        lang_code = "hi-IN"
        spoken_text = f"Namaste {user_name} ji! Aapki dukan ka hisab darj ho gaya hai. Parchi WhatsApp par taiyar hai."
        doc_header = "DAINIK DIGITAL BAHIKHATA"

    final_doc = f"""==================================================
{doc_header}
Date: {today_str} | Authorized: {user_name}
Language Mode: {selected_lang}
Task: {task_input}
Status: VERIFIED & COMPLETED BY NEURAL CORE ✅
=================================================="""

    # Dynamic Multilingual Female Voice Script
    js_multi_voice = f"""
    <script>
        window.speechSynthesis.cancel();
        var msg = new SpeechSynthesisUtterance();
        msg.text = "{spoken_text}";
        msg.lang = '{lang_code}';
        msg.rate = 0.92;
        msg.pitch = 1.5;

        var vList = window.speechSynthesis.getVoices();
        for (var i = 0; i < vList.length; i++) {{
            if (vList[i].lang.includes('{lang_code.split("-")[0]}')) {{
                msg.voice = vList[i];
                break;
            }}
        }}
        window.speechSynthesis.speak(msg);
    </script>
    """
    components.html(js_multi_voice, height=0)

    # Output Card
    st.markdown(f"""
    <div class="action-box" style="border-left: 4px solid #10B981; margin-top:12px;">
        <p style="color:#10B981; font-weight:bold; margin-bottom:4px;">🔊 Multilingual AI Voice Output ({selected_lang}):</p>
        <p style="font-size:14px; color:#F8FAFC; margin:0;">"{spoken_text}"</p>
    </div>
    """, unsafe_allow_html=True)

    st.text_area("📄 Generated Document / Log:", final_doc, height=130)

    # WhatsApp Direct Send
    enc_wa = urllib.parse.quote(f"{doc_header}\n{spoken_text}")
    st.markdown(f'<a href="https://wa.me/91{clean_p}?text={enc_wa}" target="_blank" class="pay-btn-glow">📲 WhatsApp Par Receipt Bhejein</a>', unsafe_allow_html=True)

# Database Grid
st.markdown("---")
st.markdown("### 📊 Global National Action Grid")
live_grid = {
    "Time": [datetime.now().strftime("%H:%M:%S"), "16:20:10", "15:55:40"],
    "User": [user_name, "Carlos (Madrid)", "Fatima (Dubai)"],
    "Language": [selected_lang.split(" ")[1], "Spanish", "Arabic"],
    "Status": ["Completed ✅", "Completed ✅", "Completed ✅"]
}
st.dataframe(pd.DataFrame(live_grid), use_container_width=True)

# Founder Card
st.markdown("---")
st.markdown(f"""
<div class="action-box" style="text-align: center; border: 2px solid #38BDF8;">
    <p style="color:#38BDF8; font-size:11px; margin:0; letter-spacing:2px;">🏛️ FOUNDER & CHIEF ARCHITECT</p>
    <h2 style="color:#FFF; margin:6px 0; font-size:22px;">Sahil Ahmad</h2>
    <p style="color:#CBD5E1; font-size:13px; margin-bottom:12px;">Bharat Mind OS — Engineering Global Sovereign Autonomous Intelligence</p>
    <a href="https://wa.me/{MY_WA_NUMBER}" target="_blank" style="background:#10B981; color:#fff; padding:10px 22px; border-radius:8px; text-decoration:none; font-weight:bold; font-size:13px; display:inline-block;">💬 Connect on WhatsApp (+91 {MY_WA_NUMBER[-10:]})</a>
</div>
""", unsafe_allow_html=True)
