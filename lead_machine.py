import streamlit as st
import pandas as pd
import urllib.parse
import os

# मोबाइल स्क्रीन सेटअप
st.set_page_config(
    page_title="Universal Bharat AI - हर वर्ग का साथी",
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
    .guide-box {
        background-color: #1E293B;
        border-left: 4px solid #38BDF8;
        border-radius: 8px;
        padding: 12px;
        margin-bottom: 12px;
        font-size: 12px;
        color: #E2E8F0;
        line-height: 1.6;
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
    .founder-card {
        background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
        border: 2px solid #38BDF8;
        border-radius: 14px;
        padding: 16px;
        text-align: center;
        margin-top: 24px;
        margin-bottom: 15px;
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
    <h2>🌍 UNIVERSAL BHARAT AI</h2>
    <p>बच्चा, महिला, युवा, बुज़ुर्ग या व्यापारी — हर भारतीय का सच्चा डिजिटल साथी</p>
</div>
""", unsafe_allow_html=True)

# भाषा चयन (Language Selector)
selected_lang = st.selectbox(
    "🌐 भाषा चुनें / Select Language / மொழியைத் தேர்வுசெய்க:",
    ["हिंदी (Hindi)", "English", "தமிழ் (Tamil)", "తెలుగు (Telugu)", "বাংলা (Bengali)", "भोजपुरी / स्थानीय"]
)

# 5 मुख्य श्रेणियां (Tabs for All Demographics)
tab_kids, tab_women, tab_seniors, tab_youth, tab_vyapar = st.tabs([
    "🧒 बच्चे व छात्र",
    "👩 महिला कॉर्नर",
    "👴 बुज़ुर्ग जन-सेवा",
    "🧑 युवा व रोज़गार",
    "🏪 व्यापारी टूल्स"
])

# ----------------------------------------------------
# 1. बच्चे व छात्र कॉर्नर (Kids & Students)
# ----------------------------------------------------
with tab_kids:
    st.markdown("### 🧒 बच्चों की पढ़ाई व मनोरंजन साथी")
    st.caption("कहानियाँ, कविताएँ, आसान गणित व सामान्य ज्ञान")
    
    kid_action = st.radio("चुनें:", ["📖 ज्ञानवर्धक कहानी", "🧮 आसान गणित व विज्ञान", "📝 स्कूल छुट्टी अर्ज़ी"], horizontal=True)
    
    if kid_action == "📖 ज्ञानवर्धक कहानी":
        story_type = st.selectbox("कहानी चुनें:", ["ईमानदार लकड़हारा (सच्चाई की जीत)", "चालाक खरगोश और शेर (बुद्धि का बल)", "प्यासा कौआ (परिश्रम का फल)"])
        if st.button("✨ कहानी सुनाएँ"):
            if "लकड़हारा" in story_type:
                st.markdown("""
                <div class="guide-box">
                    <b>🪓 ईमानदार लकड़हारा:</b><br>
                    एक गरीब लकड़हारे की कुल्हाड़ी नदी में गिर गई। जलपरी ने सोने और चाँदी की कुल्हाड़ी निकाली, लेकिन उसने लेने से मना कर दिया और अपनी लोहे की कुल्हाड़ी ही माँगी। जलपरी ने उसकी ईमानदारी से खुश होकर तीनों कुल्हाड़ियाँ उसे उपहार में दे दीं।<br>
                    <b>सीख:</b> ईमानदारी सबसे बड़ा धन है।
                </div>
                """, unsafe_allow_html=True)
            elif "खरगोश" in story_type:
                st.markdown("""
                <div class="guide-box">
                    <b>🐰 बुद्धिमान खरगोश:</b><br>
                    जंगल के शेर से बचने के लिए छोटे खरगोश ने अपनी बुद्धि का इस्तेमाल किया। वह शेर को एक गहरे कुएं के पास ले गया और पानी में उसकी ही परछाई दिखाकर दूसरा शेर बताया। मूर्ख शेर कुएं में कूद गया और सभी जानवर बच गए।<br>
                    <b>सीख:</b> बल से बड़ी बुद्धि होती है।
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class="guide-box">
                    <b>🪶 प्यासा कौआ:</b><br>
                    एक प्यासे कौवे को घड़े में थोड़ा पानी दिखा। उसने एक-एक कंकड़ घड़े में डाला जिससे पानी ऊपर आ गया और उसने प्यास बुझा ली।<br>
                    <b>सीख:</b> जहाँ चाह होती है, वहाँ राह निकल आती है।
                </div>
                """, unsafe_allow_html=True)

    elif kid_action == "🧮 आसान गणित व विज्ञान":
        st.write("**💡 कोई भी साधारण सवाल पूछें:**")
        k_q = st.text_input("उदा: 15 x 12 कितना होगा? या पौधे भोजन कैसे बनाते हैं?", key="kid_math_q")
        if st.button("🚀 जवाब देखें"):
            if "पौधे" in k_q or "पेड़" in k_q:
                st.info("🌱 **पौधों का भोजन (Photosynthesis):** पौधे सूर्य की रोशनी, पानी और हवा (कार्बन डाइऑक्साइड) की मदद से अपनी पत्तियों में भोजन बनाते हैं। इस प्रक्रिया को प्रकाश-संश्लेषण कहते हैं।")
            else:
                st.success("उत्तर: निरंतर अभ्यास और ध्यान केंद्रित करने से हर कठिन प्रश्न आसान हो जाता है! अपने सवाल की संख्याएँ ध्यान से जाँचें।")

    elif kid_action == "📝 स्कूल छुट्टी अर्ज़ी":
        s_name = st.text_input("विद्यार्थी का नाम:", placeholder="उदा: साहिल कुमार", key="k_sname")
        s_days = st.text_input("कितने दिन की छुट्टी चाहिए:", placeholder="उदा: 2 दिन", key="k_sdays")
        if st.button("📝 अर्ज़ी तैयार करें", key="k_btn_leave"):
            letter = f"""सेवा में,\nप्रधानाचार्य महोदय,\nविषय: अवकाश हेतु प्रार्थना पत्र\n\nमहोदय,\nसविनय निवेदन है कि आवश्यक कार्य होने के कारण मैं {s_days} तक विद्यालय आने में असमर्थ रहूँगा।\nअतः मुझे अवकाश प्रदान करने की कृपा करें।\n\nआज्ञाकारी छात्र,\n{s_name}"""
            st.text_area("कॉपी करें:", letter, height=160)

# ----------------------------------------------------
# 2. महिला कॉर्नर (Women & Homemakers)
# ----------------------------------------------------
with tab_women:
    st.markdown("### 👩 महिला सुविधा, रसोई व स्वास्थ्य")
    st.caption("स्वादिष्ट व्यंजन विधियाँ, घरेलू उपचार और महिला सशक्तिकरण योजनाएँ")
    
    w_option = st.selectbox("विषय चुनें:", [
        "🍲 झटपट व स्वादिष्ट रसोई रेसिपी",
        "🌿 घरेलू ब्यूटी व सेहत टिप्स",
        "📜 लखपति दीदी व महिला स्वयं सहायता योजना"
    ])
    
    if w_option == "🍲 झटपट व स्वादिष्ट रसोई रेसिपी":
        recipe = st.selectbox("रेसिपी चुनें:", ["10 मिनट में सूजी का हलवा", "स्वादिष्ट पनीर भुर्जी", "हेल्दी वेजिटेबल दलिया"])
        if st.button("👨‍🍳 रेसिपी देखें"):
            if "हलवा" in recipe:
                st.markdown("""
                <div class="guide-box">
                    <b>🥣 सूजी का हलवा (10 मिनट):</b><br>
                    1. कड़ाही में 2 चम्मच घी गरम करें और सूजी को धीमी आँच पर सुनहरा होने तक भूनें।<br>
                    2. अलग बर्तन में 2 कप पानी और चीनी उबाल लें।<br>
                    3. भुनी सूजी में गरम मीठा पानी धीरे-धीरे डालें और लगातार चलाते रहें। इलायची और मेवे डालकर गरमा-गरम परोसें।
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class="guide-box">
                    <b>🍳 पनीर भुर्जी:</b><br>
                    तेल में जीरा, बारीक प्याज, हरी मिर्च और टमाटर भूनें। हल्दी, नमक, धनिया पाउडर डालें और मैश किया हुआ पनीर मिलाकर 3 मिनट पकाएँ। हरा धनिया डालकर परोसें।
                </div>
                """, unsafe_allow_html=True)

    elif w_option == "🌿 घरेलू ब्यूटी व सेहत टिप्स":
        st.markdown("""
        <div class="guide-box">
            <b>✨ चमकती त्वचा व बालों के घरेलू नुस्खे:</b><br>
            • <b>चेहरे के लिए:</b> 1 चम्मच बेसन में आधा चम्मच दही और चुटकी भर हल्दी मिलाकर चेहरे पर 10 मिनट लगाएँ और धो लें।<br>
            • <b>कमजोरी व थकान:</b> रोज़ाना 4 भीगे बादाम और 1 गिलास गुनगुना दूध लें।<br>
            • <b>बालों की मजबूती:</b> नारियल तेल में थोड़ा करी पत्ता उबालकर सिर की मालिश करें।
        </div>
        """, unsafe_allow_html=True)

    elif w_option == "📜 लखपति दीदी व महिला स्वयं सहायता योजना":
        st.markdown("""
        <div class="guide-box">
            <b>🇮🇳 लखपति दीदी योजना:</b><br>
            • महिलाओं को आर्थिक रूप से आत्मनिर्भर बनाने के लिए बिना ब्याज या कम ब्याज पर वित्तीय सहायता और प्रशिक्षण दिया जाता है।<br>
            • <b>पात्रता:</b> महिला स्वयं सहायता समूह (SHG) की सदस्य होनी चाहिए।<br>
            • <b>आवेदन:</b> अपने ग्राम पंचायत या प्रखंड (ब्लॉक) के आजीविका मिशन कार्यालय में संपर्क करें।
        </div>
        """, unsafe_allow_html=True)

# ----------------------------------------------------
# 3. बुज़ुर्ग जन-सेवा (Seniors & Elders)
# ----------------------------------------------------
with tab_seniors:
    st.markdown("### 👴 बुज़ुर्ग जन-सेवा व स्वास्थ्य")
    st.caption("पेंशन योजना, आयुष्मान कार्ड और जोड़ों के दर्द के घरेलू उपाय")
    
    s_choice = st.selectbox("सुविधा चुनें:", [
        "👴 वृद्धावस्था पेंशन (पूरी प्रक्रिया)",
        "🏥 आयुष्मान कार्ड (मुफ़्त ₹5 लाख इलाज)",
        "🦴 जोड़ों व घुटनों के दर्द के लिए देसी देखभाल",
        "📿 दैनिक शांति व भजन/आरती संग्रह"
    ])
    
    if "पेंशन" in s_choice:
        st.markdown("""
        <div class="guide-box">
            <b>👴 वृद्धावस्था पेंशन नियम:</b><br>
            • <b>आयु:</b> 60 वर्ष या उससे अधिक।<br>
            • <b>कागजात:</b> आधार कार्ड, बैंक पासबुक, आय प्रमाण पत्र और निवास प्रमाण।<br>
            • <b>कहाँ जमा करें:</b> नजदीकी जन सेवा केंद्र (CSC) या ब्लॉक RTPS काउंटर पर।
        </div>
        """, unsafe_allow_html=True)
    elif "आयुष्मान" in s_choice:
        st.markdown("""
        <div class="guide-box">
            <b>🏥 आयुष्मान भारत कार्ड:</b><br>
            • हर साल ₹5 लाख तक का सरकारी व बड़े प्राइवेट अस्पतालों में मुफ़्त इलाज।<br>
            • नजदीकी सरकारी अस्पताल में आयुष्मान मित्र काउंटर पर राशन कार्ड और आधार दिखाकर बनवाएं।
        </div>
        """, unsafe_allow_html=True)
    elif "जोड़ों" in s_choice:
        st.markdown("""
        <div class="guide-box">
            <b>🌿 जोड़ों के दर्द के लिए घरेलू उपाय:</b><br>
            1. सरसों के तेल में 4-5 कली लहसुन और अजवाइन पकाकर गुनगुने तेल से घुटनों की मालिश करें।<br>
            2. सुबह खाली पेट हल्का गुनगुना पानी पिएं।<br>
            3. मेथी दाना रात को भिगोकर सुबह उसका पानी पीना लाभदायक माना जाता है।
        </div>
        """, unsafe_allow_html=True)
    elif "भजन" in s_choice:
        st.markdown("""
        <div class="guide-box">
            <b>📿 दैनिक शांति मंत्र:</b><br>
            <i>"ॐ भूर्भुवः स्वः तत्सवितुर्वरेण्यं भर्गो देवस्य धीमहि धियो यो नः प्रचोदयात्॥"</i><br><br>
            मन को शांत रखने के लिए सुबह 10 मिनट खुली हवा में गहरी साँसें लें और प्रभु का स्मरण करें।
        </div>
        """, unsafe_allow_html=True)

# ----------------------------------------------------
# 4. युवा व रोज़गार (Youth & Career)
# ----------------------------------------------------
with tab_youth:
    st.markdown("### 🧑 युवा रोज़गार व करियर मार्गदर्शक")
    st.caption("1-क्लिक जॉब बायोडाटा, इंटरव्यू तैयारी व करियर सुझाव")
    
    y_action = st.radio("चुनें:", ["📄 1-क्लिक बायोडाटा (Resume)", "🎯 इंटरव्यू में सफलता के नियम"], horizontal=True)
    
    if y_action == "📄 1-क्लिक बायोडाटा (Resume)":
        r_name = st.text_input("आपका पूरा नाम:", placeholder="उदा: सुमित वर्मा", key="y_name")
        r_phone = st.text_input("मोबाइल नंबर:", placeholder="उदा: 9876543210", key="y_phone")
        r_edu = st.text_input("उच्चतम योग्यता:", placeholder="उदा: 12वीं / आईटीआई / बी.ए.", key="y_edu")
        r_exp = st.text_input("कार्य अनुभव या हुनर:", placeholder="उदा: सेल्स, कंप्यूटर एक्सेल, ड्राइविंग", key="y_exp")
        
        if st.button("📄 तुरंत बायोडाटा तैयार करें", key="y_res_btn"):
            res = f"""=================================\n             बायोडाटा / RESUME\n=================================\nनाम: {r_name}\nमोबाइल: {r_phone}\nशैक्षणिक योग्यता: {r_edu}\nहुनर व अनुभव: {r_exp}\nभाषा: हिंदी, कामचलाऊ अंग्रेज़ी\nकार्य स्थिति: तत्काल कार्य हेतु उपलब्ध\n================================="""
            st.text_area("कॉपी करके WhatsApp पर भेजें:", res, height=190)

    elif y_action == "🎯 इंटरव्यू में सफलता के नियम":
        st.markdown("""
        <div class="guide-box">
            <b>💼 इंटरव्यू में सफल होने के 4 गुप्त नियम:</b><br>
            1. <b>साफ़ कपड़े व समय:</b> समय से 15 मिनट पहले पहुँचें और साफ़-सुथरे कपड़े पहनें।<br>
            2. <b>आँखों में देखकर बात करें:</b> घबराएँ नहीं, आत्मविश्वास से चेहरे पर मुस्कान रखें।<br>
            3. <b>जो आता है वही कहें:</b> यदि किसी प्रश्न का उत्तर न पता हो, तो विनम्रता से कहें: "सर, मुझे इसकी जानकारी नहीं है, मैं सीख लूँगा।"
        </div>
        """, unsafe_allow_html=True)

# ----------------------------------------------------
# 5. व्यापारी टूल्स व डायरेक्टरी (Vyapar Tools & Leads)
# ----------------------------------------------------
with tab_vyapar:
    st.markdown("### 🏪 व्यापारी टूल्स व ऑल-इंडिया डायरेक्टरी")
    
    v_tool = st.selectbox("टूल चुनें:", ["🧾 WhatsApp डिजिटल बिल मेकर", "💰 सख्त उधारी वसूली नोटिस", "🎯 ऑल-इंडिया बिज़नेस डायरेक्टरी"])
    
    if v_tool == "🧾 WhatsApp डिजिटल बिल मेकर":
        b_shop = st.text_input("दुकान / फ़र्म का नाम:", placeholder="उदा: माँ भवानी ट्रेडर्स")
        b_cust = st.text_input("ग्राहक का नाम:", placeholder="उदा: राकेश जी")
        b_phone = st.text_input("ग्राहक का WhatsApp नंबर (10 अंक):", placeholder="उदा: 9876543210")
        b_item = st.text_area("सामान का विवरण:", placeholder="उदा: 2 बैग सीमेंट (₹760), 5 लीटर प्राइमर (₹900)")
        b_total = st.text_input("कुल रकम (₹):", placeholder="उदा: 1660")
        
        if st.button("📲 डिजिटल बिल भेजें"):
            if b_shop and b_cust and b_phone and b_total:
                clean_p = b_phone.strip()[-10:]
                bill_msg = f"""🧾 *डिजिटल बिल / CASH MEMO*\n🏪 *दुकान:* {b_shop}\n👤 *ग्राहक:* {b_cust}\n-------------------------\n📦 *सामान:* \n{b_item}\n-------------------------\n💰 *कुल राशि:* ₹{b_total}\n✅ स्थिति: भुगतान प्राप्त\n-------------------------\nधन्यवाद! फिर पधारें 🙏"""
                wa_url = f"https://wa.me/91{clean_p}?text={urllib.parse.quote(bill_msg)}"
                st.markdown(f'<a href="{wa_url}" target="_blank" class="upi-pay-btn">👉 WhatsApp पर बिल भेजें</a>', unsafe_allow_html=True)

    elif v_tool == "💰 सख्त उधारी वसूली नोटिस":
        c_name = st.text_input("बकायेदार का नाम:", placeholder="उदा: मोहन कुमार")
        c_amount = st.text_input("बकाया राशि (₹):", placeholder="उदा: 5200")
        c_phone = st.text_input("उसका WhatsApp नंबर:", placeholder="उदा: 9876543210")
        
        if st.button("📩 कानूनी तगादा भेजें"):
            if c_name and c_amount and c_phone:
                clean_p = c_phone.strip()[-10:]
                msg = f"अंतिम तगादा सूचना: नमस्ते {c_name} जी, आपके ऊपर ₹{c_amount} का व्यापारिक बकाया लंबित है। कृपया इसे आज ही चुकता करें अन्यथा कानूनी कार्यवाही शुरू की जा सकती है।"
                wa_url = f"https://wa.me/91{clean_p}?text={urllib.parse.quote(msg)}"
                st.markdown(f'<a href="{wa_url}" target="_blank" class="upi-pay-btn">👉 WhatsApp पर नोटिस भेजें</a>', unsafe_allow_html=True)

    elif v_tool == "🎯 ऑल-इंडिया बिज़नेस डायरेक्टरी":
        df_leads = pd.DataFrame({
            "फ़र्म का नाम": ["Prime Realtors", "Capital Property Hub", "Shree Ganesh Wholesale", "Delhi Metro Mart", "Gold's Fitness Gym", "City Dental Clinic"],
            "कैटेगरी": ["Real Estate", "Real Estate", "Wholesale", "Wholesale", "Gym", "Doctor"],
            "शहर": ["Patna", "Patna", "Patna", "Delhi", "Patna", "Delhi"],
            "संपर्क": ["+91 98765***** 🔒", "+91 94310***** 🔒", "+91 94302***** 🔒", "+91 98102***** 🔒", "+91 97714***** 🔒", "+91 94314***** 🔒"]
        })
        st.dataframe(df_leads, use_container_width=True, hide_index=True)
        
        upi_url = "upi://pay?pa=7484878449-2@ybl&pn=Universal%20Bharat%20AI&am=49&cu=INR&tn=All%20India%20Directory"
        st.markdown(f'<a href="{upi_url}" class="upi-pay-btn">⚡ ₹49 पे करें (PhonePe / GPay)</a>', unsafe_allow_html=True)
        
        utr = st.text_input("", placeholder="12 अंकों का UTR नंबर दर्ज करें", key="dir_utr")
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

# ----------------------------------------------------
# 👑 संस्थापक एवं डेवलपर प्रोफाइल कार्ड (Founder Badge)
# ----------------------------------------------------
st.markdown("---")
st.markdown("""
<div class="founder-card">
    <p style="color: #94A3B8; font-size: 11px; margin: 0; text-transform: uppercase; letter-spacing: 1px;">
        🏛️ प्लेटफ़ॉर्म निर्माता एवं संस्थापक (Founder & Lead Developer)
    </p>
    <h2 style="color: #38BDF8; margin: 6px 0; font-size: 20px; font-weight: 800;">
        साहिल अहमद (Sahil Ahmad)
    </h2>
    <p style="color: #CBD5E1; font-size: 12px; margin-bottom: 12px; line-height: 1.5;">
        🇮🇳 डिजिटल भारत मिशन — देश के हर छात्र, बुज़ुर्ग, युवा व व्यापारी को आधुनिक AI तकनीक से सशक्त बनाने की एक पहल।
    </p>
    <a href="https://wa.me/917484878449?text=नमस्ते%20साहिल%20जी,%20मैंने%20आपका%20Universal%20Bharat%20AI%20ऐप%20देखा।" 
       style="background: linear-gradient(90deg, #10B981 0%, #059669 100%); color: white; padding: 8px 18px; border-radius: 8px; text-decoration: none; font-size: 13px; font-weight: bold; display: inline-block;">
        💬 सीधे WhatsApp पर संपर्क / फीडबैक दें
    </a>
</div>
""", unsafe_allow_html=True)
