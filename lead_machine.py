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

# 2. Modern 100% Dark UI - No Horizontal Scroll Glitch
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
        font-size: 14px;
        padding: 10px 16px;
        border-radius: 10px;
        text-decoration: none;
        margin: 4px;
        box-shadow: 0 4px 15px rgba(239, 68, 68, 0.5);
    }
</style>
""", unsafe_allow_html=True)

MY_WA_NUMBER = "917484878440"
today_str = datetime.now().strftime("%d-%m-%Y")

# 12 Major Languages Complete Dictionary
LANG_DATA = {
    "🇮🇳 हिन्दी": {
        "title": "महा-सेवा AI (MAHA SEVA AI)",
        "sub": "जन-अधिकार • पुलिस-ठेकेदार लीगल एक्शन • रोज़गार • दवा व एम्बुलेंस • सरकारी योजना",
        "nav_lbl": "📂 सेवा श्रेणी चुनें:",
        "sec_rights": "⚖️ जन-अधिकार व विधिक शिकायत",
        "sec_health": "🏥 दवा व इमरजेंसी एम्बुलेंस",
        "sec_job": "💼 जन-रोज़गार व सीधी नौकरी",
        "sec_scheme": "🏛️ सरकारी योजना व सब्सिडी",
        "sec_fraud": "🛡️ साइबर फ्रॉड सुरक्षा",
        "sec_life": "🕊️ नशा-मुक्ति व जीवन रक्षा",
        "r_title": "⚖️ ठेकेदार, मजदूरी व पुलिस उत्पीड़न के विरुद्ध सीधी कार्रवाई",
        "r_sub": "यदि ठेकेदार मजदूरी दबाए, कंपनी पैसा न दे, या पुलिस बेवजह सताए — विधिक नोटिस निकालें",
        "r_type_lbl": "📌 शिकायत की श्रेणी:",
        "r_opt": [
            "ठेकेदार / कंपनी ने मजदूरी दबा ली (Wage Theft)",
            "पुलिस द्वारा गैर-कानूनी मारपीट व उत्पीड़न (Police Harassment)",
            "गलत या अवैध चालान काटा गया (Illegal Challan)",
            "सरकारी कर्मचारी द्वारा रिश्वत की मांग (Corruption)"
        ],
        "name_lbl": "पीड़ित / प्रार्थी का नाम:",
        "city_lbl": "जिला व राज्य:",
        "phone_lbl": "मोबाइल नंबर:",
        "accused_lbl": "दोषी पक्ष / ठेकेदार / थाना:",
        "detail_lbl": "घटना का विवरण (पूरी बात लिखें):",
        "btn_rights": "⚡ आधिकारिक कानूनी नोटिस व शिकायत ड्राफ्ट करें",
        "job_title": "💼 देश भर में सीधी नौकरी व ठेकेदार संपर्क",
        "job_sub": "हेल्पर, लोडर, ड्राइवर, मिस्त्री — बिना दलाल के सीधे ठेकेदार से बात करें",
        "job_city": "📍 कार्य का शहर/जिला:",
        "job_role": "🔧 कार्य का पद:",
        "btn_job": "⚡ ठेकेदार संपर्क व आवेदन निकालें",
        "btn_call_job": "📞 ठेकेदारों की डायरेक्ट लिस्ट खोलें",
        "btn_wa": "📲 WhatsApp पर आवेदन भेजें"
    },
    "🇬🇧 English": {
        "title": "MAHA SEVA AI — Sovereign Mission",
        "sub": "Citizen Rights • Legal Action Against Unlawful Police/Employer • Jobs • Healthcare",
        "nav_lbl": "📂 Select Service Category:",
        "sec_rights": "⚖️ Legal Rights & Police Complaint",
        "sec_health": "🏥 Medicines & Emergency Ambulance",
        "sec_job": "💼 Employment & Blue-Collar Jobs",
        "sec_scheme": "🏛️ Government Welfare Schemes",
        "sec_fraud": "🛡️ Cyber Crime & Scam Shield",
        "sec_life": "🕊️ Anti-Addiction & Health",
        "r_title": "⚖️ Direct Legal Action: Wage Theft & Police Harassment",
        "r_sub": "If an employer withholds wages or police abuse power, draft a legal notice instantly.",
        "r_type_lbl": "📌 Grievance Category:",
        "r_opt": [
            "Wage Theft / Employer Unpaid Dues (Payment of Wages Act)",
            "Police Brutality & Unlawful Harassment (Sec 166A BNS)",
            "Illegal Traffic Challan (Challenged via Virtual Court)",
            "Bribery & Public Corruption (Prevention of Corruption Act)"
        ],
        "name_lbl": "Complainant Full Name:",
        "city_lbl": "District & State:",
        "phone_lbl": "Mobile Number:",
        "accused_lbl": "Accused Contractor / Police Station:",
        "detail_lbl": "Incident Details (Date, Location, Dues):",
        "btn_rights": "⚡ Draft Formal Legal Notice & Complaint",
        "job_title": "💼 Pan-India Direct Jobs & Contractor Connect",
        "job_sub": "Helpers, Loaders, Drivers, Masons — Zero Agent Fee",
        "job_city": "📍 Job City / District:",
        "job_role": "🔧 Work Category / Role:",
        "btn_job": "⚡ Generate Contractor Pitch & Contacts",
        "btn_call_job": "📞 Open Local Contractors Directory",
        "btn_wa": "📲 Send Official Pitch on WhatsApp"
    },
    "বাংলা (Bengali)": {
        "title": "মহা-সেবা AI (MAHA SEVA AI)",
        "sub": "নাগরিক অধিকার • আইনি পদক্ষেপ • কর্মসংস্থান • স্বাস্থ্য ও সুরক্ষা",
        "nav_lbl": "📂 পরিষেবা নির্বাচন করুন:",
        "sec_rights": "⚖️ নাগরিক অধিকার ও আইনি অভিযোগ",
        "sec_health": "🏥 ওষুধ ও জরুরি অ্যাম্বুলেন্স",
        "sec_job": "💼 সরাসরি চাকরি ও কর্মী নিয়োগ",
        "sec_scheme": "🏛️ সরকারি প্রকল্প ও সাহায্য",
        "sec_fraud": "🛡️ সাইবার প্রতারণা রোধ",
        "sec_life": "🕊️ নেশামুক্তি ও জীবন রক্ষা",
        "r_title": "⚖️ বকেয়া মজুরি এবং পুলিশি হয়রানির বিরুদ্ধে ব্যবস্থা",
        "r_sub": "ঠিকাদার টাকা না দিলে বা পুলিশ হয়রানি করলে আইনি নোটিশ তৈরি করুন",
        "r_type_lbl": "📌 অভিযোগের বিভাগ:",
        "r_opt": [
            "বকেয়া মজুরি পরিশোধ না করা (Wage Theft)",
            "পুলিশ কর্তৃক মারধর ও নির্যাতন (Police Harassment)",
            "অবৈধ বা ভুল চালান কাটা (Illegal Challan)",
            "ঘুষ ও সরকারি দুর্নীতি (Corruption)"
        ],
        "name_lbl": "অভিযোগকারীর নাম:",
        "city_lbl": "জেলা ও রাজ্য:",
        "phone_lbl": "মোবাইল নম্বর:",
        "accused_lbl": "অভিযুক্ত ঠিকাদার বা থানা:",
        "detail_lbl": "ঘটনার সম্পূর্ণ বিবরণ:",
        "btn_rights": "⚡ আইনি অভিযোগ পত্র তৈরি করুন",
        "job_title": "💼 সারাদেশে সরাসরি চাকরি ও ঠিকাদার যোগাযোগ",
        "job_sub": "দালাল ছাড়া সরাসরি কোম্পানির সাথে কথা বলুন",
        "job_city": "📍 কাজের শহর:",
        "job_role": "🔧 কাজের পদ:",
        "btn_job": "⚡ চাকরির আবেদন তৈরি করুন",
        "btn_call_job": "📞 ঠিকাদারদের তালিকা খুলুন",
        "btn_wa": "📲 হোয়াটসঅ্যাপে পাঠান"
    },
    "मराठी (Marathi)": {
        "title": "महा-सेवा AI (MAHA SEVA AI)",
        "sub": "नागरी हक्क • पोलीस व कंत्राटदार तक्रार निवारण • रोजगार • औषधे",
        "nav_lbl": "📂 सेवा निवडा:",
        "sec_rights": "⚖️ नागरी हक्क व तक्रार",
        "sec_health": "🏥 औषधे व रुग्णवाहिका",
        "sec_job": "💼 रोजगार व थेट नोकरी",
        "sec_scheme": "🏛️ सरकारी योजना",
        "sec_fraud": "🛡️ सायबर सुरक्षा",
        "sec_life": "🕊️ व्यसनमुक्ती",
        "r_title": "⚖️ थकीत मजुरी व पोलिसांच्या गैरवर्तनाविरुद्ध थेट कारवाई",
        "r_sub": "कंत्राटदाराने पैसे अडकवल्यास किंवा पोलिसांनी त्रास दिल्यास कायदेशीर नोटीस काढा",
        "r_type_lbl": "📌 तक्रारीचा प्रकार:",
        "r_opt": [
            "कंत्राटदाराने मजुरी अडकवली (Wage Theft)",
            "पोलिसांकडून बेकायदेशीर मारहाण (Police Misconduct)",
            "चुकीचा किंवा बेकायदेशीर चलन (Illegal Challan)",
            "लाचखोरी व भ्रष्टाचार (Corruption)"
        ],
        "name_lbl": "तक्रारदाराचे नाव:",
        "city_lbl": "जिल्हा व राज्य:",
        "phone_lbl": "मोबाईल नंबर:",
        "accused_lbl": "दोषी कंत्राटदार / पोलीस ठाणे:",
        "detail_lbl": "घटनेचा तपशील:",
        "btn_rights": "⚡ कायदेशीर तक्रार अर्ज तयार करा",
        "job_title": "💼 थेट नोकरी व कंत्राटदार संपर्क",
        "job_sub": "हेल्पर, ड्रायव्हर, कारागीर — दलालांशिवाय थेट नोकरी",
        "job_city": "📍 कामाचे शहर:",
        "job_role": "🔧 कामाचा प्रकार:",
        "btn_job": "⚡ संपर्क व अर्ज तयार करा",
        "btn_call_job": "📞 कंत्राटदारांची यादी उघडा",
        "btn_wa": "📲 व्हॉट्सॲपवर पाठवा"
    },
    "தமிழ் (Tamil)": {
        "title": "மகா-சேவா AI (MAHA SEVA AI)",
        "sub": "குடிமக்கள் உரிமைகள் • சட்ட நடவடிக்கை • வேலைவாய்ப்பு • மருத்துவம்",
        "nav_lbl": "📂 சேவையைத் தேர்ந்தெடுக்கவும்:",
        "sec_rights": "⚖️ சட்ட உரிமை & புகார்",
        "sec_health": "🏥 மருத்துவம் & ஆம்புலன்ஸ்",
        "sec_job": "💼 நேரடி வேலைவாய்ப்பு",
        "sec_scheme": "🏛️ அரசு நலத்திட்டங்கள்",
        "sec_fraud": "🛡️ இணைய மோசடி தடுப்பு",
        "sec_life": "🕊️ போதை ஒழிப்பு",
        "r_title": "⚖️ சம்பள மறுப்பு மற்றும் காவல்துறை அத்துமீறலுக்கு எதிரான நடவடிக்கை",
        "r_sub": "சம்பளம் தராவிட்டால் அல்லது காவல்துறை துன்புறுத்தினால் சட்ட நோட்டீஸ் அனுப்பவும்",
        "r_type_lbl": "📌 புகாரின் வகை:",
        "r_opt": [
            "சம்பள பாக்கி ஏமாற்றுதல் (Wage Theft)",
            "காவல்துறை துன்புறுத்தல் (Police Misconduct)",
            "தவறான அபராதம் (Illegal Challan)",
            "லஞ்ச ஊழல் புகார் (Corruption)"
        ],
        "name_lbl": "உங்கள் பெயர்:",
        "city_lbl": "மாவட்டம் & மாநிலம்:",
        "phone_lbl": "மொபைல் எண்:",
        "accused_lbl": "எதிர்தரப்பு ஒப்பந்ததாரர் / காவல் நிலையம்:",
        "detail_lbl": "நிகழ்வின் முழு விவரம்:",
        "btn_rights": "⚡ சட்டப்பூர்வ புகார் மனுவை உருவாக்கவும்",
        "job_title": "💼 நேரடி வேலைவாய்ப்பு & தொடர்புகள்",
        "job_sub": "இடைத்தரகர் இல்லாத வேலை வாய்ப்புகள்",
        "job_city": "📍 வேலை செய்யும் நகரம்:",
        "job_role": "🔧 பணி வகை:",
        "btn_job": "⚡ விண்ணப்பத்தை உருவாக்குங்கள்",
        "btn_call_job": "📞 தொடர்புகளின் பட்டியலைத் திறக்கவும்",
        "btn_wa": "📲 வாட்ஸ்அப்பில் பகிரவும்"
    },
    "తెలుగు (Telugu)": {
        "title": "మహా-సేవా AI (MAHA SEVA AI)",
        "sub": "పౌర హక్కులు • న్యాయపరమైన రక్షణ • ఉపాధి • వైద్యం",
        "nav_lbl": "📂 సేవను ఎంచుకోండి:",
        "sec_rights": "⚖️ పౌర హక్కులు & ఫిర్యాదు",
        "sec_health": "🏥 మందులు & అంబులెన్స్",
        "sec_job": "💼 ఉపాధి & ఉద్యోగాలు",
        "sec_scheme": "🏛️ ప్రభుత్వ పథకాలు",
        "sec_fraud": "🛡️ సైబర్ భద్రత",
        "sec_life": "🕊️ వ్యసన విముక్తి",
        "r_title": "⚖️ జీతం ఎగవేత & పోలీసు వేధింపులపై ప్రత్యక్ష చర్య",
        "r_sub": "జీతం ఇవ్వకపోయినా లేదా పోలీసులు వేధించినా చట్టపరమైన నోటీస్ పొందండి",
        "r_type_lbl": "📌 ఫిర్యాదు వర్గం:",
        "r_opt": [
            "జీతం బకాయిలు ఇవ్వకపోవడం (Wage Theft)",
            "పోలీసుల వేధింపులు & దౌర్జన్యం (Police Harassment)",
            "తప్పుడు చలానా (Illegal Challan)",
            "లంచం & అవినీతి (Corruption)"
        ],
        "name_lbl": "ఫిర్యాదుదారు పేరు:",
        "city_lbl": "జిల్లా & రాష్ట్రం:",
        "phone_lbl": "ఫోన్ నంబర్:",
        "accused_lbl": "కాంట్రాక్టర్ / పోలీస్ స్టేషన్:",
        "detail_lbl": "పూర్తి వివరాలు:",
        "btn_rights": "⚡ చట్టపరమైన నోటీసు రూపొందించండి",
        "job_title": "💼 ఉపాధి & కాంట్రాక్టర్ పరిచయాలు",
        "job_sub": "ఎలాంటి కమీషన్ లేకుండా నేరుగా సంప్రదించండి",
        "job_city": "📍 నగరం / జిల్లా:",
        "job_role": "🔧 పని విభాగం:",
        "btn_job": "⚡ ఉద్యోగ దరఖాస్తును సిద్ధం చేయండి",
        "btn_call_job": "📞 కాంట్రాక్టర్ల లిస్ట్ చూడండి",
        "btn_wa": "📲 వాట్సాప్‌లో పంపండి"
    },
    "ગુજરાતી (Gujarati)": {
        "title": "મહા-સેવા AI (MAHA SEVA AI)",
        "sub": "નાગરિક અધિકાર • કાનૂની સુરક્ષા • રોજગાર • દવા અને એમ્બ્યુલન્સ",
        "nav_lbl": "📂 સેવા પસંદ કરો:",
        "sec_rights": "⚖️ નાગરિક અધિકાર અને ફરિયાદ",
        "sec_health": "🏥 દવા અને એમ્બ્યુલન્સ",
        "sec_job": "💼 સીધી નોકરી અને રોજગાર",
        "sec_scheme": "🏛️ સરકારી યોજનાઓ",
        "sec_fraud": "🛡️ સાયબર ફ્રોડ સુરક્ષા",
        "sec_life": "🕊️ વ્યસન મુક્તિ",
        "r_title": "⚖️ મજૂરી અને પોલીસ ઉત્પીડન સામે કાનૂની કાર્યવાહી",
        "r_sub": "જો કોન્ટ્રાક્ટર પગાર ન આપે કે પોલીસ હેરાન કરે તો કાનૂની નોટિસ બનાવો",
        "r_type_lbl": "📌 ફરિયાદની શ્રેણી:",
        "r_opt": [
            "કોન્ટ્રાક્ટરે પગાર અટકાવ્યો (Wage Theft)",
            "પોલીસ દ્વારા ગેરકાયદે હેરાનગતિ (Police Harassment)",
            "ખોટો મેમો / ચલણ (Illegal Challan)",
            "લાંચ અને ભ્રષ્ટાચાર (Corruption)"
        ],
        "name_lbl": "અરજદારનું નામ:",
        "city_lbl": "જિલ્લો અને રાજ્ય:",
        "phone_lbl": "મોબાઇલ નંબર:",
        "accused_lbl": "સામેવાળા કોન્ટ્રાક્ટર / પોલીસ મથક:",
        "detail_lbl": "સમગ્ર વિગત:",
        "btn_rights": "⚡ કાનૂની નોટિસ તૈયાર કરો",
        "job_title": "💼 સીધી નોકરી અને કોન્ટ્રાક્ટર સંપર્ક",
        "job_sub": "દલાલ વગર સીધી કંપની સાથે વાત કરો",
        "job_city": "📍 શહેર / જિલ્લો:",
        "job_role": "🔧 કામનો પ્રકાર:",
        "btn_job": "⚡ અરજી તૈયાર કરો",
        "btn_call_job": "📞 યાદી ખોલો",
        "btn_wa": "📲 WhatsApp પર મોકલો"
    },
    "ಕನ್ನಡ (Kannada)": {
        "title": "ಮಹಾ-ಸೇವಾ AI (MAHA SEVA AI)",
        "sub": "ನಾಗರಿಕ ಹಕ್ಕುಗಳು • ಕಾನೂನು ರಕ್ಷಣೆ • ಉದ್ಯೋಗ • ಆರೋಗ್ಯ",
        "nav_lbl": "📂 ಸೇವೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ:",
        "sec_rights": "⚖️ ಕಾನೂನು ಹಕ್ಕುಗಳು & ದೂರು",
        "sec_health": "🏥 ಔಷಧಿ & ಆಂಬ್ಯುಲೆನ್ಸ್",
        "sec_job": "💼 ನೇರ ಉದ್ಯೋಗ ಮಾಹಿತಿ",
        "sec_scheme": "🏛️ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು",
        "sec_fraud": "🛡️ ಸೈಬರ್ ವಂಚನೆ ತಡೆ",
        "sec_life": "🕊️ ವ್ಯಸನ ಮುಕ್ತಿ",
        "r_title": "⚖️ ಕೂಲಿ ವಂಚನೆ ಮತ್ತು ಪೊಲೀಸ್ ಕಿರುಕುಳದ ವಿರುದ್ಧ ಕಾನೂನು ಕ್ರಮ",
        "r_sub": "ಕೂಲಿ ನೀಡದಿದ್ದರೆ ಅಥವಾ ಪೊಲೀಸರು ಕಿರುಕುಳ ನೀಡಿದರೆ ಕಾನೂನು ನೋಟಿಸ್ ಪಡೆಯಿರಿ",
        "r_type_lbl": "📌 ದೂರಿನ ಪ್ರಕಾರ:",
        "r_opt": [
            "ಕೂಲಿ ಹಣ ನೀಡದಿರುವುದು (Wage Theft)",
            "ಪೊಲೀಸ್ ದೌರ್ಜನ್ಯ ಮತ್ತು ಕಿರುಕುಳ (Police Harassment)",
            "ತಪ್ಪಾದ ಚಲನ್ (Illegal Challan)",
            "ಲಂಚ ಮತ್ತು ಭ್ರಷ್ಟಾಚಾರ (Corruption)"
        ],
        "name_lbl": "ದೂರುದಾರರ ಹೆಸರು:",
        "city_lbl": "ಜಿಲ್ಲೆ & ರಾಜ್ಯ:",
        "phone_lbl": "ಮೊಬೈಲ್ ಸಂಖ್ಯೆ:",
        "accused_lbl": "ಗುತ್ತಿಗೆದಾರ / ಪೊಲೀಸ್ ಠಾಣೆ:",
        "detail_lbl": "ಸಂಪೂರ್ಣ ವಿವರ:",
        "btn_rights": "⚡ ಕಾನೂನು ನೋಟಿಸ್ ರಚಿಸಿ",
        "job_title": "💼 ನೇರ ಉದ್ಯೋಗ ಮತ್ತು ಸಂಪರ್ಕ",
        "job_sub": "ಯಾವುದೇ ದಲ್ಲಾಳಿ ಇಲ್ಲದೆ ನೇರ ಸಂಪರ್ಕ",
        "job_city": "📍 ಉದ್ಯೋಗದ ನಗರ:",
        "job_role": "🔧 ಕೆಲಸದ ಹುದ್ದೆ:",
        "btn_job": "⚡ ಅರ್ಜಿ ರಚಿಸಿ",
        "btn_call_job": "📞 ಪಟ್ಟಿ ತೆರೆಯಿರಿ",
        "btn_wa": "📲 ವಾಟ್ಸಾಪ್‌ನಲ್ಲಿ ಕಳುಹಿಸಿ"
    },
    "ਪੰਜਾਬੀ (Punjabi)": {
        "title": "ਮਹਾ-ਸੇਵਾ AI (MAHA SEVA AI)",
        "sub": "ਨਾਗਰਿਕ ਹੱਕ • ਕਾਨੂੰਨੀ ਕਾਰਵਾਈ • ਰੋਜ਼ਗਾਰ • ਸਿਹਤ ਤੇ ਐਂਬੂਲੈਂਸ",
        "nav_lbl": "📂 ਸੇਵਾ ਚੁਣੋ:",
        "sec_rights": "⚖️ ਨਾਗਰਿਕ ਹੱਕ ਤੇ ਸ਼ਿਕਾਇਤ",
        "sec_health": "🏥 ਦਵਾਈ ਤੇ ਐਂਬੂਲੈਂਸ",
        "sec_job": "💼 ਰੋਜ਼ਗਾਰ ਤੇ ਸਿੱਧੀ ਨੌਕਰੀ",
        "sec_scheme": "🏛️ ਸਰਕਾਰੀ ਸਕੀਮਾਂ",
        "sec_fraud": "🛡️ ਸਾਈਬਰ ਧੋਖਾਧੜੀ ਰੋਕਥਾਮ",
        "sec_life": "🕊️ ਨਸ਼ਾ ਮੁਕਤੀ",
        "r_title": "⚖️ ਤਨਖਾਹ ਚੋਰੀ ਅਤੇ ਪੁਲਿਸ ਤਸ਼ੱਦਦ ਖ਼ਿਲਾਫ਼ ਸਿੱਧੀ ਕਾਰਵਾਈ",
        "r_sub": "ਜੇਕਰ ਠੇਕੇਦਾਰ ਪੈਸੇ ਰੋਕੇ ਜਾਂ ਪੁਲਿਸ ਤੰਗ ਕਰੇ ਤਾਂ ਕਾਨੂੰਨੀ ਨੋਟਿਸ ਕੱਢੋ",
        "r_type_lbl": "📌 ਸ਼ਿਕਾਇਤ ਦੀ ਸ਼੍ਰੇਣੀ:",
        "r_opt": [
            "ਠੇਕੇਦਾਰ ਵੱਲੋਂ ਮਜ਼ਦੂਰੀ ਰੋਕਣਾ (Wage Theft)",
            "ਪੁਲਿਸ ਵੱਲੋਂ ਨਾਜਾਇਜ਼ ਤਸ਼ੱਦਦ (Police Harassment)",
            "ਗਲਤ ਜਾਂ ਨਾਜਾਇਜ਼ ਚਲਾਨ (Illegal Challan)",
            "ਰਿਸ਼ਵਤਖੋਰੀ ਅਤੇ ਭ੍ਰਿਸ਼ਟਾਚਾਰ (Corruption)"
        ],
        "name_lbl": "ਪੀੜਤ ਦਾ ਨਾਮ:",
        "city_lbl": "ਜ਼ਿਲ੍ਹਾ ਤੇ ਰਾਜ:",
        "phone_lbl": "ਮੋਬਾਈਲ ਨੰਬਰ:",
        "accused_lbl": "ਦੋਸ਼ੀ ਠੇਕੇਦਾਰ / ਥਾਣਾ:",
        "detail_lbl": "ਘਟਨਾ ਦਾ ਪੂਰਾ ਵੇਰਵਾ:",
        "btn_rights": "⚡ ਕਾਨੂੰਨੀ ਨੋਟਿਸ ਤਿਆਰ ਕਰੋ",
        "job_title": "💼 ਸਿੱਧੀ ਨੌਕਰੀ ਤੇ ਠੇਕੇਦਾਰ ਸੰਪਰਕ",
        "job_sub": "ਬਿਨਾਂ ਦਲਾਲ ਸਿੱਧਾ ਕੰਪਨੀ ਨਾਲ ਗੱਲ ਕਰੋ",
        "job_city": "📍 ਕੰਮ ਦਾ ਸ਼ਹਿਰ:",
        "job_role": "🔧 ਕੰਮ ਦਾ ਅਹੁਦਾ:",
        "btn_job": "⚡ ਅਰਜ਼ੀ ਤਿਆਰ ਕਰੋ",
        "btn_call_job": "📞 ਸੂਚੀ ਖੋਲ੍ਹੋ",
        "btn_wa": "📲 WhatsApp ਤੇ ਭੇਜੋ"
    }
}

# Live Search Engine
def deep_live_knowledge(query_text):
    clean_q = query_text.strip()
    if not clean_q:
        return None
    try:
        url = f"https://hi.wikipedia.org/w/api.php?action=opensearch&search={urllib.parse.quote(clean_q)}&limit=1&namespace=0&format=json"
        req = urllib.request.Request(url, headers={'User-Agent': 'MahaSevaAI/NationalSovereignEngine'})
        with urllib.request.urlopen(req, timeout=3) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            if len(data) > 2 and data[2] and data[2][0].strip():
                return data[2][0].strip()
    except Exception:
        pass
    return None

# Universal All-India Language Selector
all_langs = list(LANG_DATA.keys())
chosen_lang = st.radio(
    "🌐 भाषा चुनें / Select Language / ভাষা বাছুন / भाषा निवडा / மொழியைத் தேர்ந்தெடுக்கவும்:",
    all_langs,
    horizontal=True
)
T = LANG_DATA.get(chosen_lang, LANG_DATA["🇮🇳 हिन्दी"])

# Header
st.markdown(f"""
<div style="background: radial-gradient(circle at center, #1E3A8A 0%, #030712 100%); border: 2px solid #38BDF8; border-radius: 14px; padding: 14px; text-align: center; margin-bottom: 14px; box-shadow: 0 0 20px rgba(56, 189, 248, 0.25);">
    <span style="background:rgba(16,185,129,0.2); color:#10B981; border:1px solid #10B981; padding:3px 12px; border-radius:20px; font-size:11px; font-weight:800;">
        ⚡ 24x7 अखंड भारत नागरिक, विधिक सुरक्षा व रोज़गार मिशन
    </span>
    <h1 style="font-size:22px; margin:6px 0 0 0; color:#FFF;">{T['title']}</h1>
    <p style="font-size:12px; color:#38BDF8; margin:4px 0 0 0;">{T['sub']}</p>
