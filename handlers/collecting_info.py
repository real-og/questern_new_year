from loader import dp, CODE, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
from states import State
import keyboards as kb
import aiotable


@dp.message_handler(state=State.choosing_adult_childs)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text.strip() == texts.adult_quest_btn:
        await message.answer(texts.bd_corp_quest, reply_markup=kb.bd_corp_kb)
        await aiotable.update_cell(message.from_user.id, 8, 'Взрослый')

    elif message.text.strip() == texts.children_quest_btn:
        await message.answer(texts.ask_for_children_age, reply_markup=kb.children_age_kb)
        await aiotable.update_cell(message.from_user.id, 8, 'Ребенок')

    elif message.text.strip() in [texts.older_10_btn, texts.yonger_10_btn]:
        await message.answer(texts.bd_grad_quest, reply_markup=kb.bd_grad_kb)
        await aiotable.update_cell(message.from_user.id, 9, message.text.strip())

    elif message.text.strip() in [texts.bd_btn, texts.corp_btn, texts.graduating_quest_btn]:
        await message.answer(texts.boxes_rules1)
        await message.answer(texts.boxes_rules2, reply_markup=kb.boxes_kb)
        await State.collecting_gifts.set()
        await state.update_data(gifts=[])
        await aiotable.update_cell(message.from_user.id, 10, message.text.strip())
        await aiotable.update_cell(message.from_user.id, 7, 'Коробки')

    else:
        await message.answer(texts.use_kb, reply_markup=kb.age_type_kb)
    