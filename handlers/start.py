from aiogram import types
from aiogram.dispatcher import Dispatcher
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

async def cmd_start(message: types.Message):
    from database.db import get_user

    user = get_user(message.from_user.id)
    if user:
        await message.reply(
            "Вы уже зарегистрированы! Используйте команды /add, /edit, /delete для управления услугами.")
    else:
        await Form.registration.set()
        await message.reply("Добро пожаловать! Пожалуйста, зарегистрируйтесь, отправив свое имя.")

def register_handlers_start(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands='start')
