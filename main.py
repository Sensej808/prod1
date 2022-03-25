import psycopg2
import asyncio
import logging
from aiogram import Bot, Dispatcher, executor, types
from os import getenv
from sys import exit
from tokensuka import *
from config import *

bot = Bot(token=bot_token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
num = 0
num1 = 0
temp = False
Admin = E
userid = 0
ban = 0

connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=db_name
)
connection.autocommit = True

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
        await bot.send_message(userid, "Диалог завершён", reply_markup=KB)
        await bot.send_message(Admin, "Диалог завершён")
        return 0
    if uid == Admin:
        await bot.send_message(userid, msg1, reply_markup=KB1)
    else:
        await bot.send_message(Admin, msg1, reply_markup=KB1)


@dp.message_handler()
async def Head(msg1: types.Message):
    global ban
    global userid
    global temp
    global num, num1
    if ban == 1:
        await sendtodaun(msg1.text, msg1.from_user.id)

    if temp:
        temp = not temp
        await bot.send_message(Admin, "@" + msg1.from_user.username.__str__() + ": " + msg1.text, reply_markup=KBansw)

    if msg1.text == "Связь" or temp:
        temp = not temp
        userid = msg1.from_user.id
        await bot.send_message(userid, "Устанавливаю связь с администрацией...")
        await bot.send_message(userid, "Напишите свой вопрос:")
    if msg1.text == "Предложка":
        userid = msg1.from_user.id
        await bot.send_message(userid, "Предлагай. Одним предложением.")
        ban = 2
    if ban == 2 and msg1.text != "Предложка":
        with connection.cursor() as cursor:
            cursor.execute(
                f"""INSERT INTO offers (num, read, id, name, offer) VALUES
                ({num}, 0, {msg1.from_user.id}, '{msg1.from_user.username.__str__()}', '{msg1.text}');"""
            )
            num += 1
            ban = 0
    if msg1.from_user.id == Admin and msg1.text == "ЧекПредл":
        num1 = num
        with connection.cursor() as cursor:
            # cursor.execute(
            #     f"""SELECT offer FROM offers WHERE read = {0} and num < {num};"""
            # )
            # print(cursor.fetchone())
            # while cursor.fetchone() != None:
            cursor.execute(
                f"""SELECT offer FROM offers WHERE num < {num};"""
            )
            await bot.send_message(Admin, cursor.fetchone())
            cursor.execute(
                """UPDATE offers SET read = 1;"""
            )
            num1 += 1


@dp.callback_query_handler()
async def process_callback(query: types.CallbackQuery):
    data = query.data
    global ban
    if data == "ans":
        ban = 1
        await bot.edit_message_text("Диалог с " + query.message.text, chat_id=query.message.chat.id,
                                    message_id=query.message.message_id)
        await bot.send_message(userid, "Вам ответила администрация", reply_markup=KB1)

    elif data == "decline":
        await bot.edit_message_text(query.message.text, chat_id=query.message.chat.id,
                                    message_id=query.message.message_id)
        await bot.send_message(userid, "Администрация отклонил ващ просьба бля")
    await query.answer()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
