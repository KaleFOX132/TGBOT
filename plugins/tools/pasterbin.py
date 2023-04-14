
import os
import re
import json
import aiohttp
import requests
from pyrogram import Client, filters

#Headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
    "content-type": "application/json",
}

#Pastebins
async def p_paste(message, extension=None):
    siteurl = "https://pasty.lus.pm/api/v1/pastes"
    data = {"content": message}
    try:
        response = requests.post(url=siteurl, data=json.dumps(data), headers=headers)
    except Exception as e:
        return {"error": str(e)}
    if response.ok:
        response = response.json()
        purl = (
            f"https://pasty.lus.pm/{response['id']}.{extension}"
            if extension
            else f"https://pasty.lus.pm/{response['id']}.txt"
        )
        return {
            "url": purl,
            "raw": f"https://pasty.lus.pm/{response['id']}/raw",
            "bin": "Pasty",
        }
    return {"error": "Unable to reach pasty.lus.pm"}


@Client.on_message(filters.command(["paster"]))
async def who_is(client, message):
    with open(file='plugins/usuarios/premium.txt',mode='r+',encoding='utf-8') as archivo:
        x = archivo.readlines()
        if str(message.from_user.id) + '\n' in x:
            tex_t = message.text
            if ' ' in message.text:
                message_s = message.text.split(" ", 1)[1]
            elif message.reply_to_message:
                message_s = message.reply_to_message.text
            else:
                await message.reply("<b>⎚ Usar <code>/paster texto a subir a pasterbin</code></b>")
            if not tex_t:
                if not message.reply_to_message:
                    await pablo.edit("<b>⎚ Formato invalido text|cocumento</b>")
                    return
                if not message.reply_to_message.text:
                    file = await message.reply_to_message.download()
                    m_list = open(file, "r").read()
                    message_s = m_list
                    os.remove(file)
                elif message.reply_to_message.text:
                    message_s = message.reply_to_message.text
            else:
                pablo = await message.reply_text("<b>⎚ `Subiendo ala PasterBind...`</b>")

            ext = "txt"
            x = await p_paste(message_s, ext)
            p_link = x["url"]
            p_raw = x["raw"]

            pasted = f"""<b>
━━━━━━━━━━━
⎚ Text online

⎚ Link : 
⎚  •[ [ Presione ]({p_link}) ]
━
⎚ Link De Raw: 
⎚ •[ [ Presione Raw]({p_raw}) ]

⎚ Status : Valido ✅
━━━━━━━━━━━
⎚ Create <b><a href="tg://resolve?domain=RexAwait">𝗿𝗲𝘅 hᴀᴡᴀɪɪ |「💻」</a></b>
   </b> 
    """
            await pablo.edit(pasted, disable_web_page_preview=True)
        
        else:
            return await message.reply(f'<b>⎚ Chat no autorizado | O no eres Premium.</b>')



