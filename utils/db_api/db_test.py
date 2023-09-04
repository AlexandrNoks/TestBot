# import asyncio
#
# from data import config
# from utils.db_api import quick_commands as commands
# from utils.db_api.db_gino import db
#
# # Тестируем БД
# async def db_test():
#     # Подключаемся к БД
#     await db.set_bind(config.POSTGRES_URL)
#     # Очищаем данные удаляем все таблицы
#     await db.gino.drop_all()
#     # Создаем новую таблицу
#     await db.gino.create_all()
#
#     await commands.add_user(1924126688,"Вася",None,None)
#     await commands.add_user(993482289,"Петя"," ",None)
#     await commands.add_user(6284449881,"Диман"," ",None)
#
#     # await commands.update_user_direction(1924126688,"Вокал")
#     # await commands.update_user_phone(1924126688,phone="5465465465465")
#
#     # users = await commands.select_all_users()
#     # print(users)
#
#     # count = await commands.count_users()
#     # print(count)
#
#     # get_user = await commands.select_user(6284449881)
#     # print(get_user)
#
#     # user = await commands.get_user_direction(1924126688)
#     # print(user)
#     #
#     # update_direction = await commands.update_user_direction(993482289,"Гитара")
#     # update_phone = await commands.update_user_phone(993482289,"666666hgj544")
#     # print(update_direction)
#     # print(update_phone)
# loop = asyncio.get_event_loop()
# loop.run_until_complete(db_test())