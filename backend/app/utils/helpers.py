from datetime import datetime

from sqlalchemy.orm import sessionmaker
from app.models import User, MessageItem


def get_session(engine):
    Session = sessionmaker(engine)
    session = Session()
    return session

def get_last_messages(session, user, amount):
    msgs = session.query(MessageItem).filter(MessageItem.userId == user.id).order_by(MessageItem.id.desc()).limit(amount).all()
    return msgs

def get_user_by_telegram_id(session, message):
    user = session.query(User).filter(User.telegramUserId == message.from_user.id).first()
    if user:
        return user
    else:
        user = User(message.from_user.id, message.from_user.first_name, message.from_user.last_name, datetime.now())
        session.add(user)
        session.commit()
        return user
    
def check_daily_quota_exceeded(user: User):
    if (user.usedThisDay == user.dailyQuota) or user.isAdmin:
        return True
    else: 
        return False
    

