import streamlit as st
import streamlit.components.v1 as components
import urllib.parse
from datetime import datetime
import pandas as pd
import os

st.set_page_config(page_title="महा-सेवा AI", page_icon="🇮🇳", layout="centered", initial_sidebar_state="collapsed")

WA_NUM = "917484878440"
today = datetime.now().strftime("%d-%m-%Y")
t_now = datetime.now().strftime("%I:%M %p")
DB_NAME = "maha_seva_data.csv"

def save_entry(c_type, name, phone, city, details):
    row = {"Date": today, "Time": t_now, "Type": c_type, "Name": name, "Phone": str(phone), "City": city, "Details": details}
    df = pd.DataFrame([row])
    if not os.path.exists(DB_NAME):
        df.to_csv(DB_NAME, index=False)
    else:
        df.to_csv(DB_NAME, mode='a', header=False, index=False)

LANGS = ["🇮🇳 हिन्दी", "🇬🇧 English"]
c_lang = st.radio("🌐 भाषा / Language:", LANGS, horizontal=True)
is_en = (c_lang == "🇬🇧 English")

if is_en:
    UI = {
        "title": "MAHA SEVA AI — Citizen & Worker Sovereign Portal",
        "sub": "Legal Notices • Factory Accident Claim • Artisan Desk • Medicine Desk • SOS",
        "menu": ["⚖️ Legal Notice", "🏭 Factory Injury Claim", "🛠️ Artisan Desk", "🍲 Food Rescue", "💊 Medicine Checker", "🌙 Direct Aid", "🚨 Night SOS", "🎙️ Voice Help"],
        "sec_h": "⚖️ Statutory Legal Notice Generator",
        "sec_prompt": "Select Section (1 to 10):",
        "name_lbl": "Name:", "city_lbl": "District & State:", "phone_lbl": "Mobile:",
        "acc_lbl": "Accused / Company:", "det_lbl": "Details:", "btn_draft": "⚡ Draft Court Legal Notice",
        "notice_success": "🟢 Legal Notice Drafted & Data Saved:",
        "dl_txt": "📥 Download Notice (.txt)", "pdf_btn": "🖨️ Print / Save PDF",
        "inj_title": "🏭 Factory Accident & Compensation Claim (Employees Compensation Act)",
        "inj_company": "Factory / Company Name & Address:",
        "inj_post": "Job Designation (Operator / Welder / Helper):",
        "inj_date": "Accident Date & Time:",
        "inj_body": "Nature of Injury (Hand Fracture / Disability):",
        "inj_evidence": "Evidence (CCTV / Doctor MLC / Colleagues / Punch Card):",
        "inj_btn": "⚡ Generate Compensation Legal Notice",
        "k_title": "🛠️ Artisan Desk (Welder, Plumber, Electrician)",
        "k_name": "Artisan Name:", "k_work": "Trade:", "k_city": "City:",
        "k_save": "✅ Register Artisan", "k_success": "Saved directly to Founder Database!",
        "l_title": "🍲 Food Rescue & Langar Service",
        "l_desc": "Surplus Food Details (30 food packets):", "l_loc": "Location / Hall:",
        "l_btn": "📢 Broadcast Food Alert",
        "m_title": "💊 Medicine & Generic Price Checker",
        "m_input": "Enter Medicine or Disease:", "m_btn": "🔍 Check Medicine Info",
        "aid_title": "🌙 Direct Aid (Zakat & Tool Support)",
        "sos_h": "🚨 24x7 Night Safety & Live GPS SOS",
        "gps_btn": "📡 Fetch Live GPS Location Link",
        "voice_h": "🎙️ Voice Complaint (Mic)"
    }
