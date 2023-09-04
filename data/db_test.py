from data.schedule import dict_schedule_weekday,dict_schedule_today


class ScheduleWeekday:
    def __init__(self,time_lesson, name_pupil,one_weekday,two_weekday):
        self.time_lesson = time_lesson
        self.name_pupil = name_pupil
        self.one_weekday = one_weekday
        self.two_weekday = two_weekday

    def __str__(self):
        return f"{self.time_lesson} {self.name_pupil} {self.one_weekday} {self.two_weekday}"

# Метод добавляет двнные в таблицу
def gen_schedule_weekday():
    for elem in dict_schedule_weekday:
        weekday = ScheduleWeekday(time_lesson=elem,name_pupil=dict_schedule_weekday[elem][0],one_weekday=dict_schedule_weekday[elem][1][0],two_weekday=dict_schedule_weekday[elem][1][1])
        yield weekday

schedule_weekday = list(gen_schedule_weekday())
# print(schedule_weekday)
# for result in final_schedule_weekday:
#     print(result.__str__())


class ScheduleToday:
    def __init__(self,time_lesson, name_pupil,week_day=0):
        self.week_day = week_day
        self.name_pupil = name_pupil
        self.time_lesson = time_lesson

    def __str__(self):
        return f"{self.week_day} {self.time_lesson} : {self.name_pupil}"

# Метод добавляет данные в таблицу
def gen_schedule_today():
    i = 0
    for today in dict_schedule_today:
        i += 1
        obj_class = ScheduleToday(week_day=i,time_lesson=today,name_pupil=dict_schedule_today[today])
        yield obj_class

schedule_today = list(gen_schedule_today())