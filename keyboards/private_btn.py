from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup,KeyboardButton


schedule = ['11:00-11:50','12:10-13:00','13:20-14:10','14:30-15:20','15:40-16:30','16:50-17:40','18:00-18:50','19:10-20:00','20:20-21:10']
eng_weekday = ['Mon','Tu','We','Th','Fr']
keys_time = ["A","B","C","D","F","G","H","I","G"]
weekdays = ['Пн','Вт','Ср','Чт','Пт']


to_ask_bot = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="Записаться на урок", callback_data="AskReedLesson"),
        InlineKeyboardButton(text="Подписаться на канал", callback_data="AskThisChannel"),
        InlineKeyboardButton(text="Наши контакты", callback_data="AskThisContact"),
        InlineKeyboardButton(text="Пройти регистрацию", callback_data="Register")
    ]]
)















