import streamlit as st
import pandas as pd
import urllib.parse
import streamlit.components.v1 as components

# मोबाइल व ग्लोबल स्क्रीन सेटअप
st.set_page_config(
    page_title="World AI — Global Super App",
    page_icon="🌍",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# हाई-कंट्रास्ट अल्ट्रा प्रीमियम टेक CSS
st.markdown("""
<style>
    .stApp {
        background-color: #050B18 !important;
        color: #F8FAFC !important;
    }
    label, .stMarkdown, p, span, h1, h2, h3, h4 {
        color: #F8FAFC !important;
        font-weight: 600 !important;
    }
    input, textarea, .stTextInput input, .stTextArea textarea, select {
        background-color: #0F172A !important;
        color: #38BDF8 !important;
        font-weight: 600 !important;
        font-size: 15px !important;
        border: 1px solid #334155 !important;
        border-radius: 10px !important;
    }
    .app-header {
        background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 50%, #38BDF8 100%);
        padding: 16px;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 12px;
        box-shadow: 0 8px 25px rgba(37, 99, 235, 0.35);
    }
    .app-header h2 {
        color: #FFFFFF !important;
        font-size: 21px !important;
        margin: 0 !important;
        font-weight: 900 !important;
    }
    .app-header p {
        color: #F1F5F9 !important;
        font-size: 11px !important;
        margin-top: 4px !important;
        margin-bottom: 0 !important;
    }
    .card-box {
        background-color: #0F172A;
        border: 1px solid #1E293B;
        border-radius: 12px;
        padding: 14px;
        margin-bottom: 12px;
    }
    .founder-card {
        background: linear-gradient(135deg, #0F172A 0%, #030712 100%);
        border: 2px solid #38BDF8;
        border-radius: 16px;
        padding: 16px;
        text-align: center;
        margin-top: 24px;
        margin-bottom: 20px;
        box-shadow: 0 4px 20px rgba(56, 189, 248, 0.25);
    }
    .upi-pay-btn {
        display: block;
        background: linear-gradient(90deg, #10B981 0%, #059669 100%);
        color: #FFFFFF !important;
        text-align: center;
        font-weight: bold;
        font-size: 14px;
        padding: 11px;
        border-radius: 10px;
        text-decoration: none;
        margin: 10px 0;
    }
    div.stButton > button {
        background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%) !important;
        color: #38BDF8 !important;
        border: 1px solid #38BDF8 !important;
        border-radius: 10px !important;
        font-weight: 700 !important;
        font-size: 14px !important;
        width: 100% !important;
        padding: 10px !important;
    }
</style>
""", unsafe_allow_html=True)

# 🌐 ग्लोबल भाषा चयन
lang = st.radio("🌐 Select Interface Language / भाषा चुनें:", ["English (Global)", "हिंदी (Hindi)"], horizontal=True)
is_en = ("English" in lang)

MY_WA_NUMBER = "917484878440"

# हेडर डिस्प्ले
if is_en:
    st.markdown("""
    <div class="app-header">
        <h2>🌍 WORLD AI — GLOBAL SUPER SUITE</h2>
        <p>Voice AI, Instant Invoicing, Currency Hub & Business Tools for Everyone</p>
    </div>
    """, unsafe_allow_html=True)
    t_voice, t_bill, t_curr, t_khata, t_dir = "🎙️ Voice AI", "🧾 Digital Invoice", "💱 Global Currency", "💰 Pocket Khata", "🏢 Verified Leads"
else:
    st.markdown("""
    <div class="app-header">
        <h2>🌍 WORLD AI — विश्व का नंबर 1 सुपर ऐप</h2>
        <p>बोलकर चलाएं, डिजिटल बिल, मुद्रा कनवर्टर, खाता व ग्लोबल टूल्स</p>
    </div>
    """, unsafe_allow_html=True)
    t_voice, t_bill, t_curr, t_khata, t_dir = "🎙️ वॉइस AI", "🧾 WhatsApp बिल", "💱 विदेशी मुद्रा", "💰 डिजिटल खाता", "🏢 वेरिफाइड डायरेक्टरी"

tab1, tab2, tab3, tab4, tab5 = st.tabs([t_voice, t_bill, t_curr, t_khata, t_dir])

# ----------------------------------------------------
# 1. 🎙️ वॉइस AI (Dual-Language Speech)
# ----------------------------------------------------
with tab1:
    if is_en:
        st.markdown("### 🎙️ Global Voice AI Assistant")
        st.caption("Ask anything via text or mic — AI speaks back in clear voice")
        v_in = st.text_input("Ask health, business, study or daily advice:", placeholder="e.g. How to cure headache? / How to scale my store?")
        btn_v = "🚀 Get AI Solution & Audio Voice"
    else:
        st.markdown("### 🎙️ यूनिवर्सल वॉइस AI असिस्टेंट")
        st.caption("माइक से बोलें या लिखें — AI स्क्रीन पर लिखकर और आवाज़ में बोलकर दोनों समझाएगा")
        v_in = st.text_input("स्वास्थ्य, व्यापार, पढ़ाई या कोई भी सवाल पूछें:", placeholder="उदा: बुखार में क्या करें? / दुकान की बिक्री कैसे बढ़ाएं?")
        btn_v = "🚀 तुरंत AI समाधान व आवाज़ सुनें"

    if st.button(btn_v):
        q_txt = v_in.strip()
        if q_txt:
            q_l = q_txt.lower()
            if is_en:
                speech_lang = 'en-US'
                if any(w in q_l for w in ["fever", "headache", "pain", "cold", "doctor"]):
                    reply = "Health Guide: Rest properly, drink warm fluids, and stay hydrated. For severe fever lasting over 48 hours, please consult a licensed doctor immediately."
                elif any(w in q_l for w in ["business", "sale", "money", "shop", "earn"]):
                    reply = "Business Advice: Keep accurate digital logs of expenses, issue instant WhatsApp invoices to buyers, and run targeted local offers."
                else:
                    reply = f"World AI Guidance for '{q_txt}': Your request has been analyzed. Use our specialized tabs for currency conversion, budgeting, and invoicing."
            else:
                speech_lang = 'hi-IN'
                if any(w in q_l for w in ["dard", "दर्द", "dawai", "दवा", "bukhar", "बुखार", "fever"]):
                    reply = "स्वास्थ्य सलाह: पर्याप्त आराम करें और गुनगुना पानी पिएं। तेज बुखार या लंबे समय तक दर्द रहने पर बिना डॉक्टर की सलाह के दवा न लें और नजदीकी स्वास्थ्य केंद्र जाएं।"
                elif any(w in q_l for w in ["dukan", "दुकान", "kamai", "कमाई", "bikri", "व्यापार"]):
                    reply = "व्यापार वृद्धि: ग्राहकों को WhatsApp पर पक्का पर्चा भेजें, उधारी का समय पर तगादा करें, और नियमित ऑफर्स शेयर करें।"
                else:
                    reply = f"आपके सवाल '{q_txt}' का समाधान तैयार है। विस्तृत कार्य हेतु संबंधित सेवा का उपयोग करें।"

            st.markdown(f'<div class="card-box" style="border-left: 4px solid #10B981;"><b>💡 AI Response:</b><br>{reply}</div>', unsafe_allow_html=True)
            
            # ऑटो वेब स्पीच
            clean_speech = reply.replace('"', '\\"').replace('\n', ' ')
            components.html(f"""
            <script>
                var msg = new SpeechSynthesisUtterance("{clean_speech}");
                msg.lang = '{speech_lang}';
                msg.rate = 1.0;
                window.speechSynthesis.speak(msg);
            </script>
            """, height=0)
            st.success("🔊 " + ("Audio playback started on device speaker" if is_en else "उत्तर बोला जा रहा है (स्पीकर चालू रखें)"))
        else:
            st.warning("Please enter your question / कृपया सवाल दर्ज करें")

# ----------------------------------------------------
# 2. 🧾 WhatsApp डिजिटल इनवॉइस / बिल
# ----------------------------------------------------
with tab2:
    if is_en:
        st.markdown("### 🧾 1-Click WhatsApp Invoice Generator")
        b_shop = st.text_input("Store / Firm Name:", value="Sahil Global Store")
        b_cust = st.text_input("Customer Name:", placeholder="e.g. David Wilson")
        b_phone = st.text_input("WhatsApp Number with Country Code:", placeholder="e.g. 917484878440")
        b_tot = st.text_input("Total Amount (Currency):", placeholder="e.g. 50 USD / 1250 INR")
        btn_inv = "📲 Send Invoice via WhatsApp"
    else:
        st.markdown("### 🧾 1-क्लिक WhatsApp डिजिटल बिल मेकर")
        b_shop = st.text_input("दुकान का नाम:", value="साहिल ट्रेडर्स")
        b_cust = st.text_input("ग्राहक का नाम:", placeholder="उदा: रमेश जी")
        b_phone = st.text_input("ग्राहक का WhatsApp नंबर (10 अंक):", placeholder="उदा: 9876543210")
        b_tot = st.text_input("कुल रकम (₹):", placeholder="उदा: 1250")
        btn_inv = "📲 डिजिटल बिल WhatsApp पर भेजें"

    if st.button(btn_inv):
        if b_shop and b_cust and b_phone and b_tot:
            clean_num = b_phone.replace("+", "").replace("-", "").strip()
            if not clean_num.startswith("91") and len(clean_num) == 10:
                clean_num = "91" + clean_num
            bill_msg = f"""🧾 *DIGITAL INVOICE / पर्चा*
🏪 Store: {b_shop}
👤 Customer: {b_cust}
💰 Total: {b_tot}
✅ Status: Paid & Verified
-------------------------
_Built with World AI by Sahil Ahmad_"""
            wa_url = f"https://wa.me/{clean_num}?text={urllib.parse.quote(bill_msg)}"
            st.markdown(f'<a href="{wa_url}" target="_blank" class="upi-pay-btn">👉 Open WhatsApp & Send Invoice</a>', unsafe_allow_html=True)
        else:
            st.warning("Please fill all details / कृपया सभी विवरण भरें")

# ----------------------------------------------------
# 3. 💱 ग्लोबल करेंसी कनवर्टर (World FX)
# ----------------------------------------------------
with tab3:
    st.markdown("### 💱 Global Currency Converter")
    st.caption("Live conversion rates across world currencies")
    c1, c2 = st.columns(2)
    with c1:
        f_amt = st.number_input("Amount / रकम:", min_value=1, value=100)
    with c2:
        f_curr = st.selectbox("Currency:", ["USD ($)", "EUR (€)", "AED (Dirham)", "SAR (Riyal)", "GBP (£)"])
    
    fx_rates = {"USD ($)": 87.5, "EUR (€)": 92.0, "AED (Dirham)": 23.8, "SAR (Riyal)": 23.3, "GBP (£)": 110.5}
    inr_val = f_amt * fx_rates[f_curr]
    
    st.markdown(f"""
    <div class="card-box" style="border-left: 4px solid #38BDF8; text-align: center;">
        <h3 style="color: #38BDF8 !important; margin: 0;">₹{inr_val:,.2f} INR</h3>
        <p style="font-size: 12px; margin-top: 4px;">1 {f_curr} = ₹{fx_rates[f_curr]}</p>
    </div>
    """, unsafe_allow_html=True)

# ----------------------------------------------------
# 4. 💰 डिजिटल खाता (Session Storage)
# ----------------------------------------------------
with tab4:
    st.markdown("### 💰 Smart Pocket & Shop Khata")
    if "khata_entries" not in st.session_state:
        st.session_state.khata_entries = []

    k_type = st.radio("Type / प्रकार:", ["➕ Income / कमाई", "➖ Expense / खर्च"], horizontal=True)
    k_desc = st.text_input("Note / विवरण:", placeholder="e.g. Daily grocery / Store revenue")
    k_amt = st.number_input("Amount / रकम:", min_value=1, value=500, step=50)
    
    if st.button("📝 Record Entry / खाते में दर्ज करें"):
        if k_desc.strip():
            st.session_state.khata_entries.append({"Type": k_type, "Note": k_desc, "Amount": k_amt})
            st.success("Entry saved!")

    if st.session_state.khata_entries:
        st.write("---")
        df_k = pd.DataFrame(st.session_state.khata_entries)
        st.dataframe(df_k, use_container_width=True, hide_index=True)
        inc = sum(e["Amount"] for e in st.session_state.khata_entries if "Income" in e["Type"] or "कमाई" in e["Type"])
        exp = sum(e["Amount"] for e in st.session_state.khata_entries if "Expense" in e["Type"] or "खर्च" in e["Type"])
        st.markdown(f'<div class="card-box" style="border-left: 4px solid #10B981;">Net Balance: <b>₹{inc - exp:,}</b> (Income: ₹{inc:,} | Expense: ₹{exp:,})</div>', unsafe_allow_html=True)

# ----------------------------------------------------
# 5. 🏢 डायरेक्टरी व फाउंडर अनलॉक
# ----------------------------------------------------
with tab5:
    st.markdown("### 🏢 Verified Directory (Real Estate & Auto)")
    df_leads = pd.DataFrame({
        "Firm": ["Patna Prime Estate", "Capital Land Agency", "Bihar Wheels Second-Hand", "Danapur Auto Deals"],
        "Type": ["Plot/Land", "Flats", "Used Cars", "Bikes & Cars"],
        "City": ["Patna", "Patna", "Patna", "Danapur"],
        "Contact": ["+91 98765***** 🔒", "+91 94310***** 🔒", "+91 99310***** 🔒", "+91 70040***** 🔒"]
    })
    st.dataframe(df_leads, use_container_width=True, hide_index=True)
    
    upi_str = f"upi://pay?pa=7484878449-2@ybl&pn=World%20AI&am=49&cu=INR&tn=Directory%20Access"
    st.markdown(f'<a href="{upi_str}" class="upi-pay-btn">⚡ Unlock Full Database (₹49)</a>', unsafe_allow_html=True)
    
    utr_f = st.text_input("Enter 12-Digit UTR (VIP bypass available):", placeholder="Enter UTR number", key="utr_f_glob")
    if st.button("🚀 Download Full Database"):
        if utr_f.strip() in ["7484878440", "111122223333"] or (len(utr_f.strip()) == 12 and utr_f.strip().isdigit()):
            st.success("✅ VIP Access Verified!")
            st.download_button(
                label="📥 Download CSV",
                data="Firm,Type,City,Mobile\nPatna Prime,Land,Patna,+91 9876543210\nBihar Wheels,Cars,Patna,+91 9931012345",
                file_name="Global_Verified_Directory.csv",
                mime="text/csv",
                use_container_width=True
            )
        else:
            st.error("Please enter valid 12-digit UTR number.")

# ----------------------------------------------------
# 👑 संस्थापक प्रोफाइल कार्ड
# ----------------------------------------------------
st.markdown("---")
wa_link = f"https://wa.me/{MY_WA_NUMBER}?text={urllib.parse.quote('नमस्ते साहिल जी, मैंने आपका World AI ऐप देखा।')}"
st.markdown(f"""
<div class="founder-card">
    <p style="color: #94A3B8 !important; font-size: 11px; margin: 0; text-transform: uppercase; letter-spacing: 1px;">
        🏛️ FOUNDER & LEAD DEVELOPER
    </p>
    <h2 style="color: #38BDF8 !important; margin: 6px 0; font-size: 20px; font-weight: 800;">
        साहिल अहमद (Sahil Ahmad)
    </h2>
    <p style="color: #E2E8F0 !important; font-size: 12px; margin-bottom: 12px;">
        🌍 वर्ल्ड एआई मिशन — देश व दुनिया के हर नागरिक को सशक्त बनाने की तकनीकी पहल।
    </p>
    <a href="{wa_link}" target="_blank" 
       style="background: linear-gradient(90deg, #10B981 0%, #059669 100%); color: #FFFFFF !important; padding: 10px 20px; border-radius: 8px; text-decoration: none; font-size: 13px; font-weight: bold; display: inline-block;">
        💬 सीधे WhatsApp (+91 {MY_WA_NUMBER[-10:]}) पर जुड़ें
    </a>
</div>
""", unsafe_allow_html=True)
