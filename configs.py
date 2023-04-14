from os import path, getenv

class Config:
    API_ID = int(getenv('API_ID','TU_API_ID'))
    API_HASH = getenv('API_HASH','TU_HASH')
    BOT_TOKEN = getenv('BOT_TOKEN','TU_BOT_TOKEN')

config = Config()
