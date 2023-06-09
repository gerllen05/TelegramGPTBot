from os import getenv

MYSQL_PORT = getenv("MYSQL_PORT")
MYSQL_HOST = getenv("MYSQL_HOST")
MAIN_DATABASE = getenv("MYSQL_DATABASE")
MYSQL_USER = getenv("MYSQL_USER")
MYSQL_PASSWORD = getenv("MYSQL_PASSWORD")
MAIN_DB_URL = f"mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MAIN_DATABASE}"

GPT_API_KEY = getenv("GPT_API_KEY")
TELEGRAM_API_KEY = getenv("TELEGRAM_API_KEY")