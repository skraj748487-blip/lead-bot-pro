import streamlit as st
import streamlit.components.v1 as components
import urllib.parse
from datetime import datetime
import pandas as pd
import os

st.set_page_config(
    page_title="महा-सेवा AI — अखंड भारत 100% इंसानियत मिशन",
    page_icon="🇮🇳",
    layout="centered",
    initial_sidebar_state="collapsed"
)

WA_NUM = "917484878440"
today = datetime.now().strftime("%d-%m-%Y")
t_now = datetime.now().strftime("%I:%M %p")
DB_NAME = "maha_seva_data.csv"
JOBS_FILE = "live_jobs.csv"
FOOD_FILE = "live_food.csv"

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

MENU_HI = [
    "🕊️ जात-पात विरोधी व भाईचारा कवच",
    "⚖️ 28 कानूनी नोटिस", 
    "👩‍🦰 नारी सुरक्षा व महिला रोजगार",
    "🧓 बुजुर्ग सम्मान व ब्लड डोनर",
    "🔴 लाइव अन्नदाता बुलेटिन", 
    "💼 ताज़ा रोज़गार व कारीगर", 
    "🌾 किसान मंडी व ड्राइवर सेवा",
    "🏪 दुकानदार व्यापार डेस्क", 
    "🏭 फैक्ट्री हादसा दावा", 
    "💊 दवा व जेनेरिक भाव", 
    "🚨 रात की सुरक्षा SOS"
]

MENU_EN = [
    "🕊️ Anti-Caste & Unity Shield",
    "⚖️ 28 Legal Notices", 
    "👩‍🦰 Women Safety & Jobs",
    "🧓 Senior Care & Blood Donors",
    "🔴 Live Food Feed", 
    "💼 Live Jobs & Artisans", 
    "🌾 Farmer Mandi & Driver Desk",
    "🏪 Merchant Desk", 
    "🏭 Factory Injury Claim", 
    "💊 Medicine Checker", 
    "🚨 Night SOS"
]

menu_items = MENU_EN if is_en else MENU_HI

st.title("🇮🇳 महा-सेवा AI (MAHA SEVA AI)")
st.caption("अखंड भारत जन-कल्याण • 100% इंसानियत, 0% जात-पात • गरीब-अमीर, मजदूर, किसान व नारी का सच्चा मंच")

choice = st.radio("Menu:", menu_items, horizontal=True)
st.markdown("---")

