from datos import *
from pyrogram import Client, filters,enums
from pyrogram.types import Message
from pulpos.plantillas import _start 
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
import asyncio

@Client.on_message(filters.command("start", ["/", "."]))
async def start(client, message):
    await message.reply_chat_action(enums.ChatAction.TYPING)
    m=await message.reply_sticker("CAACAgUAAxkBAAIFNGJSlfOErbkSeLt9SnOniU-58UUBAAKaAAPIlGQULGXh4VzvJWoeBA")
    await asyncio.sleep(1.5)
    await m.delete()
    with open(file='plugins/usuarios/users.txt',mode='r+',encoding='utf-8') as archivo:
        x = archivo.readlines()
        if str(message.from_user.id) + '\n' in x:
            tiempo = time.strftime("%d %m %Y")
            dt_string = datetime.now().strftime("%B-%Y")
            hora = datetime.now().strftime("%H:%M %p")
            day = make_ordinal(datetime.now().strftime("%d"))
            text = _start.format(
            user=message.from_user.first_name, 
            user_id=message.from_user.id,
            day = day,
            hora=hora,
            tiempo=tiempo,
            dt_string=dt_string,
            estado=get_part_of_day()
            )
    
            await client.send_photo(message.chat.id, "https://imgur.com/a/yOiJfkM" , f'{text}',
            reply_markup=InlineKeyboardMarkup(
        [
            [
        
                InlineKeyboardButton("ᴀʙɪɢᴀɪʟ • [ 🌻 ]", url="https://t.me/AbigailRexChannel")
                
            ]
            
        ]

    )
    
 )


        else:
            return await message.reply(f'<b>⎚ Registrese <code>/register</code></b>')
    