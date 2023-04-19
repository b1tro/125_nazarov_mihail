from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
bot = Bot(token="6003495233:AAFcZPPzAG_YvWJwq3I-CBbPEn4G4V_It78")
dp = Dispatcher(bot, storage=storage)