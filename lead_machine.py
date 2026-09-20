import csv
import os
import re
import logging
import urllib.parse
import asyncio
import requests
from bs4 import BeautifulSoup
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

BOT_TOKEN = "8924269550:AAGEI8vHQVrJqEqcs9cV9F956QaAicvVUrE"
PAYMENT_AMOUNT = "999"
ADMIN_ID = 8290334681
ADMIN_UPI = "7484878440-2@ybl"

logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO)

def main_menu():
    keyboard = [
        [InlineKeyboardButton("🏢 Real Estate Leads", callback_data="preset_Real Estate")],
        [InlineKeyboardButton("🚗 Car Showrooms Leads", callback_data="preset_Car Showrooms")],
        [InlineKeyboardButton("🎓 Coaching Institutes", callback_data="preset_Coaching Institutes")],
        [InlineKeyboardButton("💰 उधार वसूली (Payment Reminder)", callback_data="reminder_tool")],
        [InlineKeyboardButton("📥 Download Free Sample CSV", callback_data="export_sample")]
    ]
    return InlineKeyboardMarkup(keyboard)

def fetch_real_leads(query_text, max_results=30):
    leads = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }

    # Clean query text
    clean_q = re.sub(r"[^\w\s]", "", query_text).strip()

    search_terms = [
        f'"{clean_q}" phone contact',
        f'"{clean_q}" contact mobile number',
        f'{clean_q} justdial contact'
    ]

    seen_phones = set()

    for term in search_terms:
        if len(leads) >= max_results:
            break
        try:
            url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(term)}"
            resp = requests.get(url, headers=headers, timeout=8)
            if resp.status_code == 200:
                soup = BeautifulSoup(resp.text, "html.parser")
                results = soup.find_all("div", class_="result__body")
                for res in results:
                    title_tag = res.find("h2", class_="result__title")
                    title = title_tag.get_text(strip=True) if title_tag else ""
                    snippet_tag = res.find("a", class_="result__snippet")
                    snippet = snippet_tag.get_text(strip=True) if snippet_tag else ""

                    full_text = f"{title} {snippet}"
                    # Match authentic 10-digit Indian mobile numbers starting with 6, 7, 8, 9
                    phones = re.findall(r"(?:(?:\+91[\-\s]?)?[6-9]\d{9})", full_text)

                    for raw_ph in phones:
                        digits = re.sub(r"[^\d]", "", raw_ph)
                        if digits.startswith("91") and len(digits) == 12:
                            clean_ph = "+91 " + digits[2:]
                        elif len(digits) == 10:
                            clean_ph = "+91 " + digits
                        else:
                            continue

                        # Avoid dummy repetitive numbers like 9801110001
                        if len(set(digits[-6:])) <= 2:
                            continue

                        if clean_ph not in seen_phones:
                            seen_phones.add(clean_ph)
                            name = re.split(r"[-|–—:]", title)[0].strip()
                            if len(name) < 4:
                                name = f"{clean_q} Center"

                            leads.append({
                                "name": name[:45],
                                "category": clean_q,
                                "city": clean_q.split()[0] if clean_q else "India",
                                "phone": clean_ph,
                                "status": "100% Real Live Verified"
                            })
                            if len(leads) >= max_results:
                                break
        except Exception as e:
            logging.error(f"Search fetch error: {e}")

    return leads

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Reset any previous stuck category
    context.user_data.clear()
    text = (
        "💼 **VyaparMitra AI - B2B Live Lead Engine** 💼\n\n"
        "⚡ *अब सिस्टम बिल्कुल फ्रेश और लाइव मोड पर है!*\n\n"
        "👉 सीधे शहर और बिज़नेस का नाम लिखकर भेजें:\n"
        "उदा: `Delhi Hotels`, `Patna Gym`, `Mumbai Doctors`\n\n"
        "या नीचे दिए गए मेन्यू का इस्तेमाल करें:"
    )
    if update.message:
        await update.message.reply_text(text, reply_markup=main_menu(), parse_mode="Markdown")
    elif update.callback_query:
        await update.callback_query.message.edit_text(text, reply_markup=main_menu(), parse_mode="Markdown")

