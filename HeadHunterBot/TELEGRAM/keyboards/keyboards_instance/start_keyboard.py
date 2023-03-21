from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_kb = ReplyKeyboardMarkup(resize_keyboard=True)
start_kb.add(KeyboardButton('Резюме 📋'), KeyboardButton('Поиск работы 💼'))