from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os
import time

# Ambil token dari variabel Railway
TOKEN = os.getenv("8358431653:AAHNZo-06ujO-K9CNiT03CxGMoha6ETtBMQ"
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
        "🆘  /help"
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

# ---------------------- JALANKAN DENGAN AMAN ----------------------
def main() -> None:
    if not TOKEN:
