from logic.config import bot, Secrets
import logging
from logic.utils.commands import set_commands


# Функции для вывода сообщений при запуске и остановке бота
async def on_startup(dp):
    await set_commands(bot)
    await bot.send_message(chat_id=Secrets.CHAT_ID, text='Bot started')
    logging.info('Bot started')


async def on_shutdown(dp):
    await bot.send_message(chat_id=Secrets.CHAT_ID, text='Bot stopped')
    logging.info('Bot stopped')
