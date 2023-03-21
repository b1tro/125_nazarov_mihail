from aiogram import Dispatcher,types, filters
from bot_initialize import bot
from TELEGRAM.keyboards.inline_keyboards_instance import change_resume_keyboard
from TELEGRAM.keyboards.keyboards_instance.start_keyboard import start_kb
from TELEGRAM.keyboards.keyboards_instance import create_resume
from TELEGRAM.keyboards.inline_keyboards_instance.change_resume_keyboard import change_check_delete_keyboard, change_or_delete_keyboard
import SQL.user_data
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from HEADHUNTER.resume import resume_processing

class Resume_values(StatesGroup):
    text = State()
    salary = State()
    area = State()
    experience = State()
    metro = State()
    employment = State()
    schedule = State()


# @dp.callback_query_handlers(filters.Text(equals="detele_resume"))
async def delete_resume(callback: types.CallbackQuery):
    SQL.user_data.delete_resume(callback.from_user.id)
    await bot.send_message(chat_id=callback.from_user.id, text="Ваше резюме <b>удалено</b>.", parse_mode='HTML',
                           reply_markup=start_kb)
    await callback.message.delete()

# @dp.callback_query_handlers(filters.Text(equals="change_resume"))
async def resume_change_command(callback : types.CallbackQuery):
    await callback.bot.send_message(text="Что вы хотите изменить?", chat_id=callback.from_user.id, reply_markup=change_resume_keyboard.change_resume_keyboard)

# @dp.callback_query_handlers(filters.Text(equals="check_resume"))
async def resume_check_command(callback : types.CallbackQuery):
    current_resume = SQL.user_data.send_resume(callback.from_user.id)
    current_resume_view = f"""
    <b>Вакансия</b> - {current_resume[0]}
    <b>Зарплата</b> - {current_resume[1]} 
    <b>Населенный пункт</b> - {current_resume[2]}
    <b>Метро</b> - {current_resume[3]}
    <b>Опыт работы</b> - {current_resume[4]}
    <b>Занятость</b> - {current_resume[5]}
    <b>График работы</b> - {current_resume[6]}"""
    await callback.bot.send_message(text=f"Ваше резюме на данный момент:\n {current_resume_view}",
                                    chat_id=callback.from_user.id, reply_markup=change_or_delete_keyboard, parse_mode='HTML')

# @dp.callback_query_handlers(filters.Text(equals="change_text"))
async def change_text(callback: types.CallbackQuery):
    await callback.bot.send_message(callback.from_user.id, text= "Меняем <b>названия вакансии</b>. Пожалуйста, укажите новое значение", parse_mode="HTML",
                                    reply_markup=create_resume.no_matter_keyboard)
    await Resume_values.text.set()

# @dp.message_handler(state="text")
async def set_new_text(message: types.Message, state: FSMContext):
    await state.finish()
    SQL.user_data.update_resume(message.from_user.id, "text", message.text)
    await bot.send_message(text="Поменяли. Что-то еще?",chat_id=message.from_user.id,reply_markup=change_resume_keyboard.change_resume_keyboard)

# @dp.callback_query_handlers(filters.Text(equals="change_salary"))
async def change_salary(callback: types.CallbackQuery):
    await callback.bot.send_message(callback.from_user.id, text= "Меняем <b>зарплату</b>. Пожалуйста, укажите новое значение", parse_mode="HTML",
                                    reply_markup=create_resume.no_matter_keyboard)
    await Resume_values.salary.set()

# @dp.message_handler(state="salary")
async def set_new_salary(message: types.Message, state: FSMContext):
    await state.finish()
    SQL.user_data.update_resume(message.from_user.id, "salary", message.text)
    await bot.send_message(text= "Поменяли. Что-то еще?", chat_id=message.from_user.id,reply_markup=change_resume_keyboard.change_resume_keyboard)

# @dp.callback_query_handlers(filters.Text(equals="change_area"))
async def change_area(callback: types.CallbackQuery):
    await callback.bot.send_message(callback.from_user.id,text= "Меняем <b>населенный пункт</b>. Пожалуйста, укажите новое значение", parse_mode="HTML",
                                    reply_markup=create_resume.no_matter_keyboard)
    await Resume_values.area.set()

# @dp.message_handler(state="change_area")
async def set_new_area(message: types.Message, state: FSMContext):
    await state.finish()
    SQL.user_data.update_resume(message.from_user.id, "area", message.text)
    await bot.send_message(text="Поменяли. Что-то еще?", chat_id=message.from_user.id,reply_markup=change_resume_keyboard.change_resume_keyboard)

# @dp.callback_query_handlers(filters.Text(equals="change_metro"))
async def change_metro(callback: types.CallbackQuery):
    await callback.bot.send_message(callback.from_user.id, text="Меняем <b>метро</b>. Пожалуйста, укажите новое значение", parse_mode="HTML",
                                    reply_markup=create_resume.no_matter_keyboard)
    await Resume_values.metro.set()

