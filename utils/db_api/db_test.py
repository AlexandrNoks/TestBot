# from asyncpg import UniqueViolationError
# from docker.types import Ulimit
# from utils.db_api.schemas.activity import Messages
# from loader import active
#
#
# # Добавить данные
# async def add_message(message_id: int, user_id: int):
#     try:
#         message = Messages(message_id=message_id, user_id=user_id)
#         await message.create()
#     except UniqueViolationError:
#         print("Сообщение не добавлено!")
#
#
# # Получить одну запись
# async def select_message(message_id):
#     message = await Messages.query.where(Messages.message_id == message_id).gino.first()
#     return message
#
#
# # Получить все записи
# async def select_all_message():
#     messages = await Messages.query.gino.all()
#     return messages
#
#
# # Получить колличество записей
# async def count_messages():
#     count_message = await active.func.count(Messages.message_id).gino.scalar()
#     return count_message
#     # return len(users)
#
#
# async def count_messages_one_user(user_id):
#     count_message = await Messages.query.where(Messages.user_id == user_id).gino.all()
#     return count_message
#     # return len(users)
