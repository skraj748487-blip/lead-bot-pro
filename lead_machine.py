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

if is_en:
    UI = {
        "title": "MAHA SEVA AI — Citizen Sovereign Infrastructure",
        "sub": "28 Statutory Legal Rights • Live Jobs • Food Rescue • Merchant Tools • Factory Claims • SOS",
        "menu": ["⚖️ 28 Legal Notices", "🔴 Live Food Feed", "💼 Live Jobs & Artisans", "🏪 Merchant Desk", "🏭 Factory Injury Claim", "💊 Medicine Checker", "🚨 Night SOS"],
        "sec_prompt": "Select Legal Section (1 to 28):",
        "f_post": "📢 Post Surplus Food (200+ Packs / Food Rescue)",
        "j_post": "📢 Post Work / Hiring (Need Workers / Artisans)",
        "adm_title": "🔐 Founder Private Database (Sahil Ahmad Only)"
    }
else:
    UI = {
        "title": "महा-सेवा AI (MAHA SEVA AI)",
        "sub": "28 कानूनी अधिकार व नोटिस • लाइव अन्नदाता • ताज़ा रोज़गार • दुकानदार व्यापार • फ़ैक्ट्री क्लेम • SOS",
        "menu": ["⚖️ 28 कानूनी नोटिस", "🔴 लाइव अन्नदाता बुलेटिन", "💼 ताज़ा रोज़गार व कारीगर", "🏪 दुकानदार व्यापार डेस्क", "🏭 फैक्ट्री हादसा दावा", "💊 दवा व जेनेरिक भाव", "🚨 रात की सुरक्षा SOS"],
        "sec_prompt": "कानूनी धारा संख्या चुनें (1 से 28):",
        "f_post": "📢 उपलब्ध खाने की सूचना डालें (200 पैकेट / बचा खाना)",
        "j_post": "📢 काम / नौकरी की पोस्ट डालें (इलेक्ट्रीशियन / वेल्डर चाहिए)",
        "adm_title": "🔐 संस्थापक गुप्त एडमिन पैनल (केवल साहिल अहमद के लिए)"
    }

st.title(UI["title"])
st.caption(UI["sub"])

choice = st.radio("Menu:", UI["menu"], horizontal=True)
st.markdown("---")

