import sqlite3
# Класс для sql-запросов
import time
# Таблица с полями: id, user_id, time
# id - пользователя в БД
# user_id пользователя в телеграмме
# time время на которое пользователь был забанен

directions = ["Вокал","Гитара","Танцы"]
def recordlesson(db):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
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

def create_table(db):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS registration (
            user_id INTEGER PRIMARY KEY,
            your_name STRING,
            direction STRING,
            name_children STRING,
            age_children INTEGER,
            your_phone STRING)
        """)
    return connection




# def create_table(db):
#     self.connection = sqlite3.connect(db_file)
# self.cursor = self.connection.cursor()

# def create_db_registration(db):
#     connection = sqlite3.connect(db)
#     cursor = connection.cursor()
#     cursor.execute(
#         """
#             CREATE TABLE IS NOT EXISTS registration (
#             user_id INTEGER PRIMARY KEY,
#             user_name STRING,
#             direction STRING,
#             user_phone STRING,
#             name_children STRING,
#             age_children INTEGER
#         """)
#     return cursor

    # def exists_user(user_id):
    #     with connection:
    #         user = cursor.execute("SELECT * FROM 'users' WHERE 'user_id' = ?", (user_id,)).fetchall()
    #         return bool(len(user))

    # def add_user(user_id,your_name,direction,your_phone,name_children,age_children):
    #     with connection:
    #         return connection.execute("INSERT INTO FROM 'users' ('user_id','your_name', 'direction','your_name','your_phone','name_children',"
    #                                        "'age_children') VALUES (?)", (user_id,your_name,direction,your_phone,name_children,age_children)).fetchone()
    #
    # def get_all_users(self):
    #     with self.connection:
    #         return self.connection.execute("SELECT * FROM 'users'").fetchall()
    #
    # def get_user(self,user_id):
    #     return self.connection.execute("SELECT * FROM 'users' WHERE id = ?", (id,)).fetchone()
    #
    # # Метод Возвращает True если время бана пользователя еще не закончилось
    # def mute(self, user_id):
    #     with self.connection:
    #         user = self.cursor.execute("SELECT * 'name_table' FROM 'user_id' = ?", (user_id,)).fetchone()
    #         # Проверяем третье поле таблицы "Время бана"
    #         return int(user[2]) >= int(time.time())
    #
    # # Метод добавляет пользователя в бан, время на которое будет забанен пользователь
    # def add_mute(self, user_id, mute_time):
    #     with self.connection:
    #         return self.connection.execute("UPDATE INTO 'name_table' SET 'mute_time' = ? WHERE 'user_id' = ?",  (int(time.time()) + int(mute_time),user_id))
    #
    # # Метод Удаляет строку из БД по id
    # def del_user(self,user_id):
    #     with self.connection:
    #         return self.connection.execute("DELETE FROM 'recordinglesson' WHERE user_id = ?", (user_id,))




# Метод проверки нахождение пользователя в Базе данных
# который возвращает True если запись одна (len(user_id) = 1)
# Или False если записей не было (len(user_id) = 0)
#     def user_exists(self,user_id):
#         with self.connection:
#             # переменная для создания sql-запроса
#             result = self.cursor.execute("SELECT * FROM 'recordinglesson' WHERE 'user_id' = ?", (user_id,)).fetchall()
#             return bool(len(result))
#
#     def check_weekday(self,weekday):
#         with self.connection:
#             # переменная для создания sql-запроса
#             user = self.user_exists(user_id=7987987989)
#             result = self.cursor.execute("SELECT * FROM 'recordinglesson' WHERE 'weekday' = ?", (weekday,)).fetchall()
#             return bool(len(result))
#
#     def check_freetime(self,user_id,weekday,time_lesson):
#         with self.connection:
#             user_id = self.user_exists(user_id=7987987989)
#             weekday = self.check_weekday(weekday='uuiyiuyiuyi')
#             result = self.cursor.execute("SELECT * FROM 'recordinglesson' WHERE 'time_lesson' = ?", (time_lesson,)).fetchall()
#             result.append(user_id)
#             result.append(weekday)
#             return len(result) == 0
#
# # Метод Добавляет новую запись в базу данных
#     def add_user(self, user_id,user_name,weekday,time_lesson,user_phone):
#         with self.connection:
#             # record_save = self.cursor.execute("SELECT * FROM 'recordinglesson' WHERE 'weekday' = ? 'time_lesson' = ?", (weekday,time_lesson)).fetchall())
#             return self.cursor.execute("INSERT INTO 'recordinglesson' ('user_id,user_name,weekday,time_lesson,phone') VALUES (?)", (user_id,user_name,weekday,time_lesson,user_phone)).fetchone()
#
# # Метод Возвращает все строки из БД в виде списка
#     def get_all_user(self):
#         with self.connection:
#             # переменная для создания sql-запроса
#             result = self.cursor.execute("SELECT * FROM 'chat_message'").fetchall()
#             return result










