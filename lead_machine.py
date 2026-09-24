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
JOBS_FILE = "live_jobs.csv"
FOOD_FILE = "live_food.csv"
AID_FILE = "live_aid.csv"

def save_entry(c_type, name, phone, city, details):
    row = {"Date": today, "Time": t_now, "Type": c_type, "Name": name, "Phone": str(phone), "City": city, "Details": details}
    df = pd.DataFrame([row])
    if not os.path.exists(DB_NAME):
        df.to_csv(DB_NAME, index=False)
    else:
        df.to_csv(DB_NAME, mode='a', header=False, index=False)

def save_feed(file_path, row_dict):
    df = pd.DataFrame([row_dict])
    if not os.path.exists(file_path):
        df.to_csv(file_path, index=False)
    else:
        df.to_csv(file_path, mode='a', header=False, index=False)

LANGS = ["🇮🇳 हिन्दी", "🇬🇧 English"]
c_lang = st.radio("🌐 भाषा / Language:", LANGS, horizontal=True)
is_en = (c_lang == "🇬🇧 English")

MENU = [
    "💼 ताज़ा रोज़गार (इंजीनियर/कारीगर/हेल्पर)",
    "🌙 ज़कात, सदक़ा व गुप्त दान डेस्क",
    "🔴 लाइव अन्नदाता बुलेटिन", 
    "🕊️ जात-पात विरोधी भाईचारा कवच",
    "⚖️ 28 कानूनी नोटिस", 
    "👩‍🦰 नारी सुरक्षा व महिला रोज़गार",
    "🧓 बुजुर्ग सम्मान व ब्लड डोनर",
    "🌾 किसान मंडी व ड्राइवर सेवा",
    "🏪 दुकानदार व्यापार डेस्क", 
    "🏭 फ़ैक्ट्री हादसा मुआवज़ा दावा", 
    "💊 दवा व जेनेरिक भाव", 
    "🚨 रात की सुरक्षा SOS"
]

st.title("🇮🇳 महा-सेवा AI (MAHA SEVA AI)")
st.caption("अखंड भारत जन-कल्याण • 100% इंसानियत, 0% जात-पात • हर हाथ को काम, कोई भूखा न सोए")

choice = st.radio("सेवा चुनें:", MENU, horizontal=True)
st.markdown("---")