SECTIONS_28 = {
    1: ("मजदूरी या वेतन चोरी", "Payment of Wages Act 1936", "लेबर कमिश्नर व डीएम", "मजदूरी दबाना गैर-कानूनी है; 10 गुना हर्जाना और 18% ब्याज का नियम।", "2 महीने का वेतन बाकी है, मांगने पर धमकी दी जा रही है।"),
    2: ("पुलिस अवैध मारपीट या फर्जी चालान", "BNSS 2023 व DK Basu Guidelines", "एसपी व मानवाधिकार आयोग", "अवैध मारपीट पर धारा 166A BNS के तहत पुलिसकर्मी पर FIR व निलंबन होता है।", "पुलिसकर्मी द्वारा अकारण अभद्रता व चालान की धमकी दी गई।"),
    3: ("अस्पताल में इमरजेंसी इलाज इनकार या शव रोकना", "Supreme Court Parmanand Katara Verdict", "CMO व स्वास्थ्य विभाग", "इमरजेंसी में पैसे के लिए इलाज से इनकार या शव रोकना संज्ञेय अपराध है।", "अस्पताल द्वारा अग्रिम राशि मांगकर इलाज में जानबूझकर देरी की गई।"),
    4: ("कार्यस्थल पर हादसा व शारीरिक अपंगता", "Employees Compensation Act 1923", "Compensation Commissioner", "हादसा होने पर ₹5 से ₹20 लाख मुआवजा व आजीवन पेंशन अनिवार्य है।", "ड्यूटी के दौरान सुरक्षा उपकरण न होने से गंभीर चोट लगी।"),
    5: ("लोन ऐप ब्लैकमेल व अवैध सूदखोरी", "RBI Fair Practices & Sec 308 BNS", "साइबर सेल व एसपी", "बिना लाइसेंस सूदखोरी और धमकी देकर वसूली करना गैर-कानूनी है।", "रिकवरी एजेंट द्वारा घर आकर गाली-गलौज व फोटो से ब्लैकमेल किया जा रहा है।"),
    6: ("सरकारी दफ्तर घूसखोरी व काम लटकाना (RTPS)", "Right to Public Services Act", "निगरानी विभाग (Vigilance)", "काम लटकाने पर कर्मचारी के वेतन से प्रतिदिन ₹250-5000 जुर्माना कटता है।", "कागजात पूरे होने पर भी रिश्वत के बिना काम नहीं किया जा रहा।"),
    7: ("दुकानदार MRP लूट व घटतौली", "Legal Metrology Act 2009", "DSO व उपभोक्ता न्यायालय", "MRP से अधिक लेना या कम तौलना गैर-कानूनी है, दुकान सील होती है।", "तय मूल्य से अधिक दाम वसूला गया और कम सामग्री दी गई।"),
    8: ("रेलवे TTE अवैध वसूली व बदसलूकी", "Indian Railway Act", "RailMadad 139 व RPF", "TTE को बदसलूकी करने या ट्रेन से धक्का देने का अधिकार नहीं है।", "यात्रा के दौरान नियम विरुद्ध पैसों की मांग व बदसलूकी की गई।"),
    9: ("थाने में FIR दर्ज न करना (Zero FIR)", "Supreme Court Lalita Kumari Directives", "SSP व CJM कोर्ट", "FIR न लिखने वाले अधिकारी पर धारा 166A BNS में खुद मुकदमा होता है।", "लिखित शिकायत देने पर भी पुलिस द्वारा FIR दर्ज नहीं की गई।"),
    10: ("पैतृक जमीन पर दबंगों का अवैध कब्जा", "Section 145/144 BNSS", "SDM व सिविल कोर्ट", "गरीब की भूमि पर कब्जे की कोशिश पर तुरंत पुलिस सुरक्षा व स्टे का नियम है।", "विपक्षी द्वारा वैध पैतृक जमीन पर जबरन कब्जे का प्रयास हो रहा है।"),
    11: ("राशन कोटेदार द्वारा राशन चोरी व मनमानी", "National Food Security Act 2013", "SDO व DSO", "राशन में कटौती करना दंडनीय अपराध है, कोटा तुरंत रद्द होता है।", "कोटेदार द्वारा निर्धारित मात्रा से कम अनाज दिया जा रहा है।"),
    12: ("बिजली विभाग द्वारा फर्जी बिल व कनेक्शन काटना", "Electricity Act 2003", "विद्युत लोकपाल व अधिशासी अभियंता", "बिना 15 दिन के वैध नोटिस के बिजली काटना पूर्णतः अवैध है।", "बिना जांच के मनमाना भारी बिल भेजकर लाइन काट दी गई।"),
    13: ("महिला घरेलू हिंसा व प्रताड़ना", "Domestic Violence Act 2005", "संरक्षण अधिकारी व महिला थाना", "महिला को सुरक्षा, भरण-पोषण और घर में रहने का पूरा कानूनी अधिकार है।", "विपक्षी द्वारा शारीरिक व मानसिक रूप से प्रताड़ित किया जा रहा है।"),
    14: ("दहेज उत्पीड़न व धमकी", "Section 85/86 BNS (498A)", "DSP व महिला सेल", "दहेज मांगना व इसके लिए प्रताड़ित करना गैर-जमानती अपराध है।", "ससुराल पक्ष द्वारा अवैध दहेज की मांग को लेकर मारपीट की जा रही है।"),
    15: ("महिला छेड़छाड़ व पीछा करना (Stalking)", "Section 78/74 BNS", "थाना प्रभारी व 1090", "किसी महिला का पीछा करना या अश्लील फब्तियां कसना दंडनीय संज्ञेय अपराध है।", "विपक्षी द्वारा लगातार पीछा कर परेशान व भयभीत किया जा रहा है।"),
    16: ("मकान मालिक द्वारा अवैध बेदखली व सामान फेंकना", "Rent Control Act & Civil Law", "SDM व सिविल जज", "बिना कोर्ट के आदेश के किराएदार का सामान फेंकना या पानी-बिजली काटना गैर-कानूनी है।", "मकान मालिक द्वारा जबरन ताला बंद कर सामान बाहर फेंकने की धमकी दी गई।"),
    17: ("सड़क दुर्घटना में हिट एंड रन व मुआवजा दावा", "Motor Vehicles Act (MACT)", "MACT ट्रिब्यूनल व SP", "सड़क दुर्घटना में सरकार व बीमा कंपनी से तुरंत मुआवजा मिलने का अधिकार है।", "लापरवाह वाहन चालक द्वारा टक्कर मारकर चोट पहुंचाई गई।"),
    18: ("ऑनलाइन साइबर फ्रॉड व बैंक खाता खाली होना", "IT Act 2000 & 1930 Helpline", "साइबर क्राइम थाना", "तुरंत 1930 पर दर्ज कराने पर बैंक खाता तुरंत फ्रीज होकर पैसा वापस होता है।", "फर्जी कॉल/लिंक के जरिए खाते से अवैध रूप से राशि निकाल ली गई।"),
    19: ("निजी स्कूल द्वारा अवैध फीस वसूली व टीसी रोकना", "Right to Education Act 2009", "जिला बेसिक शिक्षा अधिकारी (BSA)", "फीस के नाम पर छात्र की टीसी (TC) रोकना या परीक्षा से वंचित करना अपराध है।", "स्कूल प्रशासन द्वारा मनमानी फीस मांगकर टीसी देने से इनकार किया जा रहा है।"),
    20: ("बैंक एजेंट द्वारा अवैध लोन रिकवरी व धमकी", "RBI Fair Practice Code", "Banking Ombudsman व SP", "सुबह 8 से पहले और शाम 7 के बाद रिकवरी कॉल या घर पर गाली-गलौज वर्जित है।", "बैंक एजेंट द्वारा फोन पर गालियां व सामाजिक बदनामी की धमकी दी जा रही है।"),
    21: ("ठेकेदार द्वारा ईपीएफ (EPF) व पीएफ चोरी", "EPF & MP Act 1952", "PF कमिश्नर (RPFC)", "वेतन से पीएफ काटकर पीएफ खाते में न डालना संज्ञेय अपराध व गबन है।", "कंपनी द्वारा सैलरी से पीएफ काटा गया परंतु खाते में जमा नहीं किया गया।"),
    22: ("जातिसूचक गाली-गलौज व सामाजिक बहिष्कार", "SC/ST Prevention of Atrocities Act", "DSP (SC/ST सेल)", "जातिसूचक अपमान पर तुरंत गैर-जमानती धाराओं में गिरफ्तारी का नियम है।", "विपक्षी द्वारा सार्वजनिक रूप से अपमानित कर धमकियां दी गईं।"),
    23: ("वारंटी में खराब सामान बदलने से कंपनी का इनकार", "Consumer Protection Act 2019", "उपभोक्ता आयोग (DCDRC)", "वारंटी अवधि में खराब उत्पाद न बदलना या रिफंड न देना सेवा में गंभीर दोष है।", "वारंटी में होने के बावजूद कंपनी द्वारा सामान ठीक या रिप्लेस नहीं किया जा रहा।"),
    24: ("नगर निगम/पंचायत द्वारा गंदगी व नाली जाम", "Municipal Corporation Act", "नगर आयुक्त व DM", "साफ-सफाई व जन-स्वास्थ्य की सुरक्षा स्थानीय निकाय की अनिवार्य कानूनी जिम्मेदारी है।", "बार-बार शिकायत के बावजूद नाली जाम व गंदगी की सफाई नहीं की गई।"),
    25: ("सार्वजनिक रास्ते पर दबंगों द्वारा अवैध रुकावट", "Section 152 BNSS", "तहसीलदार व SDM", "आम रास्ते को अवरुद्ध करना सार्वजनिक न्यूसेंस है, प्रशासन तुरंत हटाएगा।", "विपक्षी द्वारा आम रास्ते पर दीवार/बाड़ लगाकर आवागमन रोक दिया गया है।"),
    26: ("अवैध ध्वनि प्रदूषण व रात 10 बजे बाद डीजे", "Noise Pollution Rules 2000", "प्रदूषण नियंत्रण बोर्ड व 112", "रात 10 बजे के बाद लाउडस्पीकर/डीजे बजाना सुप्रीम कोर्ट के आदेश का उल्लंघन है।", "रात के समय अत्यधिक तेज आवाज में डीजे बजाकर शांति भंग की जा रही है।"),
    27: ("बाल मजदूरी व बच्चों से खतरनाक काम कराना", "Child Labour Prohibition Act", "श्रम प्रवर्तन अधिकारी व CWC", "14 वर्ष से कम उम्र के बच्चे से काम कराना गैर-कानूनी है, जेल का नियम है।", "संस्थान द्वारा नाबालिग बच्चे से अवैध रूप से जोखिम भरा कार्य कराया जा रहा है।"),
    28: ("आरटीआई (RTI) सूचना देने से अधिकारी का इनकार", "Right to Information Act 2005", "राज्य सूचना आयोग", "30 दिन में सूचना न देने पर जनसूचना अधिकारी पर ₹25,000 तक जुर्माना लगता है।", "आवेदन के 30 दिन बीत जाने पर भी मांगी गई सरकारी सूचना उपलब्ध नहीं कराई गई।")
}

