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
userid = 0
chat_id = 463785826  # 457140523
exit = 0
logging.basicConfig(level=logging.INFO)


async def chat(userid):
    @dp.message_handler()
    async def chat1(msg2: types.Message):
        if msg2.from_user.id == chat_id:
            await bot.send_message(userid, "Admin" + ": " + msg2.text)
        else:
            await bot.send_message(chat_id, "User" + ": " + msg2.text)


@dp.message_handler(commands=["start"])
async def pars(msg: types.Message):
    await msg.delete()
    await bot.send_message(msg.from_user.id, "Добро пожаловать")


@dp.message_handler(commands=["send"])
async def pars(msg: types.Message):
    await bot.send_message(chat_id, "@" + msg.from_user.username + ": " + msg.text[6:] + '\n')
    userid = msg.from_user.id

    @dp.message_handler(commands=["back"])
    async def pars1(msg1: types.Message):
        await bot.send_message(userid, "Admin" + ": " + msg1.text[6:])
        await chat(userid)


# @dp.message_handler()
# async def pars(msg: types.Message):
#    await msg.answer(msg.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
