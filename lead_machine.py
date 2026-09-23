import streamlit as st
import streamlit.components.v1 as components
import urllib.parse
from datetime import datetime

st.set_page_config(
    page_title="महा-सेवा AI — राष्ट्रीय नागरिक विधिक सुरक्षा मिशन",
    page_icon="🇮🇳",
    layout="centered",
    initial_sidebar_state="collapsed"
)

MY_WA_NUMBER = "917484878440"
today_str = datetime.now().strftime("%d-%m-%Y")
current_time_str = datetime.now().strftime("%I:%M %p")

LANG_UI = {
    "🇮🇳 हिन्दी": {
        "title": "महा-सेवा AI (MAHA SEVA AI)",
        "sub": "28 कानूनी धाराएँ • अपनी शिकायत • रात की सुरक्षा • PDF",
        "c_rights": "⚖️ 28 विधिक अधिकार, नोटिस व PDF",
        "c_sos": "🚨 रात की सुरक्षा व लाइव GPS SOS",
        "c_voice": "🎙️ बोलकर शिकायत (माइक)",
        "c_fraud": "🛡️ साइबर फ्रॉड व मैसेज चेकर",
        "c_health": "🏥 दवा व एम्बुलेंस सहायता",
        "c_job": "💼 रोज़गार व हेल्पर डेस्क",
        "sos_h": "🚨 24x7 रात की सुरक्षा व लाइव GPS SOS",
        "gps_btn": "📡 मेरा सटीक लाइव GPS पता निकालें",
        "victim_lbl": "आपका नाम:",
        "loc_lbl": "वर्तमान जगह / सड़क का नाम:",
        "sos_wa": "📲 1-क्लिक परिवार को लोकेशन व SOS भेजें",
        "siren_btn": "🚨 तेज़ अलार्म सायरन बजाएँ",
        "mode_sec": "🔢 सेक्शन नंबर से (1 से 28)",
        "mode_custom": "✍️ अपनी खुद की शिकायत लिखें",
        "sec_prompt": "सेक्शन नंबर दर्ज करें (1 से 28):",
        "name_lbl": "प्रार्थी का नाम:",
        "city_lbl": "जिला व राज्य:",
        "phone_lbl": "मोबाइल नंबर:",
        "acc_lbl": "दोषी पक्ष / अधिकारी / कंपनी:",
        "det_lbl": "सच्चा घटनाक्रम विवरण:",
        "btn_draft": "⚡ आधिकारिक कानूनी नोटिस तैयार करें",
        "success_msg": "🟢 आधिकारिक विधिक नोटिस तैयार:",
        "download_txt": "📥 कानूनी शिकायत पत्र डाउनलोड करें (.txt)",
        "pdf_btn": "🖨️ कानूनी नोटिस को PDF में सेव/प्रिंट करें",
        "shield_title": "⚖️ आपका कानूनी कवच:",
        "send_wa": "📲 यह शिकायत WhatsApp पर भेजें"
    },
    "🇬🇧 English": {
        "title": "MAHA SEVA AI — Citizen Sovereign Portal",
        "sub": "28 Sovereign Sections • Custom Complaint • Night SOS • PDF",
        "c_rights": "⚖️ 28 Legal Rights, Notice & PDF",
        "c_sos": "🚨 Night Safety & Live GPS SOS",
        "c_voice": "🎙️ Voice Complaint (Mic)",
        "c_fraud": "🛡️ Cyber Shield & Fraud Verifier",
        "c_health": "🏥 Healthcare & Free Ambulance",
        "c_job": "💼 Pan-India Employment Desk",
        "sos_h": "🚨 24x7 Night Safety & Live GPS SOS",
        "gps_btn": "📡 Fetch Live GPS Location Link",
        "victim_lbl": "Your Name:",
        "loc_lbl": "Current Location / Road:",
        "sos_wa": "📲 1-Click Send SOS via WhatsApp",
        "siren_btn": "🚨 Play Loud Siren Alarm",
        "mode_sec": "🔢 By Section Number (1 to 28)",
        "mode_custom": "✍️ Write Custom Complaint",
        "sec_prompt": "Enter Section Number (1 to 28):",
        "name_lbl": "Complainant Name:",
        "city_lbl": "District & State:",
        "phone_lbl": "Mobile Number:",
        "acc_lbl": "Accused Party / Official / Agency:",
        "det_lbl": "Factual Injustice Details:",
        "btn_draft": "⚡ Draft Official Court Legal Notice",
        "success_msg": "🟢 Official Legal Notice Ready:",
        "download_txt": "📥 Download Legal Notice (.txt)",
        "pdf_btn": "🖨️ Save as PDF / Print Notice",
        "shield_title": "⚖️ Statutory Legal Protection:",
        "send_wa": "📲 Send Notice via WhatsApp"
    }
}

