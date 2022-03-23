import asyncio
import logging
from aiogram import Bot, Dispatcher, executor, types
from os import getenv
from sys import exit
from tokensuka import *

bot = Bot(token=bot_token)
userid = 0
ban = 0
back = 0
dp = Dispatcher(bot)
chat_id = 457140523  # 463785826
logging.basicConfig(level=logging.INFO)

KB = types.ReplyKeyboardMarkup(resize_keyboard=True)
KB.row(types.KeyboardButton("Связь"), types.KeyboardButton("Связь"))
KB.row(types.KeyboardButton("Связь"))

KB1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
KB1.row(types.KeyboardButton("Остановить"))

KBansw = types.InlineKeyboardMarkup(2)
KBansw.row(types.InlineKeyboardButton("Ответить", callback_data="ans"),
           types.InlineKeyboardButton("Отклонить", callback_data="decline"))


@dp.message_handler(commands=["help", "start"])
async def helpmes(message: types.Message):
    await message.answer("Привет! \n Команды бота:\t /help- \t /send-")
    await message.answer("Привет! \n Команды бота:\t /help- ", reply_markup=KB)


async def sendtodaun(msg1, uid):
    global ban
    if msg1 == "Остановить":
        ban = 0
        return 0
    elif uid == S:
        await bot.send_message(userid, msg1, reply_markup=KB1)
    else:

        await bot.send_message(S, msg1)


@dp.message_handler()
async def sendTOadmin(msg1: types.Message):
    global userid
    global ban
    if msg1.text == "send" and ban != 1:
        userid = msg1.from_user.id
        await bot.send_message(userid, "Устанавливаю связь с администрацией...")
        await bot.send_message(S, "Ало, ну как там с чат ботом")
        ban = 1
    elif ban == 1:
        uid = msg1.from_user.id
        await sendtodaun(msg1.text, uid)
        # elif ban == 2:

        await bot.send_message(S, msg1, reply_markup=KB1)


@dp.message_handler()
async def Head(msg1: types.Message):
    global ban
    global back
    userid = msg1.from_user.id
    m = msg1.text
    if ban == 1:
        await bot.send_message(S, "@" + msg1.from_user.username.__str__() + ":" + msg1.text, reply_markup=KBansw)
        uid = msg1.from_user.id
        # if back == 1:
        # await sendtodaun(msg1.text, uid)
        if m == "Ответить" and msg1.from_user.id == S:
            back = 1
    if msg1.text == "Связь":
        ban = 1
        back = 0
        await bot.send_message(userid, "Устанавливаю связь с администрацией...")
        await bot.send_message(userid, "Напишите ваше сообщение: ")


@dp.callback_query_handler()
async def Ans(chosen_result: types.ChosenInlineResult):
    if chosen_result.query.data == "ans":
        await sendtodaun(msg1.text, chosen_result.from_user.id)
    elif chosen_result.query.data == "decline":
        global ban, back
        ban = 0
        back = 0


# @dp.message_handler()
# async def pars(msg: types.Message):
#    await msg.answer(msg.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

    '''
    @dp.message_handler(commands=["send"])
    async def sendToNahoy(msg2: types.Message):
    global userid
    global ban
    userid = msg2.from_user.id
    await bot.send_message(userid, "Устанавливаю связь с администрацией...")
    await bot.send_message(S, "Ало, ну как там с чат ботом")
    ban = 1
    '''
