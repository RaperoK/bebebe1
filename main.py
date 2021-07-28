from aiogram import executor

import const
import filters
from init import db, bot
from handlers import dp
import asyncio
from database import database, commands
from scraper import requests
from scraper.requests import matches_url
from utils import get_time, try_parse_int, get_percents


async def print_msg(msg):
    users = await commands.select_all_users()
    for user in users:
        await bot.send_message(chat_id=user.id, text=msg)


async def show_matches(filters, save_percent):
    if filters.category == const.CATEGORY['all']:
        live_only = 'false'
        prematch_only = 'false'
    if filters.category == const.CATEGORY['live']:
        live_only = 'true'
        prematch_only = 'false'
    if filters.category == const.CATEGORY['prematch']:
        live_only = 'false'
        prematch_only = 'true'

    url = matches_url(live_only, prematch_only)
    matches = requests.get(url)
    if len(matches):
        #get percents
        old_percents = await commands.select_all_percents()
        if save_percent:
            await commands.delete_all_percents()
        #get scores
        live_matches_id = [str(match.get('e')) for match in matches if match.get('l') == 1]
        scores = {}
        if len(live_matches_id):
            scores = requests.get(requests.scores_url(live_matches_id))

        not_found = True

        for match in matches:
            print_str = match.get('m')
            all_filter = False
            #check time if live
            time_filter = True
            match_id = match.get('e')
            score = scores.get(str(match_id))
            # get old percent
            old_percent = []
            for p in old_percents:
                if p.id == match_id:
                    old_percent = p.percents
            if score and len(score) >= 2:
                time = score[0]
                time = time.split('+')[0]
                if try_parse_int(time):
                    time = int(time)
                    if not (filters.time_1['from'] <= time <= filters.time_1['to']
                    or filters.time_2['from'] <= time <= filters.time_2['to']):
                        time_filter = False
                    goals = score[1]
                    print_str += f' 🕑{time} ⚽{goals}:\n'
            else:
                time = get_time(match.get('ce'))
                print_str += f' 🕑{time}:\n'
            #check bets
            if time_filter:
                bents = match.get('i')
                percents = get_percents(list(map(lambda bent: bent[1], bents)))
                for i in range(len(bents)):
                    if len(bents[i]) >= 3:
                        name = bents[i][0]
                        money = bents[i][1]
                        coeff = bents[i][2]
                        bents_filter = True
                        if filters.money['from'] > money or money > filters.money['to']:
                            bents_filter = False
                        if filters.coeff['from'] > coeff or coeff > filters.coeff['to']:
                            bents_filter = False
                        bents_filter_2 = False
                        bents_filter_3 = False
                        if filters.percent['from'] <= percents[i] <= filters.percent['to']:
                            bents_filter_2 = True
                        if len(old_percent) == len(percents):
                            if filters.percent_change['from'] <= abs(old_percent[i] - percents[i]) <= filters.percent_change['to']:
                                bents_filter_2 = True
                                bents_filter_3 = True
                        print_str += f"{name}: 💰{money} 📈{coeff} 💯{percents[i]} {f'🔥{old_percent[i]}' if bents_filter_3 else ''}\n"
                        if bents_filter and bents_filter_2:
                            all_filter = True
            if all_filter:
                not_found = False
                if save_percent:
                    await commands.add_percent(match_id, percents)
                await asyncio.sleep(1)
                await print_msg(print_str)
        if not_found:
            await print_msg("По указанным фильтрам матчей не найдено")
    else:
        await print_msg("По указанным фильтрам матчей не найдено")


async def on_startup(dp):
    print("Подключаем БД")
    await database.on_startup(dp)
    print("Готово")

    print("Создаем таблицы")
    await db.gino.create_all()
    print("Готово")


async def main_cicle():
    while True:
        await asyncio.sleep(30)
        if not const.PAUSE and const.START:
            const.SAVE_PERCENT = not const.SAVE_PERCENT
            await show_matches(filters, const.SAVE_PERCENT)
            await print_msg("---------------------------------------------")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(main_cicle())
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)