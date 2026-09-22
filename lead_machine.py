import streamlit as st
import streamlit.components.v1 as components
import urllib.parse
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

LANG_DICT = {
    "🇮🇳 हिन्दी": {
        "title": "महा-सेवा AI (MAHA SEVA AI)",
        "sub": "14 विधिक अधिकार • रात की सुरक्षा • रोज़गार • एम्बुलेंस • सरकारी योजना",
        "tag": "⚡ 24x7 अखंड भारत नागरिक, विधिक सुरक्षा व जन-अधिकार मिशन",
        "nav_lbl": "📂 सेवा श्रेणी चुनें:",
        "sec_rights": "⚖️ 14 विधिक अधिकार व शिकायत",
        "sec_sos": "🚨 रात की सुरक्षा व पैनिक SOS",
        "sec_health": "🏥 दवा व एम्बुलेंस सहायता",
        "sec_job": "💼 रोज़गार व हेल्पर डेस्क",
        "sec_scheme": "🏛️ सरकारी योजना व सब्सिडी",
        "sec_fraud": "🛡️ साइबर फ्रॉड व नशा-मुक्ति",
        "r_title": "⚖️ जन-अधिकार व भ्रष्टाचार विरोधी विधिक मंच",
        "r_sub": "अपनी समस्या चुनें — सिस्टम तुरंत संबंधित कानून के तहत कड़ा नोटिस तैयार करेगा",
        "btn_rights": "⚡ आधिकारिक विधिक शिकायत पत्र व कानूनी नोटिस ड्राफ्ट करें",
        "name_lbl": "पीड़ित / प्रार्थी का नाम:",
        "city_lbl": "जिला व राज्य:",
        "phone_lbl": "पीड़ित का मोबाइल नंबर:",
        "accused_lbl": "दोषी पक्ष / कंपनी / अधिकारी / थाना का नाम:",
        "detail_lbl": "घटना का विवरण (पूरी बात लिखें):",
        "send_wa": "📲 शिकायत पत्र WhatsApp पर भेजें"
    },
    "🇬🇧 English": {
        "title": "MAHA SEVA AI — Sovereign Mission",
        "sub": "14 Legal Rights • Night Safety • Jobs • Healthcare • Welfare",
        "tag": "⚡ 24x7 Pan-India Sovereign Citizen Legal & Welfare Infrastructure",
        "nav_lbl": "📂 Select Service Category:",
        "sec_rights": "⚖️ 14 Legal Rights & Complaints",
        "sec_sos": "🚨 Night Safety & Panic SOS",
        "sec_health": "🏥 Health & Ambulance Support",
        "sec_job": "💼 Employment & Helper Desk",
        "sec_scheme": "🏛️ Welfare Schemes & Subsidies",
        "sec_fraud": "🛡️ Cyber Shield & Anti-Addiction",
        "r_title": "⚖️ Citizen Rights & Anti-Corruption Legal Portal",
        "r_sub": "Select any injustice faced — the system generates an official legal notice immediately.",
        "btn_rights": "⚡ Draft Official Legal Notice & Complaint",
        "name_lbl": "Victim / Complainant Name:",
        "city_lbl": "District & State:",
        "phone_lbl": "Complainant Mobile Number:",
        "accused_lbl": "Accused Party / Company / Police Station:",
        "detail_lbl": "Incident Details (Factual Summary):",
        "send_wa": "📲 Send Legal Notice via WhatsApp"
    },
    "বাংলা (Bengali)": {
        "title": "মহা-সেবা AI (MAHA SEVA AI)",
        "sub": "১৪টি আইনি অধিকার • নৈশ নিরাপত্তা • কর্মসংস্থান • স্বাস্থ্য ও অ্যাম্বুলেন্স",
        "tag": "⚡ ২৪x৭ অখণ্ড ভারত নাগরিক আইনি ও কল্যাণ মিশন",
        "nav_lbl": "📂 পরিষেবা নির্বাচন করুন:",
        "sec_rights": "⚖️ ১৪টি আইনি অধিকার ও অভিযোগ",
        "sec_sos": "🚨 নৈশ নিরাপত্তা ও প্যানিক SOS",
        "sec_health": "🏥 ওষুধ ও অ্যাম্বুলেন্স সহায়তা",
        "sec_job": "💼 কর্মসংস্থান ও হেল্পার ডেস্ক",
        "sec_scheme": "🏛️ সরকারি প্রকল্প ও অনুদান",
        "sec_fraud": "🛡️ সাইবার সুরক্ষা ও নেশামুক্তি",
        "r_title": "⚖️ নাগরিক অধিকার ও দুর্নীতি বিরোধী আইনি মঞ্চ",
        "r_sub": "অন্যায় নির্বাচন করুন — অবিলম্বে আইনি নোটিশ প্রস্তুত হবে।",
        "btn_rights": "⚡ আইনি অভিযোগ পত্র ও নোটিশ তৈরি করুন",
        "name_lbl": "অভিযোগকারীর নাম:",
        "city_lbl": "জেলা ও রাজ্য:",
        "phone_lbl": "মোবাইল নম্বর:",
        "accused_lbl": "অভিযুক্ত পক্ষ / ঠিকাদার / থানা:",
        "detail_lbl": "ঘটনার সম্পূর্ণ বিবরণ:",
        "send_wa": "📲 হোয়াটসঅ্যাপে নোটিশ পাঠান"
    },
    "मराठी (Marathi)": {
        "title": "महा-सेवा AI (MAHA SEVA AI)",
        "sub": "१४ कायदेशीर अधिकार • रात्रीची सुरक्षा • रोजगार • रुग्णवाहिका • योजना",
        "tag": "⚡ २४x७ अखंड भारत नागरिक, कायदेशीर सुरक्षा व रोजगार मिशन",
        "nav_lbl": "📂 सेवा श्रेणी निवडा:",
        "sec_rights": "⚖️ १४ कायदेशीर अधिकार व तक्रार",
        "sec_sos": "🚨 रात्रीची सुरक्षा व SOS",
        "sec_health": "🏥 औषधे व रुग्णवाहिका",
        "sec_job": "💼 रोजगार व थेट नोकरी",
        "sec_scheme": "🏛️ सरकारी योजना व अनुदान",
        "sec_fraud": "🛡️ सायबर फसवणूक व व्यसनमुक्ती",
        "r_title": "⚖️ नागरी हक्क व भ्रष्टाचार विरोधी कायदेशीर मंच",
        "r_sub": "झालेला अन्याय निवडा — प्रणाली तात्काळ कडक कायदेशीर नोटीस तयार करेल.",
        "btn_rights": "⚡ कायदेशीर नोटीस व तक्रार अर्ज तयार करा",
        "name_lbl": "तक्रारदाराचे पूर्ण नाव:",
        "city_lbl": "जिल्हा व राज्य:",
        "phone_lbl": "मोबाईल नंबर:",
        "accused_lbl": "दोषी कंत्राटदार / पोलीस ठाणे:",
        "detail_lbl": "घटनेचा संपूर्ण तपशील:",
        "send_wa": "📲 WhatsApp वर अर्ज पाठवा"
    }
}

