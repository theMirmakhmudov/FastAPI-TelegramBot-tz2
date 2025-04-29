from aiogram.fsm.state import State, StatesGroup

class Verify(StatesGroup):
    verification_code = State()