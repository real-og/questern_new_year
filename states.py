from aiogram.dispatcher.filters.state import StatesGroup, State


class State(StatesGroup):
    starting = State()
    entering_name = State()
    after_name_entered = State()
    entering_action_outside = State()
    asking_for_go_inside = State()
    entering_code = State()
    entering_home_after_code = State()
    choosing_item_to_lit = State()
    entering_lighters = State()
    entering_year = State()
    entering_gift_names = State()
    choosing_adult_childs = State()
    collecting_gifts = State()
    choosing_gift = State()
    entering_media = State()
    entering_phone = State()
    ended = State()
    offered_code = State()
    offered_look_gift = State()
    offered_rebus = State()