import calendar


time_lesson = ['11:00','12:10','13:20','14:30','15:40','16:50','18:00','19:10','20:20','21:10']
value_time = tuple(zip(time_lesson[:5],time_lesson[5:]))
keys_time = ["a","b","c","d","f","g","i","j","q","l"]
schedule = ['11:00','12:10','13:20','14:30','15:40','16:50','18:00','19:10','20:20','21:10']







# my_list = []
# for i in my_list:
#     print(i)

week_day_abbr = list(calendar.day_abbr) # дни недели
# num_day = int(input("Введите число: "))

time_busy = (time_lesson[2:7],time_lesson[6:],time_lesson[6:10],time_lesson[11:],time_lesson[5:12])
free_time = (time_lesson[:3]+time_lesson[7:],time_lesson[:6],time_lesson[:6]+time_lesson[10:],time_lesson[:11],time_lesson[:5]+time_lesson[12:])
# schedule = [i for i in range(len(free_time)) if num_day == i]
my_list = []

#     for i in free:
#         if i in result:
#             if result[i] != "Свободно":
#                 my_list.append(result[i])
#
# print(my_list)




# Рассписание свободных часов
dict_free_time = dict(zip(week_day_abbr,free_time))
# Рассписание занятые часы
dict_time_busy = dict(zip(week_day_abbr,time_busy))

# Узнать свободные часы занятий
# for i in range(1,len(week_day_abbr)):
#     int_num_week_day = input("Enter week day: ")
#     if int_num_week_day == '' or int_num_week_day == 'stop':
#         break
#     try:
#         int_num_week_day = int(int_num_week_day)
#         i = int_num_week_day
#         print("\n".join(free_time[i]))
#     except ValueError:
#         print('Please, enter for number 1 to 5')
#         continue
#     except TypeError:
#         print('Sorry, school in now day do not work.')
#         continue
#     except IndexError:
#         print('Sorry, school in now day do not work.Try it again.')
#         continue


# print(num_week_day)
# Функция генератор указываем время в часах с которого выводится
# inp_hours = str(input("Enter time: ")) + ':00'
# def generator_schedule(inp_hours,time_lesson):
#     res = datetime.strptime(inp_hours,'%H:%M')
#     for n in time_lesson:
#         date_time_obj = datetime.strptime(n, '%H:%M')
#         if date_time_obj > res:
#             yield date_time_obj.time().strftime('%H:%M')
#         else:
#             pass
# schedule = list(generator_schedule(inp_hours,time_lesson))
# print(schedule)