# 1. 28 LEGAL NOTICES
if choice == UI["menu"][0]:
    st.subheader("⚖️ 28 आधिकारिक कानूनी नोटिस जनरेटर")
    sec_num = st.number_input(UI["sec_prompt"], min_value=1, max_value=28, value=1, step=1)
    s_name, s_act, s_auth, s_rule, s_det = SECTIONS_28[sec_num]
    
    st.info(f"📌 धारा {sec_num}: {s_name}\n\nलागू कानून: {s_act} | सक्षम प्राधिकारी: {s_auth}")
    
    c1, c2 = st.columns(2)
    v_name = c1.text_input("प्रार्थी का नाम:", value="साहिल कुमार")
    v_city = c2.text_input("जिला व राज्य:", value="पश्चिम चंपारण, बिहार")
    v_phone = st.text_input("मोबाइल नंबर:", value="7484878440")
    v_acc = st.text_input("दोषी पक्ष / अधिकारी का नाम:", value="संबंधित दोषी पक्ष")
    v_desc = st.text_area("घटनाक्रम का सच्चा विवरण:", value=s_det, height=80)
    
    if st.button("⚡ आधिकारिक कानूनी नोटिस तैयार करें"):
        save_entry("कानूनी नोटिस", v_name, v_phone, v_city, f"दोषी: {v_acc} | धारा {sec_num}: {s_name}")
        notice = (
            "======================================================================\n"
            "आधिकारिक कानूनी विधिक शिकायत पत्र व नोटिस\n"
            f"अधिनियम: {s_act} | दिनांक: {today}\n\n"
            f"सेवा में: {s_auth}, {v_city}\n"
            f"विषय: '{v_acc}' के विरुद्ध कानूनी कार्रवाई बाबत (धारा {sec_num}: {s_name})\n\n"
            f"प्रार्थी: {v_name} (+91 {v_phone}), निवासी: {v_city}\n\n"
            f"घटना का विवरण:\n{v_desc}\n\n"
            f"कानूनी आधार व नियम:\n{s_rule}\n\n"
            f"प्रार्थी हस्ताक्षर: {v_name}\n"
            "महा-सेवा AI राष्ट्रीय विधिक साक्षरता मिशन\n"
            "======================================================================"
        )
        st.success("🟢 कानूनी नोटिस तैयार और डेटाबेस में सुरक्षित:")
        st.text_area("तैयार नोटिस:", notice, height=180)
        st.download_button("📥 नोटिस डाउनलोड करें (.txt)", notice, file_name=f"Legal_Notice_Sec_{sec_num}.txt")
        
        c_print = notice.replace("\n", "<br>").replace("'", "\\'")
        p_html = f"<div style='text-align:center;'><button onclick='pDoc()' style='background:#2563EB;color:#fff;padding:10px 20px;border:none;border-radius:6px;cursor:pointer;font-weight:bold;'>🖨️ PDF प्रिंट / सेव करें</button></div><script>function pDoc(){{var w=window.open('','','width=800,height=700');w.document.write('<html><body style=\"font-family:monospace;padding:20px;\">{c_print}</body></html>');w.document.close();w.print();}}</script>"
        components.html(p_html, height=50)
        st.markdown(f"[📲 यह नोटिस WhatsApp पर भेजें](https://wa.me/?text={urllib.parse.quote(notice)})")

