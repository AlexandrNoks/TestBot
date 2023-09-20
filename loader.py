import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import BaseStorage

from data.config import BOT_TOKEN
from utils.db_api.db_gino import db
from utils.db_api.db_poll import db_poll
from utils.db_api.db_schedule import schedule
from utils.db_api.db_activity import active
from data.database import DataBase

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
storage = BaseStorage
dp = Dispatcher()

# Файл с базой данных с расширением db
# db = DataBase('database.db')
reg_db = DataBase('database.db')


__all__ = ["bot","storage", "dp", "db", "db_poll", "schedule", "active"]