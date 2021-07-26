from init import dp
from aiogram import types

from keyboards.interface_keyboards import get_filters_keyboard
from states.states import States

state = States.filters

import filters
from const import LIMIT_ODD


@dp.callback_query_handler(text="min_odd_dec", state=state)
async def min_odd_dec(query: types.CallbackQuery):
    if filters.min_odd - filters.step >= 0:
        filters.min_odd = filters.min_odd - filters.step
        await query.message.edit_reply_markup(reply_markup=get_filters_keyboard())


@dp.callback_query_handler(text="min_odd_inc", state=state)
async def min_odd_inc(query: types.CallbackQuery):
    if filters.min_odd + filters.step < filters.max_odd:
        filters.min_odd = filters.min_odd + filters.step
        await query.message.edit_reply_markup(reply_markup=get_filters_keyboard())


@dp.callback_query_handler(text="max_odd_dec", state=state)
async def max_odd_dec(query: types.CallbackQuery):
    if filters.max_odd - filters.step > filters.min_odd:
        filters.max_odd = filters.max_odd - filters.step
        await query.message.edit_reply_markup(reply_markup=get_filters_keyboard())


@dp.callback_query_handler(text="max_odd_inc", state=state)
async def max_odd_inc(query: types.CallbackQuery):
    if filters.max_odd + filters.step <= LIMIT_ODD:
        filters.max_odd = filters.max_odd + filters.step
        await query.message.edit_reply_markup(reply_markup=get_filters_keyboard())
