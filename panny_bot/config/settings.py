import os
from dotenv import load_dotenv
from db.db_panni import DataBase


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
db = DataBase(os.getenv("FILE_DB"))
print(db)
