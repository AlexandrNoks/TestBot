from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup,KeyboardButton


to_ask_bot = InlineKeyboardMarkup(row_width=3)
button_write_to_lesson = InlineKeyboardButton(text="Записаться на урок", callback_data="AskReedLesson")
button_subscription = InlineKeyboardButton(text="Подписаться на канал", url='https://t.me/+xxep96iuXxk3ZDky')
button_contact = InlineKeyboardButton(text="Наши контакты", callback_data="AskContact")
to_ask_bot.insert(button_write_to_lesson)
to_ask_bot.insert(button_subscription)
to_ask_bot.insert(button_contact)