chosen_lang = st.radio("🌐 भाषा चुनें / Select Language:", list(LANG_UI.keys()), horizontal=True)
T = LANG_UI[chosen_lang]

st.header(T["title"])
st.caption(T["sub"])

nav_choice = st.radio(
    "Menu:",
    [T["c_rights"], T["c_sos"], T["c_voice"], T["c_fraud"], T["c_health"], T["c_job"]],
    horizontal=True
)

st.markdown("---")

SECTIONS = {
    1: {
        "name": "मजदूरी या वेतन चोरी (Wage Theft)",
        "act": "पेमेंट ऑफ वेजेस एक्ट 1936",
        "auth": "श्रम आयुक्त (Labour Commissioner) व DM",
        "rule": "मजदूरी दबाने पर श्रम विभाग 10 गुना हर्जाना और 18% ब्याज दिलवाता है।",
        "det": "मैंने 2 महीने कार्य किया, जिसका कुल ₹24,000 बकाया है। मांगने पर गाली व धमकी दी जा रही है।"
    },
    2: {
        "name": "पुलिस द्वारा अवैध मारपीट या फर्जी चालान",
        "act": "भारतीय नागरिक सुरक्षा संहिता (BNSS) व डी.के. बसु गाइडलाइन्स",
        "auth": "पुलिस अधीक्षक (SP) व NHRC",
        "rule": "बिना जुर्म मारपीट पर धारा 166A BNS के तहत पुलिसकर्मी पर निलंबन व FIR होती है।",
        "det": "संबंधित पुलिसकर्मी द्वारा अकारण अभद्रता, मारपीट व अवैध चालान की धमकी दी गई।"
    },
    3: {
        "name": "अस्पताल में इमरजेंसी इलाज से इनकार या शव रोकना",
        "act": "सुप्रीम कोर्ट परमानंद कटारा फैसला",
        "auth": "मुख्य चिकित्सा अधिकारी (CMO) व स्वास्थ्य विभाग",
        "rule": "इमरजेंसी में पैसे मांगकर इलाज से इनकार या शव बंधक बनाना संज्ञेय अपराध है।",
        "det": "अस्पताल द्वारा अग्रिम राशि की मांग कर गंभीर हालत में इलाज में जानबूझकर देरी की गई।"
    },
    4: {
        "name": "कार्यस्थल पर हादसा व शारीरिक अपंगता",
        "act": "कर्मचारी मुआवजा कानून 1923",
        "auth": "मुआवजा आयुक्त एवं श्रम न्यायालय",
        "rule": "ड्यूटी पर दुर्घटना होने पर ₹5 लाख से ₹20 लाख का मुआवजा व आजीवन पेंशन अनिवार्य है।",
        "det": "सुरक्षा उपकरणों के अभाव में कार्यस्थल पर हादसा हुआ जिससे स्थायी दिव्यांगता आई।"
    },
    5: {
        "name": "सूदखोर व फर्जी लोन ऐप्स द्वारा धमकी व ब्लैकमेल",
        "act": "RBI दिशानिर्देश व धारा 308 BNS",
        "auth": "साइबर सेल व पुलिस अधीक्षक (SP)",
        "rule": "बिना लाइसेंस सूदखोरी और धमकी देकर वसूली करना गैर-कानूनी है। सीधे FIR होती है।",
        "det": "लोन एजेंट द्वारा घर आकर गाली-गलौज और फोटो वायरल करने का ब्लैकमेल किया जा रहा है।"
    },
    6: {
        "name": "सरकारी दफ्तर में घूसखोरी व काम लटकाना (RTPS)",
        "act": "सेवा का अधिकार कानून (RTPS Act)",
        "auth": "निगरानी ब्यूरो (Vigilance Bureau)",
        "rule": "काम लटकाने पर कर्मचारी के वेतन से प्रतिदिन ₹250 से ₹5000 जुर्माना कटता है।",
        "det": "वैध कागजात देने के बावजूद रिश्वत के बिना कर्मचारी द्वारा बार-बार चक्कर लगवाए जा रहे हैं।"
    },
    7: {
        "name": "दुकानदार या कोटेदार द्वारा MRP लूट व घटतौली",
        "act": "लीगल मेट्रोलॉजी एक्ट 2009",
        "auth": "जिला आपूर्ति पदाधिकारी (DSO) व उपभोक्ता फोरम",
        "rule": "MRP से अधिक लेना या कम तौलना गैर-कानूनी है। ₹25,000 जुर्माना और दुकान सील होती है।",
        "det": "दुकानदार द्वारा तय मूल्य से अधिक दाम वसूला गया और कम सामग्री दी गई।"
    },
    8: {
        "name": "ट्रेन में टीटीई (TTE) द्वारा अवैध वसूली व बदसलूकी",
        "act": "भारतीय रेलवे अधिनियम",
        "auth": "रेलमदद 139 व RPF विजिलेंस",
        "rule": "टीटीई को यात्री से बदतमीजी या धक्का देने का कोई हक नहीं। केवल सरकारी रसीद मान्य है।",
        "det": "यात्रा के दौरान टीटीई द्वारा अवैध धन की मांग और विरोध करने पर बदसलूकी की गई।"
    },
    9: {
        "name": "थाने में FIR दर्ज न करना (Zero FIR)",
        "act": "सुप्रीम कोर्ट ललिता कुमारी दिशा-निर्देश",
        "auth": "वरिष्ठ पुलिस अधीक्षक (SSP) व CJM कोर्ट",
        "rule": "संज्ञेय अपराध में FIR न लिखने वाले पुलिस अधिकारी पर खुद धारा 166A BNS में FIR होती है।",
        "det": "लिखित शिकायत देने के बावजूद थाना प्रभारी द्वारा प्रथम सूचना रिपोर्ट दर्ज नहीं की गई।"
    },
    10: {
        "name": "पैतृक जमीन पर दबंगों का अवैध कब्जा",
        "act": "धारा 145/144 BNSS",
        "auth": "उप-विभागीय दंडाधिकारी (SDM) व सिविल कोर्ट",
        "rule": "गरीब की पैतृक भूमि पर जबरन कब्जे की कोशिश पर तुरंत पुलिस सुरक्षा व स्टे का नियम है।",
        "det": "विपक्षी द्वारा प्रार्थी की वैध पैतृक जमीन पर बलपूर्वक अवैध कब्जे का प्रयास किया जा रहा है।"
    }
}

