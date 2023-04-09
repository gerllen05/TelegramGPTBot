from os import getenv

def str_to_bool(debug: str):
    if debug == 'True': 
        return True 
    else: 
        return False
    
MAIN_DB_URL = getenv("MYSQL_URL")
POOL_SIZE = getenv("POOL_SIZE")
POOL_TIMEOUT = getenv("POOL_TIMEOUT")
POOL_RECYCLE = getenv("POOL_RECYCLE")
MAX_OVERFLOW = getenv("MAX_OVERFLOW")
ECHO = getenv("ECHO")

DEBUG = str_to_bool(getenv("DEBUG"))

TELEGRAM_API_KEY = getenv("TELEGRAM_API_KEY")

GPT_API_KEY = getenv("GPT_API_KEY")
CONTENT_AMOUNT = getenv("CONTENT_AMOUNT")

