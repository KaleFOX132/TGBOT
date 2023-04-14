from pyrogram import Client, filters
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

@Client.on_message(filters.command(["repre"], ["/", "."]))
async def register(_, m: Message):
    with open(file='plugins/usuarios/admins.txt',mode='r+',encoding='utf-8') as archivo:
        x = archivo.readlines()
        if str(m.from_user.id) + '\n' in x:
            data = m.text.split(" ", 2)
            if len(data) < 2:
                await m.reply_text("<b>⎚ Usar <code>/key dias-id-credit</code></b>")
                return
            
            ccs  = data[1]
            card = ccs.split("-")
            hola   = card[0]

            with open('plugins/usuarios/premium.txt', 'r') as f:
                lineas = f.readlines()

            dato_a_eliminar = f'{hola}'
            lineas = [linea for linea in lineas if dato_a_eliminar not in linea]

            with open('plugins/usuarios/premium.txt', 'w') as f:
                f.writelines(lineas)

                await m.reply(f'<b>El usuario <code>{hola}</code> dejo de ser premium</b>')
        else:
            return await m.reply(f'<b>⎚Este comando es para admins</b>')