LAW_LIST = [
    ("मजदूरी या वेतन चोरी", "Payment of Wages Act 1936", "लेबर कमिश्नर व डीएम", "मजदूरी दबाना गैर-कानूनी है; 10 गुना हर्जाना और 18% ब्याज।"),
    ("पुलिस अवैध मारपीट या चालान", "BNSS 2023 व DK Basu Guidelines", "एसपी व मानवाधिकार आयोग", "अवैध मारपीट पर धारा 166A BNS के तहत निलंबन व FIR।"),
    ("अस्पताल इमरजेंसी इलाज इनकार", "Supreme Court Parmanand Katara Verdict", "CMO व स्वास्थ्य विभाग", "इमरजेंसी में पैसे मांगकर इलाज से इनकार संज्ञेय अपराध है।"),
    ("कार्यस्थल पर हादसा व मुआवजा", "Employees Compensation Act 1923", "Compensation Commissioner", "हादसा होने पर ₹5-20 लाख मुआवजा व आजीवन पेंशन अनिवार्य।"),
    ("लोन ऐप ब्लैकमेल व सूदखोरी", "RBI Guidelines & Sec 308 BNS", "साइबर सेल व एसपी", "बिना लाइसेंस सूदखोरी और गाली देकर वसूली पर तुरंत FIR।"),
    ("सरकारी दफ्तर घूसखोरी (RTPS)", "Right to Public Services Act", "निगरानी विभाग (Vigilance)", "काम लटकाने पर कर्मचारी के वेतन से प्रतिदिन जुर्माना कटता है।"),
    ("दुकानदार MRP लूट व घटतौली", "Legal Metrology Act 2009", "DSO व उपभोक्ता न्यायालय", "MRP से अधिक लेना या कम तौलना गैर-कानूनी है।"),
    ("रेलवे TTE अवैध वसूली", "Indian Railway Act", "RailMadad 139 व RPF", "TTE को बदसलूकी करने या ट्रेन से धक्का देने का अधिकार नहीं।"),
    ("थाने में FIR दर्ज न करना", "Supreme Court Lalita Kumari Directives", "SSP व CJM कोर्ट", "FIR न लिखने वाले पुलिसकर्मी पर धारा 166A BNS में FIR।"),
    ("जमीन पर दबंगों का अवैध कब्जा", "Section 145/144 BNSS", "SDM व सिविल कोर्ट", "गरीब की जमीन पर कब्जे की कोशिश पर तुरंत पुलिस सुरक्षा व स्टे।"),
    ("राशन कोटेदार द्वारा चोरी", "National Food Security Act 2013", "SDO व DSO", "राशन कम देना दंडनीय अपराध है, कोटा तुरंत निरस्त होता है।"),
    ("बिजली विभाग फर्जी बिल व कटाई", "Electricity Act 2003", "विद्युत लोकपाल व EE", "बिना 15 दिन के नोटिस के लाइन काटना गैर-कानूनी है।"),
    ("महिला घरेलू हिंसा व प्रताड़ना", "Domestic Violence Act 2005", "संरक्षण अधिकारी व महिला थाना", "महिला को सुरक्षा, भरण-पोषण और आवास का पूरा अधिकार है।"),
    ("दहेज उत्पीड़न व धमकी", "Section 85/86 BNS", "DSP व महिला सेल", "दहेज मांगना व प्रताड़ित करना गैर-जमानती अपराध है।"),
    ("महिला छेड़छाड़ व पीछा करना", "Section 78/74 BNS", "थाना प्रभारी व 1090", "महिला का पीछा करना या फब्तियां कसना संज्ञेय अपराध है।"),
    ("मकान मालिक द्वारा अवैध बेदखली", "Rent Control Act & Civil Law", "SDM व सिविल जज", "बिना कोर्ट आदेश के किराएदार का सामान फेंकना अवैध है।"),
    ("सड़क दुर्घटना हिट एंड रन दावा", "Motor Vehicles Act (MACT)", "MACT ट्रिब्यूनल व SP", "सड़क दुर्घटना में सरकार व बीमा कंपनी से तुरंत मुआवजा हक।"),
    ("ऑनलाइन साइबर बैंक फ्रॉड", "IT Act 2000 & 1930 Helpline", "साइबर सेल व 1930", "तुरंत शिकायत पर खाता फ्रीज होकर रिकवरी होती है।"),
    ("स्कूल द्वारा अवैध फीस व TC रोकना", "Right to Education Act 2009", "जिला शिक्षा अधिकारी (BSA)", "फीस के नाम पर बच्चे की TC रोकना अपराध है।"),
    ("बैंक एजेंट अवैध वसूली कॉल", "RBI Fair Practice Code", "Banking Ombudsman व SP", "शाम 7 के बाद कॉल या घर आकर धमकी देना वर्जित है।"),
    ("ठेकेदार द्वारा EPF/PF चोरी", "EPF & MP Act 1952", "PF कमिश्नर (RPFC)", "वेतन से PF काटकर जमा न करना गबन व गैर-कानूनी है।"),
    ("जातिसूचक गाली व अपमान", "SC/ST Prevention of Atrocities Act", "DSP (SC/ST सेल)", "जातिसूचक अपमान पर गैर-जमानती धाराओं में कार्रवाई।"),
    ("वारंटी में सामान बदलने से इनकार", "Consumer Protection Act 2019", "उपभोक्ता आयोग (DCDRC)", "वारंटी अवधि में प्रोडक्ट न बदलना सेवा में गंभीर दोष है।"),
    ("नगर निगम गंदगी व नाली जाम", "Municipal Corporation Act", "नगर आयुक्त व DM", "साफ-सफाई की जिम्मेदारी स्थानीय निकाय की अनिवार्य है।"),
    ("सार्वजनिक रास्ते पर रुकावट", "Section 152 BNSS", "तहसीलदार व SDM", "आम रास्ते को रोकना गैर-कानूनी है, प्रशासन हटाएगा।"),
    ("अवैध ध्वनि प्रदूषण रात में DJ", "Noise Pollution Rules 2000", "प्रदूषण नियंत्रण बोर्ड व 112", "रात 10 बजे बाद तेज आवाज में DJ बजाना प्रतिबंधित है।"),
    ("बाल मजदूरी व जोखिम भरा काम", "Child Labour Prohibition Act", "श्रम प्रवर्तन अधिकारी व CWC", "14 वर्ष से कम उम्र के बच्चे से काम कराना दंडनीय है।"),
    ("RTI सूचना देने से इनकार", "Right to Information Act 2005", "राज्य सूचना आयोग", "30 दिन में सूचना न देने पर अधिकारी पर जुर्माना लगता है।")
]