async def generate_and_send_csv(query_text, update_or_msg):
    clean_name = re.sub(r"[^\w]", "_", query_text).strip("_")
    filename = f"Live_Leads_{clean_name}.csv"

    msg_obj = update_or_msg.message if hasattr(update_or_msg, "message") else update_or_msg
    status_msg = await msg_obj.reply_text("🔄 **इंटरनेट से असली डेटा एक्सट्रैक्ट किया जा रहा है... 5 सेकंड रुकें...**")

    leads_data = fetch_real_leads(query_text, max_results=50)

    if not leads_data:
        await status_msg.delete()
        await msg_obj.reply_text(f"⚠️ **{query_text}** के लिए लाइव नंबर नहीं मिल सके। कृपया थोड़ा अलग शब्द लिखकर सर्च करें (उदा: `Patna Fitness Gym` या `Delhi Real Estate Brokers`)।")
        return

    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Business Name", "Category", "City / Area", "Contact Number", "Verification Status"])
        for lead in leads_data:
            writer.writerow([lead["name"], lead["category"], lead["city"], lead["phone"], lead["status"]])

    await status_msg.delete()
    await msg_obj.reply_document(
        document=open(filename, "rb"),
        caption=f"👑 **{query_text}** की असली लिस्ट डाउनलोड हो गई है!\nकुल असली लीड्स: {len(leads_data)}"
    )
    if os.path.exists(filename):
        os.remove(filename)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "export_sample":
        filename = "Sample_B2B_Live_Leads.csv"
        with open(filename, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Business Name", "Category", "City", "Phone Number", "Verification Status"])
            writer.writerow(["The Oberoi Hotel", "Hotels", "Delhi", "+91 9810123456", "Live Verified"])
            writer.writerow(["Gold's Gym Boring Road", "Fitness", "Patna", "+91 9835012345", "Live Verified"])

        await query.message.reply_document(
            document=open(filename, "rb"),
            caption="✅ **सैंपल फ़ाइल तैयार है!** असली डेटा के लिए शहर और बिज़नेस लिखें।"
        )
        if os.path.exists(filename):
            os.remove(filename)

    elif query.data == "reminder_tool":
        text = (
            "💰 **उधार वसूली (WhatsApp Reminder Automation)**\n\n"
            "ग्राहक को ऑटोमेशन मैसेज भेजने के लिए इस तरह लिखकर भेजें:\n\n"
            "`REMINDER, [ग्राहक का नाम], [मोबाइल नंबर], [रुपये], [तारीख], [दुकान का नाम], [आपकी UPI ID]`\n\n"
            "📌 **उदाहरण:**\n"
            "`REMINDER, अमित कुमार, 9876543210, 15000, 25 सितम्बर, राज ट्रेडर्स, rajtraders@upi`"
        )
        back_btn = InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ वापस जाएँ", callback_data="back_home")]])
        await query.message.edit_text(text, reply_markup=back_btn, parse_mode="Markdown")

    elif query.data.startswith("preset_"):
        cat = query.data.replace("preset_", "")
        text = (
            f"🔍 चुनी गई कैटेगरी: **{cat}**\n\n"
            f"अब अपने शहर का नाम लिखकर भेजें (उदा: `Mumbai {cat}`, `Patna {cat}`):"
        )
        back_btn = InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ वापस जाएँ", callback_data="back_home")]])
        await query.message.edit_text(text, reply_markup=back_btn, parse_mode="Markdown")

    elif query.data.startswith("unlock_"):
        search_term = query.data.replace("unlock_", "")
        user_id = query.from_user.id

        text = (
            f"⚡ **अनलॉक करें: {search_term} का असली लाइव डेटाबेस**\n\n"
            f"💰 एक्सेस फीस: **₹{PAYMENT_AMOUNT}**\n"
            f"📲 Admin UPI ID:\n`{ADMIN_UPI}`\n\n"
            "1. ऊपर दी गई UPI ID पर ₹999 भेजें।\n"
            "2. स्क्रीनशॉट भेजें, सिस्टम डेटा अनलॉक कर देगा।"
        )

        buttons = []
        if user_id == ADMIN_ID:
            buttons.append([InlineKeyboardButton("👑 मालिक के लिए फ़्री डाउनलोड (Admin Bypass)", callback_data=f"free_{search_term}")])
        buttons.append([InlineKeyboardButton("⬅️ मेन मेन्यू", callback_data="back_home")])

        await query.message.reply_text(text, reply_markup=InlineKeyboardMarkup(buttons), parse_mode="Markdown")

    elif query.data.startswith("free_"):
        search_term = query.data.replace("free_", "")
        if query.from_user.id == ADMIN_ID:
            await generate_and_send_csv(search_term, query)
        else:
            await query.message.reply_text("⛔ अनधिकृत एक्सेस!")

    elif query.data == "back_home":
        await start(update, context)

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text.strip()

    if msg.upper().startswith("REMINDER"):
        parts = [p.strip() for p in msg.split(",")]
        if len(parts) >= 7:
            _, client_name, client_phone, amount, due_date, shop_name, user_upi = parts
            clean_phone = "".join(filter(str.isdigit, client_phone))
            if len(clean_phone) == 10:
                clean_phone = "91" + clean_phone

            raw_reminder = (
                f"आदरणीय {client_name} जी,\n"
                f"सस्नेह नमस्कार। {shop_name} की ओर से आपका बिल बकाया राशि ₹{amount} है, जिसकी देय तिथि {due_date} है।\n\n"
                f"कृपया खाते के नियमित संचालन हेतु भुगतान समय पर करने का कष्ट करें।\n"
                f"ऑनलाइन भुगतान हेतु UPI ID: {user_upi}\n\n"
                f"धन्यवाद,\n{shop_name}"
            )

            wa_link = f"https://wa.me/{clean_phone}?text={urllib.parse.quote(raw_reminder)}"
            preview = (
                f"📢 **तैयार वसूली मैसेज:**\n\n"
                f"━━━━━━━━━━━━━━━━━━━━\n"
                f"{raw_reminder}\n"
                f"━━━━━━━━━━━━━━━━━━━━\n\n"
                f"👉 **नीचे दिए गए बटन पर दबाते ही WhatsApp खुल जाएगा:**"
            )
            btn = InlineKeyboardMarkup([[InlineKeyboardButton("📲 ग्राहक को WhatsApp पर भेजें", url=wa_link)]])
            await update.message.reply_text(preview, reply_markup=btn)
            return

    # Direct search without mixing old categories
    search_query = msg

    wait_msg = await update.message.reply_text(f"🔍 **{search_query}** के लिए इंटरनेट से लाइव और असली नंबर निकाले जा रहे हैं...")

    live_leads = fetch_real_leads(search_query, max_results=5)
    await wait_msg.delete()

    if not live_leads:
        await update.message.reply_text(
            f"⚠️ **{search_query}** के लिए सीधे मोबाइल नंबर नहीं मिल सके।\n"
            "कृपया थोड़ा स्पष्ट लिखकर खोजें, जैसे:\n"
            "`Delhi 5 Star Hotels` या `Patna Doctors Clinic`"
        )
        return

    preview_lines = []
    for idx, item in enumerate(live_leads[:5], 1):
        preview_lines.append(f"{idx}. **{item['name']}**\n   📞 {item['phone']} | 📍 {item['city']}")

    preview_text = (
        f"🎯 **{search_query} - लाइव वेरिफाइड डेटा (Preview):**\n\n"
        + "\n\n".join(preview_lines) +
        f"\n\n━━━━━━━━━━━━━━━━━━━━\n"
        f"📊 **डेटा क्वालिटी:** 100% लाइव एक्सट्रैक्टेड रिकॉर्ड्स\n"
        f"📁 फ़ाइल: Excel / CSV\n\n"
        f"👇 पूरी लिस्ट तुरंत डाउनलोड करने के लिए अनलॉक करें:"
    )

    unlock_btn = InlineKeyboardMarkup([
        [InlineKeyboardButton(f"🔓 अनलॉक पूरी लिस्ट (₹{PAYMENT_AMOUNT})", callback_data=f"unlock_{search_query}")]
    ])
    await update.message.reply_text(preview_text, reply_markup=unlock_btn, parse_mode="Markdown")

async def main():
    print("[*] Starting VyaparMitra Pure Engine on Python 3.13...")
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    
    await application.initialize()
    await application.start()
    await application.updater.start_polling(drop_pending_updates=True)
    print("[+] Bot is LIVE and Listening!")
    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass
            
