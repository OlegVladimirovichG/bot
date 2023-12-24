import logging

from aiogram import Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from logic.config import bot
from logic.handlers import events, gro, start, show_about, show_help, stop, input_data, plan, show_data
from logic.utils.states import MyState

# Создаем объекты Bot и Dispatcher и инициализируем их

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Регистрируем обработчики
dp.register_message_handler(start.start, commands=['start'])
dp.register_message_handler(gro.process_key)
dp.register_callback_query_handler(gro.get_value_by_key, lambda c: c.data == 'gro')
dp.register_callback_query_handler(show_help.show_help, lambda c: c.data == 'help')
dp.register_callback_query_handler(show_about.show_about, lambda c: c.data == 'about')
dp.register_callback_query_handler(stop.stop_key_request, lambda c: c.data == 'stop')
dp.register_message_handler(input_data.process_data, state=MyState.waiting_for_data)
dp.register_callback_query_handler(show_data.show_data, lambda c: c.data == 'show_baza')
dp.register_callback_query_handler(input_data.input_raw_data, lambda c: c.data == 'input')
dp.register_callback_query_handler(plan.plan_callback, lambda c: c.data == 'plan')
dp.register_callback_query_handler(plan.floor1_callback, lambda c: c.data == 'floor1')
dp.register_callback_query_handler(plan.floor2_callback, lambda c: c.data == 'floor2')
dp.register_callback_query_handler(plan.floor3_callback, lambda c: c.data == 'floor3')



# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Добавляем функции on_startup и on_shutdown в параметры executor.start_polling
if __name__ == '__main__':
    executor.start_polling(dp, on_startup=events.on_startup, on_shutdown=events.on_shutdown, skip_updates=True)

