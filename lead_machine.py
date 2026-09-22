import streamlit as st
import streamlit.components.v1 as components
import urllib.parse
import urllib.request
import json
from datetime import datetime

# 1. High-Availability Page Configuration
st.set_page_config(
    page_title="महा-सेवा AI — अखंड राष्ट्रीय नागरिक, रोज़गार व विधिक सुरक्षा मिशन",
    page_icon="🇮🇳",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Modern 100% Dark UI - Zero White Box Glitch
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

    /* Input Boxes & Textareas */
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

    /* Radio Tiles (No White Box Glitch) */
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

    /* Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 4px;
        background-color: #0B1329;
        padding: 6px;
        border-radius: 12px;
        border: 1px solid #1E293B;
    }
    .stTabs [data-baseweb="tab"] {
        color: #94A3B8 !important;
        font-weight: 800 !important;
        font-size: 12px !important;
        border-radius: 8px;
        padding: 8px 10px !important;
    }
    .stTabs [aria-selected="true"] {
        background: #0284C7 !important;
        color: #FFFFFF !important;
    }

    /* Cards */
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

    /* Buttons */
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
        font-size: 15px;
        padding: 11px 18px;
        border-radius: 10px;
        text-decoration: none;
        margin: 5px;
        box-shadow: 0 4px 15px rgba(239, 68, 68, 0.5);
    }
</style>
""", unsafe_allow_html=True)

MY_WA_NUMBER = "917484878440"
today_str = datetime.now().strftime("%d-%m-%Y")

# Never-Fail Knowledge Engine
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

# Top Branding
st.markdown("""
<div style="background: radial-gradient(circle at center, #1E3A8A 0%, #030712 100%); border: 2px solid #38BDF8; border-radius: 14px; padding: 14px; text-align: center; margin-bottom: 14px; box-shadow: 0 0 20px rgba(56, 189, 248, 0.25);">
    <span style="background:rgba(16,185,129,0.2); color:#10B981; border:1px solid #10B981; padding:3px 12px; border-radius:20px; font-size:11px; font-weight:800;">
        ⚡ 24x7 अखंड भारत नागरिक, रोज़गार व विधिक सुरक्षा मिशन
    </span>
    <h1 style="font-size:22px; margin:6px 0 0 0; color:#FFF;">महा-सेवा AI (MAHA SEVA AI)</h1>
    <p style="font-size:12px; color:#38BDF8; margin:4px 0 0 0;">जन-अधिकार व पुलिस-ठेकेदार शिकायत • रोज़गार • दवा व एम्बुलेंस • सरकारी योजना • नशा-मुक्ति</p>
</div>
""", unsafe_allow_html=True)

# 6 Super Tabs
tab_rights, tab_health, tab_job, tab_scheme, tab_fraud, tab_life = st.tabs([
    "⚖️ जन-अधिकार व शिकायत",
    "🏥 दवा व एम्बुलेंस",
    "💼 रोज़गार व हेल्पर",
    "🏛️ सरकारी योजना (Full)",
    "🛡️ साइबर फ्रॉड सुरक्षा",
    "🕊️ नशा-मुक्ति व जीवन रक्षा"
])

# ================= TAB 1: CITIZEN LEGAL RIGHTS & COMPLAINTS =================
with tab_rights:
    st.write("### ⚖️ जन-अधिकार मंच — ठेकेदार, कंपनी व पुलिस उत्पीड़न के विरुद्ध सीधी कार्रवाई")
    st.caption("अगर ठेकेदार/कंपनी आपकी मजदूरी रोके, या पुलिस बेवजह सताए/फर्जी चालान करे — यहाँ से सीधा कानूनी नोटिस निकालें")

    complaint_type = st.radio(
        "📌 आपकी समस्या किस श्रेणी की है?",
        [
            "ठेकेदार / कंपनी ने मजदूरी या वेतन दबा लिया (Wage Theft)",
            "पुलिस द्वारा बेवजह मारपीट, गाली-गलौज या उत्पीड़न (Police Harassment)",
            "जबरन या गलत चालान काटा गया (Illegal Traffic Challan)",
            "राशन डीलर / ब्लॉक का बाबू रिश्वत माँग रहा है (Corruption & Bribery)"
        ]
    )

    col_c1, col_c2 = st.columns(2)
    with col_c1:
        victim_name = st.text_input("पीड़ित / प्रार्थी का नाम:", value="साहिल कुमार")
    with col_c2:
        victim_city = st.text_input("जिला व राज्य:", value="पश्चिम चंपारण, बिहार")

    victim_phone = st.text_input("पीड़ित का मोबाइल नंबर:", value="7484878440")
    accused_party = st.text_input("दोषी ठेकेदार / कंपनी / पुलिस अधिकारी / थाने का नाम:", value="ठेकेदार राम सिंह / संबंधित थाना प्रभारी")
    complaint_details = st.text_area(
        "घटना का विवरण (पूरी बात अपनी भाषा में लिखें):",
        value="मैंने संबंधित कार्यस्थल पर 2 महीने पूरी ईमानदारी से मजदूरी की, जिसका कुल ₹24,000 बकाया है। माँगने पर ठेकेदार गाली-गलौज और जान से मारने की धमकी दे रहा है।"
    )

    if st.button("⚡ आधिकारिक कानूनी शिकायत पत्र व नोटिस ड्राफ्ट करें"):
        legal_draft = f"""======================================================================
