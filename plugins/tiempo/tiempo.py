import time


from pyrogram import Client, filters
from pyrogram.types import Message
from pulpos.plantillas import _start 
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

@Client.on_message(filters.command("tiempo", ["/", "."]))
async def start(client, message):
        

    tiempo = time.strftime("%H", time.localtime())

    if tiempo < '12':
        await message.reply('<b>Buenos dias 🌅 </b>')
    if '12' <= tiempo < '18' :
        await message.reply('<b>Buenas tardes 🏞</b>')
    if tiempo >'18':
        await message.reply('<b>Buneas noches 🌃</b>')