# 2. LIVE FOOD FEED
elif choice == UI["menu"][1]:
    st.subheader("🔴 लाइव अन्नदाता व लंगर बुलेटिन")
    st.caption("शहर में कहाँ कितना खाना उपलब्ध है — सीधे कॉल करें और भूखों तक पहुँचाएँ:")
    
    with st.expander(UI["f_post"]):
        f_qty = st.text_input("खाने का विवरण (उदा: 200 पैकेट पूड़ी-सब्ज़ी / 50 प्लेट खाना):")
        f_loc = st.text_input("सटीक स्थान / होटल / शादी हॉल:", value="रेलवे स्टेशन चौक")
        f_phone = st.text_input("पिकअप संपर्क नंबर:", value="7484878440")
        if st.button("📢 लाइव बोर्ड पर जारी करें"):
            if f_qty and f_phone:
                feed_data = {"Time": t_now, "Food": f_qty, "Location": f_loc, "Phone": f_phone}
                save_feed(FOOD_FILE, feed_data)
                save_entry("अन्न-सेवा", "दानदाता", f_phone, f_loc, f_qty)
                st.success("खाना लाइव बोर्ड पर जुड़ गया है!")
                alert_wa = f"अन्नदाता अलर्ट! {f_qty} उपलब्ध है। स्थान: {f_loc}। कॉल: +91 {f_phone}। कृपया गाड़ी भेजकर भूखों तक पहुँचाएँ।"
                st.markdown(f"[📲 सेवा टीमों व WhatsApp ग्रुपों में भेजें](https://wa.me/?text={urllib.parse.quote(alert_wa)})")

    st.write("### 🍱 वर्तमान में उपलब्ध खाना:")
    if os.path.exists(FOOD_FILE):
        df_f = pd.read_csv(FOOD_FILE).tail(10)
        for _, r in df_f.iterrows():
            st.markdown(f"• **{r['Food']}** | 📍 {r['Location']} (समय: {r['Time']}) — [📞 तुरंत कॉल करें](tel:{r['Phone']})")
    else:
        st.info("वर्तमान में कोई खाना लिस्टेड नहीं है। ऊपर फ़ॉर्म से जोड़ें।")

