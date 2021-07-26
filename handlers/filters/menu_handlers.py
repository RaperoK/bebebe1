from init import dp, bot
from aiogram import types

from keyboards.interface_keyboards import get_filters_keyboard
from keyboards.navigation_keyboards import set_filters_keyboard
from states.states import States


@dp.message_handler(text="📝 Задать фильтры", state=States.filters)
async def set_filters(message: types.Message):
    await message.answer("Задайте фильтры для поиска матчей", reply_markup=get_filters_keyboard())



@dp.callback_query_handler(text="save_filters", state=States.filters)
async def save_filters(query: types.CallbackQuery):
    await query.message.edit_reply_markup(reply_markup=set_filters_keyboard)
