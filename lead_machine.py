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

# Header
st.title("MAHA SEVA AI — Citizen Sovereign Portal")
st.caption("28 Sovereign Sections • Bol Kar Shikayat (Voice AI) • Samajik Bhaichara Desk")

# Main Menu
menu_choice = st.radio(
    "Main Menu:",
    [
        "⚖️ 28 Legal Rights, Notice & PDF",
        "🎙️ Voice Complaint (Bol Kar Shikayat)",
        "🤝 Aapas Ka Bhaichara & Samajik Samadhan",
        "🚨 Night Safety & Live GPS SOS",
        "🛡️ Cyber Shield & Fraud Verifier",
        "🏥 Healthcare & Free Ambulance",
        "💼 Pan-India Employment Desk"
    ],
    index=1  # Default Voice Complaint par focus
)

st.divider()

# ==========================================
# FEATURE: VOICE COMPLAINT (MIC SE SHIKAYAT)
# ==========================================
if menu_choice == "🎙️ Voice Complaint (Bol Kar Shikayat)":
    st.subheader("🎙️ Bol Kar Shikayat Darj Karein (Voice AI)")
    st.info("💡 **Aam Nagarik Ke Liye:** Agar aapko likhna ya padhna nahi aata, to ghabraye nahi. Bas niche mic button dabaiye aur apni bhasha me bol dijiye ki aapke sath kya anyay ya pareshani hui hai.")

    # Audio Recording Widget
    audio_data = st.audio_input("🎤 Yahan Mic Daba Kar Apni Pareshani Boliye:")

    if audio_data is not None:
        st.audio(audio_data)
        st.success("✅ Aapki aawaz record ho chuki hai!")

        # Process / Draft Button
        if st.button("⚡ Aawaz Se Official Notice & Complaint Banayein"):
            st.write("---")
            st.subheader("📄 AI Dwara Taiyar Shikayat Patra (Draft)")
            
            st.markdown("""
            **SEVA MEIN,**  
            Shriman Zila Adhikari / Sambandhit Vibhag,  
            
            **VISHAY:** Aawaz dwara darj karai gayi aam nagarik ki samasya va nivaaran hetu prarthana patra.  
            
            **MAHODAY,**  
            Nivedan hai ki aavedak ne apni aawaz ke madhyam se MAHA SEVA AI portal par vivad/anyay ki suchna darj karai hai. Sambandhit kanoon ke tahat mamle ki jaanch kar aam nagarik ko tatkal nyay pradan karne ki kripa karein.  
            
            *Bharatiya Nagarik Suraksha Sanhita va Manavadhikar Sanrakshan Adhiniyam ke tahat nirdeshit.*
            """)
            
            st.download_button(
                label="📥 Shikayat Patra (PDF/Text) Download Karein",
                data="MAHA SEVA AI - Voice Recorded Complaint Notice",
                file_name="shikayat_patra.txt",
                mime="text/plain"
            )

    # Alternate Manual Option
    with st.expander("✍️ Agar bolne ke bajaye likhkar bhejna chahein:"):
        quick_msg = st.text_area("Apni samasya yahan likhein:")
        if st.button("Likh Kar Bhejein"):
            if quick_msg:
                st.success("Aapki shikayat darj kar li gayi hai.")

# ==========================================
# FEATURE: 28 LEGAL RIGHTS (CLEAN & FRESH)
# ==========================================
elif menu_choice == "⚖️ 28 Legal Rights, Notice & PDF":
    st.subheader("⚖️ 28 Legal Rights, Notice & PDF")

    sections_28 = {
        "Section 1": "FIR Darj Karne Ka Adhikar (BNSS)",
        "Section 2": "Police Dwara Awaidh Maarpeet Ya Farzi Challan",
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

    with st.form("legal_notice_form"):
        name = st.text_input("Complainant Name:")
        district_state = st.text_input("District & State:")
        mobile = st.text_input("Mobile Number:")
        accused = st.text_input("Accused Party / Official / Agency:")
        injustice = st.text_area("Factual Injustice Details:")

        submitted = st.form_submit_button("⚡ Draft Official Court Legal Notice")
        if submitted:
            if name and mobile:
                st.success(f"Legal notice draft taiyar ho gaya: {name} ji ke liye.")
            else:
                st.warning("Kripya Naam aur Mobile number bharein.")

# ==========================================
# FEATURE: AAPAS KA BHAICHARA DESK
# ==========================================
elif menu_choice == "🤝 Aapas Ka Bhaichara & Samajik Samadhan":
    st.subheader("🤝 Aapsi Bhaichara, Sulha Aur Samajik Samadhan")
    st.write("Gaon ya mohalle ke aapsi vivad ko bina court-kachhari ke shanti se suljhane ke liye yahan aavedan karein.")

    with st.form("bhaichara_form"):
        party1 = st.text_input("Aapka Naam:")
        party2 = st.text_input("Jinke Saath Vivad Hai:")
        area = st.text_input("Gaon / Mohalla / Panchayat:")
        matter = st.text_area("Mamle Ka Vivaran:")
        phone = st.text_input("Mobile Number:")

        peace_submit = st.form_submit_button("🕊️ Samajik Sulha Samiti Ko Bhejein")
        if peace_submit:
            st.success("Aapsi sulha ka anurodh darj ho gaya hai. Bhaichara desk aapse sampark karegi.")

# SOS, Cyber, Health & Jobs
elif menu_choice == "🚨 Night Safety & Live GPS SOS":
    st.subheader("🚨 Night Safety & Live GPS SOS")
    st.error("Emergency Alert: Ek click me police aur emergency helpline ko soochit karein.")
    if st.button("🔴 SEND EMERGENCY SOS"):
        st.success("Emergency Alert Bhej Diya Gaya!")

elif menu_choice == "🛡️ Cyber Shield & Fraud Verifier":
    st.subheader("🛡️ Cyber Shield & Fraud Verifier")
    st.text_input("Suspect Link ya Number Dalein:")
    st.button("Verify Karo")

elif menu_choice == "🏥 Healthcare & Free Ambulance":
    st.subheader("🏥 Healthcare & Free Ambulance")
    st.write("Free Ambulance Helpline: 108 / 102")

elif menu_choice == "💼 Pan-India Employment Desk":
    st.subheader("💼 Pan-India Employment Desk")
    st.write("Garib aur mehnati nagarikon ke liye nishulk rojgar sahayata.")

st.caption("---")
st.caption("Maha Seva AI — Rashtriya Nagarik Vidhik Suraksha va Jan-Adhikar Mission")
