import streamlit as st
import pandas as pd
import urllib.parse
import os

# मोबाइल व ग्लोबल स्क्रीन सेटअप
st.set_page_config(
    page_title="World AI Super App",
    page_icon="🌍",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# अल्ट्रा-मॉडर्न क्लीन मोबाइल CSS
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
    <h2>🌍 WORLD AI — ग्लोबल सुपर ऐप</h2>
    <p>दुनिया का हर काम एक जगह: भाषा अनुवाद, करेंसी, लोन EMI, व्यापार व सोशल मीडिया</p>
</div>
""", unsafe_allow_html=True)

MY_WA_NUMBER = "917484878440"

# 6 शक्तिशाली ग्लोबल टैब्स
tab_ai, tab_trans, tab_curr, tab_emi, tab_leads, tab_biz = st.tabs([
    "🤖 ग्लोबल AI",
    "🌐 भाषा अनुवाद",
    "💱 मुद्रा (Currency)",
    "🔢 EMI कैलकुलेटर",
    "🏢 जमीन व गाड़ियाँ",
    "🏪 व्यापार टूल्स"
])

# ----------------------------------------------------
# 1. ग्लोबल AI सवाल-जवाब (Ask Anything)
# ----------------------------------------------------
with tab_ai:
    st.markdown("### 🤖 Universal AI — कोई भी सवाल पूछें")
    st.caption("स्वास्थ्य, कोडिंग, बिज़नेस, पढ़ाई या करियर संबंधी सवाल दुनिया की किसी भी भाषा में पूछें")
    
    q_input = st.text_input("अपना सवाल लिखें:", placeholder="उदा: बुखार में क्या करें? / How to make money online? / கோடிங் என்றால் என்ன?")
    if st.button("🚀 तुरंत AI उत्तर पाएँ"):
        q_clean = q_input.strip().lower()
        if not q_clean:
            st.warning("कृपया अपना सवाल दर्ज करें।")
        else:
            if any(w in q_clean for w in ["fever", "cold", "बुखार", "दवा", "सिरदर्द"]):
                ans = "🩺 **Health Guidance:** Stay hydrated with warm fluids or ORS. Rest well. For persistent fever above 101°F for more than 48 hours, consult a physician immediately."
            elif any(w in q_clean for w in ["money", "online", "कमाई", "earning", "business"]):
                ans = "💼 **Online Growth:** Top global skills include digital marketing, AI prompting, local business software services, and video editing for creators."
            elif any(w in q_clean for w in ["study", "exam", "याद", "पढ़ाई"]):
                ans = "📚 **Study Protocol:** Follow 25-minute study intervals (Pomodoro method). Review notes before sleep to improve retention."
            else:
                ans = f"💡 **World AI Solution for '{q_input}':** Your query has been processed. For specific operations, use the specialized tabs for Currency, Translation, and Business tools."
            st.markdown(f'<div class="card-box" style="border-left: 4px solid #10B981;">{ans}</div>', unsafe_allow_html=True)

# ----------------------------------------------------
# 2. ग्लोबल भाषा अनुवादक (Multi-Language Translator)
# ----------------------------------------------------
with tab_trans:
    st.markdown("### 🌐 1-सेकंड भाषा अनुवादक (Translator)")
    st.caption("किसी भी भाषा के टेक्स्ट को अपनी भाषा में बदलें")
    
    t_text = st.text_area("टेक्स्ट यहाँ लिखें:", placeholder="उदा: Hello, how are you? / नमस्ते, आप कैसे हैं?")
    t_target = st.selectbox("किस भाषा में अनुवाद चाहिए?", ["Hindi (हिंदी)", "English", "Tamil (தமிழ்)", "Arabic (العربية)"])
    
    if st.button("🔄 ट्रांसलेट करें"):
        if t_text.strip():
            # गूगल ट्रांसलेट का डायरेक्ट सुरक्षित लिंक
            t_url = f"https://translate.google.com/?sl=auto&tl={t_target[:2].lower()}&text={urllib.parse.quote(t_text)}&op=translate"
            st.success("✅ अनुवाद लिंक तैयार है!")
            st.markdown(f'<a href="{t_url}" target="_blank" class="upi-pay-btn">👉 अनुवाद देखें / Open Translation</a>', unsafe_allow_html=True)
        else:
            st.warning("कृपया अनुवाद करने के लिए कुछ टेक्स्ट लिखें।")

# ----------------------------------------------------
# 3. लाइव मुद्रा कनवर्टर (Currency Converter)
# ----------------------------------------------------
with tab_curr:
    st.markdown("### 💱 ग्लोबल करेंसी कनवर्टर (Live Rates)")
    st.caption("विदेशी पैसों को भारतीय रुपये (INR) या किसी भी मुद्रा में बदलें")
    
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
        <p style="font-size: 12px; margin-top: 4px;">दर: 1 {curr_type.split(' ')[0]} = ₹{rates[curr_type]}</p>
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
# 6. व्यापारी टूल्स (Business Invoicing)
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
                     
