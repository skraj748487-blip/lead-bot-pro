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

# ALL INDIA 12 LANGUAGES
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
        "detail_lbl": "घटना का विवरण:",
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
        "detail_lbl": "Incident Details:",
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
    },
    "தமிழ் (Tamil)": {
        "title": "மகா-சேவா AI (MAHA SEVA AI)",
        "sub": "14 சட்ட உரிமைகள் • இரவு நேர பாதுகாப்பு • வேலைவாய்ப்பு • மருத்துவம்",
        "tag": "⚡ 24x7 குடிமக்கள் உரிமைகள் மற்றும் சட்டப் பாதுகாப்பு தளம்",
        "nav_lbl": "📂 சேவையைத் தேர்ந்தெடுக்கவும்:",
        "sec_rights": "⚖️ 14 சட்ட உரிமைகள் & புகார்",
        "sec_sos": "🚨 இரவு பாதுகாப்பு & SOS",
        "sec_health": "🏥 மருத்துவம் & ஆம்புலன்ஸ்",
        "sec_job": "💼 வேலைவாய்ப்பு தகவல்",
        "sec_scheme": "🏛️ அரசு நலத்திட்டங்கள்",
        "sec_fraud": "🛡️ இணைய பாதுகாப்பு & போதை ஒழிப்பு",
        "r_title": "⚖️ குடிமக்கள் உரிமைகள் மற்றும் ஊழல் தடுப்பு போர்டல்",
        "r_sub": "அநீதியை தேர்வு செய்யவும் — சட்டப்பூர்வ அறிவிப்பு உடனடியாக தயாராகும்.",
        "btn_rights": "⚡ சட்டப்பூர்வ நோட்டீஸ் உருவாக்கவும்",
        "name_lbl": "உங்கள் பெயர்:",
        "city_lbl": "மாவட்டம் & மாநிலம்:",
        "phone_lbl": "மொபைல் எண்:",
        "accused_lbl": "எதிர்தரப்பு நிறுவனம் / காவல் நிலையம்:",
        "detail_lbl": "நிகழ்வின் முழு விவரம்:",
        "send_wa": "📲 வாட்ஸ்அப்பில் பகிரவும்"
    },
    "తెలుగు (Telugu)": {
        "title": "మహా-సేవా AI (MAHA SEVA AI)",
        "sub": "14 చట్టపరమైన హక్కులు • రాత్రి రక్షణ • ఉపాధి • అంబులెన్స్ • పథకాలు",
        "tag": "⚡ 24x7 పౌర హక్కులు మరియు చట్టపరమైన రక్షణ మిషన్",
        "nav_lbl": "📂 సేవను ఎంచుకోండి:",
        "sec_rights": "⚖️ 14 చట్టపరమైన హక్కులు & ఫిర్యాదు",
        "sec_sos": "🚨 రాత్రి రక్షణ & SOS",
        "sec_health": "🏥 మందులు & అంబులెన్స్",
        "sec_job": "💼 ఉపాధి & ఉద్యోగాలు",
        "sec_scheme": "🏛️ ప్రభుత్వ పథకాలు",
        "sec_fraud": "🛡️ సైబర్ రక్షణ & వ్యసన విముక్తి",
        "r_title": "⚖️ పౌర హక్కులు & అవినీతి వ్యతిరేక పోర్టల్",
        "r_sub": "మీ సమస్యను ఎంచుకోండి — వెంటనే చట్టపరమైన నోటీస్ రూపొందించబడుతుంది.",
        "btn_rights": "⚡ చట్టపరమైన నోటీసు రూపొందించండి",
        "name_lbl": "ఫిర్యాదుదారు పేరు:",
        "city_lbl": "జిల్లా & రాష్ట్రం:",
        "phone_lbl": "ఫోన్ నంబర్:",
        "accused_lbl": "కాంట్రాక్టర్ / పోలీస్ స్టేషన్:",
        "detail_lbl": "పూర్తి వివరాలు:",
        "send_wa": "📲 వాట్సాప్‌లో పంపండి"
    },
    "ગુજરાતી (Gujarati)": {
        "title": "મહા-સેવા AI (MAHA SEVA AI)",
        "sub": "૧૪ કાનૂની અધિકાર • રાત્રિ સુરક્ષા • રોજગાર • એમ્બ્યુલન્સ • સરકારી યોજના",
        "tag": "⚡ ૨૪x૭ અખંડ ભારત નાગરિક કાનૂની સુરક્ષા મિશન",
        "nav_lbl": "📂 સેવા પસંદ કરો:",
        "sec_rights": "⚖️ ૧૪ કાનૂની અધિકાર અને ફરિયાદ",
        "sec_sos": "🚨 રાત્રિ સુરક્ષા અને SOS",
        "sec_health": "🏥 દવા અને એમ્બ્યુલન્સ",
        "sec_job": "💼 સીધી નોકરી અને રોજગાર",
        "sec_scheme": "🏛️ સરકારી યોજનાઓ",
        "sec_fraud": "🛡️ સાયબર સુરક્ષા અને વ્યસન મુક્તિ",
        "r_title": "⚖️ નાગરિક અધિકાર અને ભ્રષ્ટાચાર વિરોધી કાનૂની મંચ",
        "r_sub": "તમારી સમસ્યા પસંદ કરો — સિસ્ટમ તરત જ કાનૂની નોટિસ તૈયાર કરશે.",
        "btn_rights": "⚡ કાનૂની નોટિસ અને ફરિયાદ તૈયાર કરો",
        "name_lbl": "અરજદારનું નામ:",
        "city_lbl": "જિલ્લો અને રાજ્ય:",
        "phone_lbl": "મોબાઇલ નંબર:",
        "accused_lbl": "સામેવાળા કોન્ટ્રાક્ટર / પોલીસ મથક:",
        "detail_lbl": "સમગ્ર વિગત:",
        "send_wa": "📲 WhatsApp પર મોકલો"
    },
    "ಕನ್ನಡ (Kannada)": {
        "title": "ಮಹಾ-ಸೇವಾ AI (MAHA SEVA AI)",
        "sub": "14 ಕಾನೂನು ಹಕ್ಕುಗಳು • ರಾತ್ರಿ ಭದ್ರತೆ • ಉದ್ಯೋಗ • ಆಂಬ್ಯುಲೆನ್ಸ್ • ಯೋಜನೆಗಳು",
        "tag": "⚡ 24x7 ಸಾರ್ವಭೌಮ ನಾಗರಿಕ ಕಾನೂನು ರಕ್ಷಣೆ ಮಿಷನ್",
        "nav_lbl": "📂 ಸೇವೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ:",
        "sec_rights": "⚖️ 14 ಕಾನೂನು ಹಕ್ಕುಗಳು & ದೂರು",
        "sec_sos": "🚨 ರಾತ್ರಿ ಸುರಕ್ಷತೆ & SOS",
        "sec_health": "🏥 ಔಷಧಿ & ಆಂಬ್ಯುಲೆನ್ಸ್",
        "sec_job": "💼 ಉದ್ಯೋಗ ಮಾಹಿತಿ",
        "sec_scheme": "🏛️ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು",
        "sec_fraud": "🛡️ ಸೈಬರ್ ಭದ್ರತೆ & ವ್ಯಸನ ಮುಕ್ತಿ",
        "r_title": "⚖️ ನಾಗರಿಕ ಹಕ್ಕುಗಳು ಮತ್ತು ಭ್ರಷ್ಟಾಚಾರ ವಿರೋಧಿ ಪೋರ್ಟಲ್",
        "r_sub": "ಸಮಸ್ಯೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ — ತಕ್ಷಣವೇ ಕಾನೂನು ನೋಟಿಸ್ ಸಿದ್ಧವಾಗುತ್ತದೆ.",
        "btn_rights": "⚡ ಕಾನೂನು ನೋಟಿಸ್ ರಚಿಸಿ",
        "name_lbl": "ದೂರುದಾರರ ಹೆಸರು:",
        "city_lbl": "ಜಿಲ್ಲೆ & ರಾಜ್ಯ:",
        "phone_lbl": "ಮೊಬೈಲ್ ಸಂಖ್ಯೆ:",
        "accused_lbl": "ಗುತ್ತಿಗೆದಾರ / ಪೊಲೀಸ್ ಠಾಣೆ:",
        "detail_lbl": "ಸಂಪೂರ್ಣ ವಿವರ:",
        "send_wa": "📲 ವಾಟ್ಸಾಪ್‌ನಲ್ಲಿ ಕಳುಹಿಸಿ"
    },
    "മലയാളം (Malayalam)": {
        "title": "മഹാ-സേവ AI (MAHA SEVA AI)",
        "sub": "14 നിയമപരമായ അവകാശങ്ങൾ • രാത്രികാല സുരക്ഷ • തൊഴിൽ • ആംബുലൻസ്",
        "tag": "⚡ 24x7 പൗരാവകാശ നിയമ സംരക്ഷണ ദൗത്യം",
        "nav_lbl": "📂 സേവനം തിരഞ്ഞെടുക്കുക:",
        "sec_rights": "⚖️ 14 നിയമപരമായ അവകാശങ്ങളും പരാതിയും",
        "sec_sos": "🚨 രാത്രി സുരക്ഷയും SOS",
        "sec_health": "🏥 മരുന്നുകളും ആംബുലൻസും",
        "sec_job": "💼 തൊഴിൽ വിവരങ്ങൾ",
        "sec_scheme": "🏛️ സർക്കാർ ക്ഷേമപദ്ധതികൾ",
        "sec_fraud": "🛡️ സൈബർ സുരക്ഷ",
        "r_title": "⚖️ പൗരാവകാശ നിയമ സഹായ വേദി",
        "r_sub": "നിങ്ങൾ നേരിട്ട അനീതി തിരഞ്ഞെടുക്കുക — ഔദ്യോഗിക നിയമ നോട്ടീസ് ഉടൻ തയ്യാറാകും.",
        "btn_rights": "⚡ നിയമപരമായ നോട്ടീസ് തയ്യാറാക്കുക",
        "name_lbl": "പരാതിക്കാരന്റെ പേര്:",
        "city_lbl": "ജില്ലയും സംസ്ഥാനവും:",
        "phone_lbl": "മൊബൈൽ നമ്പർ:",
        "accused_lbl": "എതിർകക്ഷി / പോലീസ് സ്റ്റേഷൻ:",
        "detail_lbl": "പൂർണ്ണ വിവരങ്ങൾ:",
        "send_wa": "📲 വാട്ട്‌സ്ആപ്പിൽ അയക്കുക"
    },
    "ਪੰਜਾਬੀ (Punjabi)": {
        "title": "ਮਹਾ-ਸੇਵਾ AI (MAHA SEVA AI)",
        "sub": "14 ਕਾਨੂੰਨੀ ਹੱਕ • ਰਾਤ ਦੀ ਸੁਰੱਖਿਆ • ਰੋਜ਼ਗਾਰ • ਐਂਬੂਲੈਂਸ • ਸਰਕਾਰੀ ਸਕੀਮਾਂ",
        "tag": "⚡ 24x7 ਅਖੰਡ ਭਾਰਤ ਨਾਗਰਿਕ ਕਾਨੂੰਨੀ ਸੁਰੱਖਿਆ ਮਿਸ਼ਨ",
        "nav_lbl": "📂 ਸੇਵਾ ਚੁਣੋ:",
        "sec_rights": "⚖️ 14 ਕਾਨੂੰਨੀ ਹੱਕ ਤੇ ਸ਼ਿਕਾਇਤ",
        "sec_sos": "🚨 ਰਾਤ ਦੀ ਸੁਰੱਖਿਆ ਤੇ SOS",
        "sec_health": "🏥 ਦਵਾਈ ਤੇ ਐਂਬੂਲੈਂਸ",
        "sec_job": "💼 ਰੋਜ਼ਗਾਰ ਤੇ ਨੌਕਰੀ",
        "sec_scheme": "🏛️ ਸਰਕਾਰੀ ਸਕੀਮਾਂ",
        "sec_fraud": "🛡️ ਸਾਈਬਰ ਸੁਰੱਖਿਆ ਤੇ ਨਸ਼ਾ ਮੁਕਤੀ",
        "r_title": "⚖️ ਨਾਗਰਿਕ ਹੱਕ ਤੇ ਭ੍ਰਿਸ਼ਟਾਚਾਰ ਵਿਰੋਧੀ ਕਾਨੂੰਨੀ ਮੰਚ",
        "r_sub": "ਆਪਣੀ ਸਮੱਸਿਆ ਚੁਣੋ — ਸਿਸਟਮ ਤੁਰੰਤ ਕਾਨੂੰਨੀ ਨੋਟਿਸ ਤਿਆਰ ਕਰੇਗਾ।",
        "btn_rights": "⚡ ਕਾਨੂੰਨੀ ਨੋਟਿਸ ਤਿਆਰ ਕਰੋ",
        "name_lbl": "ਪੀੜਤ ਦਾ ਨਾਮ:",
        "city_lbl": "ਜ਼ਿਲ੍ਹਾ ਤੇ ਰਾਜ:",
        "phone_lbl": "ਮੋਬਾਈਲ ਨੰਬਰ:",
        "accused_lbl": "ਦੋਸ਼ੀ ਠੇਕੇਦਾਰ / ਥਾਣਾ:",
        "detail_lbl": "ਘਟਨਾ ਦਾ ਪੂਰਾ ਵੇਰਵਾ:",
        "send_wa": "📲 WhatsApp ਤੇ ਭੇਜੋ"
    },
    "ଓଡ଼ିଆ (Odia)": {
        "title": "ମହା-ସେବା AI (MAHA SEVA AI)",
        "sub": "୧୪ଟି ଆଇନଗତ ଅଧିକାର • ରାତ୍ରି ସୁରକ୍ଷା • ନିଯୁକ୍ତି • ଆମ୍ବୁଲାନ୍ସ • ଯୋଜନା",
        "tag": "⚡ ୨୪x୭ ନାଗରିକ ଆଇନଗତ ସୁରକ୍ଷା ମିଶନ",
        "nav_lbl": "📂 ସେବା ବାଛନ୍ତୁ:",
        "sec_rights": "⚖️ ୧୪ ଆଇନଗତ ଅଧିକାର ଓ ଅଭିଯୋଗ",
        "sec_sos": "🚨 ରାତ୍ରି ସୁରକ୍ଷା ଓ SOS",
        "sec_health": "🏥 ଔଷଧ ଓ ଆମ୍ବୁଲାନ୍ସ",
        "sec_job": "💼 ନିଯୁକ୍ତି ସୂଚନା",
        "sec_scheme": "🏛️ ସରକାରୀ ଯୋଜନା",
        "sec_fraud": "🛡️ ସାଇବର ସୁରକ୍ଷା",
        "r_title": "⚖️ ନାଗରିକ ଅଧିକାର ଓ ଦୁର୍ନୀତି ନିବାରଣ ପୋର୍ଟାଲ",
        "r_sub": "ସମସ୍ୟା ଚୟନ କରନ୍ତୁ — ଆଇନଗତ ନୋଟିସ୍ ତୁରନ୍ତ ପ୍ରସ୍ତୁତ ହେବ।",
        "btn_rights": "⚡ ଆଇନଗତ ନୋଟିସ୍ ପ୍ରସ୍ତୁତ କରନ୍ତୁ",
        "name_lbl": "ଅଭିଯୋଗକାରୀଙ୍କ ନାମ:",
        "city_lbl": "ଜିଲ୍ଲା ଓ ରାଜ୍ୟ:",
        "phone_lbl": "ମୋବାଇଲ୍ ନମ୍ବର:",
        "accused_lbl": "ଦୋଷୀ ପକ୍ଷ / ଥାନା:",
        "detail_lbl": "ସମ୍ପୂର୍ଣ୍ଣ ବିବରଣୀ:",
        "send_wa": "📲 WhatsApp ରେ ପଠାନ୍ତୁ"
    },
    "অসমীয়া (Assamese)": {
        "title": "মহা-সেৱা AI (MAHA SEVA AI)",
        "sub": "১৪টা আইনী অধিকাৰ • ৰাতিৰ সুৰক্ষা • নিয়োগ • এম্বুলেন্স • আঁচনি",
        "tag": "⚡ ২৪x৭ অখণ্ড ভাৰত নাগৰিক আইনী সুৰক্ষা অভিযান",
        "nav_lbl": "📂 সেৱা বাছক:",
        "sec_rights": "⚖️ ১৪টা আইনী অধিকাৰ আৰু অভিযোগ",
        "sec_sos": "🚨 ৰাতিৰ সুৰক্ষা আৰু SOS",
        "sec_health": "🏥 ঔষধ আৰু এম্বুলেন্স",
        "sec_job": "💼 নিয়োগ আৰু সাহায্য কেন্দ্ৰ",
        "sec_scheme": "🏛️ চৰকাৰী আঁচনি",
        "sec_fraud": "🛡️ চাইবাৰ সুৰক্ষা",
        "r_title": "⚖️ নাগৰিক অধিকাৰ আৰু দুৰ্নীতি বিৰোধী মঞ্চ",
        "r_sub": "সমস্যা বাছক — ব্যৱস্থাই ততালিকে আইনী জাননী প্ৰস্তুত কৰিব।",
        "btn_rights": "⚡ আইনী জাননী প্ৰস্তুত কৰক",
        "name_lbl": "অভিযোগকাৰীৰ নাম:",
        "city_lbl": "জিলা আৰু ৰাজ্য:",
        "phone_lbl": "মোবাইল নম্বৰ:",
        "accused_lbl": "অভিযুক্ত পক্ষ / থানা:",
        "detail_lbl": "সম্পূৰ্ণ বিৱৰণ:",
        "send_wa": "📲 WhatsAppত পঠিয়াওক"
    }
}

