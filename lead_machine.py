import streamlit as st
import streamlit.components.v1 as components
import urllib.parse
from datetime import datetime

# 1. Page Configuration
st.set_page_config(
    page_title="महा-सेवा AI — राष्ट्रीय नागरिक विधिक सुरक्षा व SOS मिशन",
    page_icon="🇮🇳",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Modern Dark UI
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

# Language Setup
LANG_DATA = {
    "🇮🇳 हिन्दी": {
        "title": "महा-सेवा AI (MAHA SEVA AI)",
        "sub": "सच्चा जन-अधिकार • 24x7 रात की सुरक्षा • बोलकर शिकायत • रोज़गार व एम्बुलेंस",
        "tag": "⚡ 24x7 अखंड भारत नागरिक व विधिक सुरक्षा मिशन",
        "nav_lbl": "📂 सेवा श्रेणी चुनें:",
        "sec_sos": "🚨 रात की सुरक्षा व लाइव GPS SOS",
        "sec_rights": "⚖️ विधिक अधिकार व सच्चा कानूनी नोटिस",
        "sec_voice": "🎙️ बोलकर शिकायत दर्ज करें (माइक)",
        "sec_fraud": "🛡️ साइबर फ्रॉड व मैसेज चेकर",
        "sec_health": "🏥 दवा व एम्बुलेंस सहायता",
        "sec_job": "💼 रोज़गार व हेल्पर डेस्क"
    },
    "🇬🇧 English": {
        "title": "MAHA SEVA AI — Citizen Mission",
        "sub": "Real Legal Rights • 24x7 Night Safety • Voice Assistance • Emergency",
        "tag": "⚡ 24x7 Pan-India Sovereign Citizen Legal & Welfare Infrastructure",
        "nav_lbl": "📂 Select Service Category:",
        "sec_sos": "🚨 Night Safety & Live GPS SOS",
        "sec_rights": "⚖️ Real Legal Notice Generator",
        "sec_voice": "🎙️ Voice-to-Text Complaint",
        "sec_fraud": "🛡️ Cyber Shield & SMS Verifier",
        "sec_health": "🏥 Health & Ambulance Support",
        "sec_job": "💼 Employment & Helper Desk"
    }
}

chosen_lang = st.radio("🌐 भाषा चुनें / Select Language:", list(LANG_DATA.keys()), horizontal=True)
T = LANG_DATA.get(chosen_lang, LANG_DATA["🇮🇳 हिन्दी"])

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
        T["sec_sos"],
        T["sec_rights"],
        T["sec_voice"],
        T["sec_fraud"],
        T["sec_health"],
        T["sec_job"]
    ],
    horizontal=True
)

st.markdown("---")

# ================= TAB 1: NIGHT SAFETY & LIVE GPS SOS =================
if nav_choice == T["sec_sos"]:
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

    st.write("### 📍 लाइव GPS लोकेशन (सटीक गूगल मैप्स लिंक)")
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

    col_s1, col_s2 = st.columns(2)
    with col_s1:
        f_number = st.text_input("परिवार/भाई/पिता का मोबाइल नंबर:", value="7484878440")
    with col_s2:
        v_person_name = st.text_input("पीड़ित का नाम:", value="साहिल")

    road_location = st.text_input("वर्तमान जगह / सड़क का नाम:", value="मुख्य सड़क / तिराहा")

    sos_wa_text = f"आपातकालीन अलर्ट (SOS)! मुझे सहायता की आवश्यकता है। नाम: {v_person_name}। लोकेशन: {road_location}। समय: {current_time_str}। कृपया तुरंत संपर्क करें।"
    enc_sos = urllib.parse.quote(sos_wa_text)
    st.markdown(f'<a href="https://wa.me/91{f_number}?text={enc_sos}" target="_blank" class="btn-green">📲 1-क्लिक परिवार को लोकेशन व SOS भेजें</a>', unsafe_allow_html=True)

    # Audio Siren
    st.write("### 🔊 पैनिक सायरन (भीड़ का ध्यान आकर्षित करने हेतु)")
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

