# import asyncio
# from data import config
# from utils.db_api import lesson_commands as commands
# from utils.db_api.db_reedlesson import reedlesson
#
# # # Тестируем БД
# async def db_test():
# #     # Подключаемся к БД
#     await reedlesson.set_bind(config.POSTGRES_URL)
#     print("Подключение к БД")
# #   Очищаем данные удаляем все таблицы
#     await reedlesson.gino.drop_all()
#     print("Удаленим все таблицы")
# #    Создаем новую таблицу
#     await reedlesson.gino.create_all()
#     print("Создаем таблицу")
#
#     await commands.add_reed(1924126688,'Пн','11:00-11:50','+79227654123')
#     await commands.add_reed(1924126633,'Вт','14:30-15:20','+79227650123')
#     await commands.add_reed(1924126622,'Ср','15:40-16:30','+79227954123')
#     user = await commands.get_user(user_id=1924126688)
#     print(user)
# #     await commands.add_message(1234,1924126688)
# #
# #     # await commands.add_message(4569, 1924128688)
# #     # await commands.add_message(3876, 1924129688)
# #     # await commands.add_message(1134,9924126689)
# #     # await commands.add_message(1135,9924106689)
# #
# #     # await commands.update_user_direction(1924126688,"Вокал")
# #     # await commands.update_user_phone(1924126688,phone="5465465465465")
# #     # #
# #     # messages = await commands.select_all_message()
# #     # for message in messages:
# #     #     print(message)
# #
# #     messages = await commands.count_messages_one_user(1924126688)
# #     print(len(messages))
# #     for message in messages:
# #         print(message)
# #
# #
# #     # count = await commands.count_users()
# #     # print(count)
# #
# #     # get_message = await commands.select_message(1234)
# #     # print(get_message)
# #
# #     # user = await commands.get_user_direction(1924126688)
# #     # print(user)
# #     #
# #     # update_direction = await commands.update_user_direction(993482289,"Гитара")
# #     # update_phone = await commands.update_user_phone(993482289,"666666hgj544")
# #     # print(update_direction)
# #     # print(update_phone)
# loop = asyncio.get_event_loop()
# loop.run_until_complete(db_test())