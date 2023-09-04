import logging
from loader import dp
from aiogram.utils.exceptions import (Unauthorized, MessageCantBeDeleted, MessageToDeleteNotFound, MessageToPinNotFound, MessageToEditNotFound, ButtonDataInvalid, MessageIdInvalid, MessageTextIsEmpty,ButtonURLInvalid,MessageIdentifierNotSpecified,MessageNotModified,
                                      RestartingTelegram, CantParseEntities, InvalidQueryID, RetryAfter, BadRequest, TelegramAPIError, CantParseUrl)


# Хэндлеры для обработки ошибок

# Обработка ошибки неправельный токен
@dp.errors_handler()
async def errors_handler(update, exception):
    if isinstance(exception,Unauthorized):
        logging.info(f"Unauthorized: {exception}")
        return True

    if isinstance(exception,MessageCantBeDeleted):
        logging.info("Сообщение не может быть удалено!")
        return True

    if isinstance(exception,MessageToDeleteNotFound):
        logging.info("Сообщение для удаление не найдено!")
        return True

    if isinstance(exception,MessageToPinNotFound):
        logging.info("Сообщение для закрепления не найдено!")
        return True

    if isinstance(exception,MessageToEditNotFound):
        logging.info("Сообщение для обработки не найдено!")
        return True

    if isinstance(exception,ButtonDataInvalid):
        logging.info("Данные кнопки не верны!")
        return True

    if isinstance(exception,MessageIdInvalid):
        logging.info("id сообщения не найдено!")
        return True

    if isinstance(exception,ButtonURLInvalid):
        logging.info("Не верный URL адрес кнопки !")
        return True

    if isinstance(exception,MessageIdentifierNotSpecified):
        logging.info("Не указан id сообщения!")
        return True

    if isinstance(exception,RestartingTelegram):
        logging.info("Перезапуск телеграмма!")
        return True

    if isinstance(exception,MessageNotModified):
        logging.info("Сообщение не может быть изменено!")
        return True

    if isinstance(exception,MessageTextIsEmpty):
        logging.debug("Вы отправили пустое сообщение!")
        return True

    if isinstance(exception,CantParseEntities):
        logging.debug(f": Не удалось разобрать html тег!,ExseptionArgs: {exception.args}")
        return True

    if isinstance(exception,CantParseUrl):
        logging.debug(f": Не удалось разобрать URL адрес!,Exseption: {exception}")
        return True

    if isinstance(exception,RetryAfter):
        logging.exception(f"Повторите после! RetryAfter: {exception}\nUpdate: {update}")
        return True

    if isinstance(exception,BadRequest):
        logging.exception(f"404 Плохой запрос! BadRequest: {exception}\nUpdate: {update}")
        return True

    if isinstance(exception,TelegramAPIError):
        logging.exception(f"Ошибка API Телеграма! TelegramAPIError: {exception}\nUpdate: {update}")
        return True

    if isinstance(exception,InvalidQueryID):
        logging.info(f"InvalidQueryID: {exception } \nUpdate: {update} Не удалось идентифицировать запрос!")
        return True

    logging.exception(f"Update: {update}, \nException: {exception}")

