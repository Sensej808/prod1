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
<<<<<<< Updated upstream
KB.row(types.KeyboardButton("Связь"), types.KeyboardButton("Связь"))
=======
KB.row(types.KeyboardButton("Связь"))

KB1 = types.ReplyKeyboardMarkup(row_width=1)
KB1.row(types.KeyboardButton("Остановить"))


def Chat(m: types.Message):
    print(1)
    global ban
    if ban == 1:
        if m.text == "stop":
            ban = 0
        elif m.from_user.id == S:
            await bot.send_message(userid, m.text, reply_markup=KB1)
        else:
            await bot.send_message(S, m.text, reply_markup=KB1)
>>>>>>> Stashed changes


@dp.message_handler(commands=["help", "start"])
async def helpmes(message: types.Message):
    await message.answer("Привет! \n Команды бота:\t /help- \t /send-", reply_markup=KB)


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
async def Head(msg1: types.Message):
    text = msg1.text
    global ban
<<<<<<< Updated upstream
    if ban == 1:
        uid = msg1.from_user.id
        await sendtodaun(msg1.text, uid)
=======
    if (text == "Связь"):
        ban = 1
        await Chat(msg1)


>>>>>>> Stashed changes


# @dp.message_handler()
# async def pars(msg: types.Message):
#    await msg.answer(msg.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
