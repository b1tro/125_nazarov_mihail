from aiogram import executor
from bot_initialize import dp
from TELEGRAM.handlers import client
from TELEGRAM.handlers import create_resume, search_vacancy

client.register_client_handlers(dp)
create_resume.register_create_resume_handlers(dp)
search_vacancy.register_search_vacancy_handlers(dp)
executor.start_polling(dp, skip_updates=True)
