from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


set_filters_keyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Изменить фильтры"),
            KeyboardButton(text="Запросить данные"),
        ]
    ], resize_keyboard=True)

def get_choice_keyboadrs(dict):
    buttons = []
    for key in dict.keys():
        buttons.append(InlineKeyboardButton(text=dict[key], callback_data=key))
    return InlineKeyboardMarkup(inline_keyboard=[buttons], resize_keyboard=True)


def get_filters_keyboard(filters):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=f"{filters.category}", callback_data="category")],
            [
                InlineKeyboardButton(text=f"От {filters.money['from']} €", callback_data="money_from"),
                InlineKeyboardButton(text=f"До {filters.money['to']} €", callback_data="money_to")
            ],
            [
                InlineKeyboardButton(text=f"От {filters.percent['from']} %", callback_data="percent_from"),
                InlineKeyboardButton(text=f"До {filters.percent['to']} %", callback_data="percent_to")
            ],
            [
                InlineKeyboardButton(text=f"От {filters.coeff['from']} кф", callback_data="coeff_from"),
                InlineKeyboardButton(text=f"До {filters.coeff['to']} кф", callback_data="coeff_to")
            ],
            [
                InlineKeyboardButton(text=f"изменение > {filters.coeff_diff} кф", callback_data="coeff_diff")
            ],
            [
                InlineKeyboardButton(text=f"От {filters.time_1['from']} мин I", callback_data="time_1_from"),
                InlineKeyboardButton(text=f"До {filters.time_1['to']} мин I", callback_data="time_1_to")
            ],
            [
                InlineKeyboardButton(text=f"От {filters.time_2['from']} мин II", callback_data="time_2_from"),
                InlineKeyboardButton(text=f"До {filters.time_2['to']} мин II", callback_data="time_2_to")
            ],
            [
                InlineKeyboardButton(text=f"Первый тайм Голы: {filters.first_half}", callback_data="first_half"),
            ],
            [
                InlineKeyboardButton(text="Сохранить", callback_data="save_filters"),
            ]
        ], resize_keyboard=True
    )