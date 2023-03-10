from aiogram import Bot, Dispatcher, executor, types
import os
import random
from keyboards import keyboard,inline_keyboard, inline_keyboard_counter, inline_keyboard_random_choice

HELP = """
Привет! Вот мой список команд!
<b>/help</b> - <i>ты здесь находишься</i>
<b>/start</b> - <i>открывать клавиатуру для работы со мной</i>
<b>/vote</b> - <i>проголосовать за то понравилась ли тебе картинка, которую я отправлю</i>
<b>/war</b> - <i>борьба между плюсами и минусами</i>
<b>/random</b> - <i>генератор случайных чисел от 0 до 1000000</i>"""

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)
users_id = []
number = 0

@dp.message_handler(commands='help')
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text=HELP, parse_mode='HTML')

@dp.message_handler(commands='start')
async def start_command(message: types.Message):
    await bot.send_message(chat_id= message.chat.id,text="We are ready to start",reply_markup=keyboard)

@dp.message_handler(commands='vote')
async def vote_command(message: types.Message):
    await bot.send_photo(chat_id = message.chat.id,photo='https://sun9-east.userapi.com/sun9-24/s/v1/ig2/4UUwat66YQQzXrgRx76gNTkDpw-xvwwkxlhPM2xQlnU2Q-kIw6BB1_dIsnGjLX53XLZjJNGk5htW59NBxnttywdY.jpg?size=700x619&quality=95&type=album',
                         caption="Rate the picture",reply_markup=inline_keyboard)
@dp.message_handler(commands='war')
async def war_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                         text=f'Счет: {number}', reply_markup=inline_keyboard_counter)
@dp.message_handler(commands='random')
async def generate_random_number(message: types.Message):
    global number
    await bot.send_photo(chat_id=message.chat.id, photo='https://sun9-73.userapi.com/impg/zZuOs7ow0oBT7sUkswaAcRFRd_eLIVCphxIRuQ/vMLpBWnJgAA.jpg?size=651x746&quality=96&sign=77a78ae42828ebbfca06796fddce4d8f&type=album',
                         caption=f'Число на данный момент равно = {number}', reply_markup=inline_keyboard_random_choice)

@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('counter'))
async def counter_changer(callback: types.CallbackQuery):
    global number
    if callback.data == 'counter_plus':
        number+=1
        await callback.message.edit_text(f'Счет: {number}',reply_markup=inline_keyboard_counter)
    else:
        number -= 1
        await callback.message.edit_text(f'Счет: {number}',reply_markup=inline_keyboard_counter)
@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('rdm'))
async def random_command(callback: types.CallbackQuery):
    if callback.data == 'rdm_generate':
        number = random.randint(0,1000000)
        await callback.message.edit_caption(caption=f'Число на данный момент равно = {number}',reply_markup=inline_keyboard_random_choice)
    else:
        await callback.message.delete()
@dp.callback_query_handler()
async def like_or_dislike_command(callback: types.CallbackQuery):
    if users_id.count(callback.from_user.id)==0:
        if callback.data == 'like':
             await callback.message.answer(text="You like it boobie")
        else:
            await callback.message.answer(text="You don't like boobie")
        users_id.append(callback.from_user.id)
        print(callback.from_user.id)
    else:
        await callback.message.answer('You have already voted')

executor.start_polling(dp, skip_updates=True)
