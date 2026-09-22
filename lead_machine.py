import streamlit as st
import urllib.parse
from datetime import datetime

# Ultra Global Configuration
st.set_page_config(
    page_title="Universal AI — Har Insaan Ka AI Assistant",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Language Selector
lang = st.radio("🌐 Bhasha Chunein / Select Language:", ["🇮🇳 Hindi", "🌍 English"], horizontal=True)

# Neon Super-App Dark UI
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
        background: linear-gradient(135deg, #7C3AED 0%, #2563EB 50%, #06B6D4 100%);
        padding: 24px;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 10px 40px rgba(124, 58, 237, 0.4);
        border: 1px solid #A78BFA;
    }
    .god-banner h2 {
        color: #FFFFFF !important;
        font-size: 24px !important;
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
        background: linear-gradient(135deg, #7C3AED 0%, #2563EB 100%) !important;
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
        <h2>🧠 UNIVERSAL LIFE-OS — दुनिया का हर समाधान</h2>
        <p>AI पॉकेट वकील • सरकारी योजना व लोन फाइंडर • इंस्टेंट जॉब और रेज़्युमे इंजन</p>
    </div>
    """, unsafe_allow_html=True)
    tabs = st.tabs([
        "⚖️ 1. AI पॉकेट वकील (Legal)",
        "🏛️ 2. सरकारी योजना व सब्सिडी",
        "📄 3. AI रेज़्युमे व जॉब इंजन",
        "👑 4. VIP लाइफटाइम एक्सेस (₹99)"
    ])
else:
    st.markdown("""
    <div class="god-banner">
        <h2>🧠 UNIVERSAL LIFE-OS — The All-in-One AI Solver</h2>
        <p>AI Pocket Lawyer • Government Schemes Finder • Instant Job & Resume Engine</p>
    </div>
    """, unsafe_allow_html=True)
    tabs = st.tabs([
        "⚖️ 1. AI Pocket Lawyer",
        "🏛️ 2. Gov Schemes & Subsidies",
        "📄 3. Instant Job Resume AI",
        "👑 4. VIP Lifetime Access (₹99)"
    ])

# ----------------------------------------------------
# 1. ⚖️ AI POCKET LAWYER
# ----------------------------------------------------
with tabs[0]:
    if "Hindi" in lang:
        st.markdown("### ⚖️ AI पॉकेट वकील — कानूनी सलाह व ड्राफ्ट")
        st.caption("किसी भी विवाद, फंसा हुआ पैसा या परेशानी के लिए कानूनी अधिकार जानें:")
        issue_type = st.selectbox("समस्या चुनें:", [
            "💰 किसी ने पैसा लेकर वापस नहीं दिया (Cheating / Fraud)",
            "🏠 मकान मालिक / किराएदार का विवाद",
            "👮 पुलिस चालान या बेवजह की परेशानी",
            "🛒 खराब सामान मिला और दुकानदार रिफंड नहीं दे रहा (Consumer Rights)"
        ])
        op_party = st.text_input("सामने वाले का नाम / कंपनी:", placeholder="उदा: रवि कुमार / XYZ इलेक्ट्रॉनिक्स")
        issue_amt = st.text_input("फंसा हुआ रुपया (₹):", placeholder="उदा: 15000")
        btn_law = "⚡ लीगल नोटिस व सलाह तैयार करें"
    else:
        st.markdown("### ⚖️ AI Pocket Lawyer — Instant Legal Notice")
        issue_type = st.selectbox("Select Legal Issue:", [
            "💰 Money Recovery / Fraud / Cheating",
            "🏠 Landlord / Tenant Dispute",
            "👮 Traffic Challan / Undue Harassment",
            "🛒 Defective Product & Refund Denied (Consumer Court)"
        ])
        op_party = st.text_input("Opposite Party Name / Company:", placeholder="e.g. John Doe / XYZ Store")
        issue_amt = st.text_input("Disputed Amount (₹ / $):", placeholder="e.g. 15000")
        btn_law = "⚡ Generate Legal Notice & Advice"

    if st.button(btn_law):
        op_clean = op_party.strip() if op_party.strip() else "Opposite Party"
        amt_clean = issue_amt.strip() if issue_amt.strip() else "Applicable Amount"
        
        legal_draft = f"""🚨 LEGAL ACTION NOTICE & RIGHT ADVISORY
Date: {datetime.now().strftime('%d-%m-%Y')}
To: {op_clean}

Subject: Urgent Demand Notice regarding unresolved matter ({issue_type.split('(')[0]})

Take notice that an amount of ₹{amt_clean} / issue remains unlawfully withheld despite repeated follow-ups. Under Section 420/406 IPC & Consumer Protection Act 2019, failure to settle within 7 days will trigger immediate formal proceedings at your sole cost and liability.

Drafted via Universal AI Legal Engine."""
        
        st.text_area("तैयार कानूनी नोटिस (Legal Notice Draft):", legal_draft, height=220)
        enc_leg = urllib.parse.quote(legal_draft)
        st.markdown(f'<a href="https://wa.me/?text={enc_leg}" target="_blank" class="pay-btn-glow" style="background:#DC2626;">📲 WhatsApp पर लीगल चेतावनी भेजें</a>', unsafe_allow_html=True)

# ----------------------------------------------------
# 2. 🏛️ SCHEMES & SUBSIDY FINDER
# ----------------------------------------------------
with tabs[1]:
    if "Hindi" in lang:
        st.markdown("### 🏛️ सरकारी योजना व सब्सिडी फाइंडर")
        st.caption("अपनी श्रेणी चुनें — सरकार आपको कौनसे लाभ दे रही है तुरंत जानें:")
        age_grp = st.selectbox("आयु वर्ग:", ["18 से 25 वर्ष (युवा/छात्र)", "25 से 45 वर्ष (व्यापारी/श्रमिक)", "45 वर्ष से अधिक"])
        occ_type = st.selectbox("पेशा / श्रेणी:", ["विद्यार्थी (Student)", "छोटा दुकानदार / रेहड़ी पटरी", "किसान / ग्रामीण", "महिला उद्यमी"])
        btn_sch = "🔍 मेरे लिए योजनाएं खोजें"
    else:
        st.markdown("### 🏛️ Government Schemes & Subsidy Finder")
        age_grp = st.selectbox("Age Group:", ["18-25 Years", "25-45 Years", "45+ Years"])
        occ_type = st.selectbox("Category:", ["Student", "Small Business / Retail", "Farmer / Rural", "Women Entrepreneur"])
        btn_sch = "🔍 Find Eligible Schemes"

    if st.button(btn_sch):
        st.markdown(f"""
        <div class="feature-card" style="border-left: 4px solid #06B6D4;">
            <h4 style="color:#06B6D4; margin:0;">🎯 आपके लिए शीर्ष योजनाएं:</h4>
            <p style="margin:8px 0; font-size:14px;">
                1. <b>PM मुद्रा योजना (PMMY):</b> बिना किसी गारंटी के ₹50,000 से ₹10 लाख तक का बिजनेस लोन।<br>
                2. <b>PM स्वनिधि योजना:</b> ₹10,000 से ₹50,000 का सीधा कार्यशील पूंजी लोन सीधे बैंक खाते में।<br>
                3. <b>कौशल विकास व फ्री सर्टिफिकेट ट्रेनिंग:</b> सरकारी छात्रवृत्ति व मान्यता प्राप्त सर्टिफिकेट।
            </p>
            <p style="font-size:12px; color:#9CA3AF;">पात्रता: आधार कार्ड + बैंक खाता अनिवार्य।</p>
        </div>
        """, unsafe_allow_html=True)

# ----------------------------------------------------
# 3. 📄 AI RESUME & JOB APPLICATION
# ----------------------------------------------------
with tabs[2]:
    if "Hindi" in lang:
        st.markdown("### 📄 1-क्लिक इंटरनेशनल AI रेज़्युमे इंजन")
        u_name = st.text_input("आपका नाम:", placeholder="उदा: राहुल शर्मा")
        u_skill = st.text_input("आपके हुनर (Skills / Work):", placeholder="उदा: सेल्स, कंप्यूटर, ड्राइविंग, अकाउंटिंग")
        btn_res = "🚀 1-पेज रेज़्युमे तैयार करें"
    else:
        st.markdown("### 📄 1-Click International AI Resume")
        u_name = st.text_input("Your Name:", placeholder="e.g. John Smith")
        u_skill = st.text_input("Your Key Skills:", placeholder="e.g. Sales, Python, Marketing, Accounting")
        btn_res = "🚀 Generate Resume"

    if st.button(btn_res):
        un = u_name.strip() if u_name.strip() else "Professional Candidate"
        us = u_skill.strip() if u_skill.strip() else "Business Operations & Communication"
        
        resume_out = f"""==================================================
📄 PROFESSIONAL CV / RESUME
Candidate: {un}
Contact: Available on Request
==================================================

🎯 EXECUTIVE SUMMARY:
Dedicated and results-oriented professional with strong expertise in {us}. Proven capability to deliver high efficiency and growth.

⚡ CORE COMPETENCIES:
• {us}
• Client Handling & Negotiation
• Problem Solving & Critical Execution

💼 WORK EXPERIENCE:
Independent Professional | 2024 - Present
• Spearheaded operations and client delivery with 100% accuracy.
• Handled tech and customer relationships seamlessly.
=================================================="""
        st.text_area("तैयार रेज़्युमे:", resume_out, height=220)
        st.download_button("📥 रेज़्युमे डाउनलोड करें (TXT)", data=resume_out, file_name=f"{un}_Resume.txt", mime="text/plain", use_container_width=True)

# ----------------------------------------------------
# 4. 👑 VIP ACCESS (₹99 MICRO-PAYMENT)
# ----------------------------------------------------
with tabs[3]:
    st.markdown("### 👑 यूनिवर्सल VIP लाइफटाइम पास (सिर्फ ₹99)")
    st.caption("चूंकि यह हर आम इंसान के लिए है, इसलिए इसकी फीस मात्र ₹99 रखी गई है ताकि लाखों लोग इसे तुरंत खरीदें!")
    
    pay_price = "99"
    upi_uni = f"upi://pay?pa={MY_UPI_ID}&pn=Universal%20AI&am={pay_price}&cu=INR&tn=VIP%20Access"
    qr_uni = f"https://api.qrserver.com/v1/create-qr-code/?size=180x180&data={urllib.parse.quote(upi_uni)}"

    st.markdown(f"""
    <div class="feature-card" style="text-align: center;">
        <p style="color: #38BDF8 !important; font-weight: bold; margin-bottom: 8px;">📲 PhonePe / GPay से ₹99 स्कैन करके एक्टिवेट करें:</p>
        <img src="{qr_uni}" width="165" style="background: #fff; padding: 6px; border-radius: 12px; border: 2px solid #7C3AED;" />
        <p style="font-size: 12px; color: #9CA3AF !important; margin-top: 6px;">UPI ID: <b>{MY_UPI_ID}</b></p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f'<a href="{upi_uni}" class="pay-btn-glow">⚡ सीधे ₹{pay_price} पे करें (Instant Unlock)</a>', unsafe_allow_html=True)

# FOUNDER BANNER
st.markdown("---")
wa_ceo = f"https://wa.me/{MY_WA_NUMBER}?text={urllib.parse.quote('Hello Sahil, I want to use Universal AI Super-App.')}"
st.markdown(f"""
<div class="founder-box">
    <p style="color: #A78BFA !important; font-size: 11px; margin: 0; text-transform: uppercase; letter-spacing: 2px;">
        🏛️ FOUNDER & TECH ARCHITECT
    </p>
    <h2 style="color: #FFFFFF !important; margin: 8px 0; font-size: 22px; font-weight: 900;">
        साहिल अहमद (Sahil Ahmad)
    </h2>
    <p style="color: #D1D5DB !important; font-size: 13px; margin-bottom: 14px;">
        Universal AI — हर आम इंसान की कानूनी, आर्थिक और नौकरी से जुड़ी समस्याओं को 5 सेकंड में हल करने वाला सुपर-इंजन।
    </p>
    <a href="{wa_ceo}" target="_blank" 
       style="background: linear-gradient(90deg, #10B981 0%, #059669 100%); color: #FFFFFF !important; padding: 12px 24px; border-radius: 10px; text-decoration: none; font-size: 13px; font-weight: bold; display: inline-block;">
        💬 सीधे WhatsApp (+91 {MY_WA_NUMBER[-10:]}) पर जुड़ें
    </a>
</div>
""", unsafe_allow_html=True)
    
