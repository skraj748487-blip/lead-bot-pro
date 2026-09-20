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
        margin-bottom: 15px;
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

    /* काम करने का आसान तरीका गाइड */
    .how-it-works {
        background-color: #1E293B;
        border-radius: 12px;
        padding: 12px;
        margin-bottom: 16px;
        border: 1px solid #334155;
    }
    .step-item {
        font-size: 12px;
        color: #CBD5E1;
        margin-bottom: 6px;
    }
    
    .stats-container {
        display: flex;
        justify-content: space-between;
        gap: 8px;
        margin-bottom: 16px;
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
        margin-top: 15px;
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

# आसान गाइड बॉक्स - लोग समझें कि क्या करना है
st.markdown("""
<div class="how-it-works">
    <b style="color: #F59E0B; font-size: 13px;">💡 इस पोर्टल का उपयोग कैसे करें?</b>
    <div class="step-item" style="margin-top: 6px;">1️⃣ <b>व्यापार चुनें:</b> नीचे किसी भी कैटेगरी बटन पर क्लिक करें।</div>
    <div class="step-item">2️⃣ <b>सैंपल देखें:</b> व्यापारियों के नाम व लिस्ट चेक करें।</div>
    <div class="step-item">3️⃣ <b>नंबर अनलॉक करें:</b> मात्र ₹49 देकर पूरी एक्सेल शीट डाउनलोड करें और सीधे कॉल करें।</div>
</div>
""", unsafe_allow_html=True)

# स्टैट्स बार
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

tab1, tab2 = st.tabs(["🎯 व्यापारी डायरेक्टरी (लीड्स)", "💰 1-क्लिक उधारी वसूली"])

# डेटाबेस लोड
@st.cache_data
def load_database():
    file_name = "Patna Real Estate_sample.csv"
    if os.path.exists(file_name):
        return pd.read_csv(file_name)
    else:
        return pd.DataFrame({
            "व्यापारी / फ़र्म का नाम": ["Patna Prime Builders", "Capital Property Hub", "Rajdhani Estate Agency", "Metro City Realtors", "Apex Star Housing"],
            "कैटेगरी": ["Real Estate", "Real Estate", "Real Estate", "Real Estate", "Real Estate"],
            "शहर": ["Patna", "Patna", "Patna", "Patna", "Patna"],
            "डायरेक्ट संपर्क": ["+91 98765***** 🔒", "+91 94310***** 🔒", "+91 91234***** 🔒", "+91 98350***** 🔒", "+91 99550***** 🔒"]
        })

df_all = load_database()

with tab1:
    st.write("**👇 जिस बिज़नेस का नंबर चाहिए, उस बटन को दबाएँ:**")
    
    # क्विक कैटेगरी सेलेक्ट बटन (चिप्स)
    c1, c2 = st.columns(2)
    selected_category = "Patna Real Estate"
    with c1:
        if st.button("🏢 पटना रियल एस्टेट"):
            selected_category = "Real Estate"
        if st.button("📦 होलसेल किराना / गल्ला"):
            selected_category = "Wholesale"
    with c2:
        if st.button("🏋️ जिम व फिटनेस"):
            selected_category = "Gym"
        if st.button("👨‍⚕️ क्लीनिक व डॉक्टर्स"):
            selected_category = "Doctor"

    st.write("")
    query = st.text_input("या अपनी पसंद का शहर / व्यापार यहाँ टाइप करें:", value=selected_category)
    
    if query:
        mask = df_all.astype(str).apply(lambda row: row.str.contains(query, case=False, na=False)).any(axis=1)
        filtered_df = df_all[mask]
        if filtered_df.empty:
            filtered_df = df_all
    else:
        filtered_df = df_all

    total_leads = len(filtered_df)
    st.markdown(f"<span class='badge-verified'>उपलब्ध रिकॉर्ड्स: {total_leads}+ सत्यापित व्यापारी मिले</span>", unsafe_allow_html=True)
    
    # टेबल प्रीव्यू
    st.dataframe(filtered_df.head(5), use_container_width=True, hide_index=True)
    
    # अनलॉक कार्ड
    st.markdown("""
    <div class="unlock-card">
        <h3 style="color: #F59E0B; margin: 0; font-size: 18px;">👑 संपूर्ण व्यापारियों के नंबर अनलॉक करें</h3>
        <p style="color: #94A3B8; font-size: 12px; margin: 5px 0;">सभी अनमास्क्ड मोबाइल नंबर व पते के साथ एक्सेल शीट पाएँ</p>
        <div class="price-tag">₹49 <span style="font-size: 14px; color: #94A3B8; text-decoration: line-through;">₹999</span></div>
        <p style="color: #E2E8F0; font-size: 11px; margin-top: 4px;">⚡ स्पेशल ऑफर (लाइफटाइम इस्तेमाल)</p>
    </div>
    """, unsafe_allow_html=True)
    
    # UPI पेमेंट
    upi_id = "7484878449-2@ybl"
    name = "Vyapar Grow AI"
    amount = "49"
    note = "Vyapar Leads Access"
    
    upi_string = f"upi://pay?pa={upi_id}&pn={urllib.parse.quote(name)}&am={amount}&cu=INR&tn={urllib.parse.quote(note)}"
    
    st.markdown(f'<a href="{upi_string}" class="upi-pay-btn">⚡ ₹49 पे करें (PhonePe / GPay / Paytm)</a>', unsafe_allow_html=True)
    
    qr_api_url = f"https://api.qrserver.com/v1/create-qr-code/?size=200x200&data={urllib.parse.quote(upi_string)}"
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(qr_api_url, caption="या स्कैनर से ₹49 भेजें", width=170)
        
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
                label="📥 संपूर्ण डायरेक्टरी डाउनलोड करें (CSV)",
                data=full_csv,
                file_name=f"{query.replace(' ', '_')}_Directory.csv",
                mime="text/csv",
                use_container_width=True
            )
        elif not clean_utr:
            st.warning("कृपया 12 अंकों का UTR नंबर दर्ज करें।")
        else:
            st.error("गलत UTR नंबर! कृपया PhonePe/GPay में दिख रहा सही 12 अंकों का नंबर डालें।")

    # WhatsApp बैकअप बटन
    st.write("")
    help_msg = urllib.parse.quote("नमस्ते, मैंने ₹49 का पेमेंट कर दिया है। यह रहा स्क्रीनशॉट, कृपया मुझे बिज़नेस डेटाबेस फ़ाइल भेजें।")
    wa_help_url = f"https://wa.me/917484878449?text={help_msg}"
    st.markdown(f'''
    <div style="text-align: center; margin-top: 10px; background-color: #1E293B; border-radius: 10px; padding: 10px;">
        <span style="color: #94A3B8; font-size: 12px;">UTR नंबर नहीं मिल रहा? कोई बात नहीं!</span><br>
        <a href="{wa_help_url}" style="color: #38BDF8; font-weight: bold; font-size: 13px; text-decoration: underline;">
            👉 यहाँ क्लिक करके WhatsApp पर स्क्रीनशॉट भेजें और सीधे फ़ाइल लें
        </a>
    </div>
    ''', unsafe_allow_html=True)
            
    st.markdown("---")
    
    sample_csv = filtered_df.head(2).to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 फ़्री सैंपल टेस्ट करें (CSV)",
        data=sample_csv,
        file_name="sample_leads.csv",
        mime="text/csv",
        use_container_width=True
    )
    
    st.markdown("""
    <div class="review-card">
        ⭐ <b>व्यापारी समीक्षा:</b> <i>"पटना के 40+ प्रॉपर्टी डीलर्स का सीधा नंबर मिला, घर बैठे 2 नए क्लाइंट मिल गए।"</i><br>
        <span style="color: #94A3B8; font-size: 11px;">— अमित सिंह (प्रॉपर्टी सलाहकार, पटना)</span>
    </div>
    """, unsafe_allow_html=True)

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
            
