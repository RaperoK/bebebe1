from init import dp
from aiogram import types

from keyboards.interface_keyboards import get_filters_keyboard
from states.states import States

state = States.filters

from const import LIMIT_TIME
import filters


@dp.callback_query_handler(text="min_time_1_dec", state=state)
async def min_time_1_dec(query: types.CallbackQuery):
    if filters.min_time_1 - filters.step >= 0:
        filters.min_time_1 = filters.min_time_1 - filters.step
        await query.message.edit_reply_markup(reply_markup=get_filters_keyboard())


@dp.callback_query_handler(text="min_time_1_inc", state=state)
async def min_time_1_inc(query: types.CallbackQuery):
    if filters.min_time_1 + filters.step < filters.max_time_1:
        filters.min_time_1 = filters.min_time_1 + filters.step
        await query.message.edit_reply_markup(reply_markup=get_filters_keyboard())


@dp.callback_query_handler(text="max_time_1_dec", state=state)
async def max_time_1_dec(query: types.CallbackQuery):
    if filters.max_time_1 - filters.step > filters.min_time_1:
        filters.max_time_1 = filters.max_time_1 - filters.step
        await query.message.edit_reply_markup(reply_markup=get_filters_keyboard())


@dp.callback_query_handler(text="max_time_1_inc", state=state)
async def max_time_1_inc(query: types.CallbackQuery):
    if filters.max_time_1 + filters.step <= LIMIT_TIME:
        filters.max_time_1 = filters.max_time_1 + filters.step
        await query.message.edit_reply_markup(reply_markup=get_filters_keyboard())


@dp.callback_query_handler(text="min_time_2_dec", state=state)
async def min_time_2_dec(query: types.CallbackQuery):
    if filters.min_time_2 - filters.step >= 0:
        filters.min_time_2 = filters.min_time_2 - filters.step
        await query.message.edit_reply_markup(reply_markup=get_filters_keyboard())


@dp.callback_query_handler(text="min_time_2_inc", state=state)
async def min_time_2_inc(query: types.CallbackQuery):
    if filters.min_time_2 + filters.step < filters.max_time_2:
        filters.min_time_2 = filters.min_time_2 + filters.step
        await query.message.edit_reply_markup(reply_markup=get_filters_keyboard())


@dp.callback_query_handler(text="max_time_2_dec", state=state)
async def max_time_2_dec(query: types.CallbackQuery):
    if filters.max_time_2 - filters.step > filters.min_time_2:
        filters.max_time_2 = filters.max_time_2 - filters.step
        await query.message.edit_reply_markup(reply_markup=get_filters_keyboard())


@dp.callback_query_handler(text="max_time_2_inc", state=state)
async def max_time_2_inc(query: types.CallbackQuery):
    if filters.max_time_2 + filters.step <= LIMIT_TIME:
        filters.max_time_2 = filters.max_time_2 + filters.step
        await query.message.edit_reply_markup(reply_markup=get_filters_keyboard())