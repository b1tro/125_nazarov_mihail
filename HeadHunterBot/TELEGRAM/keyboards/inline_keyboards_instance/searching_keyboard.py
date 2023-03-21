from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove

next_vacancy_keyboard = InlineKeyboardMarkup()
next_vacancy_keyboard.add(InlineKeyboardButton(text="Следующая вакансия ➡️", callback_data="next_vacancy"))
next_vacancy_keyboard.add(InlineKeyboardButton(text="Сохранить вакансию 📩", callback_data="save_vacancy"))
next_vacancy_keyboard.add(InlineKeyboardButton(text="Закончить просмотр 🛑", callback_data="stop_searching"))

edit_resume = InlineKeyboardMarkup()
edit_resume.add(InlineKeyboardButton(text="Редактировать резюме ✏️", callback_data="change_resume"))

search_start = InlineKeyboardMarkup()
search_start.add(InlineKeyboardButton(text="Назад к резюме ⬅️ ", callback_data="check_resume"),
                 InlineKeyboardButton(text="Искать работу 🔎", callback_data="start_searching"))
search_start.add(InlineKeyboardButton(text="Посмотреть сохраненные вакансии 📖️", callback_data="saved_vacancies"))

next_saved_vacancy = InlineKeyboardMarkup()
next_saved_vacancy.add(InlineKeyboardButton(text="Следующая вакансия ➡️", callback_data="next_saved_vacancy"))
next_saved_vacancy.add(InlineKeyboardButton(text="Удалить из сохраненного 🗑", callback_data="delete_saved_vacancy"))