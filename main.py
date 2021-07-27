from aiogram import executor, types

import const
import filters
from handlers import dp
from init import bot
import asyncio

from scraper import requests
from scraper.requests import matches_url
from utils import percent, try_calculate, get_time


async def main_cicle():
    while True:
        await asyncio.sleep(30)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(main_cicle())
    executor.start_polling(dp, skip_updates=True)