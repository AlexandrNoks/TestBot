from aiogram.filters import BaseFilter
from aiogram import types
from typing import Union,List

from aiogram.enums.chat_member_status import ChatMemberStatus
from aiogram.filters import ChatMemberUpdatedFilter
from loader import bot
from data.config import GROUP_ID



class ChatMemberFilter(BaseFilter):
    def __init__(self, chat_member: Union[str,list]):
        self.chat_member = chat_member

    async def __call__(self, message: types.Message) -> bool:
        users = await bot.get_chat_member(chat_id=GROUP_ID,user_id=message.from_user.id)
        user_status = users.status
        my_str = ''
        for user in user_status:
            my_str += user
        if isinstance(self.chat_member, str):
            return my_str == self.chat_member
        else:
            return my_str in self.chat_member
