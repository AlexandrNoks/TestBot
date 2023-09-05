from data.config import admins_id
from aiogram import types, Dispatcher
from data.config import WORDS
import gino


async def on_startup(dp):
    from utils.start_bot import on_startup_notify
    await on_startup_notify(dp)
    import filters
    filters.setup(dp)
    import middlewares
    middlewares.setup(dp)
    import logging
    from loader import db,schedule,db_poll
    from utils.db_api.db_gino import on_startup
    from utils.db_api.schemas.schedule import ScheduleWeekday
    print("Подключение к PostgreSQL")
    await on_startup(db)
    await db.gino.drop_all()
    await db.gino.create_all()

    from utils.db_api.db_poll import on_startup
    from utils.db_api.db_schedule import on_startup
    await on_startup(db_poll)
    print("Удаление базы данных")
    await db.gino.drop_all()
    print("Создание таблиц")
    await db.gino.create_all()
    print("Готово")



    logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    from handlers import dp
    from aiogram import executor

    executor.start_polling(dp, on_startup=on_startup)


# 1721708270:AAGIimt6k-cTuSQmS2pExN9dDwVpIiV7eTY