from datetime import datetime
concerts = []
id_poll = []
name_concert = ["Времена года","Праздник Победы","Улыбки"]
ids_users = []
names_users = ["Корсан Екатерина Павловна","Корнилов Павел Андреевич","Карпова Елена Геннадьевна","Чирков Александр Михайлович","Суслова Анна Евгеньевна"]
last_name_users = []
options = ["Да","Нет"]
text_poll = ""
name_pupils = []
children = []
my_list = []
count_children = []
data = ["Корсан Лиза","Корнилов Андрей","Карпов Дима","Чирков Тихон","Суслова Лиза","Суслова Настя"]
week_day = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт']
lasts_name = [name.split()[0] for name in data]
# print(lasts_name)
names = [name for name in data]
for i in range(len(lasts_name)):
    try:
        if lasts_name.count(lasts_name[i]) > 1:
            num_start = lasts_name.index(lasts_name[i])
            children.append(names[i])
        else:
            name_pupils.append(names[i])
    except IndexError:
        break
lasts_name.pop(num_start)
# print(children)
name_pupils.append(children)
# print(name_pupils)
database = dict(zip(names_users,name_pupils))
# print(database)

class Pupil:
    type: str = "pupil"

    def __init__(self,name_parent,name_kid,names_children):
        self.name_parent: str = name_parent
        self.name_kid: str = name_kid
        self.names_children: list = names_children

class Schedule:
    type: str = "schedule"
    def __init__(self, name_kid, time_lesson):
        self.name_kid: str = name_kid
        self.time_lesson: datetime = time_lesson


class PollsConcert:
    type: str = "concert"

    def __init__(self,name_concert,data_concert,text_poll,answer_yes,answer_no):
        self.name_concert: str = name_concert
        self.data_concert: datetime = data_concert
        self.text_poll: str = text_poll
        self.answer_yes: str = answer_yes
        self.answer_no: str = answer_no

class VisitLesson:
    type: str = "visit"

    def __init__(self,name_concert,data_concert,text_poll,answer_yes,answer_no,id_poll):
        self.name_pupil: str = "pupil"
        self.id_user: int = 768768768
        self.fist_name: str = "name"
        self.id_poll: int = id_poll
        self.answer_yes: str = answer_yes
        self.answer_no: str = answer_no


db_concert = {
    "name": "concert",
    "name_pupil": "name",
    "location": "loc_contest",
    "date": "date_contest",
    "count_contestant": "count"
}

db_lessons = {
    "name_pupil": "name",
    "time_lesson": "loc_contest",
}

db_visiting = {
    "name_pupil": "name",
    "count_lesson": "count",
    "count_pass": "count_pass"
}

db_answers = {
    "count_yes": "yes",
    "count_no": "no"
}



