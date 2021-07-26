from init import dp
from aiogram import types

from keyboards.interface_keyboards import get_filters_keyboard
from states.states import States

state = States.filters

import filters


@dp.callback_query_handler(text="live_only", state=state)
async def live_only(query: types.CallbackQuery):
    filters.live_only = True
    filters.prematch_only = False
    await query.message.edit_reply_markup(reply_markup=get_filters_keyboard())

@dp.callback_query_handler(text="prematch_only", state=state)
async def prematch_only(query: types.CallbackQuery):
    filters.live_only = False
    filters.prematch_only = True
    await query.message.edit_reply_markup(reply_markup=get_filters_keyboard())

@dp.callback_query_handler(text="all", state=state)
async def all(query: types.CallbackQuery):
    filters.live_only = False
    filters.prematch_only = False
    await query.message.edit_reply_markup(reply_markup=get_filters_keyboard())