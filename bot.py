from data.config import admins_id
from aiogram import types
from data.config import WORDS
import gino
from loader import dp,bot
from handlers.groups import chat,schedule
from handlers.users import private_chat,admins
from handlers.channel import channel


async def on_startup(dp):
    from handlers.users import private_chat,admins
    from loader import schedule,db_poll,active,db
    from utils.start_bot import on_startup_notify
    from utils.db_api.db_gino import on_startup
    # from utils.db_api.db_poll import on_startup
    # from utils.db_api.db_schedule import on_startup
    import logging
    await on_startup_notify(dp)
    dp.include_routers(chat.router, admins.router)
    await dp.start_polling(bot)
    # await bot.delete_webhook(drop_pending_updates=True)
    print("Подключение к PostgreSQL")
    await on_startup(db)
    print("Удаление базы данных")
    await db.gino.drop_all()
    print("Создание таблиц")
    await db.gino.create_all()
    print("Готово")
    logging.basicConfig(level=logging.DEBUG)


if __name__ == "__main__":
    from handlers import dp

    # from aiogram import executor
    import asyncio
    # from utils.db_api.db_activity import on_startup
    asyncio.run(on_startup(dp))
    print("Hello")
    # executor.start_polling(dp, on_startup=on_startup)


# 1721708270:AAGIimt6k-cTuSQmS2pExN9dDwVpIiV7eTY