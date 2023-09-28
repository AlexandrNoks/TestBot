import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import BaseStorage
from data.config import BOT_TOKEN
from utils.db_api.db_polls import poll
from utils.db_api.db_reedlesson import reedlesson
from utils.db_api.db_messages import active
from data.database import DataBase

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
storage = BaseStorage
dp = Dispatcher()

# Файл с базой данных с расширением db
# db = DataBase('database.db')
reg_db = DataBase('database.db')


__all__ = ["bot","storage", "dp", "reedlesson","active","poll"]