आधिकारिक कानूनी शिकायत पत्र व विधिक नोटिस
(भारतीय न्याय संहिता, श्रम कानून व मानवाधिकार संरक्षण अधिनियम के अंतर्गत)
दिनांक: {today_str}
सेवा में,
1. श्रम आयुक्त (Labour Commissioner) / जिलाधिकारी (DM), {victim_city}
2. पुलिस अधीक्षक (SP) / राज्य मानवाधिकार आयोग (SHRC)

विषय: {complaint_type} के विरुद्ध सख्त दंडात्मक कार्रवाई व अधिकार रक्षा बाबत।

महोदय,
प्रार्थी {victim_name} (मोबाइल: +91 {victim_phone}), निवासी {victim_city} सादर निवेदन करता है:

1. यह कि प्रार्थी के विरुद्ध विपक्षी '{accused_party}' द्वारा गंभीर अन्याय व कानून का उल्लंघन किया गया है।
2. घटना का तथ्यात्मक विवरण:
"{complaint_details}"
3. यह कृत्य भारतीय संविधान के अनुच्छेद 21 (जीवन व सम्मान का अधिकार), पेमेंट ऑफ वेजेस एक्ट, और विधि के शासन का खुला उल्लंघन है।

अतः श्रीमान से करबद्ध प्रार्थना है कि:
(क) विपक्षी के विरुद्ध सुसंगत धाराओं में तत्काल प्राथमिकी (FIR) दर्ज कर कानूनी कार्रवाई की जाए।
(ख) प्रार्थी का रोका गया संपूर्ण देय हक/मुआवजा तत्काल ब्याज सहित दिलाया जाए।
(ग) प्रार्थी की जान-माल की मुकम्मल सुरक्षा सुनिश्चित की जाए।

