from aiogram import Dispatcher, types
import SQL.user_data
from bot_initialize import bot
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from TELEGRAM.keyboards.keyboards_instance import create_resume
from SQL import user_data
import datetime
from HEADHUNTER.resume import resume_processing

class Resume(StatesGroup):
    title = State()
    salary = State()
    area = State()
    metro = State()
    experience = State()
    employment = State()
    schedule = State()

# @dp.message_handler(commands='resume', state = None, ignore_case = True)
async def start_creating_resume(message: types.Message, state: FSMContext):
    if (SQL.user_data.is_resume_exists(message.from_user.id)):
        await bot.send_message(message.from_user.id, "<b>У вас уже существует резюме. Вы можете обновить его, либо удалить.</b>",
                               parse_mode='HTML')
        await state.finish()
    else:
        await Resume.title.set()
        await state.update_data(user_id=message.from_user.id)
        await state.update_data(user_name = message.from_user.first_name + " " + message.from_user.last_name)
        await bot.send_message(message.from_user.id, "Напишите <b>ключевые слова</b> названия вакансии", parse_mode='HTML',
                               reply_markup=create_resume.no_matter_keyboard)

salary_state_text = """Отлично. Далее укажите желаемую зарплату в рублях(<b>цифрами,
без лишних знаков</b>)
<i>Пример: 60000</i>"""

# @dp.message_handler(state = Resume.title, content_types='text')
async def set_title(message: types.Message, state: FSMContext):
    await state.update_data(title=message.text.capitalize())
    await Resume.next()
    await bot.send_message(message.from_user.id, salary_state_text, parse_mode='HTML', reply_markup=create_resume.no_matter_keyboard)

area_state_text = """Принято. Далее укажите <b>населенный пункт</b>, в котором ищете работу.
<i>Пример: Москва</i>
<i>Пример: Республика Татарстан</i>
<i>Пример: Казахстан </i>
Важно - доступные страны:
Россия, Казахстан, Азербайджан, Беларусь, Грузия, Кыргызстан, Узбекистан, Другие регионы"""

# @dp.message_handler(state = Resume.salary, content_types='text')
async def set_salary(message: types.Message, state: FSMContext):
    await state.update_data(salary=message.text)
    await Resume.next()
    await bot.send_message(message.from_user.id, area_state_text,
                           parse_mode='HTML', reply_markup=create_resume.no_matter_keyboard)

metro_state_text = """Учтем. Подскажите <b>название станции метро</b>, чтобы понять территориально, где вы хотите работать.
Пример: Калужская
"""

# @dp.message_handler(state = Resume.area, content_types='text')
async def set_area(message: types.Message, state: FSMContext):
    await state.update_data(area=message.text.title())
    await Resume.next()
    await bot.send_message(message.from_user.id, metro_state_text,
                           parse_mode='HTML', reply_markup=create_resume.no_matter_keyboard)

experience_state_text = """Едем дальше. Пожалуйста, <b>выберите</b> свой опыт работы."""

# @dp.message_handler(state = Resume.metro, content_types='text')
async def set_metro(message: types.Message, state: FSMContext):
    await state.update_data(metro=message.text.capitalize())
    await Resume.next()
    await bot.send_message(message.from_user.id, experience_state_text,
                           parse_mode='HTML', reply_markup=create_resume.experience_keyboard)

employment_state_text = """Дальше. Пожалуйста, <b>выберите</b> выберите тип занятости."""

# @dp.message_handler(state = Resume.experience, content_types='text')
async def set_experience(message: types.Message, state: FSMContext):
    await state.update_data(experience=message.text)
    await Resume.next()
    await bot.send_message(message.from_user.id, employment_state_text,
                           parse_mode='HTML', reply_markup=create_resume.employment_keyboard)

employment_schedule_text = """Обработано. Пожалуйста, <b>выберите</b> тип графика работы."""


# @dp.message_handler(state = Resume.employment, content_types='text')
async def set_employment(message: types.Message, state: FSMContext):
    await state.update_data(employment=message.text)
    await Resume.next()
    await bot.send_message(message.from_user.id, employment_schedule_text,
                           parse_mode='HTML', reply_markup=create_resume.schedule_keyboard)

finish_state_text = """<b>Поздравляем! Ваше резюме сохранено.</b>"""

# @dp.message_handler(state = Resume.schedule, content_types='text')
async def set_schedule(message: types.Message, state: FSMContext):
    await state.update_data(schedule=message.text)
    await state.update_data(register_time=str(datetime.datetime.now()))
    await bot.send_message(message.from_user.id, finish_state_text,
                           parse_mode='HTML', reply_markup=create_resume.close_keyboard)
    client_resume = await state.get_data()
    client_resume_saved = (client_resume['user_id'], client_resume['user_name'],client_resume['register_time'], client_resume['title'],client_resume['salary'],client_resume['area'],
                                         client_resume['metro'],client_resume['experience'],client_resume['employment'],client_resume['schedule'])
    await state.finish()
    result = f"""
<b>Вакансия</b> - {client_resume['title']}
<b>Зарплата</b> - {client_resume['salary']} 
<b>Населенный пункт</b> - {client_resume['area']}
<b>Метро</b> - {client_resume['metro']}
<b>Опыт работы</b> - {client_resume['experience']}
<b>Занятость</b> - {client_resume['employment']}
<b>График работы</b> - {client_resume['schedule']}"""
    await bot.send_message(message.from_user.id, result, parse_mode="HTML")
    #Загружаем резюме в базу данных, изначальную и обработанную
    user_data.add_resume_to_base(tuple(client_resume_saved))
    resume_processing.send_processed_resume(list(client_resume_saved))

def register_create_resume_handlers(dp: Dispatcher):
    dp.register_message_handler(start_creating_resume,commands='resume', state = None)
    dp.register_message_handler(set_title, state = Resume.title, content_types='text')
    dp.register_message_handler(set_salary, state = Resume.salary, content_types='text')
    dp.register_message_handler(set_area,state = Resume.area, content_types='text')
    dp.register_message_handler(set_metro, state = Resume.metro, content_types='text')
    dp.register_message_handler(set_experience, state = Resume.experience, content_types='text')
    dp.register_message_handler(set_employment, state = Resume.employment, content_types='text')
    dp.register_message_handler(set_schedule, state = Resume.schedule, content_types='text')