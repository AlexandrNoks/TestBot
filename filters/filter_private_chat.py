# from aiogram import types
# from typing import Union
# from aiogram.filters import BaseFilter
# from data.config import GROUP_ID
# from loader import bot
# from aiogram.types import Message
# # Фильтры сообщений приватного чата
#
# # Пользователь еще находится в чате
#
# class ChatTypeFilter(BaseFilter):
#     def __init__(self, chat_type: Union[str, list]):
#         self.chat_type = chat_type
#
#     def __call__(self,message: Message) -> bool:
#         if isinstance(self.chat_type, str):
#             return message.chat.type == self.chat_type
#         else:
#             return message.chat.type in self.chat_type
#
# class IsPrivateChat(BaseFilter):
#     async def check(self, message: types.Message) -> bool:
#         status_user = await bot.get_chat_member(GROUP_ID,message.from_user.id)
#         if status_user.status == types.ChatMemberStatus.MEMBER:
#             return message.chat.id == types.ChatType.PRIVATE
#
# # Пользователь который еще не зашел в чат
# class IsNewUser(BoundFilter):
#     async def check(self, message: types.Message) -> bool:
#         status_user = await bot.get_chat_member(GROUP_ID,message.from_user.id)
#         if status_user.status != types.ChatMemberStatus.MEMBER or status_user.status != types.ChatMemberStatus.KICKED and status_user.status != types.ChatMemberStatus.LEFT:
#             return message.chat.id == types.ChatType.PRIVATE
#
# # Вышел из чата
# class IsUserLeftChat(BoundFilter):
#     async def check(self, message: types.Message) -> bool:
#         left_user = await bot.get_chat_member(chat_id=GROUP_ID,user_id=message.from_user.id)
#         if left_user.status == types.ChatMemberStatus.LEFT:
#             return message.chat.id == types.ChatType.PRIVATE
#
#
#
#
#
