import os
from dotenv import load_dotenv
from panny_bot.db import DataBase


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
db = DataBase(os.getenv("FILE_DB"))
print(db)