else:
    UI = {
        "title": "महा-सेवा AI (MAHA SEVA AI)",
        "sub": "अखंड भारत जन-कल्याण • फैक्ट्री हादसा व मुआवजा दावा • 28 कानूनी धाराएँ • कारीगर मंच • SOS",
        "menu": ["⚖️ 28 कानूनी नोटिस", "🏭 फैक्ट्री हादसा व मुआवजा दावा", "🛠️ कारीगर मंच", "🍲 लंगर व अन्न सेवा", "💊 दवा व जेनेरिक भाव", "🌙 सीधी मदद", "🚨 रात की सुरक्षा SOS", "🎙️ बोलकर शिकायत"],
        "sec_h": "⚖️ कानूनी नोटिस जनरेटर",
        "sec_prompt": "धारा संख्या चुनें (1 से 10):",
        "name_lbl": "प्रार्थी का नाम:", "city_lbl": "जिला व राज्य:", "phone_lbl": "मोबाइल नंबर:",
        "acc_lbl": "दोषी पक्ष / अधिकारी का नाम:", "det_lbl": "घटनाक्रम विवरण:", "btn_draft": "⚡ कानूनी नोटिस तैयार करें",
        "notice_success": "🟢 विधिक नोटिस तैयार और डेटाबेस में सुरक्षित:",
        "dl_txt": "📥 नोटिस डाउनलोड करें (.txt)", "pdf_btn": "🖨️ PDF प्रिंट / सेव करें",
        "inj_title": "🏭 कंपनी/फैक्ट्री में चोट व कानूनी मुआवजा क्लेम (Employees Compensation Act)",
        "inj_company": "कंपनी / फैक्ट्री का नाम व पता:",
        "inj_post": "पद / कार्य विभाग (ऑपरेटर / वेल्डर / हेल्पर):",
        "inj_date": "हादसे की तारीख व समय:",
        "inj_body": "चोट / अंग क्षति का विवरण (हाथ फ्रैक्चर / उंगली कटना):",
        "inj_evidence": "मौजूद सबूत (CCTV फुटेज / डॉक्टर MLC पर्ची / साथी मजदूर गवाह / गेट पास):",
        "inj_btn": "⚡ सरकारी मुआवजा व कानूनी नोटिस तैयार करें",
        "k_title": "🛠️ हुनरमंद साथी — कारीगर मंच (वेल्डर/प्लंबर/इलेक्ट्रीशियन)",
        "k_name": "कारीगर का नाम:", "k_work": "काम का प्रकार:", "k_city": "शहर / कस्बा:",
        "k_save": "✅ नाम सुरक्षित सेव करें", "k_success": "बधाई! आपका नाम सीधे संस्थापक के डेटाबेस में दर्ज हो गया है।",
        "l_title": "🍲 लंगर, दस्तरख्वान व बचा खाना सेवा",
        "l_desc": "खाने का विवरण (उदा: 30 पैकेट पूड़ी-सब्जी):", "l_loc": "होटल / शादी हॉल / जगह:",
        "l_btn": "📢 अन्न-सेवा अलर्ट जारी करें",
        "m_title": "💊 दवा जानकारी व जन औषधि सस्ता भाव",
        "m_input": "दवा या बीमारी का नाम लिखें:", "m_btn": "🔍 दवा की जानकारी व भाव देखें",
        "aid_title": "🌙 बरकत, जकात व सीधी औजार मदद",
        "sos_h": "🚨 24x7 रात की सुरक्षा व लाइव GPS SOS",
        "gps_btn": "📡 लाइव GPS निकालें",
        "voice_h": "🎙️ बोलकर शिकायत दर्ज करें"
    }

st.title(UI["title"])
st.caption(UI["sub"])

choice = st.radio("Menu:", UI["menu"], horizontal=True)
st.markdown("---")

