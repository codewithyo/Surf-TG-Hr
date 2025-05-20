from os import getenv
from dotenv import load_dotenv
from pathlib import Path

if Path("config.env").exists():
    load_dotenv("config.env")

class Telegram:
    API_ID = int(getenv("API_ID", "24439819"))
    API_HASH = getenv("API_HASH", "41f6d80d671bc8a9dfaa13f41ab5aadc")
    BOT_TOKEN = getenv("BOT_TOKEN", "7248590334:AAGmrgRmoPFgDDxik-9yHf3hcJYWltxPoFU")
    PORT = int(getenv("PORT", 8080))
    SESSION_STRING = getenv("SESSION_STRING", "")
    BASE_URL = getenv("BASE_URL", "").rstrip('/')
    DATABASE_URL = getenv("DATABASE_URL", "mongodb+srv://hrbots94:Yatin123@hrfile.orihnb1.mongodb.net/?retryWrites=true&w=majority&appName=HRfile")
    AUTH_CHANNEL = [channel.strip() for channel in getenv("AUTH_CHANNEL", "-1002381223249").split(",") if channel.strip()]
    THEME = getenv("THEME", "quartz").lower()
    USERNAME = getenv("USERNAME", "admin")
    PASSWORD = getenv("PASSWORD", "admin")
    ADMIN_USERNAME = getenv("ADMIN_USERNAME", "Hr123")
    ADMIN_PASSWORD = getenv("ADMIN_PASSWORD", "Hr@123")
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '10'))
    MULTI_CLIENT = getenv('MULTI_CLIENT', 'False')
    HIDE_CHANNEL = getenv('HIDE_CHANNEL', 'False')