LAW_LIST = [
    ("मज़दूरी या वेतन चोरी", "Payment of Wages Act 1936", "लेबर कमिश्नर व डीएम", "मज़दूरी दबाना अपराध है; 10 गुना हर्जाना और 18% ब्याज।"),
    ("पुलिस अवैध मारपीट या चालान", "BNSS 2023 व DK Basu Guidelines", "एसपी व मानवाधिकार आयोग", "अवैध मारपीट पर धारा 166A BNS के तहत निलंबन व FIR।"),
    ("अस्पताल इमरजेंसी इलाज इनकार", "Supreme Court Parmanand Katara Verdict", "CMO व स्वास्थ्य विभाग", "इमरजेंसी में पैसे मांगकर इलाज से इनकार संज्ञेय अपराध है।"),
    ("कार्यस्थल पर हादसा व मुआवज़ा", "Employees Compensation Act 1923", "Compensation Commissioner", "हादसा होने पर ₹5-20 लाख मुआवज़ा अनिवार्य।"),
    ("लोन ऐप ब्लैकमेल व सूदखोरी", "RBI Guidelines & Sec 308 BNS", "साइबर सेल व एसपी", "बिना लाइसेंस सूदखोरी और गाली देकर वसूली पर तुरंत FIR।"),
    ("सरकारी दफ्तर घूसखोरी (RTPS)", "Right to Public Services Act", "निगरानी विभाग (Vigilance)", "काम लटकाने पर कर्मचारी के वेतन से प्रतिदिन जुर्माना कटता है।"),
    ("दुकानदार MRP लूट व घटतौली", "Legal Metrology Act 2009", "DSO व उपभोक्ता न्यायालय", "MRP से अधिक लेना या कम तौलना गैर-कानूनी है।"),
    ("रेलवे TTE अवैध वसूली", "Indian Railway Act", "RailMadad 139 व RPF", "TTE को बदसलूकी करने या ट्रेन से धक्का देने का अधिकार नहीं।"),
    ("थाने में FIR दर्ज न करना", "Supreme Court Lalita Kumari Directives", "SSP व CJM कोर्ट", "FIR न लिखने वाले पुलिसकर्मी पर धारा 166A BNS में FIR।"),
    ("ज़मीन पर दबंगों का अवैध क़ब्ज़ा", "Section 145/144 BNSS", "SDM व सिविल कोर्ट", "गरीब की ज़मीन पर क़ब्ज़े की कोशिश पर तुरंत पुलिस सुरक्षा व स्टे।"),
    ("राशन कोटेदार द्वारा चोरी", "National Food Security Act 2013", "SDO व DSO", "राशन कम देना दंडनीय अपराध है, कोटा तुरंत निरस्त होता है।"),
    ("बिजली विभाग फ़र्ज़ी बिल व कटाई", "Electricity Act 2003", "विद्युत लोकपाल व EE", "बिना 15 दिन के नोटिस के लाइन काटना गैर-कानूनी है।"),
    ("महिला घरेलू हिंसा व प्रताड़ना", "Domestic Violence Act 2005", "संरक्षण अधिकारी व महिला थाना", "महिला को सुरक्षा, भरण-पोषण और आवास का पूरा अधिकार है।"),
    ("दहेज उत्पीड़न व धमकी", "Section 85/86 BNS", "DSP व महिला सेल", "दहेज मांगना व प्रताड़ित करना गैर-जमानती अपराध है।"),
    ("महिला छेड़छाड़ व पीछा करना", "Section 78/74 BNS", "थाना प्रभारी व 1090", "महिला का पीछा करना या फब्तियां कसना संज्ञेय अपराध है।"),
    ("मकान मालिक द्वारा अवैध बेदखली", "Rent Control Act & Civil Law", "SDM व सिविल जज", "बिना कोर्ट आदेश के किराएदार का सामान फेंकना अवैध है।"),
    ("सड़क दुर्घटना हिट एंड रन दावा", "Motor Vehicles Act (MACT)", "MACT ट्रिब्यूनल व SP", "सड़क दुर्घटना में सरकार व बीमा कंपनी से तुरंत मुआवज़ा हक।"),
    ("ऑनलाइन साइबर बैंक फ्रॉड", "IT Act 2000 & 1930 Helpline", "साइबर सेल व 1930", "तुरंत शिकायत पर खाता फ्रीज होकर रिकवरी होती है।"),
    ("स्कूल द्वारा अवैध फ़ीस व TC रोकना", "Right to Education Act 2009", "जिला शिक्षा अधिकारी (BSA)", "फीस के नाम पर बच्चे की TC रोकना अपराध है।"),
    ("बैंक एजेंट अवैध वसूली कॉल", "RBI Fair Practice Code", "Banking Ombudsman व SP", "शाम 7 के बाद कॉल या घर आकर धमकी देना वर्जित है।"),
    ("ठेकेदार द्वारा EPF/PF चोरी", "EPF & MP Act 1952", "PF कमिश्नर (RPFC)", "वेतन से PF काटकर जमा न करना गबन व गैर-कानूनी है।"),
    ("जातिसूचक गाली व अपमान", "SC/ST Prevention of Atrocities Act", "DSP (SC/ST सेल)", "जातिसूचक अपमान पर गैर-जमानती धाराओं में कार्रवाई।"),
    ("वारंटी में सामान बदलने से इनकार", "Consumer Protection Act 2019", "उपभोक्ता आयोग (DCDRC)", "वारंटी अवधि में प्रोडक्ट न बदलना सेवा में गंभीर दोष है।"),
    ("नगर निगम गंदगी व नाली जाम", "Municipal Corporation Act", "नगर आयुक्त व DM", "साफ-सफाई की जिम्मेदारी स्थानीय निकाय की अनिवार्य है।"),
    ("सार्वजनिक रास्ते पर रुकावट", "Section 152 BNSS", "तहसीलदार व SDM", "आम रास्ते को रोकना गैर-कानूनी है, प्रशासन हटाएगा।"),
    ("अवैध ध्वनि प्रदूषण रात में DJ", "Noise Pollution Rules 2000", "प्रदूषण नियंत्रण बोर्ड व 112", "रात 10 बजे बाद तेज आवाज में DJ बजाना प्रतिबंधित है।"),
    ("बाल मज़दूरी व जोखिम भरा काम", "Child Labour Prohibition Act", "श्रम प्रवर्तन अधिकारी व CWC", "14 वर्ष से कम उम्र के बच्चे से काम कराना दंडनीय है।"),
    ("RTI सूचना देने से इनकार", "Right to Information Act 2005", "राज्य सूचना आयोग", "30 दिन में सूचना न देने पर अधिकारी पर जुर्माना लगता है।")
]

