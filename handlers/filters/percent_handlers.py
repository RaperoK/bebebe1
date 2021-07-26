from init import dp
from aiogram import types

from keyboards.interface_keyboards import get_filters_keyboard
from states.states import States

state = States.filters

import filters
from const import LIMIT_PERCENT


@dp.callback_query_handler(text="min_percent_dec", state=state)
async def min_percent_dec(query: types.CallbackQuery):
    if filters.min_percent - filters.step >= 0:
        filters.min_percent = filters.min_percent - filters.step
        await query.message.edit_reply_markup(reply_markup=get_filters_keyboard())


@dp.callback_query_handler(text="min_percent_inc", state=state)
async def min_percent_inc(query: types.CallbackQuery):
    if filters.min_percent + filters.step > filters.max_percent:
        filters.min_percent = filters.min_percent + filters.step
        await query.message.edit_reply_markup(reply_markup=get_filters_keyboard())


@dp.callback_query_handler(text="max_percent_dec", state=state)
async def max_percent_dec(query: types.CallbackQuery):
    if filters.max_percent - filters.step > filters.min_percent:
        filters.max_percent = filters.max_percent - filters.step
        await query.message.edit_reply_markup(reply_markup=get_filters_keyboard())


@dp.callback_query_handler(text="max_percent_inc", state=state)
async def max_percent_inc(query: types.CallbackQuery):
    if filters.max_percent + filters.step <= LIMIT_PERCENT:
        filters.max_percent = filters.max_percent + filters.step
        await query.message.edit_reply_markup(reply_markup=get_filters_keyboard())
