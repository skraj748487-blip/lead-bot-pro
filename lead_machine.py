import streamlit as st
import pandas as pd
import urllib.parse
import os

# मोबाइल स्क्रीन सेटअप
st.set_page_config(
    page_title="Bharat AI - Super App",
    page_icon="🇮🇳",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# मॉडर्न मोबाइल CSS
st.markdown("""
<style>
    .stApp {
        background-color: #0F172A;
        color: #F8FAFC;
    }
    .app-header {
        background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 100%);
        padding: 16px;
        border-radius: 14px;
        text-align: center;
        margin-bottom: 14px;
    }
    .app-header h2 {
        color: #FFFFFF;
        font-size: 20px;
        margin: 0;
        font-weight: 800;
    }
    .app-header p {
        color: #E2E8F0;
        font-size: 11px;
        margin-top: 4px;
        margin-bottom: 0;
    }
    .stats-container {
        display: flex;
        justify-content: space-between;
        gap: 6px;
        margin-bottom: 14px;
    }
    .stat-box {
        background-color: #1E293B;
        border: 1px solid #334155;
        border-radius: 10px;
        padding: 8px 4px;
        text-align: center;
        flex: 1;
    }
    .stat-number {
        color: #38BDF8;
        font-size: 13px;
        font-weight: 700;
    }
    .stat-label {
        color: #94A3B8;
        font-size: 9px;
    }
    .unlock-card {
        background: linear-gradient(180deg, #1E293B 0%, #0F172A 100%);
        border: 1px solid #F59E0B;
        border-radius: 12px;
        padding: 14px;
        text-align: center;
        margin-top: 14px;
    }
    .price-tag {
        font-size: 24px;
        font-weight: 800;
        color: #10B981;
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
    .guide-box {
        background-color: #1E293B;
        border-left: 4px solid #F59E0B;
        border-radius: 8px;
        padding: 12px;
        margin-bottom: 12px;
        font-size: 12px;
        color: #E2E8F0;
    }
    div.stButton > button {
        background-color: #1E293B !important;
        color: #F8FAFC !important;
        border: 1px solid #38BDF8 !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        font-size: 13px !important;
        width: 100% !important;
        padding: 8px !important;
    }
</style>
""", unsafe_allow_html=True)

# मुख्य हेडर
st.markdown("""
<div class="app-header">
    <h2>🇮🇳 BHARAT AI — ऑल-इन-वन सुपर ऐप</h2>
    <p>छात्र, नागरिक, बुजुर्ग व व्यापारी — हर भारतीय की दैनिक डिजिटल सुविधा</p>
</div>
""", unsafe_allow_html=True)

# 4 मुख्य श्रेणियां (टैब्स)
tab_student, tab_citizen, tab_business, tab_leads = st.tabs([
    "📚 छात्र कॉर्नर",
    "📜 जन-सेवा व योजना",
    "🏪 व्यापारी टूल्स",
    "🎯 बिज़नेस डायरेक्टरी"
])

# ----------------------------------------------------
# 1. छात्र कॉर्नर (Students)
# ----------------------------------------------------
with tab_student:
    st.markdown("### 📚 छात्र सहायता व स्मार्ट लेखक")
    st.caption("स्कूल/कॉलेज अर्ज़ी, छुट्टी का पत्र या नौकरी का बायोडाटा तुरंत बनाएँ")
    
    st_option = st.selectbox("आपको क्या तैयार करना है?", [
        "स्कूल / कॉलेज की छुट्टी की अर्ज़ी (Leave Application)",
        "नौकरी के लिए साधारण बायोडाटा (Quick Resume)"
    ])
    
    if "Leave Application" in st_option:
        s_name = st.text_input("विद्यार्थी का नाम:", placeholder="उदा: साहिल कुमार")
        s_school = st.text_input("स्कूल / कॉलेज का नाम:", placeholder="उदा: राजकीय उच्च विद्यालय")
        s_reason = st.text_input("छुट्टी का कारण:", placeholder="उदा: तबियत खराब होने के कारण / आवश्यक कार्य")
        s_days = st.text_input("कितने दिन की छुट्टी चाहिए:", placeholder="उदा: 2 दिन (22 से 23 तारीख)")
        
        if st.button("📝 अर्ज़ी तैयार करें"):
            if s_name and s_school and s_reason and s_days:
                letter = f"""सेवा में,
प्रधानाचार्य महोदय,
{s_school}

विषय: {s_reason} हेतु अवकाश पत्र

महोदय,
सविनय निवेदन यह है कि मैं आपके विद्यालय/महाविद्यालय का छात्र हूँ। {s_reason} के कारण मैं {s_days} तक उपस्थित रहने में असमर्थ हूँ।

अतः आपसे विनम्र प्रार्थना है कि मुझे उक्त दिनों का अवकाश प्रदान करने की कृपा करें। इसके लिए मैं आपका सदैव आभारी रहूँगा।

धन्यवाद।
आपका आज्ञाकारी छात्र,
नाम: {s_name}"""
                st.text_area("आपकी अर्ज़ी तैयार है (कॉपी करें):", letter, height=220)
            else:
                st.warning("कृपया सभी बॉक्स भरें।")

    elif "Quick Resume" in st_option:
        r_name = st.text_input("आपका पूरा नाम:", placeholder="उदा: राहुल कुमार")
        r_phone = st.text_input("मोबाइल नंबर:", placeholder="उदा: 9876543210")
        r_edu = st.text_input("शिक्षा (Qualification):", placeholder="उदा: 10वीं पास / 12वीं पास / स्नातक")
        r_skills = st.text_input("कार्य अनुभव या हुनर (Skills):", placeholder="उदा: ड्राइविंग, कंप्यूटर टाइपिंग, सेल्स का 1 साल अनुभव")
        
        if st.button("📄 बायोडाटा (Resume) तैयार करें"):
            if r_name and r_phone and r_edu:
                resume_text = f"""==============================
        बायोडाटा / RESUME
==============================
नाम: {r_name}
संपर्क नंबर: {r_phone}
शैक्षणिक योग्यता: {r_edu}
हुनर व अनुभव: {r_skills}
भाषा ज्ञान: हिंदी, साधारण अंग्रेज़ी
स्थिति: तुरंत कार्य करने हेतु उपलब्ध
=============================="""
                st.text_area("आपका बायोडाटा तैयार है (कॉपी करें):", resume_text, height=200)
            else:
                st.warning("कृपया नाम, नंबर और शिक्षा अवश्य भरें।")

# ----------------------------------------------------
# 2. जन-सेवा व सरकारी योजना (Citizens & Seniors)
# ----------------------------------------------------
with tab_citizen:
    st.markdown("### 📜 सरकारी योजना व नागरिक सुविधा")
    st.caption("बुजुर्गों और आम परिवारों के लिए प्रमुख योजनाओं की पूरी जानकारी")
    
    yojana = st.selectbox("योजना चुनें जिसकी जानकारी चाहिए:", [
        "वृद्धावस्था / विधवा पेंशन योजना",
        "आयुष्मान भारत (₹5 लाख तक मुफ़्त इलाज)",
        "राशन कार्ड नया आवेदन / नाम जोड़ना",
        "पीएम किसान सम्मान निधि (₹6000 सालाना)"
    ])
    
    if yojana == "वृद्धावस्था / विधवा पेंशन योजना":
        st.markdown("""
        <div class="guide-box">
            <b>👴 वृद्धावस्था पेंशन नियम व दस्तावेज:</b><br>
            • <b>पात्रता:</b> आयु 60 वर्ष या उससे अधिक होनी चाहिए।<br>
            • <b>आवश्यक दस्तावेज:</b> आधार कार्ड, बैंक पासबुक, आय प्रमाण पत्र, आयु प्रमाण पत्र।<br>
            • <b>आवेदन का तरीका:</b> अपने नजदीकी ब्लॉक या जन सेवा केंद्र (CSC) से ऑनलाइन आवेदन करें।
        </div>
        """, unsafe_allow_html=True)
    elif yojana == "आयुष्मान भारत (₹5 लाख तक मुफ़्त इलाज)":
        st.markdown("""
        <div class="guide-box">
            <b>🏥 आयुष्मान कार्ड सुविधा:</b><br>
            • सरकारी व सूचीबद्ध प्राइवेट अस्पतालों में प्रति वर्ष ₹5 लाख तक का इलाज मुफ़्त।<br>
            • <b>दस्तावेज:</b> राशन कार्ड और आधार कार्ड।<br>
            • नजदीकी सरकारी अस्पताल या CSC केंद्र पर जाकर पात्रता तुरंत चेक कराएं।
        </div>
        """, unsafe_allow_html=True)
    elif yojana == "राशन कार्ड नया आवेदन / नाम जोड़ना":
        st.markdown("""
        <div class="guide-box">
            <b>🌾 राशन कार्ड सहायता:</b><br>
            • <b>दस्तावेज:</b> परिवार के मुखिया की फोटो, सभी सदस्यों का आधार कार्ड, बैंक पासबुक व निवास प्रमाण पत्र।<br>
            • आरटीपीएस (RTPS) काउंटर या राज्य खाद्य पोर्टल से ऑनलाइन जमा होता है।
        </div>
        """, unsafe_allow_html=True)
    elif yojana == "पीएम किसान सम्मान निधि (₹6000 सालाना)":
        st.markdown("""
        <div class="guide-box">
            <b>🚜 किसान सम्मान निधि:</b><br>
            • हर 4 महीने में ₹2,000 की किस्त (सालाना ₹6,000)।<br>
            • <b>आवश्यक:</b> जमीन की रसीद/जमाबंदी, आधार कार्ड, बैंक खाता और आधार e-KYC अनिवार्य।
        </div>
        """, unsafe_allow_html=True)

# ----------------------------------------------------
# 3. व्यापारी टूल्स (Business Tools)
# ----------------------------------------------------
with tab_business:
    st.markdown("### 🏪 स्मार्ट व्यापार टूल्स")
    
    b_type = st.radio("टूल चुनें:", ["🧾 WhatsApp डिजिटल बिल", "💰 सख्त उधारी वसूली नोटिस"], horizontal=True)
    
    if b_type == "🧾 WhatsApp डिजिटल बिल":
        b_shop = st.text_input("अपनी दुकान / फर्म का नाम:", placeholder="उदा: गुप्ता किराना स्टोर")
        b_cust = st.text_input("ग्राहक का नाम:", placeholder="उदा: रमेश जी")
        b_phone = st.text_input("ग्राहक का WhatsApp नंबर (10 अंक):", placeholder="उदा: 9876543210")
        b_item = st.text_area("सामान का विवरण:", placeholder="उदा: 5 किलो चीनी (₹200), 2 पैकेट तेल (₹300)")
        b_total = st.text_input("कुल रकम (₹):", placeholder="उदा: 500")
        
        if st.button("📲 डिजिटल बिल भेजें"):
            if b_shop and b_cust and b_phone and b_total:
                clean_p = b_phone.strip()[-10:]
                bill_msg = f"""🧾 *डिजिटल बिल / CASH MEMO*
🏪 *दुकान:* {b_shop}
👤 *ग्राहक:* {b_cust}
-------------------------
📦 *सामान:* 
{b_item}
-------------------------
💰 *कुल राशि:* ₹{b_total}
✅ स्थिति: भुगतान प्राप्त
-------------------------
धन्यवाद! फिर पधारें 🙏"""
                wa_url = f"https://wa.me/91{clean_p}?text={urllib.parse.quote(bill_msg)}"
                st.markdown(f'<a href="{wa_url}" target="_blank" class="upi-pay-btn">👉 WhatsApp पर बिल भेजें</a>', unsafe_allow_html=True)
            else:
                st.warning("कृपया सभी जानकारी भरें।")

    elif b_type == "💰 सख्त उधारी वसूली नोटिस":
        c_name = st.text_input("बकायेदार का नाम:", placeholder="उदा: विकास कुमार")
        c_amount = st.text_input("बकाया राशि (₹):", placeholder="उदा: 8500")
        c_phone = st.text_input("बकायेदार का WhatsApp नंबर:", placeholder="उदा: 9876543210")
        
        if st.button("📩 कानूनी तगादा भेजें"):
            if c_name and c_amount and c_phone:
                clean_rec_p = c_phone.strip()[-10:]
                msg = f"अंतिम सूचना: नमस्ते {c_name} जी, आपके ऊपर ₹{c_amount} का व्यापारिक बकाया शेष है। कृपया इसे आज ही सेटल करें, अन्यथा कानूनी कार्यवाही शुरू की जा सकती है।"
                wa_link = f"https://wa.me/91{clean_rec_p}?text={urllib.parse.quote(msg)}"
                st.markdown(f'<a href="{wa_link}" target="_blank" class="upi-pay-btn">👉 WhatsApp पर नोटिस भेजें</a>', unsafe_allow_html=True)
            else:
                st.warning("कृपया सभी जानकारी भरें।")

# ----------------------------------------------------
# 4. बिज़नेस डायरेक्टरी (Leads Directory)
# ----------------------------------------------------
with tab_leads:
    st.markdown("### 🎯 अखिल भारतीय व्यापारी डायरेक्टरी")
    
    @st.cache_data
    def load_db():
        return pd.DataFrame({
            "व्यापारी / फर्म": [
                "Patna Prime Builders", "Capital Property Hub", "Rajdhani Estate Agency", "Metro City Realtors",
                "Delhi NCR Real Infra", "Mumbai Seaface Properties", "Bengaluru Tech Properties",
                "Shree Ganesh Kirana Wholesale", "Delhi Wholesale Mart", "Mumbai Super Hub",
                "Gold's Fitness Gym", "Dr. Sharma Dental Clinic"
            ],
            "कैटेगरी": [
                "Real Estate", "Real Estate", "Real Estate", "Real Estate",
                "Real Estate", "Real Estate", "Real Estate",
                "Wholesale", "Wholesale", "Wholesale",
                "Gym", "Doctor"
            ],
            "शहर": [
                "Patna", "Patna", "Patna", "Patna",
                "Delhi", "Mumbai", "Bengaluru",
                "Patna", "Delhi", "Mumbai",
                "Patna", "Patna"
            ],
            "डायरेक्ट संपर्क": [
                "+91 98765***** 🔒", "+91 94310***** 🔒", "+91 91234***** 🔒", "+91 98350***** 🔒",
                "+91 98111***** 🔒", "+91 98200***** 🔒", "+91 98450***** 🔒",
                "+91 94302***** 🔒", "+91 98102***** 🔒", "+91 98212***** 🔒",
                "+91 97714***** 🔒", "+91 94314***** 🔒"
            ]
        })
    
    df_leads = load_db()
    st.dataframe(df_leads.head(5), use_container_width=True, hide_index=True)
    
    st.markdown("""
    <div class="unlock-card">
        <h3 style="color: #F59E0B; margin: 0; font-size: 16px;">👑 संपूर्ण ऑल-इंडिया डायरेक्टरी अनलॉक करें</h3>
        <p style="color: #94A3B8; font-size: 11px; margin: 4px 0;">सभी चालू मोबाइल नंबर एक्सेल शीट में पाएँ</p>
        <div class="price-tag">₹49</div>
    </div>
    """, unsafe_allow_html=True)
    
    upi_url = "upi://pay?pa=7484878449-2@ybl&pn=Vyapar%20Grow%20AI&am=49&cu=INR&tn=All%20India%20Leads"
    st.markdown(f'<a href="{upi_url}" class="upi-pay-btn">⚡ ₹49 पे करें (PhonePe / GPay)</a>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(f"https://api.qrserver.com/v1/create-qr-code/?size=160x160&data={urllib.parse.quote(upi_url)}", caption="स्कैन करके भुगतान करें", width=150)
        
    utr = st.text_input("", placeholder="12 अंकों का UTR नंबर दर्ज करें", key="lead_utr")
    if st.button("🚀 फ़ाइल डाउनलोड करें"):
        if len(utr.strip()) == 12 and utr.strip().isdigit():
            st.success("✅ पेमेंट सत्यापित!")
            st.download_button(
                label="📥 संपूर्ण डायरेक्टरी डाउनलोड करें (CSV)",
                data=df_leads.to_csv(index=False).encode('utf-8'),
                file_name="All_India_Directory.csv",
                mime="text/csv",
                use_container_width=True
            )
        else:
            st.error("कृपया सही 12 अंकों का UTR नंबर दर्ज करें।")
            
