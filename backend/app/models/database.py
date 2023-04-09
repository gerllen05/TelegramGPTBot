from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

from config import MAIN_DB_URL, POOL_SIZE, POOL_TIMEOUT, POOL_RECYCLE, MAX_OVERFLOW, ECHO


BASE = declarative_base()

class Database:
    def __init__(self):
        self.engine = create_engine(MAIN_DB_URL, 
            pool_size=POOL_SIZE,
            pool_timeout=POOL_TIMEOUT,
            pool_recycle=POOL_RECYCLE,
            max_overflow=MAX_OVERFLOW,
            echo=ECHO)
        try:
            BASE.metadata.create_all(self.engine)
        except Exception as e:
            print(e)

