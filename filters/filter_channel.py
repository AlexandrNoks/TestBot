from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from loader import bot


class IsChannel(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        status_user = await bot.get_chat_member(chat_id=message.chat.id,user_id=message.from_user.id)
        if status_user.status == types.ChatMemberStatus.MEMBER:
            return message.chat.type == types.ChatType.CHANNEL
