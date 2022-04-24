import logging
from aiogram import executor 
from create_bot import bot, dp

from handlers import client, admin

from database import data_base


logging.basicConfig(level=logging.INFO)

async def on_startup():
    print("IN USE")

client.register_handler_client(dp)
print("Регнуло")


if __name__ == '__main__':
    print("main")
    executor.start_polling(dp, skip_updates=True)
    print("стартануло")
