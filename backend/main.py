from telebot import TeleBot

from config import MAIN_DB_URL, GPT_API_KEY, TELEGRAM_API_KEY
from app.models import Database
from app.commands import Commands
from app.daily_uses_update import Update

DEBUG = True
DB_CONFIG = {
    'pool_size': 10,
    'pool_timeout': 30,
    'pool_recycle': 3600,
    'max_overflow': 10,
    'echo': DEBUG,
}

ENGINE = Database(MAIN_DB_URL, DB_CONFIG).engine

BOT = TeleBot(TELEGRAM_API_KEY, parse_mode='html')

CONTENT_AMOUNT = 10
Commands(BOT, ENGINE, GPT_API_KEY, CONTENT_AMOUNT, DEBUG).handle_messages()
Update(ENGINE)

BOT.polling(none_stop=True)







