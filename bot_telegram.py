import logging
from aiogram import executor 
from create_bot import bot, dp

from handlers import client, admin



logging.basicConfig(level=logging.INFO)

async def on_startup():
    pass


client.register_handler_client(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
