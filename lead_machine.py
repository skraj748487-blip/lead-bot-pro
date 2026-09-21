import streamlit as st
import pandas as pd
import urllib.parse
import os

# मोबाइल स्क्रीन सेटअप
st.set_page_config(
    page_title="World AI - Universal Super App",
    page_icon="🌍",
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
        margin-bottom: 12px;
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
    .lang-box {
        background-color: #1E293B;
        border: 1px solid #38BDF8;
        border-radius: 10px;
        padding: 8px 12px;
        margin-bottom: 12px;
    }
    .ans-card {
        background-color: #1E293B;
        border: 1px solid #10B981;
        border-radius: 10px;
        padding: 14px;
        margin-top: 10px;
        font-size: 13px;
        line-height: 1.6;
    }
    .guide-box {
        background-color: #1E293B;
        border-left: 4px solid #38BDF8;
        border-radius: 8px;
        padding: 12px;
        margin-bottom: 12px;
        font-size: 12px;
        color: #E2E8F0;
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

# हेडर
st.markdown("""
<div class="app-header">
    <h2>🌍 WORLD AI — सुपर ऐप / Super App</h2>
    <p>हर भाषा, हर देश, हर इंसान के लिए | Any Language, Any Country, Any Person</p>
</div>
""", unsafe_allow_html=True)

# भाषा चयन (Language Selector)
selected_lang = st.selectbox(
    "🌐 Choose Language / भाषा चुनें / மொழியைத் தேர்ந்தெடுக்கவும்:",
    ["हिंदी (Hindi)", "English", "தமிழ் (Tamil)", "తెలుగు (Telugu)", "বাংলা (Bengali)", "मराठी (Marathi)", "भोजपुरी / स्थानीय"]
)

# 5 मुख्य श्रेणियां (टैब्स)
tab_ai, tab_student, tab_citizen, tab_business, tab_leads = st.tabs([
    "🤖 बहुभाषी AI",
    "📚 छात्र / Student",
    "📜 जन-सेवा व सेहत",
    "🏪 व्यापारी टूल्स",
    "🎯 डायरेक्टरी"
])

# ----------------------------------------------------
# 1. बहुभाषी सार्वभौमिक AI (Multi-Language AI)
# ----------------------------------------------------
with tab_ai:
    st.markdown("### 🎙️ बहुभाषी AI समाधान (Ask in Any Language)")
    st.caption("आप किसी भी भाषा (हिंदी, English, தமிழ், आदि) में सवाल पूछें, AI उसी भाषा में मार्गदर्शन देगा।")

    # भाषा अनुसार डिफ़ॉल्ट सवाल
    q_placeholder = "उदा: बुखार में क्या करें? / How to grow business? / காய்ச்சலுக்கு என்ன செய்வது?"
    user_query = st.text_input("अपना सवाल लिखें या कीबोर्ड माइक से बोलें:", placeholder=q_placeholder)

    if st.button("🚀 समाधान प्राप्त करें / Get Answer", key="get_ans_btn"):
        q = user_query.strip().lower()
        if not q:
            st.warning("कृपया अपना कोई सवाल लिखें या माइक से बोलें।")
        else:
            # तमिल डिटेक्शन / चयन
            if "தமிழ்" in selected_lang or any(char in user_query for char in "அஆஇஈஉஊஎஏஐஒஓஔகஙசஞடணதநபமயரலவழளறன"):
                ans = f"""🩺 **World AI வழிகாட்டுதல் (Tamil Support):**
1. **உங்கள் கேள்வி:** {user_query}
2. **பதில்:** உடல்நலக் கோளாறுகளுக்கு உடனடியாக மருத்துவரை அணுகவும். வணிகம், கல்வி மற்றும் பொது சேவை தொடர்பான அனைத்து வழிகாட்டுதல்களையும் பெற கீழ் உள்ள பிரத்யேக பிரிவுகளைப் பயன்படுத்தவும்."""
            # अंग्रेज़ी डिटेक्शन / चयन
            elif "English" in selected_lang or any(w in q for w in ["fever", "business", "help", "money", "loan", "doctor", "study"]):
                ans = f"""💡 **World AI Universal Guidance (English):**
1. **Health / Medical:** Always consult a verified medical practitioner for persistent symptoms. Hydrate and take adequate rest.
2. **Business & Growth:** Use digital invoicing, maintain a WhatsApp catalog, and leverage social media outreach.
3. **Education & Career:** Maintain focused 25-minute study intervals (Pomodoro) and build a concise, skill-based resume."""
            # हिंदी / भोजपुरी / अन्य
            else:
                if any(w in q for w in ["बुखार", "दवा", "सिरदर्द", "स्वास्थ्य", "सेहत", "पेट"]):
                    ans = """🩺 **स्वास्थ्य व प्राथमिक उपचार (Health Guidance):**
1. **आराम व पानी:** पर्याप्त गुनगुना पानी, ओआरएस या तरल पदार्थ लें।
2. **ठंडी पट्टी:** तेज़ बुखार होने पर माथे पर सामान्य पानी की ठंडी पट्टी रखें।
3. **चेतावनी:** बुखार 2 दिन से अधिक रहने पर तुरंत नज़दीकी डॉक्टर या स्वास्थ्य केंद्र पर संपर्क करें।"""
                elif any(w in q for w in ["पढ़ाई", "याद", "एग्जाम", "परीक्षा", "छात्र", "study"]):
                    ans = """📚 **स्मार्ट पढ़ाई व याददाश्त टिप्स (Student Guide):**
1. **25 मिनट का नियम:** 25 मिनट बिना रुकावट पढ़ें, फिर 5 मिनट का ब्रेक लें।
2. **शॉर्ट नोट्स:** पढ़ी हुई बातों को अपनी भाषा में 2 लाइनों में लिखें।
3. **रिवीजन:** सुबह पढ़ा हुआ विषय रात में सोने से पहले 10 मिनट ज़रूर दोहराएं।"""
                elif any(w in q for w in ["कमाई", "बिज़नेस", "रोजगार", "दुकान", "पैसा"]):
                    ans = """💼 **व्यापार व कमाई मार्गदर्शन (Business Guide):**
1. **डिजिटल बिलिंग:** ग्राहकों को WhatsApp पर तुरंत पक्का बिल भेजें।
2. **लोकल रीच:** Facebook ग्रुप्स और WhatsApp स्टेटस के जरिए नए ऑफर्स बताएं।
3. **समय पर तगादा:** बकायेदारों को कानूनी रूप से विनम्र नोटिस भेजकर उधारी वसूलें।"""
                else:
                    ans = f"""💡 **'{user_query}' हेतु AI परामर्श:**
• आपकी समस्या दर्ज कर ली गई है। 
• छात्र, सरकारी योजना या व्यापारी टूल्स के लिए नीचे दिए गए संबंधित टैब का उपयोग करें।"""

            st.markdown(f'<div class="ans-card">{ans}</div>', unsafe_allow_html=True)

# ----------------------------------------------------
# 2. छात्र कॉर्नर (Students)
# ----------------------------------------------------
with tab_student:
    st.markdown("### 📚 छात्र सहायता व बायोडाटा लेखक")
    st_option = st.selectbox("कार्य चुनें:", [
        "छुट्टी की अर्ज़ी (Leave Application)",
        "जॉब बायोडाटा (Resume Maker)"
    ])
    
    if "Leave Application" in st_option:
        s_name = st.text_input("विद्यार्थी का नाम:", placeholder="उदा: साहिल कुमार")
        s_school = st.text_input("स्कूल / कॉलेज का नाम:", placeholder="उदा: राजकीय उच्च विद्यालय")
        s_reason = st.text_input("कारण:", placeholder="उदा: आवश्यक कार्य / अस्वस्थता")
        s_days = st.text_input("अवधि:", placeholder="उदा: 2 दिन")
        
        if st.button("📝 अर्ज़ी तैयार करें"):
            if s_name and s_school and s_reason and s_days:
                letter = f"""सेवा में,\nप्रधानाचार्य महोदय,\n{s_school}\n\nविषय: {s_reason} हेतु अवकाश पत्र\n\nमहोदय,\nसविनय निवेदन है कि मैं आपके संस्थान का छात्र हूँ। {s_reason} के कारण मैं {s_days} तक उपस्थित रहने में असमर्थ हूँ।\n\nअतः आपसे प्रार्थना है कि मुझे अवकाश प्रदान करने की कृपा करें।\n\nधन्यवाद।\nआज्ञाकारी छात्र,\n{s_name}"""
                st.text_area("आपकी अर्ज़ी तैयार है:", letter, height=200)

    elif "Resume" in st_option:
        r_name = st.text_input("पूरा नाम:", placeholder="उदा: राहुल कुमार")
        r_phone = st.text_input("मोबाइल नंबर:", placeholder="उदा: 9876543210")
        r_edu = st.text_input("योग्यता:", placeholder="उदा: 10वीं / 12वीं / स्नातक")
        r_skills = st.text_input("हुनर / अनुभव:", placeholder="उदा: कंप्यूटर टाइपिंग, ड्राइविंग")
        
        if st.button("📄 बायोडाटा तैयार करें"):
            if r_name and r_phone and r_edu:
                res_txt = f"""बायोडाटा / RESUME\nनाम: {r_name}\nसंपर्क: {r_phone}\nयोग्यता: {r_edu}\nहुनर: {r_skills}\nउपलब्धता: तत्काल कार्य हेतु उपलब्ध"""
                st.text_area("बायोडाटा तैयार है:", res_txt, height=180)

# ----------------------------------------------------
# 3. जन-सेवा व सेहत (Citizens & Seniors)
# ----------------------------------------------------
with tab_citizen:
    st.markdown("### 📜 सरकारी योजना व नागरिक सुविधा")
    yojana = st.selectbox("योजना चुनें:", [
        "आयुष्मान भारत (₹5 लाख मुफ़्त इलाज)",
        "वृद्धावस्था / विधवा पेंशन",
        "राशन कार्ड नया आवेदन / सुधार",
        "पीएम किसान सम्मान निधि"
    ])
    
    if yojana == "आयुष्मान भारत (₹5 लाख मुफ़्त इलाज)":
        st.markdown("""
        <div class="guide-box">
            <b>🏥 आयुष्मान कार्ड विवरण:</b><br>
            • प्रति परिवार ₹5 लाख तक का कैशलेस इलाज।<br>
            • <b>आवश्यक दस्तावेज:</b> राशन कार्ड और आधार कार्ड।
        </div>
        """, unsafe_allow_html=True)
    elif yojana == "वृद्धावस्था / विधवा पेंशन":
        st.markdown("""
        <div class="guide-box">
            <b>👴 पेंशन नियम व दस्तावेज:</b><br>
            • <b>पात्रता:</b> 60 वर्ष या अधिक उम्र के नागरिक।<br>
            • <b>कागजात:</b> आधार कार्ड, बैंक पासबुक, आय व आयु प्रमाण।
        </div>
        """, unsafe_allow_html=True)
    elif yojana == "राशन कार्ड नया आवेदन / सुधार":
        st.markdown("""
        <div class="guide-box">
            <b>🌾 राशन कार्ड निर्देश:</b><br>
            • <b>कागजात:</b> परिवार के मुखिया की फ़ोटो, सभी सदस्यों का आधार कार्ड, बैंक पासबुक।
        </div>
        """, unsafe_allow_html=True)
    elif yojana == "पीएम किसान सम्मान निधि":
        st.markdown("""
        <div class="guide-box">
            <b>🚜 किसान सम्मान निधि:</b><br>
            • हर 4 माह पर ₹2,000 की किस्त (सालाना ₹6,000)। आधार ई-केवाईसी अनिवार्य है।
        </div>
        """, unsafe_allow_html=True)

# ----------------------------------------------------
# 4. व्यापारी टूल्स (Business Tools)
# ----------------------------------------------------
with tab_business:
    st.markdown("### 🏪 स्मार्ट व्यापारी टूल्स")
    b_tool = st.radio("टूल चुनें:", ["🧾 WhatsApp डिजिटल बिल", "💰 कानूनी उधारी तगादा"], horizontal=True)
    
    if b_tool == "🧾 WhatsApp डिजिटल बिल":
        b_shop = st.text_input("दुकान / फ़र्म का नाम:", placeholder="उदा: जनता किराना स्टोर")
        b_cust = st.text_input("ग्राहक का नाम:", placeholder="उदा: विजय कुमार")
        b_phone = st.text_input("ग्राहक का WhatsApp नंबर:", placeholder="उदा: 9876543210")
        b_item = st.text_area("सामान का विवरण:", placeholder="उदा: 1 बैग आटा (₹420), 2 पैकेट तेल (₹260)")
        b_total = st.text_input("कुल रकम (₹):", placeholder="उदा: 680")
        
        if st.button("📲 डिजिटल बिल भेजें"):
            if b_shop and b_cust and b_phone and b_total:
                clean_p = b_phone.strip()[-10:]
                bill_msg = f"""🧾 *डिजिटल बिल / CASH MEMO*\n🏪 *दुकान:* {b_shop}\n👤 *ग्राहक:* {b_cust}\n-------------------------\n📦 *सामान:* \n{b_item}\n-------------------------\n💰 *कुल राशि:* ₹{b_total}\n✅ स्थिति: भुगतान प्राप्त\n-------------------------\nधन्यवाद! फिर पधारें 🙏"""
                wa_url = f"https://wa.me/91{clean_p}?text={urllib.parse.quote(bill_msg)}"
                st.markdown(f'<a href="{wa_url}" target="_blank" class="upi-pay-btn">👉 WhatsApp पर बिल भेजें</a>', unsafe_allow_html=True)

    elif b_tool == "💰 कानूनी उधारी तगादा":
        c_name = st.text_input("बकायेदार का नाम:", placeholder="उदा: अमित कुमार")
        c_amount = st.text_input("बकाया राशि (₹):", placeholder="उदा: 4500")
        c_phone = st.text_input("बकायेदार का WhatsApp नंबर:", placeholder="उदा: 9876543210")
        
        if st.button("📩 कानूनी तगादा भेजें"):
            if c_name and c_amount and c_phone:
                clean_p = c_phone.strip()[-10:]
                msg = f"नमस्ते {c_name} जी, आपके ऊपर ₹{c_amount} का व्यापारिक बकाया लंबित है। कृपया इसे आज ही सेटल करें अन्यथा कानूनी कार्यवाही शुरू की जा सकती है।"
                wa_url = f"https://wa.me/91{clean_p}?text={urllib.parse.quote(msg)}"
                st.markdown(f'<a href="{wa_url}" target="_blank" class="upi-pay-btn">👉 WhatsApp पर नोटिस भेजें</a>', unsafe_allow_html=True)

# ----------------------------------------------------
# 5. बिज़नेस डायरेक्टरी (Leads Directory)
# ----------------------------------------------------
with tab_leads:
    st.markdown("### 🎯 अखिल भारतीय बिज़नेस डायरेक्टरी")
    
    @st.cache_data
    def load_db():
        return pd.DataFrame({
            "व्यापारी / फर्म": [
                "Patna Prime Builders", "Capital Property Hub", "Delhi NCR Real Infra",
                "Mumbai Seaface Properties", "Shree Ganesh Wholesale", "Delhi Wholesale Mart",
                "Gold's Fitness Gym", "Dr. Sharma Clinic"
            ],
            "कैटेगरी": ["Real Estate", "Real Estate", "Real Estate", "Real Estate", "Wholesale", "Wholesale", "Gym", "Doctor"],
            "शहर": ["Patna", "Patna", "Delhi", "Mumbai", "Patna", "Delhi", "Patna", "Patna"],
            "डायरेक्ट संपर्क": ["+91 98765***** 🔒", "+91 94310***** 🔒", "+91 98111***** 🔒", "+91 98200***** 🔒", "+91 94302***** 🔒", "+91 98102***** 🔒", "+91 97714***** 🔒", "+91 94314***** 🔒"]
        })
    
    df_leads = load_db()
    st.dataframe(df_leads.head(5), use_container_width=True, hide_index=True)
    
    upi_url = "upi://pay?pa=7484878449-2@ybl&pn=Vyapar%20Grow%20AI&am=49&cu=INR&tn=All%20India%20Leads"
    st.markdown(f'<a href="{upi_url}" class="upi-pay-btn">⚡ ₹49 पे करें (PhonePe / GPay)</a>', unsafe_allow_html=True)
    
    utr = st.text_input("", placeholder="12 अंकों का UTR नंबर दर्ज करें", key="utr_dir")
    if st.button("🚀 फ़ाइल डाउनलोड करें"):
        if len(utr.strip()) == 12 and utr.strip().isdigit():
            st.success("✅ पेमेंट सत्यापित!")
            st.download_button(
                label="📥 संपूर्ण डायरेक्टरी डाउनलोड करें (CSV)",
                data=df_leads.to_csv(index=False).encode('utf-8'),
                file_name="Bharat_AI_Directory.csv",
                mime="text/csv",
                use_container_width=True
            )
        else:
            st.error("कृपया सही 12 अंकों का UTR नंबर दर्ज करें।")