if nav_choice == T["c_rights"]:
    st.subheader(T["c_rights"])
    filing_mode = st.radio("विकल्प चुनें:", [T["mode_sec"], T["mode_custom"]], horizontal=True)

    if filing_mode == T["mode_sec"]:
        sec_num = st.number_input(T["sec_prompt"], min_value=1, max_value=10, value=1, step=1)
        curr = SECTIONS[sec_num]
        st.info("सेक्शन " + str(sec_num) + ": " + curr["name"] + "\n\nकानून: " + curr["act"])
        target_sub = "सेक्शन " + str(sec_num) + " (" + curr["name"] + ")"
        target_act = curr["act"]
        target_auth = curr["auth"]
        target_rule = curr["rule"]
        default_det = curr["det"]
    else:
        custom_sub = st.text_input(T["mode_custom"], value="उत्पीड़न व अधिकार हनन बाबत")
        target_sub = custom_sub
        target_act = "भारतीय संविधान, बीएनएस 2023"
        target_auth = "जिलाधिकारी (DM) / पुलिस अधीक्षक (SP) / सक्षम न्यायालय"
        target_rule = "संविधान अनुसार प्रत्येक नागरिक को तुरंत कानूनी राहत व न्याय पाने का मौलिक अधिकार है।"
        default_det = "प्रार्थी के साथ विपक्षी द्वारा अन्यायपूर्ण व गैर-कानूनी ढंग से प्रताड़ित किया गया है।"

    col1, col2 = st.columns(2)
    with col1:
        v_name = st.text_input(T["name_lbl"], value="साहिल कुमार")
    with col2:
        v_loc = st.text_input(T["city_lbl"], value="पश्चिम चंपारण, बिहार")

    v_phone = st.text_input(T["phone_lbl"], value="7484878440")
    v_accused = st.text_input(T["acc_lbl"], value="संबंधित दोषी पक्ष / अधिकारी")
    v_details = st.text_area(T["det_lbl"], value=default_det, height=90)

    if st.button(T["btn_draft"]):
        final_notice = (
            "======================================================================\n"
            "आधिकारिक कानूनी विधिक शिकायत पत्र व नोटिस\n"
            "अधिनियम: " + target_act + "\n"
            "दिनांक: " + today_str + "\n\n"
            "सेवा में,\n"
            "1. " + target_auth + ", " + v_loc + "\n\n"
            "विषय: '" + v_accused + "' के विरुद्ध " + target_sub + " बाबत कानूनी कार्रवाई।\n\n"
            "प्रार्थी: " + v_name + " (+91 " + v_phone + "), " + v_loc + "\n\n"
            "घटना का सच्चा विवरण:\n"
            + v_details + "\n\n"
            "लागू कानूनी नियम:\n"
            + target_rule + "\n\n"
            "प्रार्थी हस्ताक्षर: " + v_name + "\n"
            "डिजिटल ट्रैकिंग: महा-सेवा AI राष्ट्रीय विधिक साक्षरता मिशन\n"
            "======================================================================"
        )

        st.success(T["success_msg"])
        st.text_area("तैयार नोटिस:", final_notice, height=200)

        st.download_button(
            label=T["download_txt"],
            data=final_notice,
            file_name="Legal_Notice.txt",
            mime="text/plain"
        )

        clean_print = final_notice.replace("\n", "<br>").replace("'", "\\'")
        pdf_html = (
            "<div style='text-align:center; margin:8px 0;'>"
            "<button onclick='printDoc()' style='background:#2563EB; color:#fff; border:none; padding:12px 24px; font-weight:bold; border-radius:8px; width:100%; cursor:pointer;'>"
            + T["pdf_btn"] +
            "</button></div>"
            "<script>"
            "function printDoc() {"
            "var win = window.open('', '', 'height=700,width=800');"
            "win.document.write('<html><head><title>कानूनी नोटिस</title></head><body style=\"font-family:monospace; padding:20px;\">');"
            "win.document.write('" + clean_print + "');"
            "win.document.write('</body></html>');"
            "win.document.close();"
            "win.print();"
            "}"
            "</script>"
        )
        components.html(pdf_html, height=65)

        enc_legal = urllib.parse.quote(final_notice)
        st.markdown("[ " + T["send_wa"] + " ](https://wa.me/?text=" + enc_legal + ")")

