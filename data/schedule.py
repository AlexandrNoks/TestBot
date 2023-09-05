import random
table_data = [
    [1,"Корсан Лиза",7,"+7 922 874 873"],
    [2,"Корнилов Андрей",4,"+7 922 874 873"],
    [4,"Карпов Дима",11,"+7 922 874 873"],
    [5,"Чирков Тихон",6,"+7 922 874 873"],
    [6,"Виценко Оля",6,"+7 922 874 873"],
    [8,"Минеева Настя",11,"+7 922 874 873"],
    [9,"Унинбаева Азалия",12,"+7 922 874 873"],
    [10,"Пархомцев Даниил",16,"+7 922 874 873"],
    [11,"Тюрина Анастасия",25,"+7 922 874 873"],
    [12,"Власенко Валерия",42,"+7 922 874 873"],
    [13,"Макаров Юра",30,"+7 922 874 873"],
    [14,"Семаева София",6,"+7 922 874 873"],
    [15,"Минзафарова Оксана",40,"+7 922 874 873"],
    [16,"Суслова Лиза",6,"+7 922 874 873"],
    [17,"Суслова Настя",6,"+7 922 874 873"],
    [18,"Хисангулова Елена",33,"+7 922 874 873"],
    [19,"Хисангулова Ирада",7,"+7 922 874 873"],
    [20,"Черкова Василиса",8,"+7 922 874 873"]
]
time_lesson = ['11:00','12:10','13:20','14:30','15:40','16:50','18:00','19:10','20:20','21:10']
weekday_list = []
double_weekday = []
# num_week_day = datetime.today().isoweekday()
data = []
for name in table_data:
    data.append(name[1])
def filter_week_day():
    week_day_one = ['Пн','Вт','Ср','Чт','Пт']
    week_day_two = ['Пн','Вт','Ср','Чт','Пт']
    random.shuffle(week_day_two)
    count = list(zip(week_day_one,week_day_two))
    return count

gen_week_day = list(filter_week_day())
# print(gen_week_day)


# [('Пн', 'Ср'), ,('Вт', 'Чт'), ('Ср', 'Пт'), ('Пн', 'Чт'), ('Вт', 'Пт')]
my_list = []
i = 1
filter_day = filter_week_day()
# print(filter_day)

for day in range(len(data)):
    result_list = gen_week_day + gen_week_day
set_week_day = result_list + result_list
# print(set_week_day)
random.shuffle(set_week_day)
dict_pupil_weekday = dict(zip(data,set_week_day))
# print(dict_pupil_weekday)
list_pupil_weekday = list(zip(data,set_week_day))
# print(list_pupil_weekday)

class ScheduleToday:
    def __init__(self,time_lesson, name_pupil,week_day=0):
        self.week_day = week_day
        self.name_pupil = name_pupil
        self.time_lesson = time_lesson

    def __str__(self):
        return f"{self.week_day} {self.time_lesson} : {self.name_pupil}"


class ScheduleWeekday:
    def __init__(self,time_lesson, name_pupil,one_weekday,two_weekday):
        self.time_lesson = time_lesson
        self.name_pupil = name_pupil
        self.one_weekday = one_weekday
        self.two_weekday = two_weekday

    def __str__(self):
        return f"{self.time_lesson} {self.name_pupil} {self.one_weekday} {self.two_weekday}"

# Рассписание занятий
for i in time_lesson:
    try:
        if len(data) != len(time_lesson):
            time_lesson.append(f"{i},")
    except IndexError:
        break
value_list = []
# print(time_lesson)
key_list = []
# print(len(time_lesson))
dict_time_pupil = dict(zip(time_lesson,data))
# print(f"{len(dict_time_pupil)}")
# for elem in dict_time_pupil:
#
#     print(f"{elem}: {dict_time_pupil[elem]}")


# Рассписание на неделю
dict_schedule_weekday = dict(zip(time_lesson,list_pupil_weekday))
# dict_schedule_weekday = {'11:00': ('Корсан Лиза', ('Пн', 'Пн')), '12:10': ('Корнилов Андрей', ('Пн', 'Пн')), '13:20': ('Карпов Дима', ('Ср', 'Пт')), '14:30': ('Чирков Тихон', ('Ср', 'Пт')), '15:40': ('Виценко Оля', ('Ср', 'Пт')), '16:50': ('Минеева Настя', ('Пн', 'Пн')), '18:00': ('Унинбаева Азалия', ('Пн', 'Пн')), '19:10': ('Пархомцев Даниил', ('Пт', 'Ср')), '20:20': ('Тюрина Анастасия', ('Вт', 'Вт')), '21:10': ('Власенко Валерия', ('Вт', 'Вт')), '11:00,': ('Макаров Юра', ('Чт', 'Чт')), '12:10,': ('Семаева София', ('Чт', 'Чт')), '13:20,': ('Минзафарова Оксана', ('Чт', 'Чт')), '14:30,': ('Суслова Лиза', ('Чт', 'Чт')), '15:40,': ('Суслова Настя', ('Пт', 'Ср')), '16:50,': ('Хисангулова Елена', ('Пт', 'Ср')), '18:00,': ('Хисангулова Ирада', ('Вт', 'Вт')), '19:10,': ('Черкова Василиса', ('Вт', 'Вт'))}

# print(dict_schedule_weekday)
# Генератор в какие дни удобно заниматься два раза в неделю
for schedule in dict_time_pupil:
    if dict_time_pupil[schedule] == "Свободно":
        pass
    else:
        key_list.append(schedule)
        value_list.append(dict_time_pupil[schedule])
        if len(key_list) == 5 and len(value_list) == 5:
            break

dict_schedule_today = dict(zip(key_list,value_list))
# print(dict_schedule_today)