from aiogram import types
from aiogram.dispatcher import FSMContext

# from main import MyState


async def input_gro(message: types.Message):
    await message.reply("Введите данные в формате 'название, x, y, h': ")
    # await MyState.waiting_for_data.set()

async def show_data(message: types.Message):
    with open('baza.xml', 'r') as f:
        data = f.read()
    formatted_data = data.replace('<name>', '').replace('</name>', '').replace('<x>', 'x=').replace('</x>', '').replace('<y>', 'y=').replace('</y>', '').replace('<h>', 'h=').replace('</h>', '')
    await message.reply(formatted_data)

async def process_data(message: types.Message, state: FSMContext):
    data = message.text.split(',')
    if len(data) == 4:
        name = data[0].strip()
        x = data[1].strip()
        y = data[2].strip()
        h = data[3].strip()

        with open('baza.xml', 'a') as f:
            f.write(f"**********************\n"
                    f" "
                    f"<name>{name}: \n"
                    f"              </name><x>{x}</x>  \n"
                    f"              <y>{y}</y>  \n"
                    f"              <h>{h}</h> \n")

        await message.reply("Данные успешно записаны")
    else:
        await message.reply("Некорректный формат данных")

    await state.finish()
