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
        "title": "MAHA SEVA AI — Citizen & Merchant Sovereign Network",
        "sub": "Live Jobs • Food Rescue • Merchant Desk • Factory Claims • Legal Rights • SOS",
        "menu": ["🔴 Live Food Feed", "💼 Live Jobs & Artisans", "🏪 Merchant Desk", "🏭 Factory Injury Claim", "⚖️ Legal Notice", "💊 Medicine Checker", "🚨 Night SOS"],
        "f_post": "📢 Post Available Food (200+ Packs / Surplus)",
        "j_post": "📢 Post Work / Hiring (Need Electrician / Welder)",
        "adm_title": "🔐 Founder Private Database (Sahil Ahmad Only)"
    }
else:
    UI = {
        "title": "महा-सेवा AI (MAHA SEVA AI)",
        "sub": "लाइव अन्न सेवा • ताज़ा रोज़गार • दुकानदार व्यापार • फ़ैक्ट्री हादसा दावा • क़ानूनी अधिकार • SOS",
        "menu": ["🔴 लाइव अन्नदाता बुलेटिन", "💼 ताज़ा रोज़गार व कारीगर", "🏪 दुकानदार व्यापार डेस्क", "🏭 फैक्ट्री हादसा दावा", "⚖️ 28 क़ानूनी नोटिस", "💊 दवा व जेनेरिक भाव", "🚨 रात की सुरक्षा SOS"],
        "f_post": "📢 उपलब्ध खाने की सूचना डालें (200 पैकेट / बचा खाना)",
        "j_post": "📢 काम / नौकरी की पोस्ट डालें (इलेक्ट्रीशियन / वेल्डर चाहिए)",
        "adm_title": "🔐 संस्थापक गुप्त एडमिन पैनल (केवल साहिल अहमद के लिए)"
    }

st.title(UI["title"])
st.caption(UI["sub"])

choice = st.radio("Menu:", UI["menu"], horizontal=True)
st.markdown("---")

# 1. LIVE FOOD FEED
if choice == UI["menu"][0]:
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

# 2. LIVE JOBS & ARTISANS
elif choice == UI["menu"][1]:
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

# 3. MERCHANT DESK
elif choice == UI["menu"][2]:
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

# 4. FACTORY ACCIDENT CLAIM
elif choice == UI["menu"][3]:
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
            f"Signature: {w_name}\n"
            "======================================================================"
        )
        st.success("🟢 दावा नोटिस तैयार व डेटाबेस में सुरक्षित:")
        st.text_area("Claim Notice:", cl_notice, height=180)
        st.download_button("📥 डाउनलोड क्लेम (.txt)", cl_notice, file_name="Accident_Claim.txt")
        c_cl = cl_notice.replace("\n", "<br>").replace("'", "\\'")
        cp_html = f"<div style='text-align:center;'><button onclick='pDoc()' style='background:#2563EB;color:#fff;padding:10px 20px;border:none;border-radius:6px;cursor:pointer;font-weight:bold;'>🖨️ PDF प्रिंट / सेव करें</button></div><script>function pDoc(){{var w=window.open('','','width=800,height=700');w.document.write('<html><body style=\"font-family:monospace;padding:20px;\">{c_cl}</body></html>');w.document.close();w.print();}}</script>"
        components.html(cp_html, height=50)
        st.markdown(f"[📲 WhatsApp पर भेजें](https://wa.me/?text={urllib.parse.quote(cl_notice)})")

