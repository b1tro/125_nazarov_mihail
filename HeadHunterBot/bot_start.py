from aiogram import executor
from bot_initialize import dp
from TELEGRAM.handlers import client
from TELEGRAM.handlers import create_resume

client.register_client_handlers(dp)
create_resume.register_create_resume_handlers(dp)
executor.start_polling(dp, skip_updates=True)
