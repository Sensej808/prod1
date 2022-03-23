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
KB.row(types.KeyboardButton("Связь"))

KB1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
KB1.row(types.KeyboardButton("Остановить"))

KBansw = types.InlineKeyboardMarkup(2)
KBansw.row(types.InlineKeyboardButton("Ответить", callback_data="ans"),
           types.InlineKeyboardButton("Отклонить", callback_data="decline"))


@dp.message_handler(commands=["help", "start"])
async def helpmes(message: types.Message):
    await message.answer("Привет! \n Команды бота:\t /help- ", reply_markup=KB)


async def sendtodaun(msg1, uid):
    global ban
    if msg1 == "Остановить":
        ban = 0
        return 0
    if uid == E:
        await bot.send_message(userid, msg1, reply_markup=KB1)
    else:
        await bot.send_message(E, msg1, reply_markup=KB1)


@dp.message_handler()
async def Head(msg1: types.Message):
    global ban
    global userid

    if ban == 1:
        await sendtodaun(msg1.text, msg1.from_user.id)
    if msg1.text == "Связь":
        userid = msg1.from_user.id
        await bot.send_message(userid, "Устанавливаю связь с администрацией...")
        await bot.send_message(E, "@" + msg1.from_user.username.__str__() + ":", reply_markup=KBansw)


@dp.callback_query_handler()
async def process_callback(query: types.CallbackQuery):
    data = query.data
    global ban
    if data == "ans":
        ban = 1
        await bot.send_message(userid, "Вам ответила администрация")

    elif data == "decline":
        await bot.send_message(userid, "Администрация отклонил ващ просьба бля")
    await query.answer()


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
