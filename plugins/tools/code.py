from pyrogram import filters
from aiohttp import ClientSession
from pyrogram import Client as bot
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from asyncio import gather
from datetime import datetime, timedelta
from io import BytesIO
from math import atan2, cos, radians, sin, sqrt
from os import execvp
from random import randint
from re import findall
from re import sub as re_sub
from sys import executable
import aiofiles
import speedtest
#from PIL import Image
from pyrogram.types import Message

aiohttpsession = ClientSession()

async def make_carbon(code):
    url = "https://carbonara.vercel.app/api/cook"
    async with aiohttpsession.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image


@bot.on_message(filters.command("code"))
async def carbon_func(_, message):
    with open(file='plugins/usuarios/premium.txt',mode='r+',encoding='utf-8') as archivo:
        x = archivo.readlines()
        if str(message.from_user.id) + '\n' in x:
            if not message.reply_to_message:
                return await message.reply_text(
                    "<b>⎚ Debe usarse sobre un text.</b>"
                )
            if not message.reply_to_message.text:
                return await message.reply_text(
                    "<b>⎚ Debe usarse sobre un text.</b>"
                )
            user_id = message.from_user.id
            m = await message.reply_text("<b>⎚ `Pasando a Img...`</b>")
            carbon = await make_carbon(message.reply_to_message.text)
            await m.edit("`Pasando a Img...`..")
            await message.reply_photo(
                photo=carbon,
                caption="""<b>⎚ Create <b><a href="tg://resolve?domain=RexAwait">𝗿𝗲𝘅 hᴀᴡᴀɪɪ |「💻」</a></b></b>""",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("C R E A D O R", url="https://t.me/RexAwait")]]),                   
            )
            await m.delete()
            carbon.close()
        else:
            return await message.reply(f'<b>⎚ Chat no autorizado | O no eres Premium.</b>')



