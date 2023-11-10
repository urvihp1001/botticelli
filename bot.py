import os
import pyrogram
import openai
from pyrogram.filters import private
from handlers.message_handler import MessageHandler
from config import Config

# Init the Pyrogram client
app = pyrogram.Client(
    name="my_bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

# Initialise the OPENAI API
openai.api_key = Config.OPENAI_API_KEY

# Initialise the message handler
msg_handler = MessageHandler(openai.api_key)

# Register the message handler with the "private" filter using app.on_message decorator
@app.on_message(private)
def handle_private_message(client, message):
    msg_handler.handle(client, message)

# Run the bot
app.run()
