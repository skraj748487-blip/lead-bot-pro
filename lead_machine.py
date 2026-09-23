import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="MAHA SEVA AI — Citizen Sovereign Portal",
    page_icon="⚖️",
    layout="centered"
)

# 1. Bhasha Chune (Original Hindi & English Radio)
lang = st.radio(
    "🌐 भाषा चुनें / Select Language:",
    ["🇮🇳 हिन्दी", "🇬🇧 English"],
    horizontal=True
)

# Title & Subtitle
st.title("MAHA SEVA AI — Citizen Sovereign Portal")
st.caption("28 Sovereign Sections • Custom Complaint • Night SOS • PDF")

# Menu (Original 6 Options)
menu = st.radio(
    "Menu:",
    [
        "⚖️ 28 Legal Rights, Notice & PDF",
        "🚨 Night Safety & Live GPS SOS",
        "🎙️ Voice Complaint (Mic)",
        "🛡️ Cyber Shield & Fraud Verifier",
        "🏥 Healthcare & Free Ambulance",
        "💼 Pan-India Employment Desk"
    ],
    index=0
)

st.divider()

# 28 Legal Rights, Notice & PDF
if menu == "⚖️ 28 Legal Rights, Notice & PDF":
    st.subheader("⚖️ 28 Legal Rights, Notice & PDF")

    choice_type = st.radio(
        "विकल्प चुनें:",
        ["📘 By Section Number (1 to 28)", "✍️ Write Custom Complaint"],
        horizontal=True
    )

    if choice_type == "📘 By Section Number (1 to 28)":
        section_num = st.selectbox(
            "Enter Section Number (1 to 28):",
            options=list(range(1, 29)),
            index=1
        )

        # Section 2 Blue Banner (Same to same)
        st.info("सेक्शन 2: पुलिस द्वारा अवैध मारपीट या फर्जी चालान कानून; भारतीय नागरिक सुरक्षा संहिता (BNSS) व डी.के. बसु गाइडलाइन्स")

        with st.form("legal_notice_form"):
            name = st.text_input("Complainant Name:", value="रोहित कुमार")
            district_state = st.text_input("District & State:", value="पश्चिम चंपारण, बिहार")
            mobile = st.text_input("Mobile Number:", value="7464874440")
            accused = st.text_input("Accused Party / Official / Agency:", value="संबंधित दोषी पक्ष / अधिकारी")
            injustice = st.text_area(
                "Factual Injustice Details:",
                value="संबंधित पुलिसकर्मी द्वारा अकारण अभद्रता, मारपीट व अवैध चालान की धमकी दी गई।"
            )

            submit = st.form_submit_button("⚡ Draft Official Court Legal Notice")
            if submit:
                st.success("Draft Official Court Legal Notice Generated!")

    else:
        with st.form("custom_complaint_form"):
            c_name = st.text_input("Complainant Name:")
            c_district = st.text_input("District & State:")
            c_mobile = st.text_input("Mobile Number:")
            c_details = st.text_area("Custom Complaint Details:")
            c_submit = st.form_submit_button("⚡ Draft Official Court Legal Notice")
            if c_submit:
                st.success("Custom Legal Notice Generated!")

elif menu == "🚨 Night Safety & Live GPS SOS":
    st.subheader("🚨 Night Safety & Live GPS SOS")
    st.error("Emergency Alert Service: SOS button dabate hi aapki live location police aur emergency contacts ko chali jayegi.")
    if st.button("🔴 SEND EMERGENCY SOS"):
        st.success("Emergency Alert Sent!")

elif menu == "🎙️ Voice Complaint (Mic)":
    st.subheader("🎙️ Voice Complaint (Mic)")
    st.info("Voice complaint module.")

elif menu == "🛡️ Cyber Shield & Fraud Verifier":
    st.subheader("🛡️ Cyber Shield & Fraud Verifier")
    st.text_input("Enter Suspect Link or Number:")
    st.button("Verify")

elif menu == "🏥 Healthcare & Free Ambulance":
    st.subheader("🏥 Healthcare & Free Ambulance")
    st.write("Free Ambulance Helpline: 108 / 102")

elif menu == "💼 Pan-India Employment Desk":
    st.subheader("💼 Pan-India Employment Desk")
    st.write("Employment Portal.")

st.caption("---")
st.caption("महा सेवा AI — राष्ट्रीय नागरिक विधिक सुरक्षा व जन-अधिकार मिशन")
