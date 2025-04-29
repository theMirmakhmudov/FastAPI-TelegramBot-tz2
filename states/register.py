from aiogram.fsm.state import State, StatesGroup

class Register(StatesGroup):
    user_data = State()
    user_phone = State()