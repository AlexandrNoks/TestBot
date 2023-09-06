from asyncpg import UniqueViolationError
from .schemas.schedule import ReedLesson


async def add_reed(number: int, weekday: str, time_lesson: str, name_children: str, age_children):
        try:
            weekdays = ReedLesson()
        except UniqueViolationError:
            print("Данные не добавлены")