import streamlit as st
import streamlit.components.v1 as components
import urllib.parse
from datetime import datetime

# 1. Page Configuration
st.set_page_config(
    page_title="Maha Seva AI — Citizen Legal Mission",
    page_icon="🇮🇳",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Modern 100% Dark UI
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

# Language Setup & Complete Bilingual Dictionary
LANG_CONFIG = {
    "🇮🇳 हिन्दी": {
        "tag": "⚡ 24x7 अखंड भारत नागरिक व विधिक सुरक्षा मिशन",
        "title": "महा-सेवा AI (MAHA SEVA AI)",
        "sub": "28 कानूनी धाराएँ • अपनी शिकायत लिखें • वीडियो डाउनलोड • रात की सुरक्षा SOS",
        "cat_lbl": "📂 सेवा श्रेणी चुनें:",
        "c_rights": "⚖️ कानूनी सेक्शन, नोटिस व वीडियो",
        "c_sos": "🚨 रात की सुरक्षा व लाइव GPS SOS",
        "c_voice": "🎙️ बोलकर शिकायत दर्ज करें (माइक)",
        "c_fraud": "🛡️ साइबर फ्रॉड व मैसेज चेकर",
        "c_health": "🏥 दवा व एम्बुलेंस सहायता",
        "c_job": "💼 रोज़गार व हेल्पर डेस्क",
        "mode_lbl": "शिकायत का तरीका चुनें:",
        "mode_sec": "🔢 सेक्शन नंबर से चुनें (1 से 28 कानून)",
        "mode_custom": "✍️ अपनी खुद की नई शिकायत लिखें (Custom Complaint)",
        "sec_prompt": "सेक्शन नंबर दर्ज करें (1 से 28):",
        "name_lbl": "पीड़ित / प्रार्थी का नाम:",
        "city_lbl": "जिला व राज्य:",
        "phone_lbl": "मोबाइल नंबर:",
        "acc_lbl": "दोषी पक्ष / अधिकारी / कंपनी का नाम:",
        "det_lbl": "सच्चा घटनाक्रम विवरण (Fact Details):",
        "btn_draft": "⚡ आधिकारिक कानूनी नोटिस व टेम्पलेट वीडियो तैयार करें",
        "success_msg": "🟢 आधिकारिक विधिक नोटिस व कानूनी टेम्पलेट तैयार:",
        "doc_box_lbl": "📄 तैयार कानूनी दस्तावेज:",
        "download_txt_btn": "📥 कानूनी शिकायत पत्र डाउनलोड करें (Download Legal Notice .txt)",
        "video_title": "🎬 विधिक जागरूकता व प्रमाणित टेम्पलेट वीडियो",
        "video_sub": "यह वीडियो सीधे अपने मोबाइल में डाउनलोड करें और व्हाट्सएप स्टेटस पर शेयर करें:",
        "download_video_btn": "📥 विधिक टेम्पलेट वीडियो डाउनलोड करें (Download Video MP4)",
        "shield_title": "⚖️ इस मामले में आपका कानूनी कवच:",
        "send_wa": "📲 यह शिकायत पत्र WhatsApp पर भेजें",
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
        "sub": "28 Sovereign Sections • Custom Complaint • Video Download • Night SOS",
        "cat_lbl": "📂 Select Service Category:",
        "c_rights": "⚖️ Legal Sections, Notice & Video",
        "c_sos": "🚨 Night Safety & Live GPS SOS",
        "c_voice": "🎙️ Voice-to-Text Complaint (Mic)",
        "c_fraud": "🛡️ Cyber Shield & Fraud Verifier",
        "c_health": "🏥 Healthcare & Free Ambulance",
        "c_job": "💼 Pan-India Employment Desk",
        "mode_lbl": "Select Filing Method:",
        "mode_sec": "🔢 Select by Section Number (1 to 28)",
        "mode_custom": "✍️ Write Your Own Custom Complaint",
        "sec_prompt": "Enter Section Number (1 to 28):",
        "name_lbl": "Complainant Name:",
        "city_lbl": "District & State:",
        "phone_lbl": "Mobile Number:",
        "acc_lbl": "Accused Party / Official / Agency:",
        "det_lbl": "Factual Details of Injustice:",
        "btn_draft": "⚡ Draft Official Court-Grade Legal Notice & Video",
        "success_msg": "🟢 Official Legal Notice & Template Generated:",
        "doc_box_lbl": "📄 Prepared Legal Document:",
        "download_txt_btn": "📥 Download Legal Notice Document (.txt)",
        "video_title": "🎬 Legal Awareness & Certified Template Video",
        "video_sub": "Download this video directly to your mobile and share on WhatsApp status:",
        "download_video_btn": "📥 Download Template Video (MP4)",
        "shield_title": "⚖️ Your Statutory Legal Protection:",
        "send_wa": "📲 Send Notice via WhatsApp",
        "def_name": "Sahil Kumar",
        "def_city": "West Champaran, Bihar",
        "def_acc": "Accused Employer / Officer / Agency",
        "custom_sub_lbl": "Complaint Subject:",
        "custom_sub_val": "Regarding Unlawful Harassment and Violation of Fundamental Rights",
        "custom_act": "Constitution of India, BNS 2023 & Relevant Special Statutes",
        "custom_auth": "District Magistrate (DM) / Superintendent of Police (SP)",
        "custom_rule": "Every citizen has the guaranteed fundamental right to legal remedy, justice, and immediate protection under the Constitution of India.",
        "custom_det": "The complainant has been unlawfully harassed and aggrieved by the accused party, and formal relief is sought."
    }
}

chosen_lang = st.radio("🌐 भाषा चुनें / Select Language:", ["🇮🇳 हिन्दी", "🇬🇧 English"], horizontal=True)
T = LANG_CONFIG[chosen_lang]
is_eng = (chosen_lang == "🇬🇧 English")

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

# 28 LEGAL SECTIONS MASTER DATA (100% BILINGUAL)
LEGAL_28 = {
    1: {
        "hi_name": "मजदूरी/वेतन चोरी (Wage Theft)",
        "en_name": "Wage Theft & Unpaid Salary by Contractor",
        "hi_act": "पेमेंट ऑफ वेजेस एक्ट 1936",
        "en_act": "Payment of Wages Act 1936 & Industrial Disputes Act",
        "hi_auth": "श्रम आयुक्त (Labour Commissioner) व DM",
        "en_auth": "Labour Commissioner & District Magistrate (DM)",
        "hi_rule": "मजदूरी दबाने पर श्रम विभाग 10 गुना हर्जाना और 18% ब्याज दिलवाता है।",
        "en_rule": "Withholding wages is strictly illegal. Labour Court enforces 10x compensation and 18% interest.",
        "hi_det": "मैंने 2 महीने कार्य किया, जिसका कुल ₹24,000 बकाया है। मांगने पर गाली व धमकी दी जा रही है।",
        "en_det": "I worked diligently for 2 months, pending dues are Rs 24,000. Demanding salary resulted in criminal threats."
    },
    2: {
        "hi_name": "पुलिस अवैध मारपीट या फर्जी चालान",
        "en_name": "Police Harassment, Brutality & Illegal Challan",
        "hi_act": "भारतीय नागरिक सुरक्षा संहिता (BNSS) व डी.के. बसु गाइडलाइन्स",
        "en_act": "BNSS 2023 & Supreme Court DK Basu Directives",
        "hi_auth": "पुलिस अधीक्षक (SP) व NHRC",
        "en_auth": "Superintendent of Police (SP) & NHRC",
        "hi_rule": "बिना जुर्म मारपीट पर धारा 166A BNS के तहत पुलिसकर्मी पर निलंबन व FIR होती है।",
        "en_rule": "Assault or abusive behavior triggers Section 166A BNS with suspension and departmental prosecution.",
        "hi_det": "संबंधित पुलिसकर्मी द्वारा अकारण अभद्रता, मारपीट व अवैध चालान की धमकी दी गई।",
        "en_det": "I was subjected to unlawful public harassment, physical assault, and fake challan threats by the officer."
    },
    3: {
        "hi_name": "अस्पताल में इमरजेंसी इलाज इनकार या शव रोकना",
        "en_name": "Hospital Refusing Emergency Care or Detaining Body",
        "hi_act": "सुप्रीम कोर्ट परमानंद कटारा फैसला",
        "en_act": "Supreme Court Parmanand Katara Verdict & Clinical Establishments Act",
        "hi_auth": "मुख्य चिकित्सा अधिकारी (CMO) व स्वास्थ्य विभाग",
        "en_auth": "Chief Medical Officer (CMO) & Health Department",
        "hi_rule": "इमरजेंसी में पैसे मांगकर इलाज से इनकार या शव बंधक बनाना संज्ञेय अपराध है।",
        "en_rule": "Refusing emergency care over advance money or detaining patients/bodies is a cognizable criminal offense.",
        "hi_det": "अस्पताल द्वारा अग्रिम राशि की मांग कर गंभीर हालत में इलाज में जानबूझकर देरी की गई।",
        "en_det": "The hospital delayed emergency medical treatment deliberately by demanding upfront cash advance."
    },
    4: {
        "hi_name": "कार्यस्थल पर हादसा व शारीरिक अपंगता",
        "en_name": "Workplace Accident & Disability Compensation",
        "hi_act": "कर्मचारी मुआवजा कानून 1923",
        "en_act": "Employees Compensation Act 1923",
        "hi_auth": "मुआवजा आयुक्त एवं श्रम न्यायालय",
        "en_auth": "Compensation Commissioner & Labour Court",
        "hi_rule": "ड्यूटी पर दुर्घटना होने पर ₹5 लाख से ₹20 लाख का मुआवजा व आजीवन पेंशन अनिवार्य है।",
        "en_rule": "Employer is strictly liable to pay Rs 5 to 20 Lakhs compensation and pension for workplace injury.",
        "hi_det": "सुरक्षा उपकरणों के अभाव में कार्यस्थल पर हादसा हुआ जिससे स्थायी दिव्यांगता आई।",
        "en_det": "Due to lack of safety equipment, a severe accident occurred causing permanent disability."
    },
    5: {
        "hi_name": "सूदखोर व फर्जी लोन ऐप्स द्वारा धमकी/ब्लैकमेल",
        "en_name": "Illegal Money Lenders & Loan App Blackmail",
        "hi_act": "RBI दिशानिर्देश व धारा 308 BNS (जबरन वसूली)",
        "en_act": "RBI Fair Recovery Guidelines & Extortion Law Sec 308 BNS",
        "hi_auth": "साइबर क्राइम सेल, एसपी (SP) व RBI लोकपाल",
        "en_auth": "Cyber Crime Cell, SP & RBI Ombudsman",
        "hi_rule": "बिना लाइसेंस सूदखोरी और धमकी देकर वसूली करना गैर-कानूनी है।",
        "en_rule": "Unlicensed money lending and threatening calls/photo leaks are strictly illegal, leading to immediate arrest.",
        "hi_det": "लोन एजेंट द्वारा घर आकर गाली-गलौज और फोटो वायरल करने का ब्लैकमेल किया जा रहा है।",
        "en_det": "The loan recovery agent is issuing criminal threats and blackmailing to leak private contact lists."
    },
    6: {
        "hi_name": "सरकारी दफ्तर में घूसखोरी व 'कल आना' अपमान",
        "en_name": "Government Office Bribery & Service Delay (RTPS)",
        "hi_act": "सेवा का अधिकार कानून (RTPS Act) व भ्रष्टाचार अधिनियम",
        "en_act": "Right to Public Services Act (RTPS) & Anti-Corruption Act",
        "hi_auth": "निगरानी ब्यूरो (Vigilance Bureau)",
        "en_auth": "Vigilance Bureau & Grievance Directorate",
        "hi_rule": "काम लटकाने पर कर्मचारी के वेतन से प्रतिदिन ₹250 से ₹5000 जुर्माना कटता है।",
        "en_rule": "Officers delaying public services face automatic daily salary deduction of Rs 250 to Rs 5000.",
        "hi_det": "वैध कागजात देने के बावजूद रिश्वत के बिना कर्मचारी द्वारा बार-बार चक्कर लगवाए जा रहे हैं।",
        "en_det": "Despite submitting valid documents, the government clerk is withholding service for illegal bribery."
    },
    7: {
        "hi_name": "दुकानदार या कोटेदार द्वारा MRP लूट व घटतौली",
        "en_name": "Shopkeeper/Ration Dealer Overpricing & Underweighing",
        "hi_act": "लीगल मेट्रोलॉजी एक्ट 2009",
        "en_act": "Legal Metrology Act 2009 & NFSA",
        "hi_auth": "जिला आपूर्ति पदाधिकारी (DSO) व उपभोक्ता फोरम",
        "en_auth": "District Supply Officer & Consumer Affairs",
        "hi_rule": "MRP से अधिक लेना या कम तौलना गैर-कानूनी है। ₹25,000 जुर्माना और दुकान सील होती है।",
        "en_rule": "Charging above printed MRP or underweighing attracts Rs 25,000 fine and cancellation of license.",
        "hi_det": "दुकानदार द्वारा तय मूल्य से अधिक दाम वसूला गया और कम सामग्री दी गई।",
        "en_det": "The vendor charged price above printed MRP and delivered commodities below legally prescribed weight."
    },
    8: {
        "hi_name": "ट्रेन में टीटीई (TTE) द्वारा अवैध वसूली व बदसलूकी",
        "en_name": "Railway TTE Extortion & Passenger Misbehavior",
        "hi_act": "भारतीय रेलवे अधिनियम",
        "en_act": "Indian Railway Act & Safety Regulations",
        "hi_auth": "रेलमदद 139 व RPF विजिलेंस",
        "en_auth": "RailMadad 139 & Railway Vigilance Board",
        "hi_rule": "टीटीई को यात्री से बदतमीजी या धक्का देने का कोई हक नहीं। केवल सरकारी रसीद मान्य है।",
        "en_rule": "TTE has zero legal authority to deboard passengers forcefully. Only official receipt (EFT) is permitted.",
        "hi_det": "यात्रा के दौरान टीटीई द्वारा अवैध धन की मांग और विरोध करने पर बदसलूकी की गई।",
        "en_det": "The on-duty TTE demanded illegal money and engaged in aggressive misbehavior upon objection."
    },
    9: {
        "hi_name": "थाने में FIR दर्ज न करना (Zero FIR)",
        "en_name": "Police Station Refusing FIR (Zero FIR Right)",
        "hi_act": "सुप्रीम कोर्ट ललिता कुमारी दिशा-निर्देश",
        "en_act": "Supreme Court Lalita Kumari Directives & Sec 173 BNSS",
        "hi_auth": "वरिष्ठ पुलिस अधीक्षक (SSP) व CJM कोर्ट",
        "en_auth": "Senior Superintendent of Police (SSP) & CJM Court",
        "hi_rule": "संज्ञेय अपराध में FIR न लिखने वाले पुलिस अधिकारी पर खुद धारा 166A BNS में FIR होती है।",
        "en_rule": "Refusal to register an FIR for a cognizable offense makes the police officer liable under Sec 166A BNS.",
        "hi_det": "लिखित शिकायत देने के बावजूद थाना प्रभारी द्वारा प्रथम सूचना रिपोर्ट दर्ज नहीं की गई।",
        "en_det": "Despite submitting a written complaint detailing the cognizable crime, the station in-charge refused FIR."
    },
    10: {
        "hi_name": "पैतृक जमीन पर दबंगों का अवैध कब्जा",
        "en_name": "Ancestral Land Encroachment by Strongmen",
        "hi_act": "धारा 145/144 BNSS",
        "en_act": "Section 145/144 BNSS & Civil Rights Laws",
        "hi_auth": "उप-विभागीय दंडाधिकारी (SDM) व सिविल कोर्ट",
        "en_auth": "Sub-Divisional Magistrate (SDM) & Civil Court",
        "hi_rule": "गरीब की पैतृक भूमि पर जबरन कब्जे की कोशिश पर तुरंत पुलिस सुरक्षा व स्टे का नियम है।",
        "en_rule": "Police and administration are obligated to issue immediate stay against illegal land grabbing.",
        "hi_det": "विपक्षी द्वारा प्रार्थी की वैध पैतृक जमीन पर बलपूर्वक अवैध कब्जे का प्रयास किया जा रहा है।",
        "en_det": "The opposite party is attempting to forcefully grab my legally inherited ancestral land."
    },
    11: {
        "hi_name": "सड़क हादसे (Hit & Run) में सरकारी मुआवजा",
        "en_name": "Road Accident (Hit and Run) Compensation",
        "hi_act": "मोटर वाहन संशोधन अधिनियम",
        "en_act": "Motor Vehicles Amendment Act (Hit & Run Scheme)",
        "hi_auth": "दावा अधिकरण (MACT) व जिला कलेक्टर",
        "en_auth": "MACT & District Magistrate Relief Fund",
        "hi_rule": "मृत्यु पर सरकार द्वारा ₹2 लाख और गंभीर घायल को ₹50,000 की तत्काल राहत मिलती है।",
        "en_rule": "Government provides mandatory interim relief of Rs 2 Lakhs for death and Rs 50,000 for injury.",
        "hi_det": "सड़क दुर्घटना के उपरांत तत्काल सरकारी राहत कोष व बीमा क्लेम की मांग की जा रही है।",
        "en_det": "Following a serious road accident, formal application is submitted for immediate compensation."
    },
    12: {
        "hi_name": "मुफ्त सरकारी वकील पाने हेतु आवेदन (DLSA)",
        "en_name": "Free Government Legal Aid Advocate (DLSA)",
        "hi_act": "विधिक सेवा प्राधिकरण अधिनियम (अनुच्छेद 39A)",
        "en_act": "Legal Services Authorities Act 1987 (Article 39A)",
        "hi_auth": "जिला विधिक सेवा प्राधिकरण (DLSA) सचिव",
        "en_auth": "District Legal Services Authority (DLSA) Secretary",
        "hi_rule": "गरीब, मजदूर और महिला को कोर्ट केस लड़ने के लिए सरकार मुफ्त वकील देती है।",
        "en_rule": "Every underprivileged citizen, worker, and woman is entitled to a free advocate at state expense.",
        "hi_det": "प्रार्थी आर्थिक रूप से असमर्थ है और उसे मुकदमे की पैरवी हेतु सरकारी वकील चाहिए।",
        "en
