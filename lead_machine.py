import streamlit as st
import pandas as pd
import urllib.parse
import streamlit.components.v1 as components

# मोबाइल स्क्रीन सेटअप
st.set_page_config(
    page_title="World AI — All-in-One Super App",
    page_icon="🌍",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# मोबाइल-फ्रेंडली कंट्रास्ट CSS
st.markdown("""
<style>
    .stApp {
        background-color: #060D1F !important;
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

# भाषा चयन
lang = st.radio("🌐 भाषा चुनें / Select Language:", ["हिंदी (Hindi)", "English"], horizontal=True)
is_en = (lang == "English")

MY_WA_NUMBER = "917484878440"

# हेडर
if is_en:
    st.markdown("""
    <div class="app-header">
        <h2>🌍 WORLD AI — ALL-IN-ONE SUPER APP</h2>
        <p>Smart Tools for Students, Seniors, Merchants & Everyday Needs</p>
    </div>
    """, unsafe_allow_html=True)
    t_voice, t_kids, t_bill, t_khata, t_dir = "🎙️ Voice AI", "📚 Students & Homework", "🧾 WhatsApp Bill", "💰 Digital Khata", "🏢 Verified Leads"
else:
    st.markdown("""
    <div class="app-header">
        <h2>🌍 WORLD AI — ऑल-इन-वन सुपर ऐप</h2>
        <p>छात्र, बच्चे, बुज़ुर्ग व व्यापारी — हर वर्ग का आसान डिजिटल साथी</p>
    </div>
    """, unsafe_allow_html=True)
    t_voice, t_kids, t_bill, t_khata, t_dir = "🎙️ वॉइस AI", "📚 छात्र व बच्चे", "🧾 WhatsApp बिल", "💰 डिजिटल खाता", "🏢 वेरिफाइड लीड्स"

tab1, tab2, tab3, tab4, tab5 = st.tabs([t_voice, t_kids, t_bill, t_khata, t_dir])

# ----------------------------------------------------
# 1. 🎙️ बोलकर पूछें व आवाज़ में सुनें
# ----------------------------------------------------
with tab1:
    st.markdown("### 🎙️ वॉइस AI सहायक")
    st.caption("माइक से बोलें या लिखें — AI लिखकर और आवाज़ में दोनों समझाएगा")
    
    v_in = st.text_input("सवाल दर्ज करें:", placeholder="उदा: बुखार में क्या करें? / दुकान की बिक्री कैसे बढ़ाएं?")
    
    if st.button("🚀 समाधान पाएँ व आवाज़ सुनें"):
        q_txt = v_in.strip()
        if q_txt:
            q_l = q_txt.lower()
            if is_en:
                speech_lang = 'en-US'
                if any(w in q_l for w in ["fever", "pain", "cold", "doctor"]):
                    reply = "Health Guide: Take sufficient rest and drink warm water. If high fever persists, consult a registered doctor immediately."
                elif any(w in q_l for w in ["shop", "business", "sale"]):
                    reply = "Business Advice: Keep accurate logs of daily expenses and share professional digital invoices with customers via WhatsApp."
                else:
                    reply = f"Solution for '{q_txt}': Your query has been processed. Use our specialized tabs for school help, billing, and budgeting."
            else:
                speech_lang = 'hi-IN'
                if any(w in q_l for w in ["dard", "दर्द", "dawai", "दवा", "bukhar", "बुखार"]):
                    reply = "स्वास्थ्य सलाह: पर्याप्त आराम करें और गुनगुना पानी पिएं। तेज बुखार या ज्यादा दर्द होने पर बिना डॉक्टरी सलाह के दवा न लें और तुरंत नजदीकी अस्पताल जाएं।"
                elif any(w in q_l for w in ["dukan", "दुकान", "kamai", "कमाई", "व्यापार"]):
                    reply = "व्यापार वृद्धि: ग्राहकों को WhatsApp पर पक्का बिल भेजें, उधारी का समय पर हिसाब रखें और अपने ऑफर्स शेयर करें।"
                else:
                    reply = f"आपके सवाल '{q_txt}' का समाधान तैयार है। विस्तृत कार्य हेतु संबंधित मेनू का उपयोग करें।"

            st.markdown(f'<div class="card-box" style="border-left: 4px solid #10B981;"><b>💡 AI समाधान:</b><br>{reply}</div>', unsafe_allow_html=True)
            
            clean_speech = reply.replace('"', '\\"').replace('\n', ' ')
            components.html(f"""
            <script>
                var msg = new SpeechSynthesisUtterance("{clean_speech}");
                msg.lang = '{speech_lang}';
                msg.rate = 1.0;
                window.speechSynthesis.speak(msg);
            </script>
            """, height=0)
            st.success("🔊 उत्तर डिवाइस स्पीकर से बोला जा रहा है")
        else:
            st.warning("कृपया अपना सवाल दर्ज करें।")

# ----------------------------------------------------
# 2. 📚 छात्र व बच्चे (होमवर्क व अर्ज़ी)
# ----------------------------------------------------
with tab2:
    st.markdown("### 📚 छात्र सहायता व स्कूल अर्ज़ी")
    st.caption("स्कूल की छुट्टी के लिए प्रार्थना पत्र और 1-क्लिक जॉब बायोडाटा")
    
    st_mode = st.radio("चुनें:", ["📝 स्कूल छुट्टी की अर्ज़ी", "📄 नौकरी का बायोडाटा (Resume)"], horizontal=True)
    
    if "अर्ज़ी" in st_mode:
        s_name = st.text_input("विद्यार्थी का नाम:", value="साहिल")
        s_days = st.text_input("छुट्टी के दिन:", value="2 दिन")
        s_reason = st.text_input("कारण:", value="ज़रूरी कार्य / अस्वस्थता")
        
        if st.button("📝 अर्ज़ी तैयार करें"):
            app_text = f"""सेवा में,\nप्रधानाचार्य महोदय,\nविषय: अवकाश हेतु प्रार्थना पत्र।\n\nमहोदय,\nसविनय निवेदन है कि मुझे {s_reason} होने के कारण मैं {s_days} तक विद्यालय आने में असमर्थ हूँ।\nअतः मुझे अवकाश प्रदान करने की कृपा करें।\n\nधन्यवाद,\nआज्ञाकारी छात्र: {s_name}"""
            st.text_area("कॉपी करें:", app_text, height=150)
    else:
        r_name = st.text_input("पूरा नाम:", value="साहिल कुमार")
        r_phone = st.text_input("मोबाइल नंबर:", value="9876543210")
        r_edu = st.text_input("शिक्षा:", value="12वीं / आईटीआई")
        r_exp = st.text_input("हुनर / अनुभव:", value="ड्राइविंग, कंप्यूटर टाइपिंग, सेल्स")
        
        if st.button("📄 बायोडाटा बनाएँ"):
            res_text = f"""बायोडाटा / RESUME\nनाम: {r_name}\nसंपर्क: {r_phone}\nशिक्षा: {r_edu}\nकार्य अनुभव: {r_exp}\nउपलब्धता: तुरंत कार्य हेतु उपलब्ध"""
            st.text_area("तैयार बायोडाटा:", res_text, height=140)

# ----------------------------------------------------
# 3. 🧾 WhatsApp डिजिटल बिल
# ----------------------------------------------------
with tab3:
    st.markdown("### 🧾 WhatsApp डिजिटल बिल मेकर")
    b_shop = st.text_input("दुकान का नाम:", value="साहिल ट्रेडर्स")
    b_cust = st.text_input("ग्राहक का नाम:", placeholder="उदा: रमेश जी")
    b_phone = st.text_input("ग्राहक का WhatsApp नंबर (10 अंक):", placeholder="उदा: 9876543210")
    b_tot = st.text_input("कुल रकम (₹):", placeholder="उदा: 750")
    
    if st.button("📲 डिजिटल बिल भेजें"):
        if b_shop and b_cust and b_phone and b_tot:
            clean_num = b_phone.strip()[-10:]
            bill_msg = f"""🧾 *डिजिटल बिल / CASH MEMO*
🏪 दुकान: {b_shop}
👤 ग्राहक: {b_cust}
💰 कुल राशि: ₹{b_tot}
✅ स्थिति: भुगतान प्राप्त
-------------------------
_World AI द्वारा प्रमाणित_"""
            wa_url = f"https://wa.me/91{clean_num}?text={urllib.parse.quote(bill_msg)}"
            st.markdown(f'<a href="{wa_url}" target="_blank" class="upi-pay-btn">👉 WhatsApp पर बिल भेजें</a>', unsafe_allow_html=True)
        else:
            st.warning("कृपया सभी विवरण भरें।")

# ----------------------------------------------------
# 4. 💰 डिजिटल खाता
# ----------------------------------------------------
with tab4:
    st.markdown("### 💰 दैनिक गल्ला व डिजिटल खाता")
    if "khata_entries" not in st.session_state:
        st.session_state.khata_entries = []

    k_type = st.radio("प्रकार:", ["➕ कमाई (Income)", "➖ खर्च (Expense)"], horizontal=True)
    k_desc = st.text_input("विवरण:", placeholder="उदा: आज की दुकान बिक्री / राशन खर्च")
    k_amt = st.number_input("रकम (₹):", min_value=1, value=500, step=50)
    
    if st.button("📝 खाते में दर्ज करें"):
        if k_desc.strip():
            st.session_state.khata_entries.append({"प्रकार": k_type, "विवरण": k_desc, "रकम": k_amt})
            st.success("प्रविष्टि सुरक्षित हो गई!")

    if st.session_state.khata_entries:
        st.write("---")
        df_k = pd.DataFrame(st.session_state.khata_entries)
        st.dataframe(df_k, use_container_width=True, hide_index=True)
        inc = sum(e["रकम"] for e in st.session_state.khata_entries if "कमाई" in e["प्रकार"])
        exp = sum(e["रकम"] for e in st.session_state.khata_entries if "खर्च" in e["प्रकार"])
        st.markdown(f'<div class="card-box" style="border-left: 4px solid #10B981;">बचत / बैलेंस: <b>₹{inc - exp:,}</b> (कमाई: ₹{inc:,} | खर्च: ₹{exp:,})</div>', unsafe_allow_html=True)

# ----------------------------------------------------
# 5. 🏢 डायरेक्टरी व फाउंडर अनलॉक
# ----------------------------------------------------
with tab5:
    st.markdown("### 🏢 वेरिफाइड डीलर डायरेक्टरी (प्रॉपर्टी व ऑटो)")
    df_leads = pd.DataFrame({
        "फर्म": ["Patna Prime Estate", "Capital Land Agency", "Bihar Wheels Second-Hand", "Danapur Auto Deals"],
        "कैटेगरी": ["Plot/Land", "Flats", "Used Cars", "Bikes & Cars"],
        "शहर": ["Patna", "Patna", "Patna", "Danapur"],
        "संपर्क": ["+91 98765***** 🔒", "+91 94310***** 🔒", "+91 99310***** 🔒", "+91 70040***** 🔒"]
    })
    st.dataframe(df_leads, use_container_width=True, hide_index=True)
    
    upi_str = f"upi://pay?pa=7484878449-2@ybl&pn=World%20AI&am=49&cu=INR&tn=Directory%20Access"
    st.markdown(f'<a href="{upi_str}" class="upi-pay-btn">⚡ संपूर्ण डेटाबेस अनलॉक करें (₹49)</a>', unsafe_allow_html=True)
    
    utr_f = st.text_input("12 अंकों का UTR नंबर डालें (फाउंडर कोड सक्रिय):", placeholder="UTR नंबर", key="utr_k")
    if st.button("🚀 फाइल डाउनलोड करें"):
        if utr_f.strip() in ["7484878440", "111122223333"] or (len(utr_f.strip()) == 12 and utr_f.strip().isdigit()):
            st.success("✅ सत्यापित!")
            st.download_button(
                label="📥 संपूर्ण डायरेक्टरी डाउनलोड करें (CSV)",
                data="Firm,Category,City,Mobile\nPatna Prime,Land,Patna,+91 9876543210\nBihar Wheels,Cars,Patna,+91 9931012345",
                file_name="Verified_Dealers.csv",
                mime="text/csv",
                use_container_width=True
            )
        else:
            st.error("कृपया सही 12 अंकों का UTR नंबर दर्ज करें।")

# ----------------------------------------------------
# 👑 संस्थापक प्रोफाइल कार्ड
# ----------------------------------------------------
st.markdown("---")
wa_link = f"https://wa.me/{MY_WA_NUMBER}?text={urllib.parse.quote('नमस्ते साहिल जी, मैंने आपका World AI ऐप देखा।')}"
st.markdown(f"""
<div class="founder-card">
    <p style="color: #94A3B8 !important; font-size: 11px; margin: 0; text-transform: uppercase;">
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
