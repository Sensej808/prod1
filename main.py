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

KB = aiogram.types.ReplyKeyboardMarkup(resize_keyboard=True)
KB.row(aiogram.types.KeyboardButton("Связь"), aiogram.types.KeyboardButton("Связь"))

@dp.message_handler(commands=["help", "start"])
async def helpmes(message: types.Message):
    await message.answer("Привет! \n Команды бота:\t /help- \t /send-")


@dp.message_handler(commands=["send"])
async def sendToNahoy(msg2: types.Message):
    global userid
    userid = msg2.from_user.id
    await bot.send_message(userid, "Устанавливаю связь с администрацией...")
    await bot.send_message(S, "Ало, ну как там с чат ботом")
    global ban
    ban = 1


@dp.message_handler()
async def sendTOadmin(msg1: types.Message):
    global ban
    if ban == 1:
        if msg1.text == "stop":
            ban = 0
        elif msg1.from_user.id == S:
            await bot.send_message(userid, msg1.text)
        else:
            await bot.send_message(S, msg1.text)


# @dp.message_handler()
# async def pars(msg: types.Message):
#    await msg.answer(msg.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
