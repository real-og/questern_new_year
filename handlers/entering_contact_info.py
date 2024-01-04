from loader import dp, CODE, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
from states import State
import keyboards as kb


@dp.message_handler(state=State.entering_media)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text in [texts.telegram_btn, texts.whatsapp_btn]:
        await message.answer(texts.enter_phone, reply_markup=kb.phone_keyboard)
        await State.entering_phone.set()
    else:
        await message.answer(texts.use_kb, reply_markup=kb.choose_media_kb)




@dp.message_handler(content_types=types.ContentType.CONTACT, state=State.entering_phone)
async def set_phone_handler(message: types.Message, state: FSMContext):
    phone = message.contact.phone_number
    await message.answer(texts.finish1)
    await message.answer(texts.finish2)
    await message.answer(texts.finish3)
    await State.ended.set()


@dp.message_handler(state=State.entering_phone)
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer(texts.press_share_phone, reply_markup=kb.phone_keyboard)
