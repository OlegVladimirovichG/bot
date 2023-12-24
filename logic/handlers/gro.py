import logging
from aiogram import types
from logic.config import bot
import xml.etree.ElementTree as ET

key_request = {}


# Создаем обработчик для кнопки "ГРО"
async def get_value_by_key(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)

    user_id = callback_query.from_user.id

    # Проверяем состояние запроса ключа для этого пользователя
    if user_id in key_request:
        await bot.send_message(user_id, "Запрос ключа уже ожидается")
        logging.info(f"User {user_id} tried to make another key request while one was already pending")
    else:
        await bot.send_message(user_id, "Введите название пункта:")

        # Устанавливаем состояние ожидания ключа для пользователя
        key_request[user_id] = True
        logging.info(f"User {user_id} made a GRO query")


# Создаем обработчик для ввода ключа
async def process_key(message: types.Message):
    user_id = message.from_user.id

    key = message.text.strip().upper()

    # Загружаем данные из XML-файла
    tree = ET.parse('data.xml')
    root = tree.getroot()

    value = None
    # Поиск значения по ключу в XML
    for child in root:
        if child.attrib['key'] == key:
            value = child.text
            break

    if value is not None:
        await message.reply(f"Координаты ' {key} ': {value}")
        logging.info(f"User {user_id} successfully got the value for key '{key}'")
    else:
        await message.reply(f"Пункта ГРО '{key}' не найдено.")
        logging.warning(f"User {user_id} could not find the value for key '{key}'")

    # Удаляем состояние ожидания ключа для пользователя
    del key_request[user_id]
