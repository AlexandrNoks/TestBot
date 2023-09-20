from aiogram.dispatcher.event.bases import CancelHandler
from filters.chat_member import ChatMemberFilter
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardBuilder

from loader import bot

from data.config import GROUP_ID

# Фильтр проверки подписки на телеграмм канал
class IsSubscriber(ChatMemberFilter):
    async def check(self, message: types.Message):
        subscribet = 0
        for chat_id in GROUP_ID:
            sub = await bot.get_chat_member(chat_id=chat_id,user_id=message.from_user.id)
            if sub.status != types.ChatMember.LEFT:
                subscribet += 1
            else:
                break
        else:
            if subscribet == len(GROUP_ID):
                return True
            else:
                subscribe_btn = InlineKeyboardBuilder()
                sign = InlineKeyboardButton(text="Подписаться", url='https://t.me/+xxep96iuXxk3ZDky')
                subscribe_btn.row(sign)
                await bot.send_message("Подпишитесь на наш канал", reply_markup=subscribe_btn)
                raise CancelHandler()

