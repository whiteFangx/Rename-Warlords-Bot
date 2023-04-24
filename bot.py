import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5977287848:AAEt3eZQQvdFgFPBqyBooYswn9yVUU4kpps")

API_ID = int(os.environ.get("API_ID", "1834575"))

API_HASH = os.environ.get("API_HASH", "29716347f1926810cdeeae2d23b99862")

STRING = os.environ.get("STRING", "")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