# 0. ANTI-CASTE & BROTHERHOOD SHIELD
if choice in [MENU_HI[0], MENU_EN[0]]:
    st.subheader("🕊️ राष्ट्रीय सद्भाव, जात-पात विरोधी व भाईचारा सुरक्षा कवच")
    st.info("भारतीय संविधान व बीएनएस (BNS): किसी भी नागरिक के साथ जाति, धर्म या वर्ग के आधार पर भेदभाव करना, नफ़रत फैलाना या सामाजिक बहिष्कार कराना गैर-जमानती संज्ञेय अपराध है (धारा 196, 197, 299 BNS)।")
    
    st.markdown("""
    * **100% इंसानियत का नियम:** इस मंच पर न कोई ऊँच है, न नीच। सेवा, खाना, खून और रोज़गार सबको बराबर मिलेगा।
    * **नेताओं व असामाजिक तत्वों की नफरत पर रोक:** यदि कोई नेता या व्यक्ति जात-पात के नाम पर लड़ाने, गालियाँ देने या मंदिर/मस्जिद/सार्वजनिक स्थान पर जाने से रोके, तो तुरंत आधिकारिक कानूनी नोटिस जारी करें।
    """)
    
    c1, c2 = st.columns(2)
    u_name = c1.text_input("शिकायतकर्ता का नाम:", value="साहिल कुमार")
    u_city = c2.text_input("जिला व राज्य:", value="पश्चिम चंपारण, बिहार")
    u_phone = st.text_input("मोबाइल नंबर:", value="7484878440")
    accused_leader = st.text_input("नफ़रत/भेदभाव फैलाने वाले व्यक्ति / नेता का नाम:")
    act_type = st.selectbox("किए गए भेदभाव का प्रकार:", [
        "जाति/धर्म के आधार पर सार्वजनिक भेदभाव व गालियाँ देना",
        "दुकान, पानी या सार्वजनिक रास्ते से वंचित करना",
        "सोशल मीडिया पर दंगा भड़काने व नफरत फैलाने वाला बयान",
        "वर्कप्लेस या मजदूरी में जातिगत पक्षपात व प्रताड़ना"
    ])
    evid_text = st.text_area("घटनाक्रम व मौजूद साक्ष्य (ऑडियो/वीडियो/गवाह):", value="संबंधित व्यक्ति द्वारा सार्वजनिक रूप से जातिसूचक व नफरती शब्दों का प्रयोग कर सामाजिक सौहार्द्र बिगाड़ने का कृत्य किया गया।")
    
    if st.button("⚡ नफ़रत व जातिगत भेदभाव विरोधी आधिकारिक कानूनी नोटिस तैयार करें"):
        if accused_leader:
            save_entry("सद्भाव शिकायत", u_name, u_phone, u_city, f"आरोपी: {accused_leader} | {act_type}")
            hate_notice = (
                "======================================================================\n"
                "STATUTORY NOTICE AGAINST CASTE DISCRIMINATION & COMMUNAL DISHARMONY\n"
                "(भारतीय न्याय संहिता 2023 - धारा 196, 197, 299 व SC/ST अत्याचार निवारण अधिनियम)\n"
                f"दिनांक: {today}\n\n"
                f"सेवा में:\n1. पुलिस अधीक्षक (SP) / जिलाधिकारी (DM), {u_city}\n"
                "2. राष्ट्रीय मानवाधिकार आयोग (NHRC), नई दिल्ली\n\n"
                f"विषय: '{accused_leader}' द्वारा जातिगत नफ़रत, सामाजिक विद्वेष व भेदभाव फैलाने के विरुद्ध गैर-जमानती FIR दर्ज करने बाबत।\n\n"
                f"महोदय,\n"
                f"प्रार्थी {u_name} (मोबाइल: +91 {u_phone}), निवासी {u_city}, राज्य करता है:\n"
                f"1. विपक्षी '{accused_leader}' द्वारा दिनांक {today} को जानबूझकर {act_type} का आपराधिक कृत्य किया गया।\n"
                f"2. साक्ष्य व घटना विवरण: {evid_text}\n"
                "3. सर्वोच्च न्यायालय के दिशा-निर्देशों अनुसार किसी भी नागरिक को जाति या धर्म के आधार पर प्रताड़ित करना संविधान के अनुच्छेद 14, 15 और 21 का खुला उल्लंघन है।\n\n"
                "अतः निवेदन है कि विपक्षी के विरुद्ध अविलंब गैर-जमानती धाराओं में प्राथमिकी (FIR) दर्ज कर कड़ी विधिक कार्रवाई की जाए।\n\n"
                f"प्रार्थी हस्ताक्षर: {u_name}\n"
                "प्रमाणित: महा-सेवा AI राष्ट्रीय अखंडता व जन-कल्याण मिशन\n"
                "======================================================================"
            )
            st.success("🟢 आधिकारिक नोटिस तैयार व डेटाबेस में सुरक्षित:")
            st.text_area("नोटिस कॉपी करें:", hate_notice, height=180)
            st.download_button("📥 नोटिस डाउनलोड करें (.txt)", hate_notice, file_name="Anti_Discrimination_Notice.txt")
            c_h = hate_notice.replace("\n", "<br>").replace("'", "\\'")
            p_html = f"<div style='text-align:center;'><button onclick='pDoc()' style='background:#2563EB;color:#fff;padding:10px 20px;border:none;border-radius:6px;cursor:pointer;font-weight:bold;'>🖨️ PDF प्रिंट / सेव करें</button></div><script>function pDoc(){{var w=window.open('','','width=800,height=700');w.document.write('<html><body style=\"font-family:monospace;padding:20px;\">{c_h}</body></html>');w.document.close();w.print();}}</script>"
            components.html(p_html, height=50)
            st.markdown(f"[📲 यह नोटिस SP व प्रशासन को WhatsApp पर भेजें](https://wa.me/?text={urllib.parse.quote(hate_notice)})")
        else:
            st.error("कृपया आरोपी/नेता का नाम दर्ज करें।")

