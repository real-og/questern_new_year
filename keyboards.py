from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import texts
from typing import List

start_quest_kb = ReplyKeyboardMarkup([[texts.start_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

come_in_kb = ReplyKeyboardMarkup([[texts.come_in_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

action_outside_kb = ReplyKeyboardMarkup([[texts.lay_in_snow_btn, texts.take_shovel_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

come_to_house_kb = ReplyKeyboardMarkup([[texts.come_to_house_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

def get_code_keyboard(selected: List[int]):
    kb = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton(text='✅' if 1 in selected else '1️⃣', callback_data='1')
    button_2 = InlineKeyboardButton(text='✅' if 2 in selected else '2️⃣', callback_data='2')
    button_3 = InlineKeyboardButton(text='✅' if 3 in selected else '3️⃣', callback_data='3')
    button_4 = InlineKeyboardButton(text='✅' if 4 in selected else '4️⃣', callback_data='4')

    kb.row(button_1, button_2, button_3, button_4)
    return kb

choose_item_to_lit_kb = ReplyKeyboardMarkup([[texts.candle_btn, texts.lamp_btn, texts.other_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

hint_kb = ReplyKeyboardMarkup([[texts.get_hint_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

hint2_kb = ReplyKeyboardMarkup([[texts.get_hint_2_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

age_type_kb = ReplyKeyboardMarkup([[texts.adult_quest_btn, texts.children_quest_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

bd_corp_kb = ReplyKeyboardMarkup([[texts.bd_btn, texts.corp_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

children_age_kb = ReplyKeyboardMarkup([[texts.older_10_btn, texts.yonger_10_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

bd_grad_kb = ReplyKeyboardMarkup([[texts.bd_btn, texts.graduating_quest_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

boxes_kb = ReplyKeyboardMarkup([[texts.box1_btn, texts.box2_btn,texts.box3_btn,texts.box4_btn,], 
                                [texts.box5_btn,texts.box6_btn,texts.box7_btn,texts.box8_btn,],
                                [texts.choose_box_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

gift_texts = {texts.box2_btn: texts.gift1_short,
              texts.box4_btn: texts.gift2_short,
              texts.box5_btn: texts.gift3_short,
              }

def generate_gifts_kb(gifts):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    for gift in gifts:
        kb.add(KeyboardButton(text=gift_texts[gift]))
    return kb


choose_media_kb = ReplyKeyboardMarkup([[texts.telegram_btn, texts.whatsapp_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

phone_keyboard = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
phone_keyboard.add(KeyboardButton(text=texts.phone_btn,
                                  request_contact=True,
                                 ))

find_code_kb = ReplyKeyboardMarkup([[texts.find_code_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

look_gift_kb = ReplyKeyboardMarkup([[texts.look_gift_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

read_letter_kb = ReplyKeyboardMarkup([[texts.read_letter_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)





