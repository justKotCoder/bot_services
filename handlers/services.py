from aiogram import types
from aiogram.dispatcher import FSMContext, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from database.db import add_service, get_services, update_service, delete_service

class Form(StatesGroup):
    service_name = State()
    service_description = State()
    service_price = State()
    edit_service_name = State()
    edit_service_description = State()
    edit_service_price = State()
    edit_service_price_final = State()
    delete_service = State()

async def cmd_add(message: types.Message):
    await Form.service_name.set()
    await message.reply("Введите название услуги:")

async def process_service_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['service_name'] = message.text
        data['user_id'] = message.from_user.id
    await Form.next()
    await message.reply("Введите описание услуги:")

async def process_service_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['service_description'] = message.text
    await Form.next()
    await message.reply("Введите цену услуги:")

async def process_service_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['service_price'] = message.text
        add_service(data['user_id'], data['service_name'], data['service_description'], data['service_price'])
    await state.finish()
    await message.reply("Услуга успешно добавлена и ожидает утверждения.")

async def cmd_list(message: types.Message):
    user_id = message.from_user.id
    services = get_services(user_id)
    if services:
        response = "\n\n".join([
            f"Название: {name}\nОписание: {description}\nЦена: {price}\nСтатус: {'Утверждено' if approved == 1 else 'Ожидает утверждения' if approved is None else 'Отклонено'}"
            for name, description, price, approved in services])
    else:
        response = "Список услуг пуст."
    await message.reply(response)

def register_handlers_services(dp: Dispatcher):
    dp.register_message_handler(cmd_add, commands='add')
    dp.register_message_handler(process_service_name, state=Form.service_name)
    dp.register_message_handler(process_service_description, state=Form.service_description)
    dp.register_message_handler(process_service_price, state=Form.service_price)
    dp.register_message_handler(cmd_list, commands='list')
