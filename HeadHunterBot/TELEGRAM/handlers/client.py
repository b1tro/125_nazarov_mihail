from aiogram import Dispatcher,types
import bot_initialize
from TELEGRAM.keyboards.keyboards_instance.start_keyboard import start_kb


# @dp.message_handler(commands='start')
async def start_command(message: types.Message):
    await bot_initialize.bot.send_message(message.chat.id, 'Для начала работы создай резюме', reply_markup=start_kb)

def register_client_handlers(dp : Dispatcher):
    dp.register_message_handler(start_command,commands='start')