# 3. LIVE JOBS & ARTISANS
elif choice == UI["menu"][2]:
    st.subheader("💼 ताज़ा रोज़गार व हुनरमंद साथी बोर्ड")
    st.caption("सीधे दिहाड़ी व नौकरी — बीच में कोई दलाल या ठेकेदार नहीं:")
    
    t1, t2 = st.tabs(["📢 काम / कारीगर चाहिए (Hire)", "🛠️ कारीगर सीधे कॉल करें"])
    
    with t1:
        st.write("### नई ज़रूरत पोस्ट करें:")
        j_req = st.text_input("ज़रूरत (उदा: 10 इलेक्ट्रीशियन और 5 वेल्डर चाहिए):")
        j_wage = st.text_input("दिहाड़ी / वेतन (उदा: ₹600 प्रतिदिन / भोजन सहित):", value="₹600 दिहाड़ी")
        j_loc = st.text_input("कार्यस्थल का पता:", value="मेन मार्केट / इंडस्ट्रियल एरिया")
        j_phone = st.text_input("मालिक / ठेकेदार का नंबर:", value="7484878440")
        if st.button("📢 रोज़गार बोर्ड पर पोस्ट करें"):
            if j_req and j_phone:
                job_data = {"Time": t_now, "Job": j_req, "Wage": j_wage, "Location": j_loc, "Phone": j_phone}
                save_feed(JOBS_FILE, job_data)
                save_entry("रोज़गार मांग", "नियोक्ता", j_phone, j_loc, f"{j_req} | {j_wage}")
                st.success("काम लाइव बोर्ड पर दर्ज हो गया!")
                job_wa = f"रोज़गार अलर्ट! {j_req}। दिहाड़ी: {j_wage}। स्थान: {j_loc}। सीधे कॉल करें: +91 {j_phone}"
                st.markdown(f"[📲 मिस्त्री भाइयों के WhatsApp ग्रुप में भेजें](https://wa.me/?text={urllib.parse.quote(job_wa)})")

        st.write("### 📌 ताज़ा उपलब्ध काम:")
        if os.path.exists(JOBS_FILE):
            df_j = pd.read_csv(JOBS_FILE).tail(10)
            for _, r in df_j.iterrows():
                st.markdown(f"• **{r['Job']}** ({r['Wage']}) | 📍 {r['Location']} — [📞 सीधे काम पकड़ें](tel:{r['Phone']})")
        else:
            st.info("वर्तमान में कोई काम लिस्टेड नहीं है। ऊपर से पोस्ट करें।")

    with t2:
        st.write("### 📞 सीधे मिस्त्री / कारीगर को कॉल करें:")
        st.markdown("• **अकबर अली** — वेल्डर (गेट/ग्रिल) | 📍 पश्चिम चंपारण | [📞 कॉल](tel:9876543210)\n• **राकेश शर्मा** — इलेक्ट्रीशियन (वायरिंग/मोटर) | 📍 पश्चिम चंपारण | [📞 कॉल](tel:9876543211)\n• **मोहम्मद सलीम** — प्लंबर (नल फिटिंग) | 📍 पश्चिम चंपारण | [📞 कॉल](tel:9876543212)")
        st.markdown("---")
        k_name = st.text_input("नया कारीगर अपना नाम जोड़ें:")
        k_trade = st.selectbox("हुनर:", ["वेल्डर", "प्लंबर", "इलेक्ट्रीशियन", "राजमिस्त्री", "बढ़ई"])
        k_mob = st.text_input("मोबाइल नंबर:")
        if st.button("✅ डायरेक्टरी में दर्ज करें"):
            if k_name and k_mob:
                save_entry("कारीगर", k_name, k_mob, "लोकल", k_trade)
                st.success("आपका नंबर संस्थापक के डेटाबेस में सुरक्षित सेव हो गया!")