SECTIONS_DATA = {
    1: ("मजदूरी या वेतन चोरी (Wage Theft)", "Payment of Wages Act 1936", "Labour Commissioner & DM", "मजदूरी दबाना गैर-कानूनी है; 10 गुना हर्जाना और 18% ब्याज मिलता है।", "2 महीने का वेतन बकाया है, मांगने पर धमकी दी जा रही है।"),
    2: ("पुलिस अवैध मारपीट या फर्जी चालान", "BNSS 2023 & DK Basu Guidelines", "SP & NHRC", "अवैध मारपीट पर धारा 166A BNS के तहत पुलिसकर्मी पर FIR व निलंबन होता है।", "संबंधित पुलिसकर्मी द्वारा अकारण अभद्रता व चालान की धमकी दी गई।"),
    3: ("अस्पताल में इमरजेंसी इलाज इनकार", "Supreme Court Parmanand Katara Verdict", "CMO & Health Dept", "इमरजेंसी में पैसे के लिए इलाज से इनकार या शव रोकना संज्ञेय अपराध है।", "अस्पताल द्वारा अग्रिम राशि मांगकर इलाज में जानबूझकर देरी की गई।"),
    4: ("कार्यस्थल पर हादसा व मुआवजा", "Employees Compensation Act 1923", "Compensation Commissioner", "हादसा होने पर ₹5 से ₹20 लाख मुआवजा व आजीवन पेंशन अनिवार्य है।", "ड्यूटी के दौरान सुरक्षा उपकरण न होने से गंभीर चोट लगी।"),
    5: ("लोन ऐप ब्लैकमेल व सूदखोरी", "RBI Guidelines & Sec 308 BNS", "Cyber Cell & SP", "बिना लाइसेंस सूदखोरी और धमकी देकर वसूली करना गैर-कानूनी है।", "रिकवरी एजेंट द्वारा घर आकर गाली-गलौज व फोटो से ब्लैकमेल किया जा रहा है।"),
    6: ("सरकारी दफ्तर घूसखोरी (RTPS)", "Right to Public Services Act", "Vigilance Bureau", "काम लटकाने पर कर्मचारी के वेतन से प्रतिदिन ₹250-5000 जुर्माना कटता है।", "कागजात पूरे होने पर भी रिश्वत के बिना काम नहीं किया जा रहा।"),
    7: ("दुकानदार MRP लूट व घटतौली", "Legal Metrology Act 2009", "DSO & Consumer Court", "MRP से अधिक लेना या कम तौलना गैर-कानूनी है, दुकान सील होती है।", "तय मूल्य से अधिक दाम वसूला गया और कम सामग्री दी गई।"),
    8: ("रेलवे TTE अवैध वसूली", "Indian Railway Act", "RailMadad 139 & RPF", "TTE को बदसलूकी करने या ट्रेन से धक्का देने का अधिकार नहीं है।", "यात्रा के दौरान नियम विरुद्ध पैसों की मांग व बदसलूकी की गई।"),
    9: ("थाने में FIR दर्ज न करना", "Supreme Court Lalita Kumari Directives", "SSP & CJM Court", "FIR न लिखने वाले अधिकारी पर धारा 166A BNS में खुद मुकदमा होता है।", "लिखित शिकायत देने पर भी पुलिस द्वारा FIR दर्ज नहीं की गई।"),
    10: ("पैतृक जमीन पर अवैध कब्जा", "Section 145/144 BNSS", "SDM & Civil Court", "गरीब की भूमि पर कब्जे की कोशिश पर तुरंत पुलिस सुरक्षा व स्टे का नियम है।", "विपक्षी द्वारा वैध पैतृक जमीन पर जबरन कब्जे का प्रयास हो रहा है।")
}

