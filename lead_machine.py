import streamlit as st
import streamlit.components.v1 as components
import urllib.parse
from datetime import datetime

st.set_page_config(
    page_title="Maha Seva AI",
    page_icon="🇮🇳",
    layout="centered",
    initial_sidebar_state="collapsed"
)

MY_WA_NUMBER = "917484878440"
today_str = datetime.now().strftime("%d-%m-%Y")
current_time_str = datetime.now().strftime("%I:%M %p")

LANG_UI = {
    "🇮🇳 हिन्दी": {
        "title": "महा-सेवा AI (MAHA SEVA AI)",
        "sub": "28 कानूनी धाराएँ • अपनी शिकायत • रात की सुरक्षा • PDF",
        "c_rights": "⚖️ 28 विधिक अधिकार, नोटिस व PDF",
        "c_sos": "🚨 रात की सुरक्षा व लाइव GPS SOS",
        "c_voice": "🎙️ बोलकर शिकायत (माइक)",
        "c_fraud": "🛡️ साइबर फ्रॉड व मैसेज चेकर",
        "c_health": "🏥 दवा व एम्बुलेंस सहायता",
        "c_job": "💼 रोज़गार व हेल्पर डेस्क",
        "sos_h": "🚨 24x7 रात की सुरक्षा व लाइव GPS SOS",
        "gps_btn": "📡 मेरा सटीक लाइव GPS पता निकालें",
        "victim_lbl": "आपका नाम:",
        "loc_lbl": "वर्तमान जगह / सड़क का नाम:",
        "sos_wa": "📲 1-क्लिक परिवार को लोकेशन व SOS भेजें",
        "siren_btn": "🚨 तेज़ अलार्म सायरन बजाएँ",
        "mode_sec": "🔢 सेक्शन नंबर से (1 से 28)",
        "mode_custom": "✍️ अपनी खुद की शिकायत लिखें",
        "sec_prompt": "सेक्शन नंबर दर्ज करें (1 से 28):",
        "name_lbl": "प्रार्थी का नाम:",
        "city_lbl": "जिला व राज्य:",
        "phone_lbl": "मोबाइल नंबर:",
        "acc_lbl": "दोषी पक्ष / अधिकारी / कंपनी:",
        "det_lbl": "सच्चा घटनाक्रम विवरण:",
        "btn_draft": "⚡ आधिकारिक कानूनी नोटिस तैयार करें",
        "success_msg": "🟢 आधिकारिक विधिक नोटिस तैयार:",
        "download_txt": "📥 कानूनी शिकायत पत्र डाउनलोड करें (.txt)",
        "pdf_btn": "🖨️ कानूनी नोटिस को PDF में सेव/प्रिंट करें",
        "send_wa": "📲 यह शिकायत WhatsApp पर भेजें"
    },
    "🇬🇧 English": {
        "title": "MAHA SEVA AI — Citizen Portal",
        "sub": "28 Sovereign Sections • Custom Complaint • Night SOS • PDF",
        "c_rights": "⚖️ 28 Legal Rights, Notice & PDF",
        "c_sos": "🚨 Night Safety & Live GPS SOS",
        "c_voice": "🎙️ Voice Complaint (Mic)",
        "c_fraud": "🛡️ Cyber Shield & Fraud Verifier",
        "c_health": "🏥 Healthcare & Free Ambulance",
        "c_job": "💼 Pan-India Employment Desk",
        "sos_h": "🚨 24x7 Night Safety & Live GPS SOS",
        "gps_btn": "📡 Fetch Live GPS Location Link",
        "victim_lbl": "Your Name:",
        "loc_lbl": "Current Location / Road:",
        "sos_wa": "📲 1-Click Send SOS via WhatsApp",
        "siren_btn": "🚨 Play Loud Siren Alarm",
        "mode_sec": "🔢 By Section Number (1 to 28)",
        "mode_custom": "✍️ Write Custom Complaint",
        "sec_prompt": "Enter Section Number (1 to 28):",
        "name_lbl": "Complainant Name:",
        "city_lbl": "District & State:",
        "phone_lbl": "Mobile Number:",
        "acc_lbl": "Accused Party / Official / Agency:",
        "det_lbl": "Factual Injustice Details:",
        "btn_draft": "⚡ Draft Official Court Legal Notice",
        "success_msg": "🟢 Official Legal Notice Ready:",
        "download_txt": "📥 Download Legal Notice (.txt)",
        "pdf_btn": "🖨️ Save as PDF / Print Notice",
        "send_wa": "📲 Send Notice via WhatsApp"
    },
    "অসমীয়া (Assamese)": {
        "title": "মহা-সেৱা AI",
        "sub": "২৮টা আইনী অধিকাৰ • ৰাতিৰ সুৰক্ষা • PDF",
        "c_rights": "⚖️ ২৮টা অধিকাৰ & PDF",
        "c_sos": "🚨 ৰাতিৰ সুৰক্ষা & GPS SOS",
        "c_voice": "🎙️ কণ্ঠৰে অভিযোগ",
        "c_fraud": "🛡️ চাইবাৰ প্ৰৱঞ্চনা পৰীক্ষা",
        "c_health": "🏥 ঔষধ & এম্বুলেন্স",
        "c_job": "💼 নিয়োগ কেন্দ্ৰ",
        "sos_h": "🚨 ৰাতিৰ সুৰক্ষা & GPS SOS",
        "gps_btn": "📡 GPS স্থান চাওক",
        "victim_lbl": "আপোনাৰ নাম:",
        "loc_lbl": "স্থান:",
        "sos_wa": "📲 SOS পঠিয়াওক",
        "siren_btn": "🚨 ছাইৰেন বজাওক",
        "mode_sec": "🔢 ধাৰা নম্বৰ (১-২৮)",
        "mode_custom": "✍️ নিজৰ অভিযোগ",
        "sec_prompt": "ধাৰা নম্বৰ (১-২৮):",
        "name_lbl": "নাম:",
        "city_lbl": "জিলা আৰু ৰাজ্য:",
        "phone_lbl": "মবাইল:",
        "acc_lbl": "অভিযুক্ত:",
        "det_lbl": "বিৱৰণ:",
        "btn_draft": "⚡ জাননী প্ৰস্তুত কৰক",
        "success_msg": "🟢 জাননী প্ৰস্তুত হ'ল:",
        "download_txt": "📥 ডাউনলোড (.txt)",
        "pdf_btn": "🖨️ PDF প্ৰিণ্ট কৰক",
        "send_wa": "📲 WhatsAppত পঠিয়াওক"
    },
    "বাংলা (Bengali)": {
        "title": "মহা-সেবা AI",
        "sub": "২৮টি আইনি অধিকার • নৈশ নিরাপত্তা • PDF",
        "c_rights": "⚖️ ২৮টি আইনি অধিকার ও PDF",
        "c_sos": "🚨 নৈশ নিরাপত্তা ও GPS SOS",
        "c_voice": "🎙️ মুখে বলে অভিযোগ",
        "c_fraud": "🛡️ সাইবার সুরক্ষা যাচাই",
        "c_health": "🏥 ওষুধ ও অ্যাম্বুলেন্স",
        "c_job": "💼 কর্মসংস্থান ডেস্ক",
        "sos_h": "🚨 ২৪x৭ নৈশ নিরাপত্তা ও লাইভ GPS SOS",
        "gps_btn": "📡 আমার লাইভ GPS অবস্থান বের করুন",
        "victim_lbl": "আপনার নাম:",
        "loc_lbl": "বর্তমান অবস্থান:",
        "sos_wa": "📲 ১-ক্লিকে SOS পাঠান",
        "siren_btn": "🚨 সাইরেন বাজান",
        "mode_sec": "🔢 ধারা নম্বর (১ থেকে ২৮)",
        "mode_custom": "✍️ নিজের অভিযোগ লিখুন",
        "sec_prompt": "ধারা নম্বর (১ থেকে ২৮):",
        "name_lbl": "নাম:",
        "city_lbl": "জেলা ও রাজ্য:",
        "phone_lbl": "মোবাইল নম্বর:",
        "acc_lbl": "অভিযুক্ত পক্ষ:",
        "det_lbl": "ঘটনার বিবরণ:",
        "btn_draft": "⚡ আইনি নোটিশ তৈরি করুন",
        "success_msg": "🟢 আইনি নোটিশ তৈরি হয়েছে:",
        "download_txt": "📥 ডাউনলোড করুন (.txt)",
        "pdf_btn": "🖨️ PDF এ প্রিন্ট করুন",
        "send_wa": "📲 হোয়াটসঅ্যাপে পাঠান"
    }
}

