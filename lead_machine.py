import streamlit as st
import streamlit.components.v1 as components
import urllib.parse
from datetime import datetime

st.set_page_config(
    page_title="महा-सेवा AI — अखंड भारत जन-कल्याण व सुरक्षा मिशन",
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
        "sub": "अखंड भारत जन-कल्याण • कारीगर रोज़गार • लंगर सेवा • 28 कानूनी धाराएँ • SOS",
        "c_rights": "⚖️ 28 कानूनी धाराएँ व नोटिस",
        "c_karigar": "🛠️ कारीगर मंच (वेल्डर/प्लंबर/इलेक्ट्रीशियन)",
        "c_langar": "🍲 लंगर, दस्तरख्वान व बचा खाना",
        "c_barkat": "🌙 बरकत व सीधी मदद (जकात/औजार)",
        "c_sos": "🚨 रात की सुरक्षा व लाइव GPS SOS",
        "c_voice": "🎙️ बोलकर शिकायत (माइक)",
        "c_fraud": "🛡️ साइबर फ्रॉड व मैसेज चेकर",
        "sos_h": "🚨 24x7 रात की सुरक्षा व लाइव GPS SOS",
        "gps_btn": "📡 मेरा सटीक लाइव GPS पता निकालें",
        "victim_lbl": "पीड़ित / आपका नाम:",
        "loc_lbl": "वर्तमान सड़क / चौराहे का नाम:",
        "sos_wa": "📲 1-क्लिक परिवार को लोकेशन व SOS भेजें",
        "siren_btn": "🚨 तेज़ अलार्म सायरन बजाएँ",
        "mode_sec": "🔢 धारा नंबर से (1 से 28)",
        "mode_custom": "✍️ अपनी खुद की शिकायत लिखें",
        "sec_prompt": "धारा नंबर दर्ज करें (1 से 28):",
        "name_lbl": "प्रार्थी का नाम:",
        "city_lbl": "जिला व राज्य:",
        "phone_lbl": "मोबाइल नंबर:",
        "acc_lbl": "दोषी पक्ष / अधिकारी / ठेकेदार:",
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
        "sub": "Citizen Welfare • Artisan Jobs • Food Rescue • 28 Legal Rights • SOS",
        "c_rights": "⚖️ 28 Legal Rights & Notice",
        "c_karigar": "🛠️ Artisan Desk (Welder/Plumber/Electrician)",
        "c_langar": "🍲 Free Food & Surplus Rescue",
        "c_barkat": "🌙 Direct Aid (Tools & Assistance)",
        "c_sos": "🚨 Night Safety & Live GPS SOS",
        "c_voice": "🎙️ Voice Complaint (Mic)",
        "c_fraud": "🛡️ Cyber Shield & Fraud Verifier",
        "sos_h": "🚨 24x7 Night Safety & Live GPS SOS",
        "gps_btn": "📡 Fetch Live GPS Location Link",
        "victim_lbl": "Victim / Your Name:",
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

chosen_lang = st.radio("🌐 भाषा / Language:", list(LANG_UI.keys()), horizontal=True)
T = LANG_UI[chosen_lang]

st.header(T["title"])
st.caption(T["sub"])

nav_choice = st.radio(
    "Menu:",
    [
        T["c_rights"],
        T["c_karigar"],
        T["c_langar"],
        T["c_barkat"],
        T["c_sos"],
        T["c_voice"],
        T["c_fraud"]
    ],
    horizontal=True
)

st.markdown("---")

SECTIONS = {
    1: {"name": "मजदूरी या वेतन चोरी (Wage Theft)", "act": "Payment of Wages Act 1936", "auth": "Labour Commissioner & DM", "rule": "मजदूरी दबाना गैर-कानूनी है; 10 गुना हर्जाना और 18% ब्याज मिलता है।", "det": "2 महीने की मजदूरी बाकी है। मांगने पर गाली-गलौज और धमकी दी जा रही है।"},
    2: {"name": "पुलिस अवैध मारपीट या फर्जी चालान", "act": "BNSS 2023 & DK Basu Directives", "auth": "SP & NHRC", "rule": "अवैध मारपीट करने पर धारा 166A BNS के तहत पुलिसकर्मी पर निलंबन व FIR होती है।", "det": "संबंधित पुलिसकर्मी द्वारा अकारण अभद्रता, मारपीट व अवैध चालान की धमकी दी गई।"},
    3: {"name": "अस्पताल में इमरजेंसी इलाज से इनकार या शव रोकना", "act": "Supreme Court Parmanand Katara Verdict", "auth": "CMO & Health Dept", "rule": "इमरजेंसी में पैसे मांगकर इलाज से इनकार या शव रोकना गैर-कानूनी संज्ञेय अपराध है।", "det": "अस्पताल द्वारा अग्रिम राशि की मांग कर गंभीर हालत में इलाज में जानबूझकर देरी की गई।"},
    4: {"name": "कार्यस्थल पर हादसा व शारीरिक अपंगता", "act": "Employees Compensation Act 1923", "auth": "Compensation Commissioner", "rule": "हादसा होने पर मालिक को ₹5 लाख से ₹20 लाख का मुआवजा और आजीवन पेंशन देना अनिवार्य है।", "det": "सुरक्षा उपकरणों के अभाव में कार्यस्थल पर हादसा हुआ जिससे स्थायी दिव्यांगता आई।"},
    5: {"name": "सूदखोर व फर्जी लोन ऐप्स द्वारा धमकी व ब्लैकमेल", "act": "RBI Fair Rules & Sec 308 BNS", "auth": "Cyber Cell & SP", "rule": "बिना लाइसेंस सूदखोरी और धमकी देकर वसूली करना गैर-कानूनी है। सीधे FIR होती है।", "det": "लोन एजेंट द्वारा घर आकर गाली-गलौज और फोटो वायरल करने का ब्लैकमेल किया जा रहा है।"},
    6: {"name": "सरकारी दफ्तर में घूसखोरी व काम लटकाना (RTPS)", "act": "Right to Public Services Act", "auth": "Vigilance Bureau", "rule": "काम लटकाने पर कर्मचारी के वेतन से प्रतिदिन ₹250 से ₹5000 जुर्माना कटता है।", "det": "वैध कागजात देने के बावजूद रिश्वत के बिना कर्मचारी द्वारा बार-बार चक्कर लगवाए जा रहे हैं।"},
    7: {"name": "दुकानदार या कोटेदार द्वारा MRP लूट व घटतौली", "act": "Legal Metrology Act 2009", "auth": "DSO & Consumer Affairs", "rule": "MRP से अधिक लेना या कम तौलना गैर-कानूनी है। ₹25,000 जुर्माना और दुकान सील होती है।", "det": "दुकानदार द्वारा तय मूल्य से अधिक दाम वसूला गया और कम सामग्री दी गई।"},
    8: {"name": "ट्रेन में टीटीई (TTE) द्वारा अवैध वसूली व बदसलूकी", "act": "Indian Railway Act", "auth": "RailMadad 139 & RPF", "rule": "टीटीई को यात्री से बदतमीजी या धक्का देने का कोई हक नहीं। केवल सरकारी रसीद मान्य है।", "det": "यात्रा के दौरान टीटीई द्वारा अवैध धन की मांग और विरोध करने पर बदसलूकी की गई।"},
    9: {"name": "थाने में FIR दर्ज न करना (Zero FIR)", "act": "Supreme Court Lalita Kumari Guidelines", "auth": "SSP & CJM Court", "rule": "संज्ञेय अपराध में FIR न लिखने वाले पुलिस अधिकारी पर खुद धारा 166A BNS में FIR होती है।", "det": "लिखित शिकायत देने के बावजूद थाना प्रभारी द्वारा प्रथम सूचना रिपोर्ट दर्ज नहीं की गई।"},
    10: {"name": "पैतृक जमीन पर दबंगों का अवैध कब्जा", "act": "Section 145/144 BNSS", "auth": "SDM & Civil Court", "rule": "गरीब की जमीन पर जबरन कब्जे की कोशिश पर तुरंत पुलिस सुरक्षा व स्टे का नियम है।", "det": "विपक्षी द्वारा प्रार्थी की वैध पैतृक जमीन पर बलपूर्वक अवैध कब्जे का प्रयास किया जा रहा है।"}
}

# ================= TAB 1: 28 LEGAL RIGHTS =================
if nav_choice == T["c_rights"]:
    st.subheader(T["c_rights"])
    filing_mode = st.radio("विकल्प चुनें:", [T["mode_sec"], T["mode_custom"]], horizontal=True)

    if filing_mode == T["mode_sec"]:
        sec_num = st.number_input(T["sec_prompt"], min_value=1, max_value=10, value=1, step=1)
        curr = SECTIONS[sec_num]
        st.info(f"धारा {sec_num}: {curr['name']}\n\nकानून: {curr['act']}")
        target_sub = f"धारा {sec_num} ({curr['name']})"
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
            f"अधिनियम: {target_act}\n"
            f"दिनांक: {today_str}\n\n"
            "सेवा में,\n"
            f"1. {target_auth}, {v_loc}\n\n"
            f"विषय: '{v_accused}' के विरुद्ध {target_sub} बाबत कानूनी कार्रवाई।\n\n"
            f"प्रार्थी: {v_name} (+91 {v_phone}), {v_loc}\n\n"
            "घटना का सच्चा विवरण:\n"
            f"{v_details}\n\n"
            "लागू कानूनी नियम:\n"
            f"{target_rule}\n\n"
            f"प्रार्थी हस्ताक्षर: {v_name}\n"
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
            f"{T['pdf_btn']}"
            "</button></div>"
            "<script>"
            "function printDoc() {"
            "var win = window.open('', '', 'height=700,width=800');"
            "win.document.write('<html><head><title>कानूनी नोटिस</title></head><body style=\"font-family:monospace; padding:20px;\">');"
            f"win.document.write('{clean_print}');"
            "win.document.write('</body></html>');"
            "win.document.close();"
            "win.print();"
            "}"
            "</script>"
        )
        components.html(pdf_html, height=65)

        enc_legal = urllib.parse.quote(final_notice)
        st.markdown(f"[{T['send_wa']}](https://wa.me/?text={enc_legal})")

