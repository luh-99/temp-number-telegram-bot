import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext
from telegram.ext import filters

# Get the bot token from the environment variable
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

# Create the Updater and pass in the bot token
updater = Updater(token=TELEGRAM_TOKEN)

# Define command handlers
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! I am your bot.")

def echo(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)

# Set up the command and message handlers
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

# Start the bot
updater.start_polling()
updater.idle()
