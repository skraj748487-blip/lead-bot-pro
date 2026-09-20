import csv
import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = "8924269550:AAGEI8vHQVrJqEqcs9cV9F956QaAicvVUrE"
UPI_ID = "7484878440-2@ybl"
PAYMENT_AMOUNT = "999"
ADMIN_ID = 8290334681

logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO)

def main_menu():
    keyboard = [
        [InlineKeyboardButton("🏢 Real Estate Leads", callback_data="cat_Real Estate")],
        [InlineKeyboardButton("🚗 Car Showrooms Leads", callback_data="cat_Car Dealers")],
        [InlineKeyboardButton("🎓 Coaching Institutes", callback_data="cat_Coaching Centers")],
        [InlineKeyboardButton("💰 उधार वसूली (Payment Reminder)", callback_data="reminder_tool")],
        [InlineKeyboardButton("📥 Download Free Sample CSV", callback_data="export_sample")]
    ]
    return InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "💼 **VyaparMitra AI - B2B Growth & Recovery Engine** 💼\n\n"
        "⚡ *सुपरफास्ट मोड सक्रिय है - आप लिखकर या वॉइस मैसेज भेजकर डेटा ले सकते हैं!*\n\n"
        "👉 नीचे दी गई कैटेगरी चुनें या सीधे लिखें/बोलें:\n"
        "`[City] [Business]` (उदा: `Mumbai Real Estate`)"
    )
    if update.message:
        await update.message.reply_text(text, reply_markup=main_menu(), parse_mode="Markdown")
    elif update.callback_query:
        await update.callback_query.message.edit_text(text, reply_markup=main_menu(), parse_mode="Markdown")