# ================= TAB 2: KARIGAR DIRECTORY =================
elif nav_choice == T["c_karigar"]:
    st.subheader("🛠️ हुनरमंद साथी — कारीगर डायरेक्टरी (Zero Middleman)")
    st.caption("वेल्डर, प्लंबर, इलेक्ट्रीशियन, राजमिस्त्री भाई सीधे जुड़ें — बिना किसी ठेकेदार के 100% कमाई आपकी:")

    k_tab1, k_tab2 = st.tabs(["🔍 कारीगर खोजें व कॉल करें", "📝 नया कारीगर जोड़ें"])

    with k_tab1:
        st.write("### 📞 स्थानीय कारीगर सूची:")
        SAMPLE_KARIGAR = [
            {"name": "अकबर अली", "skill": "वेल्डर (Welder - गेट/ग्रिल)", "city": "पश्चिम चंपारण", "phone": "9876543210"},
            {"name": "राकेश शर्मा", "skill": "इलेक्ट्रीशियन (Electrician - वायरिंग/मोटर)", "city": "पश्चिम चंपारण", "phone": "9876543211"},
            {"name": "मोहम्मद सलीम", "skill": "प्लंबर (Plumber - फिटिंग/पाइप)", "city": "पश्चिम चंपारण", "phone": "9876543212"},
            {"name": "दिनेश मांझी", "skill": "राजमिस्त्री (Mason - निर्माण कार्य)", "city": "पश्चिम चंपारण", "phone": "9876543213"}
        ]
        for k in SAMPLE_KARIGAR:
            st.markdown(f"""
            <div style="background:#0F172A; border:1px solid #0284C7; padding:10px; border-radius:10px; margin-bottom:8px;">
                <b>👤 {k['name']}</b> — <span style="color:#38BDF8;">{k['skill']}</span><br>
                📍 {k['city']} | 📞 <a href="tel:{k['phone']}" style="color:#10B981; font-weight:bold;">{k['phone']} पर सीधे कॉल करें</a>
            </div>
            """, unsafe_allow_html=True)

    with k_tab2:
        st.write("### अपना नाम दर्ज करें:")
        k_name = st.text_input("कारीगर का नाम:")
        k_skill = st.selectbox("आपका काम:", ["वेल्डर (Welder)", "प्लंबर (Plumber)", "इलेक्ट्रीशियन (Electrician)", "राजमिस्त्री (Mason)", "बढ़ई (Carpenter)"])
        k_phone = st.text_input("मोबाइल नंबर:")
        k_city = st.text_input("शहर / कस्बा:", value="पश्चिम चंपारण")
        if st.button("✅ डायरेक्टरी में नाम शामिल करें"):
            karigar_wa = f"नमस्ते, मैं {k_name} ({k_skill}) हूँ। मेरा शहर {k_city} है और मोबाइल +91 {k_phone} है। मुझे डायरेक्टरी में जोड़ें।"
            enc_k = urllib.parse.quote(karigar_wa)
            st.success("विवरण तैयार है! नीचे क्लिक करके एडमिन को भेजें:")
            st.markdown(f"[📲 एडमिन को लिस्टिंग भेजें](https://wa.me/{MY_WA_NUMBER}?text={enc_k})")

