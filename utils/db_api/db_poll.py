from gino import Gino
import sqlalchemy as sa
from aiogram import Dispatcher

from typing import List

from data import config



db_poll = Gino()


class BaseModel(db_poll.Model):
    __abstract__ = True

    def __str__(self):
        model = self.__class__.__name__
        table: sa.Table = sa.inspect(self.__class__)
        primary_key_column: List[sa.Column] = table.columns
        values = {
            column.name: getattr(self,self._column_name_map[column.name])
            for column in primary_key_column
        }
        values_str = " ".join(f"{name}={value!r}" for name, value in values.items())
        return f"<{model} {values_str}>"


class TimedBaseModel(BaseModel):
    __abstract__ = True
    created_at = db_poll.Column(db_poll.DateTime(True),server_default=db_poll.func.now())


async def on_startup(dispatcher: Dispatcher):
    await db_poll.set_bind(config.POSTGRES_URL)
