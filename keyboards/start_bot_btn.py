from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, \
    KeyboardButtonRequestUser
from data.config import GROUP_ID, CHANNEL_ID, BOT_ID, GROUP_URL, ADMIN_ID,ADMIN_URL

start_button_admin = ReplyKeyboardMarkup(
                                        keyboard=[
                                            [
                                                KeyboardButton(text="Перейти..", request_id=-1001978690583),
                                                KeyboardButton(text="Отправить в чат", request_id=1400170440)
                                            ],
                                            [
                                                KeyboardButton(text="Написать ученику в л/с"),
                                                KeyboardButton(text="Создать опрос")
                                            ]
                                        ],
                                         resize_keyboard=True)

start_button_user = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Написать педагогу"),
            KeyboardButton(text="Узнать расписание"),
            KeyboardButton(text="Перейти...")
        ],
    ],
    resize_keyboard=True)

schedule = ['11:00-11:50','12:10-13:00','13:20-14:10','14:30-15:20','15:40-16:30','16:50-17:40','18:00-18:50','19:10-20:00','20:20-21:10']
eng_weekday = ['Mon','Tu','We','Th','Fr']
keys_time = ["A","B","C","D","F","G","H","I","G"]
weekdays = ['Пн','Вт','Ср','Чт','Пт']


to_ask_bot = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text="Записаться на урок", callback_data="AskReedLesson"),
    InlineKeyboardButton(text="Подписаться на канал", callback_data="ThisChannel"),
    InlineKeyboardButton(text="Наши контакты", callback_data="ThisContact"),
    InlineKeyboardButton(text="Пройти регистрацию", callback_data="Register")
]]
)