# ================= TAB 3: LANGAR & FOOD RESCUE =================
elif nav_choice == T["c_langar"]:
    st.subheader("🍲 लंगर, दस्तरख्वान व बचा खाना सेवा (Zero Hunger)")
    st.caption("कोई भी इंसान भूखा न सोए और किसी भी शादी या दुकान का खाना बर्बाद न हो:")

    l_type = st.radio("आप क्या साझा करना चाहते हैं?", ["🍱 शादी/होटल/दुकान का बचा हुआ ताजा खाना", "📍 फ्री लंगर/भंडारा/दस्तरख्वान की जगह"])
    l_food_details = st.text_input("खाने का विवरण (उदा: 30 पैकेट पूड़ी-सब्जी या 15 प्लेट खाना):")
    l_location = st.text_input("सटीक पता / होटल या जगह का नाम:", value="मेन मार्केट तिराहा")
    l_contact = st.text_input("संपर्क नंबर:", value="7484878440")

    if st.button("📢 तुरंत सेवा अलर्ट जारी करें"):
        langar_alert = f"अन्न-सेवा अलर्ट! विवरण: {l_food_details}। स्थान: {l_location}। संपर्क: +91 {l_contact}। समय: {current_time_str}। कृपया खाना तुरंत जरूरतमंदों तक पहुँचाएँ।"
        enc_la = urllib.parse.quote(langar_alert)
        st.success("अन्न-सेवा संदेश तैयार:")
        st.markdown(f"[📲 सेवा टीमों व WhatsApp ग्रुप में शेयर करें](https://wa.me/?text={enc_la})")

