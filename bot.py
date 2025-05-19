from pyrogram import Client, idle
from plugins.cb_data import app as Client2
from config import *
import pyromod
import pyrogram.utils
from threading import Thread
from http.server import HTTPServer, BaseHTTPRequestHandler
import os
from pyrogram import Client

# Dummy HTTP server for Koyeb health check
class DummyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running!")

def run_dummy_server():
    server = HTTPServer(("0.0.0.0", 8080), DummyHandler)
    server.serve_forever()

# Start dummy server in a separate thread
Thread(target=run_dummy_server).start()

# Load credentials from environment variables
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

bot = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

bot.run()
