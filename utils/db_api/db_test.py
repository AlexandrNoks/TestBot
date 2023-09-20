import asyncio
from datetime import datetime
from data import config
from utils.db_api import message_commands as commands
from utils.db_api.db_activity import active

# Тестируем БД
async def db_test():
    # Подключаемся к БД
    await active.set_bind(config.POSTGRES_URL)
    # Очищаем данные удаляем все таблицы
    await active.gino.drop_all()
    # Создаем новую таблицу
    await active.gino.create_all()

    await commands.add_message(4567, 1924126688)
    await commands.add_message(9876, 1924126688)
    await commands.add_message(1234,1924126688)

    await commands.add_message(4569, 1924128688)
    await commands.add_message(3876, 1924129688)
    await commands.add_message(1134,9924126689)

    # await commands.update_user_direction(1924126688,"Вокал")
    # await commands.update_user_phone(1924126688,phone="5465465465465")
    # #
    # messages = await commands.select_all_message()
    # for message in messages:
    #     print(message)

    messages = await commands.count_messages_one_user(1924126688)
    print(len(messages))
    for message in messages:
        print(message)


    # count = await commands.count_users()
    # print(count)

    # get_message = await commands.select_message(1234)
    # print(get_message)

    # user = await commands.get_user_direction(1924126688)
    # print(user)
    #
    # update_direction = await commands.update_user_direction(993482289,"Гитара")
    # update_phone = await commands.update_user_phone(993482289,"666666hgj544")
    # print(update_direction)
    # print(update_phone)
loop = asyncio.get_event_loop()
loop.run_until_complete(db_test())