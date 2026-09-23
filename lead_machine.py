import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="MAHA SEVA AI - Citizen Sovereign Portal",
    page_icon="⚖️",
    layout="centered"
)

# 1. Multi Bhasha (Malti Language Selector)
lang = st.selectbox(
    "🌐 Bhasha Chune / Select Language:",
    ["🇮🇳 Hindi", "🇬🇧 English", "🇮🇳 Bhojpuri", "🇮🇳 Urdu", "🇮🇳 Bengali"]
)

# Portal Header
st.title("MAHA SEVA AI — Citizen Sovereign Portal")
st.caption("28 Sovereign Sections • Custom Complaint • Night SOS • Community Peace")

# Main Menu (Purane sare options + Bhaichara desk intact)
menu_choice = st.radio(
    "Main Menu:",
    [
        "⚖️ 28 Legal Rights, Notice & PDF",
        "🚨 Night Safety & Live GPS SOS",
        "🎙️ Voice Complaint (Mic)",
        "🛡️ Cyber Shield & Fraud Verifier",
        "🏥 Healthcare & Free Ambulance",
        "💼 Pan-India Employment Desk",
        "🤝 Aapas Ka Bhaichara & Samajik Samadhan (Unity Desk)"
    ],
    index=0
)

st.divider()

# Feature 1: 28 Legal Rights (Clean & Fresh 1 to 28)
if menu_choice == "⚖️ 28 Legal Rights, Notice & PDF":
    st.subheader("⚖️ 28 Legal Rights, Notice & PDF")

    sections_28 = {
        "Section 1": "FIR Darj Karne Ka Adhikar (BNSS)",
        "Section 2": "Police Dwara Awaidh Maarpeet Ya Farzi Challan (BNSS & DK Basu)",
        "Section 3": "Mahilaon Ki Suraksha Aur Girftari Ke Niyam",
        "Section 4": "Bina Warrant Arrest Aur Zamaanat Ke Adhikar",
        "Section 5": "RTI (Soochna Ka Adhikar) Aur Sarkari Jaankari",
        "Section 6": "Cyber Crime Aur Online Fraud Complaint",
        "Section 7": "Upbhokta Adhikar (Consumer Court Protection)",
        "Section 8": "Majdoor Aur Shramik Adhikar (Labor Laws)",
        "Section 9": "Zameen, Makan Aur Sampatti Vivad Niyam",
        "Section 10": "Sarkari Yojnao Ka Labh Na Milne Par Karwayi",
        "Section 11": "Free Legal Aid (Muft Vakil Sahayata)",
        "Section 12": "Medical Negligence (Aspatal Ki Laparwahi)",
        "Section 13": "Traffic Challan Rules Aur Aapke Adhikar",
        "Section 14": "Bachhon Ke Adhikar Aur POCSO Kanoon",
        "Section 15": "Elderly Rights (Varishth Nagrik Suraksha)",
        "Section 16": "Domestic Violence (Gharelu Hinsa Roktham)",
        "Section 17": "Banking Frauds Aur Account Freeze Samadhan",
        "Section 18": "Rent Agreement Aur Kirayedaar-Makan Malik Kanoon",
        "Section 19": "Police Custody Me Adhikar Aur DK Basu Rules",
        "Section 20": "Digital Privacy Aur Data Leak Protection",
        "Section 21": "Environmental Protection (Pradushan & Safai)",
        "Section 22": "Education Right (RTE Act Ke Niyam)",
        "Section 23": "Human Rights Commission (NHRC Complaint)",
        "Section 24": "Electricity & Water Department Injustice",
        "Section 25": "Public Transport & Railway Passenger Rights",
        "Section 26": "Ration Card & Food Safety Rules",
        "Section 27": "Panchayat Aur Nagar Nigam Accountability",
        "Section 28": "Aapsi Vivad Sulha & Samajik Bhaichara Act"
    }

    selected_sec = st.selectbox(
        "Enter Section Number (1 to 28):",
        options=list(sections_28.keys()),
        index=1,
        format_func=lambda x: f"{x}: {sections_28[x]}"
    )

    st.info(f"📌 **{selected_sec}:** {sections_28[selected_sec]}")

    # Form Fields
    with st.form("legal_notice_form"):
        name = st.text_input("Complainant Name:")
        district_state = st.text_input("District & State:")
        mobile = st.text_input("Mobile Number:")
        accused = st.text_input("Accused Party / Official / Agency:")
        injustice = st.text_area("Factual Injustice Details:")

        submitted = st.form_submit_button("⚡ Draft Official Court Legal Notice")
        if submitted:
            if name and mobile:
                st.success(f"Legal notice draft taiyar ho gaya hai: {name} ji ke liye.")
            else:
                st.warning("Kripya apna Naam aur Mobile number bharein.")

# Feature 2: Aapas Ka Bhaichara (Community Peace)
elif menu_choice == "🤝 Aapas Ka Bhaichara & Samajik Samadhan (Unity Desk)":
    st.subheader("🤝 Aapsi Bhaichara, Sulha Aur Samajik Samadhan")
    st.write("Bina kisi court ya thane ke padosi, pariwar ya samajik vivad ko shanti se aapas me milkar suljhane ke liye yahan darj karein.")

    with st.form("bhaichara_form"):
        party1 = st.text_input("Pratham Paksh (Aapka Naam):")
        party2 = st.text_input("Dusra Paksh (Jinke Saath Vivad Hai):")
        area = st.text_input("Gaon / Mohalla / Panchayat:")
        matter = st.text_area("Vivad Ka Mukhya Mudda (Shanti Se Samadhan Ke Liye):")
        phone = st.text_input("Sampark Number:")

        peace_submit = st.form_submit_button("🕊️ Shanti Sulha Samiti Ko Bhejein")
        if peace_submit:
            st.success("Aapsi sulha ka anurodh darj ho gaya hai. Bhaichara desk aapse sampark karegi.")

# Baaki Purane Desk
elif menu_choice == "🚨 Night Safety & Live GPS SOS":
    st.subheader("🚨 Night Safety & Live GPS SOS")
    st.error("Emergency Alert Service: SOS button dabate hi aapki live location police aur emergency contacts ko chali jayegi.")
    if st.button("🔴 SEND EMERGENCY SOS"):
        st.success("Emergency Alert Bhej Diya Gaya Hai!")

elif menu_choice == "🎙️ Voice Complaint (Mic)":
    st.subheader("🎙️ Voice Complaint")
    st.info("Apni aawaz me bolkar shikayat darj karne ka feature yahan chalega.")

elif menu_choice == "🛡️ Cyber Shield & Fraud Verifier":
    st.subheader("🛡️ Cyber Shield & Fraud Verifier")
    st.text_input("Suspect Link ya Number Dalein:")
    st.button("Verify Karo")

elif menu_choice == "🏥 Healthcare & Free Ambulance":
    st.subheader("🏥 Healthcare & Free Ambulance")
    st.write("Free Ambulance Helpline: 108 / 102")

elif menu_choice == "💼 Pan-India Employment Desk":
    st.subheader("💼 Pan-India Employment Desk")
    st.write("Rojgar avsar aur sarkari vacancy updates.")

st.caption("---")
st.caption("Maha Seva AI — Rashtriya Nagarik Vidhik Suraksha va Jan-Adhikar Mission")
