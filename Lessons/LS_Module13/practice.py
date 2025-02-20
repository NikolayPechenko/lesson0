import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

from practice_config import *
from practice_keyaboards import *
from practice_text import *
from admin import *

logging.basicConfig(level=logging.INFO)
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands='start')
async def star(message):
    await message.answer(f'Добро пожаловать, {message.from_user.username}. ' + start, reply_markup=start_kb)

#  message.answer_photo
#  message.answer_video
#  message.answer_file


@dp.message_handler(text='О нас')
async def info(message):
    with open('files/fotocartochka2.jpg', 'rb') as img:
        await message.answer_photo(img, about, reply_markup=start_kb)


@dp.message_handler(text='Стоимость')
async def price(message):
    await message.answer('Что вас интересует?', reply_markup=price_kb)


@dp.callback_query_handler(text='medium')
async def buy_m(call):
    await call.message.answer(Mgame, reply_markup=buy_kb)
    await call.answer()


@dp.callback_query_handler(text='big')
async def buy_l(call):
    await call.message.answer(Lgame, reply_markup=buy_kb)
    await call.answer()


@dp.callback_query_handler(text='mega')
async def buy_xl(call):
    await call.message.answer(XLgame, reply_markup=buy_kb)
    await call.answer()


@dp.callback_query_handler(text='other')
async def buy_other(call):
    await call.message.answer(other, reply_markup=buy_kb)
    await call.answer()


@dp.callback_query_handler(text='back_to_catalog')
async def back(call):
    await call.message.answer('Что вас интересует?', reply_markup=price_kb)
    await call.answer()


@dp.message_handler()
async def star(message):
    await message.answer('Рады вас видеть, для начала введите /start')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