# ================= TAB 2: REAL LEGAL RIGHTS & NOTICE =================
elif nav_choice == T["sec_rights"]:
    st.write("### ⚖️ जन-अधिकार व वास्तविक कानूनी नोटिस")
    st.caption("केवल सच्ची घटना और वास्तविक तथ्यों के आधार पर ही कानूनी कार्रवाई होती है।")

    LEGAL_CASES = {
        "1. ठेकेदार या कंपनी ने मजदूरी/वेतन रोक लिया": {
            "act": "पेमेंट ऑफ वेजेस एक्ट 1936 एवं बीएनएसएस",
            "authority": "श्रम आयुक्त (Labour Commissioner) व जिलाधिकारी (DM)",
            "rule": "मजदूरी दबाना गैर-कानूनी अपराध है। श्रम विभाग बकाया राशि 10 गुना हर्जाने और 18% ब्याज सहित दिलाता है।",
            "det": "मैंने 2 महीने पूरी ईमानदारी से कार्य किया, जिसकी कुल बकाया राशि ₹24,000 है। मांगने पर गाली-गलौज व धमकी दी जा रही है।"
        },
        "2. पुलिस द्वारा गैर-कानूनी मारपीट या फर्जी चालान": {
            "act": "भारतीय नागरिक सुरक्षा संहिता (BNSS) व डी.के. बसु गाइडलाइन्स",
            "authority": "पुलिस अधीक्षक (SP), राज्य पुलिस शिकायत प्राधिकरण व NHRC",
            "rule": "बिना जुर्म मारपीट या गाली-गलौज करने पर धारा 166A BNS के तहत पुलिसकर्मी पर निलंबन व मुकदमा बनता है।",
            "det": "संबंधित पुलिसकर्मी द्वारा बिना किसी अपराध के मेरे साथ सार्वजनिक रूप से अभद्रता, मारपीट व अवैध चालान की धमकी दी गई।"
        },
        "3. अस्पताल द्वारा इमरजेंसी में भर्ती न करना या शव रोकना": {
            "act": "सुप्रीम कोर्ट परमानंद कटारा फैसला व क्लिनिकल एस्टेब्लिशमेंट एक्ट",
            "authority": "मुख्य चिकित्सा अधिकारी (CMO) व स्वास्थ्य विभाग",
            "rule": "इमरजेंसी में पैसे मांगकर इलाज से इनकार नहीं किया जा सकता। शव या मरीज को बंधक बनाना संज्ञेय अपराध है।",
            "det": "इमरजेंसी में अस्पताल द्वारा पहले पैसे जमा करने का दबाव बनाकर इलाज में जानबूझकर देरी की गई।"
        },
        "4. कार्यस्थल पर हादसा व शारीरिक अपंगता (मुआवजा)": {
            "act": "कर्मचारी मुआवजा कानून 1923 (Employees Compensation Act)",
            "authority": "मुआवजा आयुक्त एवं श्रम न्यायालय",
            "rule": "ड्यूटी के दौरान दुर्घटना होने पर मालिक को ₹5 लाख से ₹20 लाख का मुआवजा व आजीवन पेंशन देना अनिवार्य है।",
            "det": "कार्यस्थल पर सुरक्षा उपकरणों के अभाव में गंभीर दुर्घटना हुई जिससे स्थायी दिव्यांगता आई है। मालिक मुआवजा देने से मुकर रहा है।"
        },
        "5. सूदखोरों व फर्जी लोन ऐप्स द्वारा धमकी व ब्लैकमेल": {
            "act": "RBI रिकवरी गाइडलाइन्स व धारा 308 BNS (जबरन वसूली)",
            "authority": "साइबर क्राइम सेल, एसपी (SP) व RBI लोकपाल",
            "rule": "बिना लाइसेंस सूदखोरी और धमकी देकर वसूली करना गैर-कानूनी है। सीधे FIR और गिरफ्तारी होती है।",
            "det": "अवैध ब्याज वसूली हेतु लोन एजेंट द्वारा धमकी, घर आकर गाली-गलौज और फोटो वायरल करने का ब्लैकमेल किया जा रहा है।"
        },
        "6. सरकारी दफ्तर में घूसखोरी व 'कल आना' अपमान": {
            "act": "सेवा का अधिकार कानून (RTPS Act) व भ्रष्टाचार निवारण अधिनियम",
            "authority": "निगरानी ब्यूरो (Vigilance) व मुख्यमंत्री हेल्पलाइन",
            "rule": "तय समय में काम न करने पर संबंधित सरकारी कर्मचारी के वेतन से प्रतिदिन ₹250 से ₹5000 जुर्माना कटता है।",
            "det": "वैध दस्तावेज देने के बावजूद बिना रिश्वत के संबंधित कर्मचारी द्वारा बार-बार चक्कर लगवाए जा रहे हैं।"
        }
    }

    selected_issue = st.radio("📌 अपनी समस्या चुनें:", list(LEGAL_CASES.keys()))
    case_info = LEGAL_CASES[selected_issue]

    st.info(f"⚖️ **कानून:** {case_info['act']} | **प्राधिकारी:** {case_info['authority']}")

    col_v1, col_v2 = st.columns(2)
    with col_v1:
        v_name = st.text_input("पीड़ित का नाम:", value="साहिल कुमार")
    with col_v2:
        v_loc = st.text_input("जिला व राज्य:", value="पश्चिम चंपारण, बिहार")

    v_phone = st.text_input("मोबाइल नंबर:", value="7484878440")
    v_accused = st.text_input("दोषी पक्ष / अधिकारी का नाम:", value="संबंधित दोषी पक्ष / अधिकारी")

    issue_code = selected_issue.split(".")[0].strip()
    v_details = st.text_area("घटना का सच्चा विवरण:", value=case_info["det"], key=f"det_text_{issue_code}")

    if st.button("⚡ आधिकारिक विधिक शिकायत पत्र व नोटिस तैयार करें"):
        legal_notice = f"""======================================================================
आधिकारिक कानूनी विधिक शिकायत पत्र व नोटिस
(अधिनियम: {case_info['act']})
दिनांक: {today_str}

सेवा में,
1. {case_info['authority']}, {v_loc}
2. राष्ट्रीय मानवाधिकार आयोग (NHRC) / विधिक निगरानी बोर्ड

विषय: '{selected_issue}' के संबंध में दोषी '{v_accused}' पर प्राथमिकी (FIR) व दंडात्मक कार्रवाई बाबत।

महोदय,
प्रार्थी {v_name} (मोबाइल: +91 {v_phone}), निवासी {v_loc} सादर सूचित करता है कि:

1. यह कि प्रार्थी भारत का संविधान-सम्मत नागरिक है और विपक्षी '{v_accused}' द्वारा प्रार्थी के मौलिक व वैधानिक अधिकारों का खुला उल्लंघन किया गया है।
2. तथ्यात्मक घटनाक्रम (सच्चा विवरण):
"{v_details}"
3. विधिक नियम व कानूनी आधार:
- {case_info['rule']}

अतः सक्षम प्राधिकारी से प्रार्थना है कि दोषी '{v_accused}' के विरुद्ध कानून सम्मत कार्रवाई कर प्रार्थी को उसका संपूर्ण देय हक व सुरक्षा अविलंब प्रदान की जाए।

भवदीय:
{v_name}
संपर्क सूत्र: +91 {v_phone}
डिजिटल निगरानी: महा-सेवा AI राष्ट्रीय विधिक साक्षरता मिशन
======================================================================"""

        st.success("🟢 आधिकारिक विधिक नोटिस तैयार:")
        st.text_area("📄 तैयार कानूनी दस्तावेज:", legal_notice, height=220)

        st.markdown(f"""
        <div class="caution-card">
            <h3 style="color:#EF4444; margin:0 0 6px 0;">⚖️ इस मामले में आपका कानूनी कवच:</h3>
            <p style="margin:0; font-size:14px; color:#FCA5A5;">{case_info['rule']}</p>
        </div>
        """, unsafe_allow_html=True)

        enc_legal = urllib.parse.quote(legal_notice)
        st.markdown(f'<a href="https://wa.me/?text={enc_legal}" target="_blank" class="btn-green">📲 यह शिकायत WhatsApp पर भेजें</a>', unsafe_allow_html=True)

