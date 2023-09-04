from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from data.config import WORDS, GROUP_ID, users_id
from loader import bot
from aiogram.dispatcher.handler import CancelHandler


# Проверяем состоит этот пользователь в группе или нет
class IsUserGroup(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        status_user = await bot.get_chat_member(chat_id=message.chat.id,user_id=message.from_user.id)
        return status_user.status != types.ChatMemberStatus.ADMINISTRATOR



# Сообщение от админа/создателя чата
class IsAdminGroup(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        user_admin = await bot.get_chat_member(chat_id=GROUP_ID,user_id=message.from_user.id)
        return user_admin.status == types.ChatMemberStatus.ADMINISTRATOR or user_admin.status == types.ChatMemberStatus.CREATOR


# Сообщение от забаненого пользователя
class IsUserBanned(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        ban_user = await bot.get_chat_member(chat_id=message.chat.id,user_id=message.from_user.id)
        if ban_user.status == types.ChatMemberStatus.BANNED:
            await bot.delete_message(message.chat.id,message.message_id)
        return ban_user == types.ChatType.SUPERGROUP