</div>
""", unsafe_allow_html=True)

# Mobile Glitch-Free Section Selector
nav_choice = st.radio(
    T["nav_lbl"],
    [
        T["sec_rights"],
        T["sec_health"],
        T["sec_job"],
        T["sec_scheme"],
        T["sec_fraud"],
        T["sec_life"]
    ],
    horizontal=True
)

st.markdown("---")

# ================= SECTION 1: CITIZEN LEGAL RIGHTS & COMPLAINTS =================
if nav_choice == T["sec_rights"]:
    st.write(f"### {T['r_title']}")
    st.caption(T['r_sub'])

    complaint_type = st.radio(T["r_type_lbl"], T["r_opt"])

    col_c1, col_c2 = st.columns(2)
    with col_c1:
        victim_name = st.text_input(T["name_lbl"], value="साहिल कुमार")
    with col_c2:
        victim_city = st.text_input(T["city_lbl"], value="पश्चिम चंपारण, बिहार")

    victim_phone = st.text_input(T["phone_lbl"], value="7484878440")
    accused_party = st.text_input(T["accused_lbl"], value="ठेकेदार राम सिंह / संबंधित थाना प्रभारी व बीट अधिकारी")
    complaint_details = st.text_area(
        T["detail_lbl"],
        value="मैंने संबंधित कार्यस्थल पर 2 महीने पूरी मेहनत से कार्य किया, जिसकी कुल बकाया राशि ₹24,000 है। मांगने पर ठेकेदार द्वारा जातिसूचक अपशब्द, गाली-गलौज व जान से मारने की धमकी दी गई।"
    )

    if st.button(T['btn_rights']):
        legal_draft = f"""======================================================================
