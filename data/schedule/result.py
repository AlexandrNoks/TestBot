weekdays = ['Пн','Вт','Ср','Чт','Пт']
two_weekdays = [('Пн', 'Ср'), ('Вт', 'Чт'), ('Ср', 'Пт'), ('Пн', 'Чт'), ('Вт', 'Пт')]
time_lesson = ['11:00','12:10','13:20','14:30','15:40','16:50','18:00','19:10','20:20','21:10']
schedule_day = ['11:00-11:50','12:10-13:00','13:20-14:10','14:30-15:20','15:40-16:30','16:50-17:40','18:00-18:50','19:10-20:00','20:20-21:10']
# print(len((schedule_day)))
day_lesson = {}
for lesson in weekdays:
    day_lesson[lesson] = time_lesson
# print(day_lesson)
days_lesson = {}


class ScheduleWeekday:
    def __init__(self,time_day_one,time_day_two,name_pupil,one_weekday: str=None, two_weekday: str=None):
        self.one_weekday = one_weekday
        self.two_weekday = two_weekday
        self.time_day_one = time_day_one
        self.time_day_two = time_day_two

        self.name_pupil = name_pupil

    def __str__(self):
        # return f"{self.name_pupil}\n{self.one_weekday} {self.time_day_one}\n{self.two_weekday} {self.time_day_two}"
        return f"{self.name_pupil} {self.one_weekday} {self.time_day_one} {self.two_weekday} {self.time_day_two}"


time_busy = ScheduleWeekday(name_pupil="Петя",one_weekday="Пн",time_day_one="11:00",two_weekday="Ср",time_day_two="15:00")
busy_list = time_busy.__str__().split(" ")
print(busy_list)
# print(time_busy.__str__())