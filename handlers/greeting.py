from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
from states import State
import keyboards as kb
import aiotable

@dp.message_handler(state=State.starting)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == texts.start_btn:
        with open('images/lady.jpg', 'rb') as photo:
            await message.answer_photo(photo)
        await message.answer(texts.hello)
        await message.answer(texts.ask_name)
        await State.entering_name.set()
    else:
        await message.answer(texts.use_kb, reply_markup=kb.start_quest_kb)


@dp.message_handler(state=State.entering_name)
async def send_welcome(message: types.Message, state: FSMContext):
    name = message.text.strip()
    await message.answer(texts.generate_name_greeting(name), reply_markup=kb.come_in_kb)
    await State.after_name_entered.set()
    await aiotable.update_cell(message.from_user.id, 5, name)


@dp.message_handler(state=State.after_name_entered)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == texts.come_in_btn:
        with open('images/house.jpg', 'rb') as photo:
            await message.answer_photo(photo)
        await message.answer(texts.thats_my_house)
        await message.answer(texts.the_road_in_snow, reply_markup=kb.action_outside_kb)
        await State.entering_action_outside.set()
    else:
        await message.answer(texts.use_kb, reply_markup=kb.come_in_kb)


@dp.message_handler(state=State.entering_action_outside)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text.strip() == texts.lay_in_snow_btn:
        with open('images/lay_snow.mp4', 'rb') as video:
            await message.answer_video(video)
        await message.answer(texts.answer_lay_in_snow1)
        await message.answer(texts.answer_lay_in_snow2, reply_markup=kb.come_to_house_kb)
        await State.asking_for_go_inside.set()
    elif message.text.strip() == texts.take_shovel_btn:
        with open('images/shovel.mp4', 'rb') as video:
            await message.answer_video(video)
        await message.answer(texts.answer_take_shovel, reply_markup=kb.come_to_house_kb)
        await State.asking_for_go_inside.set()
    else:
        await message.answer(texts.use_kb, reply_markup=kb.action_outside_kb)
    
    