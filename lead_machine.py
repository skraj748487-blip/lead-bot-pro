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
        "en_det": "I am financially incapable of bearing litigation fees and formally request a free government advocate."
    },
    13: {
        "hi_name": "मकान मालिक द्वारा जबरन बेदखली व बिजली काटना",
        "en_name": "Landlord Forcible Eviction & Disconnecting Utilities",
        "hi_act": "रेंट कंट्रोल एक्ट व BNS",
        "en_act": "Rent Control Act & Bharatiya Nyaya Sanhita",
        "hi_auth": "किराया नियंत्रक (Rent Controller) व पुलिस",
        "en_auth": "Rent Controller & Local Police",
        "hi_rule": "मकान मालिक बिना कोर्ट ऑर्डर के ताला नहीं तोड़ सकता, न ही बिजली-पानी काट सकता है।",
        "en_rule": "Landlords cannot cut electricity/water or break locks without a formal judicial decree.",
        "hi_det": "मकान मालिक द्वारा बिना कानूनी नोटिस पानी-बिजली बंद कर जबरन मकान खाली कराने की धमकी दी गई।",
        "en_det": "The landlord unlawfully disconnected electricity and water, attempting forcible eviction without notice."
    },
    14: {
        "hi_name": "जातिगत भेदभाव व सामाजिक बहिष्कार",
        "en_name": "Caste Discrimination & Harassment (SC/ST Act)",
        "hi_act": "अनुसूचित जाति/जनजाति अत्याचार निवारण अधिनियम",
        "en_act": "SC/ST Prevention of Atrocities Act & Article 15",
        "hi_auth": "पुलिस अधीक्षक (SP) व विशेष अदालत",
        "en_auth": "Superintendent of Police (SP) & Special Court",
        "hi_rule": "जाति के आधार पर अपमानित करने या रास्ता रोकने पर गैर-जमानती गिरफ्तारी होती है।",
        "en_rule": "Casteist slurs, social boycott, or blocking public roads invite mandatory non-bailable arrest.",
        "hi_det": "विपक्षी द्वारा जातिसूचक अपशब्दों का प्रयोग कर सार्वजनिक रूप से अपमानित किया गया।",
        "en_det": "The accused party used derogatory casteist slurs publicly and subjected me to humiliation."
    },
    15: {
        "hi_name": "धर्म के नाम पर भेदभाव व नफरत",
        "en_name": "Religious Discrimination & Hate Speech",
        "hi_act": "संविधान अनुच्छेद 15 व धारा 196 BNS",
        "en_act": "Article 15 & Section 196 BNS (Communal Harmony)",
        "hi_auth": "जिला दंडाधिकारी (DM) व NHRC",
        "en_auth": "District Magistrate (DM) & NHRC",
        "hi_rule": "धार्मिक सद्भाव बिगाड़ने या भेदभाव करने पर संज्ञेय गैर-जमानती मुकदमा होता है।",
        "en_rule": "Discrimination or spreading communal hatred is a cognizable non-bailable penal offense.",
        "hi_det": "धार्मिक आधार पर प्रार्थी के साथ सार्वजनिक स्थल पर भेदभावपूर्ण दुर्व्यवहार किया गया।",
        "en_det": "I was subjected to unlawful religious discrimination and public exclusion by the accused party."
    },
    16: {
        "hi_name": "गिग वर्कर डिलीवरी बॉय व ड्राइवर अधिकार",
        "en_name": "Gig Workers, Delivery Boy & Cab Driver Rights",
        "hi_act": "कोड ऑन सोशल सिक्योरिटी 2020",
        "en_act": "Code on Social Security 2020 & Gig Worker Rules",
        "hi_auth": "श्रम कल्याण बोर्ड एवं कंपनी नोडल अधिकारी",
        "en_auth": "Labour Welfare Board & Company Nodal Officer",
        "hi_rule": "कंपनी बिना कारण आईडी ब्लॉक नहीं कर सकती और दुर्घटना पर इलाज-मुआवजा अनिवार्य है।",
        "en_rule": "Companies cannot block worker IDs without notice and must provide accident medical compensation.",
        "hi_det": "बिना किसी सूचना के डिलीवरी आईडी ब्लॉक कर दी गई और बकाया भुगतान रोक लिया गया।",
        "en_det": "My driver/delivery ID was blocked without show-cause notice and pending payout was withheld."
    },
    17: {
        "hi_name": "राशन कार्ड में अंगूठा लगवाकर राशन न देना",
        "en_name": "PDS Ration Card Dealer Fingerprint Fraud",
        "hi_act": "राष्ट्रीय खाद्य सुरक्षा अधिनियम (NFSA)",
        "en_act": "National Food Security Act (NFSA) 2013",
        "hi_auth": "जिला आपूर्ति पदाधिकारी (DSO) व SDO",
        "en_auth": "District Supply Officer (DSO) & SDO",
        "hi_rule": "अंगूठा लगवाकर अनाज न देना सीधे खाद्यान्न चोरी का अपराध है; कोटेदार का लाइसेंस रद्द होता है।",
        "en_rule": "Taking biometric fingerprint and denying foodgrains constitutes criminal theft under NFSA.",
        "hi_det": "ई-पॉस मशीन पर फिंगरप्रिंट लेने के बावजूद इस माह का निर्धारित राशन नहीं दिया गया।",
        "en_det": "The ration dealer obtained my biometric thumbprint but refused to release the allocated foodgrains."
    },
    18: {
        "hi_name": "बैंक अकाउंट अवैध फ्रीज व मिनिमम बैलेंस कटौती",
        "en_name": "Bank Account Unlawful Freeze & Balance Loot",
        "hi_act": "RBI बैंकिंग लोकपाल दिशानिर्देश",
        "en_act": "RBI Banking Ombudsman Scheme & Circulars",
        "hi_auth": "बैंकिंग लोकपाल (RBI Ombudsman)",
        "en_auth": "Banking Ombudsman & Bank Nodal Officer",
        "hi_rule": "बैंक सेविंग्स खाते को चार्ज काटकर माइनस में नहीं ले जा सकता, न बिना नोटिस फ्रीज कर सकता है।",
        "en_rule": "Banks cannot force savings accounts into negative balances or freeze accounts without written notice.",
        "hi_det": "बैंक द्वारा बिना किसी कानूनी नोटिस के खाता फ्रीज किया गया व अनुचित शुल्क काटा गया।",
        "en_det": "The bank unlawfully froze my savings account without prior notice and levied unjustified penalties."
    },
    19: {
        "hi_name": "बिजली विभाग मनमानी व ट्रांसफार्मर खराबी",
        "en_name": "Electricity Discom High Bills & Burnt Transformer",
        "hi_act": "विद्युत अधिनियम 2003 नियमावली",
        "en_act": "Electricity Act 2003 (Consumer Rights Rules)",
        "hi_auth": "उपभोक्ता फोरम (CGRF) व कार्यपालक अभियंता",
        "en_auth": "Consumer Grievance Redressal Forum (CGRF) & EE",
        "hi_rule": "जला हुआ ट्रांसफार्मर ग्रामीण क्षेत्र में 48 घंटे व शहरी में 24 घंटे में बदलना अनिवार्य है।",
        "en_rule": "Burnt transformers must be replaced within 24-48 hours and arbitrary inflated bills corrected.",
        "hi_det": "कई दिनों से ट्रांसफार्मर खराब है और विभाग द्वारा अत्यधिक फर्जी बिल भेजा गया है।",
        "en_det": "The transformer has been non-functional for days and an exorbitant inflated bill was served."
    },
    20: {
        "hi_name": "आयुष्मान कार्ड (PM-JAY) पर अस्पताल का इनकार",
        "en_name": "Hospital Refusing Treatment on Ayushman Card",
        "hi_act": "राष्ट्रीय स्वास्थ्य प्राधिकरण (NHA) अनुबंध नियम",
        "en_act": "National Health Authority (NHA) Empanelment Rules",
        "hi_auth": "स्टेट एंटी-फ्रॉड यूनिट (SAFU) व CMO",
        "en_auth": "State Anti-Fraud Unit (SAFU) & CMO",
        "hi_rule": "सूचीबद्ध अस्पताल आयुष्मान कार्ड धारक को मना नहीं कर सकता; उल्लंघन पर पैनल रद्द होता है।",
        "en_rule": "Empaneled hospitals cannot deny free cashless treatment; violation cancels commercial registration.",
        "hi_det": "सक्रिय आयुष्मान कार्ड होने के बावजूद निजी अस्पताल द्वारा निशुल्क इलाज से मना किया गया।",
        "en_det": "Despite holding an active Ayushman card, the hospital refused cashless admission and emergency care."
    },
    21: {
        "hi_name": "पीएम आवास योजना में रिश्वत की मांग",
        "en_name": "Bribery & Commission Demand in PM Awas Yojana",
        "hi_act": "भ्रष्टाचार निवारण अधिनियम",
        "en_act": "Prevention of Corruption Act & PMAY Grievance Rules",
        "hi_auth": "निगरानी ब्यूरो (Vigilance) व DDC",
        "en_auth": "Vigilance Bureau & District Ombudsman",
        "hi_rule": "आवास योजना के पैसे में कमीशन मांगना संज्ञेय भ्रष्टाचार अपराध है।",
        "en_rule": "Demanding commission for releasing PMAY housing funds constitutes a cognizable corruption offense.",
        "hi_det": "आवास योजना की किस्त जारी करने के एवज में संबंधित कर्मी द्वारा रिश्वत की मांग की जा रही है।",
        "en_det": "The local official is demanding illegal bribery to release the approved housing installment."
    },
    22: {
        "hi_name": "प्राइवेट स्कूल में 25% फ्री एडमिशन (RTE)",
        "en_name": "Private School Denying 25% Free Quota (RTE)",
        "hi_act": "शिक्षा का अधिकार अधिनियम (RTE) धारा 12(1)(c)",
        "en_act": "Right to Education (RTE) Act Section 12(1)(c)",
        "hi_auth": "जिला शिक्षा पदाधिकारी (DEO) व बाल आयोग",
        "en_auth": "District Education Officer (DEO) & Child Rights Commission",
        "hi_rule": "हर प्राइवेट स्कूल में 25% सीटें गरीब बच्चों के लिए पूर्णतः निशुल्क आरक्षित हैं।",
        "en_rule": "25% of seats in non-minority private schools are mandatorily free for underprivileged children.",
        "hi_det": "RTE पात्रता होने के बावजूद संबंधित निजी स्कूल द्वारा छात्र का दाखिला लेने से इनकार किया गया।",
        "en_det": "Despite official RTE allotment, the private school refused free admission to the child."
    },
    23: {
        "hi_name": "नकली खाद-बीज से फसल बर्बादी का हर्जाना",
        "en_name": "Fake Seeds & Adulterated Fertilizer Compensation",
        "hi_act": "कीटनाशक अधिनियम 1968 व आवश्यक वस्तु कानून",
        "en_act": "Insecticides Act & Essential Commodities Act",
        "hi_auth": "जिला कृषि पदाधिकारी (DAO) व उपभोक्ता कोर्ट",
        "en_auth": "District Agriculture Officer (DAO) & Consumer Court",
        "hi_rule": "नकली सामग्री बेचने पर विक्रेता पर मुकदमा और किसान को 100% फसल नुकसान का हर्जाना मिलता है।",
        "en_rule": "Selling sub-standard seeds/fertilizers invites criminal trial and 100% crop damage compensation.",
        "hi_det": "दुकानदार द्वारा नकली बीज व खाद दिए जाने के कारण मेरी संपूर्ण खड़ी फसल नष्ट हो गई।",
        "en_det": "Sub-standard seeds and adulterated fertilizers caused total loss of my standing agricultural crop."
    },
    24: {
        "hi_name": "फसल बीमा (PMFBY) क्लेम चोरी व रिजेक्शन",
        "en_name": "Crop Insurance (PMFBY) Claim Rejection",
        "hi_act": "PMFBY परिचालन दिशानिर्देश",
        "en_act": "PMFBY Operational Guidelines & Agricultural Laws",
        "hi_auth": "जिला कृषि समिति (DLMC) व कृषि विभाग",
        "en_auth": "District Agriculture Committee & Insurance Grievance Cell",
        "hi_rule": "आपदा के समय 72 घंटे में सूचना देने पर 12% ब्याज सहित बीमा क्लेम मिलना अनिवार्य है।",
        "en_rule": "Intimating within 72 hours of disaster obligates insurance companies to settle claims with 12% interest.",
        "hi_det": "बाढ़/सूखा से हुए प्रमाणित नुकसान के बावजूद बीमा कंपनी द्वारा क्लेम को निरस्त किया गया।",
        "en_det": "Despite verified localized crop inundation, the insurance company wrongfully rejected my claim."
    },
    25: {
        "hi_name": "बुजुर्ग माता-पिता की संपत्ति हड़पना व प्रताड़ना",
        "en_name": "Senior Citizen Parents Property Usurpation",
        "hi_act": "वरिष्ठ नागरिक भरण-पोषण कानून 2007",
        "en_act": "Senior Citizens Maintenance & Welfare Act 2007",
        "hi_auth": "SDM ट्रिब्यूनल",
        "en_auth": "Maintenance Tribunal (SDM Court)",
        "hi_rule": "प्रताड़ित करने पर माता-पिता द्वारा संतानों को दी गई संपत्ति की रजिस्ट्री रद्द हो जाती है।",
        "en_rule": "Tribunals hold sovereign power to revoke gift deeds and order eviction of abusive children.",
        "hi_det": "संपत्ति नाम कराने के उपरांत संतानों द्वारा भोजन-दवा बंद कर घर से बेदखल करने की धमकी दी गई।",
        "en_det": "After securing property registration, my children stopped food and medical care, attempting eviction."
    },
    26: {
        "hi_name": "छात्र पेपर लीक व कोचिंग फीस वापसी",
        "en_name": "Student Paper Leak Mafia & Coaching Fee Refund",
        "hi_act": "लोक परीक्षा कानून 2024 व UGC नियम",
        "en_act": "Public Examinations Act 2024 & UGC Fee Guidelines",
        "hi_auth": "उच्च शिक्षा विभाग व उपभोक्ता आयोग",
        "en_auth": "Higher Education Department & Consumer Commission",
        "hi_rule": "कोचिंग बीच में छोड़ने पर शेष बची फीस वापस करना अनिवार्य है।",
        "en_rule": "Institutes must refund unutilized course fees upon exit; paper leak invites up to 10-year prison.",
        "hi_det": "कोर्स छोड़ने के बाद भी संस्थान द्वारा नियमानुसार बची हुई फीस वापस नहीं की गई।",
        "en_det": "Upon legitimate course withdrawal, the coaching academy refused to refund the remaining prepaid fees."
    },
    27: {
        "hi_name": "ट्रैफिक पुलिस द्वारा चाबी छीनना व डंडा मारना",
        "en_name": "Traffic Police Snatching Keys & Illegal Seizure",
        "hi_act": "मोटर वाहन अधिनियम व गृह मंत्रालय सर्कुलर",
        "en_act": "Motor Vehicles Act & Ministry of Road Transport Directives",
        "hi_auth": "यातायात पुलिस अधीक्षक (SP Traffic)",
        "en_auth": "Superintendent of Police (Traffic)",
        "hi_rule": "चलती गाड़ी से चाबी निकालना अपराध है; DigiLocker के डिजिटल दस्तावेज 100% मान्य हैं।",
        "en_rule": "Police cannot snatch keys from running vehicles; DigiLocker documents are legally equivalent to originals.",
        "hi_det": "वैध डिजिटल दस्तावेज दिखाने के बावजूद ट्रैफिक कर्मी द्वारा दुर्व्यवहार कर चाबी छीनी गई।",
        "en_det": "Despite presenting valid DigiLocker documents, the traffic personnel misbehaved and forcefully snatched keys."
    },
    28: {
        "hi_name": "मरीज का अधिकार (मेडिकल फाइल व सस्ती दवा)",
        "en_name": "Patient Rights Charter (Medical File & Generic Meds)",
        "hi_act": "NHRC पेशेंट राइट्स चार्टर",
        "en_act": "NHRC Charter of Patients Rights & Medical Council Rules",
        "hi_auth": "CMO व राज्य चिकित्सा परिषद",
        "en_auth": "Chief Medical Officer & State Medical Council",
        "hi_rule": "अस्पताल मरीज को मेडिकल फाइल और बाहर से सस्ती जेनेरिक दवा लेने से नहीं रोक सकता।",
        "en_rule": "Hospitals cannot deny clinical case sheets or compel patients to purchase in-house branded medicines.",
        "hi_det": "अस्पताल द्वारा केस फाइल देने से मना किया गया तथा बाहर से जेनेरिक दवा लाने पर रोक लगाई गई।",
        "en_det": "The hospital refused access to treatment files and forcefully barred procuring cheaper generic medicines."
    }
}

