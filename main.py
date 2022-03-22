import asyncio
import logging
from aiogram import Bot, Dispatcher, executor, types
from os import getenv
from sys import exit
from tokensuka import *

bot = Bot(token=bot_token)
userid = 0
ban = 0
dp = Dispatcher(bot)
chat_id = 457140523  # 463785826
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=[help, start])
async def helpmes(message: types.Message):
    await message.answer("Привет! \n Команды бота:\n /help- \n /send-")


@dp.message_handler(commands=[send])
async def sendToAdmin(message: types.Message):
    await bot.send_message(S, "@" + msg.from_user.username + ": " + msg.text[6:])


# @dp.message_handler()
# async def pars(msg: types.Message):
#    await msg.answer(msg.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
