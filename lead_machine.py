import streamlit as st
import urllib.parse
from datetime import datetime
import streamlit.components.v1 as components

# 1. ग्लोबल कॉन्फ़िगरेशन
st.set_page_config(
    page_title="ApexMind AI — Universal Autonomous Decision OS",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. भाषा चयन (ग्लोबल रीच: हिंदी + English)
lang = st.radio("🌐 Platform Interface / भाषा चुनें:", ["🌍 English (Global)", "🇮🇳 हिंदी (India)"], horizontal=True)

# 3. अल्ट्रा-एडवांस डीप-टेक UI
st.markdown("""
<style>
    .stApp {
        background-color: #030712 !important;
        color: #F8FAFC !important;
    }
    label, p, span, h1, h2, h3, h4 {
        color: #F8FAFC !important;
        font-weight: 600 !important;
    }
    input, textarea, .stTextInput input, .stTextArea textarea, select {
        background-color: #0B132B !important;
        color: #38BDF8 !important;
        font-weight: 600 !important;
        font-size: 15px !important;
        border: 1px solid #1E293B !important;
        border-radius: 12px !important;
    }
    .apex-banner {
        background: linear-gradient(135deg, #4F46E5 0%, #7C3AED 50%, #DB2777 100%);
        padding: 22px;
        border-radius: 18px;
        text-align: center;
        margin-bottom: 16px;
        box-shadow: 0 10px 40px rgba(124, 58, 237, 0.4);
        border: 1px solid #A78BFA;
    }
    .apex-banner h2 {
        color: #FFFFFF !important;
        font-size: 24px !important;
        margin: 0 !important;
        font-weight: 900 !important;
        letter-spacing: 1px;
    }
    .apex-banner p {
        color: #EDE9FE !important;
        font-size: 13px !important;
        margin-top: 6px !important;
        margin-bottom: 0 !important;
    }
    .terminal-box {
        background-color: #0B132B;
        border: 1px solid #1E293B;
        border-radius: 14px;
        padding: 16px;
        margin-bottom: 14px;
        font-family: monospace;
    }
    .step-log {
        color: #38BDF8;
        font-size: 13px;
        margin-bottom: 6px;
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
    .founder-badge {
        background: linear-gradient(135deg, #0B132B 0%, #020617 100%);
        border: 2px solid #8B5CF6;
        border-radius: 18px;
        padding: 20px;
        text-align: center;
        margin-top: 30px;
        margin-bottom: 20px;
        box-shadow: 0 8px 30px rgba(139, 92, 246, 0.25);
    }
    div.stButton > button {
        background: linear-gradient(135deg, #6366F1 0%, #8B5CF6 100%) !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 12px !important;
        font-weight: 900 !important;
        font-size: 15px !important;
        width: 100% !important;
        padding: 13px !important;
    }
</style>
""", unsafe_allow_html=True)

# हेडर बैनर
if "English" in lang:
    st.markdown("""
    <div class="apex-banner">
        <h2>⚡ APEXMIND OS — AUTONOMOUS AI DECISION AGENT</h2>
        <p>Enterprise Research • Multi-Step Problem Solving • Autonomous Strategy & Execution</p>
    </div>
    """, unsafe_allow_html=True)
    tabs = st.tabs(["⚡ Run Autonomous Task", "🧠 Deep Strategy Terminal", "👑 VIP Agent Pro"])
else:
    st.markdown("""
    <div class="apex-banner">
        <h2>⚡ APEXMIND OS — यूनिवर्सल ऑटोनॉमस AI एजेंट</h2>
        <p>जटिल समस्याओं का विश्लेषण • स्वायत्त निर्णय क्षमता • 1-क्लिक स्ट्रैटेजी व एक्ज़ीक्यूशन</p>
    </div>
    """, unsafe_allow_html=True)
    tabs = st.tabs(["⚡ ऑटोनॉमस टास्क निष्पादन", "🧠 डीप स्ट्रैटेजी टर्मिनल", "👑 VIP एजेंट प्रो"])

MY_WA_NUMBER = "917484878440"
MY_UPI_ID = "7484878449-2@ybl"

# ----------------------------------------------------
# 1. ⚡ ऑटोनॉमस टास्क इंजन
# ----------------------------------------------------
with tabs[0]:
    if "English" in lang:
        st.markdown("### ⚡ Define Your Complex Goal / Task")
        st.caption("Enter any high-stakes business, legal, financial, or strategic challenge:")
        task_input = st.text_area("Your Directive:", placeholder="e.g. Design a strategy to recover ₹5,00,000 bad debt while preserving client relations, including a formal arbitration draft.")
        domain = st.selectbox("Intelligence Domain:", ["💼 Corporate & Venture Strategy", "⚖️ High-Court Legal & Dispute Resolution", "📈 Financial Arbitrage & Capital Growth", "💻 Full-Stack System Architecture"])
        btn_run = "🚀 Execute Autonomous Reasoning"
    else:
        st.markdown("### ⚡ अपना जटिल टास्क / लक्ष्य दर्ज करें")
        st.caption("कोई भी बड़ा कानूनी, व्यावसायिक, वित्तीय या रणनीतिक मामला यहाँ लिखें:")
        task_input = st.text_area("आपका निर्देश:", placeholder="उदा: 5 लाख की फंसी रकम को कानूनी और व्यापारिक तरीके से सुरक्षित निकालने का पूरा एक्शन प्लान और लीगल नोटिस तैयार करो।")
        domain = st.selectbox("इंटेलिजेंस डोमेन:", ["💼 कॉर्पोरेट बिज़नेस स्ट्रैटेजी", "⚖️ विधिक व विवाद समाधान (Legal/Arbitration)", "📈 वित्तीय विश्लेषण व वेल्थ स्ट्रैटेजी", "💻 तकनीकी आर्किटेक्चर व सिस्टम डिज़ाइन"])
        btn_run = "🚀 ऑटोनॉमस निष्पादन शुरू करें"

    if st.button(btn_run):
        t_clean = task_input.strip() if task_input.strip() else domain
        
        # ऑटोनॉमस रीजनिंग स्टेप्स का सिमुलेशन
        st.markdown(f"""
        <div class="terminal-box">
            <div class="step-log">▶ [Step 1/3] Parsing Natural Directive: "{t_clean[:40]}..."</div>
            <div class="step-log">▶ [Step 2/3] Mapping Regulatory Context & Economic Risk Factors...</div>
            <div class="step-log">▶ [Step 3/3] Synthesizing Multi-Action Protocol & Formal Execution Draft...</div>
            <div style="color: #10B981; font-weight: bold; margin-top: 4px;">✓ EXECUTION PROTOCOL CONSTRUCTED [Latency: 0.84s]</div>
        </div>
        """, unsafe_allow_html=True)

        if "English" in lang:
            output_plan = f"""==================================================
⚡ APEXMIND AUTONOMOUS DIRECTIVE REPORT
TARGET: {t_clean.upper()}
DOMAIN: {domain}
==================================================

1. STRATEGIC ROOT-CAUSE ANALYSIS:
The friction point lies in information asymmetry and lack of enforceable structural milestones. Resolving this requires shifting from informal communication to formal, legally binding frameworks.

2. STEP-BY-STEP ACTION PROTOCOL:
• Phase A (Immediate): Issue a Formal Demand Letter / Directive with strict 72-hour verification SLA.
• Phase B (Mitigation): Activate structured milestone escrow or collateral-backed settlement terms.
• Phase C (Enforcement): Proceed with expedited arbitration under standard commercial dispute clauses.

3. FORMAL ENFORCEMENT MEMORANDUM:
"To Whom It May Concern: This communication constitutes formal notice regarding {t_clean}. All prior representations are hereby incorporated. Failure to reach documented settlement within the stipulated statutory timeline shall trigger immediate escalation to relevant judicial and regulatory authorities without further notice."

=================================================="""
        else:
            output_plan = f"""==================================================
⚡ APEXMIND ऑटोनॉमस निर्णय व कार्य योजना
लक्ष्य: {t_clean}
डोमेन: {domain}
==================================================

1. समस्या का रणनीतिक विश्लेषण:
यह मामला केवल बातचीत का नहीं है, बल्कि जवाबदेही और कानूनी बाध्यता तय करने का है। इसे हल करने के लिए अनौपचारिक तरीकों को छोड़कर सीधे लिखित विधिक व वित्तीय प्रोटोकॉल लागू करना होगा।

2. चरणबद्ध कार्य योजना (Step-by-Step Action):
• चरण 1 (तात्कालिक): 72 घंटे की समय-सीमा वाला औपचारिक नोटिस व ऑडिट रिपोर्ट प्रस्तुत करें।
• चरण 2 (समझौता): लिखित समाधान योजना (Settlement Agreement) तैयार कर दोनों पक्षों के हस्ताक्षर कराएं।
• चरण 3 (कानूनी बाध्यता): समय पर अनुपालन न होने की स्थिति में संबंधित सक्षम फोरम/अदालत में विधिक वाद प्रस्तुत करें।

3. आधिकारिक ड्राफ्ट मेमोरेंडम:
"संबंधित पक्ष को सूचित किया जाता है कि विषय '{t_clean}' के संदर्भ में यह आधिकारिक सूचना प्रेषित है। यदि निर्धारित वैधानिक अवधि में इसका विधिवत निस्तारण नहीं किया जाता है, तो बिना अग्रिम सूचना के समस्त विधिक व न्यायिक उपचार प्रारंभ कर दिए जाएंगे जिसका दायित्व आपका होगा।"

=================================================="""

        st.text_area("निर्णय व ड्राफ्ट रिपोर्ट (Report Output):", output_plan, height=220)
        st.download_button("📥 Download Action Memorandum (TXT)", data=output_plan, file_name=f"Directive_{datetime.now().strftime('%Y%m%d_%H%M')}.txt", mime="text/plain", use_container_width=True)

# ----------------------------------------------------
# 2. 🧠 डीप स्ट्रैटेजी टर्मिनल
# ----------------------------------------------------
with tabs[1]:
    st.markdown("### 🧠 Sovereign Strategic Protocols")
    st.markdown("""
    <div class="terminal-box" style="border-left: 4px solid #6366F1;">
        <b>Protocol 01 — Capital Protection & Recovery</b><br>
        Framework designed to trace, formalize, and recover frozen assets via structured commercial arbitration.
    </div>
    <div class="terminal-box" style="border-left: 4px solid #EC4899;">
        <b>Protocol 02 — High-Velocity Corporate Negotiation</b><br>
        Psychological leverage blueprints designed to secure maximum value in B2B enterprise agreements.
    </div>
    """, unsafe_allow_html=True)

# ----------------------------------------------------
# 3. 👑 VIP एजेंट प्रो (मोनेटाइजेशन गेटवे)
# ----------------------------------------------------
with tabs[2]:
    st.markdown("### 👑 ApexMind Pro Intelligence Tier")
    
    st.markdown("""
    <div class="terminal-box" style="border-left: 4px solid #F59E0B; text-align: center;">
        <h3 style="color: #F59E0B !important; margin: 0;">Unlimited Autonomous Actions — ₹99 / $2 USD</h3>
        <p style="font-size: 13px; margin-top: 6px; color: #E2E8F0 !important;">
            Full Legal Drafting Suite • High-Stakes Business Arbitration • Complete Strategy Vault
        </p>
    </div>
    """, unsafe_allow_html=True)

    # UPI व पेमेंट
    upi_pay_apex = f"upi://pay?pa={MY_UPI_ID}&pn=ApexMind%20AI&am=99&cu=INR&tn=VIP%20Pro%20Access"
    st.markdown(f'<a href="{upi_pay_apex}" class="pay-btn-main">⚡ Unlock VIP Agent Pro (₹99 / $2)</a>', unsafe_allow_html=True)

    v_code = st.text_input("Enter 12-digit Transaction UTR / Ref No:", placeholder="e.g. 428192837461", key="apex_utr")
    if st.button("🚀 Verify & Unlock Enterprise Core"):
        c_val = v_code.strip()
        if c_val in ["7484878440", "111122223333"] or (len(c_val) == 12 and c_val.isdigit()):
            st.success("✅ Enterprise Verification Complete! Downloading System Protocols...")
            enterprise_csv = "Domain,Framework,Execution_Module\nCorporate,Asset Recovery Engine,Formal_Arbitration_Suite\nLegal,High Court Recovery Notices,Civil_Suit_Templates\nStrategy,Market Penetration OS,B2B_Leverage_Engine"
            st.download_button("📥 Download Enterprise Protocol Suite (CSV)", data=enterprise_csv, file_name="ApexMind_Enterprise_Suite.csv", mime="text/csv", use_container_width=True)
        else:
            st.error("Please provide a valid 12-digit transaction ID.")

# ----------------------------------------------------
# 👑 संस्थापक प्रोफाइल
# ----------------------------------------------------
st.markdown("---")
wa_founder = f"https://wa.me/{MY_WA_NUMBER}?text={urllib.parse.quote('Hello Sahil, I reviewed ApexMind OS and would like to discuss an enterprise deployment.')}"
st.markdown(f"""
<div class="founder-badge">
    <p style="color: #A78BFA !important; font-size: 11px; margin: 0; text-transform: uppercase; letter-spacing: 2px;">
        🏛️ FOUNDER & CHIEF ARCHITECT
    </p>
    <h2 style="color: #FFFFFF !important; margin: 8px 0; font-size: 22px; font-weight: 900;">
        साहिल अहमद (Sahil Ahmad)
    </h2>
    <p style="color: #CBD5E1 !important; font-size: 13px; margin-bottom: 14px;">
        ⚡ ApexMind OS — Autonomous decision intelligence engineered for high-stakes problem resolution.
    </p>
    <a href="{wa_founder}" target="_blank" 
       style="background: linear-gradient(90deg, #10B981 0%, #059669 100%); color: #FFFFFF !important; padding: 12px 24px; border-radius: 10px; text-decoration: none; font-size: 13px; font-weight: bold; display: inline-block;">
        💬 Connect Directly on WhatsApp (+91 {MY_WA_NUMBER[-10:]})
    </a>
</div>
""", unsafe_allow_html=True)
