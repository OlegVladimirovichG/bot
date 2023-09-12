from logic.utils.logger import log_request
from aiogram import types

key_request = {}


# Создаем обработчик для команды /start
async def start(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    button_input = types.InlineKeyboardButton(text='ВВОД СЫРЫХ ГРО', callback_data='input')
    button_show = types.InlineKeyboardButton(text='ПОКАЗАТЬ ВСЕ СЫРЫЕ ДАННЫЕ', callback_data='show_baza')
    gro_button = types.InlineKeyboardButton(text='ЗАПРОС ГРО', callback_data='gro')
    stop_button = types.InlineKeyboardButton(text='STOP', callback_data='stop')
    help_button = types.InlineKeyboardButton(text='HELP', callback_data='help')
    about_button = types.InlineKeyboardButton(text='ABOUT', callback_data='about')
    plan_button = types.InlineKeyboardButton(text='ПЛАН', callback_data='plan')

    keyboard.add(gro_button, plan_button)
    keyboard.add(button_input, button_show)
    keyboard.add(stop_button, help_button, about_button)

    await message.reply(
        "Нажмите на кнопку 'ЗАПРОС ГРО' и введи нахвание пункта, что бы получить координаты,"
        "'ВВОД СЫРЫХ ГРО' для ввода данных в файл baza.xml или "
        "'ПОКАЗАТЬ ВСЕ СЫРЫЕ ДАННЫЕ' для отображения содержимого baza.xml.",
        reply_markup=keyboard)

