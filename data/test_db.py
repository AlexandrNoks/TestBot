import sqlite3


class DBReedLesson:
    def __init__(self,db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def create_table(self):
        connection = self.connection
        cursor = self.connection.cursor()
        cursor.execute(
            """
                CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                your_name STRING,
                direction STRING,
                weekday STRING,
                time_lesson STRING,
                your_phone STRING
            )
        """)
        return connection

    def add_user(self,your_name,direction,weekday,time_lesson,your_phone):
        with self.connection:
            data = self.cursor.execute("""
                INSERT INTO users (your_name, direction, weekday, time_lesson, your_phone) VALUES (?,?,?,?,?)""",
                                       (your_name,direction,weekday,time_lesson,your_phone))
            return data