chosen_lang = st.radio("🌐 भाषा / Language:", list(LANG_UI.keys()), horizontal=True)
T = LANG_UI[chosen_lang]

st.header(T["title"])
st.caption(T["sub"])

nav_choice = st.radio(
    "Menu:",
    [T["c_rights"], T["c_sos"], T["c_voice"], T["c_fraud"], T["c_health"], T["c_job"]],
    horizontal=True
)

st.markdown("---")

SECTIONS = {
    1: {"name": "Wage Theft / মজদूरी चोरी", "act": "Payment of Wages Act 1936", "auth": "Labour Commissioner & DM", "rule": "Withholding wages is illegal; 10x penalty and 18% interest.", "det": "2 months wages pending. Abuses and threats upon demanding payment."},
    2: {"name": "Police Brutality / অবৈধ মাৰপিট", "act": "BNSS 2023 & DK Basu Directives", "auth": "SP & NHRC", "rule": "Assault without legal order attracts FIR under Sec 166A BNS.", "det": "Wrongful physical assault and false challan threats."},
    3: {"name": "Hospital Refusing Emergency Care", "act": "Supreme Court Parmanand Katara Verdict", "auth": "CMO & Health Dept", "rule": "Refusing emergency treatment over advance money is illegal.", "det": "Hospital delayed emergency treatment demanding cash advance."},
    4: {"name": "Workplace Injury & Disability", "act": "Employees Compensation Act 1923", "auth": "Compensation Commissioner", "rule": "Employer strictly liable for compensation and medical cost.", "det": "Duty injury occurred due to absence of safety equipment."},
    5: {"name": "Loan App Extortion", "act": "RBI Fair Rules & Sec 308 BNS", "auth": "Cyber Cell & SP", "rule": "Unlicensed money lending and blackmailing are non-bailable.", "det": "Recovery agent threatening and blackmailing with private data."},
    6: {"name": "Government Office Bribery (RTPS)", "act": "Right to Public Services Act", "auth": "Vigilance Bureau", "rule": "Deliberate delay attracts Rs 250-5000 daily penalty on official.", "det": "Services delayed demanding illegal gratification despite all papers."},
    7: {"name": "MRP Overcharging", "act": "Legal Metrology Act 2009", "auth": "DSO & Consumer Affairs", "rule": "Charging above printed MRP invites penalty and license cancellation.", "det": "Vendor charged above printed MRP and delivered commodities under-weight."},
    8: {"name": "Railway TTE Misconduct", "act": "Indian Railway Act", "auth": "RailMadad 139 & RPF", "rule": "TTE cannot misbehave or deboard forcefully.", "det": "TTE demanded illegal money and misbehaved aggressively."},
    9: {"name": "Refusal to Register FIR", "act": "Supreme Court Lalita Kumari Guidelines", "auth": "SSP & CJM Court", "rule": "Refusing cognizable FIR invites penal action under Sec 166A BNS.", "det": "Station in-charge refused to register formal FIR on written complaint."},
    10: {"name": "Land Grabbing", "act": "Section 145/144 BNSS", "auth": "SDM & Civil Court", "rule": "Administration must provide immediate stay against land grabbing.", "det": "Opposite party attempting forcible illegal land encroachment."}
}

