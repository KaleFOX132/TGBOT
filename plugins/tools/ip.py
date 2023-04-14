import requests 
from pyrogram import Client, filters
from pyrogram.types import Message
from pulpos.plantillas import _cmdbotons, _cmd

@Client.on_message(filters.command("ip"))
async def cmds(client, message):
    with open(file='plugins/usuarios/users.txt',mode='r+',encoding='utf-8') as archivo:
        x = archivo.readlines()
        if str(message.from_user.id) + '\n' in x:
            zipcode = message.text[len('/ip '):]
            if not zipcode:
               await message.reply("<b>⎚ Usar <code>/ip 1.1.1.1</code><b>")
            spli = zipcode.split()
            ips = spli[0]
            if not spli:
                await message.reply_text(f'<b>⎚ Usar <code>/ip 1.1.1.1</code><b>')
            
            headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'es-ES,es;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',}
            
            response = requests.get(f'http://ipwho.is/{ips}', headers=headers, verify=False).json()
            ip = response['ip']
            flag = response['flag']['emoji']
            connection = response['connection']['asn']
            connection1 = response['connection']['org']
            connection2 = response['connection']['isp']
            connection3 = response['connection']['domain']
            timezone = response['timezone']['id']
            timezone1 = response['timezone']['abbr']
            timezone2 = response['timezone']['is_dst']
            timezone3 = response['timezone']['utc']
            timezone4 = response['timezone']['current_time']

            await message.reply(f"""<b>
⎚  𝐈𝐏 𝐂𝐇𝐄𝐂𝐊 
⎚ 𝐈𝐩:  <code>{ip}</code> ✅
━━━━━━━━━━━━━━
⎚ 𝐂𝐢𝐭𝐲: <code>{timezone} {flag}</code>
⎚ 𝐈𝐩𝐬: <code>{connection2}</code>
⎚ 𝐀𝐛𝐛𝐫 : <code>{timezone1}</code>
⎚ 𝐃𝐨𝐦𝐢𝐧𝐢𝐨: <code>{connection3}</code>
⎚ 𝐎𝐫𝐠: <code>{connection1}</code>
⎚ 𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐁𝐲: @{message.from_user.username}
━━━━━━━━━━━━━━
⎚ Create <b><a href="tg://resolve?domain=RexAwait">𝗿𝗲𝘅 hᴀᴡᴀɪɪ |「💻」</a></b>

    </b>""")
        else:
            return await message.reply(f'<b>⎚ Registrese <code>/register</code></b>')
    
            




