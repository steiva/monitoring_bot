from aiogram.dispatcher.filters.state import StatesGroup, State

class Speaker(StatesGroup):
    name = State()
    phone = State()
    email = State()

class Journalist(StatesGroup):
    name = State()
    company = State()
    category = State()
    deadline = State()