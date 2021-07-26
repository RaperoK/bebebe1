from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import filters
from const import VOL_RANGE, ODD_RANGE


def range_buttons(dec_callback, value, inc_callback):
    return [
        InlineKeyboardButton("➖", callback_data=dec_callback),
        InlineKeyboardButton(f"{value}", callback_data="empty"),
        InlineKeyboardButton("➕", callback_data=inc_callback)
    ]


def get_state_buttons(live_only, prematch_only):
    return [
        InlineKeyboardButton(f"Онлайн {'✔' if live_only else ' '}", callback_data="live_only"),
        InlineKeyboardButton(f"Предстоящие {'✔' if prematch_only else ' '}", callback_data="prematch_only"),
        InlineKeyboardButton(f"️Все {'✔' if not live_only and not prematch_only else ' '}", callback_data="all")
    ]


def get_filters_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            range_buttons("step_dec", f"✖️{filters.step}", "step_inc"),
            range_buttons("min_vol_dec", VOL_RANGE(filters.min_vol), "min_vol_inc"),
            range_buttons("max_vol_dec", VOL_RANGE(filters.max_vol), "max_vol_inc"),
            range_buttons("min_percent_dec", filters.min_percent, "min_percent_inc"),
            range_buttons("max_percent_dec", filters.max_percent, "max_percent_inc"),
            range_buttons("min_odd_dec", ODD_RANGE(filters.min_odd), "min_odd_inc"),
            range_buttons("max_odd_dec", ODD_RANGE(filters.max_odd), "max_odd_inc"),
            get_state_buttons(filters.live_only, filters.prematch_only),
            range_buttons("min_time_1_dec", filters.min_time_1, "min_time_1_inc"),
            range_buttons("max_time_1_dec", filters.max_time_1, "max_time_1_inc"),
            range_buttons("min_time_1_dec", filters.min_time_1, "min_time_1_inc"),
            range_buttons("max_time_1_dec", filters.max_time_1, "max_time_1_inc"),
            [InlineKeyboardButton("Сохранить", callback_data="save_filters")]
        ]
    )
