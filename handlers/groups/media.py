from aiogram import Bot, types, F, Router

from filters.chat_type import ChatTypeFilter
from loader import dp,bot
from data.config import GROUP_ID,CHANNEL_ID
from aiogram.types import BufferedInputFile, URLInputFile
from filters.chat_member import ChatMemberFilter
from middlewares.violation import ForbiddenWordsMiddleware
from middlewares.weekend import WeekendMessageMiddleware

# message_date = datetime.datetime.today().strftime('%d.%m.%Y')
# message_time = datetime.datetime.today().strftime('%H:%M')
router = Router()
router.message.filter(ChatTypeFilter(chat_type='supergroup'))
router.message.filter(ChatMemberFilter(chat_member='member'))
router.message.middleware(ForbiddenWordsMiddleware())
router.message.middleware(WeekendMessageMiddleware())

# Кнопка Отправить фото или видео в чат
@router.callback_query(F.data.startswith("media"))
async def media_file(call: types.CallbackQuery):
    if call.data == "mediaPhoto":
        file_ids = []
        with open('media/photos/file_20.jpg', 'rb') as image_from_buffer:
            photo_chat = await call.message.answer_photo(
                BufferedInputFile(
                    image_from_buffer.read(),filename='image_from_buffer.jpg'),caption='Изоброжение из буферобмена')
        file_ids.append(photo_chat.photo[-1].file_id)
        await bot.send_photo(chat_id=GROUP_ID,photo=file_ids[-1])
        await bot.send_photo(chat_id=CHANNEL_ID,photo=file_ids[-1])
    if call.data == "mediaVideo":
        file_ids = []
        with open('media/photos/test_3.mp4', 'rb') as video_from_buffer:
            video_chat = await call.message.answer_video(
                BufferedInputFile(
                    video_from_buffer.read(),filename='video_from_buffer.mp4'),caption='Видео из буферобмена')
        file_ids.append(video_chat.video.file_id)
        await bot.send_video(chat_id=GROUP_ID,video=file_ids[-1])
        await bot.send_video(chat_id=CHANNEL_ID,video=file_ids[-1])

# Получить фото и отправить на канал
@router.message(F.photo)
async def photo_group(message: types.Message):
    file_ids = []
    photo_chat = message.photo[-1].file_id
    file_ids.append(photo_chat)
    await bot.send_photo(chat_id=CHANNEL_ID,photo=file_ids[-1])
    await bot.send_message(GROUP_ID,"Фото получено и опубликовано на нашем канале ")


# Получить фото по ссылке
@dp.message(F.photo)
async def photo_url_group(message: types.Message):
    file_ids = []
    image_from_url = URLInputFile('https://.../')
    photo_url = await message.answer_photo(image_from_url,caption='Изоброжение из буферобмена')
    file_ids.append(photo_url.photo[-1].file_id)
    await dp.bot.send_photo(chat_id=CHANNEL_ID,photo=file_ids[-1])


# Получить и сохранить фото
@dp.message(F.photo)
async def download_photo(message: types.Message, bot: Bot):
    await bot.download(message.photo[-1],destination=f"media/photos{message.photo[-1].file_id}")


# Получить и сохранить фото
@dp.message(F.video)
async def download_video(message: types.Message, bot: Bot):
    await bot.download(message.video[-1],destination=f"media/{message.video[-1].file_id}")


# @dp.callback_query(F.data == "ToShare")
# async def to_share(call: types.CallbackQuery):
#     if call.data == "ToShare":
#         for user in users_log:
#             try:
#                 await bot.send_message(1875053743,text=f"Поделитесь с друзьями @{user}")
#             except StopIteration:
#                 break