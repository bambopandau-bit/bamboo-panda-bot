from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os

# Ambil token dari pengaturan Railway
TOKEN = os.getenv("TOKEN")

# Simpan jumlah pesan anggota (diperbaiki agar lebih stabil)
pesan_anggota = {}

# ---------------------- PERINTAH UTAMA ----------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "🐼 Welcome to Bamboo Panda!\n\n"
        "The Community-Driven Meme Token on Solana.\n"
        "Join our mission to build one of the strongest crypto communities.\n\n"
        "Choose an option below 👇\n\n"
        "ℹ️  /info\n"
        "🔗  /social\n"
        "🗺  /roadmap\n"
        "📊  /tokenomics\n"
        "📋  /tasks\n"
        "🎖  /xp\n"
        "🏆  /leaderboard\n"
        "🆘  /help\n"
        "📝 /myposts"
    )

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "ℹ️ About Bamboo Panda\n\n"
        "Blockchain: Solana\n\n"
        "Mission:\n"
        "Building a strong, transparent and community-driven meme token with long-term utility.\n\n"
        "Status:\n"
        "🟢 Community Building"
    )

async def social(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "🔗 Official Links\n\n"
        "🌐 Website\nhttps://bambopandau-bit.github.io/\n\n"
        "📄 Whitepaper\nhttps://bambopandau-bit.github.io/whitepaper.pdf\n\n"
        "💬 Telegram\nhttps://t.me/bamboopanda_official\n\n"
        "❌ X\nhttps://x.com/BamboPanda_coin\n\n"
        "ℹ️ Note: The website, whitepaper and X page content are currently inaccessible. Only the official Telegram channel is active, showing basic project info."
    )

async def roadmap(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "🗺 Roadmap\n\n"
        "✅ Phase 1 — Completed\n"
        "• Branding\n• Website\n• Whitepaper\n• Telegram\n• X\n\n"
        "⏳ Phase 2 — In Progress\n"
        "• Community Growth\n• Marketing\n• Airdrop Campaign\n\n"
        "🔜 Phase 3 — Upcoming\n"
        "• Token Launch\n• DEX Listing\n• CoinGecko\n• CoinMarketCap\n\n"
        "🔮 Phase 4 — Future Plans\n"
        "• Partnerships\n• Staking\n• NFT Collection"
    )

async def tokenomics(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "📊 Tokenomics\n\n"
        "Total Supply: 1,000,000,000 BP\n"
        "Liquidity: 🔒 Locked\n"
        "Ownership: ✅ Renounced\n"
        "Taxes: 0%\n"
        "Network: Solana\n\n"
        "*Figures may be adjusted before final launch*"
    )

async def tasks(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "📋 Earn XP\n\n"
        "✅ Join Telegram\n"
        "✅ Follow X\n"
        "✅ Like pinned post\n"
        "✅ Repost pinned post\n"
        "✅ Invite friends\n\n"
        "Complete tasks to earn XP!"
    )

async def xp(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "🎖 Your XP\n\n"
        "Current XP: 0\n"
        "Rank: New Panda 🐼"
    )

async def leaderboard(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "🏆 Leaderboard\n\n"
        "🥇 User1\n🥈 User2\n🥉 User3"
    )

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "🆘 Help\n\n"
        "Contact Admin.\n\n"
        "⚠️ Stay away from scammers.\n"
        "Admins will NEVER ask for your wallet seed phrase."
    )

# ---------------------- FITUR PENYAMBUT & PENGHITUNG PESAN ----------------------
# Menyambut anggota baru
async def sapa_anggota_baru(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    for member in update.message.new_chat_members:
        nama = member.first_name
        await update.message.reply_text(
            f"👋 Halo {nama}!\nSelamat bergabung di grup **Bamboo Panda** 🐼\n"
            "Silakan perkenalkan diri dan ikuti aturan grup ya!"
        )

# Menghitung pesan (diperbaiki agar pasti tercatat)
async def catat_pesan(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Abaikan pesan dari bot
    if update.effective_user.is_bot:
        return
    # Ambil data pengguna
    id_user = str(update.effective_user.id) # Ubah jadi teks agar lebih stabil
    nama_user = update.effective_user.first_name

    # Tambah jumlah pesan
    if id_user not in pesan_anggota:
        pesan_anggota[id_user] = {"nama": nama_user, "jumlah": 0}
    pesan_anggota[id_user]["jumlah"] += 1

# Perintah melihat jumlah pesan sendiri (diperbaiki pasti jalan)
async def lihat_pesan(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    id_user = str(update.effective_user.id)
    nama = update.effective_user.first_name
    if id_user in pesan_anggota:
        jumlah = pesan_anggota[id_user]["jumlah"]
        await update.message.reply_text(f"📝 Hai {nama}!\nKamu sudah mengirim **{jumlah} pesan** di grup ini.")
    else:
        await update.message.reply_text(f"📝 Hai {nama}!\nKamu belum mengirim pesan apapun di grup ini.")

# ---------------------- JALANKAN BOT ----------------------
def main() -> None:
    if not TOKEN:
        print("❌ ERROR: TOKEN tidak ditemukan!")
        return

    app = Application.builder().token(TOKEN).build()

    # Daftar semua perintah
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("info", info))
    app.add_handler(CommandHandler("social", social))
    app.add_handler(CommandHandler("roadmap", roadmap))
    app.add_handler(CommandHandler("tokenomics", tokenomics))
    app.add_handler(CommandHandler("tasks", tasks))
    app.add_handler(CommandHandler("xp", xp))
    app.add_handler(CommandHandler("leaderboard", leaderboard))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("myposts", lihat_pesan))

    # Penanganan pesan & anggota baru
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, sapa_anggota_baru))
    # Catat SEMUA pesan biasa (bukan perintah)
    app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, catat_pesan))

    print("✅ Bamboo Panda Bot Running Successfully!")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
    
