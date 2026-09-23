import streamlit as st
import streamlit.components.v1 as components
import urllib.parse
from datetime import datetime

# 1. Page Configuration
st.set_page_config(
    page_title="Maha Seva AI — Pan-India Citizen Legal Mission",
    page_icon="🇮🇳",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Universal Dark Theme CSS
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

    input, .stTextInput input, textarea, .stTextArea textarea, .stNumberInput input {
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

    .btn-blue {
        display: block;
        background: linear-gradient(90deg, #2563EB 0%, #1D4ED8 100%);
        color: #FFFFFF !important;
        text-align: center;
        font-weight: 800;
        font-size: 15px;
        padding: 12px;
        border-radius: 10px;
        text-decoration: none;
        margin: 8px 0;
        box-shadow: 0 4px 15px rgba(37, 99, 235, 0.4);
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

# ALL 12 LANGUAGES COMPLETE MAPPING
LANGUAGES = {
    "🇮🇳 हिन्दी": {
        "tag": "⚡ 24x7 अखंड भारत नागरिक व विधिक सुरक्षा मिशन",
        "title": "महा-सेवा AI (MAHA SEVA AI)",
        "sub": "28 कानूनी धाराएँ • अपनी शिकायत • रात की सुरक्षा • बोलकर शिकायत • PDF",
        "cat_lbl": "📂 सेवा श्रेणी चुनें:",
        "c_rights": "⚖️ 28 विधिक अधिकार, नोटिस व PDF",
        "c_sos": "🚨 रात की सुरक्षा व लाइव GPS SOS",
        "c_voice": "🎙️ बोलकर शिकायत दर्ज करें (माइक)",
        "c_fraud": "🛡️ साइबर फ्रॉड व मैसेज चेकर",
        "c_health": "🏥 दवा व एम्बुलेंस सहायता",
        "c_job": "💼 रोज़गार व हेल्पर डेस्क",
        "sos_h": "🚨 24x7 रात की सुरक्षा व लाइव GPS SOS",
        "sos_sub": "रात में किसी भी खतरे, पीछा करने या घेरने पर तुरंत कॉल करें:",
        "sos_c1": "📞 112 पुलिस आपातकाल",
        "sos_c2": "📞 1090 वीमेन पावर लाइन",
        "sos_c3": "📞 181 महिला हेल्पलाइन",
        "sos_note": "(बिना इंटरनेट के भी सीधी कॉल लगेगी - 100% फ्री 24 घंटे)",
        "gps_btn": "📡 मेरा सटीक लाइव GPS पता निकालें",
        "family_lbl": "परिवार / भाई / पिता का मोबाइल नंबर:",
        "victim_lbl": "पीड़ित / आपका नाम:",
        "loc_lbl": "वर्तमान जगह / सड़क का नाम:",
        "sos_wa_btn": "📲 1-क्लिक परिवार को लोकेशन व SOS भेजें",
        "siren_h": "🔊 पैनिक सायरन (हमलावर को भगाने हेतु)",
        "siren_btn": "🚨 तेज़ अलार्म सायरन बजाएँ (Play Siren)",
        "mode_lbl": "शिकायत दर्ज करने का तरीका चुनें:",
        "mode_sec": "🔢 सेक्शन नंबर से चुनें (1 से 28 कानून)",
        "mode_custom": "✍️ अपनी खुद की नई शिकायत लिखें (Custom Complaint)",
        "sec_prompt": "सेक्शन नंबर दर्ज करें (1 से 28):",
        "name_lbl": "पीड़ित / प्रार्थी का नाम:",
        "city_lbl": "जिला व राज्य:",
        "phone_lbl": "मोबाइल नंबर:",
        "acc_lbl": "दोषी पक्ष / अधिकारी / कंपनी का नाम:",
        "det_lbl": "सच्चा घटनाक्रम विवरण (Fact Details):",
        "btn_draft": "⚡ आधिकारिक कानूनी नोटिस तैयार करें",
        "success_msg": "🟢 आधिकारिक विधिक नोटिस तैयार:",
        "doc_box_lbl": "📄 तैयार कानूनी दस्तावेज:",
        "download_txt_btn": "📥 कानूनी शिकायत पत्र डाउनलोड करें (.txt)",
        "pdf_btn": "🖨️ कानूनी नोटिस को PDF में सेव/प्रिंट करें",
        "shield_title": "⚖️ इस मामले में आपका कानूनी कवच:",
        "send_wa": "📲 यह शिकायत WhatsApp पर भेजें",
        "def_name": "साहिल कुमार",
        "def_city": "पश्चिम चंपारण, बिहार",
        "def_acc": "संबंधित दोषी पक्ष / अधिकारी",
        "custom_sub_lbl": "शिकायत का विषय (Subject):",
        "custom_sub_val": "दबंगों व भ्रष्ट कर्मियों द्वारा अवैध उत्पीड़न बाबत",
        "custom_act": "भारतीय संविधान, बीएनएस 2023 एवं संबंधित विशेष अधिनियम",
        "custom_auth": "जिलाधिकारी (DM) / पुलिस अधीक्षक (SP) / सक्षम प्राधिकारी",
        "custom_rule": "भारत के संविधान अनुसार प्रत्येक नागरिक को विधिक संरक्षण व तुरंत न्याय पाने का मौलिक अधिकार प्राप्त है।",
        "custom_det": "प्रार्थी के साथ विपक्षी द्वारा अन्यायपूर्ण व गैर-कानूनी ढंग से प्रताड़ित किया गया है, जिसकी लिखित सूचना प्रस्तुत है।"
    },
    "🇬🇧 English": {
        "tag": "⚡ 24x7 Pan-India Sovereign Citizen Legal Mission",
        "title": "MAHA SEVA AI — Citizen Sovereign Portal",
        "sub": "28 Sovereign Sections • Custom Complaint • Night SOS • Voice Help • PDF",
        "cat_lbl": "📂 Select Service Category:",
        "c_rights": "⚖️ 28 Legal Rights, Notice & PDF",
        "c_sos": "🚨 Night Safety & Live GPS SOS",
        "c_voice": "🎙️ Voice-to-Text Complaint (Mic)",
        "c_fraud": "🛡️ Cyber Shield & Fraud Verifier",
        "c_health": "🏥 Healthcare & Free Ambulance",
        "c_job": "💼 Pan-India Employment Desk",
        "sos_h": "🚨 24x7 Night Safety & Live GPS SOS",
        "sos_sub": "In case of any danger, stalking, or road harassment call immediately:",
        "sos_c1": "📞 112 National Police",
        "sos_c2": "📞 1090 Women Power Line",
        "sos_c3": "📞 181 Women Crisis Line",
        "sos_note": "(Works without internet directly via SIM - 100% Free 24/7)",
        "gps_btn": "📡 Fetch My Live GPS Location Link",
        "family_lbl": "Family / Father / Brother Mobile Number:",
        "victim_lbl": "Victim / Your Name:",
        "loc_lbl": "Current Road / Landmark Location:",
        "sos_wa_btn": "📲 1-Click Send SOS & Location via WhatsApp",
        "siren_h": "🔊 Panic Alarm Siren (Deter Attackers)",
        "siren_btn": "🚨 Play Loud Siren Alarm",
        "mode_lbl": "Select Filing Method:",
        "mode_sec": "🔢 Select by Section Number (1 to 28)",
        "mode_custom": "✍️ Write Your Own Custom Complaint",
        "sec_prompt": "Enter Section Number (1 to 28):",
        "name_lbl": "Complainant Name:",
        "city_lbl": "District & State:",
        "phone_lbl": "Mobile Number:",
        "acc_lbl": "Accused Party / Official / Agency:",
        "det_lbl": "Factual Details of Injustice:",
        "btn_draft": "⚡ Draft Official Court-Grade Legal Notice",
        "success_msg": "🟢 Official Legal Notice & Document Ready:",
        "doc_box_lbl": "📄 Prepared Legal Document:",
        "download_txt_btn": "📥 Download Legal Notice File (.txt)",
        "pdf_btn": "🖨️ Save as PDF / Print Official Notice",
        "shield_title": "⚖️ Your Statutory Legal Protection:",
        "send_wa": "📲 Send Notice via WhatsApp",
        "def_name": "Sahil Kumar",
        "def_city": "West Champaran, Bihar",
        "def_acc": "Accused Employer / Officer / Agency",
        "custom_sub_lbl": "Complaint Subject:",
        "custom_sub_val": "Regarding Unlawful Harassment and Violation of Fundamental Rights",
        "custom_act": "Constitution of India, BNS 2023 & Relevant Special Statutes",
        "custom_auth": "District Magistrate (DM) / Superintendent of Police (SP)",
        "custom_rule": "Every citizen has the guaranteed fundamental right to legal remedy and justice under the Constitution of India.",
        "custom_det": "The complainant has been unlawfully aggrieved and harassed by the accused party, and formal relief is sought."
    },
    "বাংলা (Bengali)": {
        "tag": "⚡ ২৪x৭ অখণ্ড ভারত নাগরিক আইনি মিশন",
        "title": "মহা-সেবা AI (MAHA SEVA AI)",
        "sub": "২৮টি আইনি অধিকার • নৈশ নিরাপত্তা • ভয়েস অভিযোগ • কর্মসংস্থান • PDF",
        "cat_lbl": "📂 পরিষেবা বিভাগ নির্বাচন করুন:",
        "c_rights": "⚖️ ২৮টি আইনি অধিকার ও নোটিশ",
        "c_sos": "🚨 নৈশ নিরাপত্তা ও GPS SOS",
        "c_voice": "🎙️ মুখে বলে অভিযোগ (মাইক)",
        "c_fraud": "🛡️ সাইবার সুরক্ষা ও প্রতারণা যাচাই",
        "c_health": "🏥 ওষুধ ও অ্যাম্বুলেন্স সহায়তা",
        "c_job": "💼 কর্মসংস্থান ও হেল্পার ডেস্ক",
        "sos_h": "🚨 ২৪x৭ নৈশ নিরাপত্তা ও লাইভ GPS SOS",
        "sos_sub": "রাস্তায় বিপদে পড়লে অবিলম্বে কল করুন:",
        "sos_c1": "📞 ১১২ পুলিশ জরুরি সেবা",
        "sos_c2": "📞 ১০৯০ মহিলা সুরক্ষা লাইন",
        "sos_c3": "📞 ১৮১ মহিলা হেল্পলাইন",
        "sos_note": "(ইন্টারনেট ছাড়াও সরাসরি কল করা যাবে - সম্পূর্ণ ফ্রি)",
        "gps_btn": "📡 আমার লাইভ GPS অবস্থান বের করুন",
        "family_lbl": "পরিবারের মোবাইল নম্বর:",
        "victim_lbl": "আপনার নাম:",
        "loc_lbl": "বর্তমান অবস্থান বা রাস্তার নাম:",
        "sos_wa_btn": "📲 ১-ক্লিকে পরিবারকে লোকেশন ও SOS পাঠান",
        "siren_h": "🔊 প্যানিক অ্যালার্ম সাইরেন",
        "siren_btn": "🚨 জোরে সাইরেন বাজান (Play Siren)",
        "mode_lbl": "অভিযোগের পদ্ধতি বেছে নিন:",
        "mode_sec": "🔢 ধারা নম্বর অনুযায়ী (১ থেকে ২৮)",
        "mode_custom": "✍️ নিজের নতুন অভিযোগ লিখুন",
        "sec_prompt": "ধারা নম্বর লিখুন (১ থেকে ২৮):",
        "name_lbl": "অভিযোগকারীর নাম:",
        "city_lbl": "জেলা ও রাজ্য:",
        "phone_lbl": "মোবাইল নম্বর:",
        "acc_lbl": "অভিযুক্ত পক্ষ / থানা / ঠিকাদার:",
        "det_lbl": "ঘটনার সম্পূর্ণ বিবরণ:",
        "btn_draft": "⚡ আইনি অভিযোগ পত্র তৈরি করুন",
        "success_msg": "🟢 আইনি নোটিশ সফলভাবে তৈরি হয়েছে:",
        "doc_box_lbl": "📄 প্রস্তুতকৃত আইনি নোটিশ:",
        "download_txt_btn": "📥 আইনি নোটিশ ডাউনলোড করুন (.txt)",
        "pdf_btn": "🖨️ নোটিশটি PDF এ প্রিন্ট / সেভ করুন",
        "shield_title": "⚖️ আপনার আইনি সুরক্ষার ধারা:",
        "send_wa": "📲 হোয়াটসঅ্যাপে নোটিশ পাঠান",
        "def_name": "সাহিল কুমার",
        "def_city": "পশ্চিম চম্পারণ, বিহার",
        "def_acc": "অভিযুক্ত পক্ষ / সংশ্লিষ্ট কর্মকর্তা",
        "custom_sub_lbl": "অভিযোগের বিষয়:",
        "custom_sub_val": "বেআইনি হয়রানি এবং অধিকার লঙ্ঘন প্রসঙ্গে",
        "custom_act": "ভারতীয় সংবিধান ও বিএনএস ২০২৩ আইন",
        "custom_auth": "জেলা শাসক (DM) / পুলিশ সুপার (SP)",
        "custom_rule": "সংবিধানের অধীনে প্রতিটি নাগরিকের আইনি সুরক্ষা পাওয়ার পূর্ণ অধিকার রয়েছে।",
        "custom_det": "অভিযুক্ত পক্ষ কর্তৃক অন্যায়ভাবে ক্ষতিগ্রস্ত হওয়ায় এই অভিযোগ দায়ের করা হচ্ছে।"
    },
    "मराठी (Marathi)": {
        "tag": "⚡ २४x७ अखंड भारत नागरिक कायदेशीर सुरक्षा मिशन",
        "title": "महा-सेवा AI (MAHA SEVA AI)",
        "sub": "२८ कायदेशीर अधिकार • रात्रीची सुरक्षा • थेट नोकरी • PDF",
        "cat_lbl": "📂 सेवा श्रेणी निवडा:",
        "c_rights": "⚖️ २८ कायदेशीर अधिकार व नोटीस",
        "c_sos": "🚨 रात्रीची सुरक्षा व GPS SOS",
        "c_voice": "🎙️ बोलून तक्रार नोंदवा (माइक)",
        "c_fraud": "🛡️ सायबर फसवणूक तपासक",
        "c_health": "🏥 औषधे व रुग्णवाहिका",
        "c_job": "💼 रोजगार व थेट नोकरी",
        "sos_h": "🚨 २४x७ रात्रीची सुरक्षा व लाइव्ह GPS SOS",
        "sos_sub": "रात्रीच्या वेळी कोणताही धोका निर्माण झाल्यास थेट संपर्क करा:",
        "sos_c1": "📞 ११२ पोलीस आपत्कालीन",
        "sos_c2": "📞 १०९० महिला हेल्पलाइन",
        "sos_c3": "📞 १८१ महिला सुरक्षा",
        "sos_note": "(इंटरनेट नसतानाही थेट कॉल लागेल - पूर्णपणे मोफत)",
        "gps_btn": "📡 माझे लाइव्ह GPS लोकेशन मिळवा",
        "family_lbl": "कुटुंबातील सदस्याचा मोबाईल नंबर:",
        "victim_lbl": "तुमचे पूर्ण नाव:",
        "loc_lbl": "सध्याचे ठिकाण / रस्ता:",
        "sos_wa_btn": "📲 १-क्लिकवर कुटुंबाला SOS पाठवा",
        "siren_h": "🔊 मोठ्या आवाजाचा सायरन",
        "siren_btn": "🚨 अलार्म सायरन वाजवा (Play Siren)",
        "mode_lbl": "तक्रार पद्धत निवडा:",
        "mode_sec": "🔢 कलम क्रमांकानुसार (१ ते २८)",
        "mode_custom": "✍️ स्वतःची तक्रार नोंदवा",
        "sec_prompt": "कलम क्रमांक टाका (१ ते २८):",
        "name_lbl": "तक्रारदाराचे नाव:",
        "city_lbl": "जिल्हा व राज्य:",
        "phone_lbl": "मोबाईल नंबर:",
        "acc_lbl": "दोषी कंत्राटदार / अधिकारी:",
        "det_lbl": "घटनेचा संपूर्ण तपशील:",
        "btn_draft": "⚡ कायदेशीर नोटीस तयार करा",
        "success_msg": "🟢 कायदेशीर नोटीस तयार झाली आहे:",
        "doc_box_lbl": "📄 तयार कायदेशीर नोटीस:",
        "download_txt_btn": "📥 कायदेशीर नोटीस डाउनलोड करा (.txt)",
        "pdf_btn": "🖨️ PDF म्हणून सेव्ह / प्रिंट करा",
        "shield_title": "⚖️ आपले कायदेशीर संरक्षण:",
        "send_wa": "📲 WhatsApp वर पाठवा",
        "def_name": "साहिल कुमार",
        "def_city": "पश्चिम चंपारण, बिहार",
        "def_acc": "संबंधित दोषी व्यक्ती / अधिकारी",
        "custom_sub_lbl": "तक्रारीचा विषय:",
        "custom_sub_val": "बेकायदेशीर छळ व हक्क उल्लंघनाबाबत",
        "custom_act": "भारतीय संविधान आणि बीएनएस २०२३",
        "custom_auth": "जिल्हाधिकारी (DM) / पोलीस अधीक्षक (SP)",
        "custom_rule": "संविधानानुसार प्रत्येक नागरिकाला कायदेशीर न्यायाचा मूलभूत अधिकार आहे.",
        "custom_det": "माझ्यावर झालेल्या अन्यायाविरुद्ध तात्काळ कायदेशीर कारवाई करण्यात यावी."
    },
    "தமிழ் (Tamil)": {
        "tag": "⚡ 24x7 குடிமக்கள் சட்டப் பாதுகாப்பு தளம்",
        "title": "மகா-சேவா AI (MAHA SEVA AI)",
        "sub": "28 சட்ட உரிமைகள் • இரவு பாதுகாப்பு • வேலைவாய்ப்பு • PDF",
        "cat_lbl": "📂 சேவையைத் தேர்ந்தெடுக்கவும்:",
        "c_rights": "⚖️ 28 சட்ட உரிமைகள் & நோட்டீஸ்",
        "c_sos": "🚨 இரவு பாதுகாப்பு & GPS SOS",
        "c_voice": "🎙️ குரல் மூலம் புகார் (மைக்)",
        "c_fraud": "🛡️ இணைய மோசடி சரிபார்ப்பு",
        "c_health": "🏥 மருத்துவம் & ஆம்புலன்ஸ்",
        "c_job": "💼 வேலைவாய்ப்பு தகவல்",
        "sos_h": "🚨 24x7 இரவு நேர அவசர உதவி & GPS SOS",
        "sos_sub": "ஆபத்து ஏற்பட்டால் உடனடியாக அழைக்கவும்:",
        "sos_c1": "📞 112 காவல் உதவி",
        "sos_c2": "📞 1090 பெண்கள் உதவி எண்",
        "sos_c3": "📞 181 பெண்கள் உதவி மையம்",
        "sos_note": "(இணையம் இல்லாமலும் நேரடியாக அழைப்பு செல்லும் - முற்றிலும் இலவசம்)",
        "gps_btn": "📡 எனது நேரலை GPS இருப்பிடத்தைப் பெறு",
        "family_lbl": "குடும்பத்தினர் மொபைல் எண்:",
        "victim_lbl": "உங்கள் பெயர்:",
        "loc_lbl": "தற்போதைய இடம் / சாலையின் பெயர்:",
        "sos_wa_btn": "📲 1-கிளிக்கில் SOS அனுப்புக",
        "siren_h": "🔊 எச்சரிக்கை சைரன் ஒலி",
        "siren_btn": "🚨 சைரன் ஒலி எழுப்பு",
        "mode_lbl": "புகார் பதிவு செய்யும் முறை:",
        "mode_sec": "🔢 பிரிவு எண் மூலம் (1 முதல் 28 வரை)",
        "mode_custom": "✍️ உங்கள் சொந்த புகாரை எழுதவும்",
        "sec_prompt": "பிரிவு எண் உள்ளிடவும் (1 முதல் 28):",
        "name_lbl": "புகார்தாரர் பெயர்:",
        "city_lbl": "மாவட்டம் & மாநிலம்:",
        "phone_lbl": "மொபைல் எண்:",
        "acc_lbl": "எதிர்தரப்பு நிறுவனம் / அதிகாரி:",
        "det_lbl": "நிகழ்வின் முழு விவரம்:",
        "btn_draft": "⚡ சட்டப்பூர்வ நோட்டீஸ் உருவாக்கவும்",
        "success_msg": "🟢 சட்டப்பூர்வ நோட்டீஸ் தயாராக உள்ளது:",
        "doc_box_lbl": "📄 தயாரான சட்ட ஆவணம்:",
        "download_txt_btn": "📥 நோட்டீஸை பதிவிறக்குக (.txt)",
        "pdf_btn": "🖨️ PDF ஆக சேமி / அச்சிடுக",
        "shield_title": "⚖️ உங்கள் சட்டப் பாதுகாப்பு:",
        "send_wa": "📲 வாட்ஸ்அப்பில் பகிரவும்",
        "def_name": "சாஹில் குமார்",
        "def_city": "மேற்கு சம்பரான், பீகார்",
        "def_acc": "எதிர்தரப்பு அதிகாரி / நிறுவனம்",
        "custom_sub_lbl": "புகாரின் தலைப்பு:",
        "custom_sub_val": "சட்டவிரோத அத்துமீறல் மற்றும் உரிமை மீறல் குறித்து",
        "custom_act": "இந்திய அரசியலமைப்பு மற்றும் BNS 2023",
        "custom_auth": "மாவட்ட ஆட்சியர் (DM) / காவல் கண்காணிப்பாளர் (SP)",
        "custom_rule": "ஒவ்வொரு குடிமகனுக்கும் உடனடி நீதி பெற சட்டப்பூர்வ உரிமை உண்டு.",
        "custom_det": "எதிர்தரப்பினரால் இழைக்கப்பட்ட அநீதி குறித்து உடனடியாக நடவடிக்கை எடுக்க வேண்டுகிறேன்."
    },
    "తెలుగు (Telugu)": {
        "tag": "⚡ 24x7 పౌర హక్కుల రక్షణ మిషన్",
        "title": "మహా-సేవా AI (MAHA SEVA AI)",
        "sub": "28 చట్టపరమైన హక్కులు • రాత్రి రక్షణ • ఉపాధి • PDF",
        "cat_lbl": "📂 సేవను ఎంచుకోండి:",
        "c_rights": "⚖️ 28 చట్టపరమైన హక్కులు & నోటీసు",
        "c_sos": "🚨 రాత్రి రక్షణ & GPS SOS",
        "c_voice": "🎙️ వాయిస్ ద్వారా ఫిర్యాదు",
        "c_fraud": "🛡️ సైబర్ మోసాల తనిఖీ",
        "c_health": "🏥 మందులు & అంబులెన్స్",
        "c_job": "💼 ఉపాధి & ఉద్యోగాలు",
        "sos_h": "🚨 24x7 రాత్రి రక్షణ & లైవ్ GPS SOS",
        "sos_sub": "ఏదైనా ప్రమాదం జరిగితే వెంటనే కాల్ చేయండి:",
        "sos_c1": "📞 112 పోలీసు అత్యవసర సహాయం",
        "sos_c2": "📞 1090 మహిళా భద్రత",
        "sos_c3": "📞 181 మహిళా హెల్ప్‌లైన్",
        "sos_note": "(ఇంటర్నెట్ లేకుండా నేరుగా కాల్ చేయవచ్చు - ఉచితం)",
        "gps_btn": "📡 నా లైవ్ GPS లొకేషన్ పొందండి",
        "family_lbl": "కుటుంబ సభ్యుల మొబైల్ నంబర్:",
        "victim_lbl": "మీ పేరు:",
        "loc_lbl": "ప్రస్తుత ప్రాంతం లేదా రహదారి పేరు:",
        "sos_wa_btn": "📲 1-క్లిక్‌తో SOS పంపండి",
        "siren_h": "🔊 పానిక్ అలారం సైరన్",
        "siren_btn": "🚨 సైరన్ మోగించండి (Play Siren)",
        "mode_lbl": "ఫిర్యాదు విధానాన్ని ఎంచుకోండి:",
        "mode_sec": "🔢 సెక్షన్ సంఖ్య ద్వారా (1 నుండి 28)",
        "mode_custom": "✍️ మీ స్వంత సమస్యను నమోదు చేయండి",
        "sec_prompt": "సెక్షన్ సంఖ్యను నమోదు చేయండి (1 నుండి 28):",
        "name_lbl": "ఫిర్యాదుదారు పేరు:",
        "city_lbl": "జిల్లా & రాష్ట్రం:",
        "phone_lbl": "ఫోన్ నంబర్:",
        "acc_lbl": "బాధ్యులైన అధికారి / కాంట్రాక్టర్:",
        "det_lbl": "పూర్తి వివరాలు:",
        "btn_draft": "⚡ లీగల్ నోటీసు రూపొందించండి",
        "success_msg": "🟢 లీగల్ నోటీస్ సిద్ధమైంది:",
        "doc_box_lbl": "📄 సిద్ధమైన చట్టపరమైన నోటీసు:",
        "download_txt_btn": "📥 నోటీసు డౌన్‌లోడ్ చేయండి (.txt)",
        "pdf_btn": "🖨️ PDF గా సేవ్ / ప్రింట్ చేయండి",
        "shield_title": "⚖️ చట్టపరమైన రక్షణ:",
        "send_wa": "📲 వాట్సాప్‌లో పంపండి",
        "def_name
