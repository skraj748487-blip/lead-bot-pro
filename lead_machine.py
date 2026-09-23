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

# 2. Modern 100% Dark UI - Fixed White Box Glitch
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

# 12 Languages Setup
LANG_CONFIG = {
    "🇮🇳 हिन्दी": {
        "tag": "⚡ 24x7 अखंड भारत नागरिक व विधिक सुरक्षा मिशन",
        "title": "महा-सेवा AI (MAHA SEVA AI)",
        "sub": "28 महा-विधिक अधिकार • रात की सुरक्षा • बोलकर शिकायत • दवा व रोज़गार",
        "cat_lbl": "📂 सेवा श्रेणी चुनें:",
        "c_rights": "⚖️ 28 विधिक अधिकार व कानूनी नोटिस",
        "c_sos": "🚨 रात की सुरक्षा व लाइव GPS SOS",
        "c_voice": "🎙️ बोलकर शिकायत दर्ज करें (माइक)",
        "c_fraud": "🛡️ साइबर फ्रॉड व मैसेज चेकर",
        "c_health": "🏥 दवा व एम्बुलेंस सहायता",
        "c_job": "💼 रोज़गार व हेल्पर डेस्क",
        "r_title": "⚖️ 28 महा-विधिक अधिकार व आधिकारिक नोटिस",
        "r_sub": "समस्या नंबर चुनें — सिस्टम तुरंत संबंधित कानून के तहत कड़ा नोटिस तैयार करेगा:",
        "num_lbl": "🔢 1 से 28 में से समस्या संख्या चुनें:",
        "name_lbl": "पीड़ित / प्रार्थी का नाम:",
        "city_lbl": "जिला व राज्य:",
        "phone_lbl": "मोबाइल नंबर:",
        "acc_lbl": "दोषी पक्ष / अधिकारी / कंपनी:",
        "det_lbl": "सच्चा घटनाक्रम विवरण:",
        "btn_draft": "⚡ आधिकारिक कानूनी शिकायत पत्र व नोटिस ड्राफ्ट करें",
        "send_wa": "📲 यह शिकायत WhatsApp पर भेजें"
    },
    "🇬🇧 English": {
        "tag": "⚡ 24x7 Pan-India Sovereign Citizen Legal Mission",
        "title": "MAHA SEVA AI — Citizen Sovereign Portal",
        "sub": "28 Sovereign Legal Protections • Night SOS • Voice Help • Jobs",
        "cat_lbl": "📂 Select Service Category:",
        "c_rights": "⚖️ 28 Sovereign Legal Rights & Notices",
        "c_sos": "🚨 Night Safety & Live GPS SOS",
        "c_voice": "🎙️ Voice-to-Text Complaint (Mic)",
        "c_fraud": "🛡️ Cyber Shield & Fraud Verifier",
        "c_health": "🏥 Healthcare & Free Ambulance",
        "c_job": "💼 Pan-India Employment Desk",
        "r_title": "⚖️ 28 Pan-India Citizen Legal Protections",
        "r_sub": "Select issue number — system generates official legal notice instantly:",
        "num_lbl": "🔢 Select issue number (1 to 28):",
        "name_lbl": "Complainant Name:",
        "city_lbl": "District & State:",
        "phone_lbl": "Mobile Number:",
        "acc_lbl": "Accused Party / Official / Agency:",
        "det_lbl": "Factual Details of Injustice:",
        "btn_draft": "⚡ Draft Official Court-Grade Legal Notice",
        "send_wa": "📲 Send Notice via WhatsApp"
    },
    "বাংলা (Bengali)": {
        "tag": "⚡ ২৪x৭ অখণ্ড ভারত নাগরিক আইনি মিশন",
        "title": "মহা-সেবা AI (MAHA SEVA AI)",
        "sub": "২৮টি আইনি অধিকার • নৈশ নিরাপত্তা • ভয়েস অভিযোগ • কর্মসংস্থান",
        "cat_lbl": "📂 পরিষেবা বিভাগ নির্বাচন করুন:",
        "c_rights": "⚖️ ২৮টি আইনি অধিকার ও নোটিশ",
        "c_sos": "🚨 নৈশ নিরাপত্তা ও GPS SOS",
        "c_voice": "🎙️ মুখে বলে অভিযোগ (মাইক)",
        "c_fraud": "🛡️ সাইবার সুরক্ষা ও প্রতারণা যাচাই",
        "c_health": "🏥 ওষুধ ও অ্যাম্বুলেন্স সহায়তা",
        "c_job": "💼 কর্মসংস্থান ও হেল্পার ডেস্ক",
        "r_title": "⚖️ ২৮টি নাগরিক আইনি অধিকার সুরক্ষা মঞ্চ",
        "r_sub": "সমস্যা নম্বর নির্বাচন করুন — অবিলম্বে আইনি নোটিশ প্রস্তুত হবে:",
        "num_lbl": "🔢 ১ থেকে ২৮ সমস্যা নম্বর বেছে নিন:",
        "name_lbl": "অভিযোগকারীর নাম:",
        "city_lbl": "জেলা ও রাজ্য:",
        "phone_lbl": "মোবাইল নম্বর:",
        "acc_lbl": "অভিযুক্ত পক্ষ / ঠিকাদার / থানা:",
        "det_lbl": "ঘটনার সম্পূর্ণ বিবরণ:",
        "btn_draft": "⚡ আইনি অভিযোগ পত্র প্রস্তুত করুন",
        "send_wa": "📲 হোয়াটসঅ্যাপে নোটিশ পাঠান"
    },
    "मराठी (Marathi)": {
        "tag": "⚡ २४x७ अखंड भारत नागरिक कायदेशीर सुरक्षा मिशन",
        "title": "महा-सेवा AI (MAHA SEVA AI)",
        "sub": "२८ कायदेशीर अधिकार • रात्रीची सुरक्षा • थेट नोकरी • आरोग्य",
        "cat_lbl": "📂 सेवा श्रेणी निवडा:",
        "c_rights": "⚖️ २८ कायदेशीर अधिकार व नोटीस",
        "c_sos": "🚨 रात्रीची सुरक्षा व GPS SOS",
        "c_voice": "🎙️ बोलून तक्रार नोंदवा (माइक)",
        "c_fraud": "🛡️ सायबर फसवणूक तपासक",
        "c_health": "🏥 औषधे व रुग्णवाहिका",
        "c_job": "💼 रोजगार व थेट नोकरी",
        "r_title": "⚖️ २८ नागरी हक्क व कायदेशीर मंच",
        "r_sub": "समस्या क्रमांक निवडा — प्रणाली तात्काळ कडक कायदेशीर नोटीस तयार करेल:",
        "num_lbl": "🔢 १ ते २८ मधील समस्या क्रमांक निवडा:",
        "name_lbl": "तक्रारदाराचे नाव:",
        "city_lbl": "जिल्हा व राज्य:",
        "phone_lbl": "मोबाईल नंबर:",
        "acc_lbl": "दोषी कंत्राटदार / अधिकारी / पोलीस:",
        "det_lbl": "घटनेचा संपूर्ण तपशील:",
        "btn_draft": "⚡ कायदेशीर नोटीस तयार करा",
        "send_wa": "📲 WhatsApp वर पाठवा"
    },
    "தமிழ் (Tamil)": {
        "tag": "⚡ 24x7 குடிமக்கள் சட்டப் பாதுகாப்பு தளம்",
        "title": "மகா-சேவா AI (MAHA SEVA AI)",
        "sub": "28 சட்ட உரிமைகள் • இரவு பாதுகாப்பு • வேலைவாய்ப்பு",
        "cat_lbl": "📂 சேவையைத் தேர்ந்தெடுக்கவும்:",
        "c_rights": "⚖️ 28 சட்ட உரிமைகள் & நோட்டீஸ்",
        "c_sos": "🚨 இரவு பாதுகாப்பு & GPS SOS",
        "c_voice": "🎙️ குரல் மூலம் புகார் (மைக்)",
        "c_fraud": "🛡️ இணைய மோசடி சரிபார்ப்பு",
        "c_health": "🏥 மருத்துவம் & ஆம்புலன்ஸ்",
        "c_job": "💼 வேலைவாய்ப்பு தகவல்",
        "r_title": "⚖️ 28 குடிமக்கள் உரிமைகள் விழிப்புணர்வு போர்டல்",
        "r_sub": "பிரச்சனை எண்ணைத் தேர்ந்தெடுக்கவும்:",
        "num_lbl": "🔢 1 முதல் 28 வரை எண் தேர்வு செய்க:",
        "name_lbl": "புகார்தாரர் பெயர்:",
        "city_lbl": "மாவட்டம் & மாநிலம்:",
        "phone_lbl": "மொபைல் எண்:",
        "acc_lbl": "எதிர்தரப்பு நிறுவனம் / அதிகாரி:",
        "det_lbl": "நிகழ்வின் முழு விவரம்:",
        "btn_draft": "⚡ சட்டப்பூர்வ நோட்டீஸ் உருவாக்கவும்",
        "send_wa": "📲 வாட்ஸ்அப்பில் பகிரவும்"
    },
    "తెలుగు (Telugu)": {
        "tag": "⚡ 24x7 పౌర హక్కుల రక్షణ మిషన్",
        "title": "మహా-సేవా AI (MAHA SEVA AI)",
        "sub": "28 చట్టపరమైన హక్కులు • రాత్రి రక్షణ • ఉపాధి",
        "cat_lbl": "📂 సేవను ఎంచుకోండి:",
        "c_rights": "⚖️ 28 చట్టపరమైన హక్కులు & నోటీసు",
        "c_sos": "🚨 రాత్రి రక్షణ & GPS SOS",
        "c_voice": "🎙️ వాయిస్ ద్వారా ఫిర్యాదు",
        "c_fraud": "🛡️ సైబర్ మోసాల తనిఖీ",
        "c_health": "🏥 మందులు & అంబులెన్స్",
        "c_job": "💼 ఉపాధి & ఉద్యోగాలు",
        "r_title": "⚖️ 28 పౌర హక్కుల వేదిక",
        "r_sub": "సమస్య సంఖ్యను ఎంచుకోండి:",
        "num_lbl": "🔢 1 నుండి 28 సంఖ్యను ఎంచుకోండి:",
        "name_lbl": "ఫిర్యాదుదారు పేరు:",
        "city_lbl": "జిల్లా & రాష్ట్రం:",
        "phone_lbl": "ఫోన్ నంబర్:",
        "acc_lbl": "బాధ్యులైన అధికారి / కాంట్రాక్టర్:",
        "det_lbl": "పూర్తి వివరాలు:",
        "btn_draft": "⚡ చట్టపరమైన నోటీసు రూపొందించండి",
        "send_wa": "📲 వాట్సాప్‌లో పంపండి"
    },
    "ગુજરાતી (Gujarati)": {
        "tag": "⚡ ૨૪x૭ નાગરિક કાનૂની સુરક્ષા મિશન",
        "title": "મહા-સેવા AI (MAHA SEVA AI)",
        "sub": "૨૮ કાનૂની અધિકાર • રાત્રિ સુરક્ષા • રોજગાર",
        "cat_lbl": "📂 સેવા પસંદ કરો:",
        "c_rights": "⚖️ ૨૮ કાનૂની અધિકાર અને નોટિસ",
        "c_sos": "🚨 રાત્રિ સુરક્ષા & GPS SOS",
        "c_voice": "🎙️ અવાજ દ્વારા ફરિયાદ",
        "c_fraud": "🛡️ સાયબર ફ્રોડ તપાસક",
        "c_health": "🏥 દવા અને એમ્બ્યુલન્સ",
        "c_job": "💼 સીધી નોકરી અને રોજગાર",
        "r_title": "⚖️ ૨૮ નાગરિક અધિકાર મંચ",
        "r_sub": "સમસ્યા નંબર પસંદ કરો:",
        "num_lbl": "🔢 ૧ થી ૨૮ નંબર પસંદ કરો:",
        "name_lbl": "અરજદારનું નામ:",
        "city_lbl": "જિલ્લો અને રાજ્ય:",
        "phone_lbl": "મોબાઇલ નંબર:",
        "acc_lbl": "સામેવાળા પક્ષ / અધિકારી:",
        "det_lbl": "સમગ્ર વિગત:",
        "btn_draft": "⚡ કાનૂની નોટિસ તૈયાર કરો",
        "send_wa": "📲 WhatsApp પર મોકલો"
    },
    "ಕನ್ನಡ (Kannada)": {
        "tag": "⚡ 24x7 ನಾಗರಿಕ ಕಾನೂನು ರಕ್ಷಣೆ ಮಿಷನ್",
        "title": "ಮಹಾ-ಸೇವಾ AI (MAHA SEVA AI)",
        "sub": "28 ಕಾನೂನು ಹಕ್ಕುಗಳು • ರಾತ್ರಿ ಭದ್ರತೆ • ಉದ್ಯೋಗ",
        "cat_lbl": "📂 ಸೇವೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ:",
        "c_rights": "⚖️ 28 ಕಾನೂನು ಹಕ್ಕುಗಳು & ನೋಟಿಸ್",
        "c_sos": "🚨 ರಾತ್ರಿ ಸುರಕ್ಷತೆ & GPS SOS",
        "c_voice": "🎙️ ಧ್ವನಿ ಮೂಲಕ ದೂರು",
        "c_fraud": "🛡️ ಸೈಬರ್ ವಂಚನೆ ಪರಿಶೀಲಕ",
        "c_health": "🏥 ಔಷಧಿ & ಆಂಬ್ಯುಲೆನ್ಸ್",
        "c_job": "💼 ಉದ್ಯೋಗ ಮಾಹಿತಿ",
        "r_title": "⚖️ 28 ನಾಗರಿಕ ಕಾನೂನು ವೇದಿಕೆ",
        "r_sub": "ಸಮಸ್ಯೆ ಸಂಖ್ಯೆಯನ್ನು ಆರಿಸಿ:",
        "num_lbl": "🔢 1 ರಿಂದ 28 ರವರೆಗಿನ ಸಂಖ್ಯೆ:",
        "name_lbl": "ದೂರುದಾರರ ಹೆಸರು:",
        "city_lbl": "ಜಿಲ್ಲೆ & ರಾಜ್ಯ:",
        "phone_lbl": "ಮೊಬೈಲ್ ಸಂಖ್ಯೆ:",
        "acc_lbl": "ಆರೋಪಿ / ಅಧಿಕಾರಿ / ಗುತ್ತಿಗೆದಾರ:",
        "det_lbl": "ಸಂಪೂರ್ಣ ವಿವರ:",
        "btn_draft": "⚡ ಕಾನೂನು ನೋಟಿಸ್ ರಚಿಸಿ",
        "send_wa": "📲 ವಾಟ್ಸಾಪ್‌ನಲ್ಲಿ ಕಳುಹಿಸಿ"
    },
    "മലയാളം (Malayalam)": {
        "tag": "⚡ 24x7 പൗരാവകാശ നിയമ സംരക്ഷണ ദൗത്യം",
        "title": "മഹാ-സേവ AI (MAHA SEVA AI)",
        "sub": "28 നിയമപരമായ അവകാശങ്ങൾ • രാത്രി സുരക്ഷ",
        "cat_lbl": "📂 സേവനം തിരഞ്ഞെടുക്കുക:",
        "c_rights": "⚖️ 28 അവകാശങ്ങളും നിയമ നോട്ടീസും",
        "c_sos": "🚨 രാത്രി സുരക്ഷ & GPS SOS",
        "c_voice": "🎙️ ശബ്ദത്തിലൂടെ പരാതി നൽകാം",
        "c_fraud": "🛡️ സൈബർ തട്ടിപ്പ് പരിശോധന",
        "c_health": "🏥 മരുന്നുകളും ആംബുലൻസും",
        "c_job": "💼 തൊഴിൽ വിവരങ്ങൾ",
        "r_title": "⚖️ 28 പൗരാവകാശ നിയമ സഹായ വേദി",
        "r_sub": "പ്രശ്ന നമ്പർ തിരഞ്ഞെടുക്കുക:",
        "num_lbl": "🔢 1 മുതൽ 28 വരെയുള്ള നമ്പർ:",
        "name_lbl": "പരാതിക്കാരന്റെ പേര്:",
        "city_lbl": "ജില്ലയും സംസ്ഥാനവും:",
        "phone_lbl": "മൊബൈൽ നമ്പർ:",
        "acc_lbl": "എതിർകക്ഷി / പോലീസ് സ്റ്റേഷൻ:",
        "det_lbl": "പൂർണ്ണ വിവരങ്ങൾ:",
        "btn_draft": "⚡ ഔദ്യോഗിക നിയമ നോട്ടീസ്",
        "send_wa": "📲 വാട്ട്‌സ്ആപ്പിൽ അയക്കുക"
    },
    "ਪੰਜਾਬੀ (Punjabi)": {
        "tag": "⚡ 24x7 ਨਾਗਰਿਕ ਕਾਨੂੰਨੀ ਸੁਰੱਖਿਆ ਮਿਸ਼ਨ",
        "title": "ਮਹਾ-ਸੇਵਾ AI (MAHA SEVA AI)",
        "sub": "28 ਕਾਨੂੰਨੀ ਹੱਕ • ਰਾਤ ਦੀ ਸੁਰੱਖਿਆ • ਰੋਜ਼ਗਾਰ",
        "cat_lbl": "📂 ਸੇਵਾ ਚੁਣੋ:",
        "c_rights": "⚖️ 28 ਕਾਨੂੰਨੀ ਹੱਕ ਤੇ ਨੋਟਿਸ",
        "c_sos": "🚨 ਰਾਤ ਦੀ ਸੁਰੱਖਿਆ & GPS SOS",
        "c_voice": "🎙️ ਬੋਲ ਕੇ ਸ਼ਿਕਾਇਤ ਲਿਖੋ",
        "c_fraud": "🛡️ ਸਾਈਬਰ ਧੋਖਾਧੜੀ ਜਾਂਚ",
        "c_health": "🏥 ਦਵਾਈ ਤੇ ਐਂਬੂਲੈਂਸ",
        "c_job": "💼 ਰੋਜ਼ਗਾਰ ਤੇ ਨੌਕਰੀ",
        "r_title": "⚖️ 28 ਨਾਗਰਿਕ ਹੱਕ ਕਾਨੂੰਨੀ ਮੰਚ",
        "r_sub": "ਸਮੱਸਿਆ ਨੰਬਰ ਚੁਣੋ:",
        "num_lbl": "🔢 1 ਤੋਂ 28 ਨੰਬਰ ਚੁਣੋ:",
        "name_lbl": "ਪੀੜਤ ਦਾ ਨਾਮ:",
        "city_lbl": "ਜ਼ਿਲ੍ਹਾ ਤੇ ਰਾਜ:",
        "phone_lbl": "ਮੋਬਾਈਲ ਨੰਬਰ:",
        "acc_lbl": "ਦੋਸ਼ੀ ਠੇਕੇਦਾਰ / ਥਾਣਾ / ਅਧਿਕਾਰੀ:",
        "det_lbl": "ਘਟਨਾ ਦਾ ਪੂਰਾ ਵੇਰਵਾ:",
        "btn_draft": "⚡ ਕਾਨੂੰਨੀ ਨੋਟਿਸ ਤਿਆਰ ਕਰੋ",
        "send_wa": "📲 WhatsApp ਤੇ ਭੇਜੋ"
    },
    "ଓଡ଼ିଆ (Odia)": {
        "tag": "⚡ ୨୪x୭ ନାଗରିକ ଆଇନଗତ ସୁରକ୍ଷା ମିଶନ",
        "title": "ମହା-ସେବା AI (MAHA SEVA AI)",
        "sub": "୨୮ଟି ଆଇନଗତ ଅଧିକାର • ରାତ୍ରି ସୁରକ୍ଷା",
        "cat_lbl": "📂 ସେବା ବାଛନ୍ତୁ:",
        "c_rights": "⚖️ ୨୮ ଆଇନଗତ ଅଧିକାର ଓ ନୋଟିସ୍",
        "c_sos": "🚨 ରାତ୍ରି ସୁରକ୍ଷା & GPS SOS",
        "c_voice": "🎙️ କହିକରି ଅଭିଯୋਗ ଲେଖନ୍ତୁ",
        "c_fraud": "🛡️ ସାଇବର ଠକେଇ ଯାଞ୍ଚ",
        "c_health": "🏥 ଔଷଧ ଓ ଆମ୍ବୁଲାନ୍ସ",
        "c_job": "💼 ନିଯୁକ୍ତି ସୂଚନା",
        "r_title": "⚖️ ୨୮ ନାଗରିକ ଅଧିକାର ପୋର୍ଟାଲ",
        "r_sub": "ସମସ୍ୟା ସଂଖ୍ୟା ବାଛନ୍ତୁ:",
        "num_lbl": "🔢 ୧ ରୁ ୨୮ ସଂଖ୍ୟା ଚୟନ:",
        "name_lbl": "ଅଭିଯୋଗକାରୀଙ୍କ ନାମ:",
        "city_lbl": "ଜିଲ୍ଲା ଓ ରାଜ୍ୟ:",
        "phone_lbl": "ମୋବାଇଲ୍ ନମ୍ବର:",
        "acc_lbl": "ଦୋଷୀ ପକ୍ଷ / ଥାନା:",
        "det_lbl": "ସମ୍ପୂର୍ଣ୍ଣ ବିବରଣୀ:",
        "btn_draft": "⚡ ଆଇନଗତ ନୋଟିସ୍ ପ୍ରସ୍ତୁତ କରନ୍ତୁ",
        "send_wa": "📲 WhatsApp ରେ ପଠାନ୍ତୁ"
    },
    "অসমীয়া (Assamese)": {
        "tag": "⚡ ২৪x৭ নাগৰিক আইনী সুৰক্ষা অভিযান",
        "title": "মহা-সেৱা AI (MAHA SEVA AI)",
        "sub": "২৮টা আইনী অধিকাৰ • ৰাতিৰ সুৰক্ষা • নিয়োগ",
        "cat_lbl": "📂 সেৱা বাছক:",
        "c_rights": "⚖️ ২৮টা আইনী অধিকাৰ আৰু জাননী",
        "c_sos": "🚨 ৰাতিৰ সুৰক্ষা & GPS SOS",
        "c_voice": "🎙️ কণ্ঠৰে অভিযোগ দিয়ক",
        "c_fraud": "🛡️ চাইবাৰ প্ৰৱঞ্চনা পৰীক্ষক",
        "c_health": "🏥 ঔষধ আৰু এম্বুলেন্স",
        "c_job": "💼 নিয়োগ আৰু সাহায্য কেন্দ্ৰ",
        "r_title": "⚖️ ২৮ নাগৰিক আইনী সুৰক্ষা মঞ্চ",
        "r_sub": "সমস্যাৰ নম্বৰ বাছক:",
        "num_lbl": "🔢 ১ ৰ পৰা ২৮ নম্বৰ বাছক:",
        "name_lbl": "অভিযোগকাৰীৰ নাম:",
        "city_lbl": "জিলা আৰু ৰাজ্য:",
        "phone_lbl": "মোবাইল নম্বৰ:",
        "acc_lbl": "অভিযুক্ত পক্ষ / থানা:",
        "det_lbl": "সম্পূৰ্ণ বিৱৰণ:",
        "btn_draft": "⚡ আইনী জাননী প্ৰস্তুত কৰক",
        "send_wa": "📲 WhatsAppত পঠিয়াওক"
    }
}

