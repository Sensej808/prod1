import asyncio
import logging
from aiogram import Bot, Dispatcher, executor, types
from os import getenv
from sys import exit

bot_token = getenv("BOT_TOKEN")
if not bot_token:
    exit("Error: no token provided")

bot = Bot(token=bot_token)

dp = Dispatcher(bot)

chat_id = 463785826

logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=["send"])
async def pars(msg: types.Message):
    await bot.send_message(chat_id, "@" + msg.from_user.username + ": " + msg.text[6:] + '\n')

    @dp.message_handler(commands=["back"])
    async def pars1(msg1: types.Message):
        await bot.send_message(msg.from_user.id, "Admin" + ": " + msg1.text[6:])


#@dp.message_handler()
#async def pars(msg: types.Message):
#    await msg.answer(msg.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
