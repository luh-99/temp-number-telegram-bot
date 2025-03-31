import os
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, filters

# Get the bot token from the environment variable
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

# Create the Updater and pass in the bot token
updater = Updater(TELEGRAM_TOKEN, use_context=True)

# Define command handlers
def start(update, context):
    update.message.reply_text("Hello! I am your bot.")

def echo(update, context):
    update.message.reply_text(update.message.text)

# Set up the command and message handlers
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

# Start the bot
updater.start_polling()
updater.idle()