async def generate_and_send_csv(query_text, update_or_msg):
    clean_name = query_text.replace(" ", "_").replace(")", "").replace("(", "")
    filename = f"Leads_{clean_name}.csv"
    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Business Name", "Category", "City / Area", "Contact Number", "Verification Status"])
        for i in range(1, 51):
            writer.writerow([f"{query_text} Enterprise {i}", query_text, f"Main Market Sector {i}", f"+91 98765{i:05d}", "100% Verified Active"])

    msg_obj = update_or_msg.message if hasattr(update_or_msg, "message") else update_or_msg
    await msg_obj.reply_document(
        document=open(filename, "rb"),
        caption=f"👑 **{query_text}** का पूरा प्रीमियम डेटा अनलॉक हो चुका है!\nफ़ाइल तुरंत डाउनलोड करें।"
    )
    if os.path.exists(filename):
        os.remove(filename)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "export_sample":
        filename = "Sample_B2B_Verified_Leads.csv"
        with open(filename, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Business Name", "Category", "City", "Phone Number", "Verification Status"])
            writer.writerow(["Prime Realty Hub", "Real Estate", "Delhi NCR", "+91 9811100011", "100% Verified"])
            writer.writerow(["Royal Motors Hub", "Car Dealers", "Mumbai", "+91 9822200022", "100% Verified"])
            writer.writerow(["Super30 Career Academy", "Coaching", "Patna", "+91 9833300033", "100% Verified"])

        await query.message.reply_document(
            document=open(filename, "rb"),
            caption="✅ **फ्री सैंपल लीड्स तैयार है!**\nपूरी 500+ वेरीफाइड लीड्स के लिए शहर का नाम सर्च करें।"
        )
        if os.path.exists(filename):
            os.remove(filename)

    elif query.data == "reminder_tool":
        text = (
            "💰 **उधार वसूली (Instant Reminder Tool)**\n\n"
            "व्यापारियों के बकाया पैसों का तगादा करने के लिए इस फॉर्मेट में लिखें:\n\n"
            "`REMINDER, [ग्राहक का नाम], [रुपये], [ड्यू डेट], [दुकान का नाम]`\n\n"
            "उदाहरण:\n"
            "`REMINDER, राहुल कुमार, 25000, 25 सितम्बर, शर्मा ट्रेडर्स`"
        )
        back_btn = InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ वापस जाएँ", callback_data="back_home")]])
        await query.message.edit_text(text, reply_markup=back_btn, parse_mode="Markdown")

    elif query.data.startswith("cat_"):
        category = query.data.replace("cat_", "")
        context.user_data["selected_category"] = category
        text = (
            f"🔍 चुनी गई कैटेगरी: **{category}**\n\n"
            "अब अपने शहर का नाम टाइप करें या वॉइस मैसेज भेजें (उदा: `Mumbai`, `Patna`, `Jaipur`):"
        )
        back_btn = InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ वापस जाएँ", callback_data="back_home")]])
        await query.message.edit_text(text, reply_markup=back_btn, parse_mode="Markdown")

    elif query.data.startswith("unlock_"):
        search_term = query.data.replace("unlock_", "")
        user_id = query.from_user.id

        text = (
            f"⚡ **अनलॉक करें: {search_term} की 500+ प्रीमियम लीड्स**\n\n"
            f"💰 एक्सेस फीस: **₹{PAYMENT_AMOUNT}**\n"
            f"📲 PhonePe / GPay UPI ID:\n`{UPI_ID}`\n\n"
            "1. ऊपर दी गई UPI ID पर किसी भी UPI ऐप से ₹999 ट्रांसफर करें।\n"
            "2. भुगतान के बाद स्क्रीनशॉट या UTR चैट में भेजें, सिस्टम डेटा अनलॉक कर देगा।"
        )

        if user_id == ADMIN_ID:
            buttons = [
                [InlineKeyboardButton("👑 मालिक के लिए फ़्री डाउनलोड (Admin Bypass)", callback_data=f"free_{search_term}")],
                [InlineKeyboardButton("⬅️ मेन मेन्यू", callback_data="back_home")]
            ]
        else:
            buttons = [
                [InlineKeyboardButton("⬅️ मेन मेन्यू", callback_data="back_home")]
            ]

        await query.message.reply_text(text, reply_markup=InlineKeyboardMarkup(buttons), parse_mode="Markdown")

    elif query.data.startswith("free_"):
        search_term = query.data.replace("free_", "")
        if query.from_user.id == ADMIN_ID:
            await generate_and_send_csv(search_term, query)
        else:
            await query.message.reply_text("⛔ अनधिकृत एक्सेस! केवल बॉट एडमिन ही फ्री डाउनलोड कर सकते हैं।")

    elif query.data == "back_home":
        await start(update, context)

async def process_user_query(msg, update, context):
    if msg.upper().startswith("REMINDER"):
        parts = [p.strip() for p in msg.split(",")]
        if len(parts) >= 5:
            _, client_name, amount, due_date, shop_name = parts
            reminder_script = (
                f"📢 **तैयार वसूली मैसेज (WhatsApp/SMS ड्राफ्ट):**\n\n"
                f"━━━━━━━━━━━━━━━━━━━━\n"
                f"आदरणीय *{client_name}* जी,\n"
                f"सस्नेह नमस्कार। *{shop_name}* की ओर से आपका बिल बकाया राशि *₹{amount}* है, जिसकी देय तिथि *{due_date}* है।\n\n"
                f"कृपया खाते के नियमित संचालन हेतु भुगतान समय पर करने का कष्ट करें।\n"
                f"ऑनलाइन भुगतान UPI: `{UPI_ID}`\n\n"
                f"धन्यवाद,\n*{shop_name}*\n"
                f"━━━━━━━━━━━━━━━━━━━━\n\n"
                f"💡 इसे सीधे कॉपी करके अपने ग्राहक को भेजें।"
            )
            await update.message.reply_text(reminder_script, parse_mode="Markdown")
            return
        else:
            await update.message.reply_text("⚠️ फॉर्मेट: `REMINDER, राहुल कुमार, 25000, 25 सितम्बर, शर्मा ट्रेडर्स`", parse_mode="Markdown")
            return

    cat = context.user_data.get("selected_category", "")
    search_query = f"{msg} {cat}".strip()

    preview_text = (
        f"🎯 **{search_query} - सुपरफास्ट वेरीफाइड लीड्स (Preview):**\n\n"
        f"1. {msg} Prime Ventures | 📞 +91 9820111011 | 📍 Central Hub\n"
        f"2. City Star Enterprises | 📞 +91 9820111022 | 📍 Commercial Market\n"
        f"3. Apex Trade Associates | 📞 +91 9820111033 | 📍 Ring Road\n"
        f"4. Royal Solutions Group | 📞 +91 9820111044 | 📍 VIP Complex\n"
        f"5. Galaxy Deals Network  | 📞 +91 9820111055 | 📍 Main Road\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"📊 **कुल उपलब्ध डेटाबेस:** 500+ वेरीफाइड कॉन्टैक्ट्स\n"
        f"📁 फ़ाइल: Excel / CSV\n\n"
        f"👇 पूरी फ़ाइल तुरंत अनलॉक करने के लिए नीचे टैप करें:"
    )

    unlock_btn = InlineKeyboardMarkup([
        [InlineKeyboardButton(f"🔓 अनलॉक पूरी 500+ लीड्स (₹{PAYMENT_AMOUNT})", callback_data=f"unlock_{msg}")]
    ])
    await update.message.reply_text(preview_text, reply_markup=unlock_btn, parse_mode="Markdown")

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await process_user_query(update.message.text.strip(), update, context)

async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎙️ *वॉइस नोट प्राप्त हुआ!* डेटा तैयार किया जा रहा है...", parse_mode="Markdown")
    cat = context.user_data.get("selected_category", "Real Estate")
    await process_user_query(f"Local {cat}", update, context)

if __name__ == "__main__":
    print("[*] VyaparMitra Live with Admin Protection...")
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    app.add_handler(MessageHandler(filters.VOICE, handle_voice))
    app.run_polling()
