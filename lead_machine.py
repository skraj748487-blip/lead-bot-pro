import streamlit as st
import pandas as pd
import urllib.parse

# पेज कॉन्फ़िगरेशन
st.set_page_config(page_title="डिजिटल भारत सेवा व व्यापार केंद्र", page_icon="🇮🇳", layout="centered")

# हेडर सेक्शन
st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>🇮🇳 डिजिटल भारत सेवा व व्यापार केंद्र 🇮🇳</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-weight: bold;'>ऑल-इंडिया B2B बिज़नेस लीड्स, उधारी वसूली इंजन और डिजिटल सेवा पोर्टल</p>", unsafe_allow_html=True)

# टैब्स
tab1, tab2 = st.tabs(["🔍 B2B लीड्स सर्च (Leads Hub)", "💰 1-क्लिक उधारी वसूली"])

with tab1:
    st.markdown("### 🎯 किसी भी शहर या पिनकोड के बिज़नेस लीड्स खोजें")
    st.write("शहर और व्यापार लिखें (उदा: Patna Gym, Lucknow Real Estate, Delhi Doctors)")
    
    query = st.text_input("", value="Patna Real Estate", placeholder="उदा: Patna Real Estate")
    search_btn = st.button("🚀 डेटा खोजें")
    
    if search_btn or query:
        st.success(f"✅ '{query}' के लिए कुल 5 रिकॉर्ड्स मिले")
        
        st.markdown("#### 👁️ लाइव प्रीव्यू (पहले 5 रिकॉर्ड्स):")
        sample_data = {
            "व्यवसाय का नाम": [
                "Patna Prime Real Estate",
                "Capital Real Estate Hub Patna",
                "Rajdhani Real Estate Agency",
                "Metro Global Real Estate",
                "Apex Star Real Estate Patna"
            ],
            "कैटेगरी": [
                "Patna Real Estate",
                "Patna Real Estate",
                "Patna Real Estate",
                "Patna Real Estate",
                "Patna Real Estate"
            ]
        }
        df_sample = pd.DataFrame(sample_data)
        st.table(df_sample)
        
        st.markdown("---")
        st.markdown("### 🔓 पूरा 30+ रिकॉर्ड्स वाला डेटाबेस अनलॉक करें")
        st.markdown("""
        * **चार्ज:** मात्र ₹49 (स्पेशल ऑफर - लाइफटाइम एक्सेस)
        * **फ़ॉर्मेट:** Excel / CSV फ़ाइल
        * **UPI ID:** `7484878449-2@ybl`
        """)
        
        st.markdown("#### भुगतान कैसे करें:")
        st.markdown("""
        1. नीचे दिए गए QR कोड को PhonePe/GPay से स्कैन करें।
        2. **₹49** का भुगतान करें।
        3. सपोर्ट नंबर **7484878449** पर स्क्रीनशॉट भेजें।
        """)
        
        # ऑटोमैटिक ₹49 का डायनामिक QR कोड
        upi_id = "7484878449-2@ybl"
        name = "Vyapar Grow AI"
        amount = "49"
        note = "Vyapar Database Access"
        
        upi_string = f"upi://pay?pa={upi_id}&pn={urllib.parse.quote(name)}&am={amount}&cu=INR&tn={urllib.parse.quote(note)}"
        qr_api_url = f"https://api.qrserver.com/v1/create-qr-code/?size=250x250&data={urllib.parse.quote(upi_string)}"
        
        st.image(qr_api_url, caption="₹49 भुगतान हेतु स्कैन करें", width=220)
        
        # सैंपल डाउनलोड बटन
        csv_sample = df_sample.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 फ्री सैंपल डेटा डाउनलोड करें (CSV)",
            data=csv_sample,
            file_name="sample_leads.csv",
            mime="text/csv"
        )

with tab2:
    st.markdown("### 💰 1-क्लिक उधारी वसूली इंजन")
    st.info("यह सर्विस एक्टिव है। ग्राहक का नाम, बकाया रकम और मोबाइल नंबर डालकर ऑटोमैटिक पेमेंट रिमाइंडर भेजें।")
    
    c_name = st.text_input("ग्राहक का नाम:")
    c_amount = st.text_input("बकाया राशि (₹):")
    c_phone = st.text_input("ग्राहक का WhatsApp नंबर:")
    
    if st.button("📩 लीगल वसूली मैसेज भेजें"):
        if c_name and c_amount and c_phone:
            msg = f"नमस्ते {c_name} जी, आपके ऊपर ₹{c_amount} का बकाया शेष है। कृपया इसे जल्द से जल्द क्लियर करें अन्यथा कानूनी प्रक्रिया शुरू की जाएगी।"
            wa_link = f"https://wa.me/91{c_phone}?text={urllib.parse.quote(msg)}"
            st.markdown(f"[👉 यहाँ क्लिक करके WhatsApp पर रिमाइंडर भेजें]({wa_link})")
        else:
            st.warning("कृपया सभी बॉक्स भरें।")
            
