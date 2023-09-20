import sqlite3
from datetime import datetime
from states.state_registration import Registered
# Класс для sql-запросов
import time
# Таблица с полями: id, user_id, time
# id - пользователя в БД
# user_id пользователя в телеграмме
# time время на которое пользователь был забанен
# Таблица Users с полями
# id
# user_id
# user_name
# direction
# user_phone
# name_pupil
# age_pupil

directions = ["Вокал","Гитара","Танцы"]
class Users:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def exists_user(self,user_id):
        with self.connection:
            user = self.cursor.execute("SELECT * FROM 'users' WHERE 'user_id' = ?", (user_id,)).fetchall()
            return bool(len(user))

    def add_user(self,user_id,your_name,direction,your_phone,name_children,age_children):
        with self.connection:
            return self.connection.execute("INSERT INTO FROM 'users' ('user_id','your_name'direction','your_name','your_phone','name_children',"
                                           "'age_children') VALUES (?)", (user_id,your_name,direction,your_phone,name_children,age_children)).fetchone()

    def get_all_users(self):
        with self.connection:
            return self.connection.execute("SELECT * FROM 'users'").fetchall()

    def get_user(self,id):
        return self.connection.execute("SELECT * FROM 'users' WHERE id = ?", (id,)).fetchone()




class DataBase:
# Стандартный метод Инициализирует класс
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

# Метод проверки нахождение пользователя в Базе данных
# который возвращает True если запись одна (len(user_id) = 1)
# Или False если записей не было (len(user_id) = 0)
    def message_exists(self,mes_id):
        with self.connection:
            # переменная для создания sql-запроса
            result = self.cursor.execute("SELECT * FROM 'chat_message' WHERE 'mes_id' = ?", (mes_id,)).fetchall()
            return bool(len(result))

# Метод Добавляет новое сообщение в базу данных
    def add_message(self, mes_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO 'chat_message' ('mes_id') VALUES (?)", (mes_id,)).fetchone()
# Метод Возвращает все строки из БД в виде списка
    def get_all_message(self):
        with self.connection:
            # переменная для создания sql-запроса
            result = self.cursor.execute("SELECT * FROM 'chat_message'").fetchall()
            return result

# Метод Возвращает одну строку из БД по id
    def get_one_message(self,id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM 'chat_message' WHERE id = ?", (id,)).fetchall()
            return result

# Метод Возвращает один элемент строки из БД по id
    def get_answer_message(self,id):
        with self.connection:
            result = self.cursor.execute("SELECT mes_id FROM 'chat_message' WHERE id = ?", (id,))
            return result

# Метод Удаляет строку из БД по id
    def del_message(self,id):
        with self.connection:
            return self.connection.execute("DELETE FROM 'chat_message' WHERE id = ?", (id,))



class DBMessage:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def message_exists(self, message_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM 'user_message' WHERE 'message_id' = ?", (message_id,)).fetchall()
            return bool(len(result))

    def active_chat(self):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM 'user_message'")
            return result

    def active_user(self,message_id):
        with self.connection:
            result = self.cursor.execute("SELECT message_id FROM 'user_message' WHERE message_id = ?", (message_id,))
            return result


# Метод Возвращает True если время бана пользователя еще не закончилось
#     def mute(self, user_id):
#         with self.connection:
#             user = self.cursor.execute("SELECT * 'name_table' FROM 'user_id' = ?", (user_id,)).fetchone()
#             # Проверяем третье поле таблицы "Время бана"
#             return int(user[2]) >= int(time.time())

# Метод добавляет пользователя в бан, время на которое будет забанен пользователь
#     def add_mute(self, user_id, mute_time):
#         with self.connection:
#             return self.connection.execute("UPDATE INTO 'name_table' SET 'mute_time' = ? WHERE 'user_id' = ?",  (int(time.time()) + int(mute_time),user_id))






