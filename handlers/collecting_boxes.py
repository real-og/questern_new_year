from loader import dp, CODE, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
from states import State
import keyboards as kb
import aiotable


@dp.message_handler(state=State.collecting_gifts)
async def send_welcome(message: types.Message, state: FSMContext):
    data = await state.get_data()
    gifts = data.get('gifts')
    if message.text in [texts.box1_btn, texts.box2_btn, texts.box3_btn,
                        texts.box4_btn, texts.box5_btn, texts.box6_btn,
                        texts.box7_btn, texts.box8_btn]:
        
        if message.text == texts.box2_btn:
            with open('images/ten_percent.jpg', 'rb') as photo:
                await message.answer_photo(photo)
            await message.answer(texts.gift1, reply_markup=kb.boxes_kb)

            if texts.box2_btn not in gifts:
                gifts.append(texts.box2_btn)
                if len(gifts) == 1:
                    await message.answer(texts.left_2, reply_markup=kb.boxes_kb)
                elif len(gifts) == 2:
                    await message.answer(texts.left_1, reply_markup=kb.boxes_kb)
                elif len(gifts) == 3:
                    await message.answer(texts.left_0, reply_markup=kb.boxes_kb)


        elif message.text == texts.box4_btn:
            with open('images/money.jpg', 'rb') as photo:
                await message.answer_photo(photo)
            await message.answer(texts.gift2, reply_markup=kb.boxes_kb)
            if texts.box4_btn not in gifts:
                gifts.append(texts.box4_btn)
                if len(gifts) == 1:
                    await message.answer(texts.left_2, reply_markup=kb.boxes_kb)
                elif len(gifts) == 2:
                    await message.answer(texts.left_1, reply_markup=kb.boxes_kb)
                elif len(gifts) == 3:
                    await message.answer(texts.left_0, reply_markup=kb.boxes_kb)

        elif message.text == texts.box5_btn:
            with open('images/video.jpg', 'rb') as photo:
                await message.answer_photo(photo)
            await message.answer(texts.gift3, reply_markup=kb.boxes_kb)
            if texts.box5_btn not in gifts:
                gifts.append(texts.box5_btn)
                if len(gifts) == 1:
                    await message.answer(texts.left_2, reply_markup=kb.boxes_kb)
                elif len(gifts) == 2:
                    await message.answer(texts.left_1, reply_markup=kb.boxes_kb)
                elif len(gifts) == 3:
                    await message.answer(texts.left_0, reply_markup=kb.boxes_kb)

        else:
            await message.answer(texts.empty_box, reply_markup=kb.boxes_kb)

    elif message.text == texts.choose_box_btn:
        if len(gifts) == 0:
            await message.answer(texts.no_finded, reply_markup=kb.boxes_kb)
        else:
            await message.answer(texts.choose_gift, reply_markup=kb.generate_gifts_kb(gifts))
            await State.choosing_gift.set()

    else:
        await message.answer(texts.use_kb, reply_markup=kb.boxes_kb)
    await state.update_data(gifts=gifts)



@dp.message_handler(state=State.choosing_gift)
async def send_welcome(message: types.Message, state: FSMContext):
    data = await state.get_data()
    gifts = data.get('gifts')
    if message.text in [texts.gift1_short, texts.gift2_short, texts.gift3_short,]:
        await message.answer(texts.choose_media, reply_markup=kb.choose_media_kb)
        await State.entering_media.set()
        await aiotable.update_cell(message.from_user.id, 11, message.text)
    else:
        await message.answer(texts.use_kb, reply_markup=kb.generate_gifts_kb(gifts))


