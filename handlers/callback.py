from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

class Form(StatesGroup):
    edit_service_name = State()
    edit_service_description = State()
    edit_service_price = State()
    edit_service_price_final = State()

def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(callback_query_handler, lambda c: c.data and c.data.startswith('approve_'))
    dp.register_callback_query_handler(callback_query_handler, lambda c: c.data and c.data.startswith('reject_'))

async def callback_query_handler(callback_query):
    pass  # Здесь идет реализация функций callback
