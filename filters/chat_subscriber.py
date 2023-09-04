from aiogram.dispatcher.filters import BoundFilter
from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from loader import bot

from data.config import GROUP_ID

# Фильтр проверки подписки на телеграмм канал
class IsSubscriber(BoundFilter):
    async def check(self, message: types.Message):
        subscribet = 0
        for chat_id in GROUP_ID:
            sub = await bot.get_chat_member(chat_id=chat_id,user_id=message.from_user.id)
            if sub.status != types.ChatMemberStatus.LEFT:
                subscribet += 1
            else:
                break
        else:
            if subscribet == len(GROUP_ID):
                return True
            else:
                subscribet_btn = InlineKeyboardMarkup(row_width=1,
                                                  inline_keyboard=InlineKeyboardButton(text="Подписаться", url='https://t.me/+xxep96iuXxk3ZDky')
                                                  )
                await bot.send_message("Подпишитесь на наш канал", reply_markup=subscribet_btn)
                raise CancelHandler()

