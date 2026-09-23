<!DOCTYPE html>
<html lang="hi">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>MAHA SEVA AI — Citizen Sovereign Portal</title>
  <style>
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    body {
      background-color: #f4f6f9;
      color: #2d3748;
      padding: 15px;
      display: flex;
      justify-content: center;
    }
    .app-container {
      width: 100%;
      max-width: 480px;
      background: #ffffff;
      border-radius: 16px;
      padding: 20px;
      box-shadow: 0 8px 24px rgba(0,0,0,0.08);
    }
    /* Top Bar */
    .lang-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 16px;
      background: #edf2f7;
      padding: 8px 12px;
      border-radius: 10px;
    }
    .lang-bar label {
      font-size: 13px;
      font-weight: 600;
      color: #4a5568;
    }
    .lang-bar select {
      padding: 6px 10px;
      border-radius: 6px;
      border: 1px solid #cbd5e0;
      background: white;
      font-size: 13px;
    }
    /* Header */
    h1 {
      font-size: 22px;
      color: #1a202c;
      margin-bottom: 6px;
      line-height: 1.3;
    }
    .subtitle {
      font-size: 11px;
      color: #718096;
      margin-bottom: 18px;
      border-bottom: 1px solid #edf2f7;
      padding-bottom: 10px;
    }
    /* Menu List */
    .menu-title {
      font-size: 14px;
      font-weight: 700;
      color: #4a5568;
      margin-bottom: 10px;
    }
    .menu-item {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 9px 12px;
      margin-bottom: 6px;
      border-radius: 8px;
      border: 1px solid #e2e8f0;
      cursor: pointer;
      font-size: 13px;
      transition: all 0.2s;
    }
    .menu-item:hover, .menu-item.active {
      background-color: #ebf8ff;
      border-color: #3182ce;
      color: #2b6cb0;
      font-weight: 600;
    }
    .menu-item input {
      accent-color: #e53e3e;
    }
    /* Section Display */
    .section-card {
      margin-top: 20px;
      background: #f7fafc;
      border-radius: 12px;
      padding: 16px;
      border: 1px solid #e2e8f0;
    }
    .card-title {
      font-size: 16px;
      font-weight: 700;
      color: #2d3748;
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .highlight-box {
      background: #ebf4ff;
      border-left: 4px solid #3182ce;
      padding: 12px;
      border-radius: 6px;
      font-size: 13px;
      color: #2c5282;
      margin-top: 12px;
      line-height: 1.4;
    }
    /* Form Inputs */
    .form-group {
      margin-top: 14px;
    }
    .form-group label {
      display: block;
      font-size: 12px;
      font-weight: 600;
      color: #718096;
      margin-bottom: 5px;
    }
    .form-group input, .form-group textarea, select.full-select {
      width: 100%;
      padding: 10px;
      border-radius: 8px;
      border: 1px solid #cbd5e0;
      background: #edf2f7;
      font-size: 13px;
      outline: none;
    }
    .form-group input:focus, .form-group textarea:focus {
      background: white;
      border-color: #3182ce;
    }
    /* Action Buttons */
    .btn-submit {
      width: 100%;
      margin-top: 18px;
      background: #ffffff;
      color: #b7791f;
      border: 1px solid #ecc94b;
      padding: 12px;
      border-radius: 8px;
      font-size: 14px;
      font-weight: 700;
      cursor: pointer;
      box-shadow: 0 2px 4px rgba(0,0,0,0.05);
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
    }
    .btn-submit:hover {
      background: #fefcbf;
    }
    .footer-tag {
      text-align: center;
      font-size: 11px;
      color: #a0aec0;
      margin-top: 24px;
      border-top: 1px solid #edf2f7;
      padding-top: 12px;
    }
  </style>
</head>
<body>

<div class="app-container">
  <!-- 1. Multi Bhasha (Malti Language Selector) -->
  <div class="lang-bar">
    <label>🌐 Select Language / भाषा चुनें:</label>
    <select id="langSelect">
      <option value="hi">🇮🇳 हिन्दी (Hindi)</option>
      <option value="en">🇬🇧 English</option>
      <option value="bho">🇮🇳 भोजपुरी (Bhojpuri)</option>
      <option value="ur">🇮🇳 اردو (Urdu)</option>
      <option value="bn">🇮🇳 বাংলা (Bengali)</option>
    </select>
  </div>

  <!-- Header -->
  <h1>MAHA SEVA AI — Citizen Sovereign Portal</h1>
  <div class="subtitle">28 Sovereign Sections • Custom Complaint • Night SOS • Community Peace</div>

  <!-- Menu List (Purana wala intact + Bhaichara desk add) -->
  <div class="menu-title">Main Menu:</div>
  <label class="menu-item active">
    <input type="radio" name="main_menu" value="sections" checked>
    <span>⚖️ 28 Legal Rights, Notice & PDF</span>
  </label>
  <label class="menu-item">
    <input type="radio" name="main_menu" value="sos">
    <span>🚨 Night Safety & Live GPS SOS</span>
  </label>
  <label class="menu-item">
    <input type="radio" name="main_menu" value="voice">
    <span>🎙️ Voice Complaint (Mic)</span>
  </label>
  <label class="menu-item">
    <input type="radio" name="main_menu" value="fraud">
    <span>🛡️ Cyber Shield & Fraud Verifier</span>
  </label>
  <label class="menu-item">
    <input type="radio" name="main_menu" value="health">
    <span>🏥 Healthcare & Free Ambulance</span>
  </label>
  <label class="menu-item">
    <input type="radio" name="main_menu" value="job">
    <span>💼 Pan-India Employment Desk</span>
  </label>
  <!-- Naya Bhaichara/Miljul Kar Rahne Ka Option -->
  <label class="menu-item">
    <input type="radio" name="main_menu" value="peace">
    <span>🤝 Aapas Ka Bhaichara & Samajik Samadhan (Unity Desk)</span>
  </label>

  <!-- 28 Legal Rights Card (Fresh & Clean) -->
  <div class="section-card" id="legalCard">
    <div class="card-title">⚖️ 28 Legal Rights, Notice & PDF</div>

    <div style="margin-bottom: 12px;">
      <label style="font-size: 12px; font-weight: 600; color: #4a5568;">Right Chune (1 to 28):</label>
      <select class="full-select" id="rightSelector" onchange="updateSectionDetail()">
        <option value="1">Section 1: FIR Darj Karne Ka Adhikar (BNSS)</option>
        <option value="2" selected>Section 2: Police Dwara Awaidh Maarpeet Ya Farzi Challan</option>
        <option value="3">Section 3: Mahilaon Ki Suraksha Aur Girftari Ke Niyam</option>
        <option value="4">Section 4: Bina Warrant Arrest Aur Zamaanat Ke Adhikar</option>
        <option value="5">Section 5: RTI (Soochna Ka Adhikar) Aur Sarkari Jaankari</option>
        <option value="6">Section 6: Cyber Crime Aur Online Fraud Complaint</option>
        <option value="7">Section 7: Upbhokta Adhikar (Consumer Court Protection)</option>
        <option value="8">Section 8: Majdoor Aur Shramik Adhikar (Labor Laws)</option>
        <option value="9">Section 9: Zameen, Makan Aur Sampatti Vivad Niyam</option>
        <option value="10">Section 10: Sarkari Yojnao Ka Labh Na Milne Par Karwayi</option>
        <option value="11">Section 11: Free Legal Aid (Muft Vakil Sahayata)</option>
        <option value="12">Section 12: Medical Negligence (Aspatal Ki Laparwahi)</option>
        <option value="13">Section 13: Traffic Challan Rules Aur Aapke Adhikar</option>
        <option value="14">Section 14: Bachhon Ke Adhikar Aur POCSO Kanoon</option>
        <option value="15">Section 15: Elderly Rights (Varishth Nagrik Suraksha)</option>
        <option value="16">Section 16: Domestic Violence (Gharelu Hinsa Roktham)</option>
        <option value="17">Section 17: Banking Frauds Aur Account Freeze Samadhan</option>
        <option value="18">Section 18: Rent Agreement Aur Kirayedaar-Makan Malik Kanoon</option>
        <option value="19">Section 19: Police Custody Me Adhikar Aur DK Basu Rules</option>
        <option value="20">Section 20: Digital Privacy Aur Data Leak Protection</option>
        <option value="21">Section 21: Environmental Protection (Pradushan & Safai)</option>
        <option value="22">Section 22: Education Right (RTE Act Ke Niyam)</option>
        <option value="23">Section 23: Human Rights Commission (NHRC Complaint)</option>
        <option value="24">Section 24: Electricity & Water Department Injustice</option>
        <option value="25">Section 25: Public Transport & Railway Passenger Rights</option>
        <option value="26">Section 26: Ration Card & Food Safety Rules</option>
        <option value="27">Section 27: Panchayat Aur Nagar Nigam Accountability</option>
        <option value="28">Section 28: Aapsi Vivad Sulha & Samajik Bhaichara Act</option>
      </select>
    </div>

    <!-- Fresh Detail Banner -->
    <div class="highlight-box" id="sectionDesc">
      📌 <b>Section 2:</b> Police dwara avaidh maarpeet ya farzi challan kanoon; Bharatiya Nagarik Suraksha Sanhita (BNSS) va D.K. Basu guidelines ke tahat complaint draft karein.
    </div>

    <!-- Clean Form Fields -->
    <div class="form-group">
      <label>Complainant Name:</label>
      <input type="text" placeholder="Apna pura naam likhein" />
    </div>

    <div class="form-group">
      <label>District & State:</label>
      <input type="text" placeholder="Jaise: Paschim Champaran, Bihar" />
    </div>

    <div class="form-group">
      <label>Mobile Number:</label>
      <input type="tel" placeholder="10 anko ka mobile number" />
    </div>

    <div class="form-group">
      <label>Accused Party / Official / Agency:</label>
      <input type="text" placeholder="Sambandhit doshi paksh / vibhag / adhikari" />
    </div>

    <div class="form-group">
      <label>Factual Injustice Details:</label>
      <textarea rows="3" placeholder="Ghatna ki poori jankari yahan likhein..."></textarea>
    </div>

    <button class="btn-submit">⚡ Draft Official Court Legal Notice</button>
  </div>

  <div class="footer-tag">
    Maha Seva AI — Rashtriya Nagarik Vidhik Suraksha va Jan-Adhikar Mission
  </div>
</div>

<script>
  function updateSectionDetail() {
    const selector = document.getElementById("rightSelector");
    const desc = document.getElementById("sectionDesc");
    const val = selector.value;
    const text = selector.options[selector.selectedIndex].text;
    desc.innerHTML = `📌 <b>${text}:</b> Is section ke tahat turant notice aur complaint draft karne ke niyam lagu honge.`;
  }
</script>

</body>
</html>
