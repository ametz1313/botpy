import requests
import telegram
from time import sleep

# Replace these values with your own
BOT_TOKEN = "6159945847:AAEKHNX7DoC21bUGLNU2WDBdVGImJAXZGbk"
CHANNEL_NAME = "@filterchiz"
URL_TO_READ = "https://raw.githubusercontent.com/ametz1313/All/main/Ssr.txt"

# Create a Telegram bot instance
bot = telegram.Bot(token=BOT_TOKEN)

# Read lines from URL and send them to Telegram channel
while True:
    try:
        response = requests.get(URL_TO_READ)
        if response.status_code == 200:
            lines = response.text.splitlines()
            for line in lines:
                bot.send_message(chat_id=CHANNEL_NAME, text=line)
        else:
            print(f"Error reading URL: {response.status_code}")
        # Wait for 5 minutes before checking the URL again
        sleep(300)
    except Exception as e:
        print(f"Error occurred: {e}")
