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

KB = types.ReplyKeyboardMarkup(resize_keyboard=True)
KB.row(types.KeyboardButton("Связь"), types.KeyboardButton("Связь"))


@dp.message_handler(commands=["help", "start"])
async def helpmes(message: types.Message):
    await message.answer("Привет! \n Команды бота:\t /help- \t /send-")


async def sendtodaun(msg1, uid):
    global ban
    if msg1 == "stop":
        ban = 0
        return 0
    elif uid == S:
        await bot.send_message(userid, msg1)
    else:
        await bot.send_message(S, msg1)


@dp.message_handler(commands=["send"])
async def sendToNahoy(msg2: types.Message):
    global userid
    global ban
    userid = msg2.from_user.id
    await bot.send_message(userid, "Устанавливаю связь с администрацией...")
    await bot.send_message(S, "Ало, ну как там с чат ботом")
    ban = 1


@dp.message_handler()
async def sendTOadmin(msg1: types.Message):
    global ban
    if ban == 1:
        uid = msg1.from_user.id
        await sendtodaun(msg1.text, uid)
    elif ban == 2:
        print(3)


# @dp.message_handler()
# async def pars(msg: types.Message):
#    await msg.answer(msg.text)

#1
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
