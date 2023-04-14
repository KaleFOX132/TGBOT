import requests 
from pyrogram import Client, filters
from pyrogram.types import Message
from pulpos.plantillas import _cmdbotons, _cmd

@Client.on_message(filters.command("zip"))
async def cmds(client, message):
    with open(file='plugins/usuarios/users.txt',mode='r+',encoding='utf-8') as archivo:
        x = archivo.readlines()
        if str(message.from_user.id) + '\n' in x:
            zipcode = message.text[len('/zip '):]
        if not zipcode:
            await message.reply("<b>⎚ Usar <code>/zip 10020</code></b>")
        spli = zipcode.split()
        zipo = spli[0]
        

        zip_api = requests.get(f'https://zip.getziptastic.com/v2/US/{zipo}').json()
        
    
        await message.reply(f"""
    <b>
━━━━ [𝐙𝐢𝐩 𝐂𝐨𝐝𝐞] ━━━━━
⎚ 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{zip_api['country']}</code>
⎚ 𝐂𝐨𝐝𝐞_𝐏𝐨𝐬𝐭𝐚𝐥:<code> {zip_api['postal_code']}</code>
⎚ 𝐂𝐢𝐭𝐲: <code>{zip_api['city']}</code>
⎚ 𝐄𝐬𝐭𝐚𝐭𝐞: <code>{zip_api['state_short']}</code>
━━━━━━━━━━━━━━
⎚ Create <b><a href="tg://resolve?domain=RexAwait">𝗿𝗲𝘅 hᴀᴡᴀɪɪ |「💻」</a></b>
    </b>""")