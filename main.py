import asyncio
import logging
from aiogram import Bot, Dispatcher, executor, types
from os import getenv
from sys import exit
from tokensuka import *


bot = Bot(token=bot_token)
userid = 0
dp = Dispatcher(bot)
chat_id = 463785826  # 457140523
logging.basicConfig(level=logging.INFO)


async def chat(userid):
    exit = 0
    if exit == 1:
        return 0
    @dp.message_handler()
    async def chat1(msg2: types.Message):
        if msg2.text == "stop":
            exit = 1
            return 0
        if msg2.from_user.id == chat_id:
            await bot.send_message(userid, "Admin" + ": " + msg2.text)
        else:
            await bot.send_message(chat_id, "User" + ": " + msg2.text)
11

@dp.message_handler(commands=["start"])
async def pars(msg: types.Message):
    await msg.delete()
    await bot.send_message(msg.from_user.id, "Добро пожаловать")


@dp.message_handler(commands=["send"])
async def pars(msg: types.Message):
    await bot.send_message(chat_id, "@" + msg.from_user.username + ": " + msg.text[6:] + '\n')

    @dp.message_handler(commands=["back"])
    async def pars1(msg1: types.Message):
        userid = msg.from_user.id
        await bot.send_message(userid, "Admin" + ": " + msg1.text[6:])
        await chat(userid)


# @dp.message_handler()
# async def pars(msg: types.Message):
#    await msg.answer(msg.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
