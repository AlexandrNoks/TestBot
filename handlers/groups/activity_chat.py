from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from loader import bot,dp
from data.config import GROUP_ID, db, db_message, users_log


# Сохранить сообщение в БД
@dp.message_handler(text='save')
async def add_message_db(message: types.Message):
    get_user_id = types.User.get_current(no_error=True)
    if get_user_id['is_bot'] != True:
        db.add_message(message.message_id)
        await bot.send_message(GROUP_ID,'Спасибо сообщение добавлено!')

# Получить список всех сообщений
@dp.message_handler(Command('all',prefixes='/'))
async def add_message_db(message: types.Message):
    data = db.get_all_message()
    for i in data:
        await bot.send_message(GROUP_ID,f'{i}')


# Получение строки из БД по id
@dp.message_handler(Command('one',prefixes='/'))
async def get_command(message: types.Message):
    get_id = str(message.text[5:])
    res = db.get_one_message(get_id)
    for i in res:
        await bot.send_message(GROUP_ID, f"Это сообщение будет удалено {i}")


# Команда получить одного значение строки из БД по id
@dp.message_handler(Command('get',prefixes='/'))
async def get_command(message: types.Message):
    get_id = str(message.text[5:])
    res = db.get_answer_message(get_id)
    for i in res:
        await bot.send_message(GROUP_ID, f"Это сообщение будет удалено {i[0]}")


# Команда удаления сообщения из БД по id
@dp.message_handler(Command('del',prefixes='/'))
async def del_command(message: types.Message):
    get_id = str(message.text[5:])
    db.del_message(get_id)
    await bot.send_message(GROUP_ID, f"Сообщение с индексом {get_id} удалено!")


# Анализ всего чата за сутки
@dp.message_handler(Command('time',prefixes='/'))
async def analysis_chat(messege: types.Message):
    res = []
    get_objects = db_message.active_chat()
    for i in get_objects:
        if int(i[2][:2]) < 20:
            res.append(i)
        else:
            break
    await messege.reply(f"Analysis all chat {len(res)}")


# Анализ сообщений от конкретного пользователя за сутки
@dp.message_handler(Command('anl',prefixes='/'))
async def analysis_chat(messege: types.Message):
    get_objects = db_message.active_chat()
    for i in get_objects:
        if int(i[2][:2]) < 20:
            if int(i[0]) == 1673:
                await messege.reply(f"Analysis user {i}")
            else:
                break

# Команла Закрепить сообщение
@dp.message_handler(Command('pin',prefixes='/'))
async def pin_message(message: types.Message):
    user_message = message.message_id
    await bot.pin_chat_message(GROUP_ID,message_id=user_message)

# Команда вывести список админов
@dp.message_handler(Command('admin',prefixes='/'))
async def command_help(message: types.Message):
    log_user = " ".join(users_log).replace(" ","\n")
    await message.reply(f"Список админов: {log_user}")