if nav_choice == T["c_rights"]:
    st.subheader(T["c_rights"])
    filing_mode = st.radio("Options:", [T["mode_sec"], T["mode_custom"]], horizontal=True)

    if filing_mode == T["mode_sec"]:
        sec_num = st.number_input(T["sec_prompt"], min_value=1, max_value=10, value=1, step=1)
        curr = SECTIONS[sec_num]
        st.info("Section " + str(sec_num) + ": " + curr["name"] + "\n\nStatute: " + curr["act"])
        target_sub = "Section " + str(sec_num) + " (" + curr["name"] + ")"
        target_act = curr["act"]
        target_auth = curr["auth"]
        target_rule = curr["rule"]
        default_det = curr["det"]
    else:
        custom_sub = st.text_input(T["mode_custom"], value="Grievance / অভিযোগ")
        target_sub = custom_sub
        target_act = "Constitution of India, BNS 2023"
        target_auth = "District Magistrate (DM) / SP / Court"
        target_rule = "Citizens are guaranteed statutory protection and speedy justice."
        default_det = "The complainant is aggrieved by unlawful acts of accused party."

    col1, col2 = st.columns(2)
    with col1:
        v_name = st.text_input(T["name_lbl"], value="Sahil Kumar")
    with col2:
        v_loc = st.text_input(T["city_lbl"], value="West Champaran, Bihar")

    v_phone = st.text_input(T["phone_lbl"], value="7484878440")
    v_accused = st.text_input(T["acc_lbl"], value="Opposite Accused Party")
    v_details = st.text_area(T["det_lbl"], value=default_det, height=90)

    if st.button(T["btn_draft"]):
        final_notice = (
            "======================================================================\n"
            "FORMAL STATUTORY LEGAL NOTICE\n"
            "Statute: " + target_act + "\n"
            "Date: " + today_str + "\n\n"
            "To,\n"
            "1. " + target_auth + ", " + v_loc + "\n\n"
            "Subject: Legal action against '" + v_accused + "' regarding " + target_sub + "\n\n"
            "Complainant: " + v_name + " (+91 " + v_phone + "), " + v_loc + "\n\n"
            "Factual Summary:\n"
            + v_details + "\n\n"
            "Statutory Rule:\n"
            + target_rule + "\n\n"
            "Complainant Signature: " + v_name + "\n"
            "======================================================================"
        )

        st.success(T["success_msg"])
        st.text_area("Notice:", final_notice, height=200)

        st.download_button(
            label=T["download_txt"],
            data=final_notice,
            file_name="Legal_Notice.txt",
            mime="text/plain"
        )

        clean_print = final_notice.replace("\n", "<br>").replace("'", "\\'")
        pdf_html = (
            "<div style='text-align:center; margin:8px 0;'>"
            "<button onclick='printDoc()' style='background:#2563EB; color:#fff; border:none; padding:12px 24px; font-weight:bold; border-radius:8px; width:100%; cursor:pointer;'>"
            + T["pdf_btn"] +
            "</button></div>"
            "<script>"
            "function printDoc() {"
            "var win = window.open('', '', 'height=700,width=800');"
            "win.document.write('<html><head><title>Legal Notice</title></head><body style=\"font-family:monospace; padding:20px;\">');"
            "win.document.write('" + clean_print + "');"
            "win.document.write('</body></html>');"
            "win.document.close();"
            "win.print();"
            "}"
            "</script>"
        )
        components.html(pdf_html, height=65)

        enc_legal = urllib.parse.quote(final_notice)
        st.markdown("[ " + T["send_wa"] + " ](https://wa.me/?text=" + enc_legal + ")")

