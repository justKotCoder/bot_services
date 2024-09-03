from aiogram.dispatcher.filters.state import State, StatesGroup

class Form(StatesGroup):
    registration = State()
    service_name = State()
    service_description = State()
    service_price = State()
    edit_service_name = State()
    edit_service_description = State()
    edit_service_price = State()
    edit_service_price_final = State()
    delete_service = State()
    reject_reason = State()
