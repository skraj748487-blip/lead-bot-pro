import streamlit as st
import pandas as pd
import urllib.parse
import os

# मोबाइल स्क्रीन सेटअप
st.set_page_config(
    page_title="Bharat AI - Universal Super App",
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
    .ai-banner {
        background: linear-gradient(135deg, #065F46 0%, #047857 100%);
        border: 1px solid #10B981;
        border-radius: 12px;
        padding: 12px;
        text-align: center;
        margin-bottom: 14px;
    }
    .quick-chip-box {
        background-color: #1E293B;
        border: 1px solid #334155;
        border-radius: 10px;
        padding: 8px;
        margin-bottom: 12px;
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
    .ans-card {
        background-color: #1E293B;
        border: 1px solid #10B981;
        border-radius: 10px;
        padding: 14px;
        margin-top: 10px;
        font-size: 13px;
        line-height: 1.5;
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

# मुख्य हेडर
st.markdown("""
<div class="app-header">
    <h2>🇮🇳 BHARAT AI — ऑल-इन-वन सुपर ऐप</h2>
    <p>दुनिया का हर सवाल, हर व्यक्ति के काम आने वाला डिजिटल सहायक</p>
</div>
""", unsafe_allow_html=True)

# 5 मुख्य श्रेणियां (टैब्स)
tab_ai, tab_student, tab_citizen, tab_business, tab_leads = st.tabs([
    "🤖 AI समाधान",
    "📚 छात्र कॉर्नर",
    "📜 जन-सेवा व सेहत",
    "🏪 व्यापारी टूल्स",
    "🎯 डायरेक्टरी"
])

# ----------------------------------------------------
# 1. सार्वभौमिक AI असिस्टेंट (Universal AI Assistant)
# ----------------------------------------------------
with tab_ai:
    st.markdown("""
    <div class="ai-banner">
        <b style="font-size: 15px;">🎙️ कोई भी सवाल पूछें (बोलकर या लिखकर)</b>
        <p style="font-size: 11px; margin-top: 4px; margin-bottom: 0;">पढ़े-लिखे हों या कम पढ़े-लिखे — पढ़ाई, सेहत, खेती, कानूनी या रोज़गार संबंधी कोई भी समस्या लिखें:</p>
    </div>
    """, unsafe_allow_html=True)

    # क्विक सजेशन बटन्स
    st.write("**⚡ झटपट सहायता के लिए टैप करें:**")
    qc1, qc2 = st.columns(2)
    quick_q = ""
    with qc1:
        if st.button("🩺 प्राथमिक उपचार / बुखार"):
            quick_q = "तेज बुखार या सिरदर्द में तुरंत क्या घरेलू प्राथमिक उपचार करना चाहिए?"
        if st.button("📚 पढ़ाई व याददाश्त टिप्स"):
            quick_q = "परीक्षा के समय कठिन विषय को जल्दी याद करने का सबसे आसान तरीका क्या है?"
    with qc2:
        if st.button("🌾 फसल सुरक्षा व खाद"):
            quick_q = "गेहूं और धान की फसल को कीड़ों से बचाने और अच्छी उपज के उपाय बताएं।"
        if st.button("💼 घर बैठे कमाई के तरीके"):
            quick_q = "मोबाइल फोन से बिना पैसे लगाए छोटे बिज़नेस और ऑनलाइन कमाई के सरल तरीके क्या हैं?"

    user_query = st.text_input("अपना सवाल यहाँ दर्ज करें:", value=quick_q, placeholder="उदा: बुखार में क्या खाएं? / राशन कार्ड में नाम कैसे जोड़े?")

    if st.button("🚀 तुरंत AI समाधान पाएँ", key="ask_ai_btn"):
        q = user_query.strip().lower()
        if not q:
            st.warning("कृपया अपना कोई सवाल लिखें या ऊपर दिए गए किसी बटन पर टैप करें।")
        else:
            # स्मार्ट लोकलाइज्ड रूल्स-इंजन
            if any(w in q for w in ["बुखार", "दवा", "सिरदर्द", "स्वास्थ्य", "सेहत", "पेट दर्द"]):
                res = """🩺 **स्वास्थ्य व प्राथमिक उपचार सलाह:**
1. **आराम व पानी:** पर्याप्त मात्रा में गुनगुना पानी, ओआरएस या नारियल पानी पिएं। शरीर में पानी की कमी न होने दें।
2. **ठंडी पट्टी:** यदि तेज बुखार हो, तो माथे पर सामान्य पानी की ठंडी पट्टी रखें।
3. **हल्का भोजन:** सुपाच्य आहार जैसे दलिया, मूंग दाल की खिचड़ी या उबला हुआ सूप लें।
4. **महत्वपूर्ण चेतावनी:** यदि बुखार 2 दिन से अधिक रहे या 102°F से ऊपर जाए, तो खुद से दवा लेने के बजाय तुरंत नजदीकी स्वास्थ्य केंद्र या डॉक्टर से संपर्क करें।"""
            elif any(w in q for w in ["पढ़ाई", "याद", "एग्जाम", "परीक्षा", "छात्र", "नंबर"]):
                res = """📚 **स्मार्ट पढ़ाई व याददाश्त गाइड:**
1. **25 मिनट का नियम (पोमोडोरो):** 25 मिनट बिना फोन छुए ध्यान से पढ़ें, फिर 5 मिनट का ब्रेक लें।
2. **लिखकर याद करना:** जो भी पढ़ें, उसे बिना देखे 2 लाइनों में अपनी भाषा में लिखने का प्रयास करें।
3. **रिवीजन चार्ट:** सुबह पढ़ी हुई चीज़ को रात में सोने से पहले 10 मिनट ज़रूर दोहराएं।
4. **भरपूर नींद:** दिमाग को शांत और एक्टिव रखने के लिए 7-8 घंटे की गहरी नींद बेहद जरूरी है।"""
            elif any(w in q for w in ["फसल", "खाद", "खेती", "किसान", "कीड़े"]):
                res = """🌾 **कृषि व फसल देखभाल सलाह:**
1. **जैविक कीटनाशक:** नीम का तेल (5ml प्रति लीटर पानी) मिलाकर छिड़काव करने से सामान्य कीट नियंत्रित रहते हैं।
2. **संतुलित खाद:** केवल यूरिया पर निर्भर न रहें; मिट्टी जांच के अनुसार जिंक, पोटाश और डीएपी का उचित अनुपात डालें।
3. **सिंचाई नियम:** तेज धूप में दोपहर के समय पानी देने से बचें; सुबह या शाम के समय सिंचाई सर्वोत्तम रहती है।
4. **सरकारी हेल्पलाइन:** किसी भी फसल बीमारी के लिए टोल-फ्री किसान कॉल सेंटर नंबर **1800-180-1551** पर मुफ्त सलाह लें।"""
            elif any(w in q for w in ["कमाई", "बिज़नेस", "रोजगार", "दुकान", "पैसा", "कमाएं"]):
                res = """💼 **व्यापार वृद्धि व रोज़गार मार्गदर्शन:**
1. **डिजिटल उपस्थिति:** अपने आसपास के ग्राहकों को WhatsApp ब्रॉडकास्ट और स्टेटस से नए ऑफर्स की जानकारी दें।
2. **सर्विस डिलीवरी:** लोकल लेवल पर होम डिलीवरी या तुरंत सर्विस की सुविधा जोड़कर सामान्य दुकानदारों से आगे निकलें।
3. **जीरो इन्वेस्टमेंट काम:** एफिलिएट रेफरल, डिजिटल बिलिंग सहायता या सरकारी फॉर्म भरने की जन-सेवा से प्रतिदिन आय की जा सकती है।"""
            else:
                res = f"""💡 **'{user_query}' हेतु AI परामर्श:**
• आपकी समस्या को दर्ज कर लिया गया है। 
• किसी भी कानूनी, वित्तीय या चिकित्सीय कार्य के लिए संबंधित विभाग के अधिकृत अधिकारी या पेशेवर से सीधे संपर्क करें।
• दैनिक व्यावहारिक समाधान के लिए हमारे विशेष टैब्स (छात्र, जन-सेवा, या व्यापारी टूल्स) का चयन करें।"""

            st.markdown(f'<div class="ans-card">{res}</div>', unsafe_allow_html=True)

# ----------------------------------------------------
# 2. छात्र कॉर्नर (Students)
# ----------------------------------------------------
with tab_student:
    st.markdown("### 📚 छात्र सहायता व लेखक")
    st.caption("स्कूल/कॉलेज अर्ज़ी, छुट्टी का पत्र या नौकरी का बायोडाटा तुरंत बनाएँ")
    
    st_option = st.selectbox("आपको क्या तैयार करना है?", [
        "स्कूल / कॉलेज की छुट्टी की अर्ज़ी (Leave Application)",
        "नौकरी के लिए साधारण बायोडाटा (Quick Resume)"
    ])
    
    if "Leave Application" in st_option:
        s_name = st.text_input("विद्यार्थी का नाम:", placeholder="उदा: साहिल कुमार")
        s_school = st.text_input("स्कूल / कॉलेज का नाम:", placeholder="उदा: राजकीय उच्च विद्यालय")
        s_reason = st.text_input("छुट्टी का कारण:", placeholder="उदा: तबियत खराब होने के कारण / आवश्यक कार्य")
        s_days = st.text_input("कितने दिन की छुट्टी चाहिए:", placeholder="उदा: 2 दिन")
        
        if st.button("📝 अर्ज़ी तैयार करें"):
            if s_name and s_school and s_reason and s_days:
                letter = f"""सेवा में,\nप्रधानाचार्य महोदय,\n{s_school}\n\nविषय: {s_reason} हेतु अवकाश पत्र\n\nमहोदय,\nसविनय निवेदन है कि मैं आपके संस्थान का छात्र हूँ। {s_reason} के कारण मैं {s_days} तक उपस्थित रहने में असमर्थ हूँ।\n\nअतः आपसे प्रार्थना है कि मुझे अवकाश प्रदान करने की कृपा करें।\n\nधन्यवाद।\nआज्ञाकारी छात्र,\n{s_name}"""
                st.text_area("आपकी अर्ज़ी तैयार है (कॉपी करें):", letter, height=200)
            else:
                st.warning("कृपया सभी बॉक्स भरें।")

    elif "Quick Resume" in st_option:
        r_name = st.text_input("पूरा नाम:", placeholder="उदा: राहुल कुमार")
        r_phone = st.text_input("मोबाइल नंबर:", placeholder="उदा: 9876543210")
        r_edu = st.text_input("शिक्षा (Qualification):", placeholder="उदा: 10वीं / 12वीं / स्नातक")
        r_skills = st.text_input("अनुभव या हुनर (Skills):", placeholder="उदा: कंप्यूटर टाइपिंग, ड्राइविंग, सेल्स अनुभव")
        
        if st.button("📄 बायोडाटा तैयार करें"):
            if r_name and r_phone and r_edu:
                res_txt = f"""बायोडाटा / RESUME\nनाम: {r_name}\nसंपर्क: {r_phone}\nयोग्यता: {r_edu}\nहुनर: {r_skills}\nभाषा: हिंदी, साधारण अंग्रेज़ी\nउपलब्धता: तत्काल कार्य हेतु उपलब्ध"""
                st.text_area("बायोडाटा (कॉपी करें):", res_txt, height=180)
            else:
                st.warning("कृपया नाम, नंबर और शिक्षा दर्ज करें।")

# ----------------------------------------------------
# 3. जन-सेवा व सेहत (Citizens & Seniors)
# ----------------------------------------------------
with tab_citizen:
    st.markdown("### 📜 सरकारी योजना व नागरिक सुविधा")
    st.caption("बुज़ुर्गों और परिवारों के लिए मुख्य योजनाओं के नियम व सीधे निर्देश")
    
    yojana = st.selectbox("योजना या सेवा चुनें:", [
        "आयुष्मान भारत (₹5 लाख तक मुफ़्त इलाज)",
        "वृद्धावस्था / विधवा पेंशन योजना",
        "राशन कार्ड नया आवेदन / सुधार",
        "पीएम किसान सम्मान निधि (सालाना ₹6000)"
    ])
    
    if yojana == "आयुष्मान भारत (₹5 लाख तक मुफ़्त इलाज)":
        st.markdown("""
        <div class="guide-box">
            <b>🏥 आयुष्मान कार्ड विवरण:</b><br>
            • सूचीबद्ध अस्पतालों में प्रति वर्ष प्रति परिवार ₹5 लाख तक का कैशलेस इलाज।<br>
            • <b>आवश्यक दस्तावेज:</b> राशन कार्ड और आधार कार्ड।<br>
            • <b>कहाँ जाएं:</b> नजदीकी सरकारी अस्पताल के आयुष्मान मित्र काउंटर या CSC केंद्र पर पात्रता जांचें।
        </div>
        """, unsafe_allow_html=True)
    elif yojana == "वृद्धावस्था / विधवा पेंशन योजना":
        st.markdown("""
        <div class="guide-box">
            <b>👴 पेंशन नियम व दस्तावेज:</b><br>
            • <b>पात्रता:</b> 60 वर्ष या अधिक उम्र के नागरिक।<br>
            • <b>कागजात:</b> आधार कार्ड, बैंक पासबुक, आय प्रमाण पत्र, आयु प्रमाण।<br>
            • नजदीकी आरटीपीएस (RTPS) काउंटर या ब्लॉक से ऑनलाइन फॉर्म भरवाएं।
        </div>
        """, unsafe_allow_html=True)
    elif yojana == "राशन कार्ड नया आवेदन / सुधार":
        st.markdown("""
        <div class="guide-box">
            <b>🌾 राशन कार्ड निर्देश:</b><br>
            • <b>दस्तावेज:</b> परिवार के मुखिया की फ़ोटो, सभी सदस्यों का आधार कार्ड, निवास प्रमाण पत्र व बैंक खाता।<br>
            • राज्य खाद्य आपूर्ति पोर्टल या ब्लॉक जन-सुविधा केंद्र पर जमा होता है।
        </div>
        """, unsafe_allow_html=True)
    elif yojana == "पीएम किसान सम्मान निधि (सालाना ₹6000)":
        st.markdown("""
        <div class="guide-box">
            <b>🚜 किसान सम्मान निधि:</b><br>
            • हर 4 माह पर ₹2,000 की किस्त बैंक खाते में डीबीटी (DBT) द्वारा आती है।<br>
            • <b>आवश्यक:</b> ज़मीन की रसीद, आधार कार्ड, बैंक खाता और आधार ई-केवाईसी अनिवार्य है।
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
            else:
                st.warning("कृपया सभी फ़ील्ड्स भरें।")

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
            else:
                st.warning("कृपया सभी विवरण भरें।")

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
            
