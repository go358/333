from aiogram.fsm.state import StatesGroup, State

class BookingStates(StatesGroup):
    service = State()
    master = State()
    time = State()

class FeedbackStates(StatesGroup):
    rating = State()
    comment = State()

class ChatStates(StatesGroup):
    message = State()
