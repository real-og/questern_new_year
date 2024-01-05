from loader import dp, CODE, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
from states import State
import keyboards as kb
import aiotable

@dp.message_handler(state=State.asking_for_go_inside)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == texts.come_to_house_btn:
        await message.answer(texts.ask_for_code1)
        await message.answer(texts.ask_for_code2, reply_markup=kb.find_code_kb)
        await State.offered_code.set()
        await aiotable.update_cell(message.from_user.id, 6, "Код")
    else:
        await message.answer(texts.use_kb, reply_markup=kb.come_to_house_kb)



@dp.message_handler(state=State.offered_code)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == texts.find_code_btn:
        await message.answer(texts.code_rules, reply_markup=kb.get_code_keyboard([]))
        await state.update_data(selected_digits=[]) 
        await State.entering_code.set()
        await aiotable.update_cell(message.from_user.id, 6, "Код")
    else:
        await message.answer(texts.use_kb, reply_markup=kb.find_code_kb)


@dp.callback_query_handler(state=State.entering_code)
async def send_series(callback: types.CallbackQuery, state: FSMContext):
    tapped_num = int(callback.data)
    data = await state.get_data()
    selected_numbers = data.get('selected_digits')

    position = len(selected_numbers)

    if CODE[position] == str(tapped_num):
        selected_numbers.append(tapped_num)
    else:
        selected_numbers = []

    try:
        await bot.edit_message_reply_markup(callback.message.chat.id,
                            callback.message.message_id,
                            reply_markup=kb.get_code_keyboard(selected_numbers))
    except:
        print('Фейл во время попытки изменить клавиатуру с кодом')
    if len(selected_numbers) == 4:
        selected_numbers = []
        await callback.message.answer(texts.success_code, reply_markup=kb.come_to_house_kb)
        await State.entering_home_after_code.set()

    await state.update_data(selected_digits=selected_numbers) 
    await bot.answer_callback_query(callback.id)

@dp.message_handler(state=State.entering_home_after_code)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == texts.come_to_house_btn:
        await message.answer(texts.choose_item_to_lit, reply_markup=kb.choose_item_to_lit_kb) 
        await State.choosing_item_to_lit.set()
        await aiotable.update_cell(message.from_user.id, 6, 'Загадка со спичками')
    else:
        await message.answer(texts.use_kb, reply_markup=kb.come_to_house_kb)