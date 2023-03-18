from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

no_matter_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
no_matter_keyboard.add(KeyboardButton("Нет значения"))

experience_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
experience_keyboard.add(KeyboardButton("Нет опыта"), KeyboardButton("От 1 года до 3 лет"),
                        KeyboardButton("От 3 до 6 лет"),KeyboardButton("Более 6 лет"),
                        KeyboardButton("Не имеет значения"))

employment_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
employment_keyboard.add(KeyboardButton("Полная занятость"),
                        KeyboardButton("Частичная занятость"),
                         KeyboardButton("Проектная работа"),
                          KeyboardButton("Волонтерство"),
                           KeyboardButton("Стажировка"),
                        KeyboardButton("Не имеет значения"))

schedule_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
schedule_keyboard.add(KeyboardButton("Полный день"),
                        KeyboardButton("Сменный график"),
                         KeyboardButton("Гибкий график"),
                          KeyboardButton("Удаленная работа"),
                           KeyboardButton("Вахтовый метод"),
                        KeyboardButton("Не имеет значения"))

close_keyboard = ReplyKeyboardRemove()