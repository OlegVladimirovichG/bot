import logging
from aiogram import Bot, Dispatcher, executor
from logic.config import Secrets
from logic.handlers import events, gro, start, show_about, show_help, stop, input_data
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

# Создаем объекты Bot и Dispatcher и инициализируем их
bot = Bot(token=Secrets.BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class MyState(StatesGroup):
    waiting_for_data = State()


# Регистрируем обработчики
dp.register_message_handler(start.start, commands=['start'])
dp.register_message_handler(gro.process_key)
dp.register_callback_query_handler(gro.get_value_by_key, lambda c: c.data == 'gro')
dp.register_callback_query_handler(show_help.show_help, lambda c: c.data == 'help')
dp.register_callback_query_handler(show_about.show_about, lambda c: c.data == 'about')
dp.register_callback_query_handler(stop.stop_key_request, lambda c: c.data == 'stop')
dp.register_message_handler(input_data.process_data)
dp.register_message_handler(input_data.input_gro, lambda c: c.data == 'input')
dp.register_message_handler(input_data.show_data, lambda c: c.data == 'show_baza')

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Добавляем функции on_startup и on_shutdown в параметры executor.start_polling
if __name__ == '__main__':
    executor.start_polling(dp, on_startup=events.on_startup, on_shutdown=events.on_shutdown, skip_updates=True)
