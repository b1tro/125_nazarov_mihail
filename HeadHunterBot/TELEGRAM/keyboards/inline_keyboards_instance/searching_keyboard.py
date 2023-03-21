from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove

next_vacancy_keyboard = InlineKeyboardMarkup()
next_vacancy_keyboard.add(InlineKeyboardButton(text="Следующая вакансия ➡️", callback_data="next_vacancy"))

edit_resume = InlineKeyboardMarkup()
edit_resume.add(InlineKeyboardButton(text="Редактировать резюме ✏️", callback_data="change_resume"))