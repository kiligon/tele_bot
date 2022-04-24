from aiogram import types, Dispatcher
from create_bot import bot, dp
from keybords import select_language, menu
from dotenv import load_dotenv
from pathlib import Path
import os

from database import data_base
#import configparser

#global config
#print("config setup start")
#config = configparser.ConfigParser()
#config.read("locale.ini")
#locale = config.get("LOCALE", "language_ru") 
#config.read("{}.ini".format(locale))
#print("config setup finish")


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
        await message.answer("HELP_MESSAGE") 
    except:
        pass
#        load_dotenv()
#        ru_path = Path('./conf_lang')/'.ru'
#        load_dotenv(dotenv_path=ru_path)
#        await message.answer(config.get(section, "program_title")) 

async def catalog(message: types.Message):
    print(data_base.sql_test_out())
    await message.answer("<pre>"+data_base.sql_test_out()+"</pre>", parse_mode=types.ParseMode.HTML)

async def eng_select(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="English", show_alert=True)
#    config.read("locale.ini")
#    locale = config.get("LOCALE", "language_eng")
#    config.read("{}.ini".format(locale))

async def ru_select(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Русский", show_alert=True)
#    config.read("locale.ini")
#    locale = config.get("LOCALE", "language_ru")
#    config.read("{}.ini".format(locale))


def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start'])
    dp.register_message_handler(select_lang, commands=['select_language'])
    dp.register_callback_query_handler(eng_select, lambda c: c.data == 'en')
    dp.register_callback_query_handler(ru_select, lambda c: c.data == 'ru')
    dp.register_message_handler(help, commands=['help'])
    dp.register_message_handler(catalog, commands=['catalog'])
