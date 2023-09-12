# Обработчик нажатия на кнопку 'ПЛАН'
from aiogram import types


async def plan_callback(query: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    floor1_button = types.InlineKeyboardButton(text='Этаж1', callback_data='floor1')
    floor2_button = types.InlineKeyboardButton(text='Этаж2', callback_data='floor2')
    floor3_button = types.InlineKeyboardButton(text='Этаж3', callback_data='floor3')

    keyboard.add(floor1_button, floor2_button, floor3_button)

    await query.message.edit_reply_markup(reply_markup=keyboard)


# Создаем обработчик для команды /start
async def floor1_callback(query: types.CallbackQuery):
    # Обработка нажатия на кнопку 'Этаж1'
    await query.answer("Показываю информацию по этажу 1")
    photo1 = open('logic/utils/images/floor1/1.jpg', 'rb')
    photo2 = open('logic/utils/images/floor1/2.jpg', 'rb')
    photo3 = open('logic/utils/images/floor1/3.jpg', 'rb')
    photo4 = open('logic/utils/images/floor1/4.jpg', 'rb')

    await query.message.reply_photo(photo1)
    await query.message.reply_photo(photo2)
    await query.message.reply_photo(photo3)
    await query.message.reply_photo(photo4)

    photo1.close()
    photo2.close()
    photo3.close()
    photo4.close()


# Создаем обработчик для команды /start
async def floor2_callback(query: types.CallbackQuery):
    # Обработка нажатия на кнопку 'Этаж2'
    await query.answer("Показываю информацию по этажу 2")
    photo1 = open('logic/utils/images/floor2/1.jpg', 'rb')
    photo2 = open('logic/utils/images/floor2/2.jpg', 'rb')
    photo3 = open('logic/utils/images/floor2/3.jpg', 'rb')
    photo4 = open('logic/utils/images/floor2/4.jpg', 'rb')

    await query.message.reply_photo(photo1)
    await query.message.reply_photo(photo2)
    await query.message.reply_photo(photo3)
    await query.message.reply_photo(photo4)

    photo1.close()
    photo2.close()
    photo3.close()
    photo4.close()


# Создаем обработчик для команды /start
async def floor3_callback(query: types.CallbackQuery):
    # Обработка нажатия на кнопку 'Этаж3'
    await query.answer("Показываю информацию по этажу 3")
    # Обработка нажатия на кнопку 'Этаж2'
    await query.answer("Показываю информацию по этажу 2")
    photo1 = open('logic/utils/images/floor3/1.jpg', 'rb')
    photo2 = open('logic/utils/images/floor3/2.jpg', 'rb')
    photo3 = open('logic/utils/images/floor3/3.jpg', 'rb')
    photo4 = open('logic/utils/images/floor3/4.jpg', 'rb')

    await query.message.reply_photo(photo1)
    await query.message.reply_photo(photo2)
    await query.message.reply_photo(photo3)
    await query.message.reply_photo(photo4)

    photo1.close()
    photo2.close()
    photo3.close()
    photo4.close()