# 1. LIVE JOBS
if choice == MENU[0]:
    st.subheader("💼 अखंड भारत रोज़गार बोर्ड (हर हाथ को काम)")
    t1, t2 = st.tabs(["📢 काम / स्टाफ चाहिए (Hire)", "🛠️ काम खोजने वाले साथी"])
    with t1:
        j_cat = st.selectbox("काम की श्रेणी:", ["इंजीनियर (Civil/Mech/Elec)", "सेफ्टी ऑफिसर (HSE)", "सुपरवाइजर", "वेल्डर / फिटर", "इलेक्ट्रीशियन / प्लंबर", "राजमिस्त्री / बढ़ई", "फैक्ट्री वर्कर / हेल्पर", "सिलाई / कुकिंग / पैकिंग"])
        j_req = st.text_input("ज़रूरत (उदा: 2 वेल्डर और 1 सेफ्टी ऑफिसर):")
        j_wage = st.text_input("वेतन / दिहाड़ी:", value="₹650 प्रतिदिन")
        j_loc = st.text_input("कार्यस्थल पता:", value="इंडस्ट्रियल एरिया")
        j_phone = st.text_input("मालिक का मोबाइल नंबर:", value="7484878440")
        if st.button("📢 रोज़गार बोर्ड पर पोस्ट करें"):
            if j_req and j_phone:
                save_feed(JOBS_FILE, {"Time": t_now, "Category": j_cat, "Job": j_req, "Wage": j_wage, "Location": j_loc, "Phone": j_phone})
                save_entry("रोज़गार मांग", "नियोक्ता", j_phone, j_loc, f"{j_cat} | {j_req} | {j_wage}")
                st.success("पोस्ट लाइव हो गई!")
                st.markdown(f"[📲 WhatsApp पर भेजें](https://wa.me/?text={urllib.parse.quote(f'रोज़गार अलर्ट! {j_cat}: {j_req}। दिहाड़ी: {j_wage}। स्थान: {j_loc}। कॉल: +91 {j_phone}')})")

        st.write("### 📌 ताज़ा उपलब्ध नौकरियाँ:")
        if os.path.exists(JOBS_FILE):
            df_j = pd.read_csv(JOBS_FILE).tail(10)
            for _, r in df_j.iterrows():
                st.markdown(f"• **{r.get('Category', 'काम')}**: {r['Job']} ({r['Wage']}) | 📍 {r['Location']} — [📞 सीधे कॉल करें](tel:{r['Phone']})")
        else:
            st.info("वर्तमान में कोई वैकेंसी लिस्टेड नहीं है।")

    with t2:
        k_name = st.text_input("आपका पूरा नाम:")
        k_skill = st.selectbox("हुनर:", ["इंजीनियर", "सेफ्टी ऑफिसर", "सुपरवाइजर", "वेल्डर", "इलेक्ट्रीशियन", "प्लंबर", "राजमिस्त्री", "हेल्पर", "महिला गृह उद्योग"])
        k_mob = st.text_input("मोबाइल नंबर:")
        k_city = st.text_input("शहर / जिला:", value="पश्चिम चंपारण")
        if st.button("✅ डायरेक्टरी में नाम जोड़ें"):
            if k_name and k_mob:
                save_entry("हुनरमंद साथी", k_name, k_mob, k_city, k_skill)
                st.success("नाम सुरक्षित सेव हो गया!")

