from loader import dp, CODE, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
from states import State
import keyboards as kb
import aiotable


@dp.message_handler(state=State.choosing_item_to_lit)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == texts.candle_btn:
        await message.answer(texts.candle_to_lit)
        await State.entering_lighters.set()
    elif message.text == texts.lamp_btn:
        await message.answer(texts.lamp_to_lit)
        await State.entering_lighters.set()
    elif message.text == texts.other_btn:
        await message.answer(texts.other_to_lit)
        await State.entering_lighters.set()
    else:
        await message.answer(texts.use_kb, reply_markup=kb.choose_item_to_lit_kb)


@dp.message_handler(state=State.entering_lighters)
async def send_welcome(message: types.Message, state: FSMContext):
    is_correct_answer = False
    for ans in texts.lightning_answers:
        if ans in message.text.lower():
            is_correct_answer = True

    if is_correct_answer:
        with open('images/lit.mp4', 'rb') as video:
            await message.answer_video(video)
        await message.answer(texts.right)
        await message.answer(texts.success_riddle, reply_markup=kb.look_gift_kb)
        await State.offered_look_gift.set()
        await aiotable.update_cell(message.from_user.id, 6, '1961')
    else:
        await message.answer(texts.wrong_answer)



@dp.message_handler(state=State.offered_look_gift)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == texts.look_gift_btn:
        await message.answer(texts.ask_for_year1)
        with open('images/riddle.jpg', 'rb') as f:
            await message.answer_photo(f)
        await message.answer(texts.ask_for_year2, reply_markup=kb.hint_kb)
        await State.entering_year.set()
    else:
        await message.answer(texts.use_kb, reply_markup=kb.look_gift_kb)
    