# 4. MERCHANT DESK
elif choice == UI["menu"][3]:
    st.subheader("🏪 स्थानीय दुकानदार व्यापार डेस्क (Vyapar Tool)")
    st.caption("दुकानदारों के लिए बिना कमीशन बिक्री व उधारी वसूली का डिजिटल समाधान:")
    
    m_tool = st.radio("टूल चुनें:", ["⚡ Near-Expiry / सस्ता सामान निकालें", "📲 WhatsApp उधारी तकादा रिमाइंडर"])
    
    if m_tool == "⚡ Near-Expiry / सस्ता सामान निकालें":
        st.write("### फँसा हुआ स्टॉक 40-50% छूट पर बेचें:")
        item_name = st.text_input("सामान का नाम व मात्रा (उदा: 20 पैकेट रिफाइंड तेल / आटा):")
        item_disc = st.text_input("छूट मूल्य (उदा: MRP ₹150, ऑफर भाव ₹90):")
        shop_name = st.text_input("दुकान का नाम व पता:", value="गुप्ता किराना स्टोर, मेन रोड")
        shop_phone = st.text_input("दुकानदार फोन नंबर:", value="7484878440")
        if st.button("📢 सस्ता ऑफर ग्राहकों को भेजें"):
            save_entry("दुकानदार ऑफर", shop_name, shop_phone, "लोकल", f"{item_name} @ {item_disc}")
            offer_wa = f"किराना महा-छूट अलर्ट! {shop_name} पर {item_name} भारी छूट पर उपलब्ध: {item_disc}। संपर्क करें: +91 {shop_phone}"
            st.success("ऑफ़र तैयार है!")
            st.markdown(f"[📲 ग्राहकों के WhatsApp पर शेयर करें](https://wa.me/?text={urllib.parse.quote(offer_wa)})")
            
    else:
        st.write("### सम्मानजनक तरीक़े से उधारी का तकादा भेजें:")
        cust_name = st.text_input("ग्राहक का नाम:")
        cust_phone = st.text_input("ग्राहक का मोबाइल नंबर:")
        due_amt = st.text_input("बकाया राशि (₹):", value="1500")
        my_shop = st.text_input("आपकी दुकान का नाम:", value="साहिल ट्रेडर्स")
        if st.button("⚡ WhatsApp रिमाइंडर तैयार करें"):
            rem_wa = f"नमस्ते {cust_name} जी, {my_shop} पर आपका पिछला ₹{due_amt} का हिसाब बाकी है। कृपया सुविधानुसार भुगतान कराने का कष्ट करें। धन्यवाद!"
            st.markdown(f"[📲 ग्राहक को उधारी रिमाइंडर भेजें](https://wa.me/91{cust_phone}?text={urllib.parse.quote(rem_wa)})")