# 1. 28 LEGAL NOTICES
elif choice in [MENU_HI[1], MENU_EN[1]]:
    st.subheader("⚖️ 28 आधिकारिक कानूनी नोटिस जनरेटर")
    sec_num = st.number_input("धारा संख्या चुनें (1 से 28):", min_value=1, max_value=28, value=1, step=1)
    s_name, s_act, s_auth, s_rule = LAW_LIST[sec_num - 1]
    st.info(f"धारा {sec_num}: {s_name}\n\nअधिनियम: {s_act} | सक्षम प्राधिकारी: {s_auth}")

    c1, c2 = st.columns(2)
    v_name = c1.text_input("प्रार्थी का नाम:", value="साहिल कुमार")
    v_city = c2.text_input("जिला व राज्य:", value="पश्चिम चंपारण, बिहार")
    v_phone = st.text_input("मोबाइल नंबर:", value="7484878440")
    v_acc = st.text_input("दोषी पक्ष / अधिकारी का नाम:", value="संबंधित दोषी पक्ष")
    v_desc = st.text_area("घटनाक्रम का विवरण:", value=f"{s_name} के संबंध में प्रार्थी को गैर-कानूनी रूप से प्रताड़ित किया जा रहा है।", height=80)

    if st.button("⚡ कानूनी नोटिस तैयार करें"):
        save_entry("कानूनी नोटिस", v_name, v_phone, v_city, f"दोषी: {v_acc} | धारा {sec_num}: {s_name}")
        notice = (
            "======================================================================\n"
            "आधिकारिक कानूनी विधिक शिकायत पत्र व नोटिस\n"
            f"अधिनियम: {s_act} | दिनांक: {today}\n\n"
            f"सेवा में: {s_auth}, {v_city}\n"
            f"विषय: '{v_acc}' के विरुद्ध कानूनी कार्रवाई बाबत (धारा {sec_num}: {s_name})\n\n"
            f"प्रार्थी: {v_name} (+91 {v_phone}), निवासी: {v_city}\n\n"
            f"घटना विवरण:\n{v_desc}\n\n"
            f"कानूनी आधार: {s_rule}\n\n"
            f"प्रार्थी हस्ताक्षर: {v_name}\n"
            "महा-सेवा AI राष्ट्रीय विधिक साक्षरता मिशन\n"
            "======================================================================"
        )
        st.success("🟢 कानूनी नोटिस तैयार व डेटाबेस में सुरक्षित:")
        st.text_area("नोटिस:", notice, height=180)
        st.download_button("📥 नोटिस डाउनलोड करें (.txt)", notice, file_name=f"Legal_Notice_{sec_num}.txt")
        c_print = notice.replace("\n", "<br>").replace("'", "\\'")
        p_html = f"<div style='text-align:center;'><button onclick='pDoc()' style='background:#2563EB;color:#fff;padding:10px 20px;border:none;border-radius:6px;cursor:pointer;font-weight:bold;'>🖨️ PDF प्रिंट / सेव करें</button></div><script>function pDoc(){{var w=window.open('','','width=800,height=700');w.document.write('<html><body style=\"font-family:monospace;padding:20px;\">{c_print}</body></html>');w.document.close();w.print();}}</script>"
        components.html(p_html, height=50)
        st.markdown(f"[📲 WhatsApp पर भेजें](https://wa.me/?text={urllib.parse.quote(notice)})")