all_langs = list(LANG_DICT.keys())
chosen_lang = st.radio(
    "🌐 भाषा चुनें / Select Language / ভাষা বাছুন / भाषा निवडा:",
    all_langs,
    horizontal=True
)
T = LANG_DICT.get(chosen_lang, LANG_DICT["🇮🇳 हिन्दी"])

st.markdown(f"""
<div style="background: radial-gradient(circle at center, #1E3A8A 0%, #030712 100%); border: 2px solid #38BDF8; border-radius: 14px; padding: 14px; text-align: center; margin-bottom: 14px; box-shadow: 0 0 20px rgba(56, 189, 248, 0.25);">
    <span style="background:rgba(16,185,129,0.2); color:#10B981; border:1px solid #10B981; padding:3px 12px; border-radius:20px; font-size:11px; font-weight:800;">
        {T['tag']}
    </span>
    <h1 style="font-size:22px; margin:6px 0 0 0; color:#FFF;">{T['title']}</h1>
    <p style="font-size:12px; color:#38BDF8; margin:4px 0 0 0;">{T['sub']}</p>
</div>
""", unsafe_allow_html=True)

nav_choice = st.radio(
    T["nav_lbl"],
    [
        T["sec_rights"],
        T["sec_sos"],
        T["sec_health"],
        T["sec_job"],
        T["sec_scheme"],
        T["sec_fraud"]
    ],
    horizontal=True
)

st.markdown("---")