# 1. LEGAL NOTICE
if choice == UI["menu"][0]:
    st.subheader(UI["sec_h"])
    sec_num = st.number_input(UI["sec_prompt"], min_value=1, max_value=10, value=1)
    s_name, s_act, s_auth, s_rule, s_det = SECTIONS_DATA[sec_num]
    st.info(f"📌 {s_name}\n\nAct: {s_act} | Auth: {s_auth}")
    
    c1, c2 = st.columns(2)
    v_name = c1.text_input(UI["name_lbl"], value="साहिल कुमार")
    v_city = c2.text_input(UI["city_lbl"], value="पश्चिम चंपारण, बिहार")
    v_phone = st.text_input(UI["phone_lbl"], value="7484878440")
    v_acc = st.text_input(UI["acc_lbl"], value="संबंधित दोषी पक्ष")
    v_desc = st.text_area(UI["det_lbl"], value=s_det, height=80)
    
    if st.button(UI["btn_draft"]):
        save_entry("Legal Notice", v_name, v_phone, v_city, f"Accused: {v_acc} | Subject: {s_name}")
        notice = (
            "======================================================================\n"
            "OFFICIAL LEGAL NOTICE & STATUTORY COMPLAINT\n"
            f"Act: {s_act} | Date: {today}\n\n"
            f"To: {s_auth}, {v_city}\n"
            f"Subject: Legal action against '{v_acc}' regarding {s_name}\n\n"
            f"Complainant: {v_name} (+91 {v_phone}), {v_city}\n"
            f"Factual Summary: {v_desc}\n\n"
            f"Legal Protection: {s_rule}\n\n"
            f"Signature: {v_name}\n"
            "Maha Seva AI Sovereign Mission\n"
            "======================================================================"
        )
        st.success(UI["notice_success"])
        st.text_area("Notice:", notice, height=180)
        st.download_button(UI["dl_txt"], notice, file_name="Notice.txt")
        
        c_print = notice.replace("\n", "<br>").replace("'", "\\'")
        p_html = f"<div style='text-align:center;'><button onclick='pDoc()' style='background:#2563EB;color:#fff;padding:10px 20px;border:none;border-radius:6px;cursor:pointer;font-weight:bold;'>{UI['pdf_btn']}</button></div><script>function pDoc(){{var w=window.open('','','width=800,height=700');w.document.write('<html><body style=\"font-family:monospace;padding:20px;\">{c_print}</body></html>');w.document.close();w.print();}}</script>"
        components.html(p_html, height=50)
        st.markdown(f"[📲 Send via WhatsApp](https://wa.me/?text={urllib.parse.quote(notice)})")

# 2. FACTORY ACCIDENT & COMPENSATION CLAIM
elif choice == UI["menu"][1]:
    st.subheader(UI["inj_title"])
    st.info("Employees' Compensation Act 1923: Duty par chot lagne par 100% cashless ilaj, chhutti ki salary aur ₹3 se ₹20 lakh compensation 30 din me milna kanooni haq hai.")

    c1, c2 = st.columns(2)
    w_name = c1.text_input("Worker / Aggrieved Name:", value="साहिल कुमार")
    w_city = c2.text_input("District & State:", value="पश्चिम चंपारण, बिहार")
    w_phone = st.text_input("Mobile Number:", value="7484878440")
    w_company = st.text_input(UI["inj_company"], value="ABC Manufacturing Pvt. Ltd.")
    w_post = st.text_input(UI["inj_post"], value="मशीन ऑपरेटर / हेल्पर")
    w_time = st.text_input(UI["inj_date"], value=f"{today}, सुबह 11:30 बजे")
    w_injury = st.text_area(UI["inj_body"], value="मशीन में गार्ड न होने से दाहिने हाथ में गंभीर चोट व फ्रैक्चर।")
    w_evid = st.text_area(UI["inj_evidence"], value="अस्पताल MLC पर्ची, ड्यूटी गेट पास, सीसीटीवी फुटेज और साथी मजदूर की गवाही।")

    if st.button(UI["inj_btn"]):
        save_entry("Accident Claim", w_name, w_phone, w_city, f"Company: {w_company} | Injury: {w_injury}")
        claim_notice = (
            "======================================================================\n"
            "STATUTORY WORKPLACE INJURY & COMPENSATION DEMAND NOTICE\n"
            "(Under Section 10, Employees' Compensation Act, 1923 & ESI Act)\n"
            f"Date: {today}\n\n"
            f"To:\n1. Factory Management / MD, {w_company}\n"
            f"2. Compensation Commissioner / Labour Court, {w_city}\n\n"
            f"Subject: Immediate Cashless Treatment & Statutory Compensation for {w_name}\n\n"
            f"I, {w_name} (+91 {w_phone}), working as '{w_post}' at {w_company}, state:\n"
            f"1. OCCURRENCE: On {w_time}, sustained injury on duty: {w_injury}\n"
            f"2. EVIDENCE ON RECORD: {w_evid}\n"
            "3. DEMAND: Provide 100% cashless treatment, full leave salary and deposit statutory compensation under Section 4 with 12% interest within 30 days.\n\n"
            f"Signature: {w_name}\n"
            "======================================================================"
        )
        st.success("🟢 क्लेम नोटिस तैयार व डेटाबेस में सुरक्षित:")
        st.text_area("Claim Notice:", claim_notice, height=180)
        st.download_button("📥 Download Claim (.txt)", claim_notice, file_name="Accident_Claim.txt")
        c_cl = claim_notice.replace("\n", "<br>").replace("'", "\\'")
        cp_html = f"<div style='text-align:center;'><button onclick='pDoc()' style='background:#2563EB;color:#fff;padding:10px 20px;border:none;border-radius:6px;cursor:pointer;font-weight:bold;'>{UI['pdf_btn']}</button></div><script>function pDoc(){{var w=window.open('','','width=800,height=700');w.document.write('<html><body style=\"font-family:monospace;padding:20px;\">{c_cl}</body></html>');w.document.close();w.print();}}</script>"
        components.html(cp_html, height=50)
        st.markdown(f"[📲 Send Claim via WhatsApp](https://wa.me/?text={urllib.parse.quote(claim_notice)})")

