from aiogram import Dispatcher
from handlers import start, verify_code, login

def register_all_handlers(dp: Dispatcher):
    dp.include_router(start.router)
    dp.include_router(verify_code.router)
    dp.include_router(login.router)