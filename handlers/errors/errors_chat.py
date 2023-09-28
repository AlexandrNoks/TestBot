import logging
from aiogram.exceptions import TelegramUnauthorizedError, TelegramAPIError,TelegramBadRequest, RestartingTelegram,UnsupportedKeywordArgument
from loader import dp
# Хэндлеры для обработки ошибок

# Обработка ошибки неправельный токен
@dp.error()
async def errors_handler(exception: Exception):
#     if isinstance(exception,TelegramUnauthorizedError):
#         logging.info(f"Unauthorized: {exception}")
#         return True
#
#     if isinstance(exception,UnsupportedKeywordArgument):
#         logging.info("Данные кнопки не верны!")
#         return True
#
#     if isinstance(exception,RestartingTelegram):
#         logging.info("Перезапуск телеграмма!")
#         return True
#
    if isinstance(exception, TelegramBadRequest):
        logging.exception(f"404 Плохой запрос! BadRequest")
        return True
#
#     if isinstance(exception,TelegramAPIError):
#         logging.exception(f"Ошибка API Телеграма! TelegramAPIError: {exception}\nUpdate: {update}")
#         return True
#
#     if isinstance(exception,ExceptionMessageFilter):
#         logging.exception(f"Не удалось распознать сообщение: {exception}\nUpdate: {update}")
#         return True
#
    logging.exception(f"Exception: {exception}")
#
