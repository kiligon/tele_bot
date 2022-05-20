from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token="5290196270:AAHaI5Gm3Eo0ODtU2siyzVTrjMK-XZ1lLJ4")             
dp = Dispatcher(bot, storage=MemoryStorage())
