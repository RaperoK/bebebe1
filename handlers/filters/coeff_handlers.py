from aiogram import types
from aiogram.dispatcher import FSMContext

import const
import filters
from init import dp
from keyboards.filters_keyboards import get_filters_keyboard
from states.states import States
from utils import try_parse_float

state = States.Filters.set_filters


@dp.callback_query_handler(text="coeff_from", state=state)
async def coeff_from(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("От:")
    await call.message.delete()
    await States.Filters.coeff_from.set()


@dp.callback_query_handler(text="coeff_to", state=state)
async def coeff_to(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("До:")
    await call.message.delete()
    await States.Filters.coeff_to.set()


@dp.message_handler(state=States.Filters.coeff_from)
async def coeff_from(message: types.Message):
    value = message.text
    if try_parse_float(value) and float(value) >= const.COEFF['min'] and float(value) < filters.coeff['to']:
        filters.coeff['from'] = float(value)
        await message.delete()
        await States.Filters.set_filters.set()
        await message.answer("Выберите, какие фильтры вы хотите изменить:", reply_markup=get_filters_keyboard(filters))
    else:
        await message.answer(f"Значение должно быть >= {const.COEFF['min']} и < {filters.coeff['to']}")

@dp.message_handler(state=States.Filters.coeff_to)
async def coeff_to(message: types.Message):
    value = message.text
    if try_parse_float(value) and float(value) > filters.coeff['from'] and float(value) <= const.COEFF['max']:
        filters.coeff['to'] = float(value)
        await message.delete()
        await States.Filters.set_filters.set()
        await message.answer("Выберите, какие фильтры вы хотите изменить:", reply_markup=get_filters_keyboard(filters))
    else:
        await message.answer(f"Значение должно быть > {filters.coeff['from']} и <= {const.COEFF['max']}")


@dp.callback_query_handler(text="coeff_diff", state=state)
async def coeff_diff(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("Изменение коэффициента:")
    await call.message.delete()
    await States.Filters.coeff_diff.set()

@dp.message_handler(state=States.Filters.coeff_diff)
async def coeff_to(message: types.Message):
    value = message.text
    if try_parse_float(value):
        filters.coeff_diff = float(value)
        await message.delete()
        await States.Filters.set_filters.set()
        await message.answer("Выберите, какие фильтры вы хотите изменить:", reply_markup=get_filters_keyboard(filters))
    else:
        await message.answer(f"Значение должно быть числом")