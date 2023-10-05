import asyncio
from handlers.users import admins,start
from handlers.groups import chat,private_chat,media
from utils.start_bot import on_startup_notify
from keyboards.start_bot_btn import start_button_admin,start_button_user
import logging
from data.config import ADMIN_ID, GROUP_ID
from datetime import datetime




async def on_startup():
    from loader import bot,dp
    from handlers.users.start import router
    dp.include_routers(chat.router, admins.router, media.router, start.router, private_chat.router)
    await bot.send_message(ADMIN_ID,'Бот Запущен и готов к работе', reply_markup=start_button_admin)
    await bot.send_message(GROUP_ID,f"{datetime.today().strftime('%d.%m.%Y')}", reply_markup=start_button_user)
    await dp.start_polling(bot)
    # await on_startup_notify(dp)
    # await bot.delete_webhook(drop_pending_updates=True)

    # print("Подключение к PostgreSQL")
    # await active.set_bind(config.POSTGRES_URL)
    # await poll.set_bind(config.POSTGRES_URL)
    # print("Удаление базы данных")
    # await active.gino.drop_all()
    # await poll.gino.drop_all()
    # print("Создание таблиц")
    # await active.gino.create_all()
    # await poll.gino.create_all()
    # print("Готово")

    logging.basicConfig(level=logging.DEBUG)


if __name__ == "__main__":
    try:
        asyncio.run(on_startup())
        print("Hello")
    except KeyboardInterrupt:
        print("Exit")



# 1721708270:AAGIimt6k-cTuSQmS2pExN9dDwVpIiV7eTY