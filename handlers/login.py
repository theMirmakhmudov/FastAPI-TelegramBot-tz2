from aiogram import Router, types
from aiogram.filters import Command
from keyboards.verify import verify
from services.verify_code import generate_code

router = Router()

@router.message(Command("login"))
async def login_user(message: types.Message):
    verification_code = generate_code(user_id=message.from_user.id)
    await message.answer(text=f"<b>Your verification code: <code>{verification_code}</code></b>", reply_markup=verify)