# 14 LEGAL CASES IN PURE HINDI (DEVANAGARI)
if nav_choice == T["sec_rights"]:
    st.write(f"### {T['r_title']}")
    st.caption(T['r_sub'])

    LEGAL_CASES = {
        "1. ठेकेदार या कंपनी ने मजदूरी/वेतन रोक लिया (Wage Theft)": {
            "act": "पेमेंट ऑफ वेजेस एक्ट 1936 एवं औद्योगिक विवाद अधिनियम",
            "authority": "श्रम आयुक्त (Labour Commissioner) एवं जिलाधिकारी (DM)",
            "rule": "मजदूरी दबाना गैर-कानूनी अपराध है। श्रम विभाग 10 गुना हर्जाना और 18% ब्याज दिलवाता है।",
            "default_det": "मैंने कार्यस्थल पर 2 महीने पूरी ईमानदारी से कार्य किया, जिसकी कुल बकाया राशि ₹24,000 है। मांगने पर गाली-गलौज व धमकी दी जा रही है।"
        },
        "2. पुलिस द्वारा गैर-कानूनी मारपीट, अभद्रता या फर्जी चालान": {
            "act": "भारतीय नागरिक सुरक्षा संहिता (BNSS) एवं सुप्रीम कोर्ट डी.के. बसु गाइडलाइन्स",
            "authority": "पुलिस अधीक्षक (SP), राज्य पुलिस शिकायत प्राधिकरण एवं NHRC",
            "rule": "बिना जुर्म मारपीट या गाली-गलौज करने पर धारा 166A BNS के तहत पुलिसकर्मी पर निलंबन व FIR होती है।",
            "default_det": "संबंधित पुलिसकर्मी द्वारा बिना किसी अपराध के मेरे साथ सार्वजनिक रूप से अभद्रता, मारपीट व अवैध चालान की धमकी दी गई।"
        },
        "3. अस्पताल द्वारा इमरजेंसी में भर्ती न करना या शव/मरीज को बंधक बनाना": {
            "act": "सुप्रीम कोर्ट परमानंद कटारा फैसला एवं क्लिनिकल एस्टेब्लिशमेंट एक्ट",
            "authority": "मुख्य चिकित्सा अधिकारी (CMO), स्वास्थ्य विभाग एवं उपभोक्ता आयोग",
            "rule": "इमरजेंसी में अग्रिम पैसे मांगकर इलाज से इनकार नहीं किया जा सकता। मरीज या शव को रोकना संज्ञेय अपराध है।",
            "default_det": "इमरजेंसी में अस्पताल द्वारा पहले अग्रिम राशि जमा करने का दबाव बनाकर इलाज में जानबूझकर देरी की गई।"
        },
        "4. कार्यस्थल/फैक्ट्री पर हादसा और शारीरिक अपंगता (मुआवजा)": {
            "act": "कर्मचारी मुआवजा कानून 1923 (Employees Compensation Act)",
            "authority": "मुआवजा आयुक्त एवं श्रम न्यायालय",
            "rule": "ड्यूटी के दौरान दुर्घटना होने पर मालिक को ₹5 लाख से ₹20 लाख का मुआवजा व आजीवन पेंशन देना अनिवार्य है।",
            "default_det": "कार्यस्थल पर सुरक्षा उपकरणों के अभाव में गंभीर दुर्घटना हुई जिससे स्थायी दिव्यांगता आई है। मालिक मुआवजा देने से मुकर रहा है।"
        },
        "5. सूदखोरों व फर्जी लोन ऐप्स द्वारा धमकी, गाली-गलौज और ब्लैकमेल": {
            "act": "RBI रिकवरी गाइडलाइन्स एवं जबरन वसूली कानून (धारा 308 BNS)",
            "authority": "साइबर क्राइम सेल, पुलिस अधीक्षक (SP) एवं RBI लोकपाल",
            "rule": "बिना लाइसेंस सूदखोरी और धमकी देकर वसूली करना गैर-कानूनी है। सीधे FIR और गिरफ्तारी होती है।",
            "default_det": "अवैध ब्याज वसूली हेतु लोन एजेंट द्वारा धमकी, घर आकर गाली-गलौज और फोटो वायरल करने का ब्लैकमेल किया जा रहा है।"
        },
        "6. सरकारी दफ्तर में घूसखोरी, 'कल आना' और लाइन में भगा देना (RTPS)": {
            "act": "सेवा का अधिकार कानून (RTPS Act) एवं भ्रष्टाचार निवारण अधिनियम",
            "authority": "निगरानी ब्यूरो (Vigilance Bureau) एवं मुख्यमंत्री हेल्पलाइन",
            "rule": "तय समय में काम न करने पर संबंधित सरकारी कर्मचारी के वेतन से प्रतिदिन ₹250 से ₹5,000 जुर्माना कटता है।",
            "default_det": "आवश्यक वैध दस्तावेज देने के बावजूद बिना रिश्वत के संबंधित कर्मचारी द्वारा बार-बार चक्कर लगवाए जा रहे हैं।"
        },
        "7. दुकानदार या राशन डीलर द्वारा MRP से ज्यादा दाम व घटतौली": {
            "act": "लीगल मेट्रोलॉजी एक्ट 2009 एवं राष्ट्रीय खाद्य सुरक्षा कानून (NFSA)",
            "authority": "उपभोक्ता मामले विभाग एवं जिला आपूर्ति पदाधिकारी (DSO)",
            "rule": "MRP से ₹1 भी ज्यादा लेना या राशन कम तौलना गैर-कानूनी है। ₹25,000 जुर्माना और लाइसेंस रद्द होता है।",
            "default_det": "दुकानदार/कोटेदार द्वारा तय मूल्य से अधिक राशि वसूली गई और निर्धारित मात्रा से कम सामग्री दी गई।"
        },
        "8. ट्रेन में टीटीई (TTE) या किसी द्वारा अवैध वसूली व बदसलूकी": {
            "act": "भारतीय रेलवे अधिनियम एवं रेल सुरक्षा नियम",
            "authority": "रेलवे बोर्ड विजिलेंस, आरपीएफ (RPF) एवं रेल मदद 139",
            "rule": "टीटीई को यात्री से बदतमीजी करने या ट्रेन से धक्का देने का कोई हक नहीं। केवल सरकारी रसीद (EFT) दी जा सकती है।",
            "default_det": "यात्रा के दौरान टीटीई द्वारा नियम विरुद्ध अतिरिक्त पैसे की मांग और विरोध करने पर बदसलूकी की गई।"
        },
        "9. थाने में एफआईआर (FIR) दर्ज न करना (Zero FIR का अधिकार)": {
            "act": "सुप्रीम कोर्ट ललिता कुमारी दिशा-निर्देश एवं धारा 173 BNSS",
            "authority": "वरिष्ठ पुलिस अधीक्षक (SSP), डीजीपी एवं सीजेएम कोर्ट",
            "rule": "संज्ञेय अपराध में FIR न लिखने वाले पुलिस अधिकारी पर धारा 166A BNS के तहत खुद FIR दर्ज होती है।",
            "default_det": "घटना की लिखित सूचना देने के बावजूद थाना प्रभारी द्वारा प्रथम सूचना रिपोर्ट (FIR) दर्ज करने से मना किया गया।"
        },
        "10. पैतृक जमीन पर दबंगों द्वारा अवैध कब्जा या मेड़ काटना": {
            "act": "धारा 145/144 BNSS एवं नागरिक अधिकार संरक्षण कानून",
            "authority": "उप-विभागीय दंडाधिकारी (SDM) एवं सिविल न्यायालय",
            "rule": "गरीब की पैतृक भूमि पर जबरन कब्जे की कोशिश पर प्रशासन को तुरंत सुरक्षा देना और स्टे लगाना अनिवार्य है।",
            "default_det": "विपक्षी द्वारा प्रार्थी की वैध पैतृक जमीन पर बलपूर्वक अवैध कब्जे का प्रयास किया जा रहा है।"
        },
        "11. सड़क हादसे (Hit and Run) में सरकारी मुआवजा व राहत": {
            "act": "मोटर वाहन संशोधन अधिनियम (हिट एंड रन मुआवजा योजना)",
            "authority": "दावा अधिकरण (MACT) एवं जिला कलेक्टर राहत कोष",
            "rule": "मृत्यु पर सरकार द्वारा तत्काल ₹2 लाख और गंभीर घायल को ₹50,000 की अंतरिम राहत देने का कानून है।",
            "default_det": "सड़क दुर्घटना के उपरांत तत्काल सरकारी राहत कोष व बीमा क्लेम की मांग की जा रही है।"
        },
        "12. मुफ्त सरकारी वकील पाने हेतु आवेदन (न्याय सबका अधिकार)": {
            "act": "विधिक सेवा प्राधिकरण अधिनियम 1987 (अनुच्छेद 39A)",
            "authority": "जिला विधिक सेवा प्राधिकरण (DLSA) सचिव",
            "rule": "गरीब, मजदूर और महिला को कोर्ट केस लड़ने के लिए सरकार अपने खर्चे पर मुफ्त वकील उपलब्ध कराती है।",
            "default_det": "प्रार्थी आर्थिक रूप से असमर्थ है और उसे अपने मुकदमे की पैरवी हेतु मुफ्त सरकारी वकील की आवश्यकता है।"
        },
        "13. मकान मालिक द्वारा बिना नोटिस जबरन बेदखली या बिजली-पानी काटना": {
            "act": "रेंट कंट्रोल एक्ट एवं भारतीय न्याय संहिता",
            "authority": "किराया नियंत्रक (Rent Controller) एवं स्थानीय पुलिस",
            "rule": "मकान मालिक बिना कोर्ट ऑर्डर के ताला नहीं तोड़ सकता, न ही बिजली-पानी काट सकता है।",
            "default_det": "मकान मालिक द्वारा बिना कानूनी नोटिस पानी-बिजली बंद कर जबरन मकान खाली कराने की धमकी दी जा रही है।"
        },
        "14. जातिगत भेदभाव, गाली-गलौज व सामाजिक बहिष्कार निवारण": {
            "act": "अनुसूचित जाति/जनजाति अत्याचार निवारण अधिनियम (SC/ST Act) एवं अनुच्छेद 15",
            "authority": "पुलिस अधीक्षक (SP) एवं विशेष अदालत",
            "rule": "जाति के आधार पर अपमानित करने, गाली देने या रास्ता रोकने पर गैर-जमानती गिरफ्तारी होती है।",
            "default_det": "विपक्षी द्वारा जातिसूचक अपशब्दों का प्रयोग कर सार्वजनिक रूप से अपमानित और प्रताड़ित किया गया।"
        }
    }

    selected_issue = st.radio("📌 अपनी समस्या का चयन करें:", list(LEGAL_CASES.keys()))
    case_info = LEGAL_CASES[selected_issue]

    st.info(f"⚖️ **कानून:** {case_info['act']} | **प्राधिकारी:** {case_info['authority']}")

    col_v1, col_v2 = st.columns(2)
    with col_v1:
        v_name = st.text_input(T["name_lbl"], value="साहिल कुमार", key=f"name_{chosen_lang}")
    with col_v2:
        v_loc = st.text_input(T["city_lbl"], value="पश्चिम चंपारण, बिहार", key=f"city_{chosen_lang}")

    v_phone = st.text_input(T["phone_lbl"], value="7484878440", key=f"phone_{chosen_lang}")
    v_accused = st.text_input(T["accused_lbl"], value="संबंधित दोषी पक्ष / अधिकारी", key=f"acc_{chosen_lang}")
    
    # ISSUE KEY DYNAMIC: समस्या बदलते ही ब्योरा तुरंत बदलेगा
    issue_num = selected_issue.split(".")[0].strip()
    v_details = st.text_area(T["detail_lbl"], value=case_info["default_det"], key=f"det_{chosen_lang}_{issue_num}")

    if st.button(T['btn_rights'], key=f"btn_r_{chosen_lang}_{issue_num}"):
        full_notice = f"""======================================================================
आधिकारिक कानूनी विधिक शिकायत पत्र व नोटिस
(अधिनियम: {case_info['act']})
दिनांक: {today_str}

सेवा में,
1. {case_info['authority']}, {v_loc}
2. राष्ट्रीय मानवाधिकार आयोग (NHRC) / विधिक निगरानी बोर्ड

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

        st.success("🟢 आधिकारिक विधिक नोटिस तैयार:")
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
        st.markdown(f'<a href="https://wa.me/?text={enc_notice}" target="_blank" class="btn-green">{T["send_wa"]}</a>', unsafe_allow_html=True)

elif nav_choice == T["sec_sos"]:
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

elif nav_choice == T["sec_health"]:
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

elif nav_choice == T["sec_job"]:
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

elif nav_choice == T["sec_scheme"]:
    st.write("### 🏛️ सरकारी योजना व सब्सिडी खोजक")
    custom_scheme = st.text_input("योजना का नाम लिखें:", value="पीएम आवास योजना")
    if st.button("⚡ संपूर्ण योजना विश्लेषण निकालें"):
        st.markdown(f"""
        <div class="info-card">
            <h3 style="color:#38BDF8; margin:0 0 6px 0;">📌 योजना विवरण: {custom_scheme}</h3>
            <p style="margin:0; font-size:14px;">पात्र परिवारों को पक्का मकान निर्माण हेतु ₹1,20,000 से ₹2,50,000 तक की सीधी वित्तीय सहायता बैंक खाते में DBT द्वारा मिलती है।</p>
        </div>
        """, unsafe_allow_html=True)

elif nav_choice == T["sec_fraud"]:
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
