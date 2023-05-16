import random
import urllib.request
from telegram import Bot

# Replace YOUR_TOKEN with your actual bot token and CHANNEL_ID with the ID of the channel you want to send messages to
bot = Bot(token='6159945847:AAHwIV1P7NfgdiPg5_qzh4vOOdPWMDk-LBc')
channel_id = '-1001482956376'

# Read the lines from the remote text file
url = 'https://raw.githubusercontent.com/ametz1313/All/main/Trojan.txt'
with urllib.request.urlopen(url) as f:
    lines = f.readlines()

# Choose 10 random lines from the list
random_lines = random.sample(lines, k=10)

# Send each line as a message to the channel
async def send_messages():
    for line in random_lines:
        await bot.send_message(chat_id=channel_id, text=line.decode().strip())

send_messages()
