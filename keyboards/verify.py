from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

ask_verify = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text='get verification code', callback_data='verify')]]
)
verify = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Generate Code", callback_data="verify_code")
        ]
    ]
)