import json
import requests
import time
import asyncio

from asyncio import sleep
from pyrogram import Client, filters
#from configs import Config                         # aqui dice que de configs importe lan classe config
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

@Client.on_message(filters.command(["idk"], ["/", "."]))
async def chaid(_, m: Message):
    await m.reply(f"""    
<b>Chat Id</b> : <b><code>{m.chat.id}</code></b>

    """)