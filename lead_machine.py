import streamlit as st
import pandas as pd
import urllib.parse
import os

# मोबाइल स्क्रीन सेटअप
st.set_page_config(
    page_title="Bharat AI Super App",
    page_icon="🇮🇳",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# बिल्कुल साफ़ विज़िबल मोबाइल CSS (सफ़ेद बॉक्स में साफ़ काला टेक्स्ट)
st.markdown("""
<style>
    .stApp {
        background-color: #0B1329 !important;
        color: #FFFFFF !important;
    }
    
    label, .stMarkdown, p, span, h1, h2, h3, h4 {
        color: #FFFFFF !important;
        font-weight: 600 !important;
    }

    /* इनपुट बॉक्स और टेक्स्ट-एरिया को साफ़ और पठनीय बनाना */
    input, textarea, .stTextInput input, .stTextArea textarea {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        font-weight: 600 !important;
        font-size: 15px !important;
        border-radius: 8px !important;
    }

    .app-header {
        background: linear-gradient(135deg, #1D4ED8 0%, #3B82F6 100%);
        padding: 16px;
        border-radius: 14px;
        text-align: center;
        margin-bottom: 14px;
        border: 1px solid #60A5FA;
    }
    .app-header h2 {
        color: #FFFFFF !important;
        font-size: 21px !important;
        margin: 0 !important;
        font-weight: 800 !important;
    }
    .app-header p {
        color: #E2E8F0 !important;
        font-size: 12px !important;
        margin-top: 4px !important;
        margin-bottom: 0 !important;
    }

    .guide-box {
        background-color: #1E293B;
        border-left: 4px solid #38BDF8;
        border-radius: 8px;
        padding: 14px;
        margin-bottom: 14px;
        font-size: 13px;
        color: #F8FAFC !important;
        line-height: 1.6;
    }

    .founder-card {
        background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
        border: 2px solid #38BDF8;
        border-radius: 14px;
        padding: 16px;
        text-align: center;
        margin-top: 24px;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(56, 189, 248, 0.2);
    }

    .upi-pay-btn {
        display: block;
        background: linear-gradient(90deg, #10B981 0%, #059669 100%);
        color: #FFFFFF !important;
        text-align: center;
        font-weight: bold;
        font-size: 15px;
        padding: 12px;
        border-radius: 10px;
        text-decoration: none;
        margin: 12px 0;
    }

    div.stButton > button {
        background-color: #1E293B !important;
        color: #38BDF8 !important;
        border: 1px solid #38BDF8 !important;
        border-radius: 8px !important;
        font-weight: 700 !important;
        font-size: 14px !important;
        width: 100% !important;
        padding: 10px !important;
    }
</style>
""", unsafe_allow_html=True)

# 🌐 भाषा विकल्प (केवल हिंदी और English)
lang = st.selectbox(
    "🌐 भाषा चुनें / Select Language:",
    ["हिंदी + English (Hinglish)", "Pure English"]
)

is_pure_en = ("Pure English" in lang)

# हेडर
if is_pure_en:
    st.markdown("""
    <div class="app-header">
        <h2>🇮🇳 BHARAT AI — SUPER APP</h2>
        <p>Real Estate, Car Bazaar, Students, Seniors & Business Toolkit</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div class="app-header">
        <h2>🇮🇳 BHARAT AI — सुपर ऐप</h2>
        <p>जमीन-मकान, पुरानी गाड़ियाँ, छात्र, बुज़ुर्ग व व्यापारियों का ऑल-इन-वन ऐप</p>
    </div>
    """, unsafe_allow_html=True)

# मुख्य नंबर
MY_WA_NUMBER = "917484878440"

# 5 मुख्य टैब्स
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🏢 ज़मीन-मकान व गाड़ियाँ",
    "📚 छात्र व बच्चे",
    "🏪 व्यापारी बिल व उधारी",
    "👵 जन-सेवा व बुज़ुर्ग",
    "🤖 AI सवाल-जवाब"
])

