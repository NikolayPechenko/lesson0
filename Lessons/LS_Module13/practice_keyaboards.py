from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text='Стоимость')
button2 = KeyboardButton(text='О нас')
start_kb.add(button1)
start_kb.insert(button2)

price_kb = InlineKeyboardMarkup(resize_keyboard=True)
button3 = InlineKeyboardButton(text='Средняя игра', callback_data='medium')
button4 = InlineKeyboardButton(text='Большая игра', callback_data='big')
button5 = InlineKeyboardButton(text='Очень большая игра', callback_data='mega')
button6 = InlineKeyboardButton(text='Что-то другое', callback_data='other')
price_kb.add(button3)
price_kb.add(button4)
price_kb.add(button5)
price_kb.add(button6)

buy_kb = InlineKeyboardMarkup(resize_keyboard=True)
button7 = InlineKeyboardButton(text='Купить', url='http://ya.ru')
button8 = InlineKeyboardButton(text='Назад', callback_data='back_to_catalog')
buy_kb.add(button7)
buy_kb.add(button8)

admin_panel = InlineKeyboardMarkup(resize_keyboard=True)
button9 = InlineKeyboardButton(text='Пользователи', callback_data='users')
button10 = InlineKeyboardButton(text='Статистика', callback_data='stats')
button11 = InlineKeyboardButton(text='Блокировка', callback_data='block')
button12 = InlineKeyboardButton(text='Разблокировка', callback_data='unblock')
admin_panel.add(button9)
admin_panel.add(button10)
admin_panel.row(button10, button11)