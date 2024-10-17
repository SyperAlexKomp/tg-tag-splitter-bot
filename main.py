import asyncio
import logging
import sys

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message

from helpers.config import config

dp = Dispatcher()


@dp.message(Command("start"))
async def start_command(message: Message) -> None:
    await message.reply(
        text="Send me a list of tags in the format that is output when generating a caption and I will give it to you in a form that can be used on websites"
    )


@dp.message()
async def tags_handler(message: Message) -> None:
    tags_text = message.text

    try:
        await message.reply(
            f'Space separated:'
            f'\n<pre>{" ".join(tags_text.replace(" ", "_").split(",_"))}</pre>'
            f'\n\nComma separated:'
            f'\n<pre>{", ".join(tags_text.replace(" ", "_").split(",_"))}</pre>'
        )
    except Exception as e:
        await message.reply(
            "Something went wrong"
        )



async def main():
    bot = Bot(
        token=config.BOT.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout, format="[%(asctime)s][%(levelname)s][%(funcName)s][%(module)s][%(lineno)d] - %(message)s")
    asyncio.run(main())