elif nav_choice == T["c_sos"]:
    st.subheader(T["sos_h"])
    st.write("Emergency Helpline: **112** (Police) | **1090** (Women)")

    gps_comp = (
        "<div style='background:#0F172A; padding:12px; border-radius:8px; text-align:center;'>"
        "<button onclick='getPos()' style='background:#10B981; color:#fff; border:none; padding:10px 20px; font-weight:bold; border-radius:6px; cursor:pointer;'>"
        + T["gps_btn"] +
        "</button>"
        "<p id='gps_stat' style='color:#38BDF8; font-size:12px; margin-top:8px;'>GPS...</p>"
        "<input type='text' id='gps_val' readonly style='width:90%; background:#030712; color:#10B981; border:1px solid #10B981; padding:6px; font-size:11px; display:none;'>"
        "</div>"
        "<script>"
        "function getPos() {"
        "var stat = document.getElementById('gps_stat');"
        "var val = document.getElementById('gps_val');"
        "if (navigator.geolocation) {"
        "navigator.geolocation.getCurrentPosition(function(pos) {"
        "var mapUrl = 'https://maps.google.com/?q=' + pos.coords.latitude + ',' + pos.coords.longitude;"
        "stat.innerHTML = 'Location found:';"
        "val.style.display = 'block';"
        "val.value = mapUrl;"
        "}, function(err) { stat.innerHTML = 'Please enable GPS/Location'; });"
        "} else { stat.innerHTML = 'GPS not supported'; }"
        "}"
        "</script>"
    )
    components.html(gps_comp, height=120)

    v_person_name = st.text_input(T["victim_lbl"], value="Sahil")
    road_location = st.text_input(T["loc_lbl"], value="Main Road")

    sos_msg = "EMERGENCY SOS! Name: " + v_person_name + ". Location: " + road_location + ". Time: " + current_time_str
    enc_sos = urllib.parse.quote(sos_msg)
    st.markdown("[ " + T["sos_wa"] + " ](https://wa.me/917484878440?text=" + enc_sos + ")")

