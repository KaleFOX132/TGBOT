import requests 
from pyrogram import Client, filters
import time
from psutil import cpu_percent, virtual_memory, disk_usage, boot_time

bot_uptime = int(time.time())
from platform import python_version
from io import BytesIO
from pyrogram import filters, __version__
#Uptime
app = Client
@app.on_message(filters.command("prelist"))
async def status(client, message):
    with open(file='plugins/usuarios/admins.txt',mode='r+',encoding='utf-8') as archivo:
        x = archivo.readlines()
        if str(message.from_user.id) + '\n' in x:
            with open(file='plugins/usuarios/premium.txt',mode='r+',encoding='utf-8') as archivo:
                x = archivo.readlines()

            chats = x
            
            
            chatfile = "Esta es la lista de los usuarios Prmeium de abigail.\n\n"
            P = 1
            for chat in chats:
                try:
                    chatfile += "{} : {}".format(P, chat)
                    P = P + 1
                except:
                    pass
            with BytesIO(str.encode(chatfile)) as output:
                output.name = "Usuarios premium.txt"
                await message.reply_document(document=output, disable_notification=True)