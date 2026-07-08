from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8358431653:AAFGYjcHPZ42EdPPdwLhu-zUUA86KfQBdtI"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🐼 Welcome to Bamboo Panda!\n\n"
        "Official Community Bot\n\n"
        "🌐 Website: https://bambopandau-bit.github.io/\n"
        "❌ X: https://x.com/BamboPanda_coin"
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bamboo Panda Bot Running...")
app.run_polling()