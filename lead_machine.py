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
    /* बैकग्राउंड और फॉन्ट */
    .stApp {
        background-color: #0F172A;
        color: #F8FAFC;
    }
    
    /* ऐप हेडर कार्ड */
    .app-header {
        background: linear-gradient(135deg, #1E3A8A 0%, #3B82F6 100%);
        padding: 20px;
        border-radius: 18px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
        margin-bottom: 20px;
    }
    .app-header h2 {
        color: #FFFFFF;
        font-size: 22px;
        margin: 0;
        font-weight: 800;
        letter-spacing: 0.5px;
    }
    .app-header p {
        color: #E2E8F0;
        font-size: 13px;
        margin-top: 6px;
        margin-bottom: 0;
    }
    
    /* मेट्रिक्स कार्ड्स */
    .stats-container {
        display: flex;
        justify-content: space-between;
        gap: 10px;
        margin-bottom: 20px;
    }
    .stat-box {
        background-color: #1E293B;
        border: 1px solid #334155;
        border-radius: 14px;
        padding: 12px 8px;
        text-align: center;
        flex: 1;
    }
    .stat-number {
        color: #38BDF8;
        font-size: 16px;
        font-weight: 700;
    }
    .stat-label {
        color: #94A3B8;
        font-size: 11px;
        margin-top: 2px;
    }

    /* प्रीमियम अनलॉक बॉक्स */
    .unlock-card {
        background: linear-gradient(180deg, #1E293B 0%, #0F172A 100%);
        border: 1px solid #F59E0B;
        border-radius: 16px;
        padding: 18px;
        text-align: center;
        margin-top: 20px;
        box-shadow: 0 4px 12px rgba(245, 158, 11, 0.15);
    }
    .price-tag {
        font-size: 28px;
        font-weight: 800;
        color: #10B981;
    }
    .badge-verified {
        background-color: #065F46;
        color: #34D399;
        font-size: 11px;
        padding: 3px 8px;
        border-radius: 20px;
        font-weight: bold;
    }

    /* बटन स्टाइल */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        background: linear-gradient(90deg, #2563EB 0%, #1D4ED8 100%);
        color: white;
        font-weight: bold;
        border: none;
        padding: 10px;
        height: 48px;
    }
</style>
""", unsafe_allow_html=True)

# 1. हेडर कार्ड
st.markdown("""
<div class="app-header">
    <h2>⚡ VYAPAR GROW AI</h2>
    <p>ऑल-इंडिया B2B लीड्स व स्मार्ट रिकवरी पोर्टल</p>
</div>
""", unsafe_allow_html=True)

# 2. लाइव स्टैट्स बार
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
        <div class="stat-label">इंस्टेंट डिलीवरी</div>
    </div>
</div>
""", unsafe_allow_html=True)

# टैब्स
tab1, tab2 = st.tabs(["🎯 B2B लीड्स हब", "💰 1-क्लिक रिकवरी इंजन"])

# डेटाबेस लोड करने का फंक्शन
@st.cache_data
def load_database():
    file_name = "Patna Real Estate_sample.csv"
    if os.path.exists(file_name):
        return pd.read_csv(file_name)
    else:
        return pd.DataFrame({
            "व्यवसाय का नाम": ["Patna Prime Builders", "Capital Property Hub", "Rajdhani Estate Agency", "Metro City Realtors", "Global Infra Patna"],
            "कैटेगरी": ["Real Estate", "Real Estate", "Real Estate", "Real Estate", "Real Estate"],
            "संपर्क": ["98765***** (Locked)", "94310***** (Locked)", "91234***** (Locked)", "98350***** (Locked)", "99550***** (Locked)"],
            "वेरिफिकेशन": ["✅ Verified", "✅ Verified", "✅ Verified", "✅ Verified", "✅ Verified"]
        })

df_all = load_database()

with tab1:
    st.write("**🔍 अपने व्यापार या शहर की लीड्स खोजें:**")
    query = st.text_input("", value="Patna Real Estate", placeholder="शहर या बिज़नेस टाइप लिखें...")
    
    if st.button("🚀 सर्च लीड्स"):
        pass
    
    if query:
        mask = df_all.astype(str).apply(lambda row: row.str.contains(query, case=False, na=False)).any(axis=1)
        filtered_df = df_all[mask]
        if filtered_df.empty:
            filtered_df = df_all
            
        total_leads = len(filtered_df)
        
        st.markdown(f"<span class='badge-verified'>सर्च पूरा हुआ: {total_leads}+ रिकॉर्ड्स उपलब्ध</span>", unsafe_allow_html=True)
        st.write("")
        
        # टेबल प्रीव्यू
        st.dataframe(filtered_df.head(5), use_container_width=True, hide_index=True)
        
        # प्रीमियम कार्ड
        st.markdown(f"""
        <div class="unlock-card">
            <h3 style="color: #F59E0B; margin: 0;">👑 पूरा डेटाबेस अनलॉक करें</h3>
            <p style="color: #94A3B8; font-size: 13px; margin: 6px 0;">संपूर्ण नाम, डायरेक्ट कॉलिंग नंबर व पते के साथ</p>
            <div class="price-tag">₹49 <span style="font-size: 14px; color: #94A3B8; text-decoration: line-through;">₹999</span></div>
            <p style="color: #E2E8F0; font-size: 12px; margin-top: 5px;">⚡ स्पेशल लॉन्च ऑफर (लाइफटाइम एक्सेस)</p>
        </div>
        """, unsafe_allow_html=True)
        
        # UPI स्ट्रिंग और QR कोड
        upi_id = "7484878449-2@ybl"
        name = "Vyapar Grow AI"
        amount = "49"
        note = "Vyapar Database Access"
        
        upi_string = f"upi://pay?pa={upi_id}&pn={urllib.parse.quote(name)}&am={amount}&cu=INR&tn={urllib.parse.quote(note)}"
        qr_api_url = f"https://api.qrserver.com/v1/create-qr-code/?size=220x220&data={urllib.parse.quote(upi_string)}"
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.write("")
            st.image(qr_api_url, caption="PhonePe / GPay से स्कैन करें", width=180)
            
        st.markdown("""
        <div style="background-color: #1E293B; border-radius: 12px; padding: 12px; font-size: 12px; color: #CBD5E1; margin-top: 10px;">
            <b>📲 भुगतान निर्देश:</b><br>
            1. QR कोड स्कैन कर ₹49 भेजें।<br>
            2. स्क्रीनशॉट WhatsApp नंबर <b>7484878449</b> पर भेजें। तुरंत फ़ाइल मिल जाएगी।
        </div>
        """, unsafe_allow_html=True)
        
        # सैंपल CSV डाउनलोड
        sample_csv = filtered_df.head(2).to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 मुफ़्त सैंपल डेटा टेस्ट करें (CSV)",
            data=sample_csv,
            file_name="sample_leads.csv",
            mime="text/csv"
        )

with tab2:
    st.markdown("### 💰 1-क्लिक उधारी वसूली इंजन")
    st.caption("व्यापारियों के बकाये पैसे आसानी से कानूनी नोटिस फॉर्मेट में मांगें")
    
    c_name = st.text_input("ग्राहक / पार्टी का नाम:")
    c_amount = st.text_input("बकाया राशि (₹):")
    c_phone = st.text_input("WhatsApp नंबर:")
    
    if st.button("📩 कानूनी पेमेंट रिमाइंडर भेजें"):
        if c_name and c_amount and c_phone:
            msg = f"नमस्ते {c_name} जी, आपके ऊपर ₹{c_amount} का व्यापारिक बकाया शेष है। कृपया इसे आज ही सेटल करें अन्यथा कानूनी कार्यवाही शुरू की जा सकती है। - Vyapar Grow AI"
            wa_link = f"https://wa.me/91{c_phone}?text={urllib.parse.quote(msg)}"
            st.markdown(f"[👉 यहाँ क्लिक करके तुरंत WhatsApp पर भेजें]({wa_link})")
        else:
            st.warning("कृपया तीनों बॉक्स भरें।")
            
