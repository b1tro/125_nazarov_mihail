from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

change_resume_keyboard = InlineKeyboardMarkup()

change_resume_keyboard.add(InlineKeyboardButton(text="Должность 🛠", callback_data="change_text"),
                           InlineKeyboardButton(text="Зарплата 🤑", callback_data="change_salary"),
                           InlineKeyboardButton(text="Населенный пункт 🚩", callback_data="change_area"),
                           InlineKeyboardButton(text="Метро 🚇", callback_data="change_metro"),
                           InlineKeyboardButton(text="Опыт 👨‍💻", callback_data="change_experience"),
                           InlineKeyboardButton(text="Занятость 🕓", callback_data="change_employment"),
                           InlineKeyboardButton(text="График 📊", callback_data="change_schedule"))
change_resume_keyboard.add(InlineKeyboardButton(text="Готово ✅", callback_data="done"))

change_check_delete_keyboard = InlineKeyboardMarkup()
change_check_delete_keyboard.add(InlineKeyboardButton(text="Редактировать резюме ✏️", callback_data="change_resume"),
                              InlineKeyboardButton(text="Удалить резюме ❌", callback_data="delete_resume"))
change_check_delete_keyboard.add(InlineKeyboardButton(text="Посмотреть резюме 👀", callback_data="check_resume"))

change_or_delete_keyboard= InlineKeyboardMarkup()
change_or_delete_keyboard.add(InlineKeyboardButton(text="Редактировать резюме ✏️", callback_data="change_resume"),
                              InlineKeyboardButton(text="Удалить резюме ❌", callback_data="delete_resume"))
change_or_delete_keyboard.add(InlineKeyboardButton(text="Поиск работы 💼 👀", callback_data="start_searching"))