# 2. DIRECT AID & ZAKAT
elif choice == MENU[1]:
    st.subheader("🌙 बरकत, ज़कात, सदक़ा व गुप्त दान डेस्क")
    st.info("यह सेवा 100% पारदर्शी है। दानदाता का पैसा सीधे ज़रूरतमंद के हाथ या अस्पताल/स्कूल में जाएगा, बीच में कोई दलाल नहीं।")
    
    a_tab1, a_tab2 = st.tabs(["🤝 दान / ज़कात देने वाले", "🤲 ज़रूरतमंद सहायता आवेदन"])
    
    with a_tab1:
        st.write("### दानदाता अपना संकल्प दर्ज करें:")
        d_name = st.text_input("दानदाता का नाम (या 'गुप्त दान' लिखें):", value="गुप्त दानदाता")
        d_type = st.selectbox("दान / ज़कात का माध्यम:", ["गरीब कारीगर को औज़ार दिलाना", "यतीम/अनाथ बच्चे की स्कूल फीस", "अस्पताल में गरीब मरीज़ की दवा", "गरीब परिवार को सूखा राशन कीट", "सामान्य ज़कात राशि"])
        d_amt = st.text_input("राशि (₹):", value="1000")
        d_phone = st.text_input("फोन नंबर (गोपनीय रहेगा):", value="7484878440")
        if st.button("🤝 दान संकल्प दर्ज करें"):
            save_entry("दान-संकल्प", d_name, d_phone, "लोकल", f"{d_type} | ₹{d_amt}")
            st.success("अल्हम्दुलिल्लाह / धन्यवाद! आपका संकल्प संस्थापक के पास सुरक्षित दर्ज हो गया है।")

    with a_tab2:
        st.write("### वास्तविक ज़रूरतमंद सीधे आवेदन करें:")
        n_name = st.text_input("ज़रूरतमंद का नाम:")
        n_need = st.selectbox("किस सहायता की आवश्यकता है:", ["काम शुरू करने के लिए औज़ार चाहिए", "बच्चे की पढ़ाई/कॉपी-किताब हेतु", "मरीज़ की दवा व इलाज", "राशन सहायता"])
        n_desc = st.text_area("अपनी परेशानी का सच्चा विवरण लिखें:")
        n_phone = st.text_input("संपर्क नंबर:")
        if st.button("🤲 सहायता का आवेदन भेजें"):
            if n_name and n_phone:
                save_entry("मदद गुहार", n_name, n_phone, "लोकल", f"{n_need} | {n_desc}")
                st.success("आपका आवेदन संस्थापक के पास पहुँच चुका है। सत्यापन के बाद सीधे मदद की जाएगी।")

# 3. LIVE FOOD FEED
elif choice == MENU[2]:
    st.subheader("🔴 लाइव अन्नदाता व लंगर बुलेटिन")
    with st.expander("📢 उपलब्ध खाने की सूचना दर्ज करें (200+ पैकेट / बचा खाना)"):
        f_qty = st.text_input("खाने का विवरण (उदा: 200 पैकेट पूड़ी-सब्ज़ी):")
        f_loc = st.text_input("सटीक स्थान / होटल / शादी हॉल:", value="रेलवे स्टेशन चौक")
        f_phone = st.text_input("पिकअप फोन नंबर:", value="7484878440")
        if st.button("📢 लाइव बोर्ड पर जारी करें"):
            if f_qty and f_phone:
                save_feed(FOOD_FILE, {"Time": t_now, "Food": f_qty, "Location": f_loc, "Phone": f_phone})
                save_entry("अन्न-सेवा", "दानदाता", f_phone, f_loc, f_qty)
                st.success("खाना लाइव बोर्ड पर जुड़ गया!")
                st.markdown(f"[📲 WhatsApp पर भेजें](https://wa.me/?text={urllib.parse.quote(f'अन्नदाता अलर्ट! {f_qty} उपलब्ध है। स्थान: {f_loc}। कॉल: +91 {f_phone}')})")

    st.write("### 🍱 वर्तमान में उपलब्ध खाना:")
    if os.path.exists(FOOD_FILE):
        df_f = pd.read_csv(FOOD_FILE).tail(10)
        for _, r in df_f.iterrows():
            st.markdown(f"• **{r['Food']}** | 📍 {r['Location']} ({r['Time']}) — [📞 तुरंत कॉल करें](tel:{r['Phone']})")
    else:
        st.info("वर्तमान में कोई खाना लिस्टेड नहीं है।")

