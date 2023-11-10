from asyncpg import UniqueViolationError
# from docker.types import Ulimit
from TestBot.utils.db_api.schemas.activity import Messages
from TestBot.utils.db_api.schemas.poll import PollUsers


# # Добавить данные
async def add_message(message_id: int, user_id: int):
    try:
        message = Messages(message_id=message_id, user_id=user_id)
        await message.create()
    except UniqueViolationError:
        print("Сообщение не добавлено!")


# Получить одну запись
async def select_message(message_id):
    message = await Messages.query.where(Messages.message_id == message_id).gino.first()
    return message


# # Получить все записи
async def select_all_message():
    messages = await Messages.query.gino.all()
    return messages


async def add_answer(user_id: int, user_name: str, user_answer):
    try:
        answer = PollUsers(user_id=user_id, user_name=user_name,user_answer=user_answer)
        await answer.create()
    except UniqueViolationError:
        print("Ответ не сохранен!")


async def select_all_answers():
    answers = await PollUsers.query.gino.all()
    for answer in answers:
        user_name = await answer.select("user_name").gino.first()
        user_answer = await answer.select("user_answer").gino.first()
        return f"Имя {user_name[0]}\nОтвет {user_answer[0]}"

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


async def add_answer(user_id: int, user_name: str, user_answer):
    try:
        answer = PollUsers(user_id=user_id, user_name=user_name,user_answer=user_answer)
        await answer.create()
    except UniqueViolationError:
        print("Ответ не сохранен!")


async def select_all_answers():
    answers = await PollUsers.query.gino.all()
    for answer in answers:
        user_name = await answer.select("user_name").gino.first()
        user_answer = await answer.select("user_answer").gino.first()
        return f"Имя {user_name[0]}\nОтвет {user_answer[0]}"


async def select_user_answer(user_id):
    user = await PollUsers.query.where(PollUsers.user_id==user_id).gino.first()
    return user
