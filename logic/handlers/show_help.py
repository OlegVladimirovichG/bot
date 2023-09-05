import logging
from aiogram import types
from logic.config import bot


# Создаем обработчик для кнопки "HELP"
async def show_help(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)

    # Отправляем информацию о помощи
    await bot.send_message(callback_query.from_user.id,
                           "Это бот помощи. Введите команду /help, чтобы получить справку.")
    logging.info(f"User {callback_query.from_user.id} requested help")
