from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text

from .database import BASE


class MessageItem(BASE):
    __tablename__ = "Messages"

    id = Column("id", Integer, primary_key=True)
    userId = Column("userId", Integer, ForeignKey("Users.id", ondelete="CASCADE"), nullable=False)
    role = Column("role", String(16), nullable=False)
    content = Column("content", Text, nullable=False)
    createdAt = Column("createdAt", DateTime, nullable=False)
    tokensCost = Column("tokensCost", Integer, nullable=False, default=0)
    isForgotten = Column("isForgotten", Boolean, nullable=False)

    def __init__(self, messageId, userId, role, content, createdAt, tokensCost=0, isForgotten=False):
        self.messageId = messageId
        self.userId = userId
        self.role = role
        self.content = content 
        self.createdAt = createdAt
        self.tokensCost = tokensCost
        self.isForgotten = isForgotten

    def __repr__(self):
        return f""" 
            messageId: {self.messageId}  
            userId: {self.userId}
            role: {self.role}
            content: {self.content}
            createdAt: {self.createdAt}
            tokensCost: {self.tokensCost}
            isForgotten: {self.isForgotten} """