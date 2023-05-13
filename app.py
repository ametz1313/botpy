import logging

from telegram.ext import Application, CommandHandler, MessageHandler, filters
from queue import Queue
queue = Queue()

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Create the updater
updater = Updater('6159945847:AAHLiJuL75pEZJ1XtlmA214cUcPpMS455Mo', update_queue=Queue())

# Define a command handler
def start(update, context):
    update.message.reply_text('Hello! I am a simple Telegram bot.')

# Define a message handler
def echo(update, context):
    update.message.reply_text(update.message.text)

# Add the handlers to the dispatcher
application.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))

# Start the bot
updater.start_polling()

# Run the bot until you press Ctrl+C
updater.idle()
