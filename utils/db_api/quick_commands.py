from asyncpg import UniqueViolationError
from docker.types import Ulimit

from utils.db_api.db_gino import db
from utils.db_api.schemas.registration import Registarion
from utils.db_api.schemas.poll_users import PollUsers


# Добавить данные
async def add_user(user_id: int, your_name: str, your_phone: str = None, direction: str = None):
    try:
        user = Registarion(user_id=user_id,your_name=your_name, your_phone=your_phone, direction=direction)
        await user.create()
    except UniqueViolationError:
        print("Пользователь не добавлен!")





# Получить одну запись
async def select_user(user_id):
    # users = await Registarion.query.gino.all()
    user = await Registarion.query.where(Registarion.user_id == user_id).gino.first()
    return user
    # for user in users:
    #     if user_id in user:
    #         return user
    #     else:
    #         return f"Пользователь с {user_id} не найден"


async def get_user_direction(user_id):
    user = await select_user(user_id)
    get_direction = await user.select("your_name").gino.first()
    return get_direction


async def update_user_direction(user_id, choose_direction):
    direction = await select_user(user_id)
    await direction.update(direction=choose_direction).apply()


async def update_user_phone(user_id, choose_phone):
    your_phone = await select_user(user_id)
    await your_phone.update(your_phone=choose_phone).apply()



# Получить все записи
async def select_all_users():
    users = await Registarion.query.gino.all()
    return users


# Получить колличество записей
async def count_users():
    users = await Registarion.query.gino.all()
    count = await db.func.count(Registarion.user_id).gino.scalar()
    return count
    # return len(users)


