from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

contact_key = [[KeyboardButton(text="Share Contact", request_contact=True)]]

contact_keyboard = ReplyKeyboardMarkup(keyboard=contact_key, resize_keyboard=True, one_time_keyboard=True)