# @dp.message_handler(state="metro")
async def set_new_metro(message: types.Message, state: FSMContext):
    await state.finish()
    metro_data = (message.text).capitalize()
    SQL.user_data.update_resume(message.from_user.id, "metro", metro_data)
    await bot.send_message(text="Поменяли. Что-то еще?",chat_id=message.from_user.id,reply_markup=change_resume_keyboard.change_resume_keyboard)

# @dp.callback_query_handlers(filters.Text(equals="change_experience"))
async def change_experience(callback: types.CallbackQuery):
    await callback.bot.send_message(callback.from_user.id, text="Меняем <b>опыт</b>. Пожалуйста, укажите новое значение", parse_mode="HTML",
                                    reply_markup=create_resume.experience_keyboard)
    await Resume_values.experience.set()

# @dp.message_handler(state="experience")
async def set_new_experience(message: types.Message, state: FSMContext):
    await state.finish()
    SQL.user_data.update_resume(message.from_user.id, "experience", message.text)
    await bot.send_message(text="Поменяли. Что-то еще?",chat_id=message.from_user.id,reply_markup=change_resume_keyboard.change_resume_keyboard)

# @dp.callback_query_handlers(filters.Text(equals="change_employment"))
async def change_employment(callback: types.CallbackQuery):
    await callback.bot.send_message(callback.from_user.id, text="Меняем <b>занятость</b>. Пожалуйста, укажите новое значение", parse_mode="HTML",
                                    reply_markup=create_resume.employment_keyboard)
    await Resume_values.employment.set()

# @dp.message_handler(state="employment")
async def set_new_employment(message: types.Message, state: FSMContext):
    await state.finish()
    SQL.user_data.update_resume(message.from_user.id, "employment", message.text)
    await bot.send_message(text="Поменяли. Что-то еще?",chat_id=message.from_user.id,reply_markup=change_resume_keyboard.change_resume_keyboard)

# @dp.callback_query_handlers(filters.Text(equals="change_schedule"))
async def change_schedule(callback: types.CallbackQuery):
    await callback.bot.send_message(callback.from_user.id, text="Меняем <b>график</b>. Пожалуйста, укажите новое значение", parse_mode="HTML",
                                    reply_markup=create_resume.schedule_keyboard)
    await Resume_values.schedule.set()

# @dp.message_handler(state="schedule")
async def set_new_schedule(message: types.Message, state: FSMContext):
    await state.finish()
    SQL.user_data.update_resume(message.from_user.id, "schedule", message.text)
    await bot.send_message(text="Поменяли. Что-то еще?",chat_id=message.from_user.id,reply_markup=change_resume_keyboard.change_resume_keyboard)

# @dp.callback_query_handlers(filters.Text(equals="done"))
async def done_command(callback: types.CallbackQuery, state: FSMContext):
    adapted_values = resume_processing.adapt_changed_resume(SQL.user_data.send_resume_to_update(callback.from_user.id))
    SQL.user_data.update_adapted_resume(tuple(adapted_values), user_id=callback.from_user.id)
    updated_resume = SQL.user_data.send_resume(callback.from_user.id)
    updated_resume_view = f"""
<b>Вакансия</b> - {updated_resume[0]}
<b>Зарплата</b> - {updated_resume[1]} 
<b>Населенный пункт</b> - {updated_resume[2]}
<b>Метро</b> - {updated_resume[3]}
<b>Опыт работы</b> - {updated_resume[4]}
<b>Занятость</b> - {updated_resume[5]}
<b>График работы</b> - {updated_resume[6]}"""
    await callback.bot.send_message(text=f"Готово! Вот ваше резюме на данный момент:\n {updated_resume_view}",
                                    chat_id=callback.from_user.id, reply_markup=start_kb, parse_mode='HTML')


def register_change_resume_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(delete_resume, filters.Text(equals="delete_resume"))
    dp.register_callback_query_handler(resume_change_command,filters.Text(equals="change_resume"))
    dp.register_callback_query_handler(resume_check_command, filters.Text(equals="check_resume"))
    dp.register_callback_query_handler(change_text,filters.Text(equals="change_text"))
    dp.register_message_handler(set_new_text,state= Resume_values.text, content_types='text')
    dp.register_callback_query_handler(change_salary, filters.Text(equals="change_salary"))
    dp.register_message_handler(set_new_salary, state= Resume_values.salary, content_types='text')
    dp.register_callback_query_handler(change_area, filters.Text(equals="change_area"))
    dp.register_message_handler(set_new_area, state= Resume_values.area, content_types='text')
    dp.register_callback_query_handler(change_metro, filters.Text(equals="change_metro"))
    dp.register_message_handler(set_new_metro, state= Resume_values.metro, content_types='text')
    dp.register_callback_query_handler(change_experience, filters.Text(equals="change_experience"))
    dp.register_message_handler(set_new_experience,state= Resume_values.experience, content_types='text')
    dp.register_callback_query_handler(change_employment,filters.Text(equals="change_employment"))
    dp.register_message_handler(set_new_employment,state= Resume_values.employment, content_types='text')
    dp.register_callback_query_handler(change_schedule, filters.Text(equals="change_schedule"))
    dp.register_message_handler(set_new_schedule, state= Resume_values.schedule, content_types='text')
    dp.register_callback_query_handler(done_command, filters.Text(equals="done"))



