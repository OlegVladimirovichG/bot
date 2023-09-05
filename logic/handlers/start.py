import logging
from logic.utils.logger import log_request

from aiogram import types

key_request = {}


# Создаем обработчик для команды /start
async def start(message: types.Message):
    log_request(int, message, message.text)
    keyboard = types.InlineKeyboardMarkup()
    button_input = types.InlineKeyboardButton(text='ВВОД СЫРЫХ ГРО', callback_data='input')
    button_show = types.InlineKeyboardButton(text='ПОКАЗАТЬ ВСЕ СЫРЫЕ ДАННЫЕ', callback_data='show_baza')
    gro_button = types.InlineKeyboardButton(text='ЗАПРОС ГРО', callback_data='gro')
    stop_button = types.InlineKeyboardButton(text='STOP', callback_data='stop')
    help_button = types.InlineKeyboardButton(text='HELP', callback_data='help')
    about_button = types.InlineKeyboardButton(text='ABOUT', callback_data='about')
    keyboard.add(button_input, button_show)
    keyboard.add(gro_button)
    keyboard.add(stop_button, help_button, about_button)
    await message.reply(
        "Нажмите на кнопку 'Ввод гро' для ввода данных или 'Показать данные' для отображения содержимого baza.xml",
        reply_markup=keyboard)

    logging.info(f"User {message.from_user.id} started the bot")