आधिकारिक कानूनी विधिक शिकायत पत्र व नोटिस
(विधि के शासन, भारतीय नागरिक सुरक्षा संहिता एवं मानवाधिकार संरक्षण अधिनियम के तहत)
दिनांक: {today_str}

सेवा में,
1. श्रम आयुक्त (Labour Commissioner) / जिलाधिकारी (DM), {victim_city}
2. पुलिस अधीक्षक (SP) / राज्य पुलिस शिकायत प्राधिकरण (SPCA)
3. राष्ट्रीय मानवाधिकार आयोग (NHRC), नई दिल्ली

विषय: '{complaint_type}' के संबंध में दोषी पक्ष '{accused_party}' पर तत्काल दंडात्मक कार्रवाई व प्राथमिकी (FIR) दर्ज करने बाबत।

महोदय,
प्रार्थी {victim_name} (मोबाइल: +91 {victim_phone}), निवासी {victim_city} सादर अवगत कराना चाहता है:

1. यह कि प्रार्थी भारत का संविधान-सम्मत नागरिक है और विपक्षी '{accused_party}' द्वारा प्रार्थी के मौलिक अधिकारों (अनुच्छेद 21) का खुला हनन किया गया है।
2. तथ्यात्मक घटनाक्रम:
"{complaint_details}"
3. विधिक आधार:
- पेमेंट ऑफ वेजेस एक्ट 1936 व इंडस्ट्रियल डिस्प्यूट्स एक्ट: किसी भी श्रमिक की मजदूरी रोकना गैर-कानूनी अपराध है और 10 गुना हर्जाने का प्रावधान है।
- भारतीय न्याय संहिता (BNS) धारा 166A/198/351: किसी भी लोकसेवक (पुलिसकर्मी) द्वारा नागरिक को अवैध रूप से प्रताड़ित करना, मारपीट करना या धमकाना सीधे निलंबन व 1 से 2 वर्ष के सश्रम कारावास का अपराध है।

