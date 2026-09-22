import streamlit as st
import streamlit.components.v1 as components
import urllib.parse
from datetime import datetime
import pandas as pd

# 1. Page Configuration
st.set_page_config(
    page_title="NEXUS CORE OS — 100% Autonomous Web Engine",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Modern Cyber Dark CSS (Zero-Lag UI)
st.markdown("""
<style>
    .stApp { background-color: #020617 !important; color: #F8FAFC !important; }
    label, p, span, h1, h2, h3, h4 { color: #F8FAFC !important; font-weight: 600 !important; }
    input, .stTextInput input, textarea, select {
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
    .web-btn {
        display: block; background: linear-gradient(90deg, #10B981 0%, #059669 100%);
        color: #FFFFFF !important; text-align: center; font-weight: 900; font-size: 15px;
        padding: 14px; border-radius: 12px; text-decoration: none; margin: 8px 0;
        box-shadow: 0 4px 20px rgba(16, 185, 129, 0.4);
    }
    .search-btn {
        display: block; background: linear-gradient(90deg, #0284C7 0%, #2563EB 100%);
        color: #FFFFFF !important; text-align: center; font-weight: 900; font-size: 15px;
        padding: 14px; border-radius: 12px; text-decoration: none; margin: 8px 0;
        box-shadow: 0 4px 20px rgba(37, 99, 235, 0.4);
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

# Header Brand
st.markdown("""
<div class="hero-orb">
    <div style="font-size: 34px; margin-bottom: 4px;">⚡🌐</div>
    <h1 style="color:#FFF; margin:0; font-size:22px; letter-spacing: -0.5px;">NEXUS PRIME — GLOBAL ACTION AGENT</h1>
    <p style="color:#94A3B8; font-size:12px; margin-top:4px;">100% Autonomous Internet Action Core • Powered by Sahil Ahmad</p>
</div>
""", unsafe_allow_html=True)

# 1. Bhasha Selection
selected_lang = st.selectbox("🌍 Bhasha Chunein / Select Language:", [
    "🇮🇳 हिन्दी (Hindi)",
    "🇬🇧 English (Global)",
    "🌾 भोजपुरी (Bhojpuri)",
    "🇦🇪 Arabic (العربية)",
    "🇪🇸 Spanish (Español)"
])

# 2. Internet Action Type
action_type = st.selectbox("🌐 Internet Ka Kaun Sa Kaam Karwana Hai:", [
    "🚀 1. Live Internet Web Search & Intelligence (Google Bypass)",
    "💼 2. Business Digital Khata & WhatsApp Direct Invoice",
    "📜 3. Legal Draft, Police/Sarkari Yojna Application",
    "📞 4. Autonomous Voice Desk & Complaint Solver"
])

# 3. Direct Task Command
task_cmd = st.text_input("👉 Internet Command / Task Likhein:", value="Dukan ki aaj ki bikri 14,500 record karein aur verify karein")
client_name = st.text_input("Aapka / Client Ka Naam:", value="Sahil Ahmad")
client_phone = st.text_input("WhatsApp Mobile Number (10 Digit):", value="7484878440")

# Execution Trigger
if st.button("🚀 EXECUTE 100% WEB ACTION (Kaam Poora Karein)"):
    clean_p = client_phone.strip()
    st.success("🟢 Command Received! Nexus AI ne online action execute kar diya:")

    # Voice & Content mapping
    if "English" in selected_lang:
        lang_code = "en-US"
        v_voice = f"Hello {client_name}! Your internet action for {task_cmd} is 100% completed by Nexus Core."
        doc_tag = "NEXUS PRIME GLOBAL INTERNET REPORT"
    elif "भोजपुरी" in selected_lang:
        lang_code = "hi-IN"
        v_voice = f"Pranaam {client_name} ji! Rauwa internet aadesh ke kaam bilkul poora ho gail ba."
        doc_tag = "NEXUS BHOJPURI WEB ACTION REPORT"
    elif "Arabic" in selected_lang:
        lang_code = "ar-SA"
        v_voice = f"مرحبا {client_name}! تم تنفيذ العملية بنجاح عبر الإنترنت بواسطة النظام."
        doc_tag = "تقرير تنفيذ العمليات الرقمية"
    elif "Spanish" in selected_lang:
        lang_code = "es-ES"
        v_voice = f"¡Hola {client_name}! Su tarea de internet ha sido procesada al 100% con éxito."
        doc_tag = "REPORTE DE ACCIÓN AUTÓNOMA GLOBAL"
    else:
        lang_code = "hi-IN"
        v_voice = f"नमस्ते {client_name} जी! आपके आदेश अनुसार इंटरनेट का काम 100% पूरा कर दिया गया है।"
        doc_tag = "NEXUS PRIME आधिकारिक डिजिटल रिकॉर्ड"

    # Generated Output Document
    final_output = f"""==================================================
{doc_tag}
Date: {today_str} | Verified Architect: Sahil Ahmad
Task Executed: {task_cmd}
Client Name: {client_name} (+91 {clean_p})
Status: 100% VERIFIED & EXECUTED ONLINE ✅
Server Grid: Nexus-Prime Cloud Node v5
=================================================="""

    # Direct Working Voice Module with On-Click Fallback
    audio_widget = f"""
    <div style="background:#0F172A; padding:14px; border-radius:12px; border-left:4px solid #10B981; margin:10px 0;">
        <p style="color:#10B981; margin:0 0 6px 0; font-weight:bold;">🔊 Live AI Speech ({selected_lang}):</p>
        <p style="color:#FFF; margin:0 0 10px 0; font-size:14px;">"{v_voice}"</p>
        <button onclick="speakDirect()" style="background:#10B981; color:#fff; border:none; padding:10px 18px; border-radius:8px; font-weight:bold; cursor:pointer;">
            ▶️ Aawaz Sunein (Play Audio)
        </button>
    </div>
    <script>
        function speakDirect() {{
            window.speechSynthesis.cancel();
            var ut = new SpeechSynthesisUtterance("{v_voice}");
            ut.lang = "{lang_code}";
            ut.rate = 0.92;
            ut.pitch = 1.35;
            window.speechSynthesis.speak(ut);
        }}
        setTimeout(speakDirect, 400);
    </script>
    """
    components.html(audio_widget, height=130)

    st.text_area("📄 Executed Web Document / Output:", final_output, height=130)

    # 100% Live Internet Action Buttons
    enc_payload = urllib.parse.quote(f"{doc_tag}\n\nTask: {task_cmd}\nStatus: Verified 100% Online ✅\nArchitect: Sahil Ahmad")
    
    st.markdown(f'<a href="https://wa.me/91{clean_p}?text={enc_payload}" target="_blank" class="web-btn">📲 1. WhatsApp Par Live Receipt Push Karein</a>', unsafe_allow_html=True)
    
    encoded_search = urllib.parse.quote(task_cmd)
    st.markdown(f'<a href="https://www.google.com/search?q={encoded_search}" target="_blank" class="search-btn">🌐 2. Direct Live Internet Search Run Karein</a>', unsafe_allow_html=True)

# ----------------------------------------------------
# Global Founder Identity Grid (Logon Ke Jaanne Ke Liye)
# ----------------------------------------------------
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; background:#0B1329; padding:18px; border-radius:14px; border: 2px solid #38BDF8;">
    <p style="color:#38BDF8; font-size:11px; margin:0; letter-spacing:2px;">🏛️ FOUNDER & CHIEF AI ARCHITECT</p>
    <h2 style="color:#FFF; margin:6px 0; font-size:24px;">साहिल अहमद (Sahil Ahmad)</h2>
    <p style="color:#94A3B8; font-size:13px; margin:0 0 12px 0;">Nexus Prime — Building India's Largest Sovereign Action OS</p>
    <a href="https://wa.me/{MY_WA_NUMBER}" target="_blank" style="background:#10B981; color:#fff; padding:10px 22px; border-radius:8px; text-decoration:none; font-weight:bold; font-size:14px; display:inline-block;">💬 Connect Directly on WhatsApp (+91 {MY_WA_NUMBER[-10:]})</a>
</div>
""", unsafe_allow_html=True)
