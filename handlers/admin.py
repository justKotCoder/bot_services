from aiogram import types
from aiogram.dispatcher import FSMContext, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.db import get_pending_services, approve_service, reject_service
from config import ADMIN_USER_ID

class Form(StatesGroup):
    reject_reason = State()

async def cmd_admin(message: types.Message):
    services = get_pending_services()
    if services:
        for service in services:
            service_id, service_name = service
            keyboard = InlineKeyboardMarkup(row_width=2)
            approve_button = InlineKeyboardButton(text="Утвердить", callback_data=f"approve_{service_id}")
            reject_button = InlineKeyboardButton(text="Отклонить", callback_data=f"reject_{service_id}")
            keyboard.add(approve_button, reject_button)
            await message.reply(f"Услуга: {service_name}", reply_markup=keyboard)
    else:
        await message.reply("Нет услуг для утверждения.")

async def process_approve(callback_query: types.CallbackQuery):
    service_id = int(callback_query.data.split('_')[1])
    approve_service(service_id)
    await callback_query.answer("Услуга утверждена.")

async def process_reject(callback_query: types.CallbackQuery):
    service_id = int(callback_query.data.split('_')[1])
    await Form.reject_reason.set()
    async with callback_query.bot.current_state(user=callback_query.from_user.id).proxy() as data:
        data['service_id'] = service_id
    await callback_query.message.reply("Введите причину отказа:")

async def process_reject_reason(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        service_id = data['service_id']
        reject_reason = message.text
        reject_service(service_id, reject_reason, message.from_user.id)
    await state.finish()
    await message.reply("Отказ отправлен клиенту.")

def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cmd_admin, commands='admin', user_id=ADMIN_USER_ID)
    dp.register_callback_query_handler(process_approve, lambda c: c.data.startswith('approve_'))
    dp.register_callback_query_handler(process_reject, lambda c: c.data.startswith('reject_'))
    dp.register_message_handler(process_reject_reason, state=Form.reject_reason, user_id=ADMIN_USER_ID)
