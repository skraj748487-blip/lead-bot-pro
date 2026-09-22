import streamlit as st
import streamlit.components.v1 as components
import urllib.parse
from datetime import datetime

# 1. Page Configuration
st.set_page_config(
    page_title="Maha Seva AI — Sovereign Citizen Legal Mission",
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

LANG_DATA = {
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
        "send_wa": "📲 शिकायत पत्र WhatsApp पर भेजें",
        "def_name": "साहिल कुमार",
        "def_city": "पश्चिम चंपारण, बिहार",
        "def_accused": "संबंधित दोषी पक्ष / अधिकारी",
        "law_prefix": "कानून",
        "auth_prefix": "प्राधिकारी",
        "cases": {
            "1. ठेकेदार या कंपनी ने मजदूरी/वेतन रोक लिया (Wage Theft)": {
                "act": "पेमेंट ऑफ वेजेस एक्ट 1936 एवं औद्योगिक विवाद अधिनियम",
                "authority": "श्रम आयुक्त (Labour Commissioner) एवं जिलाधिकारी (DM)",
                "rule": "मजदूरी दबाना गैर-कानूनी अपराध है। श्रम विभाग 10 गुना हर्जाना और 18% ब्याज दिलवाता है।",
                "det": "मैंने कार्यस्थल पर 2 महीने पूरी ईमानदारी से कार्य किया, जिसकी कुल बकाया राशि ₹24,000 है। मांगने पर गाली-गलौज व धमकी दी जा रही है।"
            },
            "2. पुलिस द्वारा गैर-कानूनी मारपीट, अभद्रता या फर्जी चालान": {
                "act": "भारतीय नागरिक सुरक्षा संहिता (BNSS) एवं डी.के. बसु गाइडलाइन्स",
                "authority": "पुलिस अधीक्षक (SP), राज्य पुलिस शिकायत प्राधिकरण एवं NHRC",
                "rule": "बिना जुर्म मारपीट या गाली देने पर धारा 166A BNS के तहत पुलिसकर्मी पर निलंबन व FIR होती है।",
                "det": "संबंधित पुलिसकर्मी द्वारा बिना किसी अपराध के मेरे साथ सार्वजनिक रूप से अभद्रता, मारपीट व अवैध चालान की धमकी दी गई।"
            },
            "3. अस्पताल द्वारा इमरजेंसी में भर्ती न करना या शव बंधक बनाना": {
                "act": "सुप्रीम कोर्ट परमानंद कटारा फैसला एवं क्लिनिकल एस्टेब्लिशमेंट एक्ट",
                "authority": "मुख्य चिकित्सा अधिकारी (CMO) एवं स्वास्थ्य विभाग",
                "rule": "इमरजेंसी में पैसे मांगकर इलाज से इनकार नहीं किया जा सकता। शव या मरीज को बंधक बनाना अपराध है।",
                "det": "इमरजेंसी में अस्पताल द्वारा अग्रिम राशि का दबाव बनाकर इलाज में जानबूझकर देरी की गई।"
            },
            "4. कार्यस्थल/फैक्ट्री पर हादसा और शारीरिक अपंगता (मुआवजा)": {
                "act": "कर्मचारी मुआवजा कानून 1923 (Employees Compensation Act)",
                "authority": "मुआवजा आयुक्त एवं श्रम न्यायालय",
                "rule": "ड्यूटी के दौरान दुर्घटना होने पर मालिक को ₹5 लाख से ₹20 लाख का मुआवजा व आजीवन पेंशन देना अनिवार्य है।",
                "det": "कार्यस्थल पर सुरक्षा उपकरणों के अभाव में गंभीर दुर्घटना हुई जिससे स्थायी दिव्यांगता आई है। मालिक मुआवजा देने से मुकर रहा है।"
            },
            "5. सूदखोरों व फर्जी लोन ऐप्स द्वारा धमकी व ब्लैकमेल": {
                "act": "RBI रिकवरी गाइडलाइन्स एवं जबरन वसूली कानून (धारा 308 BNS)",
                "authority": "साइबर क्राइम सेल, एसपी (SP) एवं RBI लोकपाल",
                "rule": "बिना लाइसेंस सूदखोरी और धमकी देकर वसूली करना गैर-कानूनी है। सीधे FIR होती है।",
                "det": "अवैध ब्याज वसूली हेतु लोन एजेंट द्वारा धमकी, घर आकर गाली-गलौज और फोटो वायरल करने का ब्लैकमेल किया जा रहा है।"
            },
            "6. सरकारी दफ्तर में घूसखोरी, 'कल आना' और लाइन में भगा देना": {
                "act": "सेवा का अधिकार कानून (RTPS Act) एवं भ्रष्टाचार निवारण अधिनियम",
                "authority": "निगरानी ब्यूरो (Vigilance Bureau) एवं मुख्यमंत्री हेल्पलाइन",
                "rule": "तय समय में काम न करने पर सरकारी कर्मचारी के वेतन से प्रतिदिन ₹250 से ₹5000 जुर्माना कटता है।",
                "det": "वैध दस्तावेज देने के बावजूद बिना रिश्वत के संबंधित कर्मचारी द्वारा बार-बार चक्कर लगवाए जा रहे हैं।"
            },
            "7. दुकानदार या राशन डीलर द्वारा MRP से ज्यादा दाम व घटतौली": {
                "act": "लीगल मेट्रोलॉजी एक्ट 2009 एवं NFSA",
                "authority": "उपभोक्ता मामले विभाग एवं जिला आपूर्ति पदाधिकारी (DSO)",
                "rule": "MRP से ₹1 भी ज्यादा लेना या राशन कम तौलना गैर-कानूनी है। ₹25,000 जुर्माना और लाइसेंस रद्द होता है।",
                "det": "दुकानदार/कोटेदार द्वारा तय मूल्य से अधिक राशि वसूली गई और निर्धारित मात्रा से कम सामग्री दी गई।"
            },
            "8. ट्रेन में टीटीई (TTE) द्वारा अवैध वसूली व बदसलूकी": {
                "act": "भारतीय रेलवे अधिनियम एवं रेल सुरक्षा नियम",
                "authority": "रेलवे बोर्ड विजिलेंस, आरपीएफ (RPF) एवं रेल मदद 139",
                "rule": "टीटीई को यात्री से बदतमीजी करने या धक्का देने का कोई हक नहीं। केवल सरकारी रसीद दी जा सकती है।",
                "det": "यात्रा के दौरान टीटीई द्वारा नियम विरुद्ध पैसे की मांग और विरोध करने पर बदसलूकी की गई।"
            },
            "9. थाने में एफआईआर (FIR) दर्ज न करना (Zero FIR)": {
                "act": "सुप्रीम कोर्ट ललिता कुमारी दिशा-निर्देश एवं धारा 173 BNSS",
                "authority": "वरिष्ठ पुलिस अधीक्षक (SSP), डीजीपी एवं सीजेएम कोर्ट",
                "rule": "FIR न लिखने वाले पुलिस अधिकारी पर धारा 166A BNS के तहत खुद FIR दर्ज होती है।",
                "det": "घटना की लिखित सूचना देने के बावजूद थाना प्रभारी द्वारा FIR दर्ज करने से मना किया गया।"
            },
            "10. पैतृक जमीन पर दबंगों द्वारा अवैध कब्जा": {
                "act": "धारा 145/144 BNSS एवं नागरिक अधिकार संरक्षण कानून",
                "authority": "उप-विभागीय दंडाधिकारी (SDM) एवं सिविल न्यायालय",
                "rule": "गरीब की पैतृक भूमि पर जबरन कब्जे की कोशिश पर प्रशासन को तुरंत सुरक्षा देना और स्टे लगाना अनिवार्य है।",
                "det": "विपक्षी द्वारा प्रार्थी की वैध पैतृक जमीन पर बलपूर्वक अवैध कब्जे का प्रयास किया जा रहा है।"
            },
            "11. सड़क हादसे (Hit and Run) में सरकारी मुआवजा": {
                "act": "मोटर वाहन संशोधन अधिनियम (हिट एंड रन मुआवजा योजना)",
                "authority": "दावा अधिकरण (MACT) एवं जिला कलेक्टर राहत कोष",
                "rule": "मृत्यु पर सरकार द्वारा तत्काल ₹2 लाख और गंभीर घायल को ₹50,000 की राहत देने का कानून है।",
                "det": "सड़क दुर्घटना के उपरांत तत्काल सरकारी राहत कोष व बीमा क्लेम की मांग की जा रही है।"
            },
            "12. मुफ्त सरकारी वकील पाने हेतु आवेदन (DLSA)": {
                "act": "विधिक सेवा प्राधिकरण अधिनियम 1987 (अनुच्छेद 39A)",
                "authority": "जिला विधिक सेवा प्राधिकरण (DLSA) सचिव",
                "rule": "गरीब, मजदूर और महिला को कोर्ट केस लड़ने के लिए सरकार अपने खर्चे पर मुफ्त वकील उपलब्ध कराती है।",
                "det": "प्रार्थी आर्थिक रूप से असमर्थ है और उसे मुकदमे की पैरवी हेतु मुफ्त सरकारी वकील की आवश्यकता है।"
            },
            "13. मकान मालिक द्वारा बिना नोटिस जबरन बेदखली": {
                "act": "रेंट कंट्रोल एक्ट एवं भारतीय न्याय संहिता",
                "authority": "किराया नियंत्रक (Rent Controller) एवं स्थानीय पुलिस",
                "rule": "मकान मालिक बिना कोर्ट ऑर्डर के ताला नहीं तोड़ सकता, न ही बिजली-पानी काट सकता है।",
                "det": "मकान मालिक द्वारा बिना कानूनी नोटिस पानी-बिजली बंद कर जबरन मकान खाली कराने की धमकी दी जा रही है।"
            },
            "14. जातिगत भेदभाव, गाली-गलौज व सामाजिक बहिष्कार": {
                "act": "अनुसूचित जाति/जनजाति अत्याचार निवारण अधिनियम (SC/ST Act)",
                "authority": "पुलिस अधीक्षक (SP) एवं विशेष अदालत",
                "rule": "जाति के आधार पर अपमानित करने या रास्ता रोकने पर गैर-जमानती गिरफ्तारी होती है।",
                "det": "विपक्षी द्वारा जातिसूचक अपशब्दों का प्रयोग कर सार्वजनिक रूप से अपमानित और प्रताड़ित किया गया।"
            }
        }
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
        "send_wa": "📲 Send Legal Notice via WhatsApp",
        "def_name": "Sahil Kumar",
        "def_city": "West Champaran, Bihar",
        "def_accused": "Accused Employer / Officer",
        "law_prefix": "Applicable Law",
        "auth_prefix": "Competent Authority",
        "cases": {
            "1. Wage Theft & Unpaid Salary by Contractor/Company": {
                "act": "Payment of Wages Act 1936 & Industrial Disputes Act",
                "authority": "Labour Commissioner & District Magistrate (DM)",
                "rule": "Withholding wages is illegal. Labour department enforces up to 10x penalty and 18% interest.",
                "det": "I worked diligently for 2 months, total pending dues are Rs 24,000. Upon demanding my payment, I was verbally abused and threatened."
            },
            "2. Police Harassment, Brutality & Illegal Challan": {
                "act": "Bharatiya Nagarik Suraksha Sanhita (BNSS) & DK Basu Directives",
                "authority": "Superintendent of Police (SP), SPCA & NHRC",
                "rule": "Assault or abusive behavior without judicial order triggers Section 166A BNS with suspension and FIR.",
                "det": "I was subjected to unlawful public harassment, physical assault, and threats of fake challan by the police officer."
            },
            "3. Hospital Refusing Emergency Care or Detaining Patient/Body": {
                "act": "Supreme Court Parmanand Katara Verdict & Clinical Establishments Act",
                "authority": "Chief Medical Officer (CMO) & Health Department",
                "rule": "Hospitals cannot deny emergency care over advance payment. Detaining bodies or patients is a cognizable offense.",
                "det": "The hospital delayed emergency medical treatment deliberately by demanding upfront cash advance."
            },
            "4. Workplace Accident & Permanent Disability Compensation": {
                "act": "Employees Compensation Act 1923",
                "authority": "Compensation Commissioner & Labour Court",
                "rule": "Employer is strictly liable to pay Rs 5 to 20 Lakhs compensation and life pension for duty injuries.",
                "det": "Due to lack of safety equipment, a severe accident occurred causing permanent disability. The employer refuses compensation."
            },
            "5. Illegal Money Lenders & Loan App Blackmail/Threats": {
                "act": "RBI Fair Recovery Guidelines & Extortion Section 308 BNS",
                "authority": "Cyber Crime Cell, SP & RBI Ombudsman",
                "rule": "Unlicensed money lending and threatening calls/photo leaks are strictly illegal, leading to immediate arrest.",
                "det": "The loan recovery agent is issuing criminal threats, visiting home unlawfully, and blackmailing to leak private photos."
            },
            "6. Government Office Bribery & Endless Delay (RTPS)": {
                "act": "Right to Public Services Act (RTPS) & Prevention of Corruption Act",
                "authority": "Vigilance Bureau & Chief Minister Grievance Portal",
                "rule": "Officers failing to deliver public services on time face automatic daily salary deduction of Rs 250 to Rs 5000.",
                "det": "Despite submitting all valid documents, the government clerk is withholding work and demanding illegal gratification."
            },
            "7. Shopkeeper/Ration Dealer Overpricing (MRP) & Underweighing": {
                "act": "Legal Metrology Act 2009 & National Food Security Act",
                "authority": "Consumer Affairs Department & District Supply Officer",
                "rule": "Charging above MRP or underweighing attracts Rs 25,000 fine and cancellation of commercial license.",
                "det": "The vendor charged price above printed MRP and delivered commodities below the legally prescribed weight."
            },
            "8. Railway TTE Extortion & Passenger Harassment": {
                "act": "Indian Railway Act & Railway Safety Regulations",
                "authority": "Railway Vigilance Board, RPF & RailMadad 139",
                "rule": "TTE has zero legal power to assault or deboard passengers forcefully. Only official EFT receipts are allowed.",
                "det": "The on-duty TTE demanded illegal money in violation of rules and engaged in aggressive misbehavior upon objection."
            },
            "9. Police Station Refusing to Register FIR (Zero FIR Right)": {
                "act": "Supreme Court Lalita Kumari Guidelines & Section 173 BNSS",
                "authority": "Senior Superintendent of Police (SSP), DGP & CJM Court",
                "rule": "Refusal to register an FIR for a cognizable crime makes the police officer liable for criminal trial under Sec 166A BNS.",
                "det": "Despite submitting a written complaint detailing the cognizable offense, the station in-charge refused to register an FIR."
            },
            "10. Land Encroachment & Illegal Grabbing by Strongmen": {
                "act": "Section 145/144 BNSS & Civil Rights Protection Laws",
                "authority": "Sub-Divisional Magistrate (SDM) & Civil Court",
                "rule": "Police and administration are obligated to issue immediate stay and provide protection against land grabbing.",
                "det": "The opposite party is attempting to forcefully and illegally grab my legally inherited ancestral land."
            },
            "11. Road Accident (Hit and Run) Government Compensation": {
                "act": "Motor Vehicles Amendment Act (Hit & Run Scheme)",
                "authority": "MACT & District Magistrate Relief Fund",
                "rule": "Government provides mandatory interim relief of Rs 2 Lakhs for death and Rs 50,000 for grievous injury.",
                "det": "Following a serious road accident, formal application is submitted for immediate compensation and emergency relief fund."
            },
            "12. Application for Free Government Lawyer (NALSA/DLSA)": {
                "act": "Legal Services Authorities Act 1987 (Article 39A)",
                "authority": "District Legal Services Authority (DLSA) Secretary",
                "rule": "Every underprivileged citizen, worker, and woman is entitled to a free government advocate at state expense.",
                "det": "I am financially incapable of bearing litigation expenses and formally request a free government advocate."
            },
            "13. Landlord Forcible Eviction Without Legal Notice": {
                "act": "R
