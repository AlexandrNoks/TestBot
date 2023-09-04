from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from data.config import GROUP_ID
from loader import bot
# Фильтры сообщений приватного чата

# Пользователь еще находится в чате
class IsPrivateChat(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        status_user = await bot.get_chat_member(GROUP_ID,message.from_user.id)
        if status_user.status == types.ChatMemberStatus.MEMBER:
            return message.chat.id == types.ChatType.PRIVATE

# Пользователь который еще не зашел в чат
class IsNewUser(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        status_user = await bot.get_chat_member(GROUP_ID,message.from_user.id)
        if status_user.status != types.ChatMemberStatus.MEMBER or status_user.status != types.ChatMemberStatus.KICKED and status_user.status != types.ChatMemberStatus.LEFT:
            return message.chat.id == types.ChatType.PRIVATE

# Вышел из чата
class IsUserLeftChat(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        left_user = await bot.get_chat_member(chat_id=GROUP_ID,user_id=message.from_user.id)
        if left_user.status == types.ChatMemberStatus.LEFT:
            return message.chat.id == types.ChatType.PRIVATE





