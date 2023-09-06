from asyncpg import UniqueViolationError
from .schemas.schedule import ReedLesson

async def get_weekday(weekday):
    lesson = await ReedLesson.query.where(ReedLesson.weekday == weekday).gino.first()
    return lesson

async def get_time(time_lesson):
    lesson = await ReedLesson.query.where(ReedLesson.time_lesson == time_lesson).gino.first()
    return lesson

async def find_freetime(weekday,time_lesson):
    find_weekday = await get_weekday(weekday)
    find_time = await get_time(time_lesson)
    freetime = [find_weekday,find_time]
    return freetime

async def add_reed(number: int, weekday: str, time_lesson: str, name_children: str, age_children):
    try:
        new_pupil = ReedLesson(number=number,weekday=weekday,time_lesson=time_lesson,name_children=name_children,age_children=age_children)
        freetime = await find_freetime(weekday,time_lesson)
        if new_pupil.weekday not in freetime and new_pupil.time_lesson not in freetime:
            await new_pupil.create()
        else:
            await freetime[1]
    except UniqueViolationError:
        print("Данные не добавлены")



