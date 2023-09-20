from aiogram import types, BaseMiddleware
from typing import Callable,Any, Dict, Awaitable
from data.config import WORDS, GROUP_ID, time_bun_sec
from loader import bot


def _is_message_chat(message: types.Message) -> bool:
    return message.text in WORDS


def _is_violation(user_id,chat_id):
    return bot.ban_chat_member(chat_id=chat_id,user_id=user_id)


class ForbiddenWordls(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[types.Message, Dict[str,Any]], Awaitable[Any]],
        event: types.Message,
        data: Dict[str, Any]
    ) -> Any:
        if _is_message_chat(message=event):
            await bot.delete_message(chat_id=GROUP_ID,message_id=event.message_id)
            await event.answer(f"В нашем чате есть свои правила, если вы их нарушаете, вы будите удалены!")
        else:
            return await handler(event,data)

