from os import getenv
from pytz import timezone

def str_to_bool(debug: str):
    if debug == 'True': 
        return True 
    else: 
        return False
    
MAIN_DB_URL = getenv("MYSQL_URL")
POOL_SIZE = int(getenv("POOL_SIZE"))
POOL_TIMEOUT = int(getenv("POOL_TIMEOUT"))
POOL_RECYCLE = int(getenv("POOL_RECYCLE"))
MAX_OVERFLOW = int(getenv("MAX_OVERFLOW"))
ECHO = str_to_bool(getenv("ECHO"))

DEBUG = str_to_bool(getenv("DEBUG"))

TELEGRAM_API_KEY = getenv("TELEGRAM_API_KEY")

GPT_API_KEY = getenv("GPT_API_KEY")
CONTENT_AMOUNT = int(getenv("CONTENT_AMOUNT"))

TIMEZONE = timezone(getenv("TIMEZONE"))

