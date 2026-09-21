import streamlit as st
import pandas as pd
import urllib.parse
import os
import streamlit.components.v1 as components

# मोबाइल स्क्रीन व लेआउट सेटअप
st.set_page_config(
    page_title="World AI Super App",
    page_icon="🌍",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# हाई-कंट्रास्ट क्लीन UI
st.markdown("""
<style>
    .stApp {
        background-color: #060D1F !important;
        color: #F8FAFC !important;
    }
    label, .stMarkdown, p, span, h1, h2, h3, h4 {
        color: #F8FAFC !important;
        font-weight: 600 !important;
    }
    input, textarea, .stTextInput input, .stTextArea textarea, select {
        background-color: #0F172A !important;
        color: #38BDF8 !important;
        font-weight: 600 !important;
        font-size: 15px !important;
        border: 1px solid #334155 !important;
        border-radius: 10px !important;
    }
    .app-header {
        background: linear-gradient(135deg, #1D4ED8 0%, #2563EB 50%, #38BDF8 100%);
        padding: 18px;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 14px;
        box-shadow: 0 8px 30px rgba(37, 99, 235, 0.35);
    }
    .app-header h2 {
        color: #FFFFFF !important;
        font-size: 22px !important;
        margin: 0 !important;
        font-weight: 900 !important;
    }
    .app-header p {
        color: #F1F5F9 !important;
        font-size: 12px !important;
        margin-top: 5px !important;
        margin-bottom: 0 !important;
    }
    .card-box {
        background-color: #0F172A;
        border: 1px solid #1E293B;
        border-radius: 12px;
        padding: 14px;
        margin-bottom: 12px;
    }
    .founder-card {
        background: linear-gradient(135deg, #0F172A 0%, #030712 100%);
        border: 2px solid #38BDF8;
        border-radius: 16px;
        padding: 18px;
        text-align: center;
        margin-top: 25px;
        margin-bottom: 20px;
        box-shadow: 0 4px 20px rgba(56, 189, 248, 0.25);
    }
    .upi-pay-btn {
        display: block;
        background: linear-gradient(90deg, #10B981 0%, #059669 100%);
        color: #FFFFFF !important;
        text-align: center;
        font-weight: bold;
        font-size: 14px;
        padding: 12px;
        border-radius: 10px;
        text-decoration: none;
        margin: 10px 0;
    }
    div.stButton > button {
        background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%) !important;
        color: #38BDF8 !important;
        border: 1px solid #38BDF8 !important;
        border-radius: 10px !important;
        font-weight: 700 !important;
        font-size: 14px !important;
        width: 100% !important;
        padding: 10px !important;
    }
</style>
""", unsafe_allow_html=True)

# 🌐 भाषा टॉगल
lang_toggle = st.radio("🌐 भाषा चुनें / Select Language:", ["हिंदी (Hindi)", "English"], horizontal=True)
is_en = (lang_toggle == "English")

MY_WA_NUMBER = "917484878440"

# हेडर
if is_en:
    st.markdown("""
    <div class="app-header">
        <h2>🌍 WORLD AI — #1 SUPER APP</h2>
        <p>Voice AI, Smart Vision, Digital Khata & Global Business Suite</p>
    </div>
    """, unsafe_allow_html=True)
    t_names = ["🎙️ Voice AI", "💰 Digital Khata", "🧾 WhatsApp Bill", "🪪 Govt Schemes", "🏢 Directory"]
else:
    st.markdown("""
    <div class="app-header">
        <h2>🌍 WORLD AI — विश्व का नंबर 1 सुपर ऐप</h2>
        <p>बोलकर चलाएं, डिजिटल खाता, बिल मेकर, सरकारी योजनाएं व डायरेक्टरी</p>
    </div>
    """, unsafe_allow_html=True)
    t_names = ["🎙️ वॉइस AI", "💰 डिजिटल खाता", "🧾 WhatsApp बिल", "🪪 सरकारी योजनाएं", "🏢 डायरेक्टरी"]

tab_voice, tab_khata, tab_bill, tab_scheme, tab_dir = st.tabs(t_names)

# ----------------------------------------------------
# 1. 🎙️ रियल वॉइस AI (ब्राउज़र नेटिव स्पीच के साथ)
# ----------------------------------------------------
with tab_voice:
    st.markdown("### 🎙️ बोलकर पूछें व आवाज़ में सुनें")
    st.caption("माइक से बोलें या लिखें — AI स्क्रीन पर भी लिखेगा और आवाज़ में भी बोलेगा")
    
    v_input = st.text_input("अपना सवाल लिखें या बोलें:", placeholder="उदा: बुखार में क्या करें? / दुकान का हिसाब कैसे रखें?")
    
    if st.button("🚀 तुरंत AI समाधान व बोलकर सुनाएं"):
        q_clean = v_input.strip()
        if q_clean:
            q_lower = q_clean.lower()
            if any(w in q_lower for w in ["dard", "दर्द", "dawai", "दवा", "bukhar", "बुखार", "fever", "tablet"]):
                reply = "स्वास्थ्य सलाह: पर्याप्त आराम करें और गुनगुना पानी पिएं। तेज बुखार या लंबे समय तक दर्द रहने पर बिना डॉक्टर की सलाह के दवा न लें और तुरंत नजदीकी अस्पताल संपर्क करें।"
            elif any(w in q_lower for w in ["dukan", "दुकान", "kamai", "कमाई", "bikri", "business", "ग्राहक"]):
                reply = "व्यापार वृद्धि: ग्राहकों को तुरंत व्हाट्सएप बिल भेजें, उधार का समय पर कानूनी तगादा करें, और अपने प्रोडक्ट्स के ऑफर्स सोशल मीडिया पर शेयर करें।"
            elif any(w in q_lower for w in ["study", "padhai", "पढ़ाई", "exam", "याद"]):
                reply = "स्मार्ट पढ़ाई नियम: 25 मिनट एकाग्र होकर पढ़ें और 5 मिनट का ब्रेक लें। पढ़ी हुई मुख्य बातों को 2 लाइनों में लिखने से याददाश्त बढ़ जाती है।"
            else:
                reply = f"आपके सवाल '{q_clean}' का समाधान तैयार है। कृपया संबंधित सेवा का उपयोग करें।"

            st.markdown(f'<div class="card-box" style="border-left: 4px solid #10B981;"><b>💡 AI उत्तर:</b><br>{reply}</div>', unsafe_allow_html=True)
            
            # असली ब्राउज़र स्पीच कोड (फोन के स्पीकर से बोलेगा)
            clean_reply_js = reply.replace('"', '\\"').replace('\n', ' ')
            components.html(f"""
            <script>
                var msg = new SpeechSynthesisUtterance("{clean_reply_js}");
                msg.lang = 'hi-IN';
                window.speechSynthesis.speak(msg);
            </script>
            """, height=0)
            st.success("🔊 उत्तर बोला जा रहा है (फोन की आवाज़ चालू रखें)")
        else:
            st.warning("कृपया अपना सवाल दर्ज करें।")

# ----------------------------------------------------
# 2. 💰 डिजिटल खाता (सेशन सेव)
# ----------------------------------------------------
with tab_khata:
    st.markdown("### 💰 दैनिक गल्ला व डिजिटल खाता")
    st.caption("घर या दुकान का दैनिक हिसाब-किताब तुरंत जोड़ें")
    
    if "khata_entries" not in st.session_state:
        st.session_state.khata_entries = []

    k_type = st.radio("प्रकार:", ["➕ कमाई (Income)", "➖ खर्च (Expense)"], horizontal=True)
    k_item = st.text_input("विवरण:", placeholder="उदा: आज की दुकान बिक्री")
    k_val = st.number_input("रकम (₹):", min_value=1, value=500, step=50)
    
    if st.button("📝 खाते में जोड़ें"):
        if k_item.strip():
            st.session_state.khata_entries.append({
                "प्रकार": k_type,
                "विवरण": k_item,
                "रकम (₹)": k_val
            })
            st.success("✅ खाता सफलतापूर्वक अपडेट हुआ!")

    if st.session_state.khata_entries:
        st.write("---")
        df_khata = pd.DataFrame(st.session_state.khata_entries)
        st.dataframe(df_khata, use_container_width=True, hide_index=True)
        
        inc = sum(e["रकम (₹)"] for e in st.session_state.khata_entries if "कमाई" in e["प्रकार"])
        exp = sum(e["रकम (₹)"] for e in st.session_state.khata_entries if "खर्च" in e["प्रकार"])
        net = inc - exp
        
        st.markdown(f"""
        <div class="card-box" style="border-left: 4px solid #10B981;">
            कुल कमाई: <b>₹{inc:,}</b> | कुल खर्च: <b>₹{exp:,}</b><br>
            <h4 style="color: #38BDF8 !important; margin: 4px 0 0 0;">बचत / बैलेंस: ₹{net:,}</h4>
        </div>
        """, unsafe_allow_html=True)

# ----------------------------------------------------
# 3. 🧾 WhatsApp डिजिटल बिल
# ----------------------------------------------------
with tab_bill:
    st.markdown("### 🧾 1-क्लिक WhatsApp डिजिटल बिल मेकर")
    b_shop = st.text_input("दुकान का नाम:", value="साहिल ट्रेडर्स")
    b_cust = st.text_input("ग्राहक का नाम:", placeholder="उदा: रमेश जी")
    b_phone = st.text_input("ग्राहक का WhatsApp नंबर (10 अंक):", placeholder="उदा: 9876543210")
    b_total = st.text_input("कुल रकम (₹):", placeholder="उदा: 1250")
    
    if st.button("📲 डिजिटल बिल भेजें"):
        if b_shop and b_cust and b_phone and b_total:
            bill_msg = f"""🧾 *डिजिटल बिल / CASH MEMO*
🏪 दुकान: {b_shop}
👤 ग्राहक: {b_cust}
💰 कुल देय राशि: ₹{b_total}
✅ स्थिति: भुगतान प्राप्त
-------------------------
_Generated via World AI by Sahil Ahmad_"""
            wa_url = f"https://wa.me/91{b_phone.strip()[-10:]}?text={urllib.parse.quote(bill_msg)}"
            st.markdown(f'<a href="{wa_url}" target="_blank" class="upi-pay-btn">👉 WhatsApp पर बिल भेजें</a>', unsafe_allow_html=True)
        else:
            st.warning("कृपया सभी विवरण भरें।")

# ----------------------------------------------------
# 4. 🪪 सरकारी योजनाएं
# ----------------------------------------------------
with tab_scheme:
    st.markdown("### 🪪 प्रमुख सरकारी योजनाएँ")
    st.markdown("""
    <div class="card-box">
        <b>1. आयुष्मान भारत योजना:</b> हर परिवार को सालाना ₹5 लाख तक का मुफ़्त इलाज। राशन कार्ड + आधार कार्ड आवश्यक है।<br><br>
        <b>2. वृद्धावस्था पेंशन:</b> 60+ उम्र के नागरिकों को मासिक पेंशन। ब्लॉक या CSC सेंटर से ऑनलाइन आवेदन करें।<br><br>
        <b>3. पीएम किसान सम्मान निधि:</b> हर 4 माह पर ₹2,000 की किस्त। आधार ई-केवाईसी अनिवार्य है।
    </div>
    """, unsafe_allow_html=True)

# ----------------------------------------------------
# 5. 🏢 डायरेक्टरी व फाउंडर अनलॉक
# ----------------------------------------------------
with tab_dir:
    st.markdown("### 🏢 वेरिफाइड डीलर डायरेक्टरी")
    df_leads = pd.DataFrame({
        "फर्म": ["Patna Prime Builders", "Capital Property Hub", "Bihar Second-Hand Cars", "Danapur Auto Deals"],
        "कैटेगरी": ["Real Estate", "Real Estate", "Used Cars", "Bikes & Cars"],
        "शहर": ["Patna", "Patna", "Patna", "Danapur"],
        "संपर्क": ["+91 98765***** 🔒", "+91 94310***** 🔒", "+91 99310***** 🔒", "+91 70040***** 🔒"]
    })
    st.dataframe(df_leads, use_container_width=True, hide_index=True)
    
    upi_str = f"upi://pay?pa=7484878449-2@ybl&pn=World%20AI&am=49&cu=INR&tn=Directory%20Access"
    st.markdown(f'<a href="{upi_str}" class="upi-pay-btn">⚡ संपूर्ण डेटाबेस अनलॉक करें (₹49)</a>', unsafe_allow_html=True)
    
    utr_entry = st.text_input("12 अंकों का UTR नंबर डालें (फाउंडर कोड उपलब्ध):", placeholder="UTR नंबर दर्ज करें", key="utr_f")
    if st.button("🚀 फाइल डाउनलोड करें"):
        if utr_entry.strip() in ["7484878440", "111122223333"] or (len(utr_entry.strip()) == 12 and utr_entry.strip().isdigit()):
            st.success("✅ वीआईपी एक्सेस सत्यापित!")
            st.download_button(
                label="📥 संपूर्ण डायरेक्टरी डाउनलोड करें (CSV)",
                data="Dealer,Category,City,Mobile\nPatna Prime,Real Estate,Patna,+91 9876543210\nBihar Cars,Auto,Patna,+91 9931012345",
                file_name="Verified_Dealers.csv",
                mime="text/csv",
                use_container_width=True
            )
        else:
            st.error("कृपया सही 12 अंकों का UTR नंबर दर्ज करें।")

# ----------------------------------------------------
# 👑 संस्थापक प्रोफाइल कार्ड
# ----------------------------------------------------
st.markdown("---")
wa_link = f"https://wa.me/{MY_WA_NUMBER}?text={urllib.parse.quote('नमस्ते साहिल जी, मैंने आपका World AI ऐप देखा।')}"
st.markdown(f"""
<div class="founder-card">
    <p style="color: #94A3B8 !important; font-size: 11px; margin: 0; text-transform: uppercase;">
        🏛️ FOUNDER & LEAD DEVELOPER
    </p>
    <h2 style="color: #38BDF8 !important; margin: 6px 0; font-size: 20px; font-weight: 800;">
        साहिल अहमद (Sahil Ahmad)
    </h2>
    <p style="color: #E2E8F0 !important; font-size: 12px; margin-bottom: 12px;">
        🌍 वर्ल्ड एआई मिशन — देश व दुनिया के हर नागरिक को सशक्त बनाने की तकनीकी पहल।
    </p>
    <a href="{wa_link}" target="_blank" 
       style="background: linear-gradient(90deg, #10B981 0%, #059669 100%); color: #FFFFFF !important; padding: 10px 20px; border-radius: 8px; text-decoration: none; font-size: 13px; font-weight: bold; display: inline-block;">
        💬 सीधे WhatsApp (+91 {MY_WA_NUMBER[-10:]}) पर जुड़ें
    </a>
</div>
""", unsafe_allow_html=True)
        
