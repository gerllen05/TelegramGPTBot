import schedule

from app.utils.helpers import get_session
from app.models import User


class Update:
    def __init__(self, engine):
        self.engine = engine

        schedule.every().day.at('00:00').do(self.daily_uses_update)

    def daily_uses_update(self):
        session = get_session(self.engine)
        for user in session.query(User).all():
            user.usedThisDay = 0
        session.close()

