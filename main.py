from aiogram import executor
from handlers import dp
import asyncio
from datetime import datetime
import pytz
from scraper import requests

async def main_cicle():
    while True:
        await asyncio.sleep(30)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(main_cicle())
    executor.start_polling(dp, skip_updates=True)