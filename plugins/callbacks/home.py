from pyrogram import Client, filters
from pyrogram.types import Message
from pulpos.plantillas import _cmdbotons, _cmd

@Client.on_callback_query(filters.regex("home"))
async def home(client, callback_query):
    await callback_query.edit_message_text(
        _cmd,
        reply_markup=_cmdbotons
    )

