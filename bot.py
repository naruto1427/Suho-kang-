from threading import Thread
from http.server import BaseHTTPRequestHandler, HTTPServer
from pyrogram import Client, idle
from plugins.cb_data import app as Client2
from config import *
import pyromod
import pyrogram.utils

# Dummy server for health checks
def run_dummy_server():
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Bot is running!")
    server = HTTPServer(("", 8080), Handler)
    server.serve_forever()

Thread(target=run_dummy_server).start()

# Pyrogram config patch
pyrogram.utils.MIN_CHAT_ID = -999999999999
pyrogram.utils.MIN_CHANNEL_ID = -100999999999999

# Initialize bot
bot = Client("Renamer", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH, plugins=dict(root='plugins'))

if STRING_SESSION:
    apps = [Client2, bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
else:
    bot.run()
