from init import dp
from aiogram import types

from keyboards.interface_keyboards import get_filters_keyboard
from states.states import States

state = States.filters

import filters

@dp.callback_query_handler(text="step_dec", state=state)
async def step_dec(query: types.CallbackQuery):
    if filters.step != 0:
        filters.step = filters.step - 1
        await query.message.edit_reply_markup(reply_markup=get_filters_keyboard())


@dp.callback_query_handler(text="step_inc", state=state)
async def step_inc(query: types.CallbackQuery):
    filters.step = filters.step + 1
    await query.message.edit_reply_markup(reply_markup=get_filters_keyboard())