from aiogram import types
from aiogram.dispatcher import FSMContext
from logic.utils.states import MyState


async def input_data(message: types.Message):
    await message.reply("Введите данные в формате 'название, x, y, h': ")
    await MyState.waiting_for_data.set()


async def process_data(message: types.Message, state: FSMContext):
    data = message.text.split(',')
    if len(data) == 4:
        name = data[0].strip()
        x = data[1].strip()
        y = data[2].strip()
        h = data[3].strip()

        with open('baza.xml', 'a', encoding='utf-8') as f:
            f.write(
                f"**********************\n"
                f"<name>{name}: \n"
                f"              </name><x>{x}</x>  \n"
                f"              <y>{y}</y>  \n"
                f"              <h>{h}</h> \n"
            )

        await message.reply("Данные успешно записаны")
    else:
        await message.reply("Некорректный формат данных")

    await state.finish()


async def input_raw_data(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Отправляем ответ пользователю, чтобы убрать "часики"
    await input_data(callback_query.message)  # Запускаем функцию input_data из модуля input_data
