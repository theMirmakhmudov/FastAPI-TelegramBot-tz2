import asyncio
from aiogram import Router, Bot, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from keyboards.number import contact_keyboard
from keyboards.verify import  ask_verify
from states.register import Register
from services.register import register_user

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext, bot: Bot):
    await message.answer(f"<b>Assalomu Aleykum, Xurmatli {message.from_user.mention_html()}</b>")
    del_mes = await message.answer("<b>Registration boshlandi ⚠️\nMalumotlar olinmoqda.....</b>")
    await state.set_state(Register.user_data)
    await asyncio.sleep(3)
    await bot.delete_message(chat_id=message.from_user.id,
                             message_id=del_mes.message_id)
    del_mes_2 = await message.answer("<b>Telefon raqamingizni yuboring: </b>", reply_markup=contact_keyboard)
    await state.update_data(user_id=message.from_user.id, full_name=message.from_user.full_name,
                            username=message.from_user.username, del_mes=del_mes_2.message_id)
    await state.set_state(Register.user_phone)
    await asyncio.sleep(5)


@router.message(Register.user_phone, F.contact)
async def receive_user_data(message: Message, state: FSMContext, bot:Bot):
    user_phone = message.contact.phone_number
    await state.update_data(phone_number=user_phone)
    await message.delete()
    data = await state.get_data()
    await state.clear()
    del_mes = data.get("del_mes")
    user_id = data.get("user_id")
    full_name = data.get("full_name")
    username = data.get("username")
    phone_number = data.get("phone_number")
    await bot.delete_message(chat_id=message.from_user.id, message_id=del_mes)
    response = register_user(user_id=user_id, fullname=full_name, username=username, phone_number=phone_number)
    if response is None:
        await message.answer("<b>❌ Server bilan bog'lanib bo'lmadi. Iltimos, keyinroq urinib ko'ring.</b>")
    elif response["status_code"] == 201:
        await message.answer("<b>✅ Siz muvaffaqiyatli ro'yhatdan o'tdingiz!</b>")
        await message.answer("<b>️️⚠️ Akkauntingizni verification qilishingiz kerak.</b>", reply_markup=ask_verify)
    elif response["status_code"] == 409:
        await message.answer("<b>⚠️ Siz allaqachon ro'yxatdan o'tgansiz.</b>")
    else:
        await message.answer(f"<b>❌ Noma'lum xatolik</b>")

