import streamlit as st
import streamlit.components.v1 as components
import urllib.parse
from datetime import datetime
import pandas as pd
import os

st.set_page_config(
    page_title="महा-सेवा AI",
    page_icon="🇮🇳",
    layout="centered",
    initial_sidebar_state="collapsed"
)

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

LANGS = ["🇮🇳 हिन्दी", "🇬🇧 English", "বাংলা (Bengali)", "मराठी (Marathi)"]
c_lang = st.radio("🌐 भाषा / Select Language:", LANGS, horizontal=True)

is_en = "English" in c_lang

st.title("🇮🇳 महा-सेवा AI (MAHA SEVA AI)")
st.caption("अखंड भारत जन-कल्याण • 28 कानूनी अधिकार • कारीगर रोजगार • लंगर सेवा • SOS")

tabs = ["⚖️ 28 कानूनी नोटिस", "🛠️ कारीगर मंच", "🍲 लंगर व अन्न सेवा", "🌙 सीधी मदद", "🚨 रात की सुरक्षा SOS", "🎙️ बोलकर शिकायत"]
choice = st.radio("सेवा चुनें:", tabs, horizontal=True)
st.markdown("---")

SECTIONS_DATA = {
    1: ("मजदूरी या वेतन चोरी", "Payment of Wages Act 1936", "Labour Commissioner & DM", "मजदूरी दबाना गैर-कानूनी है; 10 गुना हर्जाना और 18% ब्याज मिलता है।", "2 महीने का वेतन बकाया है, मांगने पर धमकी दी जा रही है।"),
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

# 1. LEGAL RIGHTS
if choice == "⚖️ 28 कानूनी नोटिस":
    st.subheader("⚖️ कानूनी नोटिस जनरेटर")
    sec_num = st.number_input("धारा संख्या चुनें (1 से 10):", min_value=1, max_value=10, value=1)
    s_name, s_act, s_auth, s_rule, s_det = SECTIONS_DATA[sec_num]
    
    st.info("📌 विषय: " + s_name + "\n\nलागू कानून: " + s_act + " | सक्षम अधिकारी: " + s_auth)
    
    c1, c2 = st.columns(2)
    v_name = c1.text_input("प्रार्थी का नाम:", value="साहिल कुमार")
    v_city = c2.text_input("जिला व राज्य:", value="पश्चिम चंपारण, बिहार")
    v_phone = st.text_input("मोबाइल नंबर:", value="7484878440")
    v_acc = st.text_input("दोषी पक्ष / अधिकारी का नाम:", value="संबंधित दोषी पक्ष")
    v_desc = st.text_area("घटनाक्रम विवरण:", value=s_det, height=80)
    
    if st.button("⚡ कानूनी नोटिस तैयार करें"):
        save_entry("कानूनी नोटिस", v_name, v_phone, v_city, "दोषी: " + v_acc + " | विषय: " + s_name)
        notice = (
            "======================================================================\n"
            "आधिकारिक कानूनी विधिक शिकायत पत्र व नोटिस\n"
            "अधिनियम: " + s_act + " | दिनांक: " + today + "\n\n"
            "सेवा में: " + s_auth + ", " + v_city + "\n"
            "विषय: '" + v_acc + "' के विरुद्ध कानूनी कार्रवाई बाबत (" + s_name + ")\n\n"
            "प्रार्थी: " + v_name + " (+91 " + v_phone + "), निवासी: " + v_city + "\n"
            "घटना विवरण: " + v_desc + "\n\n"
            "कानूनी आधार: " + s_rule + "\n\n"
            "हस्ताक्षर: " + v_name + "\n"
            "महा-सेवा AI राष्ट्रीय विधिक साक्षरता मिशन\n"
            "======================================================================"
        )
        st.success("🟢 विधिक नोटिस तैयार और डेटाबेस में सुरक्षित:")
        st.text_area("नोटिस कॉपी करें:", notice, height=180)
        st.download_button("📥 नोटिस डाउनलोड करें (.txt)", notice, file_name="Notice.txt")
        
        c_print = notice.replace("\n", "<br>").replace("'", "\\'")
        p_html = "<div style='text-align:center;'><button onclick='pDoc()' style='background:#2563EB;color:#fff;padding:10px 20px;border:none;border-radius:6px;cursor:pointer;font-weight:bold;'>🖨️ PDF प्रिंट / सेव करें</button></div><script>function pDoc(){var w=window.open('','','width=800,height=700');w.document.write('<html><body style=\"font-family:monospace;padding:20px;\">'+'" + c_print + "'+'</body></html>');w.document.close();w.print();}</script>"
        components.html(p_html, height=50)
        
        q_text = urllib.parse.quote(notice)
        st.markdown("[📲 यह नोटिस WhatsApp पर भेजें](https://wa.me/?text=" + q_text + ")")

# 2. KARIGAR
elif choice == "🛠️ कारीगर मंच":
    st.subheader("🛠️ हुनरमंद साथी — कारीगर मंच")
    st.caption("वेल्डर, प्लंबर, इलेक्ट्रीशियन, राजमिस्त्री भाई सीधे जुड़ें — बिना किसी दलाल के 100% कमाई आपकी:")
    
    st.write("### 📞 स्थानीय कारीगर सूची:")
    st.markdown("• **अकबर अली** — वेल्डर (गेट/ग्रिल) | 📍 पश्चिम चंपारण | [📞 कॉल करें](tel:9876543210)\n• **राकेश शर्मा** — इलेक्ट्रीशियन (वायरिंग/मोटर) | 📍 पश्चिम चंपारण | [📞 कॉल करें](tel:9876543211)\n• **मोहम्मद सलीम** — प्लंबर (फिटिंग/पाइप) | 📍 पश्चिम चंपारण | [📞 कॉल करें](tel:9876543212)")
    
    st.markdown("---")
    st.write("### 📝 अपना नाम डायरेक्टरी में जोड़ें:")
    k_name = st.text_input("कारीगर का नाम:")
    k_work = st.selectbox("काम का प्रकार:", ["वेल्डर (Welder)", "प्लंबर (Plumber)", "इलेक्ट्रीशियन (Electrician)", "राजमिस्त्री (Mason)", "बढ़ई (Carpenter)"])
    k_phone = st.text_input("फोन नंबर:")
    k_city = st.text_input("शहर / कस्बा:", value="पश्चिम चंपारण")
    if st.button("✅ नाम सुरक्षित सेव करें"):
        if k_name and k_phone:
            save_entry("कारीगर", k_name, k_phone, k_city, k_work)
            st.success("बधाई! आपका नाम सीधे संस्थापक के डेटाबेस में दर्ज हो गया है।")
        else:
            st.error("कृपया नाम और फोन नंबर दर्ज करें।")

# 3. LANGAR
elif choice == "🍲 लंगर व अन्न सेवा":
    st.subheader("🍲 लंगर, दस्तरख्वान व बचा खाना सेवा")
    l_food = st.text_input("खाने का विवरण (उदा: 30 पैकेट पूड़ी-सब्जी):")
    l_place = st.text_input("होटल / शादी हॉल / जगह:", value="मेन मार्केट")
    l_phone = st.text_input("संपर्क फोन नंबर:", value="7484878440")
    if st.button("📢 अन्न-सेवा अलर्ट जारी करें"):
        save_entry("अन्न-सेवा", "होटल/संस्था", l_phone, l_place, l_food)
        msg = "अन्न-सेवा अलर्ट! खाना: " + l_food + " उपलब्ध है। स्थान: " + l_place + "। फोन: +91 " + l_phone
        st.success("अन्न-सेवा अलर्ट सेव हो गया!")
        st.markdown("[📲 WhatsApp पर शेयर करें](https://wa.me/?text=" + urllib.parse.quote(msg) + ")")

# 4. DIRECT AID
elif choice == "🌙 सीधी मदद":
    st.subheader("🌙 बरकत, जकात व सीधी औजार मदद")
    st.caption("सीधे गरीब वेल्डर/प्लंबर को औजार या जरूरतमंद तक राशन पहुँचाएं:")
    d_type = st.selectbox("मदद का प्रकार:", ["कारीगर को औजार दिलाना", "गरीब परिवार को राशन", "दवा व इलाज सहायता"])
    d_amt = st.text_input("अनुमानित राशि (₹):", value="1000")
    d_phone = st.text_input("आपका फोन नंबर:", value="7484878440")
    if st.button("🤝 संकल्प दर्ज करें"):
        save_entry("दान-संकल्प", "दानदाता", d_phone, "लोकल", d_type + " | ₹" + d_amt)
        st.success("आपका संकल्प दर्ज कर लिया गया है।")

# 5. NIGHT SAFETY SOS
elif choice == "🚨 रात की सुरक्षा SOS":
    st.subheader("🚨 24x7 रात की सुरक्षा व लाइव GPS SOS")
    st.write("आपातकालीन कॉल: **112** (पुलिस) | **1090** (महिला सुरक्षा)")
    
    g_html = "<div style='text-align:center;'><button onclick='fPos()' style='background:#10B981;color:#fff;padding:10px;border:none;border-radius:6px;font-weight:bold;cursor:pointer;'>📡 लाइव GPS निकालें</button><p id='g_res' style='color:#38BDF8;font-size:12px;'></p></div><script>function fPos(){navigator.geolocation.getCurrentPosition(function(p){document.getElementById('g_res').innerHTML='https://maps.google.com/?q='+p.coords.latitude+','+p.coords.longitude;});}</script>"
    components.html(g_html, height=80)
    
    u_name = st.text_input("पीड़ित का नाम:", value="साहिल")
    u_road = st.text_input("सड़क / तिराहे का नाम:", value="मेन रोड")
    sos_txt = "आपातकालीन SOS अलर्ट! नाम: " + u_name + "। स्थान: " + u_road + "। समय: " + t_now
    st.markdown("[📲 परिवार को WhatsApp SOS भेजें](https://wa.me/" + WA_NUM + "?text=" + urllib.parse.quote(sos_txt) + ")")
    
    s_html = "<div style='text-align:center;margin-top:10px;'><button onclick='sPlay()' style='background:#EF4444;color:#fff;padding:10px 20px;border:none;border-radius:6px;font-weight:bold;cursor:pointer;'>🚨 अलार्म सायरन बजाएँ</button></div><script>function sPlay(){var a=new (window.AudioContext||window.webkitAudioContext)();var o=a.createOscillator();o.type='sawtooth';o.frequency.setValueAtTime(800,a.currentTime);o.frequency.linearRampToValueAtTime(1400,a.currentTime+0.3);o.connect(a.destination);o.start();o.stop(a.currentTime+3);}</script>"
    components.html(s_html, height=50)

# 6. VOICE
elif choice == "🎙️ बोलकर शिकायत":
    st.subheader("🎙️ बोलकर शिकायत दर्ज करें")
    st.caption("माइक बटन दबाएं और बोलें — आवाज़ अपने आप टाइप होगी:")
    v_html = "<div style='text-align:center;'><button onclick='rVoice()' style='background:#EF4444;color:#fff;padding:8px 16px;border:none;border-radius:6px;cursor:pointer;'>🎤 बोलें</button><br><textarea id='v_box' style='width:95%;height:70px;margin-top:8px;'></textarea></div><script>function rVoice(){var R=window.SpeechRecognition||window.webkitSpeechRecognition;var r=new R();r.onresult=function(e){document.getElementById('v_box').value=e.results[0][0].transcript;};r.start();}</script>"
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
st.caption("🏛️ संस्थापक: साहिल अहमद (Sahil Ahmad) • महा-सेवा AI राष्ट्रीय विधिक व जन-कल्याण मिशन")
