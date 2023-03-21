from aiogram import executor
from bot_initialize import dp
from TELEGRAM.handlers import client
from TELEGRAM.handlers import create_resume, search_vacancy, change_resume

client.register_client_handlers(dp)
create_resume.register_create_resume_handlers(dp)
search_vacancy.register_search_vacancy_handlers(dp)
search_vacancy.register_search_vacancy_callback_handlers(dp)
change_resume.register_change_resume_callback_handlers(dp)
executor.start_polling(dp, skip_updates=True)
