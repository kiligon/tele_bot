from aiogram import types, Dispatcher
from create_bot import bot, dp
from keybords import select_language, menu, game_selector, pay
from pathlib import Path
import os

from req import title 
import configparser


from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class Order(StatesGroup):
    waiting_for_id = State()
    waiting_for_count = State()


global config

CART = ""

config = configparser.ConfigParser()
config.read("locale.ini")
locale = config.get("LOCALE", "language_ru") 
config.read("{}.ini".format(locale))


async def send_welcome(message: types.Message):
    await message.answer("Глвное Меню: \n"
    "• Cмена языка        /select_language\n"
    "• Каталог            /catalog\n"
    "• Помощь             /help\n"
    "• История транзакций /story", reply_markup=menu.kb_client)


async def select_lang(message: types.Message):
    await message.answer("""Здраствуйте, пожалуйста выберете язык\n Hello, please choose a language\n""", reply_markup = select_language.lang_select_kb)


async def help(message: types.Message):
    try:
        await message.answer(config.get("LANGUAGE","help_meassge"))
    except:
        pass

async def catalog(message: types.Message):
    await message.answer("<pre>"+title.get_games(config.get("LANGUAGE", "lang"))+"</pre>", parse_mode=types.ParseMode.HTML, reply_markup = game_selector.game_slector(config.get("LANGUAGE", "add")))

async def add_to_card_message(callback_query: types.CallbackQuery):
    await callback_query.message.answer(config.get("LANGUAGE","add_message"))
    await callback_query.answer()
    await Order.waiting_for_id.set()

async def game_id(message: types.Message, state: FSMContext):
    if not (message.text.isdigit() and len(str(message.text))==7):
        await message.answer(config.get("LANGUAGE","false_id"))
        return
    await state.update_data(game_id=message.text)
    await message.answer(config.get("LANGUAGE","count"))
    await Order.next()

async def game_count(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer(config.get("LANGUAGE","false_count"))
        return
    user_data = await state.get_data()
    global CART
    CART = title.add_to_cart(product_id=user_data["game_id"], product_cnt=int(message.text), cart_uid=CART)
    await message.answer(config.get("LANGUAGE","cart_commit"))
    await state.reset_state(with_data=False)


async def game_id_back(message: types.Message):
    message_text = message.text.replace("/", "")
    if not (message_text.isdigit() and len(str(message_text))==7):
        await message.answer(config.get("LANGUAGE","false_id"))
        return
    await state.update_data(game_id=message.text)
    await message.answer(config.get("LANGUAGE","count"))
    await Order.next()


async def eng_select(callback_query: types.CallbackQuery):
    await callback_query.answer("English") #bot.answer_callback_query(callback_query.id, text="English", show_alert=True)
    config.read("locale.ini")
    locale = config.get("LOCALE", "language_eng")
    config.read("{}.ini".format(locale)) 

async def ru_select(callback_query: types.CallbackQuery):
    await callback_query.answer("Русский") # bot.answer_callback_query(callback_query.id, text="Русский", show_alert=True)
    config.read("locale.ini")
    locale = config.get("LOCALE", "language_ru")
    config.read("{}.ini".format(locale))


async def cart(message: types.Message):
    await message.answer("<pre>"+title.print_cart(CART, config.get("LANGUAGE", "lang"))[1]+"</pre>", parse_mode=types.ParseMode.HTML, reply_markup=pay.pay_button(config.get("LANGUAGE", "pay")))

async def pay_message(callback_query: types.CallbackQuery):
    await callback_query.message.answer( title.payment(CART, config.get("LANGUAGE", "lang")) )

def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start'], state="*")
    dp.register_message_handler(select_lang, commands=['select_language'], state="*")
        
    dp.register_callback_query_handler(eng_select, lambda c: c.data == 'en')
    dp.register_callback_query_handler(ru_select, lambda c: c.data == 'ru')
    dp.register_callback_query_handler(add_to_card_message, lambda c: c.data == 'add_to_card')
    dp.register_callback_query_handler(pay_message, lambda c: c.data == 'pay')
    dp.register_message_handler(game_id, state=Order.waiting_for_id)
    dp.register_message_handler(game_id, state=Order.waiting_for_id, lambda message: message.text.startswith('/'))
    dp.register_message_handler(game_count, state=Order.waiting_for_count) 
    dp.register_message_handler(help, commands=['help'], state="*")
    dp.register_message_handler(catalog, commands=['catalog'], state="*")
    dp.register_message_handler(cart, commands=['cart'], state="*")