# ================= TAB 4: BARKAT & DIRECT AID =================
elif nav_choice == T["c_barkat"]:
    st.subheader("🌙 बरकत, जकात व सीधी औजार मदद (Direct Support)")
    st.caption("बिना किसी बिचौलिए के सीधे जरूरतमंद मजदूर या बेवा बहन तक मदद पहुँचाना:")

    st.markdown("""
    * **🛠️ औजार बैंक (Tool Bank):** गरीब वेल्डर, प्लंबर या इलेक्ट्रीशियन को काम शुरू करने के लिए टूलकिट या वेल्डिंग मशीन दिलाना।
    * **🌾 सीधा राशन पैक:** किसी गरीब परिवार या बेवा बहन के लिए सीधे पास के किराना स्टोर पर 1 महीने का राशन बुक कराना।
    * **🤲 100% पारदर्शी व्यवस्था:** दान देने वाला सीधे दुकानदार या मिस्त्री को भुगतान करता है; कोई तीसरा व्यक्ति बीच में नहीं आता।
    """)

    donor_type = st.selectbox("आप किस प्रकार की मदद करना चाहते हैं?", ["मजदूर/कारीगर को औजार दिलाना", "राशन किट उपलब्ध कराना", "दवा व इलाज सहायता"])
    donor_amount = st.text_input("अनुमानित सहायता राशि (₹):", value="1000")
    donor_city = st.text_input("आपका शहर:", value="पश्चिम चंपारण")

    if st.button("🤝 स्थानीय जरूरतमंद से संपर्क करें"):
        aid_txt = f"सदाक़ह/मदद संकल्प: मैं {donor_city} में '{donor_type}' हेतु ₹{donor_amount} की सीधी मदद करना चाहता हूँ। कृपया सत्यापित जरूरतमंद से जोड़ें।"
        enc_aid = urllib.parse.quote(aid_txt)
        st.markdown(f"[📲 एडमिन से जुड़कर सीधी मदद करें](https://wa.me/{MY_WA_NUMBER}?text={enc_aid})")

