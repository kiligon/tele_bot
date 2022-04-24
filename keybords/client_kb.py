from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


b1 = KeyboardButton("/start")
b1 = KeyboardButton("/help")

kb_client = ReplyKeyboardMarkup()

kb_client.add(b1).add(b2)
