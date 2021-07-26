from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

set_filters_keyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="📝 Задать фильтры")
        ],
        [
            KeyboardButton(text="📝 Запросить данные")
        ]
    ], resize_keyboard=True
)