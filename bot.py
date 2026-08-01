import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 NielBot aktif!\n\nKetik /status untuk cek status."
    )


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):

    teks = """
🟢 Online - 🔴 Offline - 🔵 Patch

🔴 Fluorite Ios FF
🔴 Migul Ios
🟢 Fluorite Ios 8 ball
🔴 Fluorite Ios mlbb
🟢 Br Mods Pc
🔴 Br mods Root
🔴 Aurora Vn Pc
🔴 Kiwmods Andro / Pc
🟢 Reaper X Pro Root
🟢 Pato Team Andro
🟢 Prime hook Andro
🟢 Hg Apkm Andro
🟢 Hg Proxy Andro
🟢 Drip Client Proxy Andro
🔴 Drip Client Apkm Andro
🔴 Slient Cheats
🟢 Plugin Mlbb/Codm/8bp/blodstrk
"""

    await update.message.reply_text(teks)


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("status", status))

print("NielBot Online")

app.run_polling()