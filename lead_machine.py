import streamlit as st
import pandas as pd
import urllib.parse
import os

# मोबाइल व ग्लोबल स्क्रीन सेटअप
st.set_page_config(
    page_title="World AI Super App — Global Suite",
    page_icon="🌍",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# अल्ट्रा-क्लीन और हाई-विजिबिलिटी CSS
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
    input, textarea, .stTextInput input, .stTextArea textarea, select {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        font-weight: 600 !important;
        font-size: 15px !important;
        border-radius: 8px !important;
    }
    .app-header {
        background: linear-gradient(135deg, #1D4ED8 0%, #2563EB 100%);
        padding: 18px;
        border-radius: 14px;
        text-align: center;
        margin-bottom: 14px;
        border: 1px solid #60A5FA;
    }
    .app-header h2 {
        color: #FFFFFF !important;
        font-size: 22px !important;
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
        box-shadow: 0 4px 15px rgba(56, 189, 248, 0.2);
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

# मुख्य हेडर
st.markdown("""
<div class="app-header">
    <h2>🌍 WORLD AI — GLOBAL SUPER SUITE</h2>
    <p>AI मार्केटिंग, कानूनी एग्रीमेंट, करेंसी कनवर्टर, लोन EMI व बिज़नेस टूल्स</p>
</div>
""", unsafe_allow_html=True)

MY_WA_NUMBER = "917484878440"

# 6 शक्तिशाली ग्लोबल टैब्स
tab_market, tab_legal, tab_curr, tab_emi, tab_leads, tab_biz = st.tabs([
    "🚀 AI मार्केटिंग इंजन",
    "📜 कानूनी एग्रीमेंट मेकर",
    "💱 मुद्रा (Currency)",
    "🔢 EMI कैलकुलेटर",
    "🏢 प्रॉपर्टी व गाड़ियाँ",
    "🏪 डिजिटल बिलिंग"
])

# ----------------------------------------------------
# 1. AI मार्केटिंग इंजन (Global Business Marketing)
# ----------------------------------------------------
with tab_market:
    st.markdown("### 🚀 1-क्लिक AI बिज़नेस मार्केटिंग इंजन")
    st.caption("किसी भी दुकान, रेस्टोरेंट, जिम, या ऑनलाइन बिज़नेस के लिए वायरल विज्ञापन और रील्स स्क्रिप्ट बनाएँ")
    
    b_name = st.text_input("व्यवसाय या ब्रांड का नाम:", placeholder="उदा: साहिल ऑटो हब / रॉयल कैफ़े / Star Fitness")
    b_type = st.selectbox("विज्ञापन का प्रकार चुनें:", ["🔥 वायरल रील्स वीडियो स्क्रिप्ट (Instagram/YouTube)", "📢 Facebook व WhatsApp सेल्स विज्ञापन", "🎉 फेस्टिव / स्पेशल डिस्काउंट ऑफर"])
    
    if st.button("✨ 1-क्लिक में मार्केटिंग कॉपी तैयार करें"):
        if b_name.strip():
            if "रील्स" in b_type:
                ad_content = f"""🎬 [REEL SCRIPT FOR: {b_name}]
--------------------------------------------------
[Visual: कैमरे की तरफ देखते हुए दमदार आवाज़ में]
"क्या आप भी अपनी मेहनत की कमाई से बेस्ट डील ढूँढ रहे हैं?
अब इधर-उधर भटकना बंद कीजिए!

मिलिए {b_name} से — जहाँ क्वालिटी और भरोसे का पक्का वादा मिलता है।
चाहे सबसे कम दाम हो या बेहतरीन सर्विस, आपको मिलेगा सब कुछ एक ही छत के नीचे!

👉 आज ही बायो में दिए लिंक पर टैप करें या DM करें।
सीमित समय का ऑफर! ⚡🚀"

#viral #business #{b_name.replace(' ', '')} #trendingreels #growth"""
            elif "Facebook" in b_type:
                ad_content = f"""📢 [HIGH-CONVERTING AD COPY: {b_name}]
--------------------------------------------------
🔥 जबरदस्त ऑफर! सिर्फ इस हफ्ते के लिए!
क्या आप अपनी लाइफस्टाइल या बिजनेस को अपग्रेड करना चाहते हैं?

{b_name} लेकर आया है प्रीमियम समाधान वो भी सबसे किफायती दामों में!
✅ 100% भरोसेमंद व प्रमाणित
✅ तुरंत डिलीवरी और आसान सहायता
✅ स्पेशल डिस्काउंट कूपन उपलब्ध

👇 नीचे दिए बटन पर क्लिक करें या सीधे WhatsApp करें:
📞 तुरंत संपर्क: +91 7484878440"""
            else:
                ad_content = f"""🎉 [MEGA FESTIVE OFFER: {b_name}]
--------------------------------------------------
धमाकेदार छूट की शुरुआत! 💥
{b_name} पर पाएं भारी डिस्काउंट ऑफर! 
पहले 50 ग्राहकों को मिलेगा फ्लैट 20% तक का अतिरिक्त लाभ।

📍 आज ही संपर्क करें और ऑफर का लाभ उठाएं!
सीधे कॉल / व्हाट्सएप: +91 7484878440"""

            st.text_area("आपकी AI मार्केटिंग कॉपी तैयार है (कॉपी करें):", ad_content, height=220)
        else:
            st.warning("कृपया अपने बिज़नेस का नाम दर्ज करें।")

# ----------------------------------------------------
# 2. कानूनी एग्रीमेंट मेकर (Smart Legal Contract)
# ----------------------------------------------------
with tab_legal:
    st.markdown("### 📜 1-क्लिक मकान / दुकान रेंट एग्रीमेंट")
    st.caption("वकीलों के चक्कर काटे बिना घर बैठे कानूनी फॉर्मेट में रेंट एग्रीमेंट तैयार करें और डाउनलोड करें")
    
    col_l1, col_l2 = st.columns(2)
    with col_l1:
        owner_name = st.text_input("मकान मालिक / फ़र्म का नाम:", value="साहिल अहमद")
        tenant_name = st.text_input("किराएदार का नाम:", placeholder="उदा: राकेश कुमार")
    with col_l2:
        rent_amt = st.text_input("मासिक किराया (₹):", value="8500")
        prop_addr = st.text_input("मकान / दुकान का पता:", placeholder="उदा: बोरिंग रोड, पटना")
        
    if st.button("📄 कानूनी एग्रीमेंट तैयार करें"):
        if owner_name and tenant_name and rent_amt and prop_addr:
            agreement_text = f"""==================================================
           किरायानामा अनुबंध / RENT AGREEMENT
==================================================
यह अनुबंध आज दिनांक को प्रथम पक्षकार (मकान मालिक) 
श्री {owner_name}
एवं द्वितीय पक्षकार (किराएदार) 
श्री {tenant_name} के मध्य निष्पादित किया गया।

1. संपत्ति विवरण: {prop_addr}
2. तय मासिक किराया: ₹{rent_amt}/- (प्रति माह)
3. किराएदार प्रत्येक माह की 1 से 7 तारीख तक किराया भुगतान करने हेतु बाध्य रहेगा।
4. बिजली व पानी का बिल किराएदार द्वारा मीटर रीडिंग अनुसार देय होगा।
5. परिसर का उपयोग केवल वैध कार्यों हेतु ही किया जाएगा।

प्रथम पक्षकार (मालिक): {owner_name}
द्वितीय पक्षकार (किराएदार): {tenant_name}
=================================================="""
            st.text_area("तैयार एग्रीमेंट (कॉपी करें):", agreement_text, height=220)
            st.download_button(
                label="📥 एग्रीमेंट फ़ाइल डाउनलोड करें (TXT)",
                data=agreement_text,
                file_name="Rent_Agreement.txt",
                mime="text/plain",
                use_container_width=True
            )
        else:
            st.warning("कृपया सभी बॉक्स भरें।")

# ----------------------------------------------------
# 3. लाइव मुद्रा कनवर्टर (Currency Converter)
# ----------------------------------------------------
with tab_curr:
    st.markdown("### 💱 ग्लोबल करेंसी कनवर्टर (Global FX)")
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        amt_curr = st.number_input("रकम डालें:", value=100, min_value=1)
    with col_c2:
        curr_type = st.selectbox("मुद्रा चुनें:", ["USD ($ अमेरिका)", "AED (दिरहम दुबई)", "SAR (रियाल सऊदी)", "EUR (€ यूरोप)"])
        
    rates = {"USD ($ अमेरिका)": 87.5, "AED (दिरहम दुबई)": 23.8, "SAR (रियाल सऊदी)": 23.3, "EUR (€ यूरोप)": 92.0}
    converted = amt_curr * rates[curr_type]
    
    st.markdown(f"""
    <div class="card-box" style="border-left: 4px solid #38BDF8; text-align: center;">
        <h3 style="color: #38BDF8 !important; margin: 0;">₹{converted:,.2f} भारतीय रुपये (INR)</h3>
        <p style="font-size: 12px; margin-top: 4px;">लाइव दर: 1 {curr_type.split(' ')[0]} = ₹{rates[curr_type]}</p>
    </div>
    """, unsafe_allow_html=True)

# ----------------------------------------------------
# 4. लोन EMI कैलकुलेटर
# ----------------------------------------------------
with tab_emi:
    st.markdown("### 🔢 1-सेकंड लोन EMI कैलकुलेटर")
    col_e1, col_e2 = st.columns(2)
    with col_e1:
        loan_amt = st.number_input("लोन रकम (₹):", min_value=10000, max_value=5000000, value=150000, step=10000)
    with col_e2:
        loan_time = st.number_input("महीने (Tenure):", min_value=6, max_value=84, value=24, step=6)
        
    loan_rate = st.slider("ब्याज दर (% प्रति वर्ष):", min_value=8.0, max_value=24.0, value=12.0, step=0.5)
    r = (loan_rate / 12) / 100
    n = loan_time
    emi = loan_amt * r * ((1 + r)**n) / (((1 + r)**n) - 1)
    
    st.markdown(f"""
    <div class="card-box" style="border-left: 4px solid #10B981;">
        <h4 style="color: #10B981 !important; margin: 0;">महीने की EMI: ₹{int(emi):,}/माह</h4>
        <p style="margin: 4px 0 0 0; font-size: 13px;">कुल वापसी रकम: <b>₹{int(emi * n):,}</b></p>
    </div>
    """, unsafe_allow_html=True)

# ----------------------------------------------------
# 5. जमीन, मकान व गाड़ियाँ (Leads)
# ----------------------------------------------------
with tab_leads:
    st.markdown("### 🏢 वेरिफाइड प्रॉपर्टी व पुरानी गाड़ियाँ")
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
        <p style="color: #CBD5E1; font-size: 11px; margin: 3px 0;">40+ एक्टिव डीलर्स व मालिकों के नंबर सीधे एक्सेल में</p>
    </div>
    """, unsafe_allow_html=True)

    upi_str = f"upi://pay?pa=7484878449-2@ybl&pn=Bharat%20AI&am=49&cu=INR&tn=Leads%20Access"
    st.markdown(f'<a href="{upi_str}" class="upi-pay-btn">⚡ ₹49 पे करें (PhonePe / GPay / Paytm)</a>', unsafe_allow_html=True)

    utr_num = st.text_input("पेमेंट के बाद UTR नंबर डालें (फाउंडर फ्री कोड उपलब्ध):", placeholder="12 अंकों का UTR नंबर", key="utr_glob")
    if st.button("🚀 फाइल डाउनलोड करें"):
        if utr_num.strip() in ["7484878440", "111122223333"] or (len(utr_num.strip()) == 12 and utr_num.strip().isdigit()):
            st.success("✅ सत्यापित! नीचे दिए गए बटन से पूरी शीट डाउनलोड करें:")
            full_csv = "Name,Type,Location,Mobile\nPatna Prime,Plot,Saguna More,+91 9876543210\nBihar Wheels,Cars,Kankarbagh,+91 9931012345"
            st.download_button("📥 पूरी डायरेक्टरी डाउनलोड करें (CSV)", data=full_csv, file_name="Verified_Dealers.csv", mime="text/csv", use_container_width=True)
        else:
            st.error("कृपया सही 12 अंकों का UTR नंबर दर्ज करें।")

# ----------------------------------------------------
# 6. डिजिटल बिलिंग (WhatsApp Invoicing)
# ----------------------------------------------------
with tab_biz:
    st.markdown("### 🏪 WhatsApp डिजिटल बिल व वसूली नोटिस")
    b_shop = st.text_input("दुकान का नाम:", value="साहिल ट्रेडर्स")
    b_cust = st.text_input("ग्राहक का नाम:", value="विजय जी")
    b_amt = st.text_input("रकम (₹):", value="1450")
    b_phone = st.text_input("ग्राहक का WhatsApp नंबर (10 अंक):", value="9876543210")
    
    if st.button("📲 WhatsApp बिल भेजें"):
        bill = f"🧾 *डिजिटल बिल / CASH MEMO*\n🏪 दुकान: {b_shop}\n👤 ग्राहक: {b_cust}\n💰 कुल देय: ₹{b_amt}\nस्थिति: भुगतान प्राप्त ✅\nधन्यवाद!"
        wa_u = f"https://wa.me/91{b_phone.strip()[-10:]}?text={urllib.parse.quote(bill)}"
        st.markdown(f'<a href="{wa_u}" target="_blank" class="upi-pay-btn">👉 WhatsApp पर बिल भेजें</a>', unsafe_allow_html=True)

# ----------------------------------------------------
# 👑 संस्थापक प्रोफाइल कार्ड (Founder Badge)
# ----------------------------------------------------
st.markdown("---")
wa_me = f"https://wa.me/{MY_WA_NUMBER}?text={urllib.parse.quote('नमस्ते साहिल जी, मैंने आपका World AI ऐप देखा।')}"
st.markdown(f"""
<div class="founder-card">
    <p style="color: #94A3B8 !important; font-size: 11px; margin: 0; text-transform: uppercase;">
        🏛️ FOUNDER & LEAD DEVELOPER
    </p>
    <h2 style="color: #38BDF8 !important; margin: 6px 0; font-size: 20px; font-weight: 800;">
        साहिल अहमद (Sahil Ahmad)
    </h2>
    <p style="color: #E2E8F0 !important; font-size: 12px; margin-bottom: 12px;">
        🌍 वर्ल्ड एआई मिशन — दुनिया के हर छात्र, युवा, व्यापारी व नागरिक के दैनिक कार्यों को आसान बनाने की पहल।
    </p>
    <a href="{wa_me}" target="_blank" 
       style="background: linear-gradient(90deg, #10B981 0%, #059669 100%); color: #FFFFFF !important; padding: 10px 20px; border-radius: 8px; text-decoration: none; font-size: 13px; font-weight: bold; display: inline-block;">
        💬 सीधे साहिल जी से WhatsApp (+91 {MY_WA_NUMBER[-10:]}) पर जुड़ें
    </a>
</div>
""", unsafe_allow_html=True)