# ================= TAB 1: SECTION NUMBER, CUSTOM COMPLAINT & VIDEO DOWNLOAD =================
if nav_choice == T["c_rights"]:
    st.write(f"### {T['title']} — {T['c_rights']}")

    filing_mode = st.radio(
        T["mode_lbl"],
        [T["mode_sec"], T["mode_custom"]],
        horizontal=True
    )

    if filing_mode == T["mode_sec"]:
        sec_num = st.number_input(T["sec_prompt"], min_value=1, max_value=28, value=1, step=1)
        curr_case = LEGAL_28[sec_num]

        case_name = curr_case["en_name"] if is_eng else curr_case["hi_name"]
        case_act = curr_case["en_act"] if is_eng else curr_case["hi_act"]
        case_auth = curr_case["en_auth"] if is_eng else curr_case["hi_auth"]
        case_rule = curr_case["en_rule"] if is_eng else curr_case["hi_rule"]
        default_det = curr_case["en_det"] if is_eng else curr_case["hi_det"]

        st.markdown(f"""
        <div class="info-card">
            <h3 style="color:#38BDF8; margin:0 0 6px 0;">{'Section' if is_eng else 'धारा/सेक्शन'} {sec_num}: {case_name}</h3>
            <p style="margin:0; font-size:14px;"><b>{'Statute:' if is_eng else 'लागू अधिनियम:'}</b> {case_act}</p>
            <p style="margin:4px 0 0 0; font-size:14px; color:#10B981;"><b>{'Authority:' if is_eng else 'सक्षम प्राधिकारी:'}</b> {case_auth}</p>
        </div>
        """, unsafe_allow_html=True)

        target_subject = f"Section {sec_num} ({case_name})" if is_eng else f"सेक्शन {sec_num} ({case_name})"
        target_act = case_act
        target_auth = case_auth
        target_rule = case_rule

    else:
        st.info("✍️ " + ("Write your custom grievance details below:" if is_eng else "अपनी समस्या का शीर्षक और जो हुआ है वो नीचे साफ-साफ लिखें:"))
        custom_subject = st.text_input(T["custom_sub_lbl"], value=T["custom_sub_val"])
        target_subject = custom_subject
        target_act = T["custom_act"]
        target_auth = T["custom_auth"]
        target_rule = T["custom_rule"]
        default_det = T["custom_det"]

    col_v1, col_v2 = st.columns(2)
    with col_v1:
        v_name = st.text_input(T["name_lbl"], value=T["def_name"])
    with col_v2:
        v_loc = st.text_input(T["city_lbl"], value=T["def_city"])

    v_phone = st.text_input(T["phone_lbl"], value="7484878440")
    v_accused = st.text_input(T["acc_lbl"], value=T["def_acc"])
    v_details = st.text_area(T["det_lbl"], value=default_det, height=100)

    if st.button(T["btn_draft"]):
        if is_eng:
            final_notice = f"""======================================================================
OFFICIAL FORMAL LEGAL NOTICE & STATUTORY COMPLAINT
(Under: {target_act})
Date: {today_str}

To,
1. {target_auth}, {v_loc}
2. National Human Rights Commission (NHRC) / Legal Vigilance Board

Subject: Urgent FIR, Statutory Prosecution & Restitution against '{v_accused}' for '{target_subject}'.

Respected Authority,
The complainant {v_name} (Mobile: +91 {v_phone}), resident of {v_loc}, submits:

1. The complainant is a law-abiding citizen of India. The accused '{v_accused}' has flagrantly violated constitutional and statutory rights.
2. Factual Summary of Injustice:
"{v_details}"
3. Statutory Provisions & Legal Shield:
- {target_rule}

Prayer for Relief:
(a) Register immediate FIR under relevant penal provisions against '{v_accused}'.
(b) Ensure full recovery of unpaid dues, statutory compensation, or protection without delay.
(c) Safeguard the life and liberty of the complainant.

Complainant:
{v_name}
Contact: +91 {v_phone}
Digital Evidence Tracked: Maha Seva AI Sovereign Legal Mission
======================================================================"""
        else:
            final_notice = f"""======================================================================
आधिकारिक कानूनी विधिक शिकायत पत्र व नोटिस
(अधिनियम: {target_act})
दिनांक: {today_str}

सेवा में,
1. {target_auth}, {v_loc}
2. राष्ट्रीय मानवाधिकार आयोग (NHRC) / विधिक निगरानी प्राधिकरण

विषय: '{target_subject}' के संबंध में दोषी '{v_accused}' पर तत्काल कानूनी कार्रवाई व अधिकार रक्षा बाबत।

महोदय,
प्रार्थी {v_name} (मोबाइल: +91 {v_phone}), निवासी {v_loc} सादर सूचित करता है कि:

1. यह कि प्रार्थी भारत का विधि-सम्मत नागरिक है और विपक्षी '{v_accused}' द्वारा प्रार्थी के विधिक अधिकारों का खुला उल्लंघन किया गया है।
2. तथ्यात्मक घटनाक्रम (सच्चा विवरण):
"{v_details}"
3. विधिक नियम व कानूनी आधार:
- {target_rule}

अतः सक्षम प्राधिकारी से प्रार्थना है कि:
(क) दोषी '{v_accused}' के विरुद्ध सुसंगत कानूनी धाराओं में तत्काल संज्ञान लेकर कड़ी प्राथमिकी दर्ज की जाए।
(ख) प्रार्थी को उसका संपूर्ण विधिक हक, सुरक्षा अथवा मुआवजा अविलंब दिलाया जाए।

भवदीय:
{v_name}
संपर्क सूत्र: +91 {v_phone}
डिजिटल साक्ष्य सुरक्षित: महा-सेवा AI राष्ट्रीय विधिक साक्षरता मिशन
======================================================================"""

        # BILINGUAL SUCCESS MESSAGE
        st.success(T["success_msg"])
        st.text_area(T["doc_box_lbl"], final_notice, height=220)

        # 1. DOWNLOAD LEGAL NOTICE AS TEXT/DOCUMENT
        st.download_button(
            label=T["download_txt_btn"],
            data=final_notice,
            file_name=f"Legal_Notice_{today_str}.txt",
            mime="text/plain"
        )

        # 2. LEGAL EXPLAINER TEMPLATE VIDEO
        st.markdown("---")
        st.write(f"### {T['video_title']}")
        st.caption(T["video_sub"])

        sample_video_url = "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4"
        st.video(sample_video_url)

        st.markdown(f'<a href="{sample_video_url}" download="Legal_Awareness_Video.mp4" target="_blank" class="btn-blue">{T["download_video_btn"]}</a>', unsafe_allow_html=True)

        st.markdown(f"""
        <div class="caution-card">
            <h3 style="color:#EF4444; margin:0 0 6px 0;">{T['shield_title']}</h3>
            <p style="margin:0; font-size:14px; color:#FCA5A5;">{target_rule}</p>
        </div>
        """, unsafe_allow_html=True)

        enc_legal = urllib.parse.quote(final_notice)
        st.markdown(f'<a href="https://wa.me/?text={enc_legal}" target="_blank" class="btn-green">{T["send_wa"]}</a>', unsafe_allow_html=True)

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

# ================= TAB 3: VOICE-TO-TEXT =================
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