# 2. WOMEN SAFETY & HOME JOBS
elif choice in [MENU_HI[2], MENU_EN[2]]:
    st.subheader("👩‍🦰 नारी शक्ति व महिला स्वावलंबन डेस्क")
    st.info("हेल्पलाइन: 1090 (महिला हेल्पलाइन) | 181 (घरेलू हिंसा) | 112 (इमरजेंसी पुलिस)")
    
    w_tab1, w_tab2 = st.tabs(["🛡️ महिला सुरक्षा व कानूनी सहायता", "🧵 घर बैठे महिला रोजगार"])
    
    with w_tab1:
        st.write("### त्वरित महिला सुरक्षा शिकायत:")
        wm_name = st.text_input("पीड़िता / बहन का नाम:")
        wm_phone = st.text_input("संपर्क नंबर:")
        wm_city = st.text_input("जिला व पता:", value="पश्चिम चंपारण")
        wm_prob = st.selectbox("समस्या का प्रकार:", ["दहेज उत्पीड़न व मारपीट", "ससुराल में प्रताड़ना", "छेड़छाड़ / पीछा करना (Stalking)", "साइबर ब्लैकमेल व फर्जी फोटो"])
        wm_details = st.text_area("सच्चा विवरण दर्ज करें:")
        if st.button("⚡ महिला सुरक्षा विधिक आवेदन बनाएं"):
            if wm_name and wm_phone:
                save_entry("महिला शिकायत", wm_name, wm_phone, wm_city, f"{wm_prob} | {wm_details}")
                wm_notice = f"महिला सुरक्षा आवेदन\nदिनांक: {today}\nसेवा में: महिला थाना प्रभारी / संरक्षण अधिकारी, {wm_city}\nविषय: {wm_prob} बाबत सुरक्षा व कानूनी कार्रवाई।\nआवेदिका: {wm_name} (+91 {wm_phone})\nविवरण: {wm_details}\nहस्ताक्षर: {wm_name}"
                st.success("आवेदन तैयार:")
                st.text_area("आवेदन पत्र:", wm_notice, height=130)
                st.markdown(f"[📲 महिला सेल को WhatsApp पर भेजें](https://wa.me/?text={urllib.parse.quote(wm_notice)})")

    with w_tab2:
        st.write("### स्वरोजगार / हुनर दर्ज करें (सिलाई, बुनाई, टिफिन):")
        w_art = st.text_input("बहन का नाम:")
        w_skill = st.selectbox("आपका काम:", ["सिलाई व बुनाई (Tailoring)", "टिफिन / होम कुकिंग", "हैंडीक्राफ्ट / ब्यूटीशियन", "होम ट्यूशन"])
        w_contact = st.text_input("ऑर्डर संपर्क नंबर:")
        if st.button("✅ महिला उद्यमी सूची में जुड़ें"):
            if w_art and w_contact:
                save_entry("महिला रोजगार", w_art, w_contact, "लोकल", w_skill)
                st.success("आपका विवरण सुरक्षित सेव हो गया है!")

