import telegram
from telegram.ext import Updater, CommandHandler

# Define your bot token and chat ID
BOT_TOKEN = '6159945847:AAHLiJuL75pEZJ1XtlmA214cUcPpMS455Mo'
CHAT_ID = '-1001482956376'

# Define a function to handle the /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm your Telegram bot.")

# Create an instance of the Updater class and pass in your bot token
updater = Updater(BOT_TOKEN, pass_context=True)

# Register the start command handler with the dispatcher
updater.dispatcher.add_handler(CommandHandler('start', start))

# Start the bot
updater.start_polling()

# Send a test message to the chat
bot = telegram.Bot(token=BOT_TOKEN)
bot.send_message(CHAT_ID, 'Bot started')
