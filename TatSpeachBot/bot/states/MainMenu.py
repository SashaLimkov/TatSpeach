from aiogram.dispatcher.filters.state import StatesGroup, State


class MainMenuState(StatesGroup):
    MM = State()
    TAT_VOICE = State()
    RU_VOICE = State()
    TAT_TEXT = State()
    RU_TEXT = State()