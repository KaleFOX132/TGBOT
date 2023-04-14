import requests 
from pyrogram import Client, filters
from pyrogram.types import Message
from pulpos.plantillas import _cmdbotons, _cmd

@Client.on_message(filters.command("rand"))
async def cmds(client, message):
    with open(file='plugins/usuarios/users.txt',mode='r+',encoding='utf-8') as archivo:
        x = archivo.readlines()
        if str(message.from_user.id) + '\n' in x:
            api = requests.get("https://randomuser.me/api/?nat=us&inc=name,location").json()

            mr = api["results"][0]["name"]["title"]
            nombre = api["results"][0]["name"]["first"]
            last = api["results"][0]["name"]["last"]
            loca = api["results"][0]["location"]["street"]["name"]
            nm = api["results"][0]["location"]["street"]["number"]
            city = api["results"][0]["location"]["city"]
            state = api["results"][0]["location"]["state"]
            country = api["results"][0]["location"]["country"]
            postcode = api["results"][0]["location"]["postcode"]
            latitude = api["results"][0]["location"]["coordinates"]["latitude"]
            longitude = api["results"][0]["location"]["coordinates"]["longitude"]
            
            await message.reply(f"""
        <b> 
⎚ 𝐅𝐚𝐤𝐞 𝐀𝐝𝐝𝐫𝐞𝐬𝐬
⎚ 𝐍𝐚𝐦𝐞: <code>{mr} {nombre} {last}</code>
⎚ 𝐒𝐭𝐫𝐞𝐞𝐭:  <code>{state}</code>
⎚ 𝐂𝐢𝐭𝐲: <code>{city}</code>
⎚ 𝐒𝐭𝐚𝐭𝐞:<code> {loca} {nm}</code>
⎚ 𝐙𝐢𝐩: <code> {postcode}</code>
⎚ 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country}</code>
⎚ 𝐂𝐡𝐞𝐤𝐞𝐝 𝐁𝐲 <code> @{message.from_user.username}[Free User]</code>
━━━━━━━━━━━━━━
⎚ Create <b><a href="tg://resolve?domain=RexAwait">𝗿𝗲𝘅 hᴀᴡᴀɪɪ |「💻」</a></b>
 </b>""")
        else:
            return await message.reply(f'<b>⎚ Registrese <code>/register</code></b>')
    