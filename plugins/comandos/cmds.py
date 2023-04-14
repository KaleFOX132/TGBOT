from pyrogram import Client, filters
from pyrogram.types import Message
from pulpos.plantillas import _cmdbotons, _cmd

@Client.on_message(filters.command("cmds", ["/", "."]))
async def cmds(client, message):
    with open(file='plugins/usuarios/users.txt',mode='r+',encoding='utf-8') as archivo:
        x = archivo.readlines()
        if str(message.from_user.id) + '\n' in x:
            await client.send_message(message.chat.id, _cmd, reply_markup= _cmdbotons, reply_to_message_id =message.id)
        else:
            return await message.reply(f'<b>⎚ Registrese <code>/register</code></b>')
    