# Language Picker
all_langs = list(LANG_DICT.keys())
chosen_lang = st.radio(
    "🌐 भाषा चुनें / Select Language / ভাষা বাছুন / भाषा निवडा / மொழியைத் தேர்ந்தெடுக்கவும்:",
    all_langs,
    horizontal=True
)
T = LANG_DICT.get(chosen_lang, LANG_DICT["🇮🇳 हिन्दी"])

# Header
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

# 14 CASES WITH SAFE LITERAL STRINGS
if nav_choice == T["sec_rights"]:
    st.write(f"### {T['r_title']}")
    st.caption(T['r_sub'])

    LEGAL_CASES = {
        "1. Thekedar ya Company ne majdoori/salary roki (Wage Theft)": {
            "act": "Payment of Wages Act 1936 and Industrial Disputes Act",
            "authority": "Labour Commissioner and DM",
            "rule": "Majdoori dabana gair-kanooni hai. Shram vibhag 10 guna harjana dilata hai.",
            "default_det": "Maine 2 mahine imaandari se kaam kiya, jiska kul Rs 24000 bakaya hai. Mangne par gaali aur dhamki di ja rahi hai."
        },
        "2. Police dwara gair-kanooni maarpeet ya farzi challan": {
            "act": "BNSS and Supreme Court DK Basu Guidelines",
            "authority": "SP, State Police Complaints Authority and NHRC",
            "rule": "Bina jurm maarpeet ya gaali dene par Section 166A BNS ke tahet FIR aur suspension hota hai.",
            "default_det": "Police dwara bina kisi apradh ke abhadra vyavhar, maarpeet aur farzi challan ki dhamki di gayi."
        },
        "3. Hospital dwara emergency me bharti na karna ya dead body rokna": {
            "act": "Supreme Court Parmanand Katara Verdict and Clinical Establishments Act",
            "authority": "CMO, Health Department and Consumer Forum",
            "rule": "Emergency me advance paise mang kar ilaaj se inkar nahi kiya ja sakta. Body rokna gair-kanooni jurm hai.",
            "default_det": "Emergency me hospital dwara pehle advance paise mang kar ilaaj me jaanboojhkar deri ki gayi."
        },
        "4. Karyasthal par hadsa aur sharirik apangta (Workplace Injury)": {
            "act": "Employees Compensation Act 1923",
            "authority": "Compensation Commissioner and Labour Court",
            "rule": "Duty ke dauran hadsa hone par malik ko Rs 5 se 20 lakh ka muavza aur pension dena anivarya hai.",
            "default_det": "Suraksha ke abhav me hadsa hua jisse divyangta aayi. Malik muavza dene se mukar raha hai."
        },
        "5. Soodkhor aur farzi loan apps dwara dhamki aur blackmail": {
            "act": "RBI Guidelines and Extortion Law Section 308 BNS",
            "authority": "Cyber Crime Cell, SP and RBI Ombudsman",
            "rule": "Bina license soodkhori aur dhamki dekar vasooli karna gair-kanooni hai. Seedhe FIR hoti hai.",
            "default_det": "Avadh byaj vasooli ke liye loan agent dwara dhamki aur photo viral karne ka blackmail kiya ja raha hai."
        },
        "6. Sarkari daftar me ghuskhori aur line me bhaga dena (RTPS)": {
            "act": "Right to Public Services Act and Anti-Corruption Act",
            "authority": "Vigilance Bureau and CM Helpline",
            "rule": "Samay par kaam na karne par karmchari ki salary se rozana jurmana katne ka niyam hai.",
            "default_det": "Zaroori dastavez dene ke bawajood bina rishwat ke babu dwara baar-baar chakkar lagwaye ja rahe hain."
        },
        "7. Dukandar ya ration dealer dwara MRP se zyada dam aur chori": {
            "act": "Legal Metrology Act 2009 and NFSA",
            "authority": "Consumer Affairs and DSO",
            "rule": "MRP se zyada dam lena ya ration kam tolna gair-kanooni hai. Rs 25000 jurmana aur license radd hota hai.",
            "default_det": "Dukandar dwara MRP se zyada dam vasoola gaya aur kam quantity di gayi."
        },
        "8. Train me TTE ya kisi dwara avadh vasooli aur badsulooki": {
            "act": "Indian Railway Act and Rail Safety Rules",
            "authority": "Railway Board Vigilance, RPF and RailMadad 139",
            "rule": "TTE ko badtameezi karne ya train se nikalne ka haq nahi. Sirf receipt di ja sakti hai.",
            "default_det": "Yatra ke dauran TTE dwara niyam viruddh paise ki mang aur virodh karne par badsulooki ki gayi."
        },
        "9. Thane me FIR darj na karna (Zero FIR ka adhikar)": {
            "act": "Supreme Court Lalita Kumari Guidelines and Section 173 BNSS",
            "authority": "SSP, DGP and CJM Court",
            "rule": "FIR na likhne wale police adhikari par Section 166A BNS ke tahet seedhe FIR darj hoti hai.",
            "default_det": "Ghatna ki written complaint dene ke bawajood thana incharge dwara FIR darj karne se mana kiya gaya."
        },
        "10. Zameen par dabangon dwara avadh kabza": {
            "act": "Section 145/144 BNSS and Protection of Civil Rights Act",
            "authority": "SDM and Civil Court",
            "rule": "Garib ki paetrik zameen par kabze ki koshish par police ko suraksha dena aur stay lagana anivarya hai.",
            "default_det": "Vipakshi dwara prarthi ki paetrik zameen par balpoorvak avadh kabze ki koshish ki ja rahi hai."
        },
        "11. Sadak hadse (Hit and Run) me sarkari muavza": {
            "act": "Motor Vehicles Amendment Act (Hit and Run Scheme)",
            "authority": "MACT and District Collector Relief Fund",
            "rule": "Maut par sarkar dwara Rs 2 lakh aur ghayal ko Rs 50000 ki tatkaal rahat di jati hai.",
            "default_det": "Sadak hadse ke uprant sarkari rahat kosh aur bima claim ki mang ki ja rahi hai."
        },
        "12. Muft sarkari vakeel pane hetu aavedan": {
            "act": "Legal Services Authorities Act 1987 (Article 39A)",
            "authority": "DLSA Secretary",
            "rule": "Garib, mazdoor aur mahila ko case ladne ke liye sarkar apne kharche par vakeel deti hai.",
            "default_det": "Prarthi arthik roop se asamarth hai aur use court case ladne hetu muft sarkari vakeel chahiye."
        },
        "13. Makan malik dwara bina notice zabardasti bedakhli": {
            "act": "Rent Control Act and BNS",
            "authority": "Rent Controller and Local Police",
            "rule": "Makan malik bina court order ke tala nahi tod sakta, na hi paani-bijli kaat sakta hai.",
            "default_det": "Makan malik dwara bina notice paani-bijli band kar makaan khali karne ki dhamki di ja rahi hai."
        },
        "14. Jatigat bhedbhav aur samajik bahishkar nivaran": {
            "act": "SC/ST Prevention of Atrocities Act and Article 15",
            "authority": "SP and Special Court",
            "rule": "Jati ke aadhar par gaali dene ya raasta rokne par non-bailable arrest hoti hai.",
            "default_det": "Vipakshi dwara jati-soochak gaaliyan dekar sarvajanik roop se apmanit aur pratatit kiya gaya."
        }
    }

    selected_issue = st.radio("📌 अपनी समस्या का चयन करें:", list(LEGAL_CASES.keys()))
    case_info = LEGAL_CASES[selected_issue]

    st.info(f"⚖️ **Kanoon:** {case_info['act']} | **Adhikari:** {case_info['authority']}")

    col_v1, col_v2 = st.columns(2)
    with col_v1:
        v_name = st.text_input(T["name_lbl"], value="साहिल कुमार", key=f"name_{chosen_lang}")
    with col_v2:
        v_loc = st.text_input(T["city_lbl"], value="पश्चिम चंपारण, बिहार", key=f"city_{chosen_lang}")

    v_phone = st.text_input(T["phone_lbl"], value="7484878440", key=f"phone_{chosen_lang}")
    v_accused = st.text_input(T["accused_lbl"], value="संबंधित दोषी पक्ष / अधिकारी", key=f"acc_{chosen_lang}")
    v_details = st.text_area(T["detail_lbl"], value=case_info["default_det"], key=f"det_{chosen_lang}")

    if st.button(T['btn_rights'], key=f"btn_r_{chosen_lang}"):
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
