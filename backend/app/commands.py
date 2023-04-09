from telebot import TeleBot
from telebot.types import Message 

from config import DEBUG
from app.utils.messages import *
from app.gpt import chat_gpt_query
from app.utils.helpers import get_session, get_user_by_telegram_id, check_daily_quota_exceeded, get_last_messages
from app.models import User, MessageItem 

class Commands:

    def __init__(self, bot: TeleBot, engine):
        self.bot = bot
        self.engine = engine


    async def handle_messages(self):
        @self.bot.message_handler(commands=['start', 'help'])
        async def start(message: Message):
            self.bot.send_message(message.chat.id, HelloMessage)

        @self.bot.message_handler(commands=['quota'])
        async def get_user_uses(message: Message):
            session = get_session(self.engine)
            user = get_user_by_telegram_id(session, message)
            self.bot.reply_to(message, f"Your quota: <b>{user.dailyQuota}</b> messages per day. \nYou have <b>{user.dailyQuota - user.usedThisDay}</b> messages left today.")
            session.close()

        @self.bot.message_handler(commands=['forget'])
        async def get_user_uses(message: Message):
            session = get_session(self.engine)
            user = get_user_by_telegram_id(session, message)
            messages = get_last_messages(session, user)
            for msg in messages:
                msg.isForgotten = True
            session.commit()
            session.close()

        @self.bot.message_handler(content_types='text')
        async def ask_chat_gpt(message: Message):
            if DEBUG:
                print(message.text)
            if not (message.text in ['start', 'help', 'quota']):
                if len(message.text) > 128:
                    self.bot.reply_to(message, TooBigPromptError + len(message.text))
                else:
                    try:
                        # trying to get user from database, if user does not exist it creates user
                        session = get_session(self.engine)
                        user = get_user_by_telegram_id(session, message)

                        # checking if user is allowed to ask questions today
                        if check_daily_quota_exceeded(user):
                            self.bot.reply_to(message, DailyQuotaExceededError)
                        else: 
                            user.usedThisDay += 1
                            session.commit()

                        wait_msg = self.bot.reply_to(message, WaitAnswer + str(user.dailyQuota - user.usedThisDay))
                        chat_id = message.chat.id

                        # adds user's message to database
                        user_message = MessageItem(message.id, user.id, 'user', message.text)
                        session.add(user_message)
                        session.commit()
                        
                        answer = chat_gpt_query(session, user)

                        # adds assistant's answer to database
                        assistant_message = MessageItem(None, user.id, 'assistant', answer[0])
                        session.add(assistant_message)
                        session.commit()

                        user_message.tokensCost += answer[1].prompt_tokens
                        assistant_message.tokensCost += answer[1].completion_tokens
                        user.tokensSpent += answer[1].total_tokens
                        session.commit()
                        session.close()

                        self.bot.delete_message(chat_id, wait_msg.id)
                        self.bot.reply_to(message, ChatGPTAnswer + f"<i>{answer[0]}</i>")
                    except Exception as e:
                        print(e)
            


    
