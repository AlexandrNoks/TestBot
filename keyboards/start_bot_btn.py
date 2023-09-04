from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardButton
from data.config import GROUP_ID,CHANNEL_ID,BOT_ID,GROUP_URL


start_button_admin = ReplyKeyboardMarkup(
                                        keyboard=[
                                            [
                                                KeyboardButton(text="Перейти..", request_id=-1001978690583),
                                                KeyboardButton(text="Отправить в чат", request_id=1400170440)
                                            ],
                                            [
                                                KeyboardButton(text="Написать ученику в л/с"),
                                                KeyboardButton(text="Создать опрос"),
                                                KeyboardButton(text="Запросить контакт")
                                            ]
                                        ],
                                         resize_keyboard=True)

