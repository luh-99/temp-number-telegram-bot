import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackContext
from telegram.ext import filters

# Get the bot token from the environment variable
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

# Create the Application instance
app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

# Define command handlers
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Hello! I am your bot.")

async def echo(update: Update, context: CallbackContext):
    await update.message.reply_text(update.message.text)

# Set up the command and message handlers
app.add_handler(CommandHandler('start', start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

# Start the bot
app.run_polling()
