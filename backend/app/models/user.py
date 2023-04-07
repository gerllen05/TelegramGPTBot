from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey

from .database import BASE


class User(BASE):
    __tablename__ = "Users"

    id = Column("id", Integer, primary_key=True)
    telegramUserId = Column("telegramUserId", Integer, nullable=False)
    telegramFirstName = Column("telegramFirstName", String(16))
    telegramLastName = Column("telegramLastName", String(16))
    createdAt = Column("createdAt", DateTime, nullable=False)
    dailyQuota = Column("dailyQuota", Integer, nullable=False, default=30)
    usedThisDay = Column("usedThisDay", Integer, nullable=False, default=0)
    tokensSpent = Column("tokensSpent", Integer, nullable=False, default=0)
    hasSubscribtion = Column("hasSubscribtion", Boolean, nullable=False)
    isAdmin = Column("isAdmin", Boolean, nullable=False)

    def __init__(self, telegramUserId, telegramFirstName, telegramLastName, createdAt, dailyQuota=30, usedThisDay=0, tokensSpent=0, hasSubscribtion=False, isAdmin=False):
        self.telegramUserId = telegramUserId
        self.telegramFirstName = telegramFirstName
        self.telegramLastName = telegramLastName
        self.createdAt = createdAt
        self.dailyQuota = dailyQuota
        self.usedThisDay = usedThisDay
        self.tokensSpent = tokensSpent
        self.hasSubscribtion = hasSubscribtion 
        self.isAdmin = isAdmin

    def __repr__(self):
        return f""" 
            telegramUserId: {self.telegramUserId}
            telegramFirstName: {self.telegramFirstName}
            telegramLastName: {self.telegramLastName}
            createdAt: {self.createdAt}
            dailyQuota: {self.dailyQuota}
            usedThisDay: {self.usedThisDay}
            tokensSpent: {self.tokensSpent}
            hasSubscribtion: {self.hasSubscribtion}
            isAdmin: {self.isAdmin} """