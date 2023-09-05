from data.schedule import *

def gen_schedule_weekday():
    for elem in dict_schedule_weekday:
        weekday = ScheduleWeekday(time_lesson=elem,name_pupil=dict_schedule_weekday[elem][0],one_weekday=dict_schedule_weekday[elem][1][0],two_weekday=dict_schedule_weekday[elem][1][1])
        yield weekday
final_schedule_weekday = list(gen_schedule_weekday())
# print(final_schedule_weekday)
# for result in final_schedule_weekday:
#     print(result.__str__())


# Рассписание на сегодня
def gen_schedule_today():
    i = 0
    for today in dict_schedule_today:
        i += 1
        obj_class = ScheduleToday(week_day=i,time_lesson=today,name_pupil=dict_schedule_today[today])
        yield obj_class

obj_class_schedule = list(gen_schedule_today())


Mon = [obj_class.__str__() for obj_class in obj_class_schedule]
We = [obj_class.__str__() for obj_class in obj_class_schedule]
Tu = [obj_class.__str__() for obj_class in obj_class_schedule]
Fr = [obj_class.__str__() for obj_class in obj_class_schedule]
Th = [obj_class.__str__() for obj_class in obj_class_schedule]
# for obj in We:
#     print(obj)


time_schedule_weekday = dict_schedule_weekday.keys()
name_pupil_weekday = list(dict_schedule_weekday.values())
list_schedule = list(zip(time_schedule_weekday,name_pupil_weekday))

for weekday in dict_schedule_weekday:
    if dict_schedule_weekday[weekday][1] in dict_schedule_weekday[weekday]:
        weekday_list.append(dict_schedule_weekday[weekday][1])
print(weekday_list)
# print(dict_schedule_weekday)

for item in weekday_list:
    if weekday_list.count(item) > 1 and item not in double_weekday:
        double_weekday.append(item)
print(double_weekday)
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
print(index_schedule)


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
# for today in dict_schedule_today:
#     print(f"{today} {dict_schedule_today[today]}")



# for today in dict_schedule_today:
#     print(f"{today}: {dict_schedule_today[today]}")

