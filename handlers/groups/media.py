from aiogram import Bot, types, F
from aiogram.types import InputFile, InlineKeyboardMarkup, InlineKeyboardButton

from loader import dp,bot
from data.config import GROUP_ID,users_log, CHANNEL_ID
from filters.chat_type import ChatTypeFilter
from aiogram.types import FSInputFile, URLInputFile, BufferedInputFile


# message_date = datetime.datetime.today().strftime('%d.%m.%Y')
# message_time = datetime.datetime.today().strftime('%H:%M')

# Получить id photo
@dp.message(ChatTypeFilter(chat_type=['private', 'supergroup']), F.photo)
async def photo_group(message: types.Message):
    file_ids = []
    with open('media/photos/file_1.jpg', 'rb') as image_from_buffer:
        photo_chat = await message.answer_photo(
            BufferedInputFile(
                image_from_buffer.read(),filename='image_from_buffer.jpg'),caption='Изоброжение из буферобмена')
    file_ids.append(photo_chat.photo[-1].file_id)
    await bot.send_photo(chat_id=GROUP_ID,photo=file_ids[-1])
    await bot.send_photo(chat_id=CHANNEL_ID,photo=file_ids[-1])


@dp.message(ChatTypeFilter(chat_type=['private', 'supergroup']), F.video)
async def video_group(message: types.Message):
    file_ids = []
    with open('media/videos/test_3.mp4', 'rb') as video_from_buffer:
        video_chat = await message.answer_video(
            BufferedInputFile(
                video_from_buffer.read(),filename='video_from_buffer.mp4'),caption='Видео из буферобмена')
    file_ids.append(video_chat.video[-1].file_id)
    await bot.send_video(chat_id=GROUP_ID,video=file_ids[-1])
    await bot.send_video(chat_id=CHANNEL_ID,video=file_ids[-1])


# Отправка фото по ссылке
@dp.message(ChatTypeFilter(chat_type=['supergroup','group']), F.photo)
async def photo_url_group(message: types.Message):
    file_ids = []
    image_from_url = URLInputFile('https://.../')
    photo_url = await message.answer_photo(image_from_url,caption='Изоброжение из буферобмена')
    file_ids.append(photo_url.photo[-1].file_id)
    await dp.bot.send_photo(chat_id=CHANNEL_ID,photo=file_ids[-1])

# @dp.message(ChatTypeFilter(chat_type=['group', 'supergroup']))
# async def video_group(message: types.Message):
#     file_ids = []
#     with open('media/', 'rb') as image_from_buffer:
#         photo_chat = await message.answer_video(
#             BufferedInputFile(
#                 image_from_buffer.read(),filename='video_from_buffer.avi'),caption='Видео из буферобмена')
#     file_ids.append(photo_chat.photo[-1].file_id)
#     await dp.bot.send_photo(chat_id=CHANNEL_ID,photo=file_ids[-1])

# @dp.message(ChatTypeFilter(chat_type=['group', 'supergroup']))
# async def video_url_group(message: types.Message):
#     file_ids = []
#     image_from_url = URLInputFile('https://.../')
#     video_url = await message.answer_video(image_from_url,caption='Видео по ссылке')
#     file_ids.append(video_url.video[-1].file_id)
    # await dp.bot.se(chat_id=CHANNEL_ID,video=file_ids[-1])

# Загрузить фото
@dp.message(ChatTypeFilter(chat_type=['group', 'supergroup']))
async def download_photo(message: types.Message, bot: Bot):
    await bot.download(message.photo[-1],destination=f"media/photos{message.photo[-1].file_id}")


# Загрузить видео
@dp.message(ChatTypeFilter(chat_type=['group', 'supergroup']))
async def download_video(message: types.Message, bot: Bot):
    await bot.download(message.video[-1],destination=f"media/{message.video[-1].file_id}")

# @dp.callback_query(F.data == "mailing")
# async def send_media(call: types.CallbackQuery):
#     if call.data == "mailingPhoto":
#         album = MediaGroup()
#         album.attach_photo(InputFile("media/photo/c.jpg"))
#         album.attach_photo(InputFile("media/photo/c1.jpg"))
#         album.attach_photo(InputFile("media/photo/c2.jpg"))
#         btn_to_share = InlineKeyboardMarkup(row_width=1)
#         to_share = InlineKeyboardButton(text="Поделиться", callback_data="ToShare")
#         btn_to_share.insert(to_share)
#         await bot.send_media_group(call.message.chat.id,media=album)
#         await bot.send_message(call.message.chat.id,"Поделиться альбомом",reply_markup=btn_to_share)
#     elif call.data == "mailingVideo":
#         album = MediaGroup()
#         album.attach_photo(InputFile("media/video/c.jpg"))
#         album.attach_photo(InputFile("media/video/c1.jpg"))
#         album.attach_photo(InputFile("media/video/c2.jpg"))
#         await bot.send_media_group(call.message.chat.id,media=album)
#     elif call.data == "mailingExit":
#         await bot.delete_message(chat_id=GROUP_ID,message_id=call.message.message_id)
# # @dp.message_handler(IsPrivate(),text="Поделиться")
# # async def mailing_chat(message: types.Message):
# #     await bot.send_message(GROUP_ID,"Поделиться с друзьями",reply_markup=to_share_btn)
#
# @dp.callback_query(F.data == "ToShare")
# async def to_share(call: types.CallbackQuery):
#     if call.data == "ToShare":
#         for user in users_log:
#             try:
#                 await bot.send_message(1875053743,text=f"Поделитесь с друзьями @{user}")
#             except StopIteration:
#                 break