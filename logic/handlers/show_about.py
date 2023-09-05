import logging
from aiogram import types
from logic.config import bot


# Создаем обработчик для кнопки "ABOUT"
async def show_about(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)

    # Отправляем информацию о боте
    await bot.send_message(callback_query.from_user.id, "Это бот для получения информации о боте.")
    logging.info(f"User {callback_query.from_user.id} requested about")
