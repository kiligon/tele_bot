from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


start_button = KeyboardButton("/start")
select_lang_button = KeyboardButton("/select_language")
help_button = KeyboardButton("/help")
catalog_button = KeyboardButton("/catalog")
story_button = KeyboardButton("/story")

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(select_lang_button).add(catalog_button).add(help_button).add(story_button)
