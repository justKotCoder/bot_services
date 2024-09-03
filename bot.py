from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import API_TOKEN
from handlers import start, registration, services, admin, callback

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Регистрация хендлеров
start.register_handlers_start(dp)
registration.register_handlers_registration(dp)
services.register_handlers_services(dp)
admin.register_handlers_admin(dp)
callback.register_handlers_callback(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
