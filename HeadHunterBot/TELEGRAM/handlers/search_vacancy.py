from aiogram import Dispatcher, types, filters
import SQL.user_data
from bot_initialize import bot
import asyncio
from HEADHUNTER.searching import search
from TELEGRAM.keyboards.inline_keyboards_instance import searching_keyboard
from aiogram import filters

# @dp.message_handler(commands='search')
async def search_menu(message: types.Message):
    await bot.send_message(chat_id = message.from_user.id, text="Что делаем?", reply_markup=searching_keyboard.search_start)

async def stop_searching(callback: types.CallbackQuery):
    await callback.message.edit_text(text="Что делаем?")
    await callback.message.edit_reply_markup(reply_markup=searching_keyboard.search_start)

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

# dp.callback.query.handler(filters.Text(equals="save_vacancy"))
async def save_vacancy(callback: types.CallbackQuery):
    current_vacancy = [callback.from_user.id ,(search.searching.load_vacancies(callback.from_user.id, page = search.get_current_page(), vacancy_number=search.get_current_number()))]
    SQL.user_data.save_vacancy(current_vacancy)

async def show_saved_vacancies(callback: types.CallbackQuery):
    saved_vacancy = SQL.user_data.get_saved_vacancy.get_saved_vacancies(callback.from_user.id, 0)
    await bot.send_message(text=saved_vacancy, chat_id=callback.from_user.id, parse_mode='HTML',
                           reply_markup=searching_keyboard.next_saved_vacancy)

async def next_saved_vacancy(callback: types.CallbackQuery):
    saved_vacancy = SQL.user_data.get_saved_vacancy.get_saved_vacancies(callback.from_user.id, SQL.user_data.get_saved_vacancy.get_number(SQL.user_data.get_saved_vacancy))
    if saved_vacancy != False:
        await callback.message.edit_text(text=saved_vacancy,parse_mode='HTML')
        await asyncio.sleep(3)
        await callback.message.edit_reply_markup(reply_markup=searching_keyboard.next_saved_vacancy)
    else:
        await callback.message.edit_text(text="Кажется, вы просмотрели все свои сохраненные вакансии")
        await callback.message.edit_reply_markup(reply_markup=searching_keyboard.search_start)

async def delete_saved_vacancy(callback: types.CallbackQuery):
    data = SQL.user_data.get_saved_vacancy.get_saved_vacancies(callback.from_user.id, SQL.user_data.get_saved_vacancy.get_current_number(SQL.user_data.get_saved_vacancy))
    SQL.user_data.delete_saved_vanancy(callback.from_user.id, data)
    await bot.send_message(chat_id = callback.from_user.id, text="Удалено!")

def register_search_vacancy_handlers(dp: Dispatcher):
    dp.register_message_handler(search_menu, filters.Text(equals=('Поиск работы 💼')))

def register_search_vacancy_callback_handlers(dp: Dispatcher):
     dp.register_callback_query_handler(stop_searching, filters.Text(equals="stop_searching"))
     dp.register_callback_query_handler(send_next_vacancy, filters.Text(equals="next_vacancy"))
     dp.register_callback_query_handler(start_search, filters.Text(equals="start_searching"))
     dp.register_callback_query_handler(save_vacancy, filters.Text(equals="save_vacancy"))
     dp.register_callback_query_handler(show_saved_vacancies, filters.Text(equals="saved_vacancies"))
     dp.register_callback_query_handler(next_saved_vacancy, filters.Text(equals="next_saved_vacancy"))
     dp.register_callback_query_handler(delete_saved_vacancy, filters.Text(equals="delete_saved_vacancy"))
