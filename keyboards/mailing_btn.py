from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton



mailing_btn = InlineKeyboardMarkup(row_width=4,
                                   inline_keyboard=[[
                                       InlineKeyboardButton(text="Рассписание", callback_data="mailingSchedule"),
                                       InlineKeyboardButton(text="Фото", callback_data="mailingPhoto"),
                                       InlineKeyboardButton(text="Видео",callback_data="mailingVideo"),
                                       InlineKeyboardButton(text="Ссылка на канал",callback_data="mailingChannel"),
                                       InlineKeyboardButton(text="Отмена",callback_data="mailingExit")
                                   ]],
                                   resize_keyboard=True)