from loader import dp, CODE, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
from states import State
import keyboards as kb
import aiotable


@dp.message_handler(state=State.entering_gift_names)
async def send_welcome(message: types.Message, state: FSMContext):
    data = await state.get_data()
    known_gifts = data.get('known_gifts')
    user_input = message.text.lower()
    answers = texts.gifts_answers
    is_correct = False
    for ans in answers:
        if (ans in user_input) and (ans not in known_gifts):
            known_gifts.append(ans)
            is_correct = True

    if len(known_gifts) == 3:
        await message.answer(texts.success_gifts_name1)
        await message.answer(texts.success_gifts_name2)
        await message.answer(texts.success_gifts_name3)
        await message.answer(texts.ask_for_age_type, reply_markup=kb.age_type_kb)
        await State.choosing_adult_childs.set()
        await aiotable.update_cell(message.from_user.id, 6, 'Собирание информации')
        return
    
    if is_correct:
        await message.answer(texts.not_full_ans)
    else:
        await message.answer(texts.wrong_answer, reply_markup=kb.hint_kb)

    if message.text == texts.get_hint_btn:
        await message.answer(texts.hint_2_1, reply_markup=kb.hint_kb)
    await state.update_data(known_gifts=known_gifts)




