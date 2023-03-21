from aiogram import Dispatcher, types, filters
import SQL.user_data
from bot_initialize import bot
import asyncio
from HEADHUNTER.searching import search
from TELEGRAM.keyboards.inline_keyboards_instance import searching_keyboard
from aiogram import filters

# @dp.message_handler(commands='search')
async def start_search(message: types.Message):
    try:
        search.searching.number = 0
        search.searching.page = 0
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


        if search.searching.load_vacancies(message.from_user.id, page = 0, vacancy_number=0) == "Не найдено ни одной вакансии. Попробуйте поменять зарплату, имя вакансии и станцию метро.":
            await bot.send_message(chat_id=message.from_user.id,
                                   text=search.searching.load_vacancies(message.from_user.id, page=0, vacancy_number=0),
                                   parse_mode="HTML", reply_markup=searching_keyboard.edit_resume)
        else:
            await bot.send_message(chat_id=message.from_user.id,
                                   text=search.searching.load_vacancies(message.from_user.id, page=0, vacancy_number=0),
                                   parse_mode="HTML", reply_markup=searching_keyboard.next_vacancy_keyboard)
    except IndexError:
        await bot.send_message(chat_id=message.from_user.id, text="Пожалуйста, сначала создайте резюме.")
# @dp.callback_query_handler(filters.Text(equals="next_vacancy"))
async def send_next_vacancy(callback: types.CallbackQuery):
    await callback.message.edit_text(text=search.searching.load_vacancies(callback.from_user.id, page = search.get_page(), vacancy_number=search.get_number()),
                                     parse_mode="HTML")
    await asyncio.sleep(3)
    await callback.message.edit_reply_markup(reply_markup=searching_keyboard.next_vacancy_keyboard)

def register_search_vacancy_handlers(dp: Dispatcher):
    dp.register_message_handler(start_search, filters.Text(equals=('Поиск работы 💼')))

def register_search_vacancy_callback_handlers(dp: Dispatcher):
     dp.register_callback_query_handler(send_next_vacancy, filters.Text(equals="next_vacancy"))
     dp.register_callback_query_handler(start_search, filters.Text(equals="start_searching"))