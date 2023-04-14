from pyrogram import Client, filters
from pyrogram.types import Message
from pulpos.plantillas import _start 
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
import random
from random import randint


@Client.on_message(filters.command("key", ["/", "."]))
async def start(client, message):
    with open(file='plugins/usuarios/admins.txt',mode='r+',encoding='utf-8') as archivo:
        x = archivo.readlines()
        if str(message.from_user.id) + '\n' in x:
            data = message.text.split(" ", 2)
            if len(data) < 2:
                await message.reply_text("<b>⎚ Usar <code>/key dias-id-credit</code></b>")
                return

            ccs  = data[1]
            card = ccs.split("-")
            dia   = card[0]
            user= card[1]
        
            cre = card[2]

            key = 'abigail''~'+str(randint(1000,9000))+'~'f'{user}''~'f'{cre}'
            print(key)
            archivo.write('{}\n\n'.format(key))

            text = f"""<b>
⎚ Key User
        
⎚ Key : Gen key Aprovad ✓
⎚ Credito : <Code>{cre}</code>
⎚ Id : <code>{user}</code>
⎚ Dias : <code>{dia}</code>
━━
<code>{key}</code> 
━━
⎚ Taken : <code>0.1 s</code>
━━━━━━━━━━
⎚ 𝗖𝗿𝗲𝗮𝘁𝗲: <b><a href="tg://resolve?domain=RexAwait">𝗿𝗲𝘅 hᴀᴡᴀɪɪ |「💻」</a></b></b>"""
            with open(file='plugins/usuarios/keys.txt',mode='r+',encoding='utf-8') as archivo:
                        x = archivo.readlines()
                        
                        archivo.write('{}\n\n'.format(key))

            await client.send_photo(message.chat.id, "https://imgur.com/a/SBTjC1l" , f'{text}',
                    reply_markup=InlineKeyboardMarkup(
                [
                    [
                
                        InlineKeyboardButton("C L A I M  👑 ", url="https://t.me/AbigailRexBot")
                        
                    ]
                    
                ]

            )
            
        )
            
        else:
            return await message.reply(f'<b>⎚Este comando es para admins</b>')



