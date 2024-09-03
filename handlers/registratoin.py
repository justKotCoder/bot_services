from aiogram import types
from aiogram.dispatcher import FSMContext, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from database.db import add_user

class Form(StatesGroup):
    registration = State()

async def process_registration(message: types.Message, state: FSMContext):
    add_user(message.from_user.id, message.text)
    await state.finish()
    await message.reply(
        "Регистрация прошла успешно! Используйте команды \n /add  -  добавить услугу,\n /edit  -  редактировать услугу,\n /delete - удалить услугу,\n /services - просмотреть список услуг ")

def register_handlers_registration(dp: Dispatcher):
    dp.register_message_handler(process_registration, state=Form.registration)
