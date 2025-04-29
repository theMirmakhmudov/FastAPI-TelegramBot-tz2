from aiogram import Router, F, types, Bot
from services.verify_code import generate_code
from keyboards.verify import verify
from states.verify import Verify
from aiogram.fsm.context import FSMContext
router = Router()

@router.callback_query(F.data == "verify")
async def check_code(call: types.CallbackQuery, state: FSMContext):
    verify_code = generate_code(call.from_user.id)
    del_mes1 = await call.message.edit_text(text=f"<b>Your verification code: <code>{verify_code}</code></b>", reply_markup=verify)
    del_mes2 = await call.message.answer("<b>Verification code kiriting: </b>")
    await state.set_state(Verify.verification_code)
    await state.update_data(verification_code=verify_code, del_mes1=del_mes1.message_id, del_mes2=del_mes2.message_id)

@router.message(Verify.verification_code)
async def verify_code(message: types.Message, state: FSMContext, bot:Bot):
    await state.update_data(user_code=message.text)
    data = await state.get_data()
    await state.clear()
    verification_code = data.get("verification_code")
    user_code = data.get("user_code")
    del_mes_1 = data.get("del_mes1")
    del_mes_2 = data.get("del_mes2")

    await bot.delete_messages(chat_id=message.from_user.id, message_ids=[del_mes_1, del_mes_2])
    await message.delete()

    if verification_code == user_code:
        await message.answer("<b>✅ User muvaffaqiyatli verificationdan o'tdi</b>")
    else:
        await message.answer("<b>❌ Nimadir xato ketdi</b>")

@router.callback_query(F.data == "verify_code")
async def login_code(call: types.CallbackQuery):
    verify_code = generate_code(call.from_user.id)
    await call.message.edit_text(text=f"<b>Your verification code: <code>{verify_code}</code></b>", reply_markup=verify)