# 3. KARIGAR
elif choice == UI["menu"][2]:
    st.subheader(UI["k_title"])
    st.write("• **अकबर अली** — वेल्डर | 📍 पश्चिम चंपारण | [📞 कॉल](tel:9876543210)\n• **राकेश शर्मा** — इलेक्ट्रीशियन | 📍 पश्चिम चंपारण | [📞 कॉल](tel:9876543211)\n• **मोहम्मद सलीम** — प्लंबर | 📍 पश्चिम चंपारण | [📞 कॉल](tel:9876543212)")
    st.markdown("---")
    k_name = st.text_input(UI["k_name"])
    k_work = st.selectbox(UI["k_work"], ["वेल्डर (Welder)", "प्लंबर (Plumber)", "इलेक्ट्रीशियन (Electrician)", "राजमिस्त्री (Mason)", "बढ़ई (Carpenter)"])
    k_phone = st.text_input("Phone Number:")
    k_city = st.text_input(UI["k_city"], value="पश्चिम चंपारण")
    if st.button(UI["k_save"]):
        if k_name and k_phone:
            save_entry("Karigar", k_name, k_phone, k_city, k_work)
            st.success(UI["k_success"])
        else:
            st.error("Name & Phone required!")

# 4. FOOD RESCUE
elif choice == UI["menu"][3]:
    st.subheader(UI["l_title"])
    l_food = st.text_input(UI["l_desc"])
    l_place = st.text_input(UI["l_loc"], value="मेन मार्केट")
    l_phone = st.text_input("Phone:", value="7484878440")
    if st.button(UI["l_btn"]):
        save_entry("Food Rescue", "Organizer", l_phone, l_place, l_food)
        msg = f"अन्न-सेवा! खाना: {l_food} उपलब्ध है। स्थान: {l_place}। फोन: +91 {l_phone}"
        st.success("Food Alert Registered!")
        st.markdown(f"[📲 Share on WhatsApp](https://wa.me/?text={urllib.parse.quote(msg)})")

# 5. MEDICINE & GENERIC CHECKER
elif choice == UI["menu"][4]:
    st.subheader(UI["m_title"])
    st.write("📞 **108** (मुफ्त एम्बुलेंस) | **102** (मातृ-शिशु एम्बुलेंस)")
    med_q = st.text_input(UI["m_input"], value="Azithromycin 500")
    if st.button(UI["m_btn"]):
        q_low = med_q.lower()
        if "paracetamol" in q_low or "बुखार" in q_low:
            info = "बुखार व दर्द निवारक दवा (Paracetamol)। जन औषधि पर मात्र ₹10-15 (बाजार में ₹30-40)।"
        elif "azithromycin" in q_low or "infection" in q_low:
            info = "एंटीबायोटिक दवा। जन औषधि भाव मात्र ₹25-35 (प्राइवेट में ₹120-150)।"
        elif "pantoprazole" in q_low or "गैस" in q_low:
            info = "गैस व एसिडिटी निवारक। जन औषधि भाव मात्र ₹15-20 (बाजार में ₹80-100)।"
        else:
            info = f"{med_q} का जेनेरिक साल्ट जन औषधि केंद्र पर 70% से 80% सस्ते भाव में उपलब्ध है।"
        st.success(info)

