from  aiogram.types import  InlineKeyboardMarkup, InlineKeyboardButton


def pay_button(pay):
    button = InlineKeyboardButton(text=pay, callback_data="pay")
    pay_kb  = InlineKeyboardMarkup()
    return pay_kb.add(button)
