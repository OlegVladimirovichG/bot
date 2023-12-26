from dataclasses import dataclass

from aiogram import Bot


@dataclass
class Secrets:
    BOT_TOKEN: str = "****"
    CHAT_ID: int = ****


bot = Bot(token=Secrets.BOT_TOKEN)