# 4. ANTI-CASTE SHIELD
elif choice == MENU[3]:
    st.subheader("🕊️ राष्ट्रीय सद्भाव व जात-पात विरोधी भाईचारा कवच")
    st.info("संविधान व कानून: किसी भी नागरिक के साथ जाति, धर्म या वर्ग के आधार पर भेदभाव करना, नफ़रत फैलाना अपराध है (धारा 196, 197, 299 BNS)।")
    u_name = st.text_input("शिकायतकर्ता का नाम:", value="साहिल कुमार")
    u_city = st.text_input("जिला व राज्य:", value="पश्चिम चंपारण, बिहार")
    u_phone = st.text_input("मोबाइल नंबर:", value="7484878440")
    accused_l = st.text_input("नफ़रत/भेदभाव फैलाने वाले व्यक्ति / नेता का नाम:")
    act_t = st.selectbox("भेदभाव का प्रकार:", ["जाति/धर्म के आधार पर सार्वजनिक गाली-गलौज", "दुकान/पानी/रास्ते से वंचित करना", "सोशल मीडिया पर नफरती बयान", "वर्कप्लेस पर जातिगत प्रताड़ना"])
    if st.button("⚡ नफ़रत विरोधी आधिकारिक कानूनी नोटिस बनाएं"):
        if accused_l:
            save_entry("सद्भाव शिकायत", u_name, u_phone, u_city, f"आरोपी: {accused_l} | {act_t}")
            h_notice = f"STATUTORY NOTICE AGAINST DISCRIMINATION\nसेवा में: SP / DM, {u_city}\nविषय: '{accused_l}' द्वारा जातिगत नफ़रत व विद्वेष फैलाने बाबत।\nप्रार्थी: {u_name} (+91 {u_phone})\nधारा 196, 197, 299 BNS के तहत गैर-जमानती प्राथमिकी दर्ज की जाए।"
            st.text_area("तैयार नोटिस:", h_notice, height=130)
            st.markdown(f"[📲 SP व प्रशासन को WhatsApp पर भेजें](https://wa.me/?text={urllib.parse.quote(h_notice)})")

# 5. 28 LEGAL NOTICES
elif choice == MENU[4]:
    st.subheader("⚖️ 28 आधिकारिक कानूनी नोटिस जनरेटर")
    sec_num = st.number_input("धारा संख्या चुनें (1 से 28):", min_value=1, max_value=28, value=1, step=1)
    s_name, s_act, s_auth, s_rule = LAW_LIST[sec_num - 1]
    st.info(f"धारा {sec_num}: {s_name} | {s_act}")
    v_name = st.text_input("प्रार्थी का नाम:", value="साहिल कुमार")
    v_city = st.text_input("जिला व राज्य:", value="पश्चिम चंपारण, बिहार")
    v_phone = st.text_input("मोबाइल नंबर:", value="7484878440")
    v_acc = st.text_input("दोषी पक्ष / अधिकारी का नाम:", value="संबंधित दोषी पक्ष")
    v_desc = st.text_area("घटनाक्रम विवरण:", value=f"{s_name} के संबंध में प्रार्थी को प्रताड़ित किया जा रहा है।", height=70)
    if st.button("⚡ कानूनी नोटिस तैयार करें"):
        save_entry("कानूनी नोटिस", v_name, v_phone, v_city, f"दोषी: {v_acc} | धारा {sec_num}: {s_name}")
        notc = f"आधिकारिक कानूनी नोटिस\nअधिनियम: {s_act}\nसेवा में: {s_auth}, {v_city}\nविषय: '{v_acc}' के विरुद्ध कानूनी कार्रवाई ({s_name})\nप्रार्थी: {v_name} (+91 {v_phone})\nविवरण: {v_desc}\nनियम: {s_rule}\nहस्ताक्षर: {v_name}"
        st.success("🟢 नोटिस तैयार:")
        st.text_area("Notice:", notc, height=150)
        st.download_button("📥 डाउनलोड (.txt)", notc, file_name=f"Notice_{sec_num}.txt")
        st.markdown(f"[📲 WhatsApp पर भेजें](https://wa.me/?text={urllib.parse.quote(notc)})")

