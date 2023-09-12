from dataclasses import dataclass

from aiogram import Bot


@dataclass
class Secrets:
    BOT_TOKEN: str = "6678253357:AAGRLewX8Ck3R0g9A3iiNum7lHiFf_RNQfU"
    CHAT_ID: int = 1222943667


bot = Bot(token=Secrets.BOT_TOKEN)