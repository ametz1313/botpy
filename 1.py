import os
from telegraf import Telegraf

# Create a new Telegraf instance with your Telegram Bot API token
tg = Telegraf(os.environ.get('BOT_TOKEN'))

# Define a function to handle the /start command
@tg.on('/start')
def start_command(ctx):
    ctx.reply('Hello! This is a simple Telegram bot.')

# Start the bot
tg.start_polling()
