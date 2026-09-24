import streamlit as st
import streamlit.components.v1 as components
import urllib.parse
from datetime import datetime
import pandas as pd
import os

st.set_page_config(page_title="महा-सेवा AI / Maha Seva AI", page_icon="🇮🇳", layout="centered", initial_sidebar_state="collapsed")

# 🔒 गिटहब लोगो, एडिट बटन, तीन डॉट मेन्यू और वॉटरमार्क हमेशा के लिए गायब करने का CSS
st.markdown("""
<style>
#MainMenu {visibility: hidden !important; display: none !important;}
header {visibility: hidden !important; display: none !important;}
footer {visibility: hidden !important; display: none !important;}
.viewerBadge_container__1QSob {display: none !important;}
.stAppDeployButton {display: none !important;}
[data-testid="stToolbar"] {display: none !important;}
[data-testid="stHeader"] {display: none !important;}
</style>
""", unsafe_allow_html=True)

WA_NUM = "917484878440"
today = datetime.now().strftime("%d-%m-%Y")
t_now = datetime.now().strftime("%I:%M %p")
DB_NAME = "maha_seva_data.csv"
JOBS_FILE = "live_jobs.csv"
FOOD_FILE = "live_food.csv"

def save_entry(c_type, name, phone, city, details):
    row = {"Date": today, "Time": t_now, "Type": c_type, "Name": name, "Phone": str(phone), "City": city, "Details": details}
    df = pd.DataFrame([row])
    df.to_csv(DB_NAME, mode='a' if os.path.exists(DB_NAME) else 'w', header=not os.path.exists(DB_NAME), index=False)

def save_feed(file_path, row_dict):
    df = pd.DataFrame([row_dict])
    df.to_csv(file_path, mode='a' if os.path.exists(file_path) else 'w', header=not os.path.exists(file_path), index=False)

LANGS = ["🇮🇳 हिन्दी", "🇬🇧 English"]
c_lang = st.radio("🌐 भाषा / Language:", LANGS, horizontal=True)
is_en = (c_lang == "🇬🇧 English")

