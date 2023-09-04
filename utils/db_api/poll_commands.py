from asyncpg import UniqueViolationError


from utils.db_api.schemas.poll_users import PollUsers


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


