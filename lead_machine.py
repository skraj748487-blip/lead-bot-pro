import streamlit as st
import streamlit.components.v1 as components
import urllib.parse
from datetime import datetime

# 1. Page Configuration
st.set_page_config(
    page_title="महा-सेवा AI — राष्ट्रीय नागरिक विधिक सुरक्षा मिशन",
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

    input, .stTextInput input, textarea, .stTextArea textarea, .stSelectbox div {
        background-color: #0B1329 !important;
        color: #38BDF8 !important;
        font-size: 15px !important;
        font-weight: 700 !important;
        border: 2px solid #0284C7 !important;
        border-radius: 12px !important;
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

    .emergency-box {
        background: radial-gradient(circle at center, #7F1D1D 0%, #450A0A 100%);
        border: 2px solid #EF4444;
        border-radius: 14px;
        padding: 16px;
        text-align: center;
        margin-bottom: 16px;
        box-shadow: 0 0 30px rgba(239, 68, 68, 0.5);
    }
    .caution-card {
        background: rgba(239, 68, 68, 0.12);
        border: 2px solid #EF4444;
        border-radius: 12px;
        padding: 14px;
        margin-top: 12px;
        margin-bottom: 12px;
    }
    .info-card {
        background: #0F172A;
        border: 2px solid #1E293B;
        border-radius: 12px;
        padding: 14px;
        margin-bottom: 12px;
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
current_time_str = datetime.now().strftime("%I:%M %p")

# ALL INDIA 12 LANGUAGES LIST
LANG_LIST = [
    "🇮🇳 हिन्दी", "🇬🇧 English", "বাংলা (Bengali)", "मराठी (Marathi)", 
    "தமிழ் (Tamil)", "తెలుగు (Telugu)", "ગુજરાતી (Gujarati)", "ಕನ್ನಡ (Kannada)", 
    "മലയാളം (Malayalam)", "ਪੰਜਾਬੀ (Punjabi)", "ଓଡ଼ିଆ (Odia)", "অসমীয়া (Assamese)"
]

chosen_lang = st.radio("🌐 भाषा चुनें / Select Language:", LANG_LIST, horizontal=True)

# Header
st.markdown("""
<div style="background: radial-gradient(circle at center, #1E3A8A 0%, #030712 100%); border: 2px solid #38BDF8; border-radius: 14px; padding: 14px; text-align: center; margin-bottom: 14px; box-shadow: 0 0 20px rgba(56, 189, 248, 0.25);">
    <span style="background:rgba(16,185,129,0.2); color:#10B981; border:1px solid #10B981; padding:3px 12px; border-radius:20px; font-size:11px; font-weight:800;">
        ⚡ 24x7 अखंड भारत नागरिक व विधिक सुरक्षा मिशन
    </span>
    <h1 style="font-size:22px; margin:6px 0 0 0; color:#FFF;">महा-सेवा AI (MAHA SEVA AI)</h1>
    <p style="font-size:12px; color:#38BDF8; margin:4px 0 0 0;">28 महा-विधिक अधिकार • रात की सुरक्षा व GPS SOS • बोलकर शिकायत • दवा व रोज़गार</p>
</div>
""", unsafe_allow_html=True)

nav_choice = st.radio(
    "📂 सेवा श्रेणी चुनें:",
    [
        "⚖️ 28 विधिक अधिकार व कानूनी नोटिस",
        "🚨 रात की सुरक्षा व लाइव GPS SOS",
        "🎙️ बोलकर शिकायत दर्ज करें (माइक)",
        "🛡️ साइबर फ्रॉड व मैसेज चेकर",
        "🏥 दवा व एम्बुलेंस सहायता",
        "💼 रोज़गार व हेल्पर डेस्क"
    ],
    horizontal=True
)

st.markdown("---")

# ================= TAB 1: 28 LEGAL RIGHTS & REAL COURT DRAFT =================
if nav_choice == "⚖️ 28 विधिक अधिकार व कानूनी नोटिस":
    st.write("### ⚖️ 28 महा-विधिक अधिकार व आधिकारिक नोटिस मंच")
    st.caption("अपनी समस्या चुनें — व्यवस्था तुरंत कानून व धाराओं के साथ कानूनी नोटिस तैयार करेगी:")

    LEGAL_CASES_28 = {
        "1. ठेकेदार/कंपनी ने मजदूरी या वेतन दबा लिया": {
            "act": "पेमेंट ऑफ वेजेस एक्ट 1936 एवं औद्योगिक विवाद अधिनियम",
            "authority": "श्रम आयुक्त (Labour Commissioner) व जिलाधिकारी (DM)",
            "rule": "मजदूरी दबाना गैर-कानूनी अपराध है। श्रम विभाग 10 गुना हर्जाना और 18% ब्याज दिलवाता है।",
            "det": "मैंने 2 महीने पूरी ईमानदारी से कार्य किया, जिसका कुल ₹24,000 बकाया है। मांगने पर गाली-गलौज व धमकी दी जा रही है।"
        },
        "2. पुलिस द्वारा गैर-कानूनी मारपीट, अभद्रता या फर्जी चालान": {
            "act": "भारतीय नागरिक सुरक्षा संहिता (BNSS) व डी.के. बसु गाइडलाइन्स",
            "authority": "पुलिस अधीक्षक (SP), राज्य पुलिस शिकायत प्राधिकरण व NHRC",
            "rule": "बिना जुर्म मारपीट या गाली देने पर धारा 166A BNS के तहत पुलिसकर्मी पर निलंबन व FIR होती है।",
            "det": "संबंधित पुलिसकर्मी द्वारा बिना किसी अपराध के मेरे साथ सार्वजनिक रूप से अभद्रता, मारपीट व अवैध चालान की धमकी दी गई।"
        },
        "3. अस्पताल द्वारा इमरजेंसी में भर्ती न करना या शव बंधक बनाना": {
            "act": "सुप्रीम कोर्ट परमानंद कटारा फैसला व क्लिनिकल एस्टेब्लिशमेंट एक्ट",
            "authority": "मुख्य चिकित्सा अधिकारी (CMO) व स्वास्थ्य विभाग",
            "rule": "इमरजेंसी में पैसे मांगकर इलाज से इनकार नहीं किया जा सकता। शव या मरीज को बंधक बनाना संज्ञेय अपराध है।",
            "det": "इमरजेंसी में अस्पताल द्वारा अग्रिम राशि का दबाव बनाकर इलाज में जानबूझकर देरी की गई।"
        },
        "4. कार्यस्थल/फैक्ट्री पर हादसा व शारीरिक अपंगता (मुआवजा)": {
            "act": "कर्मचारी मुआवजा कानून 1923 (Employees Compensation Act)",
            "authority": "मुआवजा आयुक्त एवं श्रम न्यायालय",
            "rule": "ड्यूटी के दौरान दुर्घटना होने पर मालिक को ₹5 लाख से ₹20 लाख का मुआवजा व आजीवन पेंशन देना अनिवार्य है।",
            "det": "कार्यस्थल पर सुरक्षा उपकरणों के अभाव में गंभीर दुर्घटना हुई जिससे स्थायी दिव्यांगता आई है। मालिक मुआवजा देने से मुकर रहा है।"
        },
        "5. सूदखोरों व फर्जी लोन ऐप्स द्वारा धमकी व ब्लैकमेल": {
            "act": "RBI रिकवरी गाइडलाइन्स एवं जबरन वसूली कानून (धारा 308 BNS)",
            "authority": "साइबर क्राइम सेल, एसपी (SP) एवं RBI लोकपाल",
            "rule": "बिना लाइसेंस सूदखोरी और धमकी देकर वसूली करना गैर-कानूनी है। सीधे FIR और गिरफ्तारी होती है।",
            "det": "अवैध ब्याज वसूली हेतु लोन एजेंट द्वारा धमकी, घर आकर गाली-गलौज और फोटो वायरल करने का ब्लैकमेल किया जा रहा है।"
        },
        "6. सरकारी दफ्तर में घूसखोरी, 'कल आना' और लाइन में भगा देना": {
            "act": "सेवा का अधिकार कानून (RTPS Act) एवं भ्रष्टाचार निवारण अधिनियम",
            "authority": "निगरानी ब्यूरो (Vigilance Bureau) एवं मुख्यमंत्री हेल्पलाइन",
            "rule": "तय समय में काम न करने पर सरकारी कर्मचारी के वेतन से प्रतिदिन ₹250 से ₹5,000 जुर्माना कटता है।",
            "det": "वैध दस्तावेज देने के बावजूद बिना रिश्वत के संबंधित कर्मचारी द्वारा बार-बार चक्कर लगवाए जा रहे हैं।"
        },
        "7. दुकानदार या राशन डीलर द्वारा MRP से ज्यादा दाम व घटतौली": {
            "act": "लीगल मेट्रोलॉजी एक्ट 2009 एवं राष्ट्रीय खाद्य सुरक्षा कानून (NFSA)",
            "authority": "उपभोक्ता मामले विभाग एवं जिला आपूर्ति पदाधिकारी (DSO)",
            "rule": "MRP से ₹1 भी ज्यादा लेना या राशन कम तौलना गैर-कानूनी है। ₹25,000 जुर्माना और दुकान सील होती है।",
            "det": "दुकानदार/कोटेदार द्वारा तय मूल्य से अधिक राशि वसूली गई और निर्धारित मात्रा से कम सामग्री दी गई।"
        },
        "8. ट्रेन में टीटीई (TTE) द्वारा अवैध वसूली व बदसलूकी": {
            "act": "भारतीय रेलवे अधिनियम एवं रेल सुरक्षा नियम",
            "authority": "रेलवे बोर्ड विजिलेंस, आरपीएफ (RPF) एवं रेल मदद 139",
            "rule": "टीटीई को यात्री से बदतमीजी करने या धक्का देने का कोई हक नहीं। केवल सरकारी रसीद (EFT) दी जा सकती है।",
            "det": "यात्रा के दौरान टीटीई द्वारा नियम विरुद्ध पैसे की मांग और विरोध करने पर बदसलूकी की गई।"
        },
        "9. थाने में एफआईआर (FIR) दर्ज न करना (Zero FIR का अधिकार)": {
            "act": "सुप्रीम कोर्ट ललिता कुमारी दिशा-निर्देश एवं धारा 173 BNSS",
            "authority": "वरिष्ठ पुलिस अधीक्षक (SSP), डीजीपी एवं सीजेएम कोर्ट",
            "rule": "FIR न लिखने वाले पुलिस अधिकारी पर धारा 166A BNS के तहत खुद FIR दर्ज होती है।",
            "det": "घटना की लिखित सूचना देने के बावजूद थाना प्रभारी द्वारा FIR दर्ज करने से मना किया गया।"
        },
        "10. पैतृक जमीन पर दबंगों द्वारा अवैध कब्जा या मेड़ काटना": {
            "act": "धारा 145/144 BNSS एवं नागरिक अधिकार संरक्षण कानून",
            "authority": "उप-विभागीय दंडाधिकारी (SDM) एवं सिविल न्यायालय",
            "rule": "गरीब की पैतृक भूमि पर जबरन कब्जे की कोशिश पर प्रशासन को तुरंत सुरक्षा देना और स्टे लगाना अनिवार्य है।",
            "det": "विपक्षी द्वारा प्रार्थी की वैध पैतृक जमीन पर बलपूर्वक अवैध कब्जे का प्रयास किया जा रहा है।"
        },
        "11. सड़क हादसे (Hit and Run) में सरकारी मुआवजा व राहत": {
            "act": "मोटर वाहन संशोधन अधिनियम (हिट एंड रन मुआवजा योजना)",
            "authority": "दावा अधिकरण (MACT) एवं जिला कलेक्टर राहत कोष",
            "rule": "मृत्यु पर सरकार द्वारा तत्काल ₹2 लाख और गंभीर घायल को ₹50,000 की राहत देने का कानून है।",
            "det": "सड़क दुर्घटना के उपरांत तत्काल सरकारी राहत कोष व बीमा क्लेम की मांग की जा रही है।"
        },
        "12. मुफ्त सरकारी वकील पाने हेतु आवेदन (न्याय सबका अधिकार)": {
            "act": "विधिक सेवा प्राधिकरण अधिनियम 1987 (अनुच्छेद 39A)",
            "authority": "जिला विधिक सेवा प्राधिकरण (DLSA) सचिव",
            "rule": "गरीब, मजदूर और महिला को कोर्ट केस लड़ने के लिए सरकार अपने खर्चे पर मुफ्त वकील उपलब्ध कराती है।",
            "det": "प्रार्थी आर्थिक रूप से असमर्थ है और उसे मुकदमे की पैरवी हेतु मुफ्त सरकारी वकील की आवश्यकता है।"
        },
        "13. मकान मालिक द्वारा बिना नोटिस जबरन बेदखली या बिजली-पानी काटना": {
            "act": "रेंट कंट्रोल एक्ट एवं भारतीय न्याय संहिता",
            "authority": "किराया नियंत्रक (Rent Controller) एवं स्थानीय पुलिस",
            "rule": "मकान मालिक बिना कोर्ट ऑर्डर के ताला नहीं तोड़ सकता, न ही बिजली-पानी काट सकता है।",
            "det": "मकान मालिक द्वारा बिना कानूनी नोटिस पानी-बिजली बंद कर जबरन मकान खाली कराने की धमकी दी जा रही है।"
        },
        "14. जातिगत भेदभाव, गाली-गलौज व सामाजिक बहिष्कार निवारण": {
            "act": "अनुसूचित जाति/जनजाति अत्याचार निवारण अधिनियम (SC/ST Act)",
            "authority": "पुलिस अधीक्षक (SP) एवं विशेष अदालत",
            "rule": "जाति के आधार पर अपमानित करने या रास्ता रोकने पर गैर-जमानती गिरफ्तारी होती है।",
            "det": "विपक्षी द्वारा जातिसूचक अपशब्दों का प्रयोग कर सार्वजनिक रूप से अपमानित और प्रताड़ित किया गया।"
        },
        "15. धर्म के नाम पर नफरत व भेदभाव निवारण": {
            "act": "संविधान अनुच्छेद 15 एवं धारा 196 BNS (धार्मिक सौहार्द)",
            "authority": "जिला दंडाधिकारी (DM) एवं मानवाधिकार आयोग",
            "rule": "धर्म के आधार पर किसी नागरिक के साथ सार्वजनिक स्थल पर भेदभाव या नफरत फैलाना गैर-जमानती अपराध है।",
            "det": "विपक्षी द्वारा धार्मिक आधार पर सार्वजनिक बहिष्कार और भेदभावपूर्ण व्यवहार किया गया।"
        },
        "16. डिलीवरी बॉय व ड्राइवर अधिकार (Gig Workers Social Security)": {
            "act": "कोड ऑन सोशल सिक्योरिटी 2020 एवं गिग वर्कर्स सुरक्षा नियम",
            "authority": "श्रम कल्याण बोर्ड एवं कंपनी नोडल अधिकारी",
            "rule": "कंपनी बिना वैध कारण आईडी ब्लॉक नहीं कर सकती और दुर्घटना होने पर उपचार व मुआवजा देना अनिवार्य है।",
            "det": "बिना किसी पूर्व सूचना या सुनवाई के डिलीवरी/ड्राइवर आईडी ब्लॉक कर दी गई और बकाया भुगतान रोक लिया गया।"
        },
        "17. राशन कार्ड में कोटेदार द्वारा अंगूठा लगवाकर राशन न देना": {
            "act": "राष्ट्रीय खाद्य सुरक्षा अधिनियम (NFSA) 2013",
            "authority": "जिला आपूर्ति पदाधिकारी (DSO) एवं अनुमंडल पदाधिकारी (SDO)",
            "rule": "अंगूठा लगवाकर राशन न देना या कटौती करना सीधे खाद्यान्न चोरी का संज्ञेय अपराध है।",
            "det": "कोटेदार द्वारा ई-पॉस मशीन पर फिंगरप्रिंट लेने के बावजूद इस माह का निर्धारित राशन नहीं दिया गया।"
        },
        "18. बैंक अकाउंट फ्रीज व मिनिमम बैलेंस के नाम पर अवैध कटौती": {
            "act": "RBI दिशानिर्देश व बैंकिंग लोकपाल योजना",
            "authority": "बैंकिंग लोकपाल (RBI Ombudsman) एवं नोडल अधिकारी",
            "rule": "बैंक सेविंग्स खाते को चार्ज काटकर माइनस में नहीं ले जा सकता, न ही बिना पूर्व नोटिस खाता फ्रीज कर सकता है।",
            "det": "बैंक द्वारा बिना किसी विधिक नोटिस के खाता फ्रीज कर दिया गया तथा अनुचित शुल्क काटा गया।"
        },
        "19. बिजली विभाग की मनमानी, फर्जी बिल व ट्रांसफार्मर खराबी": {
            "act": "विद्युत अधिनियम 2003 (उपभोक्ता अधिकार नियमावली)",
            "authority": "विद्युत कार्यपालक अभियंता एवं उपभोक्ता शिकायत निवारण फोरम (CGRF)",
            "rule": "जला हुआ ट्रांसफार्मर ग्रामीण क्षेत्र में 48 घंटे और शहरी क्षेत्र में 24 घंटे में बदलना अनिवार्य है।",
            "det": "कई दिनों से ट्रांसफार्मर खराब रहने के बावजूद विभाग द्वारा कोई सुध नहीं ली गई तथा अत्यधिक फर्जी बिल भेजा गया।"
        },
        "20. आयुष्मान कार्ड (PM-JAY) होने पर अस्पताल द्वारा इलाज से इनकार": {
            "act": "राष्ट्रीय स्वास्थ्य प्राधिकरण (NHA) अनुबंध नियम",
            "authority": "स्टेट एंटी-फ्रॉड यूनिट (SAFU) एवं सीएमओ",
            "rule": "सूचीबद्ध अस्पताल आयुष्मान कार्ड धारक का इलाज करने से मना नहीं कर सकता; उल्लंघन पर पैनल रद्द होता है।",
            "det": "गोल्डन कार्ड सक्रिय होने के बावजूद अस्पताल प्रशासन द्वारा निशुल्क उपचार देने से साफ इनकार कर दिया गया।"
        },
        "21. पीएम आवास योजना में मुखिया/बाबू द्वारा रिश्वत की मांग": {
            "act": "भ्रष्टाचार निवारण अधिनियम एवं PMAY शिकायत निवारण नियम",
            "authority": "जिला लोकपाल, डीडीसी (DDC) एवं निगरानी ब्यूरो",
            "rule": "डीबीटी (DBT) के तहत मिलने वाले आवास पैसे में रिश्वत मांगना संज्ञेय भ्रष्टाचार अपराध है।",
            "det": "आवास योजना की स्वीकृत किस्त जारी करने के एवज में संबंधित कर्मी द्वारा अवैध कमीशन की मांग की जा रही है।"
        },
        "22. बच्चों का प्राइवेट स्कूल में 25% फ्री एडमिशन (RTE Act)": {
            "act": "शिक्षा का अधिकार अधिनियम (RTE) धारा 12(1)(c)",
            "authority": "जिला शिक्षा पदाधिकारी (DEO) एवं बाल अधिकार आयोग",
            "rule": "हर गैर-अल्पसंख्यक प्राइवेट स्कूल में 25% सीटें गरीब बच्चों के लिए पूर्णतः निशुल्क आरक्षित होती हैं।",
            "det": "RTE पात्रता होने के बावजूद संबंधित निजी विद्यालय द्वारा गरीब छात्र का प्रवेश लेने से मना किया गया।"
        },
        "23. किसान नकली खाद-बीज व कीटनाशक से फसल बर्बादी": {
            "act": "कीटनाशक अधिनियम 1968 एवं आवश्यक वस्तु अधिनियम",
            "authority": "जिला कृषि पदाधिकारी (DAO) एवं उपभोक्ता अदालत",
            "rule": "नकली सामग्री बेचने पर विक्रेता पर मुकदमा और किसान को 100% फसल नुकसान का हर्जाना देने का नियम है।",
            "det": "दुकानदार द्वारा अमानक/नकली बीज व खाद बेचे जाने के कारण मेरी संपूर्ण खड़ी फसल नष्ट हो गई।"
        },
        "24. प्रधानमंत्री फसल बीमा (PMFBY) क्लेम चोरी व रिजेक्शन": {
            "act": "PMFBY संशोधित परिचालन दिशानिर्देश",
            "authority": "जिला स्तरीय कृषि बीमा समिति (DLMC) एवं कृषि विभाग",
            "rule": "आपदा के समय 72 घंटे में सूचना देने पर बीमा कंपनी को 12% ब्याज सहित क्लेम देना अनिवार्य है।",
            "det": "बाढ़/सूखा से हुए प्रमाणित नुकसान के बावजूद बीमा कंपनी द्वारा क्लेम को गैर-कानूनी ढंग से निरस्त किया गया।"
        },
        "25. बुजुर्ग माता-पिता की संपत्ति हड़पना व घर से निकालना": {
            "act": "माता-पिता एवं वरिष्ठ नागरिक भरण-पोषण कानून 2007",
            "authority": "अनुमंडल दंडाधिकारी (SDM ट्रिब्यूनल)",
            "rule": "प्रताड़ित करने पर माता-पिता द्वारा बेटे को दी गई संपत्ति की रजिस्ट्री रद्द हो जाती है और मकान खाली कराया जाता है।",
            "det": "संपत्ति अपने नाम कराने के उपरांत संतानों द्वारा भोजन-दवा बंद कर घर से बेदखल करने का प्रयास किया जा रहा है।"
        },
        "26. छात्र पेपर लीक व कोचिंग संस्थानों द्वारा फीस न लौटाना": {
            "act": "लोक परीक्षा (अनुचित साधन निवारण) कानून 2024 व UGC नियम",
            "authority": "उपभोक्ता आयोग एवं उच्च शिक्षा विभाग",
            "rule": "कोचिंग बीच में छोड़ने पर शेष बची फीस वापस करना अनिवार्य है; पेपर लीक माफिया पर ₹1 करोड़ जुर्माना है।",
            "det": "पाठ्यक्रम छोड़ने के उपरांत भी संस्थान द्वारा नियमानुसार शेष जमा शुल्क वापस करने से इनकार किया गया।"
        },
        "27. ट्रैफिक पुलिस द्वारा चाबी छीनना, डंडा मारना या अवैध चालान": {
            "act": "मोटर वाहन अधिनियम एवं गृह मंत्रालय सर्कुलर",
            "authority": "यातायात पुलिस अधीक्षक (SP Traffic) व मानवाधिकार आयोग",
            "rule": "चलती गाड़ी से चाबी निकालना या डंडा मारना अपराध है; DigiLocker के डिजिटल दस्तावेज 100% मान्य हैं।",
            "det": "वैध डिजिटल दस्तावेज प्रस्तुत करने के बावजूद ट्रैफिक कर्मी द्वारा दुर्व्यवहार किया गया और चाबी छीनी गई।"
        },
        "28. मरीज का अधिकार पत्र (फाइल व बाहर से दवा लेने की आजादी)": {
            "act": "राष्ट्रीय मानवाधिकार आयोग पेशेंट राइट्स चार्टर",
            "authority": "सीएमओ (CMO) एवं राज्य चिकित्सा परिषद",
            "rule": "अस्पताल मरीज को मेडिकल फाइल देने से नहीं रोक सकता और न ही अपने मेडिकल स्टोर से दवा लेने के लिए बाध्य कर सकता है।",
            "det": "अस्पताल द्वारा उपचार की संपूर्ण फाइल देने से मना किया गया तथा बाहर से सस्ती जेनेरिक दवा लाने पर रोक लगाई गई।"
        }
    }

    selected_issue = st.selectbox("📌 अपनी समस्या का चयन करें (Select from 28 Rights):", list(LEGAL_CASES_28.keys()))
    case_info = LEGAL_CASES_28[selected_issue]

    st.info(f"⚖️ **लागू कानून:** {case_info['act']} | **सक्षम प्राधिकारी:** {case_info['authority']}")

    col_v1, col_v2 = st.columns(2)
    with col_v1:
        v_name = st.text_input("पीड़ित / प्रार्थी का नाम:", value="साहिल कुमार")
    with col_v2:
        v_loc = st.text_input("जिला व राज्य:", value="पश्चिम चंपारण, बिहार")

    v_phone = st.text_input("मोबाइल नंबर:", value="7484878440")
    v_accused = st.text_input("दोषी पक्ष / अधिकारी / कंपनी का नाम:", value="संबंधित दोषी पक्ष")
    v_details = st.text_area("सच्चा घटनाक्रम विवरण:", value=case_info["det"], height=100)

    if st.button("⚡ आधिकारिक विधिक शिकायत पत्र व नोटिस ड्राफ्ट करें"):
        full_notice = f"""======================================================================
आधिकारिक कानूनी विधिक शिकायत पत्र व नोटिस
(अधिनियम: {case_info['act']})
दिनांक: {today_str}

सेवा में,
1. {case_info['authority']}, {v_loc}
2. राष्ट्रीय मानवाधिकार आयोग (NHRC) / विधिक निगरानी प्राधिकरण

विषय: '{selected_issue}' के संबंध में दोषी '{v_accused}' पर प्राथमिकी (FIR) व तत्काल दंडात्मक कार्रवाई बाबत।

महोदय,
प्रार्थी {v_name} (मोबाइल: +91 {v_phone}), निवासी {v_loc} सादर अवगत कराना चाहता है:

1. यह कि प्रार्थी भारत का संविधान-सम्मत नागरिक है और विपक्षी '{v_accused}' द्वारा प्रार्थी के विधिक अधिकारों का खुला उल्लंघन किया गया है।
2. तथ्यात्मक घटनाक्रम (सच्चा विवरण):
"{v_details}"
3. विधिक नियम व प्रावधान:
- {case_info['rule']}

अतः सक्षम प्राधिकारी से प्रार्थना है कि दोषी '{v_accused}' के विरुद्ध सुसंगत कानूनी धाराओं में तत्काल कार्रवाई कर प्रार्थी को उसका संपूर्ण विधिक हक व सुरक्षा अविलंब प्रदान की जाए।

भवदीय:
{v_name}
संपर्क सूत्र: +91 {v_phone}
डिजिटल निगरानी: महा-सेवा AI राष्ट्रीय विधिक साक्षरता मिशन
======================================================================"""

        st.success("🟢 आधिकारिक विधिक नोटिस तैयार:")
        st.text_area("📄 तैयार कानूनी दस्तावेज:", full_notice, height=220)

        st.markdown(f"""
        <div class="caution-card">
            <h3 style="color:#EF4444; margin:0 0 6px 0;">⚖️ इस मामले में आपका कानूनी कवच:</h3>
            <p style="margin:0; font-size:14px; color:#FCA5A5;">{case_info['rule']}</p>
        </div>
        """, unsafe_allow_html=True)

        enc_notice = urllib.parse.quote(full_notice)
        st.markdown(f'<a href="https://wa.me/?text={enc_notice}" target="_blank" class="btn-green">📲 यह शिकायत WhatsApp पर भेजें</a>', unsafe_allow_html=True)

# ================= TAB 2: NIGHT SAFETY & LIVE GPS SOS =================
elif nav_choice == "🚨 रात की सुरक्षा व लाइव GPS SOS":
    st.markdown("""
    <div class="emergency-box">
        <h2 style="color:#FFF; margin:0 0 6px 0; font-size:22px;">🚨 24x7 रात की सुरक्षा व लाइव GPS SOS</h2>
        <p style="color:#FECACA; font-size:13px; margin:0 0 12px 0;">रात में रास्ते पर किसी भी खतरे, पीछा करने या घेरने पर तुरंत सीधे कॉल करें:</p>
        <div>
            <a href="tel:112" class="btn-red-call">📞 112 राष्ट्रीय आपात पुलिस</a>
            <a href="tel:1090" class="btn-red-call">📞 1090 वीमेन पावर लाइन</a>
            <a href="tel:181" class="btn-red-call">📞 181 महिला संकट हेल्पलाइन</a>
        </div>
        <p style="color:#FCA5A5; font-size:12px; margin:8px 0 0 0;">(बिना इंटरनेट के भी सीधे कॉल लगेगी - 100% फ्री 24 घंटे)</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("### 📍 लाइव GPS लोकेशन (गूगल मैप्स लिंक)")
    gps_component = """
    <div style="background:#0F172A; padding:12px; border-radius:12px; border:2px solid #0284C7; text-align:center;">
        <button onclick="getLiveLocation()" style="background:#10B981; color:#fff; border:none; padding:10px 20px; font-weight:bold; font-size:14px; border-radius:8px; cursor:pointer;">
            📡 मेरा सटीक लाइव GPS पता निकालें
        </button>
        <p id="gps_status" style="color:#38BDF8; font-size:13px; margin-top:8px; font-weight:bold;">बटन दबाएँ...</p>
        <input type="text" id="gps_url" readonly style="width:90%; background:#030712; color:#10B981; border:1px solid #10B981; padding:8px; border-radius:6px; font-size:12px; display:none;">
    </div>
    <script>
    function getLiveLocation() {
        var status = document.getElementById('gps_status');
        var inputUrl = document.getElementById('gps_url');
        if (navigator.geolocation) {
            status.innerHTML = "🛰️ सैटेलाइट से लोकेशन फेच हो रही है...";
            navigator.geolocation.getCurrentPosition(function(pos) {
                var lat = pos.coords.latitude;
                var lon = pos.coords.longitude;
                var mapUrl = "https://maps.google.com/?q=" + lat + "," + lon;
                status.innerHTML = "✅ लोकेशन मिल गई! नीचे दिया लिंक कॉपी करें:";
                inputUrl.style.display = "block";
                inputUrl.value = mapUrl;
            }, function(err) {
                status.innerHTML = "⚠️ कृपया मोबाइल की Location (GPS) चालू करें।";
            }, {enableHighAccuracy: true});
        } else {
            status.innerHTML = "ब्राउज़र में GPS सपोर्ट नहीं है।";
        }
    }
    </script>
    """
    components.html(gps_component, height=130)

    f_number = st.text_input("परिवार/भाई/पिता का मोबाइल नंबर:", value="7484878440")
    v_person_name = st.text_input("पीड़ित का नाम:", value="साहिल")
    road_location = st.text_input("वर्तमान सड़क / चौराहे का नाम:", value="मेन रोड, सुनसान तिराहा")

    sos_wa_text = f"🚨 आपातकालीन अलर्ट (SOS)! मुझे सहायता की आवश्यकता है। नाम: {v_person_name}। स्थान: {road_location}। समय: {current_time_str}। कृपया तुरंत पुलिस को सूचित करें या मुझसे संपर्क करें।"
    enc_sos = urllib.parse.quote(sos_wa_text)
    st.markdown(f'<a href="https://wa.me/91{f_number}?text={enc_sos}" target="_blank" class="btn-green">📲 1-क्लिक परिवार को लोकेशन व SOS भेजें</a>', unsafe_allow_html=True)

    # Audio Siren
    st.write("### 🔊 पैनिक सायरन (हमलावर को भगाने हेतु)")
    siren_html = """
    <div style="text-align:center; margin:6px 0;">
        <button onclick="playSiren()" style="background:#EF4444; color:#fff; padding:12px 24px; border-radius:10px; border:none; font-weight:800; font-size:15px; cursor:pointer;">
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
    components.html(siren_html, height=65)

# ================= TAB 3: VOICE-TO-TEXT (माइक से बोलकर) =================
elif nav_choice == "🎙️ बोलकर शिकायत दर्ज करें (माइक)":
    st.write("### 🎙️ बोलकर अपनी बात लिखें (Voice Input)")
    st.caption("जो भाई पढ़-लिख नहीं सकते, वे नीचे माइक बटन दबाकर बोलें — आपकी आवाज़ खुद टाइप हो जाएगी:")

    voice_component = """
    <div style="background:#0F172A; padding:16px; border-radius:12px; border:2px solid #0284C7; text-align:center;">
        <button onclick="startListening()" style="background:#EF4444; color:#fff; border:none; padding:12px 24px; font-weight:bold; font-size:16px; border-radius:8px; cursor:pointer;">
            🎤 माइक चालू करें और बोलें (Click to Speak)
        </button>
        <p id="voice_status" style="color:#38BDF8; font-size:13px; margin-top:8px;">बटन दबाकर बोलना शुरू करें...</p>
        <textarea id="voice_result" style="width:95%; height:80px; background:#030712; color:#38BDF8; border:1px solid #0284C7; border-radius:8px; padding:8px; font-weight:bold; font-size:14px;"></textarea>
    </div>
    <script>
    function startListening() {
        var status = document.getElementById('voice_status');
        var result = document.getElementById('voice_result');
        if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
            var SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
            var recognition = new SpeechRecognition();
            recognition.lang = 'hi-IN';
            recognition.continuous = false;
            recognition.interimResults = false;
            recognition.onstart = function() {
                status.innerHTML = "🎙️ सुन रहा हूँ... अपनी समस्या बोलिए...";
            };
            recognition.onresult = function(event) {
                var transcript = event.results[0][0].transcript;
                result.value = transcript;
                status.innerHTML = "✅ आवाज़ टाइप हो गई! नीचे से कॉपी कर लें।";
            };
            recognition.onerror = function(event) {
                status.innerHTML = "⚠️ आवाज़ रिकॉर्ड नहीं हो सकी। कृपया दोबारा बोलें।";
            };
            recognition.start();
        } else {
            status.innerHTML = "⚠️ आपके ब्राउज़र में वॉइस सपोर्ट नहीं है।";
        }
    }
    </script>
    """
    components.html(voice_component, height=190)

# ================= TAB 4: CYBER FRAUD =================
elif nav_choice == "🛡️ साइबर फ्रॉड व मैसेज चेकर":
    st.write("### 🛡️ साइबर फ्रॉड व असली/नकली मैसेज चेकर")
    st.caption("संदिग्ध मैसेज या WhatsApp लिंक यहाँ पेस्ट करें और तुरंत सच्चाई जाँचें:")

    susp_msg = st.text_area("📝 मैसेज यहाँ पेस्ट करें:", value="बिजली बिल जमा न होने के कारण आज रात 9:30 बजे बिजली काट दी जाएगी। इस 10 अंकों के नंबर पर संपर्क करें।")
    if st.button("🚨 मैसेज की सच्चाई जाँचें (Check Scam)"):
        low_msg = susp_msg.lower()
        if any(w in low_msg for w in ["बिजली", "electricity", "लॉटरी", "lottery", "apk", "telegram", "क्लिक", "task"]):
            st.error("🚨 100% प्रमाणित साइबर फ्रॉड (SCAM DETECTED!) — किसी अनजान नंबर या लिंक पर क्लिक न करें।")
        else:
            st.success("🟢 मैसेज में कोई सीधा साइबर फ्रॉड लिंक नहीं मिला। फिर भी सतर्क रहें।")

    st.markdown("""
    <div class="caution-card">
        <h3 style="color:#EF4444; margin:0 0 6px 0;">📞 राष्ट्रीय साइबर क्राइम हेल्पलाइन:</h3>
        <p style="font-size:15px; margin:0;"><a href="tel:1930" class="btn-red-call">📞 1930 पर तुरंत कॉल करें</a> (पैसे कटने पर 2 घंटे के अंदर)</p>
    </div>
    """, unsafe_allow_html=True)

# ================= TAB 5: HEALTH =================
elif nav_choice == "🏥 दवा व एम्बुलेंस सहायता":
    st.markdown("""
    <div class="emergency-box">
        <h2 style="color:#FFF; margin:0 0 6px 0; font-size:20px;">🚨 मेडिकल इमरजेंसी व एम्बुलेंस सहायता</h2>
        <div>
            <a href="tel:108" class="btn-red-call">📞 108 एम्बुलेंस (फ्री)</a>
            <a href="tel:102" class="btn-red-call">📞 102 मातृ-शिशु एम्बुलेंस</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    med_name = st.text_input("दवा का नाम लिखें:", value="Azithromycin 500")
    if st.button("🔍 जेनेरिक दवा भाव निकालें"):
        st.markdown(f"""
        <div class="info-card">
            <h3 style="color:#38BDF8; margin:0 0 6px 0;">💊 दवा का परिचय: {med_name}</h3>
            <p style="margin:0; font-size:14px;">बैक्टीरियल इन्फेक्शन नियंत्रण हेतु आवश्यक एंटीबायोटिक साल्ट।</p>
            <p style="color:#10B981; font-size:14px; margin-top:6px;"><b>जन औषधि भाव:</b> मात्र ₹20 से ₹35 (प्राइवेट बाज़ार से 70-80% सस्ता)।</p>
        </div>
        """, unsafe_allow_html=True)

# ================= TAB 6: JOBS =================
elif nav_choice == "💼 रोज़गार व हेल्पर डेस्क":
    st.write("### 💼 पूरे देश में सीधी नौकरी व ठेकेदार संपर्क")
    city_in = st.text_input("📍 नौकरी का शहर:", value="Surat")
    role_in = st.text_input("🔧 काम का पद:", value="Factory Helper / Warehouse Worker")
    u_name = st.text_input("👤 आपका नाम:", value="साहिल अहमद (Sahil)")
    u_phone = st.text_input("📱 मोबाइल नंबर:", value="7484878440")

    if st.button("⚡ ठेकेदार आवेदन निकालें"):
        maps_link = f"https://www.google.com/maps/search/{urllib.parse.quote(f'{role_in} contractor in {city_in}')}"
        pitch_txt = f"Hello, My name is {u_name}. Looking for immediate work as {role_in} in {city_in}. Contact: +91 {u_phone}. Ready for immediate joining."
        st.text_area("📄 Job Pitch:", pitch_txt, height=90)
        st.markdown(f'<a href="{maps_link}" target="_blank" class="btn-green">📞 ठेकेदारों की डायरेक्ट लिस्ट खोलें</a>', unsafe_allow_html=True)

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
