
import os
from datos import *
from pyrogram import Client, filters, enums
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from datetime import datetime
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.command(["info"]))
async def who_is(client, message):
    

    status_message = await message.reply_text(
        "`⎚ Buscando informacion Abigail`"
    )
    await status_message.edit(
        "`⎚ Informacion encontrada.`"
    )
    from_user = None
    from_user_id, _ = extract_user(message)
    try:
        from_user = await client.get_users(from_user_id)
    except Exception as error:
        await status_message.edit(str(error))
        return
    if from_user is None:
        return await status_message.edit("no valid user_id / message specified")
    last_name = from_user.last_name or "<b>None</b>"
    username = from_user.username or "<b>None</b>"
    dc_id = from_user.dc_id or "[User Doesn't Have A Valid DP]"
    message_out_str = f"""<b>⎚ User Information

⎚ Nonbre : {from_user.first_name}    
⎚ Nombre 2 : {last_name}
⎚ Id : <code>{from_user.id}</code>
⎚ Alias : @{username}
⎚ Perfil : <a href='tg://user?id={from_user.id}'><b>C L I C K</b></a>
━━━━━━━━━━
⎚ Taken : <code>6.0 s</code>
⎚ 𝗖𝗿𝗲𝗮𝘁𝗲: <b><a href="tg://resolve?domain=RexAwait">𝗿𝗲𝘅 hᴀᴡᴀɪɪ |「💻」</a></b></b>
   </b> """
    chat_photo = from_user.photo
    if chat_photo:
        local_user_photo = await client.download_media(
            message=chat_photo.big_file_id
        )
        buttons = [[
            InlineKeyboardButton('E X I T', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_photo(
            photo=local_user_photo,
            quote=True,
            reply_markup=reply_markup,
            caption=message_out_str,
            parse_mode=enums.ParseMode.HTML,
            disable_notification=True
        )
        os.remove(local_user_photo)
    else:
        buttons = [[
            InlineKeyboardButton('E X I T', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_text(
            text=message_out_str,
            reply_markup=reply_markup,
            quote=True,
            parse_mode=enums.ParseMode.HTML,
            disable_notification=True
        )
    await status_message.delete()
