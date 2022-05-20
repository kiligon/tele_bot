from  aiogram.types import  InlineKeyboardMarkup, InlineKeyboardButton


def game_slector(add):
    button = InlineKeyboardButton(text=add, callback_data="add_to_card")
    add_kb  = InlineKeyboardMarkup()
    return add_kb.add(button)
