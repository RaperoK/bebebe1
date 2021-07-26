import filters
from init import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.navigation_keyboards import set_filters_keyboard
from states.states import States
from scraper import requests
from utils import percent, get_time


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    await States.filters.set()
    await message.answer("👋 Добро пожаловать", reply_markup=set_filters_keyboard)


@dp.message_handler(text="📝 Запросить данные", state=States.filters)
async def spam_subscription(message: types.Message):
    matches = []
    live_matches_id = []
    print(requests.matches_url(filters))
    for match in requests.get(requests.matches_url(filters)):
        if match.get('l') == 1:
            matches.append(match)
            live_matches_id.append(str(match.get('e')))
    scores = requests.get(requests.scores_url(live_matches_id))

    for match in matches:
        print_str = f"{match.get('m')}\n"
        bents = match.get('i')
        if bents:
            cash = list(map(lambda bent: bent[1], bents))
            cash_percent = percent(cash)
            for i in range(len(bents)):
                print_str = print_str +\
                    f"{bents[i][0]}: " \
                    f"{bents[i][1]} - " \
                    f"{bents[i][2]} - " \
                    f"{cash_percent[i]}%\n"
            if match.get('l') == 1:
                score = scores.get(str(match.get('e')))
                if score:
                    print_str = print_str + f"🕑 {score[0]} ⚽ {score[1]}"
                else:
                    print_str = print_str + f"🕑 {get_time(match.get('ce'))}"
            await message.answer(print_str)