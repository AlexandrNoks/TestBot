# from .db_schedule import dict_schedule_weekday

weekday_list = []
double_weekday = []
# print("Корсан Лиза"[-4:])

dict_schedule_weekday = {'11:00': ('Корсан Лиза', ('Пн', 'Пн')), '12:10': ('Корнилов Андрей', ('Пн', 'Пн')), '13:20': ('Карпов Дима', ('Ср', 'Пт')), '14:30': ('Чирков Тихон', ('Ср', 'Пт')), '15:40': ('Виценко Оля', ('Ср', 'Пт')), '16:50': ('Минеева Настя', ('Пн', 'Пн')), '18:00': ('Унинбаева Азалия', ('Пн', 'Пн')), '19:10': ('Пархомцев Даниил', ('Пт', 'Ср')), '20:20': ('Тюрина Анастасия', ('Вт', 'Вт')), '21:10': ('Власенко Валерия', ('Вт', 'Вт')), '11:00,': ('Макаров Юра', ('Чт', 'Чт')), '12:10,': ('Семаева София', ('Чт', 'Чт')), '13:20,': ('Минзафарова Оксана', ('Чт', 'Чт')), '14:30,': ('Суслова Лиза', ('Чт', 'Чт')), '15:40,': ('Суслова Настя', ('Пт', 'Ср')), '16:50,': ('Хисангулова Елена', ('Пт', 'Ср')), '18:00,': ('Хисангулова Ирада', ('Вт', 'Вт')), '19:10,': ('Черкова Василиса', ('Вт', 'Вт'))}

time_schedule_weekday = dict_schedule_weekday.keys()
name_pupil_weekday = list(dict_schedule_weekday.values())
list_schedule = list(zip(time_schedule_weekday,name_pupil_weekday))

for weekday in dict_schedule_weekday:
    if dict_schedule_weekday[weekday][1] in dict_schedule_weekday[weekday]:
        weekday_list.append(dict_schedule_weekday[weekday][1])
# print(weekday_list)

for item in weekday_list:
    if weekday_list.count(item) > 1 and item not in double_weekday:
        double_weekday.append(item)
# print(double_weekday)
# Генератор индексов дубликатов в общем списке дней недели (18 эл.)
def gen_index_schedule():
    for i in weekday_list:
        if i in double_weekday:
            double_index = double_weekday.index(i)
            double_index = str(double_index)
            yield double_index


list_index_double = list(gen_index_schedule()) # индексы дубликатов
# print(list_index_double)
get_count_double = list(range(len(list_index_double))) # Индексы элемента списка с дубликатами

index_schedule = dict(zip(get_count_double,list_index_double))
# print(index_schedule)


# Генератор уроков два дня в неделю
def gen_schedule_weekday(weekday):
    list_index = []
    for item in index_schedule:
        if index_schedule[item] in str(weekday):
            list_index.append(item)
    for i in list_index:
        i = int(i)
        yield list_schedule[i]


schedule_weekday = list(gen_schedule_weekday(0))
# for elem in schedule_weekday:
#     print(elem)




