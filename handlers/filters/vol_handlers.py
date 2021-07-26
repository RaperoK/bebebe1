from init import dp
from aiogram import types

from keyboards.interface_keyboards import get_filters_keyboard
from states.states import States

state = States.filters

from const import LIMIT_VOL
import filters

@dp.callback_query_handler(text="min_vol_dec", state=state)
async def min_vol_dec(query: types.CallbackQuery):
    if filters.min_vol - filters.step >= 0:
        filters.min_vol = filters.min_vol - filters.step
        if filters.min_vol == 11:
            filters.min_vol = 10
        await query.message.edit_reply_markup(reply_markup=get_filters_keyboard())


@dp.callback_query_handler(text="min_vol_inc", state=state)
async def min_vol_inc(query: types.CallbackQuery):
    if filters.min_vol + filters.step < filters.max_vol:
        filters.min_vol = filters.min_vol + filters.step
        if filters.min_vol == 10:
            filters.min_vol = 11
        await query.message.edit_reply_markup(reply_markup=get_filters_keyboard())


@dp.callback_query_handler(text="max_vol_dec", state=state)
async def max_vol_dec(query: types.CallbackQuery):
    if filters.max_vol - filters.step > filters.min_vol:
        filters.max_vol = filters.max_vol - filters.step
        if filters.max_vol == 11:
            filters.max_vol = 10
        if filters.max_vol == 102:
            filters.max_vol = 101
        await query.message.edit_reply_markup(reply_markup=get_filters_keyboard())


@dp.callback_query_handler(text="max_vol_inc", state=state)
async def max_vol_inc(query: types.CallbackQuery):
    if filters.max_vol + filters.step <= LIMIT_VOL:
        filters.max_vol = filters.max_vol + filters.step
        if filters.max_vol == 10:
            filters.max_vol = 11
        if filters.max_vol == 102:
            filters.max_vol = 103
        await query.message.edit_reply_markup(reply_markup=get_filters_keyboard())