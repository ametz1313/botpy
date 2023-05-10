import telebot
from telegraf import Telegraf
import requests
import schedule
import time

# Create a new Telegraf instance
tg = Telegraf('YOUR_TELEGRAM_BOT_TOKEN')

# Define the URL of the web page to fetch
url = 'https://www.example.com/page.txt'

# Define the ID of the Telegram channel to send messages to
channel_id = '@your_channel_name'

# Define a function to fetch the contents of the web page and send them to the channel
def fetch_and_send():
    # Fetch the contents of the web page
    response = requests.get(url)

    # Split the contents into lines
    lines = response.text.strip().split('\n')

    # Send each line to the Telegram channel
    for line in lines:
        tg.send_message(channel_id, line)

# Schedule the function to run every 30 minutes
schedule.every(30).minutes.do(fetch_and_send)

# Start the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