# ----------------------------------------------------
# 1. ज़मीन, मकान (Real Estate) और गाड़ियाँ (Car/Bike Bazaar)
# ----------------------------------------------------
with tab1:
    st.markdown("### 🏢 प्रॉपर्टी (जमीन/मकान) व पुरानी गाड़ियाँ")
    st.caption("पटना व बिहार के वेरिफाइड डीलर्स, मकान मालिक व सेलर लिस्ट")

    market_type = st.radio("कैटेगरी चुनें:", ["🏠 जमीन / मकान / फ्लैट", "🚗 पुरानी कार व बाइक डीलर्स"], horizontal=True)

    if market_type == "🏠 जमीन / मकान / फ्लैट":
        df_prop = pd.DataFrame({
            "प्रॉपर्टी / डीलर": ["Patna Prime Properties", "Capital Land Hub", "Rajdhani Flats Danapur", "Maa Tara Homes Boring Road"],
            "प्रकार": ["Plot / Land", "Commercial Land", "2/3 BHK Flats", "House / Duplex"],
            "स्थान": ["Saguna More, Patna", "Bailey Road, Patna", "Danapur Cantt, Patna", "Boring Road, Patna"],
            "संपर्क": ["+91 98765***** 🔒", "+91 94310***** 🔒", "+91 91234***** 🔒", "+91 98350***** 🔒"]
        })
        st.dataframe(df_prop, use_container_width=True, hide_index=True)
    else:
        df_car = pd.DataFrame({
            "डीलर / शोरूम": ["Patna Second-Hand Cars", "Bihar Wheels Hub", "Danapur Auto Bazaar", "Star Pre-Owned Cars"],
            "उपलब्ध गाड़ियाँ": ["Swift, Scorpio, Bolero", "i20, WagonR, Alto", "Pulsar, Splendor Bikes", "Creta, Brezza, Innova"],
            "स्थान": ["Raja Bazar, Patna", "Kankarbagh, Patna", "Danapur, Patna", "Boring Canal Road, Patna"],
            "संपर्क": ["+91 99310***** 🔒", "+91 82100***** 🔒", "+91 70040***** 🔒", "+91 93080***** 🔒"]
        })
        st.dataframe(df_car, use_container_width=True, hide_index=True)

    st.markdown("""
    <div style="background-color: #1E293B; border: 1px solid #F59E0B; border-radius: 10px; padding: 12px; text-align: center; margin-top: 10px;">
        <h4 style="color: #F59E0B !important; margin: 0;">👑 पूरी डायरेक्टरी अनलॉक करें (मात्र ₹49)</h4>
        <p style="color: #CBD5E1 !important; font-size: 11px; margin: 4px 0;">40+ चालू नंबर सीधे एक्सेल शीट में डाउनलोड करें</p>
    </div>
    """, unsafe_allow_html=True)

    upi_link = f"upi://pay?pa=7484878449-2@ybl&pn=Bharat%20AI&am=49&cu=INR&tn=Directory%20Access"
    st.markdown(f'<a href="{upi_link}" class="upi-pay-btn">⚡ ₹49 पे करें (PhonePe / GPay / Paytm)</a>', unsafe_allow_html=True)

    utr_val = st.text_input("पेमेंट के बाद 12 अंकों का UTR नंबर डालें:", placeholder="उदा: 426819284910", key="utr_prop")
    if st.button("🚀 UTR चेक करें और फ़ाइल डाउनलोड करें"):
        if len(utr_val.strip()) == 12 and utr_val.strip().isdigit():
            st.success("✅ पेमेंट सत्यापित! नीचे बटन से पूरी डायरेक्टरी डाउनलोड करें:")
            st.download_button(
                label="📥 संपूर्ण डायरेक्टरी डाउनलोड करें (CSV)",
                data="Dealer,Type,Location,Phone\nPatna Prime,Plot,Saguna More,+91 9876543210\nCapital Land,Flat,Bailey Road,+91 9431012345",
                file_name="Patna_Property_Cars.csv",
                mime="text/csv",
                use_container_width=True
            )
        else:
            st.error("कृपया सही 12 अंकों का UTR नंबर दर्ज करें।")