# 5. LEGAL NOTICE
elif choice == UI["menu"][4]:
    st.subheader("⚖️ 28 क़ानूनी नोटिस जनरेटर")
    sec_num = st.number_input("धारा चुनें (1: वेतन चोरी, 2: पुलिस ज्यादती, 3: अस्पताल इनकार, 4: ज़मीन क़ब्ज़ा):", min_value=1, max_value=4, value=1)
    SEC_DICT = {
        1: ("वेतन व मज़दूरी चोरी", "Payment of Wages Act 1936", "लेबर कमिश्नर व डीएम"),
        2: ("पुलिस अवैध मारपीट या चालान", "BNSS 2023 व DK Basu Guidelines", "एसपी व मानवाधिकार आयोग"),
        3: ("अस्पताल इलाज से इनकार", "सुप्रीम कोर्ट परमानंद कटारा फैसला", "सीएमओ व स्वास्थ्य विभाग"),
        4: ("पैतृक ज़मीन पर अवैध क़ब्ज़ा", "धारा 145/144 BNSS", "एसडीएम व सिविल कोर्ट")
    }
    s_name, s_act, s_auth = SEC_DICT[sec_num]
    st.info(f"विषय: {s_name} | लागू क़ानून: {s_act}")
    u_name = st.text_input("प्रार्थी का नाम:", value="साहिल कुमार")
    u_city = st.text_input("जिला व राज्य:", value="पश्चिम चंपारण, बिहार")
    u_mob = st.text_input("मोबाइल नंबर:", value="7484878440")
    u_acc = st.text_input("दोषी पक्ष / अधिकारी:", value="संबंधित दोषी पक्ष")
    u_det = st.text_area("विवरण:", value="अन्यायपूर्ण तरीक़े से परेशान किया जा रहा है।")
    if st.button("⚡ क़ानूनी नोटिस तैयार करें"):
        save_entry("Legal Notice", u_name, u_mob, u_city, f"{u_acc} | {s_name}")
        notc = f"कानूनी नोटिस\nअधिनियम: {s_act}\nसेवा में: {s_auth}, {u_city}\nविषय: '{u_acc}' के विरुद्ध {s_name} बाबत।\nप्रार्थी: {u_name} (+91 {u_mob})\nविवरण: {u_det}\nहस्ताक्षर: {u_name}"
        st.success("🟢 नोटिस तैयार व सुरक्षित सेव:")
        st.text_area("Notice:", notc, height=150)
        st.download_button("📥 नोटिस डाउनलोड करें (.txt)", notc, file_name="Legal_Notice.txt")
        st.markdown(f"[📲 WhatsApp पर भेजें](https://wa.me/?text={urllib.parse.quote(notc)})")

# 6. MEDICINE CHECKER
elif choice == UI["menu"][5]:
    st.subheader("💊 दवा जानकारी व जन औषधि सस्ता विकल्प")
    st.write("एम्बुलेंस: **108** | प्रसूति सेवा: **102**")
    m_name = st.text_input("दवा या बीमारी का नाम लिखें:", value="Azithromycin 500")
    if st.button("🔍 दवा भाव जाँचें"):
        q_low = m_name.lower()
        if "paracetamol" in q_low or "बुखार" in q_low:
            txt = "बुखार व दर्द निवारक। जन औषधि पर मात्र ₹10-15 (बाज़ार में ₹35-40)।"
        elif "azithromycin" in q_low or "infection" in q_low:
            txt = "एंटीबायोटिक। जन औषधि पर मात्र ₹25-35 (बाज़ार भाव ₹120-150)।"
        elif "pantoprazole" in q_low or "गैस" in q_low:
            txt = "गैस व एसिडिटी निवारक। जन औषधि भाव मात्र ₹15-20 (बाज़ार में ₹80-100)।"
        else:
            txt = f"{m_name} का जेनेरिक साल्ट जन औषधि केंद्र पर 70-80% सस्ते भाव में उपलब्ध है।"
        st.success(txt)

# 7. NIGHT SOS
elif choice == UI["menu"][6]:
    st.subheader("🚨 24x7 रात की सुरक्षा व लाइव GPS SOS")
    st.write("पुलिस: **112** | महिला हेल्पलाइन: **1090**")
    g_html = "<div style='text-align:center;'><button onclick='fPos()' style='background:#10B981;color:#fff;padding:10px;border:none;border-radius:6px;font-weight:bold;cursor:pointer;'>📡 लाइव GPS निकालें</button><p id='g_res' style='color:#38BDF8;font-size:12px;'></p></div><script>function fPos(){navigator.geolocation.getCurrentPosition(function(p){document.getElementById('g_res').innerHTML='https://maps.google.com/?q='+p.coords.latitude+','+p.coords.longitude;});}</script>"
    components.html(g_html, height=75)
    sos_name = st.text_input("पीड़ित का नाम:", value="साहिल")
    sos_road = st.text_input("सड़क / चौराहा:", value="मेन रोड")
    st.markdown(f"[📲 परिवार को WhatsApp SOS भेजें](https://wa.me/{WA_NUM}?text={urllib.parse.quote(f'EMERGENCY SOS! Name: {sos_name}. Location: {sos_road}. Time: {t_now}.')})")

# ADMIN PANEL
st.markdown("---")
with st.expander(UI["adm_title"]):
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
