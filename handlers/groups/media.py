from aiogram.types import InputFile, MediaGroup, InlineKeyboardMarkup, InlineKeyboardButton
from filters.filter_group import *
from loader import dp,bot
from data.config import GROUP_ID,users_log, CHANNEL_ID
from aiogram.dispatcher.filters.builtin import ChatTypeFilter


# message_date = datetime.datetime.today().strftime('%d.%m.%Y')
# message_time = datetime.datetime.today().strftime('%H:%M')


# Получить id photo
@dp.message_handler(ChatTypeFilter(chat_type=[types.ChatType.SUPERGROUP, types.ChatType.GROUP]),content_types=types.ContentTypes.PHOTO)
async def photo_group(message: types.Message):
    await message.reply(message.photo[-1].file_id)
    await dp.bot.send_photo(chat_id=CHANNEL_ID,photo_bytes=InputFile(path_or_bytesio="media/"))


# Получить id видео
@dp.message_handler(ChatTypeFilter(chat_type=[types.ChatType.SUPERGROUP, types.ChatType.GROUP]),content_types=types.ContentTypes.VIDEO)
async def video_group(message: types.Message):
    await message.reply(message.video[-1].file_id)


# Получить фото
@dp.message_handler(ChatTypeFilter(chat_type=[types.ChatType.SUPERGROUP, types.ChatType.GROUP]),content_types=types.ContentTypes.PHOTO)
async def get_photo(message: types.Message):
    await dp.bot.send_photo(chat_id=CHANNEL_ID,photo_bytes=InputFile(path_or_bytesio="media/"))


@dp.message_handler(ChatTypeFilter(chat_type=[types.ChatType.SUPERGROUP, types.ChatType.GROUP]),content_types=types.ContentTypes.PHOTO)
async def send_photo(message: types.Message):
    await message.photo[-1].download(destination_dir="media/")
    await dp.bot.send_photo(chat_id=CHANNEL_ID,photo=InputFile(path_or_bytesio="media/photos/file_1.jpg"))

@dp.message_handler(ChatTypeFilter(chat_type=[types.ChatType.SUPERGROUP, types.ChatType.GROUP]),content_types=types.ContentTypes.VIDEO)
async def send_photo(message: types.Message):
    await message.photo[-1].download(destination_dir="media/")
    await dp.bot.send_photo(chat_id=GROUP_ID,photo=InputFile(path_or_bytesio="media/photos/file_1.jpg"))


# Получить видео
@dp.message_handler(ChatTypeFilter(chat_type=[types.ChatType.SUPERGROUP, types.ChatType.GROUP]),content_types=types.ContentTypes.VIDEO)
async def get_video(message: types.Message):
    await dp.bot.send_video(chat_id=GROUP_ID,video_bytes=InputFile(path_or_bytesio="media/"))


@dp.callback_query_handler(text_contains="mailing")
async def send_media(call: types.CallbackQuery):
    if call.data == "mailingPhoto":
        album = MediaGroup()
        album.attach_photo(InputFile("media/photo/c.jpg"))
        album.attach_photo(InputFile("media/photo/c1.jpg"))
        album.attach_photo(InputFile("media/photo/c2.jpg"))
        btn_to_share = InlineKeyboardMarkup(row_width=1)
        to_share = InlineKeyboardButton(text="Поделиться", callback_data="ToShare")
        btn_to_share.insert(to_share)
        await bot.send_media_group(call.message.chat.id,media=album)
        await bot.send_message(call.message.chat.id,"Поделиться альбомом",reply_markup=btn_to_share)
    elif call.data == "mailingVideo":
        album = MediaGroup()
        album.attach_photo(InputFile("media/video/c.jpg"))
        album.attach_photo(InputFile("media/video/c1.jpg"))
        album.attach_photo(InputFile("media/video/c2.jpg"))
        await bot.send_media_group(call.message.chat.id,media=album)
    elif call.data == "mailingExit":
        await bot.delete_message(chat_id=GROUP_ID,message_id=call.message.message_id)
# @dp.message_handler(IsPrivate(),text="Поделиться")
# async def mailing_chat(message: types.Message):
#     await bot.send_message(GROUP_ID,"Поделиться с друзьями",reply_markup=to_share_btn)

@dp.callback_query_handler(text_contains="ToShare",)
async def to_share(call: types.CallbackQuery):
    if call.data == "ToShare":
        for user in users_log:
            try:
                await bot.send_message(1875053743,text=f"Поделитесь с друзьями @{user}")
            except StopIteration:
                break