# ================= TAB 5: NIGHT SAFETY & SOS =================
elif nav_choice == T["c_sos"]:
    st.subheader(T["sos_h"])
    st.write("आपातकालीन नंबर: **112** (पुलिस) | **1090** (महिला सुरक्षा) | **181** (संकट हेल्पलाइन)")

    gps_comp = (
        "<div style='background:#0F172A; padding:12px; border-radius:8px; text-align:center;'>"
        "<button onclick='getPos()' style='background:#10B981; color:#fff; border:none; padding:10px 20px; font-weight:bold; border-radius:6px; cursor:pointer;'>"
        f"{T['gps_btn']}"
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

    sos_msg = f"आपातकालीन SOS अलर्ट! नाम: {v_person_name}। स्थान: {road_location}। समय: {current_time_str}। तुरंत संपर्क करें।"
    enc_sos = urllib.parse.quote(sos_msg)
    st.markdown(f"[{T['sos_wa']}](https://wa.me/{MY_WA_NUMBER}?text={enc_sos})")

    st.write("### 🔊 पैनिक सायरन (हमलावर को भगाने हेतु)")
    siren_html = (
        "<div style='text-align:center; margin:6px 0;'>"
        "<button onclick='playAlarm()' style='background:#EF4444; color:#fff; padding:12px 24px; border-radius:10px; border:none; font-weight:800; font-size:15px; cursor:pointer;'>"
        f"{T['siren_btn']}"
        "</button></div>"
        "<script>"
        "function playAlarm() {"
        "var ctx = new (window.AudioContext || window.webkitAudioContext)();"
        "var osc = ctx.createOscillator();"
        "var gain = ctx.createGain();"
        "osc.type = 'sawtooth';"
        "osc.frequency.setValueAtTime(800, ctx.currentTime);"
        "osc.frequency.linearRampToValueAtTime(1400, ctx.currentTime + 0.3);"
        "osc.frequency.linearRampToValueAtTime(800, ctx.currentTime + 0.6);"
        "gain.gain.setValueAtTime(1, ctx.currentTime);"
        "osc.connect(gain);"
        "gain.connect(ctx.destination);"
        "osc.start();"
        "osc.stop(ctx.currentTime + 3);"
        "}"
        "</script>"
    )
    components.html(siren_html, height=65)

# ================= TAB 6: VOICE COMPLAINT =================
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

# ================= TAB 7: CYBER FRAUD =================
elif nav_choice == T["c_fraud"]:
    st.subheader(T["c_fraud"])
    susp_msg = st.text_area("संदिग्ध मैसेज यहाँ डालें:", value="बिजली बिल जमा न होने के कारण आज रात 9:30 ब
