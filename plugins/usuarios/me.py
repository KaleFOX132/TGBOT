from pyrogram import Client, filters
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

@Client.on_message(filters.command(["me","yo","my","myacc"], ["/", "."]))
async def register(_, m: Message):
    user=m.from_user.first_name
    user_id =m.from_user.id
    seller = [5416957433]


    admin = [5061313850]
    
    if m.from_user.id in seller or m.from_user.id in seller:
        await m.reply(f"""<b>
⎚ User Information

⎚ Name            <code>{user} </code>
⎚ ID                   <code>{user_id}</code>
⎚ Credits           <code>9999</code>
⎚ Status           <code>CREADOR [ 🥀 ]</code>
⎚ Plan               <code>DIAMANTE [ 🛡 ]</code>
━━━━━━━━━━━━━━━━━━━━━━
⎚ Create <b><a href="tg://resolve?domain=RexAwait">𝗿𝗲𝘅 hᴀᴡᴀɪɪ |「💻」</a></b>
    </b>""")
    elif m.from_user.id in admin:
        await m.reply(f"""<b>
⎚ User Information

⎚ Name           <code>{user} </code>
⎚ ID                <code> {user_id}</code>
⎚ Credits              <code>1050</code>
⎚ Status          <code>ADMINS</code>
⎚ Plan              <code>VIP 🔥</code>
━━━━━━━━━━━━━━━━━━━━━━
⎚ Create <b><a href="tg://resolve?domain=RexAwait">𝗿𝗲𝘅 hᴀᴡᴀɪɪ |「💻」</a></b>
    </b>""")
     
    else:
       
        with open(file='plugins/usuarios/premium.txt',mode='r+',encoding='utf-8') as archivo:
            x = archivo.readlines()

            if str(m.from_user.id) + '\n' in x:            
                await m.reply(f"""<b>
⎚ User Information

⎚ Name              <code>{user} </code>
⎚ ID                   <code> {user_id}</code>
⎚ Credits              <code>500</code>
⎚ Status             <code>PLAN P</code>
⎚ Plan                 <code>PREMIUM 👑</code>
━━━━━━━━━━━━━━━━━━━━━━
⎚ Create <b><a href="tg://resolve?domain=RexAwait">𝗿𝗲𝘅 hᴀᴡᴀɪɪ |「💻」</a></b>
            </b>""")
                    
            else:
                await m.reply(f"""<b>
⎚ User Information

⎚ Name              <code>{user} </code>
⎚ ID                   <code> {user_id}</code>
⎚ Credits              <code>12</code>
⎚ Status             <code>USER</code>
⎚ Plan                 <code>FREE 🌧</code>
━━━━━━━━━━━━━━━━━━━━━━
⎚ Create <b><a href="tg://resolve?domain=RexAwait">𝗿𝗲𝘅 hᴀᴡᴀɪɪ |「💻」</a></b>
    </b>""")