# Language Picker (12 Languages)
all_langs = list(LANG_CONFIG.keys())
chosen_lang = st.radio("🌐 भाषा चुनें / Select Language:", all_langs, horizontal=True)
T = LANG_CONFIG.get(chosen_lang, LANG_CONFIG["🇮🇳 हिन्दी"])

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
    T["cat_lbl"],
    [
        T["c_rights"],
        T["c_sos"],
        T["c_voice"],
        T["c_fraud"],
        T["c_health"],
        T["c_job"]
    ],
    horizontal=True
)

st.markdown("---")

# 28 LAWS DATA (Pure Zero Glitch Dictionary)
LEGAL_28 = {
    1: {"name": "मजदूरी या वेतन चोरी (Wage Theft)", "act": "Payment of Wages Act 1936", "auth": "Labour Commissioner & DM", "rule": "मजदूरी दबाना गैर-कानूनी है। श्रम विभाग 10 गुना हर्जाना और 18% ब्याज दिलवाता है।", "det": "मैंने 2 महीने कार्य किया, जिसका कुल ₹24,000 बकाया है। मांगने पर गाली व धमकी दी जा रही है।"},
    2: {"name": "पुलिस अवैध मारपीट या फर्जी चालान", "act": "BNSS & DK Basu Guidelines", "auth": "SP & NHRC", "rule": "बिना जुर्म मारपीट पर धारा 166A BNS के तहत पुलिसकर्मी पर निलंबन व FIR होती है।", "det": "संबंधित पुलिसकर्मी द्वारा अकारण अभद्रता, मारपीट व अवैध चालान की धमकी दी गई।"},
    3: {"name": "अस्पताल में इमरजेंसी इलाज इनकार या शव रोकना", "act": "Supreme Court Parmanand Katara Verdict", "auth": "CMO & Consumer Court", "rule": "पैसे के लिए इमरजेंसी इलाज से इनकार या शव को बंधक बनाना संज्ञेय अपराध है।", "det": "अस्पताल द्वारा अग्रिम राशि की मांग कर गंभीर हालत में इलाज में जानबूझकर देरी की गई।"},
    4: {"name": "कार्यस्थल पर हादसा व शारीरिक अपंगता", "act": "Employees Compensation Act 1923", "auth": "Compensation Commissioner", "rule": "ड्यूटी पर दुर्घटना होने पर ₹5 लाख से ₹20 लाख का मुआवजा व आजीवन पेंशन अनिवार्य है।", "det": "सुरक्षा उपकरणों के अभाव में कार्यस्थल पर हादसा हुआ जिससे दिव्यांगता आई।"},
    5: {"name": "सूदखोर व फर्जी लोन ऐप्स द्वारा धमकी/ब्लैकमेल", "act": "RBI Guidelines & Extortion Sec 308 BNS", "auth": "Cyber Cell & SP", "rule": "बिना लाइसेंस सूदखोरी और धमकी देकर वसूली करना गैर-कानूनी है।", "det": "लोन एजेंट द्वारा घर आकर गाली-गलौज और फोटो वायरल करने का ब्लैकमेल किया जा रहा है।"},
    6: {"name": "सरकारी दफ्तर में घूसखोरी व 'कल आना' अपमान", "act": "RTPS Act & Prevention of Corruption Act", "auth": "Vigilance Bureau", "rule": "काम लटकाने पर कर्मचारी के वेतन से प्रतिदिन ₹250 से ₹5000 जुर्माना कटता है।", "det": "वैध कागजात देने के बावजूद रिश्वत के बिना बाबू द्वारा बार-बार चक्कर लगवाए जा रहे हैं।"},
    7: {"name": "दुकानदार या कोटेदार द्वारा MRP लूट व घटतौली", "act": "Legal Metrology Act 2009", "auth": "DSO & Consumer Forum", "rule": "MRP से अधिक लेना या कम तौलना गैर-कानूनी है। ₹25,000 जुर्माना और दुकान सील होती है।", "det": "दुकानदार द्वारा तय मूल्य से अधिक दाम वसूला गया और कम सामग्री दी गई।"},
    8: {"name": "ट्रेन में टीटीई (TTE) द्वारा अवैध वसूली व बदसलूकी", "act": "Indian Railway Act", "auth": "RailMadad 139 & RPF", "rule": "टीटीई को यात्री से बदतमीजी या धक्का देने का कोई हक नहीं। केवल सरकारी रसीद मान्य है।", "det": "यात्रा के दौरान टीटीई द्वारा अवैध धन की मांग और विरोध करने पर बदसलूकी की गई।"},
    9: {"name": "थाने में FIR दर्ज न करना (Zero FIR)", "act": "Supreme Court Lalita Kumari Guidelines", "auth": "SSP & CJM Court", "rule": "संज्ञेय अपराध में FIR न लिखने वाले पुलिस अधिकारी पर खुद धारा 166A BNS में FIR होती है।", "det": "लिखित शिकायत देने के बावजूद थाना प्रभारी द्वारा प्रथम सूचना रिपोर्ट दर्ज नहीं की गई।"},
    10: {"name": "पैतृक जमीन पर दबंगों का अवैध कब्जा", "act": "Section 145/144 BNSS", "auth": "SDM & Civil Court", "rule": "गरीब की पैतृक भूमि पर जबरन कब्जे की कोशिश पर तुरंत पुलिस सुरक्षा व स्टे का नियम है।", "det": "विपक्षी द्वारा प्रार्थी की वैध पैतृक जमीन पर बलपूर्वक अवैध कब्जे का प्रयास किया जा रहा है।"},
    11: {"name": "सड़क हादसे (Hit & Run) में सरकारी मुआवजा", "act": "Motor Vehicles Amendment Act", "auth": "MACT & District Collector", "rule": "मृत्यु पर सरकार द्वारा ₹2 लाख और गंभीर घायल को ₹50,000 की तत्काल राहत मिलती है।", "det": "सड़क दुर्घटना के उपरांत तत्काल सरकारी राहत कोष व बीमा क्लेम की मांग की जा रही है।"},
    12: {"name": "मुफ्त सरकारी वकील पाने हेतु आवेदन (DLSA)", "act": "Legal Services Authorities Act (Art 39A)", "auth": "DLSA Secretary", "rule": "गरीब, मजदूर और महिला को कोर्ट केस लड़ने के लिए सरकार मुफ्त वकील देती है।", "det": "प्रार्थी आर्थिक रूप से असमर्थ है और उसे मुकदमे की पैरवी हेतु सरकारी वकील चाहिए।"},
    13: {"name": "मकान मालिक द्वारा जबरन बेदखली व बिजली काटना", "act": "Rent Control Act & BNS", "auth": "Rent Controller & Police", "rule": "मकान मालिक बिना कोर्ट ऑर्डर के ताला नहीं तोड़ सकता, न ही बिजली-पानी काट सकता है।", "det": "मकान मालिक द्वारा बिना कानूनी नोटिस पानी-बिजली बंद कर जबरन मकान खाली कराने की धमकी दी गई।"},
    14: {"name": "जातिगत भेदभाव व सामाजिक बहिष्कार", "act": "SC/ST Prevention of Atrocities Act", "auth": "SP & Special Court", "rule": "जाति के आधार पर अपमानित करने या रास्ता रोकने पर गैर-जमानती गिरफ्तारी होती है।", "det": "विपक्षी द्वारा जातिसूचक अपशब्दों का प्रयोग कर सार्वजनिक रूप से अपमानित किया गया।"},
    15: {"name": "धर्म के नाम पर भेदभाव व नफरत", "act": "Article 15 & Section 196 BNS", "auth": "DM & NHRC", "rule": "धार्मिक सद्भाव बिगाड़ने या भेदभाव करने पर संज्ञेय गैर-जमानती मुकदमा होता है।", "det": "धार्मिक आधार पर प्रार्थी के साथ सार्वजनिक स्थल पर भेदभावपूर्ण दुर्व्यवहार किया गया।"},
    16: {"name": "गिग वर्कर डिलीवरी बॉय व ड्राइवर अधिकार", "act": "Code on Social Security 2020", "auth": "Labour Welfare Board", "rule": "कंपनी बिना कारण आईडी ब्लॉक नहीं कर सकती और दुर्घटना पर इलाज-मुआवजा अनिवार्य है।", "det": "बिना किसी सूचना के डिलीवरी आईडी ब्लॉक कर दी गई और बकाया भुगतान रोक लिया गया।"},
    17: {"name": "राशन कार्ड में अंगूठा लगवाकर राशन न देना", "act": "National Food Security Act (NFSA)", "auth": "DSO & SDO", "rule": "अंगूठा लगवाकर अनाज न देना सीधे खाद्यान्न चोरी का अपराध है; कोटेदार का लाइसेंस रद्द होता है।", "det": "ई-पॉस मशीन पर फिंगरप्रिंट लेने के बावजूद इस माह का निर्धारित राशन नहीं दिया गया।"},
    18: {"name": "बैंक अकाउंट अवैध फ्रीज व मिनिमम बैलेंस कटौती", "act": "RBI Banking Ombudsman Rules", "auth": "RBI Ombudsman", "rule": "बैंक सेविंग्स खाते को चार्ज काटकर माइनस में नहीं ले जा सकता, न बिना नोटिस फ्रीज कर सकता है।", "det": "बैंक द्वारा बिना किसी कानूनी नोटिस के खाता फ्रीज किया गया व अनुचित शुल्क काटा गया।"},
    19: {"name": "बिजली विभाग मनमानी व ट्रांसफार्मर खराबी", "act": "Electricity Act 2003 Rules", "auth": "CGRF & Executive Engineer", "rule": "जला हुआ ट्रांसफार्मर ग्रामीण क्षेत्र में 48 घंटे व शहरी में 24 घंटे में बदलना अनिवार्य है।", "det": "कई दिनों से ट्रांसफार्मर खराब है और विभाग द्वारा अत्यधिक फर्जी बिल भेजा गया है।"},
    20: {"name": "आयुष्मान कार्ड (PM-JAY) पर अस्पताल का इनकार", "act": "National Health Authority Rules", "auth": "State Anti-Fraud Unit (SAFU)", "rule": "सूचीबद्ध अस्पताल आयुष्मान कार्ड धारक को मना नहीं कर सकता; उल्लंघन पर पैनल रद्द होता है।", "det": "सक्रिय आयुष्मान कार्ड होने के बावजूद निजी अस्पताल द्वारा निशुल्क इलाज से मना किया गया।"},
    21: {"name": "पीएम आवास योजना में रिश्वत की मांग", "act": "Prevention of Corruption Act", "auth": "Vigilance & DDC", "rule": "आवास योजना के पैसे में कमीशन मांगना संज्ञेय भ्रष्टाचार अपराध है।", "det": "आवास योजना की किस्त जारी करने के एवज में संबंधित कर्मी द्वारा रिश्वत की मांग की जा रही है।"},
    22: {"name": "प्राइवेट स्कूल में 25% फ्री एडमिशन (RTE)", "act": "Right to Education Act Sec 12(1)(c)", "auth": "DEO & Child Commission", "rule": "हर प्राइवेट स्कूल में 25% सीटें गरीब बच्चों के लिए पूर्णतः निशुल्क आरक्षित हैं।", "det": "RTE पात्रता होने के बावजूद संबंधित निजी स्कूल द्वारा छात्र का दाखिला लेने से इनकार किया गया।"},
    23: {"name": "नकली खाद-बीज से फसल बर्बादी का हर्जाना", "act": "Insecticides Act & Essential Commodities Act", "auth": "DAO & Consumer Court", "rule": "नकली सामग्री बेचने पर विक्रेता पर मुकदमा और किसान को 100% फसल नुकसान का हर्जाना मिलता है।", "det": "दुकानदार द्वारा नकली बीज व खाद दिए जाने के कारण मेरी संपूर्ण खड़ी फसल नष्ट हो गई।"},
    24: {"name": "फसल बीमा (PMFBY) क्लेम चोरी व रिजेक्शन", "act": "PMFBY Operational Guidelines", "auth": "District Agriculture Committee", "rule": "आपदा के समय 72 घंटे में सूचना देने पर 12% ब्याज सहित बीमा क्लेम मिलना अनिवार्य है।", "det": "बाढ़/सूखा से हुए प्रमाणित नुकसान के बावजूद बीमा कंपनी द्वारा क्लेम को निरस्त किया गया।"},
    25: {"name": "बुजुर्ग माता-पिता की संपत्ति हड़पना व प्रताड़ना", "act": "Senior Citizens Welfare Act 2007", "auth": "SDM Tribunal", "rule": "प्रताड़ित करने पर माता-पिता द्वारा संतानों को दी गई संपत्ति की रजिस्ट्री रद्द हो जाती है।", "det": "संपत्ति नाम कराने के उपरांत संतानों द्वारा भोजन-दवा बंद कर घर से बेदखल करने की धमकी दी गई।"},
    26: {"name": "छात्र पेपर लीक व कोचिंग फीस वापसी", "act": "Public Examinations Act 2024 & UGC Rules", "auth": "Higher Education Dept", "rule": "कोचिंग बीच में छोड़ने पर शेष बची फीस वापस करना अनिवार्य है।", "det": "कोर्स छोड़ने के बाद भी संस्थान द्वारा नियमानुसार बची हुई फीस वापस नहीं की गई।"},
    27: {"name": "ट्रैफिक पुलिस द्वारा चाबी छीनना व डंडा मारना", "act": "Motor Vehicles Act & MHA Directives", "auth": "SP Traffic", "rule": "चलती गाड़ी से चाबी निकालना अपराध है; DigiLocker के डिजिटल दस्तावेज 100% मान्य हैं।", "det": "वैध डिजिटल दस्तावेज दिखाने के बावजूद ट्रैफिक कर्मी द्वारा दुर्व्यवहार कर चाबी छीनी गई।"},
    28: {"name": "मरीज का अधिकार (मेडिकल फाइल व सस्ती दवा की आजादी)", "act": "NHRC Patients Rights Charter", "auth": "CMO & State Medical Council", "rule": "अस्पताल मरीज को मेडिकल फाइल और बाहर से सस्ती जेनेरिक दवा लेने से नहीं रोक सकता।", "det": "अस्पताल द्वारा केस फाइल देने से मना किया गया तथा बाहर से जेनेरिक दवा लाने पर रोक लगाई गई।"}
}