# 3. SENIOR CITIZENS & BLOOD DONOR
elif choice in [MENU_HI[3], MENU_EN[3]]:
    st.subheader("🧓 बुजुर्ग सम्मान व आपातकालीन ब्लड डोनर डेस्क")
    s_tab1, s_tab2 = st.tabs(["🩸 रक्तदाता खोजें / बनें", "🧓 माता-पिता भरण-पोषण कानून"])
    
    with s_tab1:
        st.write("### इमरजेंसी ब्लड डोनर डायरेक्टरी:")
        st.markdown("• **राहुल वर्मा** — B+ Positive | 📍 पश्चिम चंपारण | [📞 कॉल](tel:9876543210)\n• **अमित कुमार** — O+ Positive | 📍 पश्चिम चंपारण | [📞 कॉल](tel:9876543211)")
        b_name = st.text_input("डोनर का नाम:")
        b_grp = st.selectbox("ब्लड ग्रुप:", ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"])
        b_num = st.text_input("डोनर फोन नंबर:")
        if st.button("🩸 ब्लड डोनर के रूप में नाम जोड़ें"):
            if b_name and b_num:
                save_entry("ब्लड डोनर", b_name, b_num, "लोकल", b_grp)
                st.success("धन्यवाद! आपका नाम आपातकालीन रक्तदाता सूची में जुड़ गया।")

    with s_tab2:
        st.info("Senior Citizens Maintenance Act: यदि बच्चे बुजुर्ग माता-पिता की देखभाल या भरण-पोषण नहीं करते, तो SDM कोर्ट द्वारा संतान से मासिक खर्चा और संपत्ति वापस दिलाने का सख्त नियम है।")
        p_name = st.text_input("बुजुर्ग माता-पिता का नाम:")
        p_phone = st.text_input("संपर्क नंबर:")
        p_child = st.text_input("संतान / बेटे का नाम:")
        p_complaint = st.text_area("समस्या (उदा: खाना-दवा न देना, घर से निकालना):")
        if st.button("⚡ SDM भरण-पोषण कोर्ट नोटिस बनाएं"):
            save_entry("बुजुर्ग भरण-पोषण", p_name, p_phone, "लोकल", f"संतान: {p_child} | समस्या: {p_complaint}")
            sn_notice = f"वरिष्ठ नागरिक भरण-पोषण आवेदन\nसेवा में: उप-जिलाधिकारी (SDM Maintenance Tribunal)\nआवेदक: {p_name} (+91 {p_phone})\nसंतान का नाम: {p_child}\nविवरण: {p_complaint}\nनियम: Senior Citizens Act 2007 के तहत मासिक गुजारा भत्ता दिलाया जाए।"
            st.text_area("तैयार नोटिस:", sn_notice, height=130)
            st.markdown(f"[📲 WhatsApp पर भेजें](https://wa.me/?text={urllib.parse.quote(sn_notice)})")

# 4. LIVE FOOD FEED
elif choice in [MENU_HI[4], MENU_EN[4]]:
    st.subheader("🔴 लाइव अन्नदाता व लंगर बुलेटिन")
    with st.expander("📢 उपलब्ध खाने की सूचना दर्ज करें (200+ पैकेट / बचा खाना)"):
        f_qty = st.text_input("खाने का विवरण (उदा: 200 पैकेट पूड़ी-सब्ज़ी):")
        f_loc = st.text_input("सटीक स्थान / होटल / शादी हॉल:", value="रेलवे स्टेशन चौक")
        f_phone = st.text_input("पिकअप फोन नंबर:", value="7484878440")
        if st.button("📢 लाइव बोर्ड पर जारी करें"):
            if f_qty and f_phone:
                save_feed(FOOD_FILE, {"Time": t_now, "Food": f_qty, "Location": f_loc, "Phone": f_phone})
                save_entry("अन्न-सेवा", "दानदाता", f_phone, f_loc, f_qty)
                st.success("खाना लाइव बोर्ड पर जुड़ गया है!")
                alert_wa = f"अन्नदाता अलर्ट! {f_qty} उपलब्ध है। स्थान: {f_loc}। कॉल: +91 {f_phone}। कृपया गाड़ी भेजकर भूखों तक पहुँचाएँ।"
                st.markdown(f"[📲 सेवा टीमों व WhatsApp ग्रुपों में भेजें](https://wa.me/?text={urllib.parse.quote(alert_wa)})")

    st.write("### 🍱 वर्तमान में उपलब्ध खाना:")
    if os.path.exists(FOOD_FILE):
        df_f = pd.read_csv(FOOD_FILE).tail(10)
        for _, r in df_f.iterrows():
            st.markdown(f"• **{r['Food']}** | 📍 {r['Location']} ({r['Time']}) — [📞 कॉल करें](tel:{r['Phone']})")
    else:
        st.info("वर्तमान में कोई खाना लिस्टेड नहीं है। ऊपर फ़ॉर्म से जोड़ें।")

# 5. LIVE JOBS & ARTISANS
elif choice in [MENU_HI[5], MENU_EN[5]]:
    st.subheader("💼 ताज़ा रोज़गार व हुनरमंद साथी बोर्ड")
    t1, t2 = st.tabs(["📢 काम / कारीगर चाहिए (Hire)", "🛠️ कारीगर सीधे कॉल करें"])
    with t1:
        j_req = st.text_input("ज़रूरत (उदा: 10 इलेक्ट्रीशियन और 5 वेल्डर चाहिए):")
        j_wage = st.text_input("दिहाड़ी (उदा: ₹600 प्रतिदिन):", value="₹600 दिहाड़ी")
        j_loc = st.text_input("कार्यस्थल पता:", value="मेन मार्केट / इंडस्ट्रियल एरिया")
        j_phone = st.text_input("मालिक / ठेकेदार नंबर:", value="7484878440")
        if st.button("📢 रोज़गार बोर्ड पर पोस्ट करें"):
            if j_req and j_phone:
                save_feed(JOBS_FILE, {"Time": t_now, "Job": j_req, "Wage": j_wage, "Location": j_loc, "Phone": j_phone})
                save_entry("रोज़गार मांग", "नियोक्ता", j_phone, j_loc, f"{j_req} | {j_wage}")
                st.success("काम लाइव बोर्ड पर दर्ज हो गया!")
                job_wa = f"रोज़गार अलर्ट! {j_req}। दिहाड़ी: {j_wage}। स्थान: {j_loc}। कॉल: +91 {j_phone}"
                st.markdown(f"[📲 WhatsApp ग्रुप में भेजें](https://wa.me/?text={urllib.parse.quote(job_wa)})")

        st.write("### 📌 ताज़ा उपलब्ध काम:")
        if os.path.exists(JOBS_FILE):
            df_j = pd.read_csv(JOBS_FILE).tail(10)
            for _, r in df_j.iterrows():
                st.ma