# ----------------------------------------------------
# 2. छात्र व बच्चे (Students & Kids)
# ----------------------------------------------------
with tab2:
    st.markdown("### 📚 छात्र सहायता व स्कूल अर्ज़ी")
    st_opt = st.radio("चुनें:", ["📝 स्कूल छुट्टी की अर्ज़ी (Leave App)", "📖 प्रेरणादायक कहानी", "📄 1-क्लिक नौकरी बायोडाटा"], horizontal=True)

    if st_opt == "📝 स्कूल छुट्टी की अर्ज़ी (Leave App)":
        s_name = st.text_input("छात्र का नाम:", value="Sahil")
        s_days = st.text_input("कितने दिन की छुट्टी चाहिए:", value="2 दिन")
        s_reason = st.text_input("छुट्टी का कारण:", value="आवश्यक कार्य / तबियत खराब")
        
        if st.button("📝 अर्ज़ी तैयार करें"):
            res_letter = f"""सेवा में,\nप्रधानाचार्य महोदय,\nविद्यालय/महाविद्यालय\n\nविषय: {s_reason} हेतु अवकाश पत्र।\n\nमहोदय,\nसविनय निवेदन है कि मुझे {s_reason} होने के कारण मैं {s_days} तक उपस्थित नहीं हो पाऊँगा।\nअतः प्रार्थना है कि मुझे अवकाश प्रदान करें।\n\nधन्यवाद।\nआज्ञाकारी छात्र,\n{s_name}"""
            st.text_area("आपकी अर्ज़ी (कॉपी करें):", res_letter, height=180)

    elif st_opt == "📖 प्रेरणादायक कहानी":
        st.markdown("""
        <div class="guide-box">
            <b>🪓 ईमानदार लकड़हारा:</b><br>
            नदी में कुल्हाड़ी गिरने पर लकड़हारे ने जलपरी की सोने-चाँदी की कुल्हाड़ी लेने से मना कर दिया और अपनी पुरानी लोहे की कुल्हाड़ी ली। उसकी सच्चाई देखकर जलपरी ने तीनों कुल्हाड़ियाँ इनाम में दे दीं।<br>
            <b>सीख:</b> ईमानदारी सबसे बड़ा खज़ाना है।
        </div>
        """, unsafe_allow_html=True)

    else:
        r_name = st.text_input("पूरा नाम:", value="सुमित कुमार")
        r_phone = st.text_input("मोबाइल नंबर:", value="9876543210")
        r_edu = st.text_input("शिक्षा:", value="12वीं पास")
        r_skill = st.text_input("हुनर / अनुभव:", value="ड्राइविंग, सेल्स, मोबाइल रिपेयरिंग")
        if st.button("📄 बायोडाटा (Resume) बनाएँ"):
            res_txt = f"""बायोडाटा / RESUME\n--------------------\nनाम: {r_name}\nफ़ोन: {r_phone}\nशिक्षा: {r_edu}\nहुनर: {r_skill}\nउपलब्धता: तत्काल काम हेतु उपलब्ध"""
            st.text_area("तैयार बायोडाटा:", res_txt, height=140)

# ----------------------------------------------------
# 3. व्यापारी बिल व उधारी (Vyapar Tools)
# ----------------------------------------------------
with tab3:
    st.markdown("### 🏪 1-क्लिक WhatsApp बिल व उधारी तगादा")
    v_tool = st.radio("टूल:", ["🧾 WhatsApp डिजिटल बिल", "💰 कानूनी उधारी तगादा"], horizontal=True)

    if v_tool == "🧾 WhatsApp डिजिटल बिल":
        b_shop = st.text_input("दुकान का नाम:", value="साहिल ट्रेडर्स")
        b_cust = st.text_input("ग्राहक का नाम:", value="रमेश जी")
        b_phone = st.text_input("ग्राहक का WhatsApp नंबर (10 अंक):", value="9876543210")
        b_amt = st.text_input("कुल रकम (₹):", value="1250")
        
        if st.button("📲 WhatsApp बिल तैयार करें"):
            bill_msg = f"🧾 *डिजिटल बिल / CASH MEMO*\n🏪 दुकान: {b_shop}\n👤 ग्राहक: {b_cust}\n💰 कुल देय: ₹{b_amt}\n✅ स्थिति: भुगतान प्राप्त\nधन्यवाद! फिर पधारें 🙏"
            wa_url = f"https://wa.me/91{b_phone.strip()[-10:]}?text={urllib.parse.quote(bill_msg)}"
            st.markdown(f'<a href="{wa_url}" target="_blank" class="upi-pay-btn">👉 WhatsApp पर बिल भेजें</a>', unsafe_allow_html=True)

    else:
        c_name = st.text_input("बकायेदार का नाम:", value="विकास जी")
        c_amt = st.text_input("बकाया राशि (₹):", value="3500")
        c_phone = st.text_input("बकायेदार का WhatsApp नंबर:", value="9876543210")
        
        if st.button("📩 कानूनी तगादा भेजें"):
            rec_msg = f"नमस्ते {c_name} जी, आपके ऊपर ₹{c_amt} का व्यापारिक बकाया लंबित है। कृपया आज ही इसका भुगतान करें अन्यथा कानूनी प्रक्रिया शुरू की जा सकती है।"
            wa_rec = f"https://wa.me/91{c_phone.strip()[-10:]}?text={urllib.parse.quote(rec_msg)}"
            st.markdown(f'<a href="{wa_rec}" target="_blank" class="upi-pay-btn">👉 WhatsApp पर नोटिस भेजें</a>', unsafe_allow_html=True)

