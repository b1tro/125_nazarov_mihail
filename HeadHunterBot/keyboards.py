from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

#Keyboard
keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
 #Buttons
button_help = KeyboardButton('/help')
button_vote = KeyboardButton('/vote')
button_war = KeyboardButton('/war')
button_random = KeyboardButton('/random')
 #Settings
keyboard.add(button_help, button_vote, button_war,button_random)

#InlineKeyboards
inline_keyboard = InlineKeyboardMarkup(row_width=2)
inline_keyboard_counter = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='+',callback_data='counter_plus'), InlineKeyboardButton(text='-',callback_data='counter_minus')]
])
inline_keyboard_random_choice = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сгенерировать случайное число', callback_data='rdm_generate'), InlineKeyboardButton(text='Закрыть', callback_data='rdm_close')]
])
 #Buttons
button_like = InlineKeyboardButton('🥶',callback_data='like')
button_dislike = InlineKeyboardButton('🤬', callback_data='dislike')
 #Settings
inline_keyboard.add(button_like, button_dislike)
