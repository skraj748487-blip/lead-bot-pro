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

# ALL INDIA 12 LANGUAGES DICTIONARY
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
        "r_sub": "अपने साथ हुए किसी भी अन्याय को चुनें — सिस्टम तुरंत संबंधित कानून के तहत कड़ा नोटिस तैयार करेगा",
        "btn_rights": "⚡ आधिकारिक विधिक शिकायत पत्र व कानूनी नोटिस ड्राफ्ट करें",
        "name_lbl": "पीड़ित / प्रार्थी का नाम:",
        "city_lbl": "जिला व राज्य:",
        "phone_lbl": "पीड़ित का मोबाइल नंबर:",
        "accused_lbl": "दोषी पक्ष / कंपनी / अधिकारी / थाना का नाम:",
        "detail_lbl": "घटना का विवरण:",
        "send_wa": "📲 शिकायत पत्र WhatsApp / सोशल मीडिया पर भेजें"
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
        "btn_rights": "⚡ Draft Official Legal Notice & Investigation Complaint",
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
        "r_sub": "আপনার সাথে ঘটা অন্যায় নির্বাচন করুন — অবিলম্বে আইনি নোটিশ প্রস্তুত হবে।",
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

# 1. TOP PAN-INDIA LANGUAGE SELECTOR
all_langs = list(LANG_DICT.keys())
chosen_lang = st.radio(
    "🌐 भाषा चुनें / Select Language / ভাষা বাছুন / भाषा निवडा / மொழியைத் தேர்ந்தெடுக்கவும்:",
    all_langs,
    horizontal=True
)
T = LANG_DICT.get(chosen_lang, LANG_DICT["🇮🇳 हिन्दी"])

# Header with Selected Language
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

# ================= TAB 1: 14 LEGAL RIGHTS & COMPLAINTS =================
if nav_choice == T["sec_rights"]:
    st.write(f"### {T['r_title']}")
    st.caption(T['r_sub'])

    LEGAL_CASES = {
        "1. ठेकेदार / कंपनी ने मजदूरी या वेतन दबा लिया (Wage Theft)": {
            "act": "पेमेंट ऑफ वेजेस एक्ट 1936 व इंडस्ट्रियल डिस्प्यूट्स एक्ट",
            "authority": "श्रम आयुक्त (Labour Commissioner) व जिलाधिकारी (DM)",
            "rule": "मजदूरी दबाना गैर-कानूनी अपराध है। श्रम विभाग में शिकायत जाते ही कंपनी पर 10 गुना हर्जाना और 18% ब्याज का आदेश होता है।",
            "default_det": "मैंने कार्यस्थल पर 2 महीने पूरी ईमानदारी से मजदूरी की, जिसका कुल ₹24,000 बकाया है। माँगने पर गाली-गलौज व धमकी दी जा रही है।"
        },
        "2. पुलिस द्वारा गैर-कानूनी मारपीट, गाली-गलौज या फर्जी चालान (Police Harassment)": {
            "act": "भारतीय नागरिक सुरक्षा संहिता (BNSS) व सुप्रीम कोर्ट डी.के. बसु गाइडलाइन्स",
            "authority": "पुलिस अधीक्षक (SP), राज्य पुलिस शिकायत प्राधिकरण (SPCA) व NHRC",
            "rule": "पुलिस को बिना जुर्म किसी नागरिक पर हाथ उठाने या गाली देने का कोई हक नहीं है। धारा 166A BNS के तहत पुलिसकर्मी पर निलंबन व मुकदमा बनता है।",
            "default_det": "संबंधित पुलिसकर्मी द्वारा बिना किसी अपराध के मेरे साथ सार्वजनिक रूप से अभद्रता, मारपीट व अवैध चालान की धमकी दी गई।"
        },
        "3. अस्पताल द्वारा इमरजेंसी में भर्ती न करना या लाश/मरीज रोकना": {
            "act": "सुप्रीम कोर्ट परमानंद कटारा फैसला व क्लिनिकल एस्टेब्लिशमेंट एक्ट",
            "authority": "मुख्य चिकित्सा अधिकारी (CMO), स्वास्थ्य विभाग व उपभोक्ता आयोग",
            "rule": "कोई भी अस्पताल आपात स्थिति में पहले पैसे माँगकर इलाज से मना नहीं कर सकता। बिल विवाद में मरीज को बंधक बनाना संज्ञेय अपराध है।",
            "default_det": "इमरजेंसी में अस्पताल द्वारा पहले अग्रिम राशि जमा करने का दबाव बनाकर इलाज में जानबूझकर देरी की गई।"
        },
        "4. फैक्ट्री/कार्यस्थल पर हादसा व हाथ-पैर कटना (Employees' Compensa
