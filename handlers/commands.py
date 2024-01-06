from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
from states import State
import keyboards as kb
from aiotable import append_user


def extract_unique_code(text):
    return text.split()[1] if len(text.split()) > 1 else None


@dp.message_handler(commands=['start'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    invite_code = extract_unique_code(message.text)
    with open('images/lady.jpg', 'rb') as photo:
            await message.answer_photo(photo)
    await message.answer(texts.hello)
    await message.answer(texts.ask_name)
    await State.entering_name.set()
    await append_user(str(invite_code), message.from_id, message.from_user.username, message.from_user.first_name)
    

@dp.message_handler(commands=['help'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer(texts.help_message)