from telebot import TeleBot

from config import DEBUG, GPT_API_KEY, TELEGRAM_API_KEY
from app.models import Database
from app.commands import Commands
from app.daily_uses_update import Update

print('Creating engine...')
ENGINE = Database().engine

print('Connecting to Telegram API...')
BOT = TeleBot(TELEGRAM_API_KEY, parse_mode='html')

print('Creating bot commands handler...')

Commands(BOT, ENGINE, DEBUG).handle_messages()
Update(ENGINE)

print('Everything is ready')
BOT.polling(none_stop=True)







