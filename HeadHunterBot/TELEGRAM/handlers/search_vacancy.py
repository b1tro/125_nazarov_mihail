from aiogram import Dispatcher, types
import SQL.user_data
from bot_initialize import bot, dp
from SQL import user_data
from HEADHUNTER.searching import search

# @dp.message_handler(commands='search')
async def start_search(message: types.Message):
    if SQL.user_data.is_adapted_resume_exists(message.from_user.id):
        resume = SQL.user_data.send_resume(message.from_user.id)
        await bot.send_message(chat_id= message.from_user.id ,text = f"""Ищем вакансии по резюме:
    <b>Вакансия</b> - {resume[0]}
    <b>Зарплата</b> - {resume[1]} 
    <b>Населенный пункт</b> - {resume[2]}
    <b>Метро</b> - {resume[3]}
    <b>Опыт работы</b> - {resume[4]}
    <b>Занятость</b> - {resume[5]}
    <b>График работы</b> - {resume[6]}
                               """, parse_mode='HTML')
        await bot.send_message(chat_id= message.from_user.id, text=search.load_vacancies(message.from_user.id, "1"), parse_mode="HTML")
    else:
        await bot.send_message(chat_id=message.from_user.id, text="Пожалуйста, сначала создайте резюме.")

def register_search_vacancy_handlers(dp: Dispatcher):
    dp.register_message_handler(start_search, commands='search')