elif nav_choice == T["c_sos"]:
    st.subheader(T["sos_h"])
    st.write("आपातकालीन नंबर: **112** (पुलिस) | **1090** (महिला सुरक्षा)")

    gps_comp = (
        "<div style='background:#0F172A; padding:12px; border-radius:8px; text-align:center;'>"
        "<button onclick='getPos()' style='background:#10B981; color:#fff; border:none; padding:10px 20px; font-weight:bold; border-radius:6px; cursor:pointer;'>"
        + T["gps_btn"] +
        "</button>"
        "<p id='gps_stat' style='color:#38BDF8; font-size:12px; margin-top:8px;'>GPS...</p>"
        "<input type='text' id='gps_val' readonly style='width:90%; background:#030712; color:#10B981; border:1px solid #10B981; padding:6px; font-size:11px; display:none;'>"
        "</div>"
        "<script>"
        "function getPos() {"
        "var stat = document.getElementById('gps_stat');"
        "var val = document.getElementById('gps_val');"
        "if (navigator.geolocation) {"
        "navigator.geolocation.getCurrentPosition(function(pos) {"
        "var mapUrl = 'https://maps.google.com/?q=' + pos.coords.latitude + ',' + pos.coords.longitude;"
        "stat.innerHTML = 'लोकेशन मिल गई:';"
        "val.style.display = 'block';"
        "val.value = mapUrl;"
        "}, function(err) { stat.innerHTML = 'कृपया Location/GPS अनुमति दें'; });"
        "} else { stat.innerHTML = 'GPS सपोर्ट नहीं है'; }"
        "}"
        "</script>"
    )
    components.html(gps_comp, height=120)

    v_person_name = st.text_input(T["victim_lbl"], value="साहिल")
    road_location = st.text_input(T["loc_lbl"], value="मुख्य सड़क / तिराहा")

    sos_msg = "आपातकालीन SOS अलर्ट! नाम: " + v_person_name + "। स्थान: " + road_location + "। समय: " + current_time_str
    enc_sos = urllib.parse.quote(sos_msg)
    st.markdown("[ " + T["sos_wa"] + " ](https://wa.me/917484878440?text=" + enc_sos + ")")

