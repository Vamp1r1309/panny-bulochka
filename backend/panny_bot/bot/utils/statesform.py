from aiogram.fsm.state import StatesGroup, State


class StateForm(StatesGroup):
    GET_NAME = State()
    GET_YEAR = State()
    GET_PHONE = State()