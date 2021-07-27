from aiogram.dispatcher.filters import CommandStart

import const
import filters
from init import dp
from aiogram import types

from keyboards.filters_keyboards import get_filters_keyboard
from scraper.requests import matches_url
from states.states import States
from scraper import requests

from utils import percent, get_time, try_calculate


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message):
    await States.Filters.set_filters.set()
    await message.answer("Выберите, какие фильтры вы хотите изменить:", reply_markup=get_filters_keyboard(filters))


@dp.callback_query_handler(text="save_filters", state=States.Filters.set_filters)
async def save_filters(call: types.CallbackQuery):
    first_half = filters.first_half
    if filters.category == const.CATEGORY['all']:
        live_only = 'false'
        prematch_only = 'false'
    if filters.category == const.CATEGORY['live']:
        live_only = 'true'
        prematch_only = 'false'
    if filters.category == const.CATEGORY['prematch']:
        live_only = 'false'
        prematch_only = 'true'
    min_percent = filters.percent['from']
    max_percent = filters.percent['to']

    matches = []
    live_matches_id = []
    for match in requests.get(matches_url(first_half, live_only, prematch_only, min_percent, max_percent)):
        if match.get('l') == 1:
            matches.append(match)
            live_matches_id.append(str(match.get('e')))
    scores = requests.get(requests.scores_url(live_matches_id))

    not_found = True
    for match in matches:
        print_str = f"{match.get('m')}\n"
        bents = match.get('i')
        if bents:
            cash = list(map(lambda bent: bent[1], bents))
            cash_percent = percent(cash)
            money_filter = False
            coeff_filter = False
            coeff_diff_filter = True
            for i in range(len(bents)):
                money = bents[i][1]
                if filters.money['from'] <= money <= filters.money['to']:
                    money_filter = True
                coeff = bents[i][2]
                if filters.coeff['from'] <= coeff <= filters.coeff['to']:
                    coeff_filter = True
                coeff_prev = bents[i][3]
                print_str = print_str + \
                            f"{bents[i][0]}: " \
                            f"{money} - " \
                            f"{coeff} - " \
                            f"{cash_percent[i]}%\n"
            if match.get('l') == 1:
                score = scores.get(str(match.get('e')))
                time = score[0]
                time_int = try_calculate(time)
                time_filter = False
                if time_int is not None and (filters.time_1['from'] <= time_int <= filters.time_1['to'] or
                                             filters.time_2['from'] <= time_int <= filters.time_2['to']):
                    time_filter = True
                if score:
                    print_str = print_str + f"🕑 {time} ⚽ {score[1]}"
                else:
                    print_str = print_str + f"🕑 {get_time(match.get('ce'))}"
            if money_filter and coeff_filter and time_filter and coeff_diff_filter:
                await call.message.answer(print_str)
                not_found = False
    if not_found:
        await call.message.answer("По указанным фильтрам матчей не найдено")