# ----------------------------------------------------
# 4. जन-सेवा व बुज़ुर्ग (Seniors & Schemes)
# ----------------------------------------------------
with tab4:
    st.markdown("### 👵 सरकारी योजनाएँ व बुज़ुर्ग सहायता")
    st.markdown("""
    <div class="guide-box">
        <b>🏥 आयुष्मान भारत योजना (₹5 लाख तक मुफ़्त इलाज):</b><br>
        • हर साल परिवार को ₹5,00,000 का मुफ़्त इलाज मिलता है।<br>
        • <b>कागज़ात:</b> आधार कार्ड और राशन कार्ड।<br>
        • <b>टोल-फ्री हेल्पलाइन:</b> 14555 पर कॉल करें।
    </div>
    <div class="guide-box">
        <b>👴 वृद्धावस्था पेंशन योजना:</b><br>
        • 60 साल या अधिक उम्र के नागरिकों के लिए।<br>
        • आधार कार्ड, बैंक पासबुक और आय प्रमाण पत्र लेकर नजदीकी CSC सेंटर या ब्लॉक RTPS में जमा करें।
    </div>
    <div class="guide-box">
        <b>🌾 राशन कार्ड सहायता:</b><br>
        • नए राशन कार्ड में नाम जुड़वाने हेतु परिवार के सभी सदस्यों के आधार कार्ड व मुखिया की फोटो ब्लॉक में जमा करें।
    </div>
    """, unsafe_allow_html=True)

# ----------------------------------------------------
# 5. AI सवाल-जवाब
# ----------------------------------------------------
with tab5:
    st.markdown("### 🤖 कोई भी सवाल पूछें")
    ask_q = st.text_input("अपनी समस्या लिखें:", placeholder="उदा: बुखार में क्या प्राथमिक उपचार करें? या दुकान की बिक्री कैसे बढ़ाएँ?")
    if st.button("🚀 तुरंत समाधान पाएँ"):
        if "बुखार" in ask_q or "दवा" in ask_q:
            st.info("🩺 **स्वास्थ्य सलाह:** आराम करें और ओआरएस/गुनगुना पानी पिएं। माथे पर सामान्य पानी की पट्टी रखें। बुखार 2 दिन से अधिक रहे तो तुरंत डॉक्टर को दिखाएँ।")
        else:
            st.success("💡 **परामर्श:** अपने काम को योजनाबद्ध तरीक़े से करें। रोज़ाना 10 नए ग्राहकों से संपर्क करने से व्यापार में तेज़ी आती है!")

# ----------------------------------------------------
# 👑 संस्थापक प्रोफाइल (100% सही WhatsApp नंबर)
# ----------------------------------------------------
st.markdown("---")
founder_url = f"https://wa.me/{MY_WA_NUMBER}?text={urllib.parse.quote('नमस्ते साहिल जी, मैंने आपका Bharat AI ऐप देखा।')}"

st.markdown(f"""
<div class="founder-card">
    <p style="color: #94A3B8 !important; font-size: 11px; margin: 0; text-transform: uppercase;">
        🏛️ FOUNDER & LEAD DEVELOPER
    </p>
    <h2 style="color: #38BDF8 !important; margin: 6px 0; font-size: 20px; font-weight: 800;">
        साहिल अहमद (Sahil Ahmad)
    </h2>
    <p style="color: #E2E8F0 !important; font-size: 12px; margin-bottom: 12px;">
        🇮🇳 डिजिटल भारत मिशन — देश के हर छात्र, बुज़ुर्ग, युवा व व्यापारी को डिजिटल शक्ति से जोड़ने की पहल।
    </p>
    <a href="{founder_url}" target="_blank" 
       style="background: linear-gradient(90deg, #10B981 0%, #059669 100%); color: #FFFFFF !important; padding: 10px 20px; border-radius: 8px; text-decoration: none; font-size: 13px; font-weight: bold; display: inline-block;">
        💬 सीधे WhatsApp (+91 {MY_WA_NUMBER[-10:]}) पर जुड़ें
    </a>
</div>
""", unsafe_allow_html=True)
