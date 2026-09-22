import streamlit as st
import streamlit.components.v1 as components
import urllib.parse
import urllib.request
import json
from datetime import datetime

# 1. Page Configuration
st.set_page_config(
    page_title="महा-सेवा AI — अखंड राष्ट्रीय नागरिक, रोज़गार व विधिक सुरक्षा मिशन",
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

# Multi-Language UI Definitions
UI_LANGUAGES = {
    "🇮🇳 हिन्दी": {
        "title": "महा-सेवा AI (MAHA SEVA AI)",
        "sub": "जन-अधिकार • पुलिस-ठेकेदार लीगल एक्शन • रोज़गार • दवा व एम्बुलेंस • सरकारी योजना",
        "tab_rights": "⚖️ जन-अधिकार व शिकायत",
        "tab_health": "🏥 दवा व एम्बुलेंस",
        "tab_job": "💼 रोज़गार व हेल्पर",
        "tab_scheme": "🏛️ सरकारी योजना",
        "tab_fraud": "🛡️ साइबर सुरक्षा",
        "tab_life": "🕊️ नशा-मुक्ति",
        "rights_title": "⚖️ ठेकेदार, मजदूरी व पुलिस उत्पीड़न के विरुद्ध सीधी कार्रवाई",
        "btn_rights": "⚡ आधिकारिक कानूनी नोटिस व FIR प्रारूप ड्राफ्ट करें"
    },
    "🇬🇧 English": {
        "title": "MAHA SEVA AI — Sovereign Mission",
        "sub": "Citizen Rights • Legal Action Against Unlawful Police/Employer • Jobs • Healthcare",
        "tab_rights": "⚖️ Legal Rights & Action",
        "tab_health": "🏥 Health & Ambulance",
        "tab_job": "💼 Jobs & Helpers",
        "tab_scheme": "🏛️ Welfare Schemes",
        "tab_fraud": "🛡️ Cyber Shield",
        "tab_life": "🕊️ Anti-Addiction",
        "rights_title": "⚖️ Direct Legal Action Against Wage Theft & Police Misconduct",
        "btn_rights": "⚡ Draft Official Legal Notice & Investigation Complaint"
    },
    "বাংলা (Bengali)": {
        "title": "মহা-সেবা AI (MAHA SEVA AI)",
        "sub": "নাগরিক অধিকার • আইনি পদক্ষেপ • কর্মসংস্থান • স্বাস্থ্য ও অ্যাম্বুলেন্স",
        "tab_rights": "⚖️ নাগরিক অধিকার",
        "tab_health": "🏥 ঔষধ ও অ্যাম্বুলেন্স",
        "tab_job": "💼 কর্মসংস্থান",
        "tab_scheme": "🏛️ সরকারি প্রকল্প",
        "tab_fraud": "🛡️ প্রতারণা রোধ",
        "tab_life": "🕊️ নেশামুক্তি",
        "rights_title": "⚖️ বেতন চুরি ও পুলিশি হয়রানির বিরুদ্ধে সরাসরি অভিযোগ",
        "btn_rights": "⚡ আইনি অভিযোগ পত্র তৈরি করুন"
    },
    "मराठी (Marathi)": {
        "title": "महा-सेवा AI (MAHA SEVA AI)",
        "sub": "नागरी हक्क • पोलीस व कंत्राटदार तक्रार निवारण • रोजगार • औषधे",
        "tab_rights": "⚖️ नागरी हक्क व तक्रार",
        "tab_health": "🏥 औषधे व रुग्णवाहिका",
        "tab_job": "💼 रोजगार व मदतनीस",
        "tab_scheme": "🏛️ सरकारी योजना",
        "tab_fraud": "🛡️ सायबर सुरक्षा",
        "tab_life": "🕊️ व्यसनमुक्ती",
        "rights_title": "⚖️ थकीत मजुरी व पोलिसांच्या गैरवर्तनाविरुद्ध थेट कारवाई",
        "btn_rights": "⚡ कायदेशीर नोटीस व तक्रार अर्ज तयार करा"
    },
    "தமிழ் (Tamil)": {
        "title": "மகா-சேவா AI (MAHA SEVA AI)",
        "sub": "குடிமக்கள் உரிமைகள் • சட்ட நடவடிக்கை • வேலைவாய்ப்பு • மருத்துவம்",
        "tab_rights": "⚖️ சட்ட உரிமை & புகார்",
        "tab_health": "🏥 மருத்துவம் & ஆம்புலன்ஸ்",
        "tab_job": "💼 வேலைவாய்ப்பு",
        "tab_scheme": "🏛️ அரசு திட்டங்கள்",
        "tab_fraud": "🛡️ இணைய பாதுகாப்பு",
        "tab_life": "🕊️ போதை ஒழிப்பு",
        "rights_title": "⚖️ கூலி மறுப்பு மற்றும் காவல்துறை அத்துமீறலுக்கு எதிரான நேரடி நடவடிக்கை",
        "btn_rights": "⚡ சட்டப்பூர்வ புகார் மனுவை உருவாக்கவும்"
    }
}

# Universal Knowledge Fetcher
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

# Language Selector
chosen_lang = st.radio(
    "🌐 भाषा चुनें / Select Language / ভাষা বাছুন / भाषा निवडा / மொழியைத் தேர்ந்தெடுக்கவும்:",
    ["🇮🇳 हिन्दी", "🇬🇧 English", "বাংলা (Bengali)", "मराठी (Marathi)", "தமிழ் (Tamil)"],
    horizontal=True
)
L = UI_LANGUAGES.get(chosen_lang, UI_LANGUAGES["🇮🇳 हिन्दी"])

# Header
st.markdown(f"""
<div style="background: radial-gradient(circle at center, #1E3A8A 0%, #030712 100%); border: 2px solid #38BDF8; border-radius: 14px; padding: 14px; text-align: center; margin-bottom: 14px; box-shadow: 0 0 20px rgba(56, 189, 248, 0.25);">
    <span style="background:rgba(16,185,129,0.2); color:#10B981; border:1px solid #10B981; padding:3px 12px; border-radius:20px; font-size:11px; font-weight:800;">
        ⚡ 24x7 अखंड भारत नागरिक, विधिक सुरक्षा व रोज़गार मिशन
    </span>
    <h1 style="font-size:22px; margin:6px 0 0 0; color:#FFF;">{L['title']}</h1>
    <p style="font-size:12px; color:#38BDF8; margin:4px 0 0 0;">{L['sub']}</p>
</div>
""", unsafe_allow_html=True)

# 6 Tabs
tab_rights, tab_health, tab_job, tab_scheme, tab_fraud, tab_life = st.tabs([
    L['tab_rights'],
    L['tab_health'],
    L['tab_job'],
    L['tab_scheme'],
    L['tab_fraud'],
    L['tab_life']
])

# ================= TAB 1: CITIZEN LEGAL RIGHTS & COMPLAINTS =================
with tab_rights:
    st.write(f"### {L['rights_title']}")
    st.caption("यदि ठेकेदार मजदूरी दबाए, कंपनी पैसा न दे, या पुलिसकर्मी बिना जुर्म मारपीट/अवैध वसूली/फर्जी चालान करे — विधिक नोटिस जनरेट करें")

    complaint_type = st.radio(
        "📌 शिकायत की गंभीर श्रेणी चुनें:",
        [
            "ठेकेदार / कंपनी द्वारा मजदूरी व वेतन का गबन (Payment of Wages Act)",
            "पुलिस द्वारा गैर-कानूनी मारपीट, गाली-गलौज व मानसिक प्रताड़ना (Police Misconduct)",
            "यातायात पुलिस / अधिकारी द्वारा अवैध या फर्जी चालान (Illegal Challan)",
            "सरकारी कर्मचारी / राशन डीलर द्वारा रिश्वत की मांग (Corruption & Bribery)"
        ]
    )

    col_c1, col_c2 = st.columns(2)
    with col_c1:
        victim_name = st.text_input("पीड़ित / प्रार्थी का नाम:", value="साहिल कुमार")
    with col_c2:
        victim_city = st.text_input("जिला व राज्य:", value="पश्चिम चंपारण, बिहार")

    victim_phone = st.text_input("पीड़ित का मोबाइल नंबर:", value="7484878440")
    accused_party = st.text_input("दोषी ठेकेदार / कंपनी / पुलिस अधिकारी व थाना:", value="ठेकेदार राम सिंह / संबंधित थाना प्रभारी व बीट अधिकारी")
    complaint_details = st.text_area(
        "घटना का विस्तृत विवरण (तारीख, स्थान, बकाया राशि व हुआ अन्याय):",
        value="मैंने संबंधित कार्यस्थल पर 2 महीने पूरी मेहनत से कार्य किया, जिसकी कुल बकाया राशि ₹24,000 है। मांगने पर ठेकेदार द्वारा जातिसूचक अपशब्द, गाली-गलौज व जान से मारने की धमकी दी गई।"
    )

    if st.button(L['btn_rights']):
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

        st.success("🟢 100% आधिकारिक विधिक नोटिस तैयार:")
        st.text_area("📄 तैयार विधिक शिकायत पत्र (Official Legal Notice):", legal_draft, height=220)

        st.markdown("""
        <div class="caution-card">
            <h3 style="color:#EF4444; margin:0 0 6px 0;">⚖️ आपका कानूनी कवच (कोई भी अधिकारी या ठेकेदार कानून से ऊपर नहीं है):</h3>
            <ul style="margin:0; padding-left:18px; font-size:14px; color:#FCA5A5;">
                <li><b>मजदूरी का पाई-पाई हिसाब:</b> यदि ठेकेदार पैसा रोके, तो श्रम अदालत में शिकायत जाने पर कंपनी का खाता सीज हो सकता है।</li>
                <li><b>पुलिस बर्बरता पर सजा:</b> सुप्रीम कोर्ट (डी.के. बसु बनाम पश्चिम बंगाल) के निर्देशानुसार किसी भी नागरिक के साथ थाने में या सड़क पर गाली-गलौज व मारपीट करने वाले पुलिसकर्मी पर सीधे मुकदमा और नौकरी से बर्खास्तगी की कार्रवाई होती है।</li>
                <li><b>गलत चालान:</b> यदि पुलिस ने बिना गलती चालान काटा है, तो उसे ऑनलाइन ई-कोर्ट (Virtual Court) में चुनौती दें, जज के सामने पुलिसकर्मी को प्रमाण देना होता है।</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="text-align:center; margin:10px 0;">
            <p style="color:#38BDF8; font-size:13px; margin-bottom:6px;"><b>सीधे राष्ट्रीय न्याय एवं सतर्कता हेल्पलाइन पर कॉल करें (Toll-Free):</b></p>
            <a href="tel:112" class="btn-red-call">📞 112 राष्ट्रीय पुलिस हेल्पलाइन</a>
            <a href="tel:1064" class="btn-red-call">📞 1064 एंटी-करप्शन / घूसखोरी विरोधी</a>
            <a href="tel:14434" class="btn-red-call">📞 14434 श्रम व वेतन समाधान हेल्पलाइन</a>
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
                <h3 style="color:#EF4444; margin:0 0 6px 0;">⚠️ दवा के उपयोग में अनिवार्य सावधानी:</h3>
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

       