# 6. WOMEN SAFETY
elif choice == MENU[5]:
    st.subheader("👩‍🦰 नारी सुरक्षा व महिला स्वावलंबन डेस्क")
    st.info("हेल्पलाइन: 1090 (महिला हेल्पलाइन) | 181 (घरेलू हिंसा) | 112 (पुलिस)")
    wm_name = st.text_input("बहन / आवेदिका का नाम:")
    wm_phone = st.text_input("संपर्क नंबर:")
    wm_prob = st.selectbox("समस्या:", ["दहेज प्रताड़ना व मारपीट", "ससुराल में हिंसा", "छेड़छाड़ / पीछा करना", "घर बैठे सिलाई/कुकिंग काम चाहिए"])
    if st.button("⚡ आवेदन / शिकायत दर्ज करें"):
        if wm_name and wm_phone:
            save_entry("महिला डेस्क", wm_name, wm_phone, "लोकल", wm_prob)
            st.success("आवेदन सुरक्षित दर्ज हो गया!")

# 7. SENIOR CITIZENS
elif choice == MENU[6]:
    st.subheader("🧓 बुजुर्ग सम्मान व आपातकालीन ब्लड डोनर डेस्क")
    st.markdown("• **राहुल वर्मा** — B+ | 📍 पश्चिम चंपारण | [📞 कॉल](tel:9876543210)\n• **अमित कुमार** — O+ | 📍 पश्चिम चंपारण | [📞 कॉल](tel:9876543211)")
    p_name = st.text_input("बुजुर्ग माता-पिता या डोनर का नाम:")
    p_phone = st.text_input("फोन नंबर:")
    p_act = st.selectbox("सेवा प्रकार:", ["रक्तदाता बनना चाहते हैं", "संतान भरण-पोषण नहीं दे रही (SDM Notice)"])
    if st.button("✅ सुरक्षित दर्ज करें"):
        save_entry("बुजुर्ग/ब्लड डेस्क", p_name, p_phone, "लोकल", p_act)
        st.success("डेटा सुरक्षित सेव हो गया!")

# 8. FARMER & DRIVER
elif choice == MENU[7]:
    st.subheader("🌾 किसान मंडी व ड्राइवर / वाहन सेवा")
    st.markdown("• **गेहूँ:** ₹2275-₹2400 / क्विंटल | **धान:** ₹2180-₹2300 / क्विंटल | **मक्का:** ₹1900-₹2100 / क्विंटल")
    d_name = st.text_input("ड्राइवर का नाम:")
    d_veh = st.selectbox("वाहन प्रकार:", ["ऑटो / ई-रिक्शा", "पिकअप / मालवाहक", "ट्रैक्टर / ट्रॉली", "टैक्सी / कार"])
    d_ph = st.text_input("ड्राइवर मोबाइल नंबर:")
    if st.button("✅ वाहन सूची में जुड़ें"):
        save_entry("ड्राइवर", d_name, d_ph, "लोकल", d_veh)
        st.success("वाहन चालक सूची में जुड़ गया!")

# 9. MERCHANT DESK
elif choice == MENU[8]:
    st.subheader("🏪 स्थानीय दुकानदार व्यापार डेस्क")
    m_tool = st.radio("टूल:", ["⚡ Near-Expiry / सस्ता सामान निकालें", "📲 WhatsApp उधारी तकादा"])
    if m_tool == "⚡ Near-Expiry / सस्ता सामान निकालें":
        item_name = st.text_input("सामान व मात्रा (उदा: 20 पैकेट तेल):")
        item_disc = st.text_input("ऑफ़र भाव (उदा: MRP ₹150, भाव ₹90):")
        shop_phone = st.text_input("दुकानदार फोन नंबर:", value="7484878440")
        if st.button("📢 ऑफ़र शेयर करें"):
            st.markdown(f"[📲 ग्राहकों को WhatsApp भेजें](https://wa.me/?text={urllib.parse.quote(f'महा-छूट! {item_name} भारी छूट पर उपलब्ध: {item_disc}। संपर्क: +91 {shop_phone}')})")
    else:
        cust_name = st.text_input("ग्राहक का नाम:")
        due_amt = st.text_input("बकाया राशि (₹):", value="1500")
        cust_phone = st.text_input("ग्राहक का मोबाइल नंबर:")
        if st.button("⚡ WhatsApp रिमाइंडर भेजें"):
            st.markdown(f"[📲 उधारी रिमाइंडर भेजें](https://wa.me/91{cust_phone}?text={urllib.parse.quote(f'नमस्ते {cust_name} जी, आपका ₹{due_amt} का हिसाब बाकी है। कृपया भुगतान कराने का कष्ट करें।')})")

