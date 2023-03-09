from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
import os

HELP = """
Привет! Вот мой список команд!
<b>/help</b> - <i>ты здесь находишься</i>
<b>/give</b> - <i>запросить стикер</i>"""

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

#Keyboard
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
 #Buttons
help_button = KeyboardButton("/help")
description_button = KeyboardButton("/description")
close_button = KeyboardButton("/close")
heart_button = KeyboardButton("❤️")
 #Keyboard config
keyboard.add(help_button)
keyboard.add(description_button)
keyboard.add(close_button)
keyboard.add(heart_button)
@dp.message_handler(commands='help')
async def help_command(message: types.Message):
    await bot.send_message(message.from_user.id, text = HELP, parse_mode="HTML")
@dp.message_handler(commands='start')
async def start_command(message: types.Message):
    await bot.send_message(message.chat.id, text = "Давайте приступим!", reply_markup=keyboard)
@dp.message_handler(commands='description')
async def description_command(message: types.Message):
    await bot.send_message(message.from_user.id, text = "Я ботик")
@dp.message_handler(commands='close')
async def close_command(message: types.Message):
    await bot.send_message(message.chat.id, text = 'Закрываем!', reply_markup=ReplyKeyboardRemove())
@dp.message_handler()
async def heart_command(message: types.Message):
    if message.text == '❤️':
     await bot.send_sticker(message.chat.id,
                           sticker='CAACAgIAAxkBAAImxmQKK7DKzOlQiZcroINoWAXW99sqAAJkAQACo2hvF0B8-JdeFM-oLwQ')

executor.start_polling(dp, skip_updates=True)