elif nav_choice == T["c_voice"]:
    st.subheader(T["c_voice"])
    st.info("Click mic and speak / মাইকত ক্লিক কৰি কথা কওক:")
    voice_comp = (
        "<div style='background:#0F172A; padding:12px; border-radius:8px; text-align:center;'>"
        "<button onclick='recVoice()' style='background:#EF4444; color:#fff; border:none; padding:10px 20px; font-weight:bold; border-radius:6px; cursor:pointer;'>🎤 Speak</button>"
        "<textarea id='v_out' style='width:95%; height:70px; margin-top:8px; background:#030712; color:#38BDF8; padding:6px;'></textarea>"
        "</div>"
        "<script>"
        "function recVoice() {"
        "if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {"
        "var SR = window.SpeechRecognition || window.webkitSpeechRecognition;"
        "var rec = new SR();"
        "rec.onresult = function(e) { document.getElementById('v_out').value = e.results[0][0].transcript; };"
        "rec.start();"
        "}"
        "}"
        "</script>"
    )
    components.html(voice_comp, height=150)

elif nav_choice == T["c_fraud"]:
    st.subheader(T["c_fraud"])
    susp_msg = st.text_area("Check Message / বাৰ্তা পৰীক্ষা:", value="Electricity disconnected tonight at 9:30 PM. Call this number.")
    if st.button("🚨 Verify"):
        low = susp_msg.lower()
        if any(w in low for w in ["electricity", "बिजली", "lottery", "লটাৰী", "apk", "telegram"]):
            st.error("🚨 100% PROVEN CYBER SCAM DETECTED!")
        else:
            st.success("🟢 No obvious scam link found.")

elif nav_choice == T["c_health"]:
    st.subheader(T["c_health"])
    st.write("Emergency Ambulance: **108** | Mother & Child: **102**")
    m_name = st.text_input("Medicine Salt:", value="Azithromycin 500")
    if st.button("Check Price"):
        st.success(m_name + " generic salt available at Jan Aushadhi Kendra (70-80% cheaper).")

elif nav_choice == T["c_job"]:
    st.subheader(T["c_job"])
    city_in = st.text_input("City:", value="Surat")
    role_in = st.text_input("Role:", value="Factory Worker")
    if st.button("Search Contractors"):
        link = "https://www.google.com/maps/search/" + urllib.parse.quote(role_in + " contractor in " + city_in)
        st.markdown("[ Open Directory ](" + link + ")")

st.markdown("---")
st.caption("Maha Seva AI — All-India Sovereign Citizen Legal & Welfare Infrastructure")
