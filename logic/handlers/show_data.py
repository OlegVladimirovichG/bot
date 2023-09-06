from aiogram import types


async def show_data(callback_query: types.CallbackQuery):
    message = callback_query.message
    with open('baza.xml', 'r', encoding='utf-8') as f:
        data = f.read()
    formatted_data = (
        data.replace('<name>', '')
        .replace('</name>', '')
        .replace('<x>', 'x=')
        .replace('</x>', '')
        .replace('<y>', 'y=')
        .replace('</y>', '')
        .replace('<h>', 'h=')
        .replace('</h>', '')
    )
    await message.reply(formatted_data)