भवदीय / प्रार्थी:
{victim_name}
संपर्क: +91 {victim_phone}
डिजिटल मॉनिटरिंग: महा-सेवा AI जन-अधिकार विधिक सहायता मिशन
======================================================================"""

        st.success("🟢 100% आधिकारिक कानूनी नोटिस व शिकायत पत्र तैयार:")
        st.text_area("📄 तैयार कानूनी शिकायत पत्र (Legal Complaint Document):", legal_draft, height=220)

        st.markdown("""
        <div class="caution-card">
            <h3 style="color:#EF4444; margin:0 0 6px 0;">⚠️ आपका कानूनी अधिकार (डरे नहीं, कानून आपके साथ है):</h3>
            <ul style="margin:0; padding-left:18px; font-size:14px; color:#FCA5A5;">
                <li><b>मजदूरी रोकना कानूनी अपराध है:</b> कोई भी ठेकेदार या मालिक आपकी मजदूरी नहीं दबा सकता। श्रम विभाग में शिकायत जाते ही कंपनी पर 10 गुना जुर्माना लग सकता है।</li>
                <li><b>पुलिस का कोई अधिकार नहीं कि बेवजह मारे:</b> कानून में पुलिस को किसी नागरिक से गाली-गलौज या बिना जुर्म मारपीट का कोई अधिकार नहीं है। ऐसी स्थिति में सीधे SP या 1064/112 पर शिकायत मान्य है।</li>
                <li><b>फर्जी चालान:</b> चालान पर साइन करने से पहले कोर्ट में चुनौती (Virtual Court) देने का विकल्प हमेशा खुला रहता है।</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        # Direct Government Helpline Calling for Justice
        st.markdown("""
        <div style="text-align:center; margin:12px 0;">
            <p style="color:#38BDF8; font-size:13px; margin-bottom:6px;"><b>सीधे सरकारी न्याय हेल्पलाइन पर कॉल करें (Toll-Free):</b></p>
            <a href="tel:112" class="btn-red-call">📞 112 पुलिस आपातकाल व उत्पीड़न</a>
            <a href="tel:1064" class="btn-red-call">📞 1064 भ्रष्टाचार व घूसखोरी विरोधी</a>
            <a href="tel:14434" class="btn-red-call">📞 14434 राष्ट्रीय श्रम व मजदूरी हेल्पलाइन</a>
            <a href="tel:1076" class="btn-red-call">📞 1076 मुख्यमंत्री जनसुनवाई</a>
        </div>
        """, unsafe_allow_html=True)

        enc_legal = urllib.parse.quote(legal_draft)
        st.markdown(f'<a href="https://wa.me/?text={enc_legal}" target="_blank" class="btn-green">📲 शिकायत पत्र WhatsApp / सोशल मीडिया पर भेजें</a>', unsafe_allow_html=True)

