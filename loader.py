import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data.config import BOT_TOKEN
from utils.db_api.db_gino import db
from utils.db_api.db_poll import db_poll
from utils.db_api.db_schedule import schedule
from data.database import DataBase

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot,storage=storage)
# Файл с базой данных с расширением db
# db = DataBase('database.db')


__all__ = ["bot","storage", "dp", "db", "db_poll", "schedule"]