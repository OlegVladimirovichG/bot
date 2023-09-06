from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class MyState(StatesGroup):
    waiting_for_data = State()
