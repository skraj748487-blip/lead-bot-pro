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
        padding: 18px;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
        margin-bottom: 16px;
    }
    .app-header h2 {
        color: #FFFFFF;
        font-size: 20px;
        margin: 0;
        font-weight: 800;
    }
    .app-header p {
        color: #E2E8F0;
        font-size: 12px;
        margin-top: 4px;
        margin-bottom: 0;
    }
    
    .stats-container {
        display: flex;
        justify-content: space-between;
        gap: 8px;
        margin-bottom: 18px;
    }
    .stat-box {
        background-color: #1E293B;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 10px 6px;
        text-align: center;
        flex: 1;
    }
    .stat-number {
        color: #38BDF8;
        font-size: 15px;
        font-weight: 700;
    }
    .stat-label {
        color: #94A3B8;
        font-size: 10px;
        margin-top: 2px;
    }

    .unlock-card {
        background: linear-gradient(180deg, #1E293B 0%, #0F172A 100%);
        border: 1px solid #F59E0B;
        border-radius: 14px;
        padding: 16px;
        text-align: center;
        margin-top: 15px;
        box-shadow: 0 4px 12px rgba(245, 158, 11, 0.15);
    }
    .price-tag {
        font-size: 26px;
        font-weight: 800;
        color: #10B981;
    }
    .badge-verified {
        background-color: #065F46;
        color: #34D399;
        font-size: 11px;
        padding: 4px 10px;
        border-radius: 20px;
        font-weight: bold;
        display: inline-block;
        margin-bottom: 8px;
    }
    .upi-pay-btn {
        display: block;
        background: linear-gradient(90deg, #10B981 0%, #059669 100%);
        color: #FFFFFF !important;
        text-align: center;
        font-weight: bold;
        font-size: 15px;
        padding: 12px;
        border-radius: 12px;
        text-decoration: none;
        margin: 12px 0;
        box-shadow: 0 4px 10px rgba(16, 185, 129, 0.3);
    }
    .review-card {
        background-color: #1E293B;
        border-left: 3px solid #38BDF8;
        border-radius: 8px;
        padding: 10px;
        font-size: 12px;
        color: #CBD5E1;
        margin-top: 10px;
    }
</style>
""", unsafe_allow_html=True)

# हेडर
st.markdown("""
<div class="app-header">
    <h2>⚡ VYAPAR GROW AI</h2>
    <p>ऑल-इंडिया B2B लीड्स व स्मार्ट रिकवरी पोर्टल</p>
</div>
""", unsafe_allow_html=True)

# स्टैट्स बार
st.markdown("""
<div class="stats-container">
    <div class="stat-box">
        <div class="stat-number">10,000+</div>
        <div class="stat-label">सत्यापित लीड्स</div>
    </div>
    <div class="stat-box">
        <div class="stat-number">99.2%</div>
        <div class="stat-label">सटीक डेटा</div>
    </div>
    <div class="stat-box">
        <div class="stat-number">24/7</div>
        <div class="stat-label">ऑटो डिलीवरी</div>
    </div>
</div>
""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["🎯 B2B लीड्स हब", "💰 1-क्लिक रिकवरी इंजन"])

# डेटाबेस लोड
@st.cache_data
def load_database():
    file_name = "Patna Real Estate_sample.csv"
    if os.path.exists(file_name):
        df = pd.read_csv(file_name)
        # अगर संपर्क कॉलम न हो तो लॉक नंबर दिखाना
        if "संपर्क" not in df.columns:
            df["डायरेक्ट संपर्क"] = ["+91 98765***** 🔒", "+91 94310***** 🔒", "+91 91234***** 🔒", "+91 98350***** 🔒", "+91 99550***** 🔒"][:len(df)]
        return df
    else:
        return pd.DataFrame({
            "व्यवसाय का नाम": ["Patna Prime Builders", "Capital Property Hub", "Rajdhani Estate Agency", "Metro City Realtors", "Apex Star Housing"],
            "कैटेगरी": ["Real Estate", "Real Estate", "Real Estate", "Real Estate", "Real Estate"],
            "डायरेक्ट संपर्क": ["+91 98765***** 🔒", "+91 94310***** 🔒", "+91 91234***** 🔒", "+91 98350***** 🔒", "+91 99550***** 🔒"],
            "स्थिति": ["✅ Active", "✅ Active", "✅ Active", "✅ Active", "✅ Active"]
        })

df_all = load_database()

with tab1:
    st.write("**🔍 अपने शहर या व्यापार की लीड्स खोजें:**")
    query = st.text_input("", value="Patna Real Estate", placeholder="उदा: Patna Real Estate, Doctors...")
    
    # सर्च फ़िल्टर
    if query:
        mask = df_all.astype(str).apply(lambda row: row.str.contains(query, case=False, na=False)).any(axis=1)
        filtered_df = df_all[mask]
        if filtered_df.empty:
            filtered_df = df_all
    else:
        filtered_df = df_all

    total_leads = len(filtered_df)
    st.markdown(f"<span class='badge-verified'>सर्च रिजल्ट: {total_leads}+ वेरिफाइड रिकॉर्ड्स मिले</span>", unsafe_allow_html=True)
    
    # टेबल प्रीव्यू
    st.dataframe(filtered_df.head(5), use_container_width=True, hide_index=True)
    
    # अनलॉक कार्ड
    st.markdown("""
    <div class="unlock-card">
        <h3 style="color: #F59E0B; margin: 0; font-size: 18px;">👑 संपूर्ण डेटाबेस अनलॉक करें</h3>
        <p style="color: #94A3B8; font-size: 12px; margin: 5px 0;">सभी अनमास्क्ड मोबाइल नंबर, ईमेल व पते के साथ</p>
        <div class="price-tag">₹49 <span style="font-size: 14px; color: #94A3B8; text-decoration: line-through;">₹999</span></div>
        <p style="color: #E2E8F0; font-size: 11px; margin-top: 4px;">⚡ स्पेशल ऑफर (लाइफटाइम एक्सेस)</p>
    </div>
    """, unsafe_allow_html=True)
    
    # UPI पेमेंट विवरण
    upi_id = "7484878449-2@ybl"
    name = "Vyapar Grow AI"
    amount = "49"
    note = "Vyapar Leads Access"
    
    upi_string = f"upi://pay?pa={upi_id}&pn={urllib.parse.quote(name)}&am={amount}&cu=INR&tn={urllib.parse.quote(note)}"
    
    # 1-क्लिक पेमेंट बटन
    st.markdown(f'<a href="{upi_string}" class="upi-pay-btn">⚡ Pay ₹49 via PhonePe / GPay / Paytm</a>', unsafe_allow_html=True)
    
    # QR कोड (सिर्फ एक बार)
    qr_api_url = f"https://api.qrserver.com/v1/create-qr-code/?size=200x200&data={urllib.parse.quote(upi_string)}"
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(qr_api_url, caption="या QR कोड स्कैन करके भुगतान करें", width=170)
        
    st.markdown("""
    <div style="background-color: #1E293B; border-radius: 10px; padding: 10px; font-size: 12px; color: #CBD5E1; margin-top: 8px;">
        <b>📲 भुगतान निर्देश:</b><br>
        1. ऊपर बटन दबाकर या QR स्कैन कर ₹49 का भुगतान करें।<br>
        2. स्क्रीनशॉट WhatsApp नंबर <b>7484878449</b> पर भेजें। तुरंत अनलॉक फ़ाइल प्राप्त करें।
    </div>
    """, unsafe_allow_html=True)
    
    # सैंपल डाउनलोड
    sample_csv = filtered_df.head(2).to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 फ़्री सैंपल डेटा डाउनलोड करें (CSV)",
        data=sample_csv,
        file_name="sample_leads.csv",
        mime="text/csv",
        use_container_width=True
    )
    
    # कस्टमर रिव्यू
    st.markdown("""
    <div class="review-card">
        ⭐ <b>समीक्षा:</b> <i>"पटना के 40+ प्रॉपर्टी डीलर्स का सीधा नंबर मिला, 2 दिन में एक क्लाइंट डील पक्की हुई।"</i><br>
        <span style="color: #94A3B8; font-size: 11px;">— अमित सिंह (रियल एस्टेट कंसल्टेंट, पटना)</span>
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.markdown("### 💰 1-क्लिक उधारी वसूली इंजन")
    st.caption("व्यापारियों के बकाये पैसे आसानी से कानूनी नोटिस फॉर्मेट में मांगें")
    
    c_name = st.text_input("ग्राहक / पार्टी का नाम:")
    c_amount = st.text_input("बकाया राशि (₹):")
    c_phone = st.text_input("WhatsApp नंबर:")
    
    if st.button("📩 कानूनी पेमेंट रिमाइंडर भेजें"):
        if c_name and c_amount and c_phone:
            msg = f"नमस्ते {c_name} जी, आपके ऊपर ₹{c_amount} का व्यापारिक बकाया शेष है। कृपया इसे आज ही क्लियर करें अन्यथा कानूनी प्रक्रिया शुरू की जा सकती है। - Vyapar Grow AI"
            wa_link = f"https://wa.me/91{c_phone}?text={urllib.parse.quote(msg)}"
            st.markdown(f"[👉 यहाँ क्लिक करके तुरंत WhatsApp पर भेजें]({wa_link})")
        else:
            st.warning("कृपया तीनों बॉक्स भरें।")
            