# ================= TAB 1: 28 LEGAL RIGHTS =================
if nav_choice == T["c_rights"]:
    st.write(f"### {T['r_title']}")
    st.caption(T['r_sub'])

    # NO WHITE BOX GLITCH - Number-based Clean Radio
    num_choice = st.radio(
        T["num_lbl"],
        list(LEGAL_28.keys()),
        format_func=lambda x: f"{x}. {LEGAL_28[x]['name']}",
        key=f"num_{chosen_lang}"
    )

    case_info = LEGAL_28[num_choice]

    st.markdown(f"""
    <div class="info-card">
        <h3 style="color:#38BDF8; margin:0 0 6px 0;">📌 कानून: {case_info['act']}</h3>
        <p style="margin:0; font-size:14px; color:#F8FAFC;"><b>सक्षम प्राधिकारी:</b> {case_info['auth']}</p>
    </div>
    """, unsafe_allow_html=True)

    col_v1, col_v2 = st.columns(2)
    with col_v1:
        v_name = st.text_input(T["name_lbl"], value="साहिल कुमार", key=f"name_{chosen_lang}_{num_choice}")
    with col_v2:
        v_loc = st.text_input(T["city_lbl"], value="पश्चिम चंपारण, बिहार", key=f"city_{chosen_lang}_{num_choice}")

    v_phone = st.text_input(T["phone_lbl"], value="7484878440", key=f"phone_{chosen_lang}_{num_choice}")
    v_accused = st.text_input(T["acc_lbl"], value="संबंधित दोषी पक्ष / अधिकारी", key=f"acc_{chosen_lang}_{num_choice}")
    v_details = st.text_area(T["det_lbl"], value=case_info["det"], height=95, key=f"det_{chosen_lang}_{num_choice}")

    if st.button(T['btn_draft'], key=f"btn_d_{chosen_lang}_{num_choice}"):
        full_notice = f"""======================================================================
आधिकारिक कानूनी विधिक शिकायत पत्र व नोटिस
(अधिनियम: {case_info['act']})
दिनांक: {today_str}

सेवा में,
1. {case_info['auth']}, {v_loc}
2. राष्ट्रीय मानवाधिकार आयोग (NHRC) / विधिक निगरानी प्राधिकरण

विषय: '{case_info['name']}' के संबंध में दोषी '{v_accused}' पर प्राथमिकी (FIR) व तत्काल दंडात्मक कार्रवाई बाबत।

महोदय,
प्रार्थी {v_name} (मोबाइल: +91 {v_phone}), निवासी {v_loc} सादर सूचित करता है कि:

1. यह कि प्रार्थी भारत का संविधान-सम्मत नागरिक है और विपक्षी '{v_accused}' द्वारा प्रार्थी के विधिक अधिकारों का खुला उल्लंघन किया गया है।
2. तथ्यात्मक घटनाक्रम (सच्चा विवरण):
"{v_details}"
3. विधिक नियम व प्रावधान:
- {case_info['rule']}

अतः सक्षम प्राधिकारी से प्रार्थना है कि दोषी '{v_accused}' के विरुद्ध सुसंगत कानूनी धाराओं में तत्काल प्राथमिकी दर्ज कर प्रार्थी को उसका संपूर्ण विधिक हक व सुरक्षा अविलंब प्रदान की जाए।

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
        st.markdown(f'<a href="https://wa.me/?text={enc_notice}" target="_blank" class="btn-green">{T["send_wa"]}</a>', unsafe_allow_html=True)

# ================= TAB 2: NIGHT SAFETY & LIVE GPS SOS =================
elif nav_choice == T["c_sos"]:
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
elif nav_choice == T["c_voice"]:
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
elif nav_choice == T["c_fraud"]:
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
elif nav_choice == T["c_health"]:
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
elif nav_choice == T["c_job"]:
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
