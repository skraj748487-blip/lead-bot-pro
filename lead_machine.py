import streamlit as st
import streamlit.components.v1 as components
import urllib.parse
from datetime import datetime
import pandas as pd
import os

st.set_page_config(page_title="महा-सेवा AI / Maha Seva AI", page_icon="🇮🇳", layout="centered", initial_sidebar_state="collapsed")

# 🔒 गिटहब लोगो, एडिट बटन, मेन्यू और हेडर छिपाने का पक्का कोड
st.markdown("""
<style>
#MainMenu, header, footer, [data-testid="stToolbar"], [data-testid="stHeader"], .stAppDeployButton {
    display: none !important;
    visibility: hidden !important;
}
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

c_lang = st.radio("🌐 भाषा / Language:", ["🇮🇳 हिन्दी", "🇬🇧 English"], horizontal=True)
is_en = (c_lang == "🇬🇧 English")

MENU_HI = ["💼 रोज़गार बोर्ड", "🌙 ज़कात व गुप्त दान", "🔴 अन्नदाता बुलेटिन", "🕊️ भाईचारा कवच", "⚖️ 28 कानूनी नोटिस", "👩‍🦰 नारी सुरक्षा", "🧓 बुजुर्ग व ब्लड", "🌾 किसान व ड्राइवर", "🏪 दुकानदार डेस्क", "🏭 मुआवज़ा दावा", "💊 दवा भाव", "🚨 रात की सुरक्षा SOS"]
MENU_EN = ["💼 Live Jobs", "🌙 Zakat & Direct Aid", "🔴 Food Bulletin", "🕊️ Harmony Shield", "⚖️ 28 Legal Notices", "👩‍🦰 Women Safety", "🧓 Senior & Blood", "🌾 Farmer & Driver", "🏪 Merchant Desk", "🏭 Injury Claim", "💊 Medicine Checker", "🚨 Night SOS"]

menu_items = MENU_EN if is_en else MENU_HI

st.title("MAHA SEVA AI" if is_en else "🇮🇳 महा-सेवा AI")
st.caption("100% Humanity, 0% Discrimination • Every Hand Deserves Work" if is_en else "अखंड भारत जन-कल्याण • 100% इंसानियत, 0% जात-पात • हर हाथ को काम")

choice = st.radio("सेवा चुनें / Select Service:", menu_items, horizontal=True)
st.markdown("---")

LAW_LIST = ["मजदूरी चोरी (Payment of Wages Act)", "पुलिस ज्यादती (BNSS / DK Basu)", "अस्पताल इलाज इनकार (Sec 39A)", "हादसा मुआवज़ा (Workmen Comp Act)", "लोन ब्लैकमेल (RBI / Sec 308 BNS)", "सरकारी घूसखोरी (RTPS Act)", "MRP लूट (Legal Metrology)", "TTE अवैध वसूली (Railway Act)", "FIR न लिखना (Lalita Kumari SC)", "ज़मीन क़ब्ज़ा (Sec 145 BNSS)", "राशन चोरी (Food Security Act)", "बिजली फ़र्ज़ी बिल (Electricity Act)", "घरेलू हिंसा (DV Act 2005)", "दहेज प्रताड़ना (Sec 85 BNS)", "छेड़छाड़ (Sec 78 BNS)", "अवैध बेदखली (Rent Act)", "रोड एक्सीडेंट दावा (MV Act)", "साइबर फ्रॉड (IT Act 1930)", "स्कूल फ़ीस/TC (RTE Act)", "रिकवरी धमकी (RBI Code)", "EPF/PF चोरी (EPF Act)", "जातिसूचक गाली (SC/ST Act)", "वारंटी इनकार (Consumer Act)", "गंदगी/नाली जाम (Municipal Act)", "रास्ता रुकावट (Sec 152 BNSS)", "तेज DJ शोर (Noise Rules)", "बाल मज़दूरी (Child Labour)", "RTI इनकार (RTI Act)"]

# 1. LIVE JOBS
if choice in [MENU_HI[0], MENU_EN[0]]:
    st.subheader("💼 " + ("Live Job Board" if is_en else "रोज़गार बोर्ड"))
    t1, t2 = st.tabs(["📢 " + ("Hire / काम देना है" if is_en else "काम / स्टाफ चाहिए"), "🛠️ " + ("Job Seekers" if is_en else "काम खोजने वाले साथी")])
    with t1:
        j_cat = st.selectbox("श्रेणी / Category:", ["Site Engineer", "Safety Officer", "Supervisor", "Welder/Fitter", "Electrician/Plumber", "Mason", "Helper/Labor", "Tailoring/Cooking"])
        j_req = st.text_input("काम का विवरण:")
        j_wage = st.text_input("वेतन / दिहाड़ी:")
        j_loc = st.text_input("कार्यस्थल पता:")
        j_phone = st.text_input("मालिक का मोबाइल नंबर:")
        if st.button("📢 पोस्ट करें / Post"):
            if j_req and j_phone:
                save_feed(JOBS_FILE, {"Time": t_now, "Category": j_cat, "Job": j_req, "Wage": j_wage, "Location": j_loc, "Phone": j_phone})
                save_entry("Job Post", "Employer", j_phone, j_loc, f"{j_cat} | {j_req} | {j_wage}")
                st.success("पोस्ट लाइव हो गई!")
        st.write("### 📌 ताज़ा नौकरियाँ:")
        if os.path.exists(JOBS_FILE):
            df_j = pd.read_csv(JOBS_FILE).tail(8)
            for _, r in df_j.iterrows():
                st.markdown(f"• **{r.get('Category','काम')}**: {r['Job']} ({r['Wage']}) | 📍 {r['Location']} — [📞 कॉल करें](tel:{r['Phone']})")
    with t2:
        k_name = st.text_input("आपका नाम:")
        k_skill = st.selectbox("हुनर:", ["Engineer", "Safety Officer", "Supervisor", "Welder", "Electrician", "Plumber", "Mason", "Helper", "सिलाई/कुकिंग"])
        k_mob = st.text_input("मोबाइल नंबर:")
        k_city = st.text_input("शहर / जिला:")
        if st.button("✅ नाम जोड़ें"):
            if k_name and k_mob:
                save_entry("Worker", k_name, k_mob, k_city, k_skill)
                st.success("नाम सुरक्षित सेव हो गया!")

# 2. ZAKAT & AID
elif choice in [MENU_HI[1], MENU_EN[1]]:
    st.subheader("🌙 " + ("Zakat & Direct Aid Desk" if is_en else "ज़कात, सदक़ा व गुप्त दान डेस्क"))
    st.info("100% पारदर्शी। दानदाता का सहयोग सीधे ज़रूरतमंद तक पहुँचेगा।")
    a1, a2 = st.tabs(["🤝 दानदाता", "🤲 ज़रूरतमंद"])
    with a1:
        d_name = st.text_input("नाम (या 'गुप्त दान'):")
        d_type = st.selectbox("माध्यम:", ["औज़ार सहायता", "अनाथ बच्चे की फीस", "मरीज़ की दवा", "राशन कीट", "सामान्य ज़कात"])
        d_amt = st.text_input("राशि (₹):")
        d_phone = st.text_input("फ़ोन नंबर:")
        if st.button("🤝 संकल्प दर्ज करें"):
            if d_name and d_phone:
                save_entry("Aid Donor", d_name, d_phone, "Local", f"{d_type} | ₹{d_amt}")
                st.success("संकल्प दर्ज हो गया!")
    with a2:
        n_name = st.text_input("ज़रूरतमंद का नाम:")
        n_need = st.selectbox("सहायता प्रकार:", ["काम के औज़ार", "स्कूल कॉपी-किताब", "दवा व इलाज", "राशन"])
        n_desc = st.text_area("परेशानी का विवरण:")
        n_phone = st.text_input("संपर्क नंबर:")
        if st.button("🤲 आवेदन भेजें"):
            if n_name and n_phone:
                save_entry("Aid Seeker", n_name, n_phone, "Local", f"{n_need} | {n_desc}")
                st.success("आवेदन संस्थापक के पास दर्ज हो गया!")

# 3. FOOD FEED
elif choice in [MENU_HI[2], MENU_EN[2]]:
    st.subheader("🔴 " + ("Live Food Feed" if is_en else "लाइव अन्नदाता बुलेटिन"))
    with st.expander("📢 उपलब्ध खाने की सूचना दर्ज करें"):
        f_qty = st.text_input("खाने का विवरण (उदा: 100 पैकेट खाना):")
        f_loc = st.text_input("पिकअप स्थान:")
        f_phone = st.text_input("पिकअप फोन:")
        if st.button("📢 लाइव जारी करें"):
            if f_qty and f_phone:
                save_feed(FOOD_FILE, {"Time": t_now, "Food": f_qty, "Location": f_loc, "Phone": f_phone})
                save_entry("Food", "Donor", f_phone, f_loc, f_qty)
                st.success("खाना लाइव बोर्ड पर जुड़ गया!")
    if os.path.exists(FOOD_FILE):
        df_f = pd.read_csv(FOOD_FILE).tail(8)
        for _, r in df_f.iterrows():
            st.markdown(f"• **{r['Food']}** | 📍 {r['Location']} ({r['Time']}) — [📞 कॉल](tel:{r['Phone']})")

# 4. BROTHERHOOD SHIELD
elif choice in [MENU_HI[3], MENU_EN[3]]:
    st.subheader("🕊️ भाईचारा व सद्भाव कवच")
    u_name = st.text_input("शिकायतकर्ता नाम:")
    u_city = st.text_input("जिला व राज्य:")
    u_phone = st.text_input("मोबाइल:")
    acc_l = st.text_input("नफ़रत/भेदभाव फैलाने वाले का नाम:")
    if st.button("⚡ कानूनी नोटिस बनाएं"):
        if acc_l and u_name and u_phone:
            save_entry("Harmony", u_name, u_phone, u_city, acc_l)
            notc = f"STATUTORY LEGAL NOTICE\nसेवा में: SP/DM, {u_city}\nविषय: '{acc_l}' के विरुद्ध धारा 196, 197 BNS के तहत FIR दर्ज करने बाबत।\nप्रार्थी: {u_name} (+91 {u_phone})"
            st.text_area("Notice:", notc, height=120)
            st.markdown(f"[📲 WhatsApp भेजें](https://wa.me/?text={urllib.parse.quote(notc)})")

# 5. 28 LEGAL NOTICES
elif choice in [MENU_HI[4], MENU_EN[4]]:
    st.subheader("⚖️ 28 कानूनी नोटिस जनरेटर")
    sec_idx = st.selectbox("अधिकार चुनें:", range(1, 29), format_func=lambda x: f"धारा {x}: {LAW_LIST[x-1]}")
    v_name = st.text_input("प्रार्थी का नाम:")
    v_city = st.text_input("जिला:")
    v_phone = st.text_input("मोबाइल:")
    v_acc = st.text_input("दोषी पक्ष का नाम:")
    v_desc = st.text_area("घटनाक्रम विवरण:")
    if st.button("⚡ नोटिस तैयार करें"):
        if v_name and v_phone and v_acc:
            save_entry("Legal", v_name, v_phone, v_city, f"{v_acc} | Sec {sec_idx}")
            notc = f"OFFICIAL STATUTORY NOTICE\nविषय: कानूनी कार्रवाई ({LAW_LIST[sec_idx-1]})\nप्रार्थी: {v_name} (+91 {v_phone}), {v_city}\nदोषी: {v_acc}\nविवरण: {v_desc}"
            st.success("नोटिस तैयार:")
            st.text_area("Notice:", notc, height=130)
            st.download_button("📥 डाउनलोड", notc, file_name=f"Notice_{sec_idx}.txt")
            st.markdown(f"[📲 WhatsApp भेजें](https://wa.me/?text={urllib.parse.quote(notc)})")

# 6. WOMEN SAFETY
elif choice in [MENU_HI[5], MENU_EN[5]]:
    st.subheader("👩‍🦰 नारी सुरक्षा डेस्क")
    st.info("हेल्पलाइन: 1090 (महिला हेल्पलाइन) | 181 (घरेलू हिंसा) | 112 (पुलिस)")
    wm_name = st.text_input("बहन का नाम:")
    wm_phone = st.text_input("फ़ोन नंबर:")
    wm_prob = st.selectbox("समस्या:", ["घरेलू हिंसा/मारपीट", "दहेज प्रताड़ना", "छेड़छाड़", "घर बैठे सिलाई/कुकिंग काम चाहिए"])
    if st.button("⚡ शिकायत/आवेदन दर्ज करें"):
        if wm_name and wm_phone:
            save_entry("Women Desk", wm_name, wm_phone, "Local", wm_prob)
            st.success("आवेदन सुरक्षित दर्ज हो गया!")

# 7. SENIOR & BLOOD
elif choice in [MENU_HI[6], MENU_EN[6]]:
    st.subheader("🧓 बुजुर्ग सम्मान व आपातकालीन ब्लड डोनर")
    st.markdown("• **राहुल वर्मा** — B+ | [📞 कॉल](tel:9876543210)\n• **अमित कुमार** — O+ | [📞 कॉल](tel:9876543211)")
    p_name = st.text_input("नाम:")
    p_phone = st.text_input("फ़ोन:")
    p_act = st.selectbox("प्रकार:", ["रक्तदाता बनना चाहते हैं", "बुजुर्ग भरण-पोषण नोटिस"])
    if st.button("✅ दर्ज करें"):
        if p_name and p_phone:
            save_entry("Senior/Blood", p_name, p_phone, "Local", p_act)
            st.success("डेटा सेव हो गया!")

# 8. FARMER & DRIVER
elif choice in [MENU_HI[7], MENU_EN[7]]:
    st.subheader("🌾 किसान व ड्राइवर सेवा")
    st.markdown("• **गेहूँ:** ₹2275-₹2400 | **धान:** ₹2180-₹2300 | **मक्का:** ₹1900-₹2100")
    d_name = st.text_input("ड्राइवर का नाम:")
    d_veh = st.selectbox("वाहन:", ["ऑटो/ई-रिक्शा", "पिकअप/मालवाहक", "ट्रैक्टर", "टैक्सी"])
    d_ph = st.text_input("ड्राइवर मोबाइल:")
    if st.button("✅ ड्राइवर सूची में जुड़ें"):
        if d_name and d_ph:
            save_entry("Driver", d_name, d_ph, "Local", d_veh)
            st.success("चालक सूची में जुड़ गया!")

# 9. MERCHANT
elif choice in [MENU_HI[8], MENU_EN[8]]:
    st.subheader("🏪 दुकानदार व्यापार डेस्क")
    m_tool = st.radio("विकल्प:", ["⚡ सस्ता सामान निकालें", "📲 WhatsApp उधारी तकादा"])
    if "सस्ता" in m_tool:
        item_n = st.text_input("सामान व मात्रा:")
        item_d = st.text_input("ऑफ़र भाव:")
        sh_ph = st.text_input("दुकानदार फ़ोन:")
        if st.button("📢 ऑफ़र शेयर करें"):
            if item_n and sh_ph:
                st.markdown(f"[📲 WhatsApp भेजें](https://wa.me/?text={urllib.parse.quote(f'महा-छूट! {item_n} भाव: {item_d}। संपर्क: +91 {sh_ph}')})")
    else:
        c_n = st.text_input("ग्राहक का नाम:")
        d_a = st.text_input("बकाया राशि (₹):")
        c_p = st.text_input("ग्राहक फ़ोन:")
        if st.button("⚡ रिमाइंडर भेजें"):
            if c_n and c_p:
                st.markdown(f"[📲 रिमाइंडर भेजें](https://wa.me/91{c_p}?text={urllib.parse.quote(f'नमस्ते {c_n} जी, आपका ₹{d_a} का हिसाब बाकी है।')})")

# 10. FACTORY CLAIM
elif choice in [MENU_HI[9], MENU_EN[9]]:
    st.subheader("🏭 कंपनी/फ़ैक्ट्री मुआवज़ा दावा")
    w_n = st.text_input("मज़दूर नाम:")
    w_c = st.text_input("जिला:")
    w_p = st.text_input("मोबाइल:")
    w_co = st.text_input("कंपनी नाम:")
    w_in = st.text_area("चोट का विवरण:")
    if st.button("⚡ दावा नोटिस बनाएं"):
        if w_n and w_p and w_co:
            save_entry("Accident", w_n, w_p, w_c, f"{w_co} | {w_in}")
            cl_notc = f"STATUTORY COMPENSATION NOTICE (Employees Comp Act)\nकंपनी: {w_co}\nमज़दूर: {w_n} (+91 {w_p})\nहादसा: {w_in}\nमांग: इलाज व मुआवज़ा 30 दिन में दिया जाए।"
            st.text_area("Notice:", cl_notc, height=120)
            st.markdown(f"[📲 WhatsApp भेजें](https://wa.me/?text={urllib.parse.quote(cl_notc)})")

# 11. MEDICINE
elif choice in [MENU_HI[10], MENU_EN[10]]:
    st.subheader("💊 दवा व जन औषधि विकल्प")
    m_n = st.text_input("दवा या बीमारी का नाम:")
    if st.button("🔍 भाव जाँचें"):
        if m_n:
            q_l = m_n.lower()
            if "paracetamol" in q_l or "बुखार" in q_l or "दर्द" in q_l:
                txt = "बुखार व दर्द निवारक। जन औषधि भाव: ₹10-15 (बाज़ार: ₹35-40)।"
            elif "azithromycin" in q_l or "infection" in q_l:
                txt = "एंटीबायोटिक। जन औषधि भाव: ₹25-35 (बाज़ार: ₹120-150)।"
            elif "pantoprazole" in q_l or "गैस" in q_l:
                txt = "गैस निवारक। जन औषधि भाव: ₹15-20 (बाज़ार: ₹80-100)।"
            else:
                txt = f"{m_n} का जेनेरिक साल्ट जन औषधि पर 70-80% सस्ता उपलब्ध है।"
            st.success(txt)

# 12. NIGHT SOS
elif choice in [MENU_HI[11], MENU_EN[11]]:
    st.subheader("🚨 रात की सुरक्षा SOS")
    st.write("पुलिस: **112** | महिला हेल्पलाइन: **1090**")
    g_html = "<div style='text-align:center;'><button onclick='fPos()' style='background:#10B981;color:#fff;padding:8px;border:none;border-radius:6px;cursor:pointer;'>📡 लाइव GPS लोकेशन निकालें</button><p id='g_res' style='color:#38BDF8;font-size:12px;'></p></div><script>function fPos(){navigator.geolocation.getCurrentPosition(function(p){document.getElementById('g_res').innerHTML='https://maps.google.com/?q='+p.coords.latitude+','+p.coords.longitude;});}</script>"
    components.html(g_html, height=75)
    s_n = st.text_input("नाम:")
    s_r = st.text_input("स्थान / सड़क:")
    if s_n and s_r:
        st.markdown(f"[📲 WhatsApp SOS भेजें](https://wa.me/{WA_NUM}?text={urllib.parse.quote(f'EMERGENCY SOS! Name: {s_n}. Loc: {s_r}. Time: {t_now}')})")

# ADMIN PANEL
st.markdown("---")
with st.expander("🔐 संस्थापक गुप्त एडमिन पैनल (केवल साहिल अहमद के लिए)"):
    adm_pass = st.text_input("पासवर्ड डालें:", type="password")
    if adm_pass == "sahil786":
        st.success("🟢 स्वागत है साहिल भाई! डेटाबेस सक्रिय है:")
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
            
