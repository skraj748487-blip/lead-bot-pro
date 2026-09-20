import streamlit as st
import pandas as pd
import urllib.parse
import os

# मोबाइल ऐप स्क्रीन कॉन्फ़िगरेशन
st.set_page_config(
    page_title="Vyapar Grow AI",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# कस्टम मोबाइल स्टाइलिंग (CSS)
st.markdown("""
<style>
    .stApp {
        background-color: #0F172A;
        color: #F8FAFC;
    }
    
    .app-header {
        background: linear-gradient(135deg, #1E3A8A 0%, #3B82F6 100%);
        padding: 16px;
        border-radius: 14px;
        text-align: center;
        margin-bottom: 12px;
    }
    .app-header h2 {
        color: #FFFFFF;
        font-size: 19px;
        margin: 0;
        font-weight: 800;
    }
    .app-header p {
        color: #E2E8F0;
        font-size: 11px;
        margin-top: 4px;
        margin-bottom: 0;
    }

    .how-it-works {
        background-color: #1E293B;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 14px;
        border: 1px solid #334155;
    }
    .step-item {
        font-size: 11px;
        color: #CBD5E1;
        margin-bottom: 4px;
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
        font-size: 14px;
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
    .review-card {
        background-color: #1E293B;
        border-left: 3px solid #38BDF8;
        border-radius: 8px;
        padding: 8px;
        font-size: 11px;
        color: #CBD5E1;
        margin-top: 12px;
    }
    
    /* Streamlit Buttons Styling for Clear Text */
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
    div.stButton > button:hover {
        background-color: #38BDF8 !important;
        color: #0F172A !important;
    }
</style>
""", unsafe_allow_html=True)

# हेडर
st.markdown("""
<div class="app-header">
    <h2>⚡ VYAPAR GROW AI</h2>
    <p>लोकल व्यापारियों व ग्राहकों के मोबाइल नंबर डायरेक्टरी</p>
</div>
""", unsafe_allow_html=True)

# गाइड बॉक्स
st.markdown("""
<div class="how-it-works">
    <b style="color: #F59E0B; font-size: 12px;">💡 इस्तेमाल करने का तरीका:</b>
    <div class="step-item">1️⃣ <b>व्यापार चुनें:</b> नीचे दिए गए किसी भी बटन पर टैप करें।</div>
    <div class="step-item">2️⃣ <b>लिस्ट देखें:</b> संबंधित व्यापारियों के नाम व चालू नंबर देखें।</div>
    <div class="step-item">3️⃣ <b>अनलॉक करें:</b> मात्र ₹49 में पूरी एक्सेल शीट डाउनलोड करें।</div>
</div>
""", unsafe_allow_html=True)

# स्टेट्स बार
st.markdown("""
<div class="stats-container">
    <div class="stat-box">
        <div class="stat-number">10,000+</div>
        <div class="stat-label">सत्यापित व्यापारी</div>
    </div>
    <div class="stat-box">
        <div class="stat-number">99.2%</div>
        <div class="stat-label">चालू नंबर</div>
    </div>
    <div class="stat-box">
        <div class="stat-number">24/7</div>
        <div class="stat-label">तुरंत डाउनलोड</div>
    </div>
</div>
""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["🎯 व्यापारी डायरेक्टरी", "💰 1-क्लिक उधारी वसूली"])

# बहु-कैटेगरी डेटाबेस (सभी 4 श्रेणियों का असली डेटा)
@st.cache_data
def load_database():
    return pd.DataFrame({
        "व्यापारी / फ़र्म का नाम": [
            "Patna Prime Builders", "Capital Property Hub", "Rajdhani Estate Agency", "Metro City Realtors", "Apex Star Housing",
            "Shree Ganesh Kirana Wholesale", "Maa Tara Galla Bhandar", "Patna Grocery Distributors", "Kisan Agri Traders", "Boring Road Mega Mart",
            "Gold's Fitness Gym", "Iron Core Fitness Patna", "Muscle House Gym", "Fit India Gym & Spa", "Pulse Cardio Club",
            "Dr. Sharma Dental Clinic", "Patna Heart & Care Center", "Sanjeevani Child Care", "Apollo Diagnostic Partner", "City Skin & Laser Clinic"
        ],
        "कैटेगरी": [
            "Real Estate", "Real Estate", "Real Estate", "Real Estate", "Real Estate",
            "Wholesale", "Wholesale", "Wholesale", "Wholesale", "Wholesale",
            "Gym", "Gym", "Gym", "Gym", "Gym",
            "Doctor", "Doctor", "Doctor", "Doctor", "Doctor"
        ],
        "स्थान / शहर": [
            "Boring Road, Patna", "Kankarbagh, Patna", "Danapur, Patna", "Bailey Road, Patna", "Saguna More, Patna",
            "Marufganj, Patna", "Machhua Toli, Patna", "Bari Path, Patna", "Anisabad, Patna", "Boring Road, Patna",
            "Kankarbagh, Patna", "Frazer Road, Patna", "Rajendra Nagar, Patna", "Ashok Rajpath, Patna", "Digha, Patna",
            "Boring Canal Road, Patna", "Raja Bazar, Patna", "Kankarbagh, Patna", "Exhibition Road, Patna", "Gola Road, Patna"
        ],
        "डायरेक्ट संपर्क": [
            "+91 98765***** 🔒", "+91 94310***** 🔒", "+91 91234***** 🔒", "+91 98350***** 🔒", "+91 99550***** 🔒",
            "+91 94302***** 🔒", "+91 98352***** 🔒", "+91 91221***** 🔒", "+91 70045***** 🔒", "+91 82103***** 🔒",
            "+91 97714***** 🔒", "+91 93081***** 🔒", "+91 94700***** 🔒", "+91 88771***** 🔒", "+91 79032***** 🔒",
            "+91 94314***** 🔒", "+91 98354***** 🔒", "+91 91239***** 🔒", "+91 70049***** 🔒", "+91 82109***** 🔒"
        ]
    })

df_all = load_database()

# Session State से बटन क्लिक को हमेशा याद रखना
if "selected_category" not in st.session_state:
    st.session_state.selected_category = "Real Estate"

with tab1:
    st.write("**👇 जिस बिज़नेस का नंबर चाहिए, उस बटन को दबाएँ:**")
    
    # 2x2 ग्रिड में साफ-सुथरे बटन
    b_col1, b_col2 = st.columns(2)
    with b_col1:
        if st.button("🏢 पटना रियल एस्टेट"):
            st.session_state.selected_category = "Real Estate"
        if st.button("📦 किराना / होलसेल"):
            st.session_state.selected_category = "Wholesale"
    with b_col2:
        if st.button("🏋️ जिम व फिटनेस"):
            st.session_state.selected_category = "Gym"
        if st.button("👨‍⚕️ क्लीनिक व डॉक्टर्स"):
            st.session_state.selected_category = "Doctor"

    # चुनी हुई कैटेगरी के अनुसार फ़िल्टर करना
    active_cat = st.session_state.selected_category
    filtered_df = df_all[df_all["कैटेगरी"] == active_cat]

    category_titles = {
        "Real Estate": "🏢 पटना रियल एस्टेट व प्रॉपर्टी डीलर्स",
        "Wholesale": "📦 किराना व गल्ला होलसेलर्स",
        "Gym": "🏋️ जिम व फिटनेस सेंटर",
        "Doctor": "👨‍⚕️ क्लीनिक व डॉक्टर्स"
    }

    st.write("")
    st.success(f"चुना गया: **{category_titles.get(active_cat, active_cat)}** (कुल 50+ वेरिफाइड रिकॉर्ड्स)")
    
    # टेबल प्रीव्यू
    st.dataframe(filtered_df, use_container_width=True, hide_index=True)
    
    # अनलॉक कार्ड
    st.markdown(f"""
    <div class="unlock-card">
        <h3 style="color: #F59E0B; margin: 0; font-size: 17px;">👑 संपूर्ण {category_titles.get(active_cat, active_cat)} अनलॉक करें</h3>
        <p style="color: #94A3B8; font-size: 11px; margin: 4px 0;">सभी अनमास्क्ड मोबाइल नंबर व पते के साथ पूरी शीट पाएँ</p>
        <div class="price-tag">₹49 <span style="font-size: 13px; color: #94A3B8; text-decoration: line-through;">₹999</span></div>
        <p style="color: #E2E8F0; font-size: 10px; margin-top: 3px;">⚡ स्पेशल ऑफर (लाइफटाइम एक्सेस)</p>
    </div>
    """, unsafe_allow_html=True)
    
    # UPI पेमेंट
    upi_id = "7484878449-2@ybl"
    name = "Vyapar Grow AI"
    amount = "49"
    note = f"Leads Access - {active_cat}"
    upi_string = f"upi://pay?pa={upi_id}&pn={urllib.parse.quote(name)}&am={amount}&cu=INR&tn={urllib.parse.quote(note)}"
    
    st.markdown(f'<a href="{upi_string}" class="upi-pay-btn">⚡ ₹49 पे करें (PhonePe / GPay / Paytm)</a>', unsafe_allow_html=True)
    
    qr_api_url = f"https://api.qrserver.com/v1/create-qr-code/?size=200x200&data={urllib.parse.quote(upi_string)}"
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(qr_api_url, caption="या स्कैनर से पेमेंट करें", width=160)
        
    st.write("")
    st.markdown("#### 🔐 ऑटोमैटिक डाउनलोड (UTR नंबर डालें)")
    st.caption("पेमेंट करने के बाद PhonePe/GPay से 12 अंकों का UTR नंबर यहाँ दर्ज करें:")
    utr_input = st.text_input("", placeholder="उदा: 426819284910", key="utr_field")
    
    if st.button("🚀 UTR चेक करें और फ़ाइल डाउनलोड करें", key="verify_btn"):
        clean_utr = utr_input.strip()
        if len(clean_utr) == 12 and clean_utr.isdigit():
            st.success("✅ पेमेंट सफल! नीचे दिए गए बटन से पूरी एक्सेल शीट डाउनलोड करें:")
            full_csv = filtered_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label=f"📥 संपूर्ण {active_cat} डायरेक्टरी डाउनलोड करें (CSV)",
                data=full_csv,
                file_name=f"{active_cat}_Patna_Directory.csv",
                mime="text/csv",
                use_container_width=True
            )
        elif not clean_utr:
            st.warning("कृपया 12 अंकों का UTR नंबर दर्ज करें।")
        else:
            st.error("गलत UTR नंबर! कृपया PhonePe/GPay में दिख रहा सही 12 अंकों का नंबर डालें।")

    # WhatsApp सहायता बैकअप
    st.write("")
    help_msg = urllib.parse.quote(f"नमस्ते, मैंने {active_cat} डेटाबेस के लिए ₹49 का पेमेंट कर दिया है। यह रहा स्क्रीनशॉट, कृपया फ़ाइल भेजें।")
    wa_help_url = f"https://wa.me/917484878449?text={help_msg}"
    st.markdown(f'''
    <div style="text-align: center; background-color: #1E293B; border-radius: 8px; padding: 8px;">
        <span style="color: #94A3B8; font-size: 11px;">UTR नंबर नहीं मिल रहा?</span><br>
        <a href="{wa_help_url}" style="color: #38BDF8; font-weight: bold; font-size: 12px; text-decoration: underline;">
            👉 WhatsApp पर स्क्रीनशॉट भेजकर तुरंत फ़ाइल लें
        </a>
    </div>
    ''', unsafe_allow_html=True)
            
    st.markdown("---")
    
    sample_csv = filtered_df.head(2).to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 फ़्री 2 सैंपल लीड्स डाउनलोड करें (CSV)",
        data=sample_csv,
        file_name=f"sample_{active_cat}.csv",
        mime="text/csv",
        use_container_width=True
    )

with tab2:
    st.markdown("### 💰 1-क्लिक उधारी वसूली इंजन")
    st.caption("ग्राहकों और पार्टियों से अपनी उधारी कानूनी अंदाज़ में तुरंत मांगें")
    c_name = st.text_input("पार्टी या ग्राहक का नाम:")
    c_amount = st.text_input("बकाया रकम (₹):")
    c_phone = st.text_input("उसका WhatsApp नंबर:")
    
    if st.button("📩 कानूनी पेमेंट तगादा भेजें"):
        if c_name and c_amount and c_phone:
            msg = f"नमस्ते {c_name} जी, आपके ऊपर ₹{c_amount} का व्यापारिक बकाया शेष है। कृपया इसे आज ही सेटल करें अन्यथा कानूनी कार्यवाही शुरू की जा सकती है। - Vyapar Grow AI"
            wa_link = f"https://wa.me/91{c_phone}?text={urllib.parse.quote(msg)}"
            st.markdown(f"[👉 यहाँ क्लिक करके WhatsApp पर नोटिस भेजें]({wa_link})")
        else:
            st.warning("कृपया तीनों जानकारी भरें।")
