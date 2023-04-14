from pyrogram.types import Message, InlineKeyboardButton
from pyrogram import enums
from typing import Union
from datetime import datetime
import time
from datetime import datetime

omwer = 5416957433
admin = 5416957433
idchat = [-1001882398908, -1001749398513, -1001698867343, -1001844059236, -1001640249431, -1001787426503, -1001576963422]

CMD = ["/", "."]
spam_times = {}

def anti_spam(message, time_limit):
    chat_id = message.chat.id
    message_id = message.message_id
    if chat_id in spam_times:
        elapsed_time = time.time() - spam_times[chat_id]["time"]
        if elapsed_time < time_limit:
            return False
    spam_times[chat_id] = {
        "message_id": message_id,
        "time": time.time()
    }
    return True


def make_ordinal(n):
    n = int(n)
    suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    return str(n) + suffix



def get_part_of_day():
    h = datetime.now().hour
    if h < 12:
        return "Buenos Dias <b>⛅</b>"
    elif h >= 11 and h < 16:
        return "Buenas Tarde<b>☀️</b>"
    elif h >= 17 and h < 19:
        return "Buenas Nochesita <b>🌅</b>"
    elif h >= 19 and h < 24:
        return "Buenas Noches <b>🌃</b> "
    else:
        return "Buenos Dias <b>⛅</b>"
    


def extract_user(message: Message) -> Union[int, str]:
    """extracts the user from a message"""
    # https://github.com/SpEcHiDe/PyroGramBot/blob/f30e2cca12002121bad1982f68cd0ff9814ce027/pyrobot/helper_functions/extract_user.py#L7
    user_id = None
    user_first_name = None
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        user_first_name = message.reply_to_message.from_user.first_name

    elif len(message.command) > 1:
        if (
            len(message.entities) > 1 and
            message.entities[1].type == enums.MessageEntityType.TEXT_MENTION
        ):
           
            required_entity = message.entities[1]
            user_id = required_entity.user.id
            user_first_name = required_entity.user.first_name
        else:
            user_id = message.command[1]
            # don't want to make a request -_-
            user_first_name = user_id
        try:
            user_id = int(user_id)
        except ValueError:
            pass
    else:
        user_id = message.from_user.id
        user_first_name = message.from_user.first_name
    return (user_id, user_first_name)