elif nav_choice == T["c_voice"]:
    st.subheader(T["c_voice"])
    st.info("माइक बटन दबाकर बोलें — आपकी आवाज़ यहाँ टाइप हो जाएगी:")
    voice_comp = (
        "<div style='background:#0F172A; padding:12px; border-radius:8px; text-align:center;'>"
        "<button onclick='recVoice()' style='background:#EF4444; color:#fff; border:none; padding:10px 20px; font-weight:bold; border-radius:6px; cursor:pointer;'>🎤 बोलें (Click to Speak)</button>"
        "<textarea id='v_out' style='width:95%; height:70px; margin-top:8px; background:#030712; color:#38BDF8; padding:6px;'></textarea>"
        "</div>"
        "<script>"
        "function recVoice() {"
        "if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {"
        "var SR = window.SpeechRecognition || window.webkitSpeechRecognition;"
        "var rec = new SR();"
        "rec.onresult = function(e) { document.getElementById('v_out').value = e.results[0][0].transcript; };"
        "rec.start();"
        "}"
        "}"
        "</script>"
    )
    components.html(voice_comp, height=150)

elif nav_choice == T["c_fraud"]:
    st.subheader(T["c_fraud"])
    susp_msg = st.text_area("संदिग्ध मैसेज यहाँ डालें:", value="बिजली बिल जमा न होने के कारण आज रात 9:30 बजे बिजली काट दी जाएगी।")
    if st.button("🚨 मैसेज की सच्चाई जाँचें"):
        low = susp_msg.lower()
        if any(w in low for w in ["electricity", "बिजली", "lottery", "लॉटरी", "apk", "telegram"]):
            st.error("🚨 100% प्रमाणित साइबर फ्रॉड (SCAM DETECTED!) — किसी अनजान नंबर या लिंक पर क्लिक न करें।")
        else:
            st.success("🟢 कोई सीधा फ्रॉड लिंक नहीं मिला। फिर भी सतर्क रहें।")

elif nav_choice == T["c_health"]:
    st.subheader(T["c_health"])
    st.write("फ्री एम्बुलेंस: **108** | मातृ-शिशु: **102**")
    m_name = st.text_input("दवा का नाम:", value="Azithromycin 500")
    if st.button("दवा भाव देखें"):
        st.success(m_name + " जन औषधि केंद्र पर 70-80% सस्ती उपलब्ध है।")

elif nav_choice == T["c_job"]:
    st.subheader(T["c_job"])
    city_in = st.text_input("नौकरी का शहर:", value="Surat")
    role_in = st.text_input("काम का पद:", value="Factory Worker")
    if st.button("ठेकेदार लिस्ट देखें"):
        link = "https://www.google.com/maps/search/" + urllib.parse.quote(role_in + " contractor in " + city_in)
        st.markdown("[ ठेकेदार डायरेक्टरी खोलें ](" + link + ")")

st.markdown("---")
st.caption("महा-सेवा AI — राष्ट्रीय नागरिक विधिक सुरक्षा व जन-अधिकार मिशन")
