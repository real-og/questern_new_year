from loader import dp, CODE, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
from states import State
import keyboards as kb


@dp.message_handler(state=State.entering_year)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == '19' or message.text == '1919':
        await message.answer(texts.wa_19, reply_markup=kb.hint_kb)
    elif message.text == '91' or message.text == '1991':
        await message.answer(texts.wa_91, reply_markup=kb.hint_kb)
    elif message.text == '91' or message.text == '1991':
        await message.answer(texts.wa_91, reply_markup=kb.hint_kb)
    elif message.text == texts.get_hint_btn:
        await message.answer(texts.hint_1_1, reply_markup=kb.hint2_kb)
    elif message.text == texts.get_hint_2_btn:
        with open('images/riddle_clue.jpg', 'rb') as photo:
            await message.answer_photo(photo)
        await message.answer(texts.hint_1_2, reply_markup=kb.hint_kb)
    elif message.text == '61' or message.text == '1961':
        with open('images/riddle_ans.jpg', 'rb') as photo:
            await message.answer_photo(photo)
        await message.answer(texts.success_year1)
        await message.answer(texts.success_year2)
        await message.answer(texts.modern_card)
        await message.answer(texts.ask_for_gifts_name, reply_markup=kb.hint_kb)
        await state.update_data(known_gifts=[])
        await State.entering_gift_names.set()
    else:
        await message.answer(texts.wrong_answer, reply_markup=kb.hint_kb)