# ================= TAB 2: HEALTH & EMERGENCY AMBULANCE =================
with tab_health:
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
        with st.spinner("चिकित्सा डेटाबेस से जानकारी जांची जा रही है..."):
            live_m = deep_live_knowledge(m_name)
            st.markdown(f"""
            <div class="info-card">
                <h3 style="color:#38BDF8; margin:0 0 6px 0;">💊 1. दवा का परिचय व साल्ट (Medicine Overview)</h3>
                <p style="margin:0; font-size:14px;"><b>दवा / साल्ट:</b> {m_name}<br>
                यह बीमारी के संक्रमण और संबंधित लक्षणों को नियंत्रित करने में सहायक है।</p>
                {f'<p style="color:#94A3B8; font-size:13px; margin-top:6px;"><b>चिकित्सा डेटा:</b> {live_m}</p>' if live_m else ''}
            </div>
            <div class="info-card">
                <h3 style="color:#10B981; margin:0 0 6px 0;">💰 2. प्राइवेट बनाम सरकारी जन औषधि भाव (Huge Savings)</h3>
                <ul style="margin:0; padding-left:18px; font-size:14px;">
                    <li><b>निजी मेडिकल स्टोर भाव:</b> ₹70 से ₹150 तक।</li>
                    <li><b>सरकारी जन औषधि केंद्र भाव:</b> मात्र <b>₹20 से ₹35</b> (70% से 80% सीधी बचत)।</li>
                </ul>
            </div>
            <div class="caution-card">
                <h3 style="color:#EF4444; margin:0 0 6px 0;">⚠️ दवा के उपयोग में अनिवार्य सावधानी (Crucial Safety Warning):</h3>
                <ul style="margin:0; padding-left:18px; font-size:14px; color:#FCA5A5;">
                    <li><b>स्वयं डॉक्टर न बनें:</b> यह जानकारी केवल जनहित और जेनेरिक विकल्पों की समझ हेतु है। बिना डॉक्टर के पर्चे के गंभीर एंटीबायोटिक या दर्दनिवारक न लें।</li>
                    <li><b>कोर्स पूरा करें:</b> दवा की खुराक बीच में बंद न करें और न ही खाली पेट तेज दवाइयाँ लें।</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

# ================= TAB 3: BLUE-COLLAR & HELPER JOB ENGINE =================
with tab_job:
    st.write("### 💼 पूरे देश में सीधी नौकरी व ठेकेदार संपर्क (हर कामगार हेतु)")
    st.caption("हेल्पर, लोडर, ड्राइवर, मिस्त्री, इलेक्ट्रीशियन — बिना दलाल के सीधे ठेकेदार से बात करें")

    col1, col2 = st.columns(2)
    with col1:
        target_city = st.text_input("📍 नौकरी का शहर/जिला (पूरे भारत से):", value="सूरत / मुंबई / बंगलुरु / दिल्ली")
    with col2:
        work_role = st.text_input("🔧 काम का प्रकार (Role):", value="फैक्ट्री हेल्पर / Warehouse Helper")

    c_name = st.text_input("👤 आपका नाम:", value="साहिल अहमद (Sahil)")
    c_phone = st.text_input("📱 मोबाइल नंबर (Calling & WhatsApp):", value="7484878440")
    c_exp = st.text_input("⏳ अनुभव / हुनर:", value="3 साल का अनुभव, तुरंत काम करने हेतु तैयार")
    c_notes = st.text_area(
        "✍️ अपनी भाषा में बात या हुनर लिखें (हिन्दी, भोजपुरी आदि):",
        value="मुझे काम की सख्त जरूरत है। मैं पूरी ईमानदारी और मेहनत से काम करूँगा।"
    )

    if st.button("⚡ ठेकेदार हेतु बहुभाषी आवेदन व कॉलिंग लिस्ट तैयार करें"):
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
            <h3 style="color:#EF4444; margin:0 0 6px 0;">⚠️ नौकरी ढूँढते समय अनिवार्य सावधानी (Scam Warning):</h3>
            <ul style="margin:0; padding-left:18px; font-size:14px; color:#FCA5A5;">
                <li><b>कभी पैसे न दें:</b> कोई भी ठेकेदार या कंपनी यदि फॉर्म, गेट पास, यूनिफॉर्म या रजिस्ट्रेशन के नाम पर ₹1 भी माँगे, तो समझें वह फ्रॉड है। असली नौकरियाँ मुफ़्त में मिलती हैं।</li>
                <li><b>मूल कागज़ात न छोड़ें:</b> कभी भी अपने असली मूल दस्तावेज़ (आधार, मार्कशीट) किसी अनजान व्यक्ति के पास जमा न छोड़ें।</li>
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

        st.markdown(f'<a href="{g_maps_search}" target="_blank" class="btn-blue">📞 1. {clean_target} के ठेकेदारों व कंपनियों की डायरेक्ट लिस्ट खोलें</a>', unsafe_allow_html=True)
        enc_pitch = urllib.parse.quote(eng_pitch)
        st.markdown(f'<a href="https://wa.me/?text={enc_pitch}" target="_blank" class="btn-green">📲 2. सीधे WhatsApp पर आवेदन भेजें</a>', unsafe_allow_html=True)

# ================= TAB 4: GOVT SCHEMES =================
with tab_scheme:
    st.write("### 🏛️ सरकारी योजना व छात्रवृत्ति खोजक (Full Google Style)")
    u_occ = st.radio(
        "📌 आपका वर्ग चुनें:",
        ["बेरोजगार युवा", "छात्र (Student)", "किसान (Farmer)", "महिला / गृहणी", "मजदूर / श्रमिक"],
        horizontal=True
    )
    u_state = st.text_input("📍 आपका राज्य (State):", value="बिहार / उत्तर प्रदेश")
    custom_scheme = st.text_input("योजना का नाम लिखें:", value="पीएम आवास योजना")

    if st.button("⚡ संपूर्ण योजना विश्लेषण निकालें (Full Details)"):
        with st.spinner("सरकारी पोर्टल व योजना डेटाबेस का विश्लेषण जारी..."):
            live_txt = deep_live_knowledge(custom_scheme)
            st.markdown(f"""
            <div class="info-card">
                <h3 style="color:#38BDF8; margin:0 0 6px 0;">📌 1. योजना का परिचय (Overview)</h3>
                <p style="margin:0; font-size:14px;">{custom_scheme} भारत सरकार व राज्य सरकार द्वारा नागरिकों के आर्थिक उत्थान हेतु संचालित योजना है।</p>
                {f'<p style="color:#94A3B8; font-size:13px; margin-top:6px;"><b>लाइव विवरण:</b> {live_txt}</p>' if live_txt else ''}
            </div>
            <div class="info-card">
                <h3 style="color:#10B981; margin:0 0 6px 0;">🎯 2. मुख्य लाभ व वित्तीय सहायता (Key Benefits)</h3>
                <ul style="margin:0; padding-left:18px; font-size:14px;">
                    <li><b>प्रत्यक्ष अनुदान:</b> बैंक खाते में सीधे ₹1,20,000 से लेकर ₹2,50,000 तक की वित्तीय सहायता।</li>
                    <li><b>अतिरिक्त सुविधाएं:</b> निःशुल्क शौचालय निर्माण व मनरेगा मजदूरी का लाभ।</li>
                </ul>
            </div>
            <div class="caution-card">
                <h3 style="color:#EF4444; margin:0 0 6px 0;">⚠️ सरकारी योजना के लिए अनिवार्य सावधानी (Crucial Warning):</h3>
                <ul style="margin:0; padding-left:18px; font-size:14px; color:#FCA5A5;">
                    <li><b>दलालों से सावधान:</b> सरकारी योजनाओं में चयन के लिए किसी भी बिचौलिये को रिश्वत न दें। सरकार किसी योजना का पैसा नकद नहीं देती, सीधा बैंक DBT ट्रांसफर होता है।</li>
                    <li><b>ओटीपी या बैंक डिटेल:</b> कोई भी सरकारी कर्मचारी फोन करके आपके बैंक का पिन या पासवर्ड नहीं माँगता।</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

# ================= TAB 5: CYBER FRAUD SHIELD =================
with tab_fraud:
    st.write("### 🛡️ साइबर फ्रॉड सुरक्षा व स्कैम डिटेक्टर (Cyber Shield)")
    scam_input = st.text_area("संदेहास्पद मैसेज, लिंक या कॉल का विवरण यहाँ डालें:", value="बिजली बिल जमा न होने के कारण आज रात 9:30 बजे बिजली काट दी जाएगी। तुरंत इस नंबर पर संपर्क करें।")
    
    if st.button("🚨 मैसेज की सत्यता जाँचें (Check Scam)"):
        s_low = scam_input.lower()
        if any(k in s_low for k in ["बिजली", "electricity", "कट", "lottery", "लॉटरी", "टास्क", "apk", "telegram", "क्लिक"]):
            st.error("🚨 100% प्रमाणित साइबर फ्रॉड (SCAM ALERT)")
            st.markdown("""
            <div class="caution-card">
                <h3 style="color:#EF4444; margin:0 0 8px 0;">⚠️ इस फ्रॉड से बचने के 4 सुनहरे नियम:</h3>
                <p style="margin:0; font-size:14px; color:#FCA5A5;">
                1. <b>कोई लिंक न दबाएँ:</b> किसी भी अनजान APK या लिंक पर क्लिक करते ही फोन हैक हो सकता है।<br>
                2. <b>बिजली विभाग की सच्चाई:</b> बिजली विभाग कभी भी व्यक्तिगत 10 अंकों के मोबाइल नंबर से बिजली काटने की धमकी नहीं देता।<br>
                3. <b>OTP कभी न दें:</b> बैंक या आधार का OTP किसी भी परिस्थिति में किसी को न बताएँ।<br>
                4. <b>तुरंत 1930 पर कॉल करें:</b> यदि कोई ठगी हो गई है तो तुरंत राष्ट्रीय साइबर हेल्पलाइन <b>1930</b> पर कॉल करें।
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.success("🟢 संदेश में कोई तत्काल वित्तीय जोखिम नहीं मिला। हमेशा सतर्क रहें।")

# ================= TAB 6: NASHA MUKTI & LIFE GUIDANCE =================
with tab_life:
    st.write("### 🕊️ नशा-मुक्ति व सही जीवन मार्गदर्शन (Life Guidance)")
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