# 10. FACTORY CLAIM
elif choice == MENU[9]:
    st.subheader("🏭 कंपनी/फ़ैक्ट्री हादसा व क़ानूनी मुआवज़ा दावा")
    w_name = st.text_input("मज़दूर का नाम:", value="साहिल कुमार")
    w_city = st.text_input("जिला व राज्य:", value="पश्चिम चंपारण, बिहार")
    w_phone = st.text_input("मोबाइल नंबर:", value="7484878440")
    w_comp = st.text_input("कंपनी का नाम:", value="ABC Manufacturing Pvt. Ltd.")
    w_inj = st.text_area("चोट का विवरण:", value="मशीन में सुरक्षा उपकरण न होने से हाथ में गंभीर चोट।")
    if st.button("⚡ मुआवज़ा दावा नोटिस तैयार करें"):
        save_entry("Accident Claim", w_name, w_phone, w_city, f"{w_comp} | {w_inj}")
        cl_notice = f"STATUTORY COMPENSATION NOTICE (Sec 10, Employees Compensation Act)\nसेवा में: मैनेजमेंट, {w_comp} व लेबर कोर्ट\nपीड़ित: {w_name} (+91 {w_phone})\nहादसा व चोट: {w_inj}\nमांग: 100% मुफ्त इलाज, छुट्टी का पूरा वेतन व कानूनी मुआवजा 30 दिन में दिया जाए।"
        st.text_area("Claim Notice:", cl_notice, height=130)
        st.markdown(f"[📲 WhatsApp पर भेजें](https://wa.me/?text={urllib.parse.quote(cl_notice)})")

# 11. MEDICINE CHECKER
elif choice == MENU[10]:
    st.subheader("💊 दवा जानकारी व जन औषधि सस्ता विकल्प")
    m_name = st.text_input("दवा या बीमारी का नाम लिखें:", value="Azithromycin 500")
    if st.button("🔍 दवा भाव जाँचें"):
        q_low = m_name.lower()
        if "paracetamol" in q_low or "बुखार" in q_low:
            txt = "बुखार व दर्द निवारक। जन औषधि पर मात्र ₹10-15 (बाज़ार में ₹35-40)।"
        elif "azithromycin" in q_low or "infection" in q_low:
            txt = "एंटीबायोटिक। जन औषधि पर मात्र ₹25-35 (बाज़ार में ₹120-150)।"
        elif "pantoprazole" in q_low or "गैस" in q_low:
            txt = "गैस व एसिडिटी निवारक। जन औषधि भाव मात्र ₹15-20 (बाज़ार में ₹80-100)।"
        else:
            txt = f"{m_name} का जेनेरिक साल्ट जन औषधि केंद्र पर 70-80% सस्ते भाव में उपलब्ध है।"
        st.success(txt)

# 12. NIGHT SOS
elif choice == MENU[11]:
    st.subheader("🚨 24x7 रात की सुरक्षा व लाइव GPS SOS")
    st.write("पुलिस: **112** | महिला हेल्पलाइन: **1090**")
    g_html = "<div style='text-align:center;'><button onclick='fPos()' style='background:#10B981;color:#fff;padding:10px;border:none;border-radius:6px;font-weight:bold;cursor:pointer;'>📡 लाइव GPS निकालें</button><p id='g_res' style='color:#38BDF8;font-size:12px;'></p></div><script>function fPos(){navigator.geolocation.getCurrentPosition(function(p){document.getElementById('g_res').innerHTML='https://maps.google.com/?q='+p.coords.latitude+','+p.coords.longitude;});}</script>"
    components.html(g_html, height=75)
    sos_name = st.text_input("पीड़ित का नाम:", value="साहिल")
    sos_road = st.text_input("सड़क / चौराहा:", value="मेन रोड")
    st.markdown(f"[📲 परिवार को WhatsApp SOS भेजें](https://wa.me/{WA_NUM}?text={urllib.parse.quote(f'EMERGENCY SOS! Name: {sos_name}. Location: {sos_road}. Time: {t_now}.')})")

# ADMIN PANEL
st.markdown("---")
with st.expander("🔐 संस्थापक गुप
