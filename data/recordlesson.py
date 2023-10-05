import sqlite3


class RecordForLesson:

    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def create_table(self):
        connection = self.connection
        cursor = self.connection.cursor()
        cursor.execute(
            """
                CREATE TABLE IF NOT EXISTS recordlesson (
                user_id INTEGER PRIMARY KEY,
                user_name STRING,
                direction STRING,
                weekday STRING
                time_lesson STRING
                your_phone String)
            """)
        return connection

    def add_data(self,user_id,your_name,direction,weekday,time_lesson,your_phone):
        with self.connection:
            data = self.cursor.execute("""
                INSERT INTO users (user_id, your_name, direction, weekday, time_lesson, your_phone) VALUES (?,?,?,?,?,?)""",
                                       (user_id, your_name,direction,weekday,time_lesson,your_phone))
            return data