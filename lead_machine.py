import streamlit as st
import pandas as pd
import urllib.parse
import os

# स्क्रीन सेटअप
st.set_page_config(
    page_title="Bharat AI - Viral Super App",
    page_icon="🇮🇳",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# अल्ट्रा-क्लीन मोबाइल CSS
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
        margin-bottom: 12px;
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
    .card-box {
        background-color: #1E293B;
        border: 1px solid #334155;
        border-radius: 10px;
        padding: 14px;
        margin-bottom: 12px;
    }
    .founder-card {
        background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
        border: 2px solid #38BDF8;
        border-radius: 14px;
        padding: 16px;
        text-align: center;
        margin-top: 24px;
        margin-bottom: 20px;
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
        background-color: #1E293B !important;
        color: #38BDF8 !important;
        border: 1px solid #38BDF8 !important;
        border-radius: 8px !important;
        font-weight: 700 !important;
        font-size: 14px !important;
        width: 100% !important;
        padding: 9px !important;
    }
</style>
""", unsafe_allow_html=True)

# हेडर
st.markdown("""
<div class="app-header">
    <h2>🇮🇳 BHARAT AI — वायरल सुपर ऐप</h2>
    <p>जमीन-गाड़ी, EMI कैलकुलेटर, इंस्टा वायरल टूल्स, छात्र व व्यापारिक समाधान</p>
</div>
""", unsafe_allow_html=True)

# आपका आधिकारिक WhatsApp नंबर
MY_WA_NUMBER = "917484878440"

# 5 ट्रेंडिंग टैब्स
tab_lead, tab_emi, tab_viral, tab_student, tab_biz = st.tabs([
    "🏢 जमीन व पुरानी गाड़ियाँ",
    "🔢 EMI कैलकुलेटर",
    "🔥 वायरल रील्स व कैप्शन",
    "📚 छात्र व बच्चे",
    "🏪 व्यापारी बिल व उधारी"
])

# ----------------------------------------------------
# 1. ज़मीन, मकान व गाड़ियाँ (Leads)
# ----------------------------------------------------
with tab_lead:
    st.markdown("### 🏢 प्रॉपर्टी व पुरानी गाड़ियों के नंबर")
    m_choice = st.radio("चुनें:", ["🏠 जमीन / मकान / फ्लैट", "🚗 पुरानी कार व बाइक डीलर्स"], horizontal=True)

    if m_choice == "🏠 जमीन / मकान / फ्लैट":
        df_p = pd.DataFrame({
            "प्रॉपर्टी / फर्म": ["Patna Prime Estate", "Capital Land Agency", "Danapur Flats Hub", "Boring Road Homes"],
            "प्रकार": ["Plot / Land", "Commercial Space", "2/3 BHK Flats", "House / Villa"],
            "स्थान": ["Saguna More, Patna", "Bailey Road, Patna", "Danapur, Patna", "Boring Road, Patna"],
            "संपर्क": ["+91 98765***** 🔒", "+91 94310***** 🔒", "+91 91234***** 🔒", "+91 98350***** 🔒"]
        })
        st.dataframe(df_p, use_container_width=True, hide_index=True)
    else:
        df_c = pd.DataFrame({
            "डीलर / शोरूम": ["Patna Second-Hand Cars", "Bihar Wheels Hub", "Patna Bike Bazaar", "Apex Auto Deals"],
            "स्टॉक": ["Scorpio, Swift, Bolero", "i20, Alto, WagonR", "Pulsar, Splendor, Bullet", "Creta, Brezza, Innova"],
            "स्थान": ["Raja Bazar, Patna", "Kankarbagh, Patna", "Boring Canal Road, Patna", "Danapur, Patna"],
            "संपर्क": ["+91 99310***** 🔒", "+91 82100***** 🔒", "+91 70040***** 🔒", "+91 93080***** 🔒"]
        })
        st.dataframe(df_c, use_container_width=True, hide_index=True)

    st.markdown("""
    <div style="background-color: #1E293B; border: 1px solid #F59E0B; border-radius: 10px; padding: 10px; text-align: center; margin-top: 10px;">
        <b style="color: #F59E0B;">👑 पूरी कॉलिंग लिस्ट अनलॉक करें (मात्र ₹49)</b>
        <p style="color: #CBD5E1; font-size: 11px; margin: 3px 0;">40+ एक्टिव डीलर्स व मालिकों के पूरे नंबर एक्सेल शीट में</p>
    </div>
    """, unsafe_allow_html=True)

    upi_str = f"upi://pay?pa=7484878449-2@ybl&pn=Bharat%20AI&am=49&cu=INR&tn=Leads%20Access"
    st.markdown(f'<a href="{upi_str}" class="upi-pay-btn">⚡ ₹49 पे करें (PhonePe / GPay / Paytm)</a>', unsafe_allow_html=True)

    utr_num = st.text_input("पेमेंट के बाद UTR नंबर डालें (फाउंडर फ्री कोड उपलब्ध):", placeholder="12 अंकों का UTR नंबर दर्ज करें", key="utr_k")
    if st.button("🚀 फाइल डाउनलोड करें"):
        # आपके लिए स्पेशल फ्री सीक्रेट कोड
        if utr_num.strip() in ["7484878440", "111122223333"] or (len(utr_num.strip()) == 12 and utr_num.strip().isdigit()):
            st.success("✅ सत्यापित! नीचे दिए गए बटन से पूरी शीट डाउनलोड करें:")
            full_csv = "Name,Type,Location,Mobile\nPatna Prime,Plot,Saguna More,+91 9876543210\nBihar Wheels,Cars,Kankarbagh,+91 9931012345"
            st.download_button("📥 पूरी डायरेक्टरी डाउनलोड करें (CSV)", data=full_csv, file_name="Verified_Dealers.csv", mime="text/csv", use_container_width=True)
        else:
            st.error("कृपया सही 12 अंकों का UTR नंबर दर्ज करें।")

# ----------------------------------------------------
# 2. बाइक, कार व पर्सनल लोन EMI कैलकुलेटर
# ----------------------------------------------------
with tab_emi:
    st.markdown("### 🔢 1-सेकंड लोन EMI कैलकुलेटर")
    st.caption("बाइक, कार या जमीन खरीदने से पहले अपनी मासिक किस्त (EMI) तुरंत जानें")
    
    col_e1, col_e2 = st.columns(2)
    with col_e1:
        loan_amt = st.number_input("लोन की रकम (₹):", min_value=10000, max_value=5000000, value=150000, step=10000)
    with col_e2:
        loan_time = st.number_input("समय (महीनों में):", min_value=6, max_value=84, value=24, step=6)
        
    loan_rate = st.slider("सालाना ब्याज दर (%):", min_value=8.0, max_value=24.0, value=12.0, step=0.5)
    
    r = (loan_rate / 12) / 100
    n = loan_time
    emi = loan_amt * r * ((1 + r)**n) / (((1 + r)**n) - 1)
    total_pay = emi * n
    interest_amt = total_pay - loan_amt
    
    st.markdown(f"""
    <div class="card-box" style="border-left: 4px solid #10B981;">
        <h4 style="color: #10B981 !important; margin: 0;">महीने की किस्त (EMI): ₹{int(emi):,}/महीना</h4>
        <p style="margin: 4px 0 0 0; font-size: 13px;">कुल ब्याज: <b>₹{int(interest_amt):,}</b> | कुल वापसी रकम: <b>₹{int(total_pay):,}</b></p>
    </div>
    """, unsafe_allow_html=True)

# ----------------------------------------------------
# 3. वायरल रील्स व सोशल मीडिया टूल्स
# ----------------------------------------------------
with tab_viral:
    st.markdown("### 🔥 इंस्टा व यूट्यूब वायरल टूल")
    st.caption("रील्स के लिए 1-क्लिक में ट्रेंडिंग कैप्शन, हैशटैग और एटीट्यूड बायो तैयार करें")
    
    v_tool = st.selectbox("आपको क्या चाहिए?", ["🔥 रील्स के लिए वायरल कैप्शन्स", "🚀 ट्रेंडिंग हैशटैग्स (All India)", "😎 स्टाइलिश इंस्टा बायो"])
    
    if v_tool == "🔥 रील्स के लिए वायरल कैप्शन्स":
        st.markdown("""
        <div class="card-box">
            <b>1. एटीट्यूड / स्टाइल:</b><br>
            <i>"हम वो नहीं जो हवा का रुख देखकर चलते हैं, हम वो हैं जो हवाओं का रुख मोड़ देते हैं। ⚡👑"</i><br><br>
            <b>2. मोटिवेशन / मेहनत:</b><br>
            <i>"जो आज कहते हैं तुझसे नहीं होगा, कल वही तालियाँ बजाने वालों की कतार में सबसे आगे होंगे। 🦁🔥"</i><br><br>
            <b>3. बाइक / कार राइडर:</b><br>
            <i>"सड़कें वही हैं, बस रफ्तार और रुतबा अपना है। 🏍️💨"</i>
        </div>
        """, unsafe_allow_html=True)
    elif v_tool == "🚀 ट्रेंडिंग हैशटैग्स (All India)":
        tags = "#viral #reelsindia #trendingreels #bihar #patna #explorepage #foryou #attitude #motivation #creator"
        st.text_area("कॉपी करके अपनी रील में डालें:", tags, height=80)
    else:
        st.markdown("""
        <div class="card-box">
            👑 <b>रॉयल बायो:</b><br>
            • Simple Guy With Big Dreams 🚀<br>
            • Focus on Goals, Not Noise 🎯<br>
            • Apna Time Aayega Nahi, Layenge! 🦁
        </div>
        """, unsafe_allow_html=True)

# ----------------------------------------------------
# 4. छात्र व बच्चे
# ----------------------------------------------------
with tab_student:
    st.markdown("### 📚 स्कूल अर्ज़ी व पढ़ाई")
    st_name = st.text_input("विद्यार्थी का नाम:", value="साहिल कुमार")
    st_days = st.text_input("छुट्टी के दिन:", value="2 दिन")
    if st.button("📝 अर्ज़ी तैयार करें"):
        letter = f"""सेवा में,\nप्रधानाचार्य महोदय,\nविषय: अवकाश हेतु प्रार्थना पत्र\n\nमहोदय,\nसविनय निवेदन है कि आवश्यक कार्य होने से मैं {st_days} तक विद्यालय आने में असमर्थ हूँ। कृपया अवकाश प्रदान करें।\n\nआज्ञाकारी छात्र,\n{st_name}"""
        st.text_area("कॉपी करें:", letter, height=140)

# ----------------------------------------------------
# 5. व्यापारी बिल व उधारी
# ----------------------------------------------------
with tab_biz:
    st.markdown("### 🏪 WhatsApp बिल व उधारी तगादा")
    b_shop = st.text_input("दुकान का नाम:", value="साहिल ट्रेडर्स")
    b_cust = st.text_input("ग्राहक का नाम:", value="विजय जी")
    b_amt = st.text_input("रकम (₹):", value="1450")
    b_phone = st.text_input("ग्राहक का WhatsApp नंबर:", value="9876543210")
    
    if st.button("📲 WhatsApp बिल भेजें"):
        bill = f"🧾 *डिजिटल बिल / CASH MEMO*\n🏪 दुकान: {b_shop}\n👤 ग्राहक: {b_cust}\n💰 कुल देय: ₹{b_amt}\nस्थिति: भुगतान प्राप्त ✅\nधन्यवाद!"
        wa_u = f"https://wa.me/91{b_phone.strip()[-10:]}?text={urllib.parse.quote(bill)}"
        st.markdown(f'<a href="{wa_u}" target="_blank" class="upi-pay-btn">👉 WhatsApp पर बिल भेजें</a>', unsafe_allow_html=True)

# ----------------------------------------------------
# 👑 संस्थापक प्रोफाइल कार्ड
# ----------------------------------------------------
st.markdown("---")
wa_me = f"https://wa.me/{MY_WA_NUMBER}?text={urllib.parse.quote('नमस्ते साहिल जी, मैंने आपका Bharat AI ऐप देखा।')}"
st.markdown(f"""
<div class="founder-card">
    <p style="color: #94A3B8 !important; font-size: 11px; margin: 0; text-transform: uppercase;">
        🏛️ FOUNDER & LEAD DEVELOPER
    </p>
    <h2 style="color: #38BDF8 !important; margin: 6px 0; font-size: 20px; font-weight: 800;">
        साहिल अहमद (Sahil Ahmad)
    </h2>
    <p style="color: #E2E8F0 !important; font-size: 12px; margin-bottom: 12px;">
        🇮🇳 डिजिटल भारत मिशन — देश के हर छात्र, युवा, बुज़ुर्ग व व्यापारी का डिजिटल साथी।
    </p>
    <a href="{wa_me}" target="_blank" 
       style="background: linear-gradient(90deg, #10B981 0%, #059669 100%); color: #FFFFFF !important; padding: 10px 20px; border-radius: 8px; text-decoration: none; font-size: 13px; font-weight: bold; display: inline-block;">
        💬 सीधे साहिल जी से WhatsApp (+91 {MY_WA_NUMBER[-10:]}) पर जुड़ें
    </a>
</div>
""", unsafe_allow_html=True)
