import telegram
import requests

# Replace YOUR_TOKEN and YOUR_CHANNEL_ID with your actual token and channel ID
bot = telegram.Bot(token='6159945847:AAEKHNX7DoC21bUGLNU2WDBdVGImJAXZGbk')
channel_id = '-1001482956376'

# Replace URL with the URL of the file you want to read
url = 'https://github.com/ametz1313/All/blob/main/Ssr.txt'

# Make a GET request to the given URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Split the response into lines and send each line as a separate message to the channel
    for line in response.text.split('\n'):
        async def send_messages_to_channel(bot, channel_id, messages):
            for line in messages:
                await bot.send_message(chat_id=channel_id, text=line)
else:
    print('Error reading URL:', response.status_code, response.reason)
