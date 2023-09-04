from aiogram.types import InputFile, MediaGroup, InlineKeyboardMarkup, InlineKeyboardButton
from filters.filter_group import *
from loader import dp,bot
from data.config import GROUP_ID
from aiogram.dispatcher.filters.builtin import  ChatTypeFilter



# Получить id photo
@dp.message_handler(text="Hi")
async def photo_group(message: types.Message):
    status_user = message.text
    await bot.send_message(message.chat.id,f"Hi {status_user}")

@dp.message_handler(ChatTypeFilter(chat_type=[types.ChatType.SUPERGROUP, types.ChatType.GROUP]),content_types=types.ContentTypes.PHOTO)
async def send_photo(message: types.Message):
    await dp.bot.send_photo(chat_id=GROUP_ID,photo=InputFile(path_or_bytesio="media/photos/file_1.jpg"))

# Получить id photo
# @dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.CHANNEL),content_types=types.ContentTypes.PHOTO)
# async def photo_group(message: types.Message):
#     await message.answer("Hello!")
#
#
# # Получить id видео
# @dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.CHANNEL),content_types=types.ContentTypes.VIDEO)
# async def video_group(message: types.Message):
#     await message.reply(message.video[-1].file_id)


# Получить фото
@dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.CHANNEL),content_types=types.ContentTypes.PHOTO)
async def get_photo(message: types.Message):
    await dp.bot.send_photo(chat_id=message.channel_chat_created,photo_bytes=InputFile(path_or_bytesio="media/"))

# Получить видео
@dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.CHANNEL),content_types=types.ContentTypes.VIDEO)
async def get_video(message: types.Message):
    await dp.bot.send_video(chat_id=GROUP_ID,video_bytes=InputFile(path_or_bytesio="media/"))