from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

initial_choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Спикер", callback_data="speaker")
        ],
        [
            InlineKeyboardButton(text="Журналист", callback_data="journalist")
        ]
    ]
)

yes_no = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Все верно", callback_data="affirmative"),
            InlineKeyboardButton(text="Ввести заново", callback_data="add_user")
        ]
    ]
)