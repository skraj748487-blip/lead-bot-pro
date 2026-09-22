import streamlit as st
import streamlit.components.v1 as components
import urllib.parse
import urllib.request
import json
from datetime import datetime

# 1. Page Configuration
st.set_page_config(
    page_title="महा-सेवा AI — राष्ट्रीय नागरिक व विधिक सुरक्षा मिशन",
    page_icon="🇮🇳",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Modern 100% Dark UI - Zero Glitch
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Devanagari:wght@600;700;800&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap');

    .stApp {
        background-color: #030712 !important;
        color: #F8FAFC !important;
        font-family: 'Noto Sans Devanagari', 'Plus Jakarta Sans', sans-serif !important;
    }

    h1, h2, h3, p, span, label, div {
        color: #FFFFFF !important;
        font-weight: 700 !important;
    }

    input, .stTextInput input, textarea, .stTextArea textarea {
        background-color: #0B1329 !important;
        color: #38BDF8 !important;
        font-size: 15px !important;
        font-weight: 700 !important;
        border: 2px solid #0284C7 !important;
        border-radius: 12px !important;
        padding: 12px !important;
    }
    input:focus, textarea:focus {
        border-color: #10B981 !important;
        box-shadow: 0 0 15px rgba(16, 185, 129, 0.4) !important;
    }

    div[data-testid="stRadio"] > div {
        background-color: #0B1329 !important;
        border: 2px solid #0284C7 !important;
        border-radius: 12px !important;
        padding: 10px 14px !important;
    }
    div[data-testid="stRadio"] label {
        color: #F8FAFC !important;
        font-size: 14px !important;
        font-weight: 700 !important;
    }

    .info-card {
        background: #0F172A;
        border: 2px solid #1E293B;
        border-radius: 12px;
        padding: 14px;
        margin-bottom: 12px;
    }
    .caution-card {
        background: rgba(239, 68, 68, 0.12);
        border: 2px solid #EF4444;
        border-radius: 12px;
        padding: 14px;
        margin-top: 12px;
        margin-bottom: 12px;
    }
    .emergency-card {
        background: radial-gradient(circle at center, #991B1B 0%, #450A0A 100%);
        border: 2px solid #F87171;
        border-radius: 14px;
        padding: 16px;
        text-align: center;
        margin-bottom: 16px;
        box-shadow: 0 0 25px rgba(239, 68, 68, 0.4);
    }

    div.stButton > button {
        background: linear-gradient(135deg, #0284C7 0%, #2563EB 100%) !important;
        color: #FFFFFF !important;
        font-weight: 800 !important;
        font-size: 16px !important;
        border-radius: 10px !important;
        width: 100% !important;
        padding: 14px !important;
        border: 1px solid #38BDF8 !important;
        box-shadow: 0 4px 15px rgba(2, 132, 199, 0.4) !important;
        margin-top: 8px;
    }

    .btn-green {
        display: block;
        background: linear-gradient(90deg, #10B981 0%, #059669 100%);
        color: #FFFFFF !important;
        text-align: center;
        font-weight: 800;
        font-size: 15px;
        padding: 12px;
        border-radius: 10px;
        text-decoration: none;
        margin: 8px 0;
        box-shadow: 0 4px 15px rgba(16, 185, 129, 0.4);
    }

    .btn-blue {
        display: block;
        background: linear-gradient(90deg, #0284C7 0%, #0369A1 100%);
        color: #FFFFFF !important;
        text-align: center;
        font-weight: 800;
        font-size: 15px;
        padding: 12px;
        border-radius: 10px;
        text-decoration: none;
        margin: 8px 0;
        box-shadow: 0 4px 15px rgba(2, 132, 199, 0.4);
    }

    .btn-red-call {
        display: inline-block;
        background: #EF4444;
        color: #FFFFFF !important;
        font-weight: 800;
        font-size: 13px;
        padding: 8px 14px;
        border-radius: 10px;
        text-decoration: none;
        margin: 4px;
        box-shadow: 0 4px 15px rgba(239, 68, 68, 0.5);
    }
</style>
""", unsafe_allow_html=True)

MY_WA_NUMBER = "917484878440"
today_str = datetime.now().strftime("%d-%m-%Y")

# Header
st.markdown("""
<div style="background: radial-gradient(circle at center, #1E3A8A 0%, #030712 100%); border: 2px solid #38BDF8; border-radius: 14px; padding: 14px; text-align: center; margin-bottom: 14px; box-shadow: 0 0 20px rgba(56, 189, 248, 0.25);">
    <span style="background:rgba(16,185,129,0.2); color:#10B981; border:1px solid #10B981; padding:3px 12px; border-radius:20px; font-size:11px; font-weight:800;">
        ⚡ 24x7 अखंड भारत नागरिक, विधिक सुरक्षा व जन-अधिकार मिशन
    </span>
    <h1 style="font-size:22px; margin:6px 0 0 0; color:#FFF;">महा-सेवा AI (MAHA SEVA AI)</h1>
    <p style="font-size:12px; color:#38BDF8; margin:4px 0 0 0;">14 महा-विधिक अधिकार • रात की सुरक्षा • रोज़गार • एम्बुलेंस • सरकारी योजना</p>
</div>
""", unsafe_allow_html=True)

nav_choice = st.radio(
    "📂 सेवा श्रेणी चुनें:",
    [
        "⚖️ 14 विधिक अधिकार व शिकायत",
        "🚨 रात की सुरक्षा व पैनिक SOS",
        "🏥 दवा व एम्बुलेंस सहायता",
        "💼 रोज़गार व हेल्पर डेस्क",
        "🏛️ सरकारी योजना व सब्सिडी",
        "🛡️ साइबर फ्रॉड व नशा-मुक्ति"
    ],
    horizontal=True
)

st.markdown("---")

# ================= 14 LEGAL & CITIZEN ACTION ENGINE =================
if nav_choice == "⚖️ 14 विधिक अधिकार व शिकायत":
    st.write("### ⚖️ जन-अधिकार व भ्रष्टाचार विरोधी विधिक मंच")
    st.caption("अपने साथ हुए किसी भी अन्याय को चुनें — सिस्टम तुरंत संबंधित कानून के तहत कड़ा नोटिस तैयार करेगा")

    LEGAL_CASES = {
        "1. ठेकेदार / कंपनी ने मजदूरी या वेतन दबा लिया": {
            "act": "पेमेंट ऑफ वेजेस एक्ट 1936 व इंडस्ट्रियल डिस्प्यूट्स एक्ट",
            "authority": "श्रम आयुक्त (Labour Commissioner) व जिलाधिकारी (DM)",
            "rule": "मजदूरी दबाना गैर-कानूनी है। श्रम विभाग में शिकायत जाते ही कंपनी पर 10 गुना हर्जाना और 18% ब्याज का आदेश होता है।",
            "default_det": "मैंने 2 महीने पूरी ईमानदारी से मजदूरी की, जिसका कुल ₹24,000 बकाया है। माँगने पर गाली-गलौज व धमकी दी जा रही है।"
        },
        "2. पुलिस द्वारा गैर-कानूनी मारपीट, गाली-गलौज या फर्जी चालान": {
            "act": "भारतीय नागरिक सुरक्षा संहिता (BNSS) व सुप्रीम कोर्ट डी.के. बसु गाइडलाइन्स",
            "authority": "पुलिस अधीक्षक (SP), राज्य पुलिस शिकायत प्राधिकरण (SPCA) व NHRC",
            "rule": "पुलिस को बिना जुर्म किसी भी नागरिक को हाथ लगाने या गाली देने का कोई अधिकार नहीं है। ऐसा करने वाले पुलिसकर्मी पर धारा 166A BNS के तहत मुकदमा बनता है।",
            "default_det": "संबंधित पुलिसकर्मी द्वारा बिना किसी अपराध के मेरे साथ सार्वजनिक रूप से अभद्रता, मारपीट व अवैध चालान की धमकी दी गई।"
        },
        "3. अस्पताल द्वारा इमरजेंसी में भर्ती न करना या लाश/मरीज रोकना": {
            "act": "सुप्रीम कोर्ट परमानंद कटारा फैसला व क्लिनिकल एस्टेब्लिशमेंट एक्ट",
            "authority": "मुख्य चिकित्सा अधिकारी (CMO), स्वास्थ्य विभाग व उपभोक्ता आयोग",
            "rule": "कोई भी अस्पताल आपात स्थिति में पहले पैसे माँगकर इलाज से मना नहीं कर सकता। बिल विवाद में लाश या मरीज को बंधक बनाना संज्ञेय अपराध है।",
            "default_det": "इमरजेंसी में अस्पताल द्वारा पहले अग्रिम राशि जमा करने का दबाव बनाकर इलाज में जानबूझकर देरी की गई।"
        },
        "4. फैक्ट्री/कार्यस्थल पर हादसा व हाथ-पैर कटना (व्हीलचेयर)": {
            "act": "Employees' Compensation Act 1923 (कर्मचारी मुआवजा कानून)",
            "authority": "मुआवजा आयुक्त (Compensation Commissioner) व श्रम न्यायालय",
            "rule": "ड्यूटी के दौरान दुर्घटना होने पर मालिक को मजदूर की उम्र और चोट के आधार पर ₹5 लाख से ₹20 लाख का मुआवजा व आजीवन पेंशन देनी अनिवार्य है।",
            "default_det": "कार्यस्थल पर सुरक्षा उपकरणों के अभाव में गंभीर दुर्घटना हुई, जिसके कारण स्थायी दिव्यांगता आई है। मालिक इलाज व मुआवजे से मुकर रहा है।"
        },
        "5. सूदखोरों, साहूकारों या फर्जी लोन एजेंटों द्वारा धमकी व ब्लैकमेल": {
            "act": "RBI रिकवरी गाइडलाइन्स व भारतीय न्याय संहिता (जबरन वसूली धारा 308 BNS)",
            "authority": "साइबर क्राइम सेल, पुलिस अधीक्षक (SP) व RBI लोकपाल",
            "rule": "बिना लाइसेंस सूदखोरी और रात में फोन करना या रिश्तेदार को फोटो भेजना गैर-कानूनी अपराध है। तुरंत गिरफ्तारी का प्रावधान है।",
            "default_det": "अवैध ब्याज वसूलने हेतु साहूकार/लोन रिकवरी एजेंट द्वारा अभद्र भाषा, घर आकर धमकी और ब्लैकमेल किया जा रहा है।"
        },
        "6. सरकारी दफ्तर में 'कल आना', रिश्वत माँगना या लाइन में भगा देना": {
            "act": "सेवा का अधिकार कानून (RTPS Act) व भ्रष्टाचार निवारण अधिनियम",
            "authority": "अपीलीय अधिकारी, निगरानी ब्यूरो (Vigilance) व सीएम हेल्पलाइन",
            "rule": "तय समय में काम न करने पर संबंधित सरकारी कर्मचारी के वेतन से प्रतिदिन ₹250 से ₹5,000 जुर्माना काटकर पीड़ित को देने का नियम है।",
            "default_det": "आवश्यक प्रमाण पत्र/कार्य हेतु सभी वैध दस्तावेज देने के बावजूद संबंधित कर्मचारी द्वारा बिना घूस लिए बार-बार चक्कर कटवाए जा रहे हैं।"
        },
        "7. दुकानदार या कोटेदार द्वारा MRP से ज्यादा दाम व घटतौली": {
            "act": "लीगल मेट्रोलॉजी एक्ट 2009 व राष्ट्रीय खाद्य सुरक्षा अधिनियम (NFSA)",
            "authority": "उपभोक्ता मामले विभाग व जिला आपूर्ति पदाधिकारी (DSO)",
            "rule": "MRP से ₹1 भी ज्यादा लेना या राशन कम तौलना गैर-कानूनी है। पहली बार में ₹25,000 जुर्माना और दुकान का लाइसेंस रद्द हो सकता है।",
            "default_det": "दुकानदार/कोटेदार द्वारा तय मूल्य से अधिक राशि वसूली गई और निर्धारित मात्रा से कम सामग्री प्रदान की गई।"
        },
        "8. ट्रेन में टीटी (TTE) या अवैध वसूली करने वालों द्वारा बदसलूकी": {
            "act": "भारतीय रेलवे अधिनियम व रेल सुरक्षा नियम",
            "authority": "रेलवे बोर्ड विजिलेंस, आरपीएफ (RPF) व रेल मदद 139",
            "rule": "टीटी को यात्री के साथ अभद्रता करने या ट्रेन से धक्का देने का कोई हक नहीं। केवल निर्धारित रसीद (EFT) दी जा सकती है।",
            "default_det": "ट्रेन यात्रा के दौरान संबंधित टीटी द्वारा नियम विरुद्ध अतिरिक्त पैसे की मांग और विरोध करने पर दुर्व्यवहार किया गया।"
        },
        "9. थाने में एफआईआर (FIR) दर्ज न करना (Zero FIR का अधिकार)": {
            "act": "सुप्रीम कोर्ट ललिता कुमारी दिशा-निर्देश व धारा 173 BNSS",
            "authority": "वरिष्ठ पुलिस अधीक्षक (SSP/DGP) व न्यायिक दंडाधिकारी (CJM)",
            "rule": "संज्ञेय अपराध में एफआईआर न लिखना पुलिस अधिकारी पर खुद आपराधिक मुकदमा बनाता है, जिससे उसकी नौकरी जा सकती है।",
            "default_det": "घटना की लिखित सूचना देने के बावजूद थाना प्रभारी द्वारा प्रथम सूचना रिपोर्ट (FIR) दर्ज करने से मना कर दिया गया।"
        },
        "10. ज़मीन पर दबंगों द्वारा अवैध कब्ज़ा या पैतृक संपत्ति विवाद": {
            "act": "धारा 145/144 BNSS एवं नागरिक अधिकार संरक्षण कानून",
            "authority": "उप-विभागीय दंडाधिकारी (SDM) व सिविल न्यायालय",
            "rule": "किसी भी गरीब की पैतृक भूमि पर जबरन कब्जा होने पर प्रशासन को तुरंत यथास्थिति बनाए रखने और सुरक्षा देने का दायित्व है।",
            "default_det": "विपक्षी द्वारा प्रार्थी की वैध पैतृक भूमि पर बलपूर्वक अवैध कब्जे का प्रयास किया जा रहा है।"
        },
        "11. सड़क हादसे (Hit & Run) में मृत्यु या गंभीर चोट पर सरकारी मुआवजा": {
            "act": "मोटर वाहन संशोधन अधिनियम 2019 (हिट एंड रन मुआवजा योजना)",
            "authority": "दावा अधिकरण (MACT) व जिला कलेक्टर राहत कोष",
            "rule": "सड़क हादसे में मृत्यु पर सरकार द्वारा तत्काल ₹2 लाख और गंभीर घायल को ₹50,000 की अंतरिम राहत देने का कानून है।",
            "default_det": "सड़क दुर्घटना में घायल होने/मृत्यु होने के उपरांत तत्काल सरकारी राहत कोष व बीमा क्लेम की मांग की जाती है।"
        },
        "12. मुफ़्त सरकारी वकील पाने हेतु आवेदन (न्याय सबका अधिकार)": {
            "act": "विधिक सेवा प्राधिकरण अधिनियम 1987 (संविधान अनुच्छेद 39A)",
            "authority": "जिला विधिक सेवा प्राधिकरण (DLSA) सचिव",
            "rule": "गरीब, मजदूर, महिला और दिव्यांग को कोर्ट केस लड़ने के लिए सरकार अपने खर्चे पर मुफ़्त वकील उपलब्ध कराती है।",
            "default_det": "प्रार्थी आर्थिक रूप से असमर्थ है और उसे अपने मुकदमे की पैरवी हेतु मुफ़्त सरकारी विधिक सहायता की आवश्यकता है।"
        },
        "13. मकान मालिक द्वारा बिना नोटिस जबरन बेदखली या बिजली-पानी काटना": {
            "act": "रेंट कंट्रोल एक्ट व भारतीय न्याय संहिता",
            "authority": "किराया नियंत्रक (Rent Controller) व स्थानीय पुलिस",
            "rule": "मकान मालिक बिना कानूनी आदेश के ताला नहीं तोड़ सकता, न ही बिजली-पानी काट सकता है।",
            "default_det": "मकान मालिक द्वारा गैर-कानूनी ढंग से बुनियादी सुविधाएं बंद कर जबरन मकान खाली कराने की धमकी दी जा रही है।"
        },
        "14. जातिगत भेदभाव, गाली-गलौज व सामाजिक बहिष्कार निवारण": {
            "act": "अनुसूचित जाति/जनजाति अत्याचार निवारण अधिनियम (SC/ST Act) व अनुच्छेद 15",
            "authority": "एसपी (SP) व विशेष अदालत (Special Court)",
            "rule": "किसी भी नागरिक को जाति या वर्ग के आधार पर नीचा दिखाना, गाली देना या पानी/सड़क रोकने पर गैर-जमानती गिरफ्तारी का नियम है।",
            "default_det": "विपक्षी द्वारा जातिसूचक अपशब्दों का प्रयोग कर सार्वजनिक रूप से अपमानित और प्रताड़ित किया गया।"
        }
    }

    selected_issue = st.radio("📌 अपनी समस्या का चयन करें:", list(LEGAL_CASES.keys()))
    case_info = LEGAL_CASES[selected_issue]

    st.info(f"⚖️ **लागू कानून:** {case_info['act']} | **सक्षम प्राधिकारी:** {case_info['authority']}")

    col_v1, col_v2 = st.columns(2)
    with col_v1:
        v_name = st.text_input("पीड़ित / प्रार्थी का नाम:", value="साहिल कुमार")
    with col_v2:
        v_loc = st.text_input("जिला व राज्य:", value="पश्चिम चंपारण, बिहार")

    v_phone = st.text_input("पीड़ित का मोबाइल नंबर:", value="7484878440")
    v_accused = st.text_input("दोषी पक्ष / कंपनी / अधिकारी / थाना का नाम:", value="संबंधित दोषी पक्ष / अधिकारी")
    v_details = st.text_area("घटना का विवरण:", value=case_info["default_det"])

    if st.button("⚡ आधिकारिक विधिक शिकायत पत्र व कानूनी नोटिस ड्राफ्ट करें"):
        full_notice = f"""======================================================================
आधिकारिक कानूनी विधिक शिकायत पत्र व नोटिस
(अधिनियम: {case_info['act']})
दिनांक: {today_str}

सेवा में,
1. {case_info['authority']}, {v_loc}
2. राष्ट्रीय मानवाधिकार आयोग (NHRC) / संबंधित विधिक निगरानी बोर्ड

विषय: '{selected_issue}' के संबंध में दोषी '{v_accused}' पर तत्काल प्राथमिकी (FIR), दंडात्मक कार्रवाई व अधिकार रक्षा बाबत।

महोदय,
प्रार्थी {v_name} (मोबाइल: +91 {v_phone}), निवासी {v_loc} सादर अवगत कराना चाहता है:

1. यह कि प्रार्थी भारत का संविधान-सम्मत नागरिक है और विपक्षी '{v_accused}' द्वारा प्रार्थी के मौलिक अधिकारों व विधि के शासन का खुला उल्लंघन किया गया है।
2. तथ्यात्मक घटनाक्रम:
"{v_details}"
3. विधिक नियम व प्रावधान:
- {case_info['rule']}

अतः सक्षम प्राधिकारी से प्रार्थना है कि:
(क) दोषी '{v_accused}' के विरुद्ध सुसंगत कानूनी धाराओं में तत्काल प्राथमिकी (FIR) दर्ज कर कड़ी कार्रवाई की जाए।
(ख) प्रार्थी को उसका संपूर्ण देय हक, मुआवजा अथवा सुरक्षा अविलंब प्रदान की जाए।
(ग) प्रार्थी की जान-माल की रक्षा सुनिश्चित की जाए।

भवदीय:
{v_name}
संपर्क सूत्र: +91 {v_phone}
डिजिटल निगरानी: महा-सेवा AI राष्ट्रीय विधिक साक्षरता मिशन
======================================================================"""

        st.success("🟢 100% आधिकारिक विधिक नोटिस तैयार:")
        st.text_area("📄 तैयार कानूनी शिकायत पत्र:", full_notice, height=220)

        st.markdown(f"""
        <div class="caution-card">
            <h3 style="color:#EF4444; margin:0 0 6px 0;">⚖️ इस मामले में आपका कानूनी कवच:</h3>
            <p style="margin:0; font-size:14px; color:#FCA5A5;">{case_info['rule']}</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="text-align:center; margin:8px 0;">
            <p style="color:#38BDF8; font-size:13px; margin-bottom:6px;"><b>सीधे राष्ट्रीय सरकारी न्याय एवं सतर्कता हेल्पलाइन पर कॉल करें:</b></p>
            <a href="tel:112" class="btn-red-call">📞 112 राष्ट्रीय पुलिस</a>
            <a href="tel:1064" class="btn-red-call">📞 1064 एंटी-करप्शन</a>
            <a href="tel:14434" class="btn-red-call">📞 14434 श्रम व मजदूरी</a>
            <a href="tel:1915" class="btn-red-call">📞 1915 उपभोक्ता संरक्षण</a>
            <a href="tel:139" class="btn-red-call">📞 139 रेल मदद</a>
            <a href="tel:15100" class="btn-red-call">📞 15100 मुफ़्त विधिक सेवा (NALSA)</a>
        </div>
        """, unsafe_allow_html=True)

        enc_notice = urllib.parse.quote(full_notice)
        st.markdown(f'<a href="https://wa.me/?text={enc_notice}" target="_blank" class="btn-green">📲 शिकायत पत्र WhatsApp / सोशल मीडिया पर भेजें</a>', unsafe_allow_html=True)

# ================= TAB 2: NIGHT SAFETY & EMERGENCY SOS =================
elif nav_choice == "🚨 रात की सुरक्षा व पैनिक SOS":
    st.markdown("""
    <div class="emergency-card">
        <h2 style="color:#FFF; margin:0 0 6px 0; font-size:22px;">🚨 24x7 रात की सुरक्षा व पैनिक अलर्ट (SOS)</h2>
        <p style="color:#FECACA; font-size:13px; margin:0 0 12px 0;">रात में रास्ते पर किसी भी खतरे, पीछा करने या आपात स्थिति में तुरंत सीधे कॉल करें:</p>
        <div>
            <a href="tel:112" class="btn-red-call">📞 112 राष्ट्रीय आपात पुलिस</a>
            <a href="tel:1090" class="btn-red-call">📞 1090 वीमेन पावर लाइन</a>
            <a href="tel:181" class="btn-red-call">📞 181 महिला हेल्पलाइन</a>
        </div>
        <p style="color:#FCA5A5; font-size:12px; margin:8px 0 0 0;">(बिना इंटरनेट के भी सीधे कॉल लगेगी - 100% फ्री 24 घंटे)</p>
    </div>
    """, unsafe_allow_html=True)

    family_phone = st.text_input("परिवार / भाई / पिता का मोबाइल नंबर दर्ज करें:", value="7484878440")
    my_location = st.text_input("वर्तमान जगह / सड़क का नाम लिखें:", value="मुख्य चौराहा / मेन रोड")

    sos_msg = f"आपातकालीन अलर्ट (SOS)! मुझे तुरंत सहायता की आवश्यकता है। मेरी वर्तमान लोकेशन: {my_location}। कृपया तुरंत मुझसे संपर्क करें या पुलिस को सूचित करें।"
    enc_sos = urllib.parse.quote(sos_msg)
    
    st.markdown(f'<a href="https://wa.me/91{family_phone}?text={enc_sos}" target="_blank" class="btn-green">📲 1-क्लिक परिवार को लोकेशन व SOS भेजें</a>', unsafe_allow_html=True)

    # Audio Panic Siren
    st.write("### 🔊 पैनिक सायरन (भीड़ का ध्यान आकर्षित करने हेतु)")
    st.caption("अकेले में खतरा महसूस होने पर यह बटन दबाएँ, फोन से तेज़ सायरन आवाज़ निकलेगी:")
    siren_html = """
    <div style="text-align:center; margin:10px 0;">
        <button onclick="playSiren()" style="background:#EF4444; color:#fff; padding:12px 24px; border-radius:10px; border:none; font-weight:800; font-size:16px; cursor:pointer;">
            🚨 तेज़ अलार्म सायरन बजाएँ (Play Siren)
        </button>
    </div>
    <script>
        function playSiren() {
            var ctx = new (window.AudioContext || window.webkitAudioContext)();
            var osc = ctx.createOscillator();
            var gain = ctx.createGain();
            osc.type = 'sawtooth';
            osc.frequency.setValueAtTime(800, ctx.currentTime);
            osc.frequency.linearRampToValueAtTime(1400, ctx.currentTime + 0.3);
            osc.frequency.linearRampToValueAtTime(800, ctx.currentTime + 0.6);
            gain.gain.setValueAtTime(1, ctx.currentTime);
            osc.connect(gain);
            gain.connect(ctx.destination);
            osc.start();
            osc.stop(ctx.currentTime + 3);
        }
    </script>
    """
    components.html(siren_html, height=70)

# ================= TAB 3: HEALTH & EMERGENCY AMBULANCE =================
elif nav_choice == "🏥 दवा व एम्बुलेंस सहायता":
    st.markdown("""
    <div class="emergency-card">
        <h2 style="color:#FFF; margin:0 0 6px 0; font-size:20px;">🚨 मेडिकल इमरजेंसी व तत्काल एम्बुलेंस सहायता</h2>
        <p style="color:#FECACA; font-size:13px; margin:0 0 12px 0;">दुर्घटना, गंभीर बीमारी या प्रसव पीड़ा में तुरंत नीचे दिए गए नंबरों पर सीधे कॉल करें:</p>
        <div>
            <a href="tel:108" class="btn-red-call">📞 108 एम्बुलेंस (फ्री आपातकाल)</a>
            <a href="tel:102" class="btn-red-call">📞 102 मातृ-शिशु एम्बुलेंस</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    m_name = st.text_input("दवा का नाम लिखें या बीमारी का विवरण दें:", value="Azithromycin 500")
    if st.button("🔍 संपूर्ण दवा व जेनेरिक विश्लेषण निकालें"):
        st.markdown(f"""
        <div class="info-card">
            <h3 style="color:#38BDF8; margin:0 0 6px 0;">💊 दवा का परिचय: {m_name}</h3>
            <p style="margin:0; font-size:14px;">यह एंटीबायोटिक साल्ट बैक्टीरिया संक्रमण को नियंत्रित करने में सहायक है।</p>
            <p style="color:#10B981; font-size:14px; margin-top:6px;"><b>जन औषधि केंद्र भाव:</b> मात्र ₹20 से ₹35 (प्राइवेट से 70-80% सस्ता)।</p>
        </div>
        """, unsafe_allow_html=True)

# ================= TAB 4: BLUE-COLLAR & HELPER JOB ENGINE =================
elif nav_choice == "💼 रोज़गार व हेल्पर डेस्क":
    st.write("### 💼 पूरे देश में सीधी नौकरी व ठेकेदार संपर्क")
    target_city = st.text_input("📍 नौकरी का शहर/जिला:", value="Surat")
    work_role = st.text_input("🔧 काम का प्रकार (Role):", value="Factory Helper / Warehouse Worker")
    c_name = st.text_input("👤 आपका नाम:", value="साहिल अहमद (Sahil)")
    c_phone = st.text_input("📱 मोबाइल नंबर:", value="7484878440")

    if st.button("⚡ ठेकेदार संपर्क व अंग्रेज़ी आवेदन तैयार करें"):
        g_maps_search = f"https://www.google.com/maps/search/{urllib.parse.quote(f'{work_role} contractor agency in {target_city}')}"
        eng_pitch = f"Hello, My name is {c_name}. I am looking for immediate work as {work_role} in {target_city}. Contact: +91 {c_phone}. Ready for immediate joining."
        st.text_area("📄 तैयार आवेदन (Job Pitch):", eng_pitch, height=100)
        st.markdown(f'<a href="{g_maps_search}" target="_blank" class="btn-blue">📞 ठेकेदारों की डायरेक्ट लिस्ट खोलें</a>', unsafe_allow_html=True)

# ================= TAB 5: WELFARE SCHEMES =================
elif nav_choice == "🏛️ सरकारी योजना व सब्सिडी":
    st.write("### 🏛️ सरकारी योजना व सब्सिडी खोजक")
    custom_scheme = st.text_input("योजना का नाम लिखें:", value="पीएम आवास योजना")
    if st.button("⚡ संपूर्ण योजना विश्लेषण निकालें"):
        st.markdown(f"""
        <div class="info-card">
            <h3 style="color:#38BDF8; margin:0 0 6px 0;">📌 योजना विवरण: {custom_scheme}</h3>
            <p style="margin:0; font-size:14px;">पात्र परिवारों को पक्का मकान निर्माण हेतु ₹1,20,000 से ₹2,50,000 तक की सीधी वित्तीय सहायता बैंक खाते में DBT द्वारा मिलती है।</p>
        </div>
        """, unsafe_allow_html=True)

# ================= TAB 6: CYBER FRAUD & ADDICTION =================
elif nav_choice == "🛡️ साइबर फ्रॉड व नशा-मुक्ति":
    st.write("### 🛡️ साइबर फ्रॉड सुरक्षा व नशा-मुक्ति")
    st.markdown("""
    <div class="caution-card">
        <h3 style="color:#EF4444; margin:0 0 6px 0;">📞 राष्ट्रीय साइबर अपराध हेल्पलाइन:</h3>
        <p style="font-size:15px; margin:0;"><a href="tel:1930" style="color:#FFF; font-weight:bold;">📞 1930 पर तुरंत कॉल करें</a> (वित्तीय ठगी होने पर)</p>
    </div>
    <div class="info-card">
        <h3 style="color:#10B981; margin:0 0 6px 0;">🕊️ राष्ट्रीय नशा मुक्ति हेल्पलाइन:</h3>
        <p style="font-size:15px; margin:0;"><a href="tel:14446" style="color:#FFF; font-weight:bold;">📞 14446 (Toll-Free)</a> पर मुफ़्त परामर्श प्राप्त करें।</p>
    </div>
    """, unsafe_allow_html=True)

# Founder National Sovereign Footer
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; background: #0B1329; padding: 16px; border-radius: 14px; border: 2px solid #38BDF8;">
    <p style="color:#38BDF8; font-size:11px; margin:0; letter-spacing:2px;">🏛️ FOUNDER & CHIEF SYSTEM ARCHITECT</p>
    <h2 style="color:#FFF; margin:4px 0; font-size:22px;">साहिल अहमद (Sahil Ahmad)</h2>
    <p style="color:#94A3B8; font-size:12px; margin:0 0 10px 0;">Maha Seva AI — All-India Sovereign Citizen Legal & Welfare Infrastructure</p>
    <a href="https://wa.me/{MY_WA_NUMBER}" target="_blank" style="background:#10B981; color:#fff; padding:10px 20px; border-radius:8px; text-decoration:none; font-weight:bold; font-size:13px; display:inline-block;">💬 राष्ट्रीय संस्थापक सूत्र (+91 {MY_WA_NUMBER[-10:]})</a>
</div>
""", unsafe_allow_html=True)
