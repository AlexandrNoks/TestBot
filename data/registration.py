import sqlite3


class Registration:
    def __init__(self,db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def create_table(self):
        connection = self.connection
        cursor = self.connection.cursor()
        cursor.execute(
            """
                CREATE TABLE IF NOT EXISTS registration (
                user_id INTEGER PRIMARY KEY,
                user_status STRING,
                your_name STRING,
                direction STRING,
                name_children STRING,
                age_children INTEGER,
                your_phone STRING)
            """
        )
        return connection

    # Метод добавляет пользователя
    def add_user(self,user_id,user_status,your_name,direction,weekday,time_lesson,your_phone):
        with self.connection:
            data = self.cursor.execute("""
                INSERT INTO users (user_id,user_status,your_name, direction, weekday, time_lesson, your_phone) VALUES (?,?,?,?,?,?,?)""",
                                       (user_id,user_status,your_name,direction,weekday,time_lesson,your_phone))
            return data
    # Проверка наличие пользователя в базе данных

    def existing_user(self,user_id) -> bool:
        data = self.cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchall()
        return bool(len(data))

    def get_user(self,user_id):
        data = self.cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchone()
        return data

    def baned_user(self,user_status):
        user_update_status = self.cursor.execute("UPDATE users SET user_status = ? WHERE user_status = ?",(user_status,))
        return user_update_status

    def kick_user(self,user_id):
        user = self.cursor.execute("DELETE * FROM users WHERE user_id = ?", (user_id,)).fetchone()
        return user



