from gino import Gino
import sqlalchemy as sa
from aiogram import Dispatcher
from typing import List
import datetime

from sqlalchemy import Column, BigInteger, String

from data import config

db = Gino()


class BaseModel(db.Model):
    __abstract__ = True
    # Отображение таблицы
    def __str__(self):
        model = self.__class__.__name__
        table: sa.Table = sa.inspect(self.__class__)
        primary_key_columns: List[sa.Column] = table.columns
        values = {
            column.name: getattr(self,self._column_name_map[column.name])
            for column in primary_key_columns
        }
        values_str = " ".join(f"{name}={value!r}" for name, value in values.items())
        return f"<{model} {values_str}>"


class TimedBaseModel(BaseModel):
    __abstract__ = True
    created_at = db.Column(db.DateTime(True),server_default=db.func.now())
    # updated_at = db.Column(
    #     db.DateTime(True),
    #     dafault=datetime.datetime.utcnow(),
    #     unupdate=datetime.datetime.utcnow(),
    #     server_default=db.func.now())
# class FeedBack(BaseModel):
#     __tablename__ = "feedback"
#     user_id = Column(BigInteger, primary_key=True)
#     name = Column(String(length=200))
#     phone = Column(String(length=300))
#     direction = Column(String(length=200))
#
#
# print(FeedBack(name="Петя",phone="657657657",direction="Вокал"))


async def on_startup(dispatcher: Dispatcher):
    print("Установка связи с PostgreSQL!")
    await db.set_bind(config.POSTGRES_URL)