# 6. DIRECT AID
elif choice == UI["menu"][5]:
    st.subheader(UI["aid_title"])
    d_type = st.selectbox("Type:", ["कारीगर को औजार दिलाना", "गरीब परिवार को राशन", "दवा व इलाज सहायता"])
    d_amt = st.text_input("Amount (₹):", value="1000")
    d_phone = st.text_input("Phone:", value="7484878440")
    if st.button("🤝 Register Pledge"):
        save_entry("Aid Pledge", "Donor", d_phone, "Local", f"{d_type} | ₹{d_amt}")
        st.success("Pledge saved in Founder Database.")

# 7. NIGHT SAFETY SOS
elif choice == UI["menu"][6]:
    st.subheader(UI["sos_h"])
    st.write("Emergency: **112** (Police) | **1090** (Women Helpline)")
    g_html = f"<div style='text-align:center;'><button onclick='fPos()' style='background:#10B981;color:#fff;padding:10px;border:none;border-radius:6px;font-weight:bold;cursor:pointer;'>{UI['gps_btn']}</button><p id='g_res' style='color:#38BDF8;font-size:12px;'></p></div><script>function fPos(){{navigator.geolocation.getCurrentPosition(function(p){{document.getElementById('g_res').innerHTML='https://maps.google.com/?q='+p.coords.latitude+','+p.coords.longitude;}});}}</script>"
    components.html(g_html, height=75)
    u_name = st.text_input("Name:", value="साहिल")
    u_road = st.text_input("Road:", value="मेन रोड")
    sos_txt = f"EMERGENCY SOS! Name: {u_name}. Location: {u_road}. Time: {t_now}."
    st.markdown(f"[📲 Send WhatsApp SOS](https://wa.me/{WA_NUM}?text={urllib.parse.quote(sos_txt)})")

# 8. VOICE
elif choice == UI["menu"][7]:
    st.subheader(UI["voice_h"])
    v_html = "<div style='text-align:center;'><button onclick='rVoice()' style='background:#EF4444;color:#fff;padding:8px 16px;border:none;border-radius:6px;cursor:pointer;'>🎤 Speak</button><br><textarea id='v_box' style='width:95%;height:70px;margin-top:8px;'></textarea></div><script>function rVoice(){var R=window.SpeechRecognition||window.webkitSpeechRecognition;var r=new R();r.onresult=function(e){document.getElementById('v_box').value=e.results[0][0].transcript;};r.start();}</script>"
    components.html(v_html, height=130)

# ADMIN PANEL
st.markdown("---")
with st.expander("🔐 संस्थापक गुप्त एडमिन पैनल (केवल साहिल अहमद के लिए)"):
    adm_pass = st.text_input("पासवर्ड डालें:", type="password")
    if adm_pass == "sahil786":
        st.success("🟢 स्वागत है साहिल भाई! आपका डेटाबेस सक्रिय है:")
        if os.path.exists(DB_NAME):
            df_view = pd.read_csv(DB_NAME)
            st.dataframe(df_view, use_container_width=True)
            st.download_button("📥 संपूर्ण एक्सेल डेटाबेस डाउनलोड करें", df_view.to_csv(index=False).encode('utf-8'), file_name="Maha_Seva_Master.csv", mime="text/csv")
        else:
            st.info("डेटाबेस अभी खाली है।")
    elif adm_pass:
        st.error("गलत पासवर्ड!")

st.markdown("---")
st.write("🏛️ **संस्थापक:** साहिल अहमद (Sahil Ahmad) • महा-सेवा AI")
st.markdown(f"[💬 संस्थापक WhatsApp संपर्क (+91 7484878440)](https://wa.me/{WA_NUM})")