# ================= TAB 3: VOICE-TO-TEXT (बोलकर शिकायत) =================
elif nav_choice == T["sec_voice"]:
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

# ================= TAB 4: CYBER FRAUD VERIFIER =================
elif nav_choice == T["sec_fraud"]:
    st.write("### 🛡️ साइबर फ्रॉड व असली/नकली मैसेज चेकर")
    st.caption("संदिग्ध मैसेज या WhatsApp लिंक यहाँ पेस्ट करें और तुरंत सच्चाई जाँचें:")

    susp_msg = st.text_area("📝 मैसेज यहाँ पेस्ट करें:", value="बिजली बिल जमा न होने के कारण आज रात 9:30 बजे बिजली काट दी जाएगी। इस 10 अंकों के नंबर पर संपर्क करें।")
    if st.button("🚨 मैसेज की सच्चाई जाँचें (Check Scam)"):
        low_msg = susp_msg.lower()
        if any(w in low_msg for w in ["बिजली", "electricity", "लॉटरी", "lottery", "apk", "telegram", "क्लिक", "task"]):
            st.error("🚨 100% प्रमाणित साइबर फ्रॉड (SCAM DETECTED!)")
            st.markdown("""
            <div class="caution-card">
                <h3 style="color:#EF4444; margin:0 0 6px 0;">⚠️ सावधान! यह फ्रॉड मैसेज है:</h3>
                <ul style="margin:0; padding-left:18px; font-size:14px; color:#FCA5A5;">
                    <li>बिजली विभाग कभी व्यक्तिगत 10 अंकों के नंबर से अल्टीमेटम नहीं भेजता।</li>
                    <li>किसी भी अनजान लिंक या APK फाइल को डाउनलोड न करें।</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.success("🟢 मैसेज में कोई सीधा साइबर फ्रॉड लिंक नहीं मिला। फिर भी सतर्क रहें।")

    st.markdown("""
    <div class="caution-card">
        <h3 style="color:#EF4444; margin:0 0 6px 0;">📞 राष्ट्रीय साइबर क्राइम हेल्पलाइन:</h3>
        <p style="font-size:15px; margin:0;"><a href="tel:1930" class="btn-red-call">📞 1930 पर तुरंत कॉल करें</a> (पैसे कटने पर 2 घंटे के अंदर)</p>
    </div>
    """, unsafe_allow_html=True)

# ================= TAB 5: HEALTH =================
elif nav_choice == T["sec_health"]:
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
elif nav_choice == T["sec_job"]:
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
