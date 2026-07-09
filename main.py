from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os

# Get token from Railway environment variables
TOKEN = os.getenv("TOKEN")

# Store member message count
member_messages = {}

# ---------------------- MAIN COMMANDS ----------------------
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
        "📝 /myposts\n"
        "🔥 /topactive"
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
        "ℹ️ Note: The website, whitepaper and X page content are currently inaccessible. Only the official Telegram channel is active."
    )

async def roadmap(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "🗺 Roadmap\n\n"
        "✅ Phase 1 — Completed\n"
        "• Branding • Website • Whitepaper • Telegram • X\n\n"
        "⏳ Phase 2 — In Progress\n"
        "• Community Growth • Marketing • Airdrop Campaign\n\n"
        "🔜 Phase 3 — Upcoming\n"
        "• Token Launch • DEX Listing • CoinGecko • CoinMarketCap\n\n"
        "🔮 Phase 4 — Future Plans\n"
        "• Partnerships • Staking • NFT Collection"
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
        "🥇 User1 • 🥈 User2 • 🥉 User3"
    )

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "🆘 Help\n\n"
        "Contact Admin.\n\n"
        "⚠️ Stay away from scammers.\n"
        "Admins will NEVER ask for your wallet seed phrase."
    )

# ---------------------- WELCOME & MESSAGE COUNT ----------------------
async def welcome_new_member(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    for member in update.message.new_chat_members:
        name = member.first_name
        await update.message.reply_text(
            f"👋 Hi {name}!\nWelcome to the **Bamboo Panda** community 🐼\n"
            "Please introduce yourself and follow the group rules!"
        )

async def count_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.effective_user.is_bot:
        return
    user_id = str(update.effective_user.id)
    user_name = update.effective_user.first_name
    if user_id not in member_messages:
        member_messages[user_id] = {"name": user_name, "count": 0}
    member_messages[user_id]["count"] += 1

async def my_posts(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = str(update.effective_user.id)
    user_name = update.effective_user.first_name
    if user_id in member_messages:
        count = member_messages[user_id]["count"]
        await update.message.reply_text(f"📝 Hi {user_name}!\nYou have sent **{count} messages** in this group.")
    else:
        await update.message.reply_text(f"📝 Hi {user_name}!\nYou haven't sent any messages in this group yet.")

async def top_active(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not member_messages:
        await update.message.reply_text("📊 No message data yet. Please send a message first!")
        return
    sorted_members = sorted(member_messages.items(), key=lambda x: x[1]["count"], reverse=True)[:10]
    text = "🔥 **Top 10 Most Active Members** 🔥\n\n"
    for rank, data in enumerate(sorted_members, start=1):
        info = data[1]
        text += f"{rank}. {info['name']} → {info['count']} messages\n"
    await update.message.reply_text(text)

# ---------------------- RUN THE BOT ----------------------
def main() -> None:
    if not TOKEN:
        print("❌ ERROR: TOKEN variable not found! Please set it in Railway Variables.")
        return

    app = Application.builder().token(TOKEN).build()

    # Register all commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("info", info))
    app.add_handler(CommandHandler("social", social))
    app.add_handler(CommandHandler("roadmap", roadmap))
    app.add_handler(CommandHandler("tokenomics", tokenomics))
    app.add_handler(CommandHandler("tasks", tasks))
    app.add_handler(CommandHandler("xp", xp))
    app.add_handler(CommandHandler("leaderboard", leaderboard))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("myposts", my_posts))
    app.add_handler(CommandHandler("topactive", top_active))

    # Register event handlers
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome_new_member))
    app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, count_message))

    print("✅ Bamboo Panda Bot Running Successfully!")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
