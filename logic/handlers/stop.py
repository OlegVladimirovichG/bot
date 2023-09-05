import logging
from aiogram import types
from logic.config import bot

key_request = {}


# Создаем обработчик для кнопки STOP
async def stop_key_request(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)

    user_id = callback_query.from_user.id

    # Проверяем состояние запроса ключа для этого пользователя
    if user_id in key_request:
        del key_request[user_id]
        await bot.send_message(user_id, "Запрос ключа остановлен")
        logging.info(f"User {user_id} stopped the key request")
    else:
        await bot.send_message(user_id, "Запрос ключа не активен")
        logging.warning(f"User {user_id} tried to stop the key request when it was not active")
