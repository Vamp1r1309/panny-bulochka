import sqlite3


class DataBase:
    """База данных для поьзователей"""
    def __init__(self, db_file: object) -> None:
        self.connect = sqlite3.connect(db_file)
        self.cursor = self.connect.cursor()

    # async def add_userID(self, chat_id):
    #     with self.connect:
    #         # check = await self.check_chat_id(chat_id)
    #         # if not check:
    #         return self.cursor.execute("""INSERT INTO user (telegramID) VALUES (?)""", (chat_id,))

    # async def check_chat_id(self, chat_id):
    #     with self.connect:
    #         check_id = self.cursor.execute("""SELECT telegramID FROM user WHERE telegramID=(?)""", (chat_id,)).fetchone()
    #         return check_id is None

    async def add_users(self, chat_id, name, year, phone):
        with self.connect:
            return self.cursor.execute("""INSERT INTO user  (telegramID, username, olds, phone) VALUES (?, ?, ?, ?)""",
                                        (chat_id, name, year, phone,))