# 5. FACTORY ACCIDENT CLAIM
elif choice == UI["menu"][4]:
    st.subheader("🏭 कंपनी/फ़ैक्ट्री हादसा व क़ानूनी मुआवज़ा दावा")
    st.info("Employees' Compensation Act 1923: ड्यूटी पर चोट लगने पर 100% इलाज, छुट्टी की तनख्वाह व ₹3 से ₹20 लाख मुआवज़ा मिलना तय है।")

    c1, c2 = st.columns(2)
    w_name = c1.text_input("मज़दूर / पीड़ित का नाम:", value="साहिल कुमार")
    w_city = c2.text_input("जिला व राज्य:", value="पश्चिम चंपारण, बिहार")
    w_phone = st.text_input("मोबाइल नंबर:", value="7484878440")
    w_comp = st.text_input("कंपनी / फ़ैक्ट्री का नाम व पता:", value="ABC Manufacturing Pvt. Ltd.")
    w_post = st.text_input("पद (ऑपरेटर / वेल्डर / हेल्पर):", value="मशीन ऑपरेटर")
    w_time = st.text_input("हादसे का समय:", value=f"{today}, सुबह 11:30 बजे")
    w_inj = st.text_area("चोट का विवरण:", value="मशीन में गार्ड न होने से हाथ में गंभीर चोट व फ्रैक्चर।")
    w_ev = st.text_area("मौजूद सबूत:", value="अस्पताल MLC पर्ची, ड्यूटी गेट पास, सीसीटीवी फुटेज व साथी मज़दूर गवाह।")

    if st.button("⚡ मुआवज़ा दावा नोटिस तैयार करें"):
        save_entry("Accident Claim", w_name, w_phone, w_city, f"{w_comp} | {w_inj}")
        cl_notice = (
            "======================================================================\n"
            "STATUTORY WORKPLACE INJURY & COMPENSATION NOTICE\n"
            "(Under Section 10, Employees Compensation Act 1923 & ESI Act)\n"
            f"Date: {today}\n\n"
            f"To: 1. Management, {w_comp}\n2. Compensation Commissioner / Labour Court, {w_city}\n\n"
            f"Subject: Immediate Cashless Treatment & Statutory Compensation for {w_name}\n\n"
            f"I, {w_name} (+91 {w_phone}), working as '{w_post}' at {w_comp}, state:\n"
            f"1. OCCURRENCE: On {w_time}, sustained injury on duty: {w_inj}\n"
            f"2. EVIDENCE: {w_ev}\n"
            "3. DEMAND: Bear 100% medical expenses and deposit statutory compensation under Section 4 within 30 days.\n\n"
