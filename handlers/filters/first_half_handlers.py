from aiogram.dispatcher import FSMContext

import const
import filters
from init import dp
from aiogram import types

from keyboards.filters_keyboards import get_choice_keyboadrs, get_filters_keyboard
from states.states import States

state = States.Filters.first_half

@dp.callback_query_handler(text="first_half", state=States.Filters.set_filters)
async def first_half(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("Выберите голы:", reply_markup=get_choice_keyboadrs(const.FIRST_HALF))
    await call.message.delete()
    await States.Filters.first_half.set()

@dp.callback_query_handler(text="none", state=state)
async def none(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    await state.update_data(first_half=call.data)
    filters.first_half = const.FIRST_HALF['none']
    await call.message.delete()
    await States.Filters.set_filters.set()
    await call.message.answer("Выберите, какие фильтры вы хотите изменить:", reply_markup=get_filters_keyboard(filters))

@dp.callback_query_handler(text="goal0_5", state=state)
async def goal0_5(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    await state.update_data(first_half=call.data)
    filters.first_half = const.FIRST_HALF['goal0_5']
    await call.message.delete()
    await States.Filters.set_filters.set()
    await call.message.answer("Выберите, какие фильтры вы хотите изменить:", reply_markup=get_filters_keyboard(filters))

@dp.callback_query_handler(text="goal1_5", state=state)
async def goal1_5(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    await state.update_data(first_half=call.data)
    filters.first_half = const.FIRST_HALF['goal1_5']
    await call.message.delete()
    await States.Filters.set_filters.set()
    await call.message.answer("Выберите, какие фильтры вы хотите изменить:", reply_markup=get_filters_keyboard(filters))

@dp.callback_query_handler(text="goal2_5", state=state)
async def goal2_5(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    await state.update_data(first_half=call.data)
    filters.first_half = const.FIRST_HALF['goal2_5']
    await call.message.delete()
    await States.Filters.set_filters.set()
    await call.message.answer("Выберите, какие фильтры вы хотите изменить:", reply_markup=get_filters_keyboard(filters))
