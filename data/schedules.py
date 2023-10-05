import sqlite3
# class Schedule:
#
#     def __init__(self, db_file):
#         self.connection = sqlite3.connect(db_file)
#         self.cursor = self.connection.cursor()
#
#     def create_table(self):
#         connection = self.connection
#         cursor = self.connection.cursor()
#         cursor.execute(
#             """
#                 CREATE TABLE IF NOT EXISTS schedule (
#                 id INTEGER PRIMARY KEY,
#                 name_pupil STRING,
#                 one_day STRING
#                 time_lesson_oneday STRING
#                 two_day STRING
#                 time_lesson_twoday STRING
#                 your_phone String)
#             """)
#         return connection
#
#
# def add_data(self,id,name_pupil,one_day,time_one_day,two_day,time_two_day,your_phone):
#     with self.connection:
#         data = self.cursor.execute("""
#                 INSERT INTO users (id,name_pupil,one_day,time_one_day,two_day,time_two_day,your_phone) VALUES (?,?,?,?,?,?,?)""",
#                                    (id,name_pupil,one_day,time_one_day,two_day,time_two_day,your_phone))
#         return data

# def get_data(self,):
