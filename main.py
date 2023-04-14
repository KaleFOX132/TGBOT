import os
from configs import Config  
from pyrogram import Client

bot = Client(
    "RexAwaitBot",
    api_hash=Config.API_HASH,   
    api_id=Config.API_ID,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="plugins"),
    )

@bot.on_callback_query()
async def callback_privates(client, callback_query):
    if callback_query.message.reply_to_message.from_user.id != callback_query.from_user.id:
        await callback_query.answer("❗No tienes accesos ❗")
        return
    else:
        await callback_query.continue_propagation()

if __name__ == "__main__":
	os.system('cls')    
	print('iniciado !')         
	bot.run()
	print('iniciado !')