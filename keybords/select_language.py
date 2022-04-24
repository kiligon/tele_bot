from  aiogram.types import  InlineKeyboardMarkup, InlineKeyboardButton



rus_button = InlineKeyboardButton(text="Русский", callback_data="ru")
eng_button = InlineKeyboardButton(text="English", callback_data="en")


lang_select_kb  = InlineKeyboardMarkup()

lang_select_kb.add(rus_button,eng_button)

