import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import requests

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

# === COMMAND HANDLERS ===

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👁️ Welcome, Explorer.\n\nYou’ve just unlocked the 🔵 **Blue Key** to TiffyAI.\n\n"
        "🚀 Claim your first $TIFFY every 10 minutes:\n👉 https://tiffyai.github.io/Start/\n\n"
        "🎯 TiffyAI isn’t just a token. It’s a movement.\n\nUse /help to explore everything she can do.",
        parse_mode="Markdown"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "**TiffyAI Bot Commands:**\n"
        "/start — Unlock Blue Key\n"
        "/claim — Stamp Portal\n"
        "/wallet — Launch Wallet\n"
        "/trade — PancakeSwap + Stats\n"
        "/price — Live $TIFFY Price\n"
        "/stake — Rewards from Contract\n"
        "/ai — Ask TiffyAI Anything\n",
        parse_mode="Markdown"
    )

async def claim(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔓 Enter the Portal & Claim:\nhttps://tiffyai.github.io/Start/")

async def wallet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔐 Launch TiffyAI in your wallet:\n\n"
        "🦊 MetaMask: https://metamask.app.link/dapp/tiffyai.github.io/Start/\n"
        "📲 Trust Wallet: https://link.trustwallet.com/open_url?coin_id=60&url=https%3A%2F%2Ftiffyai.github.io%2FStart%2F\n"
        "🌐 OKX Wallet: okx://wallet/dapp/details?dappUrl=https%3A%2F%2Ftiffyai.github.io%2FStart%2F"
    )

async def trade(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📈 Trade $TIFFY & check analytics:\n\n"
        "🛒 PancakeSwap: https://pancakeswap.finance/swap?outputCurrency=0x...\n"
        "📊 BscScan: https://bscscan.com/token/0x...\n"
        "🧠 Sourcify Verified: https://sourcify.dev/#/lookup/0x...\n"
        "🏦 Treasury-linked. Burn-enabled. Purpose-coded."
    )

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        url = "https://tiffyai.github.io/TIFFY-Market-Value/price.json"
        response = requests.get(url, timeout=5)
        data = response.json()

        price = float(data['tiffyToUSD'])
        updated = data['lastUpdated']

        await update.message.reply_text(
            f"💎 $TIFFY is now **${price:.2f}**\n🕓 Updated: `{updated}`",
            parse_mode="Markdown"
        )
    except Exception as e:
        await update.message.reply_text("⚠️ Couldn't fetch price data.")
        print("Price fetch error:", e)

async def stake(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⛏️ Staking Vault Active\n\n"
        "Earn daily rewards from TiffyAI staking pool.\n"
        "📜 Contract: Auto-burns. Treasury-fueled. Deflationary.\n"
        "📍 Stake Now: https://tiffyai.github.io/Staking/"
    )

async def ai(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👁️ TiffyAI is syncing...\n(Coming soon: talk to the mind behind the chain.)")

async def fallback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💭 TiffyAI is listening... Ask anything.")

# === MAIN APP ===

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("claim", claim))
    app.add_handler(CommandHandler("wallet", wallet))
    app.add_handler(CommandHandler("trade", trade))
    app.add_handler(CommandHandler("price", price))
    app.add_handler(CommandHandler("stake", stake))
    app.add_handler(CommandHandler("ai", ai))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, fallback))

    print("🤖 TiffyAI is awake.")
    app.run_polling()
