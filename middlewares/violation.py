from aiogram import types, BaseMiddleware
from typing import Callable,Any, Dict, Awaitable
from TestBot.data.config import WORDS, GROUP_ID
from TestBot.loader import bot


def _is_message_chat(message: types.Message) -> bool:
    user_text = message.text
    return user_text.lower() in WORDS


class ForbiddenWordsMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[types.Message, Dict[str,Any]], Awaitable[Any]],
        event: types.Message,
        data: Dict[str, Any]
    ) -> Any:
        if _is_message_chat(message=event):
            await event.answer("В нашем чате есть свои правила, если вы их нарушаете, вы будите удалены!")
            return await bot.delete_message(chat_id=GROUP_ID,message_id=event.message_id)
        else:
            return await handler(event,data)

