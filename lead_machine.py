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

MENU_HI = ["⚖️ 28 कानूनी नोटिस", "🔴 लाइव अन्नदाता बुलेटिन", "💼 ताज़ा रोज़गार व कारीगर", "🏪 दुकानदार व्यापार डेस्क", "🏭 फैक्ट्री हादसा दावा", "💊 दवा व जेनेरिक भाव", "🚨 रात की सुरक्षा SOS"]
MENU_EN = ["⚖️ 28 Legal Notices", "🔴 Live Food Feed", "💼 Live Jobs & Artisans", "🏪 Merchant Desk", "🏭 Factory Injury Claim", "💊 Medicine Checker", "🚨 Night SOS"]

menu_items = MENU_EN if is_en else MENU_HI

st.title("MAHA SEVA AI — महा-सेवा AI" if is_en else "महा-सेवा AI (MAHA SEVA AI)")
st.caption("28 Statutory Legal Rights • Live Jobs • Food Rescue • Merchant Tools • Factory Claims • SOS")

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

# 1. 28 LEGAL NOTICES
if choice in [MENU_HI[0], MENU_EN[0]]:
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

# 2. LIVE FOOD FEED
elif choice in [MENU_HI[1], MENU_EN[1]]:
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

# 3. LIVE JOBS & ARTISANS
elif choice in [MENU_HI[2], MENU_EN[2]]:
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
                st.markdown(f"• **{r['Job']}** ({r['Wage']}) | 📍 {r['Location']} — [📞 काम पकड़ें](tel:{r['Phone']})")
        else:
            st.info("वर्तमान में कोई काम लिस्टेड नहीं है।")

    with t2:
        st.markdown("• **अकबर अली** — वेल्डर | 📍 पश्चिम चंपारण | [📞 कॉल](tel:9876543210)\n• **राकेश शर्मा** — इलेक्ट्रीशियन | 📍 पश्चिम चंपारण | [📞 कॉल](tel:9876543211)\n• **मोहम्मद सलीम** — प्लंबर | 📍 पश्चिम चंपारण | [📞 कॉल](tel:9876543212)")
        st.markdown("---")
        k_name = st.text_input("कारीगर नाम दर्ज करें:")
        k_trade = st.selectbox("हुनर:", ["वेल्डर", "प्लंबर", "इलेक्ट्रीशियन", "राजमिस्त्री", "बढ़ई"])
        k_mob = st.text_input("मोबाइल नंबर:")
        if st.button("✅ डायरेक्टरी में दर्ज करें"):
            if k_name and k_mob:
                save_entry("कारीगर", k_name, k_mob, "लोकल", k_trade)
                st.success("डेटा संस्थापक के डेटाबेस में सुरक्षित सेव हो गया!")

# 4. MERCHANT DESK
elif choice in [MENU_HI[3], MENU_EN[3]]:
    st.subheader("🏪 स्थानीय दुकानदार व्यापार डेस्क")
    m_tool = st.radio("विकल्प चुनें:", ["⚡ Near-Expiry / सस्ता सामान निकालें", "📲 WhatsApp उधारी तकादा रिमाइंडर"])
    if m_tool == "⚡ Near-Expiry / सस्ता सामान निकालें":
        item_name = st.text_input("सामान का नाम व मात्रा (उदा: 20 पैकेट तेल / आटा):")
        item_disc = st.text_input("छूट भाव (उदा: MRP ₹150, ऑफर ₹90):")
        shop_name = st.text_input("दुकान का नाम व पता:", value="गुप्ता किराना स्टोर")
        shop_phone = st.text_input("दुकानदार फोन नंबर:", value="7484878440")
        if st.button("📢 सस्ता ऑफर ग्राहकों को भेजें"):
            save_entry("दुकानदार ऑफर", shop_name, shop_phone, "लोकल", f"{item_name} @ {item_disc}")
            offer_wa = f"किराना महा-छूट! {shop_name} पर {item_name} भारी छूट पर: {item_disc}। संपर्क: +91 {shop_phone}"
            st.markdown(f"[📲 ग्राहकों के WhatsApp पर शेयर करें](https://wa.me/?text={urllib.parse.quote(offer_wa)})")
    else:
        cust_name = st.text_input("ग्राहक का नाम:")
        cust_phone = st.text_input("ग्राहक का मोबाइल नंबर:")
        due_amt = st.text_input("बकाया राशि (₹):", value="1500")
        my_shop = st.text_input("दुकान का नाम:", value="साहिल ट्रेडर्स")
        if st.button("⚡ WhatsApp रिमाइंडर तैयार करें"):
            rem_wa = f"नमस्ते {cust_name} जी, {my_shop} पर आपका पिछला ₹{due_amt} का हिसाब बाकी है। कृपया सुविधानुसार भुगतान कराने का कष्ट करें। धन्यवाद!"
            st.markdown(f"[📲 ग्राहक को उधारी रिमाइंडर भेजें](https://wa.me/91{cust_phone}?text={urllib.parse.quote(rem_wa)})")

