from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton,BufferedInputFile
from aiogram import types, F
from loader import dp,bot
from filters.chat_type import ChatTypeFilter
from filters.chat_member import ChatMemberFilter
from data.config import CHANNEL_URL, WORDS, CHANNEL_ID, GROUP_ID


# @dp.message(F.text == "Запустить")
# async def new_user(message: types.Message, state: FSMContext):
#     mailing_channel = ReplyKeyboardMarkup(
#         keyboard=[
#             [
#                 KeyboardButton(text="Отправить фото"),
#                 KeyboardButton(text="Отправить Видео"),
#                 KeyboardButton(text="Отправить пост")
#             ]
#         ], resize_keyboard=True)
#     await message.answer(f"Канал",reply_markup=mailing_channel)
#
#
# @dp.message(ChatTypeFilter(chat_type=['group', 'supergroup']), F.photo)
# async def photo_group(message: types.Message):
#     file_ids = []
#     with open('media/photos/file_1.jpg', 'rb') as image_from_buffer:
#         photo_chat = await message.answer_photo(
#             BufferedInputFile(
#                 image_from_buffer.read(),filename='image_from_buffer.jpg'),caption='Изоброжение из буферобмена')
#     file_ids.append(photo_chat.photo[-1].file_id)
#     await bot.send_photo(chat_id=GROUP_ID,photo=file_ids[-1])
#     await bot.send_photo(chat_id=CHANNEL_ID,photo=file_ids[-1])
#
#
# @dp.callback_query(F.data.startswitch("EnterChannel"))
# async def mailing_chat(call: types.CallbackQuery):
#     mailing_channel = ReplyKeyboardMarkup(
#         keyboard=[
#             [
#                 KeyboardButton(text="Отправить фото"),
#                 KeyboardButton(text="Отправить Видео"),
#                 KeyboardButton(text="Отправить пост")
#             ]
#         ], resize_keyboard=True)
#
#     await call.message.answer(f"Канал",reply_markup=mailing_channel)