MENU_HI = [
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

MENU_EN = [
    "💼 Live Jobs (Engineers/Artisans/Helpers)",
    "🌙 Zakat, Sadaqah & Direct Aid Desk",
    "🔴 Live Food & Annadata Feed", 
    "🕊️ Anti-Caste & Brotherhood Shield",
    "⚖️ 28 Statutory Legal Notices", 
    "👩‍🦰 Women Safety & Home Jobs",
    "🧓 Senior Care & Emergency Blood Donor",
    "🌾 Farmer Mandi & Driver Transport",
    "🏪 Local Merchant & Shopkeeper Desk", 
    "🏭 Factory Accident Compensation Claim", 
    "💊 Medicine & Generic Price Checker", 
    "🚨 24x7 Night Safety & Live GPS SOS"
]

menu_items = MENU_EN if is_en else MENU_HI

st.title("MAHA SEVA AI — महा-सेवा AI" if is_en else "🇮🇳 महा-सेवा AI (MAHA SEVA AI)")
st.caption("100% Humanity, 0% Discrimination • Every Hand Deserves Work, No One Sleeps Hungry" if is_en else "अखंड भारत जन-कल्याण • 100% इंसानियत, 0% जात-पात • हर हाथ को काम, कोई भूखा न सोए")

choice = st.radio("Select Service / सेवा चुनें:", menu_items, horizontal=True)
st.markdown("---")

LAW_28 = [
    "Wage Theft / मजदूरी चोरी (Payment of Wages Act 1936)", "Illegal Police Beating / पुलिस अवैध मारपीट (BNSS 2023 / DK Basu)", 
    "Hospital Emergency Denial / अस्पताल इलाज इनकार (SC Parmanand Katara)", "Workplace Injury Claim / कार्यस्थल हादसा मुआवज़ा (Employees Comp Act 1923)",
    "Loan App Harassment / लोन ऐप ब्लैकमेल (RBI Guidelines / Sec 308 BNS)", "Govt Office Delay / सरकारी घूसखोरी (RTPS Act)",
    "MRP Overcharge / MRP लूट व घटतौली (Legal Metrology Act)", "Railway TTE Extortion / रेलवे TTE अवैध वसूली (Indian Railway Act)",
    "Police Refusing FIR / थाने में FIR न लिखना (SC Lalita Kumari Directives)", "Land Grab / ज़मीन पर अवैध क़ब्ज़ा (Sec 145/144 BNSS)",
    "Ration Theft / राशन कोटेदार चोरी (National Food Security Act)", "Wrong Electricity Bill / बिजली फ़र्ज़ी बिल (Electricity Act 2003)",
    "Domestic Violence / महिला घरेलू हिंसा (Domestic Violence Act 2005)", "Dowry Harassment / दहेज उत्पीड़न (Sec 85/86 BNS)",
    "Stalking / महिला छेड़छाड़ व पीछा करना (Sec 78/74 BNS)", "Illegal Eviction / मकान मालिक अवैध बेदखली (Rent Control Act)",
    "Road Accident Claim / सड़क दुर्घटना दावा (Motor Vehicles Act)", "Online Cyber Fraud / बैंक साइबर फ्रॉड (IT Act & 1930)",
    "School Illegal Fee / स्कूल फ़ीस व TC रोकना (RTE Act 2009)", "Recovery Agent Harassment / बैंक एजेंट धमकी (RBI Fair Code)",
    "EPF Theft / ठेकेदार PF चोरी (EPF Act 1952)", "Casteist Slurs / जातिसूचक गाली व अपमान (SC/ST Prevention Act)",
    "Warranty Refusal / वारंटी में सामान न बदलना (Consumer Protection Act)", "Drain Overflow / गंदगी व नाली जाम (Municipal Act)",
    "Road Blocking / सार्वजनिक रास्ते पर रुकावट (Sec 152 BNSS)", "Night DJ Noise / रात में तेज आवाज़ डीजे (Noise Rules 2000)",
    "Child Labour / बाल मज़दूरी (Child Labour Act)", "RTI Denial / RTI सूचना न देना (RTI Act 2005)"
]

# 1. LIVE JOBS
if choice in [MENU_HI[0], MENU_EN[0]]:
    st.subheader("💼 " + ("Live Job Board (Every Hand Gets Work)" if is_en else "अखंड भारत रोज़गार बोर्ड (हर हाथ को काम)"))
    t1, t2 = st.tabs(["📢 " + ("Hire Workforce / Post Job" if is_en else "काम / स्टाफ चाहिए (Hire)"), "🛠️ " + ("Job Seekers Directory" if is_en else "काम खोजने वाले साथी")])
    with t1:
        j_cat = st.selectbox("Category / श्रेणी:", ["Site Engineer", "Safety Officer", "Supervisor", "Welder/Fitter", "Electrician/Plumber", "Mason", "Helper/Labor", "Tailoring/Cooking"])
        j_req = st.text_input("Job Requirement / काम का विवरण (उदा: 2 वेल्डर चाहिए):")
        j_wage = st.text_input("Wage / वेतन या दिहाड़ी (उदा: ₹600 प्रतिदिन):")
        j_loc = st.text_input("Work Location / कार्यस्थल का पता:")
        j_phone = st.text_input("Employer Contact / काम देने वाले का मोबाइल नंबर:")
        if st.button("📢 " + ("Post Job on Live Feed" if is_en else "रोज़गार बोर्ड पर पोस्ट करें")):
            if j_req and j_phone:
                save_feed(JOBS_FILE, {"Time": t_now, "Category": j_cat, "Job": j_req, "Wage": j_wage, "Location": j_loc, "Phone": j_phone})
                save_entry("Job Post", "Employer", j_phone, j_loc, f"{j_cat} | {j_req} | {j_wage}")
                st.success("Job Posted Live! / पोस्ट लाइव हो गई!")
                st.markdown(f"[📲 Share on WhatsApp](https://wa.me/?text={urllib.parse.quote(f'Job Alert! {j_cat}: {j_req}. Wage: {j_wage}. Loc: {j_loc}. Call: +91 {j_phone}')})")

        st.write("### 📌 " + ("Available Jobs / ताज़ा उपलब्ध नौकरियाँ:" if is_en else "ताज़ा उपलब्ध नौकरियाँ:"))
        if os.path.exists(JOBS_FILE):
            df_j = pd.read_csv(JOBS_FILE).tail(10)
            for _, r in df_j.iterrows():
                st.markdown(f"• **{r.get('Category', 'Job')}**: {r['Job']} ({r['Wage']}) | 📍 {r['Location']} — [📞 " + ("Direct Call" if is_en else "सीधे कॉल करें") + f"](tel:{r['Phone']})")
        else:
            st.info("No active jobs right now. / वर्तमान में कोई काम नहीं है।")

    with t2:
        k_name = st.text_input("Your Name / आपका नाम:")
        k_skill = st.selectbox("Skill / हुनर:", ["Engineer", "Safety Officer", "Supervisor", "Welder", "Electrician", "Plumber", "Mason", "Helper", "Women Home Work"])
        k_mob = st.text_input("Mobile Number / मोबाइल नंबर:")
        k_city = st.text_input("City / शहर या जिला:")
        if st.button("✅ " + ("Register Profile" if is_en else "डायरेक्टरी में नाम जोड़ें")):
            if k_name and k_mob:
                save_entry("Worker Profile", k_name, k_mob, k_city, k_skill)
                st.success("Profile saved! / नाम सुरक्षित सेव हो गया!")

# 2. ZAKAT & AID
elif choice in [MENU_HI[1], MENU_EN[1]]:
    st.subheader("🌙 " + ("Direct Zakat, Sadaqah & Aid Desk" if is_en else "बरकत, ज़कात, सदक़ा व गुप्त दान डेस्क"))
    st.info("100% Direct & Transparent. Aid goes directly to the needy without middlemen.")
    a_tab1, a_tab2 = st.tabs(["🤝 " + ("Donors / Zakat Pledges" if is_en else "दान / ज़कात देने वाले"), "🤲 " + ("Needy Applications" if is_en else "ज़रूरतमंद सहायता आवेदन")])
    with a_tab1:
        d_name = st.text_input("Donor Name / नाम (या 'गुप्त दान'):")
        d_type = st.selectbox("Aid Type / माध्यम:", ["Tool Kits for Artisans / औज़ार", "Orphan Child School Fee / शिक्षा", "Patient Medicine / दवा", "Ration Kit / राशन", "General Zakat / सामान्य ज़कात"])
        d_amt = st.text_input("Amount / राशि (₹):")
        d_phone = st.text_input("Contact Phone / फोन नंबर:")
        if st.button("🤝 " + ("Register Pledge" if is_en else "दान संकल्प दर्ज करें")):
            if d_name and d_phone:
                save_entry("Aid Pledge", d_name, d_phone, "Local", f"{d_type} | ₹{d_amt}")
                st.success("Recorded safely! / संकल्प सुरक्षित दर्ज हो गया।")
    with a_tab2:
        n_name = st.text_input("Applicant Name / ज़रूरतमंद का नाम:")
        n_need = st.selectbox("Requirement / सहायता प्रकार:", ["Need Tools for work / काम के औज़ार", "Children School Books / पढ़ाई", "Medical Support / दवा", "Ration / राशन"])
        n_desc = st.text_area("Details / सच्चा विवरण:")
        n_phone = st.text_input("Applicant Phone / संपर्क नंबर:")
        if st.button("🤲 " + ("Submit Application" if is_en else "सहायता आवेदन भेजें")):
            if n_name and n_phone:
                save_entry("Aid Request", n_name, n_phone, "Local", f"{n_need} | {n_desc}")
                st.success("Submitted safely! / आवेदन संस्थापक के पास पहुँच चुका है।")

# 3. LIVE FOOD FEED
elif choice in [MENU_HI[2], MENU_EN[2]]:
    st.subheader("🔴 " + ("Live Food & Annadata Feed" if is_en else "लाइव अन्नदाता व लंगर बुलेटिन"))
    with st.expander("📢 " + ("Post Available Surplus Food" if is_en else "उपलब्ध खाने की सूचना दर्ज करें")):
        f_qty = st.text_input("Food Details / विवरण (उदा: 100 पैकेट खाना):")
        f_loc = st.text_input("Exact Pickup Location / स्थान:")
        f_phone = st.text_input("Pickup Phone / पिकअप फोन नंबर:")
        if st.button("📢 " + ("Broadcast Food Alert" if is_en else "लाइव बोर्ड पर जारी करें")):
            if f_qty and f_phone:
                save_feed(FOOD_FILE, {"Time": t_now, "Food": f_qty, "Location": f_loc, "Phone": f_phone})
                save_entry("Food Feed", "Donor", f_phone, f_loc, f_qty)
                st.success("Food broadcasted! / खाना लाइव बोर्ड पर जुड़ गया!")
                st.markdown(f"[📲 Share on WhatsApp](https://wa.me/?text={urllib.parse.quote(f'Food Rescue Alert! {f_qty} available at {f_loc}. Call: +91 {f_phone}')})")

    st.write("### 🍱 " + ("Currently Available Food / वर्तमान में उपलब्ध खाना:" if is_en else "वर्तमान में उपलब्ध खाना:"))
    if os.path.exists(FOOD_FILE):
        df_f = pd.read_csv(FOOD_FILE).tail(10)
        for _, r in df_f.iterrows():
            st.markdown(f"• **{r['Food']}** | 📍 {r['Location']} ({r['Time']}) — [📞 कॉल करें](tel:{r['Phone']})")
        else:
            st.info("No active food listed. / वर्तमान में कोई खाना नहीं है।")

# 4. ANTI-CASTE SHIELD
elif choice in [MENU_HI[3], MENU_EN[3]]:
    st.subheader("🕊️ " + ("Anti-Caste & Communal Harmony Shield" if is_en else "राष्ट्रीय सद्भाव व जात-पात विरोधी भाईचारा कवच"))
    st.info("Sec 196, 197, 299 BNS & SC/ST Act: Non-bailable statutory offence.")
    u_name = st.text_input("Complainant Name / शिकायतकर्ता का नाम:")
    u_city = st.text_input("District & State / जिला व राज्य:")
    u_phone = st.text_input("Mobile / मोबाइल नंबर:")
    accused_l = st.text_input("Accused Person / दोषी का नाम:")
    act_t = st.selectbox("Offence / प्रकार:", ["Public slurs & discrimination", "Denial of road/water/shop", "Social media hate speech", "Workplace caste bias"])
    if st.button("⚡ " + ("Draft Legal Notice" if is_en else "कानूनी नोटिस बनाएं")):
        if accused_l and u_name and u_phone:
            save_entry("Harmony Complaint", u_name, u_phone, u_city, f"{accused_l} | {act_t}")
            h_notc = f"STATUTORY LEGAL NOTICE AGAINST DISCRIMINATION\nTo: SP / DM, {u_city}\nSubject: Registration of FIR against '{accused_l}' under Sec 196, 197, 299 BNS.\nComplainant: {u_name} (+91 {u_phone})\nAction: Register non-bailable FIR immediately for spreading hatred."
            st.text_area("Notice:", h_notc, height=130)
            st.markdown(f"[📲 Send to SP via WhatsApp](https://wa.me/?text={urllib.parse.quote(h_notc)})")

# 5. 28 LEGAL NOTICES
elif choice in [MENU_HI[4], MENU_EN[4]]:
    st.subheader("⚖️ " + ("28 Statutory Legal Notice Generator" if is_en else "28 आधिकारिक कानूनी नोटिस जनरेटर"))
    sec_idx = st.selectbox("Select Legal Right / धारा चुनें:", range(1, 29), format_func=lambda x: f"Section {x}: {LAW_28[x-1]}")
    v_name = st.text_input("Applicant Name / प्रार्थी का नाम:")
    v_city = st.text_input("District & State / जिला व राज्य:")
    v_phone = st.text_input("Mobile / मोबाइल नंबर:")
    v_acc = st.text_input("Accused Party / दोषी पक्ष:")
    v_desc = st.text_area("Incident Facts / घटनाक्रम:", height=70)
    if st.button("⚡ " + ("Generate Notice" if is_en else "कानूनी नोटिस तैयार करें")):
        if v_name and v_phone and v_acc:
            save_entry("Legal Notice", v_name, v_phone, v_city, f"{v_acc} | Sec {sec_idx}")
            notc = f"OFFICIAL STATUTORY LEGAL NOTICE\nSubject: Legal action against '{v_acc}' ({LAW_28[sec_idx-1]})\nApplicant: {v_name} (+91 {v_phone}), {v_city}\nFactual Summary: {v_desc}\nSignature: {v_name}"
            st.success("Notice Drafted! / नोटिस तैयार:")
            st.text_area("Notice Text:", notc, height=140)
            st.download_button("📥 Download (.txt)", notc, file_name=f"Notice_{sec_idx}.txt")
            st.markdown(f"[📲 Send via WhatsApp](https://wa.me/?text={urllib.parse.quote(notc)})")

# 6. WOMEN SAFETY
elif choice in [MENU_HI[5], MENU_EN[5]]:
    st.subheader("👩‍🦰 " + ("Women Safety Desk" if is_en else "नारी सुरक्षा व महिला स्वावलंबन डेस्क"))
    st.info("Helpline: 1090 (Women Helpline) | 181 (Domestic Violence) | 112 (Police)")
    wm_name = st.text_input("Woman Name / बहन का नाम:")
    wm_phone = st.text_input("Phone Number / संपर्क नंबर:")
    wm_prob = st.selectbox("Issue / समस्या:", ["Domestic Violence / मारपीट", "Dowry Harassment / दहेज उत्पीड़न", "Stalking / छेड़छाड़", "Home Work Need / सिलाई-कुकिंग काम चाहिए"])
    if st.button("⚡ " + ("Submit Grievance" if is_en else "आवेदन दर्ज करें")):
        if wm_name and wm_phone:
            save_entry("Women Desk", wm_name, wm_phone, "Local", wm_prob)
            st.success("Recorded safely! / आवेदन सुरक्षित दर्ज हो गया!")

# 7. SENIOR CITIZENS
elif choice in [MENU_HI[6], MENU_EN[6]]:
    st.subheader("🧓 " + ("Senior Care & Emergency Blood Directory" if is_en else "बुजुर्ग सम्मान व आपातकालीन ब्लड डोनर डेस्क"))
    st.markdown("• **Rahul Verma** — B+ | 📍 पश्चिम चंपारण | [📞 Call](tel:9876543210)\n• **Amit Kumar** — O+ | 📍 पश्चिम चंपारण | [📞 Call](tel:9876543211)")
    p_name = st.text_input("Name / नाम:")
    p_phone = st.text_input("Phone / फोन नंबर:")
    p_act = st.selectbox("Type / प्रकार:", ["Volunteer as Blood Donor / रक्तदान", "Elderly Maintenance Grievance / भरण-पोषण नोटिस"])
    if st.button("✅ " + ("Save Entry" if is_en else "सुरक्षित दर्ज करें")):
        if p_name and p_phone:
            save_entry("Senior/Blood", p_name, p_phone, "Local", p_act)
            st.success("Entry Saved! / डेटा सुरक्षित सेव हो गया!")

# 8. FARMER & DRIVER
elif choice in [MENU_HI[7], MENU_EN[7]]:
    st.subheader("🌾 " + ("Farmer Mandi Rates & Driver Booking" if is_en else "किसान मंडी व ड्राइवर / वाहन सेवा"))
    st.markdown("• **Wheat / गेहूँ:** ₹2275-₹2400 / Q | **Paddy / धान:** ₹2180-₹2300 / Q | **Corn / मक्का:** ₹1900-₹2100 / Q")
    d_name = st.text_input("Driver Name / नाम:")
    d_veh = st.selectbox("Vehicle / वाहन:", ["Auto / E-Rickshaw", "Pickup Van / मालवाहक", "Tractor / ट्रॉली", "Taxi / कार"])
    d_ph = st.text_input("Driver Phone / फोन नंबर:")
    if st.button("✅ " + ("Register Driver" if is_en else "वाहन सूची में जुड़ें")):
        if d_name and d_ph:
            save_entry("Driver Entry", d_name, d_ph, "Local", d_veh)
            st.success("Driver Registered! / वाहन चालक सूची में जुड़ गया!")

# 9. MERCHANT DESK
elif choice in [MENU_HI[8], MENU_EN[8]]:
    st.subheader("🏪 " + ("Local Merchant Business Desk" if is_en else "स्थानीय दुकानदार व्यापार डेस्क"))
    m_tool = st.radio("Tool / विकल्प:", ["⚡ Sell Near-Expiry Stock / सस्ता सामान", "📲 WhatsApp Udhar Payment Reminder"])
    if "Near-Expiry" in m_tool:
        item_name = st.text_input("Item & Quantity / सामान व मात्रा:")
        item_disc = st.text_input("Discount Price / ऑफ़र भाव:")
        shop_phone = st.text_input("Shopkeeper Phone / दुकानदार फोन:")
        if st.button("📢 " + ("Broadcast Offer" if is_en else "ऑफ़र शेयर करें")):
            if item_name and shop_phone:
                st.markdown(f"[📲 Share on WhatsApp](https://wa.me/?text={urllib.parse.quote(f'Mega Sale! {item_name} at discount: {item_disc}. Contact: +91 {shop_phone}')})")
    else:
        cust_name = st.text_input("Customer Name / ग्राहक का नाम:")
        due_amt = st.text_input("Due Amount / बकाया राशि (₹):")
        cust_phone = st.text_input("Customer Phone / ग्राहक फोन:")
        if st.button("⚡ " + ("Send Payment Reminder" if is_en else "WhatsApp रिमाइंडर भेजें")):
            if cust_name and cust_phone:
                st.markdown(f"[📲 Send Reminder](https://wa.me/91{cust_phone}?text={urllib.parse.quote(f'Dear {cust_name}, your balance of Rs {due_amt} is pending. Kindly clear at your convenience.')})")

# 10. FACTORY CLAIM
elif choice in [MENU_HI[9], MENU_EN[9]]:
    st.subheader("🏭 " + ("Workplace Injury Compensation Claim" if is_en else "कंपनी/फ़ैक्ट्री हादसा व क़ानूनी मुआवज़ा दावा"))
    w_name = st.text_input("Worker Name / मज़दूर का नाम:")
    w_city = st.text_input("District & State / जिला व राज्य:")
    w_phone = st.text_input("Mobile / मोबाइल नंबर:")
    w_comp = st.text_input("Company Name / कंपनी का नाम:")
    w_inj = st.text_area("Injury Description / चोट विवरण:")
    if st.button("⚡ " + ("Generate Claim Notice" if is_en else "मुआवज़ा दावा नोटिस तैयार करें")):
        if w_name and w_phone and w_comp:
            save_entry("Accident Claim", w_name, w_phone, w_city, f"{w_comp} | {w_inj}")
            cl_notice = f"STATUTORY COMPENSATION NOTICE (Sec 10, Employees Compensation Act)\nTo: Management, {w_comp} & Labour Court\nWorker: {w_name} (+91 {w_phone})\nIncident: {w_inj}\nDemand: Bear 100% cashless medical expenses and deposit statutory compensation within 30 days."
            st.text_area("Notice:", cl_notice, height=130)
            st.markdown(f"[📲 Send via WhatsApp](https://wa.me/?text={urllib.parse.quote(cl_notice)})")

# 11. MEDICINE CHECKER
elif choice in [MENU_HI[10], MENU_EN[10]]:
    st.subheader("💊 " + ("Medicine Info & Generic Prices" if is_en else "दवा जानकारी व जन औषधि सस्ता विकल्प"))
    m_name = st.text_input("Enter Medicine or Disease / दवा या बीमारी का नाम:")
    if st.button("🔍 " + ("Check Price & Info" if is_en else "दवा भाव जाँचें")):
        if m_name:
            q_low = m_name.lower()
            if "paracetamol" in q_low or "fever" in q_low or "बुखार" in q_low:
                txt = "Fever & Pain Reliever. Jan Aushadhi Price: ₹10-15 (Market: ₹35-40)." if is_en else "बुखार व दर्द निवारक। जन औषधि पर मात्र ₹10-15 (बाज़ार में ₹35-40)।"
            elif "azithromycin" in q_low or "infection" in q_low:
                txt = "Antibiotic for infections. Jan Aushadhi Price: ₹25-35 (Market: ₹120-150)." if is_en else "एंटीबायोटिक। जन औषधि पर मात्र ₹25-35 (बाज़ार भाव ₹120-150)।"
            elif "pantoprazole" in q_low or "gas" in q_low or "गैस" in q_low:
                txt = "Acid Reflux & Gas Reliever. Jan Aushadhi Price: ₹15-20 (Market: ₹80-100)." if is_en else "गैस व एसिडिटी निवारक। जन औषधि भाव मात्र ₹15-20 (बाज़ार में ₹80-100)।"
            else:
                txt = f"{m_name} generic salt available at 70-80% cheaper price in Jan Aushadhi." if is_en else f"{m_name} का जेनेरिक साल्ट जन औषधि केंद्र पर 70-80% सस्ते भाव में उपलब्ध है।"
            st.success(txt)

# 12. NIGHT SOS
elif choice in [MENU_HI[11], MENU_EN[11]]:
    st.subheader("🚨 " 
