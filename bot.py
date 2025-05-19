import os
from flask import Flask, request
from pyrogram import Client, filters
from pyrogram.types import Message

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

app = Flask(__name__)
bot = Client("webhook_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

WEBHOOK_URL = f"https://{os.environ.get('RENDER_EXTERNAL_HOSTNAME')}"  # Render sets this automatically
PORT = int(os.environ.get("PORT", 5000))  # Render also injects PORT

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def telegram_webhook():
    bot.process_new_updates([request.get_json(force=True)])
    return "OK"

@bot.on_message(filters.command("start"))
async def start_cmd(client, message: Message):
    await message.reply("Hello! I'm alive using webhook on Render.")

if __name__ == "__main__":
    bot.start()
    bot.set_webhook(WEBHOOK_URL + f"/{BOT_TOKEN}")
    app.run(host="0.0.0.0", port=PORT)
