from dataclasses import dataclass

from aiogram import Bot


@dataclass
class Secrets:
    BOT_TOKEN: str = "6660964292:AAEHpmkk78OZAmm2hhbH7gIcF_DmDu2hCy0"
    CHAT_ID: int = 1222943667


bot = Bot(token=Secrets.BOT_TOKEN)
