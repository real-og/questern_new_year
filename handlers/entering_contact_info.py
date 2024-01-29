from loader import dp, CODE, bot, ADMIN_ID
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
from states import State
import keyboards as kb
import aiotable


@dp.message_handler(state=State.entering_media)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text in [texts.telegram_btn, texts.whatsapp_btn]:
        await message.answer(texts.enter_phone, reply_markup=kb.phone_keyboard)
        await State.entering_phone.set()
        await aiotable.update_cell(message.from_user.id, 13, message.text)
    else:
        await message.answer(texts.use_kb, reply_markup=kb.choose_media_kb)




@dp.message_handler(content_types=types.ContentType.CONTACT, state=State.entering_phone)
async def set_phone_handler(message: types.Message, state: FSMContext):
    phone = message.contact.phone_number
    await message.answer(texts.finish1)
    with open('images/bye.jpg', 'rb') as photo:
        await message.answer_photo(photo)
    await message.answer(texts.finish2)
    await message.answer(texts.finish3)
    await aiotable.update_cell(message.from_user.id, 11, phone)
    await State.ended.set()
    try:
        await bot.send_message(ADMIN_ID, f'{message.from_user.id} - {message.from_user.username} закончил снегурочку')
    except:
        pass
    


@dp.message_handler(state=State.entering_phone)
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer(texts.press_share_phone, reply_markup=kb.phone_keyboard)