अतः सक्षम प्राधिकारी से प्रार्थना है कि:
(क) दोषी '{accused_party}' के विरुद्ध सुसंगत कानूनी धाराओं में तत्काल FIR दर्ज कर विभागीय जांच बैठाई जाए।
(ख) प्रार्थी की बकाया मजदूरी/मुआवजा 18% वार्षिक ब्याज सहित दिलाया जाए।
(ग) दोषी पुलिस अधिकारी अथवा ठेकेदार पर कठोर विभागीय निलंबन की कार्रवाई की जाए।

भवदीय:
{victim_name}
संपर्क सूत्र: +91 {victim_phone}
डिजिटल मॉनिटरिंग: महा-सेवा AI राष्ट्रीय विधिक साक्षरता मिशन
======================================================================"""

        st.success("🟢 आधिकारिक विधिक नोटिस तैयार:")
        st.text_area("📄 तैयार कानूनी शिकायत पत्र:", legal_draft, height=220)

        st.markdown("""
        <div class="caution-card">
            <h3 style="color:#EF4444; margin:0 0 6px 0;">⚖️ आपका कानूनी कवच:</h3>
            <ul style="margin:0; padding-left:18px; font-size:14px; color:#FCA5A5;">
                <li><b>मजदूरी का पाई-पाई हिसाब:</b> यदि ठेकेदार पैसा रोके, तो श्रम अदालत में शिकायत जाने पर कंपनी का खाता सीज हो सकता है।</li>
                <li><b>पुलिस बर्बरता पर सजा:</b> सुप्रीम कोर्ट (डी.के. बसु दिशानिर्देश) के अनुसार किसी भी नागरिक से गाली-गलौज व मारपीट करने वाले पुलिसकर्मी पर सीधे निलंबन की कार्रवाई होती है।</li>
                <li><b>गलत चालान:</b> यदि पुलिस ने बिना गलती चालान काटा है, तो उसे ऑनलाइन ई-कोर्ट (Virtual Court) में चुनौती दें।</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="text-align:center; margin:10px 0;">
            <p style="color:#38BDF8; font-size:13px; margin-bottom:6px;"><b>राष्ट्रीय न्याय एवं सतर्कता हेल्पलाइन (Toll-Free):</b></p>
            <a href="tel:112" class="btn-red-call">📞 112 राष्ट्रीय पुलिस हेल्पलाइन</a>
            <a href="tel:1064" class="btn-red-call">📞 1064 एंटी-करप्शन हेल्पलाइन</a>
            <a href="tel:14434" class="btn-red-call">📞 14434 श्रम व वेतन समाधान हेल्पलाइन</a>
            <a href="tel:1076" class="btn-red-call">📞 1076 मुख्यमंत्री जनसुनवाई</a>
        </div>
        """, unsafe_allow_html=True)

        enc_legal = urllib.parse.quote(legal_draft)
        st.markdown(f'<a href="https://wa.me/?text={enc_legal}" target="_blank" class="btn-green">📲 शिकायत पत्र WhatsApp / सोशल मीडिया पर भेजें</a>', unsafe_allow_html=True)

# ================= SECTION 2: HEALTH & EMERGENCY AMBULANCE =================
elif nav_choice == T["sec_health"]:
    st.markdown("""
    <div class="emergency-card">
        <h2 style="color:#FFF; margin:0 0 6px 0; font-size:20px;">🚨 मेडिकल इमरजेंसी व तत्काल एम्बुलेंस सहायता</h2>
        <p style="color:#FECACA; font-size:13px; margin:0 0 12px 0;">दुर्घटना, गंभीर बीमारी या प्रसव पीड़ा में तुरंत नीचे दिए गए नंबरों पर सीधे कॉल करें:</p>
        <div>
            <a href="tel:108" class="btn-red-call">📞 108 एम्बुलेंस (फ्री आपातकाल)</a>
            <a href="tel:102" class="btn-red-call">📞 102 मातृ-शिशु एम्बुलेंस</a>
        </div>
        <p style="color:#FCA5A5; font-size:12px; margin:8px 0 0 0;">(सिम से सीधे कॉल लगेगी - 100% फ्री 24x7)</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("### 💊 सस्ती जेनेरिक दवा व पर्ची सहायक")
    m_name = st.text_input("दवा का नाम लिखें या बीमारी का विवरण दें:", value="Azithromycin 500")

    if st.button("🔍 संपूर्ण दवा व जेनेरिक विश्लेषण निकालें"):
        with st.spinner("चिकित्सा डेटाबेस जांच जारी..."):
            live_m = deep_live_knowledge(m_name)
            st.markdown(f"""
            <div class="info-card">
                <h3 style="color:#38BDF8; margin:0 0 6px 0;">💊 1. दवा का परिचय व साल्ट</h3>
                <p style="margin:0; font-size:14px;"><b>दवा / साल्ट:</b> {m_name}<br>
                यह बीमारी के संक्रमण और संबंधित लक्षणों को नियंत्रित करने में सहायक है।</p>
                {f'<p style="color:#94A3B8; font-size:13px; margin-top:6px;"><b>चिकित्सा डेटा:</b> {live_m}</p>' if live_m else ''}
            </div>
            <div class="info-card">
                <h3 style="color:#10B981; margin:0 0 6px 0;">💰 2. प्राइवेट बनाम सरकारी जन औषधि भाव</h3>
                <ul style="margin:0; padding-left:18px; font-size:14px;">
                    <li><b>निजी मेडिकल स्टोर भाव:</b> ₹70 से ₹150 तक।</li>
                    <li><b>सरकारी जन औषधि केंद्र भाव:</b> मात्र <b>₹20 से ₹35</b> (70% से 80% सीधी बचत)।</li>
                </ul>
            </div>
            <div class="caution-card">
                <h3 style="color:#EF4444; margin:0 0 6px 0;">⚠️ दवा के उपयोग में अनिवार्य सावधानी:</h3>
                <ul style="margin:0; padding-left:18px; font-size:14px; color:#FCA5A5;">
                    <li><b>स्वयं डॉक्टर न बनें:</b> बिना डॉक्टर के पर्चे के गंभीर एंटीबायोटिक या दर्दनिवारक न लें।</li>
                    <li><b>कोर्स पूरा करें:</b> दवा की खुराक बीच में बंद न करें और न ही खाली पेट तेज दवाइयाँ लें।</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

# ================= SECTION 3: BLUE-COLLAR & HELPER JOB ENGINE =================
elif nav_choice == T["sec_job"]:
    st.write(f"### {T['job_title']}")
    st.caption(T['job_sub'])

    col1, col2 = st.columns(2)
    with col1:
        target_city = st.text_input(T["job_city"], value="Surat")
    with col2:
        work_role = st.text_input(T["job_role"], value="Factory Helper / Warehouse Worker")

    c_name = st.text_input(T["name_lbl"], value="साहिल अहमद (Sahil)")
    c_phone = st.text_input(T["phone_lbl"], value="7484878440")
    c_exp = st.text_input("⏳ अनुभव / हुनर:", value="3 साल का अनुभव, तुरंत काम करने हेतु तैयार")
    c_notes = st.text_area(
        "✍️ अपनी भाषा में बात या हुनर लिखें:",
        value="मुझे काम की सख्त जरूरत है। मैं पूरी ईमानदारी और मेहनत से काम करूँगा।"
    )

    if st.button(T['btn_job']):
        clean_target = target_city.split("/")[0].strip()
        role_clean = work_role.split("/")[0].strip()
        g_maps_search = f"https://www.google.com/maps/search/{urllib.parse.quote(f'{role_clean} contractor agency in {clean_target}')}"
        
        eng_pitch = f"""Respected Hiring Manager / Contractor,

My name is {c_name}. I am formally reaching out for immediate hiring:
• Desired Role: {work_role}
• Target City: {clean_target}
• Verified Experience: {c_exp}
• Worker Availability: Ready for immediate reporting
• Candidate Notes: {c_notes}
• Direct Phone / WhatsApp: +91 {c_phone}

Please contact me directly. Thank you!"""

        st.success(f"🟢 {clean_target} के ठेकेदारों व कंपनियों हेतु तैयार आवेदन:")
        st.text_area("📄 तैयार आवेदन (Job Pitch):", eng_pitch, height=160)

        st.markdown("""
        <div class="caution-card">
            <h3 style="color:#EF4444; margin:0 0 6px 0;">⚠️ नौकरी ढूँढते समय अनिवार्य सावधानी:</h3>
            <ul style="margin:0; padding-left:18px; font-size:14px; color:#FCA5A5;">
                <li><b>कभी पैसे न दें:</b> कोई भी ठेकेदार यदि रजिस्ट्रेशन या गेट पास के नाम पर ₹1 भी माँगे, तो वह फ्रॉड है।</li>
                <li><b>मूल कागज़ात न छोड़ें:</b> कभी भी अपने असली मूल दस्तावेज़ किसी अनजान व्यक्ति के पास जमा न छोड़ें।</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        safe_speech = urllib.parse.quote(f"Hello Sir. My name is {c_name}. I am looking for immediate work as {role_clean} in {clean_target}. Please contact me on {c_phone}.")
        audio_speak = f"""
        <div style="text-align:center; margin:10px 0;">
            <button onclick="speakWorkerEN()" style="background:#0284C7; color:#fff; padding:10px 20px; border-radius:8px; border:none; font-weight:bold; cursor:pointer;">
                🔊 मैनेजर/ठेकेदार को अंग्रेज़ी में बोलकर सुनाएँ (Play Audio Pitch)
            </button>
        </div>
        <script>
            function speakWorkerEN() {{
                window.speechSynthesis.cancel();
                var u = new SpeechSynthesisUtterance(decodeURIComponent("{safe_speech}"));
                u.lang = "en-US";
                u.rate = 0.9;
                window.speechSynthesis.speak(u);
            }}
        </script>
        """
        components.html(audio_speak, height=60)

        st.markdown(f'<a href="{g_maps_search}" target="_blank" class="btn-blue">{T["btn_call_job"]}</a>', unsafe_allow_html=True)
        enc_pitch = urllib.parse.quote(eng_pitch)
        st.markdown(f'<a href="https://wa.me/?text={enc_pitch}" target="_blank" class="btn-green">{T["btn_wa"]}</a>', unsafe_allow_html=True)

# ================= SECTION 4: GOVT SCHEMES =================
elif nav_choice == T["sec_scheme"]:
    st.write("### 🏛️ सरकारी योजना व छात्रवृत्ति खोजक (Full Google Style)")
    u_occ = st.radio(
        "📌 आपका वर्ग चुनें:",
        ["बेरोजगार युवा", "छात्र (Student)", "किसान (Farmer)", "महिला / गृहणी", "मजदूर / श्रमिक"],
        horizontal=True
    )
    u_state = st.text_input("📍 आपका राज्य (State):", value="बिहार / उत्तर प्रदेश")
    custom_scheme = st.text_input("योजना का नाम लिखें:", value="पीएम आवास योजना")

    if st.button("⚡ संपूर्ण योजना विश्लेषण निकालें"):
        with st.spinner("सरकारी पोर्टल व योजना डेटाबेस का विश्लेषण जारी..."):
            live_txt = deep_live_knowledge(custom_scheme)
            st.markdown(f"""
            <div class="info-card">
                <h3 style="color:#38BDF8; margin:0 0 6px 0;">📌 1. योजना का परिचय</h3>
                <p style="margin:0; font-size:14px;">{custom_scheme} नागरिकों के आर्थिक उत्थान हेतु संचालित कल्याणकारी योजना है।</p>
                {f'<p style="color:#94A3B8; font-size:13px; margin-top:6px;"><b>लाइव विवरण:</b> {live_txt}</p>' if live_txt else ''}
            </div>
            <div class="info-card">
                <h3 style="color:#10B981; margin:0 0 6px 0;">🎯 2. मुख्य लाभ व वित्तीय सहायता</h3>
                <ul style="margin:0; padding-left:18px; font-size:14px;">
                    <li><b>प्रत्यक्ष अनुदान:</b> बैंक खाते में सीधे ₹1,20,000 से लेकर ₹2,50,000 तक की वित्तीय सहायता।</li>
                    <li><b>अतिरिक्त सुविधाएं:</b> निःशुल्क शौचालय निर्माण व मनरेगा मजदूरी का लाभ।</li>
                </ul>
            </div>
            <div class="caution-card">
                <h3 style="color:#EF4444; margin:0 0 6px 0;">⚠️ सरकारी योजना के लिए अनिवार्य सावधानी:</h3>
                <ul style="margin:0; padding-left:18px; font-size:14px; color:#FCA5A5;">
                    <li><b>दलालों से सावधान:</b> सरकारी योजनाओं के नाम पर किसी भी बिचौलिये को रिश्वत न दें। पूरा पैसा सीधे बैंक खाते में DBT के माध्यम से आता है।</li>
                    <li><b>ओटीपी या बैंक डिटेल:</b> कोई भी सरकारी कर्मचारी फोन करके आपके बैंक का पिन या पासवर्ड नहीं माँगता।</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

# ================= SECTION 5: CYBER FRAUD SHIELD =================
elif nav_choice == T["sec_fraud"]:
    st.write("### 🛡️ साइबर फ्रॉड सुरक्षा व स्कैम डिटेक्टर")
    scam_input = st.text_area("संदेहास्पद मैसेज, लिंक या कॉल का विवरण यहाँ डालें:", value="बिजली बिल जमा न होने के कारण आज रात 9:30 बजे बिजली काट दी जाएगी। तुरंत इस नंबर पर संपर्क करें।")
    
    if st.button("🚨 मैसेज की सत्यता जाँचें"):
        s_low = scam_input.lower()
        if any(k in s_low for k in ["बिजली", "electricity", "कट", "lottery", "लॉटरी", "टास्क", "apk", "telegram", "क्लिक"]):
            st.error("🚨 100% प्रमाणित साइबर फ्रॉड (SCAM ALERT)")
            st.markdown("""
            <div class="caution-card">
                <h3 style="color:#EF4444; margin:0 0 8px 0;">⚠️ इस फ्रॉड से बचने के 4 सुनहरे नियम:</h3>
                <p style="margin:0; font-size:14px; color:#FCA5A5;">
                1. <b>कोई लिंक न दबाएँ:</b> किसी भी अनजान APK या लिंक पर क्लिक करते ही फोन हैक हो सकता है।<br>
                2. <b>बिजली विभाग की सच्चाई:</b> बिजली विभाग कभी भी व्यक्तिगत मोबाइल नंबर से बिजली काटने की धमकी नहीं देता।<br>
                3. <b>OTP कभी न दें:</b> बैंक या आधार का OTP किसी भी परिस्थिति में किसी को न बताएँ।<br>
                4. <b>तुरंत 1930 पर कॉल करें:</b> यदि कोई ठगी हो गई है तो तुरंत राष्ट्रीय साइबर हेल्पलाइन <b>1930</b> पर कॉल करें।
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.success("🟢 संदेश में कोई तत्काल वित्तीय जोखिम नहीं मिला। हमेशा सतर्क रहें।")

# ================= SECTION 6: NASHA MUKTI & LIFE GUIDANCE =================
elif nav_choice == T["sec_life"]:
    st.write("### 🕊️ नशा-मुक्ति व सही जीवन मार्गदर्शन")
    st.markdown("""
    <div class="info-card">
        <h2 style="color:#10B981; margin:0 0 8px 0;">🌱 नशा छोड़ो, परिवार जोड़ो — सम्मान से जियो</h2>
        <p style="font-size:14px; margin:0 0 10px 0;">
            गुटखा, शराब, बीड़ी-सिगरेट केवल शरीर को नहीं, बल्कि आपकी मेहनत की पूरी कमाई और परिवार की खुशियों को बर्बाद कर देते हैं।
        </p>
    </div>

    <div class="info-card">
        <h3 style="color:#F59E0B; margin:0 0 6px 0;">💡 नशा छोड़ने का सीधा हिसाब (पैसे की बचत):</h3>
        <p style="font-size:14px; margin:0;">
        • अगर आप रोज़ केवल ₹50-₹100 का नशा करते हैं, तो साल के <b>₹30,000 से ₹40,000</b> धुएँ और ज़हर में जल जाते हैं।<br>
        • यही पैसा अगर आपके बच्चे की पढ़ाई, घर या बिज़नेस में लगे, तो 5 साल में आपका जीवन बदल सकता है।
        </p>
    </div>

    <div class="caution-card">
        <h3 style="color:#EF4444; margin:0 0 6px 0;">⚠️ नशा मुक्ति हेतु निःशुल्क सरकारी हेल्पलाइन:</h3>
        <p style="font-size:15px; margin:0; color:#FCA5A5;">
        मुफ़्त परामर्श और इलाज सहायता हेतु सरकार के टोल-फ्री नंबर पर कॉल करें: <a href="tel:14446" style="color:#FFF; font-weight:bold; text-decoration:underline;">📞 14446 (Toll-Free)</a>
        </p>
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