# 5. FACTORY ACCIDENT CLAIM
elif choice in [MENU_HI[4], MENU_EN[4]]:
    st.subheader("🏭 कंपनी/फ़ैक्ट्री हादसा व क़ानूनी मुआवज़ा दावा")
    st.info("Employees Compensation Act 1923: ड्यूटी पर चोट लगने पर 100% इलाज, पूरी छुट्टी का वेतन और ₹3-20 लाख कानूनी मुआवजा मिलना अनिवार्य है।")
    w_name = st.text_input("मज़दूर / पीड़ित का नाम:", value="साहिल कुमार")
    w_city = st.text_input("जिला व राज्य:", value="पश्चिम चंपारण, बिहार")
    w_phone = st.text_input("मोबाइल नंबर:", value="7484878440")
    w_comp = st.text_input("कंपनी / फ़ैक्ट्री नाम व पता:", value="ABC Manufacturing Pvt. Ltd.")
    w_post = st.text_input("पद (ऑपरेटर / वेल्डर / हेल्पर):", value="मशीन ऑपरेटर")
    w_time = st.text_input("हादसे का समय:", value=f"{today}, सुबह 11:30 बजे")
    w_inj = st.text_area("चोट का विवरण:", value="मशीन में सुरक्षा गार्ड न होने से हाथ में गंभीर चोट व फ्रैक्चर।")
    w_ev = st.text_area("मौजूद सबूत:", value="अस्पताल MLC पर्ची, ड्यूटी गेट पास, सीसीटीवी फुटेज व साथी मज़दूर गवाह।")
    if st.button("⚡ मुआवज़ा दावा नोटिस तैयार करें"):
        save_entry("Accident Claim", w_name, w_phone, w_city, f"{w_comp} | {w_inj}")
        cl_notice = (
            "STATUTORY WORKPLACE INJURY & COMPENSATION NOTICE\n"
            f"(Under Section 10, Employees Compensation Act 1923)\nDate: {today}\n\n"
            f"To: 1. Management, {w_comp}\n2. Compensation Commissioner / Labour Court, {w_city}\n\n"
            f"Subject: Immediate Cashless Treatment & Statutory Compensation for {w_name}\n\n"
            f"Worker: {w_name} (+91 {w_phone}), Post: {w_post}\n"
            f"Incident: On {w_time}, sustained injury: {w_inj}\n"
            f"Evidence: {w_ev}\n"
            "Demand: 100% medical expenses, full salary and deposit statutory compensation under Section 4 within 30 days.\n\n"
            f"Signature: {w_name}\n"
        )
        st.success("🟢 दावा नोटिस तैयार व सुरक्षित सेव:")
        st.text_area("Claim Notice:", cl_notice, height=180)
        st.download_button("📥 डाउनलोड क्लेम (.txt)", cl_notice, file_name="Accident_Claim.txt")
        c_cl = cl_notice.replace("\n", "<br>").replace("'", "\\'")
        cp_html = f"<div style='text-align:center;'><button onclick='pDoc()' style='background:#2563EB;color:#fff;padding:10px 20px;border:none;border-radius:6px;cursor:pointer;font-weight:bold;'>🖨️ PDF प्रिंट / सेव करें</button></div><script>function pDoc(){{var w=window.open('','','width=800,height=700');w.document.write('<html><body style=\"font-family:monospace;padding:20px;\">{c_cl}</body></html>');w.document.close();w.print();}}</script>"
        components.html(cp_html, height=50)
        st.markdown(f"[📲 WhatsApp पर भेजें](https://wa.me/?text={urllib.parse.quote(cl_notice)})")

# 6. MEDICINE CHECKER
elif choice in [MENU_HI[5], MENU_EN[5]]:
    st.subheader("💊 दवा जानकारी व जन औषधि सस्ता विकल्प")
    st.write("एम्बुलेंस: **108** | प्रसूति सेवा: **102**")
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

# 7. NIGHT SOS
elif choice in [MENU_HI[6], MENU_EN[6]]:
    st.subheader("🚨 24x7 रात की सुरक्षा व लाइव GPS SOS")
    st.write("पुलिस: **112** | महिला हेल्पलाइन: **1090**")
    g_html = "<div style='text-align:center;'><button onclick='fPos()' style='background:#10B981;color:#fff;padding:10px;border:none;border-radius:6px;font-weight:bold;cursor:pointer;'>📡 लाइव GPS निकालें</button><p id='g_res' style='color:#38BDF8;font-size:12px;'></p></div><script>function fPos(){navigator.geolocation.getCurrentPosition(function(p){document.getElementById('g_res').innerHTML='https://maps.google.com/?q='+p.coords.latitude+','+p.coords.longitude;});}</script>"
    components.html(g_html, height=75)
    sos_name = st.text_input("पीड़ित का नाम:", value="साहिल")
    sos_road = st.text_input("सड़क / चौराहा:", value="मेन रोड")
    st.markdown(f"[📲 परिवार को WhatsApp SOS भेजें](https://wa.me/{WA_NUM}?text={urllib.parse.quote(f'EMERGENCY SOS! Name: {sos_name}. Location: {sos_road}. Time: {t_now}.')})")

# ADMIN PANEL
st.markdown("---")
with st.expander("🔐 संस्थापक गुप्त एडमिन पैनल (केवल साहिल अहमद के लिए)"):
    adm_pass = st.text_input("पासवर्ड डालें:", type="password")
    if adm_pass == "sahil786":
        st.success("🟢 स्वागत है साहिल भाई! आपका केंद्रीय डेटाबेस सक्रिय है:")
        if os.path.exists(DB_NAME):
            df_v = pd.read_csv(DB_NAME)
            st.dataframe(df_v, use_container_width=True)
            st.download_button("📥 संपूर्ण एक्सेल डेटाबेस डाउनलोड करें", df_v.to_csv(index=False).encode('utf-8'), file_name="Maha_Seva_Master.csv", mime="text/csv")
        else:
            st.info("डेटाबेस अभी खाली है।")
    elif adm_pass:
        st.error("गलत पासवर्ड!")

st.markdown("---")
st.write("🏛️ **संस्थापक:** साहिल अहमद (Sahil Ahmad) • महा-सेवा AI")
st.markdown(f"[💬 संस्थापक WhatsApp संपर्क (+91 7484878440)](https://wa.me/{WA_NUM})")
