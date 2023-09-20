from aiogram import BaseMiddleware
from aiogram.types import Message,CallbackQuery
from typing import Awaitable,Any,Callable,Dict
from datetime import datetime


def _is_weekend() -> bool:
    return datetime.utcnow().weekday() in (5, 6)

def _is_holiday() -> bool:
    holiday = (1,(list(range(1,11))))
    return datetime.utcnow().month == holiday[0] and datetime.utcnow().day in holiday[1]


class WeekendMessageMiddlewares(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message,Dict[str,Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str,Any]
    ) -> Any:
        if not _is_weekend():
            return await handler(event, data)
        else:
            await event.answer("Сегодня у нас выходной")
        if not _is_holiday():
            return await handler(event,data)
        else:
            await event.answer("Каникулы")


class WeekendCallbackDataMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[CallbackQuery,Dict[str,Any]],Awaitable[Any]],
        event: CallbackQuery,
        data: Dict[str,Any]
    ) -> Any:
        if not _is_weekend():
            return await handler(event,data)
        await event.answer("Выходные",show_alert=True)
        return









