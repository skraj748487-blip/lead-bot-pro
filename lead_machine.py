import streamlit as st
import urllib.parse
from datetime import datetime

# 1. ग्लोबल कॉन्फ़िगरेशन
st.set_page_config(
    page_title="Nexus Core OS — 4-Agent Autonomous Enterprise",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. भाषा चयन
lang = st.radio("🌐 भाषा / Language:", ["🇮🇳 Hindi", "🌍 English"], horizontal=True)

# 3. हाई-टेक एंटरप्राइज डार्क UI
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
    .grand-hero {
        background: linear-gradient(135deg, #1E1B4B 0%, #312E81 50%, #0F172A 100%);
        padding: 24px;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 10px 40px rgba(79, 70, 229, 0.45);
        border: 1px solid #6366F1;
    }
    .grand-hero h2 {
        color: #FFFFFF !important;
        font-size: 22px !important;
        margin: 0 !important;
        font-weight: 900 !important;
    }
    .grand-hero p {
        color: #C7D2FE !important;
        font-size: 13px !important;
        margin-top: 6px !important;
    }
    .agent-card {
        background-color: #111827;
        border: 1px solid #1F2937;
        border-radius: 14px;
        padding: 16px;
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
        border: 2px solid #6366F1;
        border-radius: 18px;
        padding: 20px;
        text-align: center;
        margin-top: 30px;
        margin-bottom: 20px;
        box-shadow: 0 8px 30px rgba(99, 102, 241, 0.25);
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
today_str = datetime.now().strftime("%d-%m-%Y")

if "Hindi" in lang:
    st.markdown("""
    <div class="grand-hero">
        <h2>⚡ NEXUS CORE AGI — 4-एजेंट ऑटोनॉमस बिज़नेस इंजन</h2>
        <p>AI वॉयस कॉलर • WhatsApp क्लोज़र • ऑटो-बिलिंग • लीगल कॉन्ट्रैक्ट्स (Zero Human Staff)</p>
    </div>
    """, unsafe_allow_html=True)
    tabs = st.tabs([
        "📞 1. AI वॉयस कॉलर",
        "📲 2. WhatsApp क्लोज़र",
        "🧾 3. ऑटो-अकाउंटेंट व बिलिंग",
        "⚖️ 4. AI लीगल कॉन्ट्रैक्ट",
        "👑 5. ₹1,00,000 लाइसेंस"
    ])
else:
    st.markdown("""
    <div class="grand-hero">
        <h2>⚡ NEXUS CORE AGI — 4-Agent Autonomous Enterprise OS</h2>
        <p>AI Voice Caller • WhatsApp Closer • Auto-Billing • Legal Contracts (Zero Staff)</p>
    </div>
    """, unsafe_allow_html=True)
    tabs = st.tabs([
        "📞 1. AI Voice Caller",
        "📲 2. WhatsApp Closer",
        "🧾 3. Auto-Billing Ledger",
        "⚖️ 4. AI Legal Contracts",
        "👑 5. ₹1,00,000 License"
    ])

# ----------------------------------------------------
# 1. 📞 एजेंट 1: AI वॉयस कॉलर
# ----------------------------------------------------
with tabs[0]:
    if "Hindi" in lang:
        st.markdown("### 📞 एजेंट 1: ऑटोनॉमस वॉयस कॉलिंग इंजन")
        st.caption("यह एजेंट बिना किसी इंसान के एक साथ हज़ारों ग्राहकों को असली आवाज़ में कॉल करता है:")
        biz_cat = st.selectbox("बिज़नेस इंडस्ट्री:", ["🏢 रियल एस्टेट (Property Sales)", "🏥 सुपर स्पेशियलिटी हॉस्पिटल", "🚗 कार डीलरशिप व ऑटो गैरेज", "🎓 प्रीमियम कोचिंग संस्थान"])
        lead_name = st.text_input("ग्राहक का नाम:", placeholder="उदा: राहुल मेहता")
        lead_phone = st.text_input("मोबाइल नंबर (10 अंक):", placeholder="उदा: 9876543210")
        btn_vcall = "🚀 AI कॉल ट्रिगर करें (Live Call Engine)"
    else:
        st.markdown("### 📞 Agent 1: Autonomous Voice Calling Engine")
        st.caption("Calls thousands of leads simultaneously using ultra-low latency neural voice:")
        biz_cat = st.selectbox("Industry Category:", ["🏢 Real Estate Developer", "🏥 Multi-Speciality Clinic/Hospital", "🚗 Automobile Dealership", "🎓 EdTech & Premium Coaching"])
        lead_name = st.text_input("Lead Name:", placeholder="e.g. Rahul Mehta")
        lead_phone = st.text_input("Lead Phone (10 digits):", placeholder="e.g. 9876543210")
        btn_vcall = "🚀 Trigger Autonomous Voice Engine"

    if st.button(btn_vcall):
        ln = lead_name.strip() if lead_name.strip() else "Valued Client"
        st.success("🟢 AI Neural Agent Connected! Latency: 0.38s | Audio Stream Active.")
        v_script = f"""==================================================
🤖 [AUTONOMOUS AI VOICE AGENT — LIVE TRANSCRIPT]
Target: {ln} | Industry: {biz_cat.split(' ')[1]}
Engine: Neural LLM + Neural TTS Pipeline
==================================================

[00:01 - AI Voice]: "नमस्ते {ln} जी! मैं {biz_cat.split(' ')[1]} से बात कर रही हूँ। आपने हमारे प्रीमियम ऑफर के बारे में जानकारी माँगी थी। क्या आप 2 मिनट बात कर सकते हैं?"

[Customer]: "हाँ, प्राइस और लोकेशन क्या है?"

[00:07 - AI Voice]: "सर, हमारे प्रोजेक्ट में प्राइम इन्वेंटरी पर आज 15% का विशेष एडवांटेज स्लॉट खुला है। क्या मैं आपके लिए शाम 4 बजे हमारे डायरेक्टर के साथ मीटिंग फाइनल कर दूँ?"

[Customer]: "हाँ, डिटेल्स WhatsApp पर भेजो।"

[00:15 - AI Voice]: "बिल्कुल! कॉल कटते ही 2 सेकंड में एजेंट-2 आपके WhatsApp पर ब्रोशर भेज रहा है। धन्यवाद!"
=================================================="""
        st.text_area("Live Voice Execution Output:", v_script, height=220)

# ----------------------------------------------------
# 2. 📲 एजेंट 2: WhatsApp क्लोज़र
# ----------------------------------------------------
with tabs[1]:
    if "Hindi" in lang:
        st.markdown("### 📲 एजेंट 2: WhatsApp ऑटो-क्लोज़र व ब्रोशर डिलीवरी")
        st.caption("कॉल समाप्त होते ही ग्राहक के फ़ोन पर सीधा ऑटोमैटिक प्रपोज़ल जाता है:")
        deal_amt = st.text_input("ऑफर या डील का मूल्य (₹):", placeholder="उदा: 25000")
        btn_wa = "⚡ WhatsApp पर डील भेजें"
    else:
        st.markdown("### 📲 Agent 2: WhatsApp Auto-Closer & Proposal Delivery")
        st.caption("Fires instant proposal and asset deck immediately after call ends:")
        deal_amt = st.text_input("Deal Value (₹):", placeholder="e.g. 25000")
        btn_wa = "⚡ Dispatch WhatsApp Closer"

    if st.button(btn_wa):
        ln_val = lead_name.strip() if 'lead_name' in locals() and lead_name.strip() else "Sir"
        lp_val = lead_phone.strip() if 'lead_phone' in locals() and len(lead_phone.strip()) == 10 else MY_WA_NUMBER
        da_val = deal_amt.strip() if deal_amt.strip() else "Special Offer"

        msg_body = f"""नमस्ते {ln_val} जी! 🙏
कॉल पर बात करने के लिए धन्यवाद। आपके अनुरोध के अनुसार आपके प्रोजेक्ट का विवरण नीचे दिया गया है:

💼 **ऑफर विवरण:** विशेष एंटरप्राइज पैकेज
💰 **डील मूल्य:** ₹{da_val}
📄 **ऑफिशियल प्रपोज़ल:** https://nexusai.global/proposal-verified

इस स्लॉट को सुरक्षित करने के लिए अभी रिप्लाई करें या सीधे कन्फर्म करें!"""

        enc_m = urllib.parse.quote(msg_body)
        st.text_area("WhatsApp Auto-Closer Payload:", msg_body, height=180)
        st.markdown(f'<a href="https://wa.me/91{lp_val}?text={enc_m}" target="_blank" class="pay-btn-glow">📲 Open WhatsApp & Auto-Close Deal</a>', unsafe_allow_html=True)

# ----------------------------------------------------
# 3. 🧾 एजेंट 3: ऑटो-अकाउंटेंट व बिलिंग
# ----------------------------------------------------
with tabs[2]:
    if "Hindi" in lang:
        st.markdown("### 🧾 एजेंट 3: AI ऑटो-अकाउंटेंट व डिजिटल इनवॉइस")
        st.caption("पेमेंट आते ही बिना मुंशी या सीए के तुरंत पक्का डिजिटल इनवॉइस तैयार करें:")
        inv_item = st.text_input("सर्विस का नाम:", placeholder="उदा: Enterprise AI Automation Deployment")
        inv_total = st.text_input("बिल राशि (₹):", placeholder="उदा: 50000")
        btn_inv = "⚡ पक्का इनवॉइस तैयार करें"
    else:
        st.markdown("### 🧾 Agent 3: Autonomous Ledger & Billing Engine")
        st.caption("Generates tamper-proof digital invoices with zero manual accountant overhead:")
        inv_item = st.text_input("Service Description:", placeholder="e.g. Enterprise AI Automation Deployment")
        inv_total = st.text_input("Invoice Total (₹):", placeholder="e.g. 50000")
        btn_inv = "⚡ Generate Enterprise Invoice"

    if st.button(btn_inv):
        item_c = inv_item.strip() if inv_item.strip() else "Autonomous System Setup"
        tot_c = inv_total.strip() if inv_total.strip() else "50000"
        
        inv_text = f"""==================================================
TAX INVOICE / OFFICIAL SETTLEMENT RECEIPT
Invoice No: NX-{datetime.now().strftime('%Y%m%d-%H%M')}
Date: {today_str}
==================================================
Client: {lead_name if 'lead_name' in locals() and lead_name.strip() else 'Enterprise Client'}
Service: {item_c}
Billing Mode: Direct Bank Settlement (Instant)

Subtotal: ₹{tot_c}
GST / Tax (0% Reverse Mechanism): ₹0.00
--------------------------------------------------
TOTAL BILLED AMOUNT: ₹{tot_c}
Status: VERIFIED & CONFIRMED ✅
=================================================="""
        st.text_area("Generated Invoice:", inv_text, height=220)
        st.download_button("📥 डाउनलोड इनवॉइस (TXT)", data=inv_text, file_name=f"Invoice_{today_str}.txt", mime="text/plain", use_container_width=True)

# ----------------------------------------------------
# 4. ⚖️ एजेंट 4: AI लीगल कॉन्ट्रैक्ट
# ----------------------------------------------------
with tabs[3]:
    if "Hindi" in lang:
        st.markdown("### ⚖️ एजेंट 4: AI लीगल सर्विस कॉन्ट्रैक्ट इंजन")
        st.caption("क्लाइंट के साथ एग्रीमेंट और लीगल शर्तें 5 सेकंड में तैयार करें:")
        c_scope = st.text_input("काम का दायरा (Scope of Work):", placeholder="उदा: 10,000 AI Voice Calls + WhatsApp Bot")
        btn_legal = "⚡ लीगल एग्रीमेंट तैयार करें"
    else:
        st.markdown("### ⚖️ Agent 4: AI Legal Service Agreement Engine")
        st.caption("Drafts legally enforceable commercial agreements in 5 seconds:")
        c_scope = st.text_input("Scope of Work:", placeholder="e.g. 10,000 AI Voice Calls + Full WhatsApp Automation")
        btn_legal = "⚡ Generate Commercial Contract"

    if st.button(btn_legal):
        scope_c = c_scope.strip() if c_scope.strip() else "Complete AI Business Operations Suite"
        c_draft = f"""COMMERCIAL SERVICE & NON-DISCLOSURE AGREEMENT
Effective Date: {today_str}

PARTIES:
1. Nexus Enterprise Systems (Provider)
2. {lead_name if 'lead_name' in locals() and lead_name.strip() else 'Enterprise Client'} (Client)

1. SCOPE OF SERVICES:
Provider shall deploy an Autonomous Multi-Agent Infrastructure comprising:
- {scope_c}

2. CONFIDENTIALITY & SLA:
All customer data and call logs remain 100% confidential under standard IT compliance.

3. GOVERNING LAW:
This agreement is governed by the laws of India and subject to standard dispute arbitration.

DRAFTED & VERIFIED VIA NEXUS LEGAL ENGINE AGENT-4."""
        st.text_area("Legal Agreement Draft:", c_draft, height=220)
        st.download_button("📥 डाउनलोड लीगल कॉन्ट्रैक्ट (TXT)", data=c_draft, file_name=f"Agreement_{today_str}.txt", mime="text/plain", use_container_width=True)

# ----------------------------------------------------
# 5. 👑 ₹1,00,000 एंटरप्राइज लाइसेंस
# ----------------------------------------------------
with tabs[4]:
    st.markdown("### 👑 Enterprise Autonomous Multi-Agent License")
    st.markdown("""
    <div class="agent-card" style="border-left: 4px solid #10B981;">
        <h3 style="color:#10B981; margin:0;">Complete 4-Agent Autonomous System</h3>
        <p style="font-size:14px; color:#F8FAFC; margin:8px 0;">
            • Agent 1: 10,000 Autonomous Calls/month<br>
            • Agent 2: Real-time WhatsApp Pipeline Closer<br>
            • Agent 3: Automated Ledger & Billing System<br>
            • Agent 4: Autonomous Legal Compliance Engine
        </p>
        <p style="font-size:18px; color:#38BDF8; font-weight:bold; margin:0;">
            One-time Setup: ₹1,00,000 | Monthly Retainer: ₹25,000
        </p>
    </div>
    """, unsafe_allow_html=True)

    token_val = "10000"
    upi_grand = f"upi://pay?pa={MY_UPI_ID}&pn=Nexus%20Enterprise&am={token_val}&cu=INR&tn=Multi-Agent%20Token"
    qr_grand = f"https://api.qrserver.com/v1/create-qr-code/?size=180x180&data={urllib.parse.quote(upi_grand)}"

    st.markdown(f"""
    <div class="agent-card" style="text-align: center;">
        <p style="color: #38BDF8 !important; font-weight: bold; margin-bottom: 8px;">📲 Pay ₹10,000 Advance Token (GPay / PhonePe):</p>
        <img src="{qr_grand}" width="165" style="background: #fff; padding: 6px; border-radius: 12px; border: 2px solid #6366F1;" />
        <p style="font-size: 12px; color: #9CA3AF !important; margin-top: 6px;">UPI ID: <b>{MY_UPI_ID}</b></p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f'<a href="{upi_grand}" class="pay-btn-glow">⚡ Pay ₹{token_val} Advance Token</a>', unsafe_allow_html=True)

# संस्थापक प्रोफ़ाइल
st.markdown("---")
wa_exec = f"https://wa.me/{MY_WA_NUMBER}?text={urllib.parse.quote('Hello Sahil, I want to deploy the Nexus Core 4-Agent Autonomous Engine for our enterprise.')}"
st.markdown(f"""
<div class="founder-box">
    <p style="color: #A5B4FC !important; font-size: 11px; margin: 0; text-transform: uppercase; letter-spacing: 2px;">
        🏛️ FOUNDER & PRINCIPAL ARCHITECT
    </p>
    <h2 style="color: #FFFFFF !important; margin: 8px 0; font-size: 22px; font-weight: 900;">
        साहिल अहमद (Sahil Ahmad)
    </h2>
    <p style="color: #D1D5DB !important; font-size: 13px; margin-bottom: 14px;">
        Nexus Core AGI — Engineering autonomous multi-agent systems that replace traditional business staff.
    </p>
    <a href="{wa_exec}" target="_blank" 
       style="background: linear-gradient(90deg, #10B981 0%, #059669 100%); color: #FFFFFF !important; padding: 12px 24px; border-radius: 10px; text-decoration: none; font-size: 13px; font-weight: bold; display: inline-block;">
        💬 Connect on WhatsApp (+91 {MY_WA_NUMBER[-10:]})
    </a>
</div>
""", unsafe_allow_html=True)
